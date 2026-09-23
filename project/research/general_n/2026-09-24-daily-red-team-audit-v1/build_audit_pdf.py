#!/usr/bin/env python3
from pathlib import Path
import subprocess

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "output/pdf/Erdos742_Daily_Red_Team_Audit_2026-09-24.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)
AUDIT_COMMIT = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()

navy = colors.HexColor("#17324D")
blue = colors.HexColor("#2E6F9E")
red = colors.HexColor("#9E2A2B")
amber = colors.HexColor("#A45A00")
grey = colors.HexColor("#5D6873")
pale = colors.HexColor("#EAF2F8")
pink = colors.HexColor("#FBECEC")
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Title2", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=21, leading=25, textColor=navy, spaceAfter=8))
styles.add(ParagraphStyle(name="Sub", parent=styles["Normal"], fontSize=9.2, leading=13, textColor=grey, spaceAfter=12))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=14, leading=17, textColor=navy, spaceBefore=10, spaceAfter=6))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=blue, spaceBefore=7, spaceAfter=4))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontSize=9.1, leading=13, spaceAfter=6))
styles.add(ParagraphStyle(name="Smallx", parent=styles["BodyText"], fontSize=7.1, leading=8.7, spaceAfter=1))
styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontSize=10, leading=14, leftIndent=8, rightIndent=8, spaceBefore=4, spaceAfter=8, textColor=navy, borderColor=blue, borderWidth=.6, borderPadding=7, backColor=pale))
styles.add(ParagraphStyle(name="Warning", parent=styles["BodyText"], fontSize=10, leading=14, leftIndent=8, rightIndent=8, spaceBefore=4, spaceAfter=8, textColor=red, borderColor=red, borderWidth=.8, borderPadding=7, backColor=pink))


