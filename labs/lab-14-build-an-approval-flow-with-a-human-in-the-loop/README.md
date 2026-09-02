# Lab 14 — Build an Approval Flow with a Human in the Loop

| | |
|---|---|
| **Learning Unit** | LU3 — Automated Processes with Power Automate and Copilot Studio Agents |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3/A5 — Pause an automated process for a human decision and branch on the outcome. |
| **Duration** | 50 minutes |
| **Services** | Power Automate, Approvals, Dataverse, Outlook, Microsoft Teams |

## What you will build

An approval flow that writes Confirmed or Declined back to Dataverse based on a human decision.

## Scenario

Build a flow that starts when a booking request row is created, sends an approval to a manager, waits for the response, and updates the record's status based on the outcome.

## Prerequisites

- **Lab 06** completed — the flow triggers on the Booking Request Dataverse table.
- The Approvals connector connected, plus Microsoft Teams for the actionable approval card.
- A second account to act as the approver, or approve as yourself if working solo.
- This flow is the one you package in **Lab 25** and repair in **Lab 26** (fault F-02).

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `approval-scenarios.csv` | Ten booking requests with the decision to make and the Dataverse Status the flow must write. Six approvals and four rejections, so both Condition branches are exercised. Amount = Nights x Rate from the Lab 6 kennel rates. |

## Steps

1. Create an automated cloud flow with the Dataverse trigger 'When a row is added, modified or deleted'.

2. Set Change type to Added, Table name to Booking Requests and Scope to Organization.

3. Add the action Start and wait for an approval; choose Approve/Reject - First to respond.

4. Set the Title using dynamic content, and set Assigned to the manager's account; keep approvals in Teams so they are actionable.

5. Add a Condition comparing the approval Outcome to the literal Approve.

   ```text
   outputs('Start_and_wait_for_an_approval')?['body/outcome'] is equal to Approve
   ```

6. In the If yes branch add Update a row and set Status to Confirmed; in If no set Status to Declined.

7. Add a Send an email (V2) action in each branch to notify the requester of the decision.

8. Save, then create a Booking Request row to trigger the flow and approve it from the Approvals area or Teams.

9. Open Run history and confirm the Condition took the expected branch.

## Verify

Approving the request sets the Dataverse row's Status to Confirmed and the requester receives the notification email; rejecting sets Declined.

## Troubleshooting

**Problem — The approval email arrives but the Approve and Reject buttons do nothing.**

*Fix:* Outlook approval cards are not actionable in this scenario. Respond from the **Approvals** area in Power Automate or from the Approvals app in Microsoft Teams. Keeping approvals in Teams is exactly why the step says so.

**Problem — The Condition always takes the **If no** branch even when you approved.**

*Fix:* The comparison is case-sensitive and must be against the literal `Approve` (singular, capitalised) — not `Approved`, not `approve`. Confirm the left-hand side is `outputs('Start_and_wait_for_an_approval')?['body/outcome']` and read the actual value in **Run history > Outputs** before changing anything else.

**Problem — **Update a row** fails with 400 "A required property is missing".**

*Fix:* The Row ID field is empty or holds text rather than the trigger's unique identifier. Clear it and re-insert the Booking Request GUID from the dynamic-content picker. This is the same failure you deliberately diagnose as fault **F-02** in Lab 26.

---

**Next:** [Lab 15 — Button Flows and Scheduled Flows](../lab-15-button-flows-and-scheduled-flows/README.md)
