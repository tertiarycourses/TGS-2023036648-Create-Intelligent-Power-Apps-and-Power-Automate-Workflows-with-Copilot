# Lab 17 — Build Your First Copilot Studio Agent

| | |
|---|---|
| **Learning Unit** | LU3 — Automated Processes with Power Automate and Copilot Studio Agents |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A1/A3 — Build a conversational agent with instructions and knowledge as a new integration surface. |
| **Duration** | 50 minutes |
| **Services** | Copilot Studio (new agent designer), SharePoint, Dataverse |

## What you will build

A grounded Copilot Studio agent that answers only from your documents and refuses otherwise.

## Scenario

In the new Copilot Studio agent designer, create an agent, choose its model, write constraining instructions, attach a SharePoint knowledge source and remove every other source of facts, then probe it for hallucination.

## Prerequisites

- A Copilot Studio licence or trial in the **same environment** as your flows.
- A SharePoint document library you can upload the four policy files to.
- **Lab 01** completed — the SharePoint connection must be working.
- This agent is the parent agent extended in **Lab 20**.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `hr-policies/annual-leave.md` | Leave entitlement table, pro-rating formula, carry-forward cap of 7 days and the notice-period table. The retrievable facts include 14 days in year one and 2 months' notice at 3 years. |
| `hr-policies/medical-benefits.md` | Outpatient cap SGD 800, dental cap SGD 300, wellness allowance SGD 400, hospitalisation SGD 150,000, and the 60-day claim window. |
| `hr-policies/wfh-policy.md` | Up to 2 WFH days per week, 10:00-16:00 core hours, the SGD 300 one-time home-office allowance and the 2-month response deadline for a formal flexible-work request. |
| `hr-policies/code-of-conduct.md` | Gift threshold SGD 100, hospitality threshold SGD 200 per person, the 5% shareholding declaration rule and the 24-hour breach reporting window. |
| `probe-questions.csv` | Twelve probes - six answerable from the documents and six designed to make an ungrounded agent invent an answer. If the agent answers any of the six out-of-scope questions, general knowledge or the web knowledge source is still switched on. |

## Steps

1. Open copilotstudio.microsoft.com, confirm the environment matches your flows, and select + Create > New agent.

2. Name the agent HR Policy Assistant and pick the model (GPT-5.x or Claude) from the Model dropdown on the Build tab.

3. Write instructions that state identity, source rule, refusals and escalation — type the prose, never paste @{...} expressions into the rich-text box.

4. Upload the documents in mock-data/hr-policies/ to a SharePoint library, then add that library under Knowledge and wait for the status to reach Ready.

5. Turn OFF general knowledge (Settings > Generative AI) so the model cannot answer from training data.

6. Remove the 'Search all websites' knowledge source — it is on by default and open-web facts are indistinguishable from yours.

7. Add the instruction line: Never include citation markers, reference numbers or source tags in your reply.

8. Open the Preview tab and ask three questions answerable from the documents, then three that are not — record which the agent refuses.

9. Publish the agent and note the Enforced/Not-enforced status of instructions versus knowledge.

## Verify

The agent answers the in-scope questions from the documents and explicitly declines the out-of-scope ones instead of inventing an answer.

## Troubleshooting

**Problem — The SharePoint knowledge source stays on **Indexing** and never reaches Ready.**

*Fix:* Indexing can legitimately take 10–15 minutes for a new library, but it stalls permanently in three cases: the library is empty, the files are not a supported type, or the connection was made with an account that cannot read the library. Confirm the four `.md` files uploaded successfully, and re-add the source using a connection created with your own training account. If it is still indexing after 30 minutes, delete the knowledge source and add it again — a stuck index does not recover on its own.

**Problem — The agent answers the out-of-scope probe questions confidently and in detail.**

*Fix:* Two switches are still on. Turn **general knowledge off** under *Settings > Generative AI*, and **remove the "Search all websites" knowledge source**, which is added by default. Both must be off; leaving either one on makes the model's own training data indistinguishable from your documents. Re-run the six out-of-scope rows in `probe-questions.csv` after each change.

**Problem — The replies contain citation markers such as `[1]` or bracketed source tags.**

*Fix:* Add the explicit instruction line *"Never include citation markers, reference numbers or source tags in your reply"* to the Instructions box, and type it rather than pasting — the rich-text editor mangles pasted content. If markers persist, also turn off in-text citations in the agent's generative AI settings; the instruction alone is advisory, not enforced.

---

**Next:** [Lab 18 — Give the Agent a Tool — Calling a Workflow from an Agent](../lab-18-give-the-agent-a-tool-calling-a-workflow-from-an-agent/README.md)
