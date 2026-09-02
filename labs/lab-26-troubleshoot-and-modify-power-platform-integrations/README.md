# Lab 26 — Troubleshoot and Modify Power Platform Integrations

| | |
|---|---|
| **Learning Unit** | LU4 — Model-Driven Apps with Power Apps and Dataverse |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A7/A8 — Diagnose integration failures by layer and implement the corrective modification. |
| **Duration** | 60 minutes |
| **Services** | Power Apps Monitor, Power Automate run history, Power Platform admin centre, Dataverse |

## What you will build

A troubleshooting log recording each fault, the layer it belonged to, the evidence and the fix applied.

## Scenario

Work a set of seeded faults — a delegation warning, a failed flow action, a permission error and a broken connection reference — isolating each to its layer and applying the fix.

## Prerequisites

- **Labs 07, 12, 14 and 25** completed — the four seeded faults sit in the artefacts those labs produced.
- Your trainer must have seeded the faults first (see `mock-data/seeded-faults.md`, which is trainer material).
- Access to the Power Platform admin centre to assign a security role for fault F-03.
- The second (Test) environment from Lab 25 for fault F-04.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `troubleshooting-log.csv` | The TSC A7/A8 evidence log. Rows F-01 to F-04 are worked examples showing the level of detail expected. Rows F-05 to F-08 are blank - complete them for the four faults your trainer seeded in your own environment. |
| `seeded-faults.md` | Trainer notes describing exactly how each of the four faults is seeded and what the correct fix is. Read it only at the debrief - working it out from the product is the point of the lab. |

## Steps

1. Open mock-data/troubleshooting-log.csv — you will record each fault, its layer, the evidence and the fix.

2. In the canvas app add a filter over a large table using a non-delegable function and observe the blue delegation warning.

   ```powerfx
   Filter('Booking Requests', Len('Pet Name') > 3)
   ```

3. Rewrite the same filter with a delegable expression and confirm the warning clears.

   ```powerfx
   Filter('Booking Requests', StartsWith('Pet Name', txtSearch.Text))
   ```

4. Open Power Automate > My flows and find a flow with a failed run; open the failed action and read its error message and inputs.

5. Fix the failure — typically a missing dynamic-content reference or an expired connection — then Resubmit the run.

6. Sign in as the shared user from Lab 12, open the app and capture the Dataverse permission error.

7. In the Power Platform admin centre assign the correct security role to that user and confirm the app now loads.

8. Open the imported solution from Lab 25 and repair the broken connection reference in the Test environment.

9. Use Power Apps Monitor while running the app to confirm no failing network calls remain.

10. Complete troubleshooting-log.csv with the layer, evidence and fix for all four faults.

## Verify

All four faults are resolved — no delegation warning, the flow run succeeds on resubmit, the shared user can open the app, and the connection reference is repaired — with each recorded in the log.

## Troubleshooting

**Problem — The delegation warning does not appear even with the non-delegable filter.**

*Fix:* The table is under the client-side row limit, so Power Apps can fetch everything and does not warn. Lower **Settings > General > Data row limit for non-delegable queries** to 100, or import extra rows, then re-open the property. The warning is a design-time signal — it appears next to the formula and in **App Checker > Delegation**, not at run time.

**Problem — Resubmitting the fixed flow run still fails with the same error.**

*Fix:* Resubmit replays the **original trigger payload against the saved flow definition** — so if you fixed and did not save, or saved into a different version, nothing changed. Save the flow, confirm the action now shows the dynamic-content token, then Resubmit. If it still fails, trigger a fresh run instead; a resubmit cannot recover a run whose trigger data was itself invalid.

**Problem — The security role is assigned but the shared user still sees the permission error.**

*Fix:* Dataverse privileges are cached per session. Have the user sign out completely and reopen the app in a new InPrivate window. Then confirm the role actually grants **Read on the Booking Request table at organisation or business-unit scope** — a role with only user-level read shows rows the user owns, which for imported data is none, producing an empty gallery that looks identical to no permission at all.

---

**End of the lab sequence.** Return to the [lab index](../README.md).
