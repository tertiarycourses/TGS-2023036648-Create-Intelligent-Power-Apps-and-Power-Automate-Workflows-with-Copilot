# Lab 16 — Trigger Filters and Cross-Source Integration

| | |
|---|---|
| **Learning Unit** | LU3 — Automated Processes with Power Automate and Copilot Studio Agents |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A5/A7 — Stop unnecessary runs with trigger filters and highlight performance issues. |
| **Duration** | 45 minutes |
| **Services** | Power Automate, Dataverse, SharePoint, Excel Online (Business) |

## What you will build

A filtered automated flow plus a run-count comparison showing the performance improvement.

## Scenario

Add column and row filters to an automated trigger so the flow only runs when it must, then integrate SharePoint, Dataverse and Excel in one flow and compare run counts before and after filtering.

## Prerequisites

- **Lab 06** completed — the trigger fires on the Booking Request table.
- **Lab 09** completed — the SharePoint Kennel Bookings list, for the cross-source step.
- An Excel workbook in OneDrive with a named table to act as the log (reuse the Lab 05 workbook or create a second one).

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `trigger-filter-tests.csv` | Ten edits to make against a Booking Request row, with whether the filtered trigger should fire and why. Run every case before adding the filter to get your baseline run count, then run them again afterwards - only TF-01 and TF-06 should remain. |

## Steps

1. Open the Booking Requests table, select the Status column and note its schema name (for example statuscode) — filters use schema names, not display names.

2. Create an automated flow on 'When a row is added, modified or deleted' with Change type Modified.

3. Add a Send an email (V2) action, save, and modify several rows to generate baseline runs; record the run count.

4. Open the trigger's Settings and add the schema name to Select columns so only Status changes fire the flow.

   ```text
   statuscode
   ```

5. Add a Filter rows expression so only rows moving to Confirmed trigger it.

   ```text
   statuscode eq 1
   ```

6. Save, repeat the same edits, and record the new run count against the baseline.

7. Add Get items from the SharePoint Kennel Bookings list and Add a row into a table for the Excel log workbook.

8. Run once more and confirm one business event now writes to Dataverse, SharePoint and Excel in a single run.

## Verify

After filtering, edits to non-Status columns produce no runs, and a single Confirmed change writes to all three data sources in one Succeeded run.

## Troubleshooting

**Problem — The flow still runs on every edit after adding **Select columns**.**

*Fix:* The setting takes the column's **schema name** (for example `statuscode`), not its display name (`Status`), and multiple columns are comma-separated with no spaces. Read the schema name from the table designer, paste it exactly, then save and re-test. A display name in this field silently matches nothing and the trigger falls back to firing on every change.

**Problem — Adding the **Filter rows** expression stops the flow firing at all.**

*Fix:* Filter rows uses OData against the schema names too, and a wrong option value matches zero rows. Temporarily remove the filter, run once, and read the trigger's output in run history to see the actual `statuscode` value on a Confirmed row — then put that number in the filter.

**Problem — The **Add a row into a table** Excel action fails with "The table is not found".**

*Fix:* The Excel connector needs a workbook containing a named table and the workbook must not be open with a lock. Reuse the pattern from Lab 05: create the table with Ctrl+T, give it a name, close the workbook, then re-pick the file, table and columns in the action.

---

**Next:** [Lab 17 — Build Your First Copilot Studio Agent](../lab-17-build-your-first-copilot-studio-agent/README.md)
