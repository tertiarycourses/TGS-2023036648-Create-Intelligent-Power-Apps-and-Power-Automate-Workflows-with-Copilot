# Lab 25 — Manage Solutions and Move to Another Environment

| | |
|---|---|
| **Learning Unit** | LU4 — Model-Driven Apps with Power Apps and Dataverse |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A8 — Package and ship middleware modifications between environments safely. |
| **Duration** | 45 minutes |
| **Services** | Power Apps, Dataverse solutions, Power Platform admin centre |

## What you will build

A managed solution package exported from Dev and imported into a second environment.

## Scenario

Create a publisher and an unmanaged solution, add the app, tables and flows to it, export it as managed, and import it into a second environment.

## Prerequisites

- **Labs 21 to 24** completed — the tables, app, charts and dashboard are the components you package.
- **Lab 14** completed — the approval flow ships in the same solution.
- A **second (Test) environment** you can import into. Ask the trainer if one has not been provisioned for you.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `solution-components.csv` | Twelve components with a yes/no decision and the reason. Use it as the checklist against the solution's Objects list before you export. The one No row is deliberate - the LU2 canvas app belongs to a different deliverable. |

## Steps

1. In make.powerapps.com select Solutions > + New solution and create a publisher with the prefix tic.

2. Name the solution Contoso Real Estate and set the publisher and version 1.0.0.0.

3. Select + Add existing and add the Property and Listing Agent tables, the model-driven app, the charts and the dashboard.

4. Add the approval flow from Lab 14 to the same solution so the automation ships with the app.

5. Review the solution's Objects list and confirm nothing is missing before export.

6. Select Export solution, choose Managed, and download the .zip package.

7. Switch to the second (Test) environment and select Solutions > Import solution, then upload the .zip.

8. Supply the connection references the import requests, then complete the import.

9. Open the imported app in the Test environment and confirm the components are read-only because the solution is managed.

## Verify

The managed solution imports into the second environment without errors and its components cannot be edited there.

## Troubleshooting

**Problem — **Export solution** is greyed out or warns about a missing publisher.**

*Fix:* The solution must have a real publisher with a prefix — the *Default Publisher* cannot be exported cleanly. Create a publisher with the prefix `tic`, set it on the solution, then export. Also make sure you are exporting the **unmanaged** source solution, not a managed one already imported.

**Problem — The import into the Test environment fails on missing dependencies.**

*Fix:* A component references something not in the package — typically a chart, a security role or an environment variable. Read the failure detail, then back in Dev use **+ Add existing** to include the named component and re-export. Work through `solution-components.csv` as your checklist; the charts and the dashboard are the two most commonly forgotten.

**Problem — The import succeeds but the flow is off and marked "Connection not configured".**

*Fix:* Managed solutions carry the connection **reference**, not the connection itself. Create a Dataverse connection in the Test environment, edit the connection reference to point at it, then turn the flow on. This is exactly fault **F-04** in Lab 26 — if the trainer seeded it, this is the symptom you are meant to see.

---

**Next:** [Lab 26 — Troubleshoot and Modify Power Platform Integrations](../lab-26-troubleshoot-and-modify-power-platform-integrations/README.md)