def P(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def grid_table(rows, widths, header=True, font="Smallx"):
    table = Table([[P(str(x), font) for x in row] for row in rows], colWidths=widths, repeatRows=1 if header else 0)
    commands = [
        ("GRID", (0, 0), (-1, -1), .32, colors.HexColor("#AAB7C4")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if header:
        commands += [
            ("BACKGROUND", (0, 0), (-1, 0), navy),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F8FA")]),
        ]
    table.setStyle(TableStyle(commands))
    return table


def header_footer(canvas, doc):
    canvas.saveState()
    width, _ = A4
    canvas.setStrokeColor(colors.HexColor("#CAD5DF"))
    canvas.line(18 * mm, 14 * mm, width - 18 * mm, 14 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(grey)
    canvas.drawString(18 * mm, 9.5 * mm, "Independent Erdos #742 daily adversarial audit - 24 September 2026")
    canvas.drawRightString(width - 18 * mm, 9.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(OUT), pagesize=A4, rightMargin=17 * mm, leftMargin=17 * mm,
    topMargin=16 * mm, bottomMargin=19 * mm,
    title="Independent Erdos #742 Daily Red-Team Audit - 24 September 2026",
    author="Murty-Simon independent proof programme",
)
S = [
    P("Independent Erdos #742<br/>Daily adversarial audit", "Title2"),
    P("24 September 2026 | Audited predecessor <b>083dc162be599fe102274c4ce23f4f99ba5c7476</b><br/>Published audit commit <b>%s</b>" % AUDIT_COMMIT, "Sub"),
    P("<b>Disposition.</b> The candidate maximum-degree threshold remains <b>250/429</b>, with the general theorem and equality characterization open. The retained finite edge bound is <b>S&lt;=13</b>; equality remains supported only through <b>S&lt;=8</b>.", "Callout"),
    P("<b>Load-bearing nonreproduction.</b> A fresh run of the committed support-ten helper screen returned <b>32 solver timeouts and zero proved infeasibilities</b>, whereas the saved result claims 32 infeasibilities. The saved result is not declared false, but the attempted <b>S&lt;=14</b> promotion is frozen until it is independently reproduced or certificate-backed.", "Warning"),
    P("Executive findings", "H1x"),
]

summary_rows = [
    ["Item", "Audit disposition", "Evidence"],
    ["Maximum-degree strip", "250/429 retained as internal candidate", "No lower threshold; unresolved n/2&lt;Delta&lt;250n/429"],
    ["r=12 source stage", "Reproduced", "6,386 kernels; 32 survivors; shards [10,11,0,0,6,5,0,0]"],
    ["r=12 helper stage", "NONREPRODUCTION", "Same script SHA; 32/32 HiGHS timeouts at 180 seconds per row"],
    ["Finite edge range", "Retained through S&lt;=13", "S&lt;=14 frozen"],
    ["Equality", "Retained through S&lt;=8", "Balanced complete bipartite graphs remain mandatory controls"],
    ["n=18 row", "Bounded diagnostic only", "Abstract prefix through 39,250; (5,5,5) separately UNSAT"],
    ["Independence", "No hidden external-core use found", "No e+disj+X dependency in new files"],
]
S.append(grid_table(summary_rows, [40 * mm, 53 * mm, 74 * mm]))

S += [P("Material corrections", "H1x")]
corrections = [
    ("1", "Crossed-supplement injectivity is false", "Actual D2C controls contain collisions. Only demand-restricted Hall eligibility and congestion charging remain admissible."),
    ("2", "The endpoint cap was reversed", "Assigned witnesses lie in B=N(v), so only x_i&lt;=Delta follows. The claim x_i&lt;=n-Delta-1 is withdrawn."),
    ("3", "The old 42-survivor count was bookkeeping error", "Shard 0 was double-counted. Saved and fresh source-stage totals are 32."),
    ("4", "Support-ten closure did not reproduce", "The fresh result is UNKNOWN on every row. Timeout is neither feasibility nor infeasibility."),
    ("5", "Telemetry remained nonuniform", "Historical interval keys varied. The schema now requires start, stop, seconds and unit."),
]
for n, title, body in corrections:
    S.append(KeepTogether([P(f"<b>{n}. {title}</b>", "H2x"), P(body)]))

S += [PageBreak(), P("Mathematical evidence and trust boundary", "H1x")]
S += [
    P("Reproduced finite computations", "H2x"),
    P("The source-stage support-ten enumeration completed all 6,386 strict kernels and reproduced 32 distinct survivors with zero solver unknowns. Helper screens for supports six and seven classified 5/5 rows infeasible; supports eight and nine classified 44/44 infeasible. The support-ten helper screen alone failed to finish: all 32 rows reached HiGHS status 1/time limit."),
    P("The manifest checker passed only as a saved-file consistency check; it trusts the saved helper result and is not a solver replay. The precise fresh failure is preserved in <font name='Courier'>SUPPORT10_HELPER_REPLAY_FAILURE.json</font>."),
    P("Other bounded replays", "H2x"),
    P("<font name='Courier'>star_certificate_cover.py 8 6 5 dense8</font> tested 1,264 dense extensions, found 488 certificate-feasible and minimum star slack 40. <font name='Courier'>check_n18_555_d2c_z3.py</font> returned UNSAT. <font name='Courier'>validate_d2c_local_criterion.py</font> matched literal edge deletion on 457 graphs and 5,553 edges; the 82-edge diameter-stage model is not D2C and has 61 noncritical edges."),
    P("Structural notes retained", "H2x"),
    P("<font name='Courier'>HALL_ENVELOPE_EXACTNESS.md</font>, <font name='Courier'>ASSIGNED_WITNESS_OBSTRUCTION.md</font>, <font name='Courier'>STAR_CRITICALITY_SLACK.md</font> and <font name='Courier'>DEMAND_15_16_NORMAL_FORM.md</font> survived direct review at their stated interfaces. The demand-15/16 normal form is a credible finite-dimensional obstruction, not a theorem about all D2C graphs."),
    P("Open scope", "H2x"),
    P("The 250/429 implication remains internal candidate mathematics because its graph-to-profile spine is not externally verified. The n=18 scan is an abstract necessary-condition scan, not a graph count or threshold theorem. Bounded nonappearance proves no nonrealizability. No rigidity theorem near Delta=n/2 was completed, and odd balanced complete-bipartite equality examples lie inside the remaining strip."),
]

S += [P("Confidence movement", "H1x")]
confidence_rows = [
    ["Claim", "Before audit", "After audit"],
    ["r=12 source count", "42 claimed, count disputed", "32 reproduced; bookkeeping corrected"],
    ["r=12 helper exclusion", "Saved 32 infeasible", "Frozen: fresh replay 32 UNKNOWN"],
    ["S&lt;=14", "Attempted promotion", "Not retained"],
    ["S&lt;=13", "Retained", "Retained"],
    ["Crossed injectivity", "Proposed", "Refuted on actual D2C controls"],
    ["250/429", "Internal candidate", "Unchanged internal candidate"],
]
S.append(grid_table(confidence_rows, [47 * mm, 53 * mm, 67 * mm]))

S += [PageBreak(), P("Canonical launch and utilisation audit", "H1x"), P("Each scheduled trigger is a unique accounting identity. RAN is separated from duration compliance. Missing time is never inferred from commits, unit count, prose, configuration state or nominal schedule.")]
telemetry = [
    ["Trigger", "Start", "+5 / +10", "Verified", "Units", "Class"],
    ["01", "01:01:57", "late 27s / pass", "18m10s", "7", "SHORT"],
    ["02", "02:01:19", "pass / pass", "40m10s", "3", "COMPLIANT"],
    ["03", "03:02:45", "pass / pass", "40m02s", "5", "SHORT: report crossed 04"],
    ["04", "04:59:32", "no / no", "0", "0", "MISSED"],
    ["05", "UNVERIFIED", "no / no", "0 verified", "0", "UNVERIFIED"],
    ["06", "06:03:18", "pass / pass", "17m13s", "10", "SHORT"],
    ["07", "07:59:51", "no / no", "0", "0", "MISSED"],
    ["08", "08:58:34", "no / no", "0", "0", "MISSED"],
    ["09", "09:26:51", "late / pass", "7m13s LB", "3", "LATE / unfinalized"],
    ["10", "10:00:51", "pass / pass", "31m00s", "10", "SHORT"],
    ["11", "11:04:13", "late 1s / pass", "3m08s LB", "1", "UNVERIFIED"],
    ["12", "12:02:29", "pass / pass", "31m37s", "6", "SHORT"],
    ["13", "13:08:53", "late / pass", "1m07s LB", "2", "UNVERIFIED"],
    ["14", "14:00:30", "pass / pass", "41m28s", "5", "COMPLIANT"],
    ["15", "15:00:47", "pass / pass", "37m43s", "7", "SHORT"],
    ["16", "16:06:11", "late / pass", "0m50s LB", "1", "UNVERIFIED"],
    ["17", "17:07:58", "late / pass", "4m56s LB", "1", "UNVERIFIED"],
    ["18", "18:03:44", "late 35s / pass", "31m21s", "7", "SHORT"],
    ["19", "19:00:47", "pass / pass", "40m36s", "5", "COMPLIANT"],
    ["20", "20:01:26", "pass / pass", "41m00s", "5", "COMPLIANT"],
    ["21", "21:09:54", "late / pass", "12m30s LB", "3", "UNVERIFIED"],
    ["22", "22:01:42", "pass / pass", "32m05s", "4", "SHORT"],
    ["23", "23:04:21", "late / none", "0", "0", "MISSED"],
]
S.append(grid_table(telemetry, [14 * mm, 28 * mm, 34 * mm, 26 * mm, 14 * mm, 51 * mm]))

S += [PageBreak(), P("Utilisation aggregates and launch diagnosis", "H1x")]
aggregate_rows = [
    ["Measure", "Result"],
    ["Scheduled forward triggers", "23; separate audits 1; manual research 0; admin/configuration separate"],
    ["Canonical records", "23 after one audit-only reconciliation; 22 before audit"],
    ["Evidenced substantive research", "18 sessions; 85 substantive units"],
    ["Fully finalized records", "15, including three zero-research late deliveries"],
    ["Completed evidenced 40-minute sessions", "5: 02, 03, 14, 19, 20"],
    ["Canonical classes", "4 compliant; 8 short; 1 late/N-A; 4 missed; 6 unverified"],
    ["Durable STARTED by trigger+5", "10/23"],
    ["Checkpoint within 10 minutes of entry", "18/18 sessions with evidenced substantive research"],
    ["Fully finalized utilisation", "402m25s / 622m01s = 64.70% over evidenced finalized windows only"],
    ["All closed forward intervals", "432m09.31s lower bound; not whole-day utilisation"],
]
S.append(grid_table(aggregate_rows, [62 * mm, 105 * mm]))
S += [
    P("First three post-cutover triggers", "H2x"),
    P("<b>01:00:</b> research ran and checkpointed promptly, but durable STARTED was 27 seconds late and only 18m10s is verified; no focus credit. <b>02:00:</b> 40m10s, finalized and compliant; focus credit. <b>03:00:</b> 40m02s and focus credit, but the final report crossed the next trigger, so process compliance failed."),
    P("Lost-hour finding", "H2x"),
    P("The 03:00 report crossed the 04:00 trigger and 04:00 delivered no research. The overlap is evidenced, but it does not prove that a 42-second report overrun caused the later 58-minute launch delay. Cause is unknown. No other prior preservation segment is evidenced as displacing a next trigger."),
    P("Recovery state", "H2x"),
    P("The standalone task was observed enabled with the independent-#742 prompt; the retired chat-bound task and old health checker were paused. Two watchdogs recovered some starts but did not make launches or finalization reliable. Configuration, enabled state and last-run metadata are not execution evidence."),
    P("Focused-session gate", "H1x"),
    P("<b>Count: 6/24.</b> This is the original threshold-improvement session plus five complete evidenced 40-minute sessions. Short useful research is not relabelled as no work. The gate is not due. Its success condition has been met provisionally by the 250/429 threshold improvement, and the demand-15/16 normal form supplies a credible finite-dimensional obstruction. Recommendation: continue until the first audit after 24 credited sessions, subject to the stop criteria below.", "Callout"),
]

S += [PageBreak(), P("Prioritized next-hours programme", "H1x")]
priorities = [
    ("1", "Resolve the r=12 nonreproduction", "Produce independently checkable infeasibility certificates or reimplement all 32 support-ten helper systems with a second solver or encoding. Keep S&lt;=14 frozen until every row is decisively classified."),
    ("2", "Resume n=18 only as bounded validation", "Continue the stable-index scan from 39,251 and test the next distinct survivor in the staged exact D2C model. Do not equate row closure with strip closure."),
    ("3", "Return to graph-level demand 15/16", "Use source and supplement geometry to exclude or realize the remaining normal forms. Prioritize high-demand star overlap and demand-restricted collisions; unrestricted injectivity is forbidden."),
    ("4", "Protect equality", "Develop near-zero-demand rigidity with even and odd balanced complete-bipartite graphs as positive controls at every lemma. Equality remains supported only through S&lt;=8."),
    ("5", "Repair launch reliability", "Require one canonical writer, STARTED by +5, a checkpoint by +10, exact interval keys and finalization before hard close. Do not credit watchdog configuration as a launch."),
]
for n, title, body in priorities:
    S.append(KeepTogether([P(f"<b>{n}. {title}</b>", "H2x"), P(body)]))

S += [
    P("Stop and pivot criteria", "H1x"),
    P("Keep S&lt;=14 frozen until the timeout discrepancy is resolved by decisive reproducible evidence. Freeze 250/429 on any legal-selection bridge counterexample. Reject any equality lemma excluding K(floor(n/2),ceil(n/2)). If demand 15/16 remains only an abstract scan after 24 credited sessions, pivot to a direct graph-realizability theorem or abandon this route. At the first audit after 24 credits, decide continue or pivot from evidence, not sunk cost."),
    P("Deferred items", "H1x"),
    P("This audit did not independently reimplement the r=12 source or helper MILPs, exhaustively replay all 39,250 n=18 stable indices, or rerun the unchanged 250/429 scalar package. It reran the listed load-bearing checkers and exposed the support-ten timeout discrepancy. These deferred items remain explicit trust risks."),
    P("Key identifiers", "H1x"),
]
refs = [
    ["Purpose", "Identifier"],
    ["Previous audited baseline", "f2f951e538c297243b4dbb02140fc8f96df97f5b"],
    ["Audited predecessor", "083dc162be599fe102274c4ce23f4f99ba5c7476"],
    ["Published audit commit", AUDIT_COMMIT],
    ["Helper script SHA-256", "a533881c9439d01238ef7708ba962e1c43e5a2d4abfe004af53b4616e8a731b2"],
    ["Audit note", "project/research/general_n/2026-09-24-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md"],
    ["Replay failure", ".../SUPPORT10_HELPER_REPLAY_FAILURE.json"],
    ["Telemetry reconciliation", "project/research/session_logs/2026-09-23/AUDIT_RECONCILIATION_2026-09-24.md"],
]
S.append(grid_table(refs, [50 * mm, 117 * mm]))

doc.build(S, onFirstPage=header_footer, onLaterPages=header_footer)
print(OUT)
