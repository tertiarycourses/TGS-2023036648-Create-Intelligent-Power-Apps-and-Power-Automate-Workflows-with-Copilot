# Lab 02 — Use Copilot to Build a Canvas App from a Description

| | |
|---|---|
| **Learning Unit** | LU1 — Get Started with Copilot for Microsoft Power Platform |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A1/A3 — Use Copilot to turn a natural-language need into a working app over a generated data structure. |
| **Duration** | 45 minutes |
| **Services** | Power Apps, Copilot for Power Apps, Dataverse |

## What you will build

A Copilot-generated canvas app over a Dataverse table, with the generated data structure reviewed and corrected.

## Scenario

Describe an app in plain English and let Copilot propose a data structure and screens. Iterate on the proposed table, then let Copilot generate the app and inspect what it produced.

## Prerequisites

- **Lab 01** completed — you must already be in the correct environment with Dataverse available.
- Copilot for Power Apps enabled in the environment (verified at the end of Lab 01).
- `mock-data/training-requests.csv` open alongside the browser so you can type a record from it.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `training-requests.csv` | Twelve training requests in SGD. Columns match the table Copilot generates from the Lab 2 prompt, including the TrainingProvider and WSQFunded columns you add with the refinement prompt. Use row 1 for the Preview test. |

## Steps

1. In make.powerapps.com select + Create, then choose Start with Copilot (the 'Describe it to design it' box).

2. Enter the prompt: I need an app to track employee training requests, including the employee name, course title, requested date, cost and approval status.

3. Review the data structure Copilot proposes. Rename any column that does not match the business language and set Cost to Currency and Requested Date to Date only.

4. Type a refinement prompt: add a column for the training provider and a Yes/No column for whether the course is WSQ funded.

5. Select Create app and wait for Copilot to generate the screens.

6. Open Preview (F5), add one record from mock-data/training-requests.csv, and confirm the record appears in the gallery.

7. Inspect the generated gallery's Items property to see the Dataverse table Copilot bound for you.

## Verify

The app opens in Preview, a record added in the form appears in the gallery, and the Dataverse table contains the two columns you added by prompt.

## Troubleshooting

**Problem — The **Start with Copilot** box is not on the Create page.**

*Fix:* Copilot is off for the environment or the region. Check **Power Platform admin centre > Environments > Dev One > Settings > Product > Features** and turn on the Copilot settings, then confirm the environment region supports Copilot. As a fallback, create a Dataverse table manually and generate the app from data — the rest of the lab still works.

**Problem — Copilot proposes a data structure but **Create app** fails or spins indefinitely.**

*Fix:* Usually a column name collision with a Dataverse reserved word (`Name`, `Status`, `Owner`, `Type`). Rename the offending column in the proposal — for example use *Approval Status* rather than *Status* — and create again.

**Problem — The refinement prompt adds the columns but the generated app does not show them.**

*Fix:* Copilot regenerated the table but not the form. Open the app, select the form, then **Edit fields > + Add field** and add *Training Provider* and *WSQ Funded* manually. Confirm the columns really exist in **Tables > your table > Columns** before assuming Copilot ignored the prompt.

---

**Next:** [Lab 03 — Build a Cloud Flow with Copilot for Power Automate](../lab-03-build-a-cloud-flow-with-copilot-for-power-automate/README.md)
