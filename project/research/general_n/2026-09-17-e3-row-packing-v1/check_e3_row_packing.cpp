#include <algorithm>
#include <iostream>
using namespace std;

long long slack_scaled(int k, int rho, int p, int q) {
    long long W = 1LL*q*(p+q);
    int H = rho >= 5;
    int I4 = rho == 4;
    if (k <= 2) return 3*W - (-42 - 42*rho + 28*p + 48*q + 32*H);
    if (k <= 6) return W - (-19 - 14*rho + 11*p + 17*q + 3*H - q*I4);
    if (k <= 13) return 7*W - (-133 - 98*rho + 77*p + 122*q - 10*q*I4);
    if (k == 14) return 19*W - (-460 - 332*rho + 264*p + 361*q - 24*q*I4);
    if (k == 15) return 48*W - (-1121 - 835*rho + 652*p + 912*q - 27*q*I4);
    if (k <= 19) return 3*W - (-68 - 52*rho + 40*p + 57*q);
    return 4*W - (-109 - 71*rho + 60*p + 76*q);
}

bool legal(int k, int rho, int p, int q) {
    if (rho < 1 || rho > 20) return false;
    if (p < 0 || p > min(rho+2,22)) return false;
    if (q < 0 || q > min(20-rho,22-p)) return false;
    if (q > 0) {
        if (rho < 4) return false;
        if (rho == 4 && q > 20-k) return false;
        int g = max(0,p-rho+1);
        if (g == 1 && q > 3) return false;
        if ((g == 2 || g == 3) && q > 1) return false;
        if (g >= 4) return false;
    }
    return true;
}

int main() {
    long long checked = 0;
    for (int k=0;k<=20;k++) {
        for (int rho=1;rho<=20;rho++) {
            for (int p=0;p<=22;p++) {
                for (int q=0;q<=20;q++) {
                    if (!legal(k,rho,p,q)) continue;
                    checked++;
                    if (slack_scaled(k,rho,p,q) < 0) {
                        cerr << "FAIL " << k << " " << rho << " " << p << " " << q << "\n";
                        return 1;
                    }
                }
            }
        }
    }
    cout << "PASS_E3_ROW_PACKING_LOCAL_CPP\n";
    cout << "local_states_checked " << checked << "\n";
    return 0;
}
