# Lab 18 — Give the Agent a Tool — Calling a Workflow from an Agent

| | |
|---|---|
| **Learning Unit** | LU3 — Automated Processes with Power Automate and Copilot Studio Agents |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A4 — Expose a deterministic flow to an agent as a callable tool with typed inputs and outputs. |
| **Duration** | 50 minutes |
| **Services** | Copilot Studio agent flows, Power Automate, Dataverse, Microsoft Teams |

## What you will build

An agent that calls a Power Automate flow as a tool and returns the flow's result in chat.

## Scenario

Build an agent flow that validates and writes a booking, then register it as a tool on the agent so the conversation can act on the outside world while the enforced logic stays in the flow.

## Prerequisites

- **Lab 17** completed — you add the tool to that agent.
- **Lab 06** completed — the flow writes to the Booking Request table.
- Publish rights for agent flows in the environment.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `tool-test-cases.csv` | Ten utterances to type into Preview, with the tool the agent should choose and the outcome. Includes the 30-night boundary (accepted), 31 nights (refused) and the 60-night case that proves the flow's Condition overrides whatever the agent decided to do. |

## Steps

1. In Copilot Studio open your agent, select Tools > + Add a tool > New agent flow.

2. The flow opens with the trigger 'When an agent calls the workflow'; add the input parameters petName (Text), ownerName (Text) and nights (Number).

3. Add a Condition that rejects a nights value above 30 — this validation is enforced, unlike an instruction.

4. In the valid branch add Add a new row to Booking Requests, mapping each input with the dynamic-content picker.

5. Add the 'Respond to the agent' action and return a confirmation message and the created row's id.

6. Save and publish the flow, then return to the agent and confirm the tool is listed under Tools.

7. Write the tool description for the model, not for a developer — it is how the agent decides when to call it.

8. In Preview ask: book a kennel for Rex for 3 nights, owner Jane Tan — and confirm the agent collects the inputs and calls the tool.

9. Probe the boundary: ask for 60 nights and confirm the flow's validation refuses even though the agent tried.

## Verify

A valid request creates a Dataverse row and returns the confirmation in chat; the 60-night request is refused by the flow's own Condition.

## Troubleshooting

**Problem — The tool does not appear under **Tools** after you save the flow.**

*Fix:* An agent flow must be **published**, not merely saved, before the agent can see it. Publish the flow, then return to the agent and refresh the browser. If it still does not appear, confirm the flow's trigger is *When an agent calls the workflow* — a standard manual trigger cannot be registered as a tool.

**Problem — The agent answers the booking request conversationally but never calls the tool.**

*Fix:* The tool description is written for a developer instead of for the model. Rewrite it as a plain statement of when to use it — for example *"Use this to create a kennel booking when the user gives a pet name, an owner name and a number of nights"*. Also confirm all three input parameters have descriptions; a parameter with no description is one the agent does not know how to fill.

**Problem — The 60-night request creates a row anyway.**

*Fix:* The Condition is in the wrong place or is comparing text to a number. It must sit **before** the *Add a new row* action, and `nights` must be typed as Number on the trigger — a Text input compared with `greater than 30` evaluates as a string and passes. Fix the parameter type, re-publish the flow, and re-run the boundary cases in `tool-test-cases.csv`: 30 accepted, 31 and 60 refused.

---

**Next:** [Lab 19 — Call an Agent from a Workflow with Structured Output](../lab-19-call-an-agent-from-a-workflow-with-structured-output/README.md)
