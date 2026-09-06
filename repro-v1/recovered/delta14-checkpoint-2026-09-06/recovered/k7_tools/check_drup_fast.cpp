// Independent text-DRUP checker for the Delta=14 certificate batch.
//
// This checker accepts RUP additions only. Deletion hints are ignored, which is
// sound because retaining already-derived clauses merely strengthens the
// working formula. It derives no information from the Python encoder.

#include <zlib.h>

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>

struct Clause {
    std::vector<int> lits;
    int w1 = -1;
    int w2 = -1;
};

class RUPDatabase {
  public:
    explicit RUPDatabase(int variables)
        : nvars_(variables), watches_(2 * (variables + 1) + 2),
          value_(variables + 1, 0) {}

    void add_clause(const std::vector<int>& input) {
        std::vector<int> clause;
        std::unordered_set<int> seen;
        clause.reserve(input.size());
        for (int lit : input) {
            if (seen.count(-lit)) return;  // tautology
            if (seen.insert(lit).second) clause.push_back(lit);
        }
        if (clause.empty()) {
            has_empty_ = true;
            clauses_.push_back(Clause{});
            return;
        }
        const int cid = static_cast<int>(clauses_.size());
        Clause stored;
        stored.lits = std::move(clause);
        stored.w1 = 0;
        stored.w2 = stored.lits.size() == 1 ? 0 : 1;
        clauses_.push_back(std::move(stored));
        if (clauses_[cid].lits.size() == 1) {
            units_.push_back(clauses_[cid].lits[0]);
        } else {
            watches_[lit_index(clauses_[cid].lits[0])].push_back(cid);
            watches_[lit_index(clauses_[cid].lits[1])].push_back(cid);
        }
    }

    bool is_rup(const std::vector<int>& clause) {
        if (has_empty_) return true;
        trail_.clear();
        touched_.clear();
        bool contradiction = false;
        for (int lit : units_) {
            if (!assign(lit)) {
                contradiction = true;
                break;
            }
        }
        if (!contradiction) {
            for (int lit : clause) {
                if (!assign(-lit)) {
                    contradiction = true;
                    break;
                }
            }
        }
        if (!contradiction) contradiction = !propagate();
        for (int var : touched_) value_[var] = 0;
        return contradiction;
    }

  private:
    int nvars_;
    std::vector<Clause> clauses_;
    std::vector<std::vector<int>> watches_;
    std::vector<int> units_;
    std::vector<int8_t> value_;
    std::vector<int> touched_;
    std::vector<int> trail_;
    bool has_empty_ = false;

    static int lit_index(int lit) {
        int var = std::abs(lit);
        return 2 * var + (lit < 0 ? 1 : 0);
    }

    int lit_value(int lit) const {
        int8_t v = value_[std::abs(lit)];
        return lit > 0 ? v : -v;
    }

    bool assign(int lit) {
        int var = std::abs(lit);
        int8_t wanted = lit > 0 ? 1 : -1;
        if (value_[var] == wanted) return true;
        if (value_[var] == -wanted) return false;
        value_[var] = wanted;
        touched_.push_back(var);
        trail_.push_back(lit);
        return true;
    }

    bool propagate() {
        std::size_t qhead = 0;
        while (qhead < trail_.size()) {
            int false_lit = -trail_[qhead++];
            auto& watched = watches_[lit_index(false_lit)];
            std::size_t i = 0;
            while (i < watched.size()) {
                int cid = watched[i];
                Clause& clause = clauses_[cid];
                int false_slot;
                int other_slot;
                if (clause.lits[clause.w1] == false_lit) {
                    false_slot = 1;
                    other_slot = clause.w2;
                } else if (clause.lits[clause.w2] == false_lit) {
                    false_slot = 2;
                    other_slot = clause.w1;
                } else {
                    throw std::runtime_error("stale watchlist entry");
                }

                int other = clause.lits[other_slot];
                if (lit_value(other) > 0) {
                    ++i;
                    continue;
                }

                int replacement = -1;
                for (int pos = 0; pos < static_cast<int>(clause.lits.size()); ++pos) {
                    if (pos != clause.w1 && pos != clause.w2 &&
                        lit_value(clause.lits[pos]) >= 0) {
                        replacement = pos;
                        break;
                    }
                }
                if (replacement >= 0) {
                    int new_lit = clause.lits[replacement];
                    if (false_slot == 1)
                        clause.w1 = replacement;
                    else
                        clause.w2 = replacement;
                    watched[i] = watched.back();
                    watched.pop_back();
                    watches_[lit_index(new_lit)].push_back(cid);
                    continue;
                }

                if (lit_value(other) < 0) return false;
                if (!assign(other)) return false;
                ++i;
            }
        }
        return true;
    }
};

