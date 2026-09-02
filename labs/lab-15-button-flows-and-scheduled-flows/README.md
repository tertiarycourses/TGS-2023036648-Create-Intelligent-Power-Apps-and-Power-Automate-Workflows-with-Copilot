# Lab 15 — Button Flows and Scheduled Flows

| | |
|---|---|
| **Learning Unit** | LU3 — Automated Processes with Power Automate and Copilot Studio Agents |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3 — Use manual and scheduled triggers, and collect user input at run time. |
| **Duration** | 45 minutes |
| **Services** | Power Automate, Dataverse, Outlook |

## What you will build

An instant flow with user input and a recurring digest flow that emails a formatted table.

## Scenario

Build an instant (button) flow that prompts the user for input and creates a record, then build a scheduled flow that queries rows on a recurrence and emails an HTML summary table.

## Prerequisites

- **Lab 06** completed — both flows read and write the Booking Request table.
- **Lab 14** recommended — you reuse the same Dataverse connection.
- Know the schema name of the Status column (found in Lab 06 or at the start of Lab 16) — the Filter Query uses it.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `pending-bookings.csv` | Twelve bookings all left at Requested, which is what the scheduled flow's Filter Query returns. These are the rows that must appear in the HTML table the digest emails. Kennel values match kennels.csv from Lab 6. |

## Steps

1. Select + Create > Instant cloud flow and choose the trigger 'Manually trigger a flow'.

2. On the trigger add three user inputs: Pet Name (Text), Owner Name (Text) and Drop Off (Date).

3. Add Add a new row for the Booking Requests table and map each column to the matching trigger input.

4. Save and run the flow from the Power Automate mobile app or the Test pane, supplying values; verify the Dataverse row.

5. Create a second flow with + Create > Scheduled cloud flow and set Recurrence to run daily at 08:00 with the time zone set to Singapore.

6. Add List rows for Booking Requests and set the Filter Query to return only pending rows.

   ```text
   statuscode eq 1
   ```

7. Add Select to project only the columns you need, then Create HTML table over the Select output.

8. Add Send an email (V2) with the HTML table in the body and set Is HTML to Yes.

9. Use Test > Manually to run the scheduled flow now rather than waiting for the recurrence.

## Verify

The button flow creates a Dataverse row from the values you typed, and the scheduled flow's test run emails a formatted HTML table of pending bookings.

## Troubleshooting

**Problem — The manual trigger's user inputs do not appear when you test the flow.**

*Fix:* Inputs added after the first save sometimes do not refresh in the Test pane. Save, close the flow, reopen it, then Test again. In the Power Automate mobile app, pull to refresh the flow list — the app caches the input schema.

**Problem — The scheduled flow returns no rows even though bookings exist.**

*Fix:* `statuscode eq 1` uses the **schema name and the option's numeric value**, not the display label. Open the Status column in the table designer and read the actual value assigned to *Requested* — in many environments the first custom option is `1` but Dataverse may have numbered it differently. Substitute the real number, or filter on the column's label using `Filter rows` in the designer's expression builder.

**Problem — The email arrives with raw HTML tags visible instead of a table.**

*Fix:* **Is HTML** on the Send an email (V2) action is set to No. Open the action's advanced parameters and switch it to Yes. If the table still renders as a single column, confirm the **Create HTML table** action's *From* is the output of **Select**, not the raw *List rows* value.

---

**Next:** [Lab 16 — Trigger Filters and Cross-Source Integration](../lab-16-trigger-filters-and-cross-source-integration/README.md)
