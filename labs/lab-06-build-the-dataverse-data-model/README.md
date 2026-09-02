# Lab 06 — Build the Dataverse Data Model

| | |
|---|---|
| **Learning Unit** | LU2 — Create and Manage Canvas Apps with Power Apps |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A1/A3 — Design tables, columns and a relationship as the integration point for apps and flows. |
| **Duration** | 45 minutes |
| **Services** | Power Apps, Microsoft Dataverse |

## What you will build

Two related Dataverse tables with a lookup relationship and seeded rows.

## Scenario

Create a Booking Request table in Dataverse with typed columns, then create a second table and join them with a lookup column so one row can reference another.

## Prerequisites

- **Lab 01** completed — Dataverse must be available in the environment.
- Maker permission to create tables (System Customizer role or higher).
- This lab creates the data model that **Labs 07, 09, 10, 12, 14, 15, 16, 18 and 26** all depend on. Do not skip it.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `kennels.csv` | Six kennels with capacities. Import this FIRST - the Kennel lookup in booking-requests.csv cannot resolve until these rows exist. |
| `booking-requests.csv` | Fifteen pet-boarding requests in SGD. The Kennel column contains the exact KennelName values from kennels.csv so the lookup resolves on import. Status uses only Requested, Confirmed and Declined - the three choice options you create. |

## Steps

1. In make.powerapps.com select Tables > + New table > Table (advanced properties).

2. Enter Booking Request as the Display name; on the Primary column tab enter Pet Name, then Save.

3. Add a column Owner Name — Single line of text — and set Required to Business required.

4. Add Drop Off — Date and time, and Pick Up — Date and time.

5. Add a Choice column Status with the options Requested, Confirmed and Declined, default Requested.

6. Create a second table Kennel with the primary column Kennel Name and a Whole number column Capacity.

7. In Booking Request add a Lookup column named Kennel that points at the Kennel table — this is the relationship.

8. Open each table's Data tab and import the rows from mock-data/booking-requests.csv and mock-data/kennels.csv.

## Verify

Booking Request shows the imported rows, the Status choice renders as a dropdown, and the Kennel lookup resolves to a Kennel row.

## Troubleshooting

**Problem — The CSV import fails with "The column Kennel could not be mapped".**

*Fix:* Lookup columns cannot be imported by display name unless the target rows already exist. Import `kennels.csv` into the Kennel table **first**, then import `booking-requests.csv` and map the Kennel column to the Kennel lookup, choosing *Kennel Name* as the matching column.

**Problem — The Status choice column imports as blank on every row.**

*Fix:* The CSV text must match the choice **label** exactly, including case. Confirm your three options are spelled `Requested`, `Confirmed` and `Declined` with no trailing spaces. If you created them as *Pending / Approved / Rejected*, either rename the options or edit the CSV — but rename the options, because Labs 09, 14 and 16 all assume the original three.

**Problem — The Drop Off and Pick Up values shift by a day after import.**

*Fix:* The columns were created as *Date and time* with a time-zone behaviour of *User local*, and the CSV has no time component. For this data set set the behaviour to **Date only** (or *Time zone independent*) at creation — the behaviour cannot be changed after rows are imported, so delete the column and recreate it.

---

**Next:** [Lab 07 — Create a Canvas App over Dataverse](../lab-07-create-a-canvas-app-over-dataverse/README.md)