static std::pair<int, std::vector<std::vector<int>>> read_cnf(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot open CNF: " + path);
    int nvars = -1;
    long declared = -1;
    std::vector<std::vector<int>> clauses;
    std::vector<int> pending;
    std::string line;
    while (std::getline(in, line)) {
        if (line.empty() || line[0] == 'c') continue;
        if (line[0] == 'p') {
            std::istringstream row(line);
            std::string p, kind;
            row >> p >> kind >> nvars >> declared;
            if (kind != "cnf") throw std::runtime_error("unsupported DIMACS kind");
            continue;
        }
        std::istringstream row(line);
        int lit;
        while (row >> lit) {
            if (lit == 0) {
                clauses.push_back(pending);
                pending.clear();
            } else {
                pending.push_back(lit);
            }
        }
    }
    if (!pending.empty()) throw std::runtime_error("unterminated DIMACS clause");
    if (nvars < 0 || static_cast<long>(clauses.size()) != declared)
        throw std::runtime_error("DIMACS header/count mismatch");
    return {nvars, std::move(clauses)};
}

static bool gz_getline(gzFile file, std::string& out) {
    out.clear();
    char buffer[65536];
    while (true) {
        char* got = gzgets(file, buffer, sizeof(buffer));
        if (!got) return !out.empty();
        out += buffer;
        if (!out.empty() && out.back() == '\n') {
            out.pop_back();
            return true;
        }
        if (gzeof(file)) return true;
    }
}

static std::vector<int> parse_proof_clause(const std::string& line, bool& deletion) {
    std::istringstream row(line);
    deletion = false;
    if (!line.empty() && line[0] == 'd') {
        char d;
        row >> d;
        deletion = true;
    }
    std::vector<int> clause;
    int lit;
    bool terminated = false;
    while (row >> lit) {
        if (lit == 0) {
            terminated = true;
            break;
        }
        clause.push_back(lit);
    }
    if (!terminated) throw std::runtime_error("proof line lacks trailing zero");
    return clause;
}

int main(int argc, char** argv) {
    try {
        if (argc != 3) {
            std::cerr << "usage: check_drup_fast FORMULA.cnf PROOF.drup.gz\n";
            return 2;
        }
        auto start = std::chrono::steady_clock::now();
        auto parsed = read_cnf(argv[1]);
        RUPDatabase db(parsed.first);
        for (const auto& clause : parsed.second) db.add_clause(clause);

        gzFile proof = gzopen(argv[2], "rb");
        if (!proof) throw std::runtime_error("cannot open proof");
        std::string line;
        long line_no = 0;
        long additions = 0;
        long deletions = 0;
        bool saw_empty = false;
        while (gz_getline(proof, line)) {
            ++line_no;
            if (line.empty() || line[0] == 'c') continue;
            bool deletion;
            std::vector<int> clause = parse_proof_clause(line, deletion);
            if (deletion) {
                ++deletions;
                continue;
            }
            ++additions;
            if (!db.is_rup(clause)) {
                gzclose(proof);
                std::cerr << "INVALID: non-RUP addition at proof line " << line_no << "\n";
                return 1;
            }
            db.add_clause(clause);
            if (clause.empty()) {
                saw_empty = true;
                break;
            }
        }
        int gz_status = gzclose(proof);
        if (gz_status != Z_OK) throw std::runtime_error("compressed proof checksum/read failure");
        if (!saw_empty) throw std::runtime_error("proof did not derive the empty clause");
        double seconds = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - start).count();
        std::cout << "VERIFIED UNSAT additions=" << additions
                  << " deletions_ignored=" << deletions
                  << " seconds=" << seconds << "\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "ERROR: " << error.what() << "\n";
        return 2;
    }
}
