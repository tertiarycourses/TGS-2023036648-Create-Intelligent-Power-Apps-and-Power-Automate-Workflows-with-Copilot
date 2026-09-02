# Lab 19 — Call an Agent from a Workflow with Structured Output

| | |
|---|---|
| **Learning Unit** | LU3 — Automated Processes with Power Automate and Copilot Studio Agents |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A4/A5 — Use an Agent node inside a flow and consume its typed fields downstream. |
| **Duration** | 50 minutes |
| **Services** | Copilot Studio workflow designer, Agent node, Dataverse, Outlook |

## What you will build

A flow whose Agent node returns structured JSON that the following actions branch on.

## Scenario

Build a Power Automate flow containing an Agent node that classifies an incoming request, configure Custom structured output so the result is typed JSON, and branch the flow on the returned fields.

## Prerequisites

- **Lab 17** completed — the Agent node calls an agent you have already published.
- A model that supports structured output selected on the agent (check the Model dropdown on the Build tab).
- Familiarity with the flow designer from **Labs 13 to 16**.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `classification-samples.csv` | Twelve customer messages with the category and urgency the Agent node should return. Four Booking, four Complaint and four Other, so every case of the Switch is exercised. |
| `structured-output-schema.json` | The JSON schema for the Agent node's Custom structured output - category (enum), urgency (enum) and draftReply (constrained string). Mirror these three properties in the node's schema editor. |

## Steps

1. In Copilot Studio select Flows > + New agent flow and add a manual or Dataverse trigger.

2. Add an Agent node; note its Configure tab has Connection, Agent, Instructions, Tools, Knowledge and Output — there is no user-message field.

3. Put the per-call data into Instructions using the lightning-bolt picker to insert the trigger's fields.

4. Set Output to Custom structured output and define a schema with category (string), urgency (string) and draftReply (string).

5. Delete any Parse JSON node — with structured output the fields are referenced directly.

   ```text
   body('Agent')?['structuredOutput/category']
   ```

6. Add a Switch on the category field with cases for Booking, Complaint and Other.

7. In the Complaint case add Send an email (V2) using the draftReply field, inserting the address with the picker rather than typing it.

8. Save, run the flow with a sample request, and open Run Details > Outputs on the Agent node to read the actual structured output.

## Verify

The Agent node's Run Details shows the three schema fields populated, and the Switch routes the run to the case matching the returned category.

## Troubleshooting

**Problem — The Agent node has no field to put the user's message in.**

*Fix:* That is correct — there is no user-message field. The per-call data goes into **Instructions**, inserted with the lightning-bolt dynamic-content picker. Type the surrounding prose and use the picker for every token; pasting `@{...}` expressions into the rich-text Instructions box silently corrupts them.

**Problem — `body('Agent')?['structuredOutput/category']` returns null.**

*Fix:* Either structured output is not switched on, or a Parse JSON node is still in the flow consuming the output first. Set **Output** to *Custom structured output*, define the three properties, and delete any Parse JSON node — with structured output the fields are referenced directly. Then open **Run Details > Outputs** on the Agent node and read the actual shape before writing the reference.

**Problem — The Switch always falls to the default case.**

*Fix:* The returned category does not match the case values exactly. Constrain the model with an `enum` in the schema (see `structured-output-schema.json`) so it can only return `Booking`, `Complaint` or `Other`, and make the Switch cases match that spelling character for character. Reading the node's actual output once is faster than guessing.

---

**Next:** [Lab 20 — Multi-Agent Handoff and a Human Review Gate](../lab-20-multi-agent-handoff-and-a-human-review-gate/README.md)
