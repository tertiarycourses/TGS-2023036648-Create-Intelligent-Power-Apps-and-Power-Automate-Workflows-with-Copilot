# Lab 03 — Build a Cloud Flow with Copilot for Power Automate

| | |
|---|---|
| **Learning Unit** | LU1 — Get Started with Copilot for Microsoft Power Platform |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3/A5 — Use Copilot to assemble a flow, then read and test what it built. |
| **Duration** | 45 minutes |
| **Services** | Power Automate, Copilot for Power Automate, Outlook, SharePoint |

## What you will build

A working Copilot-built cloud flow that emails a summary when a new item is created.

## Scenario

Use Copilot in Power Automate to build a flow from a description, then examine the trigger and actions it chose, correct them, and test the run.

## Prerequisites

- **Lab 01** completed — the same environment, with the Office 365 Outlook and SharePoint connections created.
- A SharePoint site you can create a list in. If you have not yet reached Lab 09, use the trainer's demo list.
- Microsoft Teams available to the training account, for the step that posts a Teams message.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `sharepoint-items.csv` | Eight facilities and IT service requests to create in the SharePoint list one at a time, so each creation fires the flow trigger once. Title, RequestedBy and Priority are the fields the generated email reads. |

## Steps

1. Open make.powerautomate.com and confirm you are in the same environment you used in Lab 1.

2. On the home page, enter the Copilot prompt: When a new item is created in a SharePoint list, send me an email with the item details.

3. Review the flow Copilot drafts. Confirm the trigger is 'When an item is created' and the action is 'Send an email (V2)'.

4. Select each step and supply the connection, the SharePoint site address and the list name from Lab 5's list (or the trainer's demo list).

5. Ask Copilot in the side pane: add a step to post a message to Microsoft Teams as well — and inspect the action it inserts.

6. Save the flow, then select Test > Manually and create a list item to fire the trigger.

7. Open the run in Run history and read the inputs and outputs of every action — this is the TSC A5 verification evidence.

## Verify

The run history shows a Succeeded run, the email arrives with the item's field values, and you can point at the action output that supplied each value.

## Troubleshooting

**Problem — Copilot drafts the flow but every action shows a red "Invalid connection" warning.**

*Fix:* The flow was drafted before the connections existed. Select each action, open the three-dot menu > **My connections > Add new connection**, sign in, then re-open the action and re-pick the site address and list name. Save only after every warning clears.

**Problem — The **Send an email (V2)** action fails at run time with "The specified object was not found in the store".**

*Fix:* The SharePoint site address or list name is stale — typically because you typed the site URL instead of picking it from the dropdown. Re-select the site from **Site Address** using the picker (it must resolve to a value, not stay as free text), then re-select the list, and Resubmit the run.

**Problem — The Teams action Copilot inserted posts to the wrong team, or fails with a 403.**

*Fix:* Copilot guesses the team and channel. Open the action and set **Post as** to *Flow bot*, then pick the Team and Channel explicitly from the dropdowns. If the dropdowns are empty, the training account is not a member of any team — ask the trainer to add you.

---

**Next:** [Lab 04 — Use Copilot to Build a Power Pages Site](../lab-04-use-copilot-to-build-a-power-pages-site/README.md)
