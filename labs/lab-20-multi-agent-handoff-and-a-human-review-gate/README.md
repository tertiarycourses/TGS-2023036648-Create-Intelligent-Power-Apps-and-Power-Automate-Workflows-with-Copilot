# Lab 20 — Multi-Agent Handoff and a Human Review Gate

| | |
|---|---|
| **Learning Unit** | LU3 — Automated Processes with Power Automate and Copilot Studio Agents |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A5/A7 — Compose connected agents and place a human where the consequence lands. |
| **Duration** | 50 minutes |
| **Services** | Copilot Studio (connected agents), agent flows, Microsoft Teams approvals |

## What you will build

A two-agent system with a working handoff and a human review gate that blocks the run.

## Scenario

Connect a second specialist agent so one conversation can hand off to another with its own knowledge, then add a Request human assistance gate so a consequential action cannot proceed without approval.

## Prerequisites

- **Lab 17** completed — the HR Policy Assistant is the parent agent.
- **Lab 18** completed — the booking agent flow is where the human review gate is inserted.
- Microsoft Teams available, because approvals in this designer are only actionable in Teams.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `finance-policies/claims-policy.md` | Submission deadline of 45 days, SGD 120 per person entertainment cap, SGD 0.75/km mileage and the four-tier approval table. |
| `finance-policies/procurement-policy.md` | Quotation thresholds from SGD 2,000 to above SGD 50,000, the SGD 5,000 capex definition and the SGD 25,000 Legal review trigger. |
| `finance-policies/travel-policy.md` | Cabin class by flight duration, hotel caps of SGD 200/320/420 by band and per diems of SGD 70/100/130. |
| `handoff-test-cases.csv` | Ten questions with the agent that should answer each. Three belong to the parent HR agent and seven must be handed off - if any Finance question is answered by the parent, the connection description is too vague. |

## Steps

1. Create a second agent named Finance Assistant with its own knowledge source from mock-data/finance-policies/.

2. Open the HR Policy Assistant and select Connected agents > + Add, then choose Finance Assistant.

3. Write the connection description so the parent knows when to hand off — for example, for questions about claims, reimbursement or budgets.

4. In Preview ask an HR question then a claims question, and confirm the second is answered by the connected agent.

5. Open the booking agent flow from Lab 18 and add Request human assistance before the row is written.

6. Route the approval to Microsoft Teams — Outlook approvals are not actionable in this designer.

7. Publish and run: submit a booking and confirm the flow pauses with a Waiting status until a human responds.

8. Reject the request and confirm no Dataverse row is written, then run again and approve it.

9. Compare the two run histories to show the gate is enforced by the flow, not by the agent's instructions.

## Verify

The claims question is answered by the connected agent, and a rejected booking leaves no Dataverse row while an approved one does.

## Troubleshooting

**Problem — The parent agent answers the Finance questions itself instead of handing off.**

*Fix:* The connection description is too vague. Rewrite it to name the topics explicitly — *"for questions about expense claims, reimbursement, procurement thresholds, purchase orders or business travel"* — and add a line to the parent's instructions telling it to hand off rather than answer when a question is about money. Then re-run the seven handoff rows in `handoff-test-cases.csv`.

**Problem — The **Request human assistance** approval never arrives.**

*Fix:* Route it to **Microsoft Teams**. Outlook approvals are not actionable in this designer, so the flow waits forever on a card nobody can respond to. Also confirm the approver is a licensed user in the same tenant; an external address leaves the run in Waiting indefinitely.

**Problem — The Dataverse row is created even though the request was rejected.**

*Fix:* The gate is in the wrong position. **Request human assistance** must sit before the *Add a new row* action, with the row creation inside the approved branch only. Compare the two run histories — the rejected run must show no *Add a new row* action at all, which is how you demonstrate the gate is enforced by the flow rather than by the agent's instructions.

---

**Next:** [Lab 21 — Create Dataverse Tables for a Model-Driven App](../lab-21-create-dataverse-tables-for-a-model-driven-app/README.md)
