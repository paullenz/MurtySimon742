# Launch-reliability repair — 22 September 2026

## User priority and scope

The user clarified: "Missed starts is more important. 24 sessions of 40 mins is better than 10 of 50."

This is an administrative change to delivery and prospective duration policy. It creates no mathematical results, historical session credit, or claim of recovered scheduling.

## Observed configuration

The active research task 6ab23822ccfc819180460a39e879b68a is tied to conversation 6ab2352e-8664-83ed-9cd0-bb5b554b1e32. The paused monitor was tied to the same conversation. Today's evidence includes missing canonical starts and late no-research deliveries. The exact backend cause is not exposed.

The already disabled task 6aab2d04da4c81919448e011b1b46cf8 has conversation_id=null. It has been prepared, still paused, with a fully replaced independent-#742 prompt and a bounded new schedule. This repurposes a standalone configuration; it does not revive the historical eventual-D2C objective. Official documentation states that standalone tasks create a new chat for each scheduled run:
https://learn.chatgpt.com/docs/automations

The browser could not load task settings (navigation/frame timeouts), and connector update/create schemas do not expose a conversation-destination field. Reusing the existing unbound task avoids inventing such a control.

## Prepared change and cutover

- First replacement trigger: 23 September 2026, 01:00:38 Europe/London.
- Research triggers: 01:00 through 23:00 daily, at second 38; 115 occurrences over 23–27 September. COUNT is used because the scheduler normalizer stripped the UTC marker from UNTIL in an initial paused preparation.
- Last replacement research trigger: 27 September 2026, 23:00:38 BST.
- Existing midnight audit and 28 September 00:05 stop schedule stay in place.
- Before enabling the replacement, pause the old chat-bound research schedule. Already delivered/current runs are not claimed cancelled.
- Keep same-chat health checker and other retired research tasks paused; never create a second research writer for one trigger.
- Aim for 40 verified research minutes, preserving the existing research cutoff and hard-close buffers.
- Record launch coverage independently of duration/focused-session credit. Historical short records are not reclassified.
- The new standalone prompt is saved in STANDALONE_RESEARCH_PROMPT.txt alongside this note.

## Verification required after activation

Verify the task readback: replacement enabled with conversation_id=null, exact bounded schedule and saved prompt; old research/health tasks disabled; audit and stop active with corrected IDs/policy.

The first three replacement triggers (23 September 01:00:38, 02:00:38, 03:00:38 BST) are the initial launch test. Each needs an actual canonical STARTED publication and a substantive durable checkpoint, with launch delay and measured work reported. At the next audit compare every due trigger against artifacts, including absent records. Do not declare the day recovered from task settings or last_run_time.

Preparation was published in commit 4b13f71482f4ff9b2c81aa783dbcfa682f0c3e8d. Mathematical state and latest research next action are unchanged.


## Activation and readback — 22 September 2026 23:13:26 BST

Status: CONFIGURATION_APPLIED; ACTUAL_LAUNCH_RECOVERY_UNVERIFIED.

The replacement was enabled at 23:12:48 BST, after the old same-chat research task was paused. A subsequent private task read verified all eight checks:

1. Replacement enabled and conversation_id=null.
2. Saved research prompt exactly matches STANDALONE_RESEARCH_PROMPT.txt (without its terminal newline).
3. Saved schedule exactly matches the validated DTSTART/RRULE/COUNT configuration.
4. Old same-chat research disabled.
5. Midnight audit enabled with launch-first counting, historical-target preservation and the first-three-launch review.
6. Stop task enabled with the replacement ID and original 28 September 00:05 schedule.
7. Same-chat health checker disabled.
8. Earlier retired research disabled.

No immediate run was requested, no historical catch-up burst was created, and no scheduled start is credited by this administrative change. The first replacement trigger remains 23 September 01:00:38 BST. The scheduler exposes no backend queue trace; these verified configuration changes do not prove a root cause or guarantee delivery.

The prior 22:00 record remains 31m02s under its original 50-minute policy. It is not upgraded by the prospective 40-minute policy. The last mathematical NEXT ACTION is unchanged.
