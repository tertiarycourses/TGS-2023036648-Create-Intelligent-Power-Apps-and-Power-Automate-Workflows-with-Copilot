# Lab 07 — Create a Canvas App over Dataverse

| | |
|---|---|
| **Learning Unit** | LU2 — Create and Manage Canvas Apps with Power Apps |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3 — Bind a hand-built canvas app to Dataverse and format the data it displays. |
| **Duration** | 40 minutes |
| **Services** | Power Apps, Microsoft Dataverse, Power Fx |

## What you will build

A canvas app with a formatted, sorted gallery over the Booking Request table.

## Scenario

Build a canvas app from blank, add Dataverse as a data source, lay out the main screen and add a gallery bound to the Booking Request table with formatted fields.

## Prerequisites

- **Lab 06** completed — the Booking Request table must exist and hold the fifteen imported rows.
- The Kennel lookup must resolve, otherwise the gallery's related columns will render blank.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `booking-requests.csv` | The same fifteen rows imported in Lab 6, copied here so the lab folder is self-contained. If Lab 6's Dataverse import succeeded you do not need to import again - use this file only to check the gallery is showing every row in drop-off order. |

## Steps

1. Select + Create > Blank app > Blank canvas app, name it Booking Request, choose Tablet format and Create.

2. On the Data pane select + Add data, search for Booking Request and add the Dataverse table.

3. Insert a Label at the top of the screen; set its Text property to "Booking Requests" and increase the font size.

4. Insert a Vertical gallery and set its Items property to the Booking Request table.

   ```powerfx
   Sort(BookingRequests, 'Drop Off', Ascending)
   ```

5. Set the gallery layout to Title, subtitle and body, then map Title to Pet Name and Subtitle to Owner Name.

6. Add a Label inside the gallery template for the drop-off date and format it.

   ```powerfx
   Text(ThisItem.'Drop Off', "dd mmm yyyy")
   ```

7. Add a Label showing the daily rate formatted as currency.

   ```powerfx
   Text(ThisItem.Rate, "[$-en-US]$#,##0.00")
   ```

8. Preview the app and confirm the gallery lists every seeded booking in drop-off order.

## Verify

The gallery lists the Dataverse rows sorted by drop-off date, with dates and currency correctly formatted.

## Troubleshooting

**Problem — The gallery shows "Sort" as an error — `Sort(BookingRequests, 'Drop Off', Ascending)` is red.**

*Fix:* The data-source name in Power Fx is the table's **plural display name** as added to the app, which for a table named *Booking Request* is usually `'Booking Requests'` with quotes. Delete the formula, retype `Sort(` and pick the table from IntelliSense rather than typing the name, then pick the column the same way.

**Problem — A blue delegation warning appears on the gallery and only some rows show.**

*Fix:* `Sort` is delegable to Dataverse but only on sortable columns. If the warning persists, sort on a simple date or text column rather than a lookup or a calculated column. This is the same class of problem you diagnose deliberately in Lab 26 — note it now.

**Problem — The currency label shows `48` instead of `$48.00`.**

*Fix:* The format string is being applied to a text value, or the Rate column imported as text. Confirm Rate is a **Currency** column in Dataverse, then use `Text(ThisItem.Rate, "[$-en-US]$#,##0.00")`. If you want the SGD symbol, use `"S$" & Text(ThisItem.Rate, "#,##0.00")` — Power Fx takes the currency symbol from the format string, not from the environment.

---

**Next:** [Lab 08 — Build and Theme the User Interface](../lab-08-build-and-theme-the-user-interface/README.md)
