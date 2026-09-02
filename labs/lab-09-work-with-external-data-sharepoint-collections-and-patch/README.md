# Lab 09 — Work with External Data — SharePoint, Collections and Patch

| | |
|---|---|
| **Learning Unit** | LU2 — Create and Manage Canvas Apps with Power Apps |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3/A4 — Integrate a second data source and write to it through API-level functions. |
| **Duration** | 50 minutes |
| **Services** | Power Apps, SharePoint Online, Power Fx, Office 365 Users |

## What you will build

A canvas app reading and writing both Dataverse and a SharePoint list, using a collection and Patch.

## Scenario

Create a SharePoint list, add it to the app as a second data source, load data into an in-memory collection, and use Patch to write status changes back to the list.

## Prerequisites

- **Lab 07** completed — you add a second data source to the same app.
- Permission to create a SharePoint team site and a list in it.
- **Lab 06**'s Status choice options (Requested / Confirmed / Declined) — mirror them exactly in the SharePoint choice column so the `Patch` calls in this lab work.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `kennel-bookings.csv` | Twelve rows in SharePoint list import shape - Title is the list's built-in primary column and holds the pet name. Import with Edit in grid view or Import from CSV. Status values match the Requested/Confirmed/Declined choice column you create. |

## Steps

1. In Microsoft 365 create a SharePoint team site named Pet Boarding, then create a list named Kennel Bookings.

2. Add the columns Pet Name (text), Owner (text), Status (choice: Requested/Confirmed/Declined) and Rate (currency); import mock-data/kennel-bookings.csv.

3. In the canvas app select + Add data > SharePoint, supply the site URL and select the Kennel Bookings list.

4. Insert a second gallery and set its Items to the SharePoint list.

   ```powerfx
   SortByColumns('Kennel Bookings', "Title", Ascending)
   ```

5. Add a button labelled Load and set its OnSelect to build an in-memory collection.

   ```powerfx
   ClearCollect(colBookings, 'Kennel Bookings')
   ```

6. Add a Decline button in the gallery template and set OnSelect to patch the selected row's status.

   ```powerfx
   Patch('Kennel Bookings', ThisItem, {Status: {Value: "Declined"}})
   ```

7. Add a Confirm button that patches the status to Confirmed.

   ```powerfx
   Patch('Kennel Bookings', ThisItem, {Status: {Value: "Confirmed"}})
   ```

8. Preview, confirm one booking and decline another, then check the SharePoint list to verify both writes.

## Verify

The SharePoint list shows the status values changed by the Confirm and Decline buttons, and colBookings appears under Variables > Collections.

## Troubleshooting

**Problem — The SharePoint list does not appear when you add the data source.**

*Fix:* Paste the **site** URL (ending at `/sites/PetBoarding`), not the list URL. If the site URL is right and the list is still missing, the list may be a *document library* or may live on a different site — the connector lists only lists on the exact site you supply.

**Problem — `Patch('Kennel Bookings', ThisItem, {Status: {Value: "Declined"}})` errors with "Invalid argument type".**

*Fix:* SharePoint choice columns need the record syntax with `Value`, but only if the column really is a Choice. If you created Status as a single line of text, the correct call is `Patch('Kennel Bookings', ThisItem, {Status: "Declined"})`. Check the column type in SharePoint before changing the formula.

**Problem — The gallery does not refresh after a Patch — the old status is still shown.**

*Fix:* `Patch` updates the record but the gallery may be bound to a stale collection. If the gallery's `Items` is `colBookings`, re-run `ClearCollect(colBookings, 'Kennel Bookings')` after the Patch, or bind the gallery directly to the list and add `Refresh('Kennel Bookings')` after the Patch in the same `OnSelect`.

---

**Next:** [Lab 10 — Write Data with Forms](../lab-10-write-data-with-forms/README.md)
