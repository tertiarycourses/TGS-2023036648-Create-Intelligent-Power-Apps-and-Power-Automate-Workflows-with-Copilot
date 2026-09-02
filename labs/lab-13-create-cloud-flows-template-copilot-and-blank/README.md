# Lab 13 — Create Cloud Flows — Template, Copilot and Blank

| | |
|---|---|
| **Learning Unit** | LU3 — Automated Processes with Power Automate and Copilot Studio Agents |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3/A5 — Build flows three ways and verify each run against its trigger and actions. |
| **Duration** | 50 minutes |
| **Services** | Power Automate, Outlook, SharePoint, Copilot for Power Automate |

## What you will build

Three working cloud flows plus a read of their run history.

## Scenario

Create one flow from a template, one with Copilot and one from blank, so the trigger-actions-outputs anatomy is visible from three directions, then read the run history of each.

## Prerequisites

- **Lab 01** completed — the same environment, with the Outlook, OneDrive and SharePoint connections.
- A SharePoint list you can create items in (the Kennel Bookings list from Lab 09 is ideal).
- **Lab 03** is useful background but not required; this lab revisits Copilot-built flows deliberately.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `flow-test-emails.csv` | Eight emails to send yourself to exercise the template flow. Three carry no attachment, which proves the Apply to each loop runs zero times rather than failing. |
| `sharepoint-list-items.csv` | Eight list items to create one at a time so the Copilot-built flow and the from-blank flow each fire a separate run you can read in Run history. |

## Steps

1. Open make.powerautomate.com and confirm you are in the Dev One environment.

2. Select Templates, search for a 'Save Office 365 email attachments to OneDrive' template and create it, supplying each connection.

3. Run the template flow by sending yourself an email with an attachment, then open Run history and read each action's inputs and outputs.

4. On the home page enter a Copilot prompt to draft a second flow: send me an email when a new item is added to my SharePoint list.

5. Select + Create > Automated cloud flow to build the third flow from blank; choose the 'When an item is created' SharePoint trigger.

6. Configure the trigger with the site address and list name, then + New step > Send an email (V2).

7. In the email body use Dynamic content to insert the item's Title and Created By — never type the values.

8. Save and test the blank flow, then compare all three flows' run histories in the Cloud flow activity page.

## Verify

All three flows show a Succeeded run, and you can name the trigger and each action's output that supplied a value in the email.

## Troubleshooting

**Problem — The template flow is created but never runs when you send yourself an email.**

*Fix:* Check the trigger's folder — the template defaults to *Inbox* only, so a message filtered into another folder by a rule never fires it. Also confirm the flow is switched **On** in *My flows*; a template flow created with an unresolved connection is created in the off state.

**Problem — Dynamic content does not offer the item's *Title* or *Created By*.**

*Fix:* The trigger has no list selected yet, so the schema is unknown. Set the Site Address and List Name on the trigger, save, then reopen the email action — the dynamic-content panel is populated from the trigger's saved schema. Never type a field value in place of a token; the lab's verification step asks you to point at the action output that supplied it.

**Problem — The Copilot-built flow and the from-blank flow both fire on the same list item.**

*Fix:* That is correct and worth noticing — two flows can share a trigger. If you want only one to run, turn the other off from **My flows**, or add a trigger condition. Comparing their run histories side by side in *Cloud flow activity* is the verification step.

---

**Next:** [Lab 14 — Build an Approval Flow with a Human in the Loop](../lab-14-build-an-approval-flow-with-a-human-in-the-loop/README.md)
