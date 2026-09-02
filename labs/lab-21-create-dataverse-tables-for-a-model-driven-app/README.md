# Lab 21 — Create Dataverse Tables for a Model-Driven App

| | |
|---|---|
| **Learning Unit** | LU4 — Model-Driven Apps with Power Apps and Dataverse |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A1/A3 — Model the business domain as Dataverse tables, columns and relationships. |
| **Duration** | 40 minutes |
| **Services** | Power Apps, Microsoft Dataverse |

## What you will build

A two-table Dataverse data model with a relationship and seeded property records.

## Scenario

Working the Contoso Real Estate scenario, create Property and Listing Agent tables with typed columns, a choice column and a lookup relationship, then seed them with data.

## Prerequisites

- **Lab 01** completed — Dataverse available in the environment.
- Maker permission to create tables. This is a fresh scenario (Contoso Real Estate) independent of the LU2 pet-boarding data.
- This data model is used by **Labs 22, 23, 24 and 25**.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `listing-agents.csv` | Six Contoso Real Estate agents with Singapore mobile numbers. Import this FIRST - the Listing Agent lookup in properties.csv will not resolve until these rows exist. |
| `properties.csv` | Eighteen Singapore properties across Tanjong Pagar, Bukit Timah, Punggol, Jurong East and other districts. Twelve Residential and six Commercial; eleven Available, four Under Offer and three Sold. Every ListingAgent value matches an AgentName in listing-agents.csv, three properties per agent. |

## Steps

1. In make.powerapps.com select Tables > + New table > Table (advanced properties) and create Property with the primary column Property Name.

2. Add Address (single line of text), Asking Price (currency), Bedrooms (whole number) and Listed On (date only).

3. Add a Choice column Property Type with the options Residential and Commercial.

4. Add a Choice column Status with the options Available, Under Offer and Sold, default Available.

5. Create a second table Listing Agent with the primary column Agent Name and columns Email and Phone.

6. In Property add a Lookup column Listing Agent pointing at the Listing Agent table.

7. Open each table's Data tab and import mock-data/properties.csv and mock-data/listing-agents.csv.

8. Open a property row and confirm the lookup resolves to the correct agent.

## Verify

Both tables show imported rows, the choice columns render as dropdowns, and each Property row links to a Listing Agent.

## Troubleshooting

**Problem — The `properties.csv` import maps Listing Agent to blank on every row.**

*Fix:* Import `listing-agents.csv` **first**. A lookup can only match rows that already exist, and the import wizard needs you to choose *Agent Name* as the column to match on. Re-run the properties import after the agents are in.

**Problem — Asking Price imports but shows as 0, or the import warns about the currency.**

*Fix:* A Currency column in Dataverse also needs a transaction currency on the row. Set the environment's base currency to SGD (**Settings > Business > Currencies**) before importing, and supply the price as a plain number with no `$`, no `S$` and no thousands separators — exactly as `properties.csv` has it.

**Problem — The Status choice column shows blank for the Under Offer rows.**

*Fix:* The label must match exactly, including the space. Create the options as `Available`, `Under Offer` and `Sold`. If you created *UnderOffer* without the space, rename the option label — the internal value is unaffected and the imported rows will resolve on re-import.

---

**Next:** [Lab 22 — Build a Model-Driven App](../lab-22-build-a-model-driven-app/README.md)
