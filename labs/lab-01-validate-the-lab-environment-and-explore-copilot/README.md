# Lab 01 — Validate the Lab Environment and Explore Copilot

| | |
|---|---|
| **Learning Unit** | LU1 — Get Started with Copilot for Microsoft Power Platform |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A1/A2 — Identify connection opportunities in Power Platform and scan the environment for feasibility. |
| **Duration** | 30 minutes |
| **Services** | Power Apps maker portal, Power Platform admin centre, Dataverse, Copilot |

## What you will build

A validated maker environment with a documented connector feasibility scan (mock-data/connector-scan.csv).

## Scenario

Sign in to the Power Apps maker portal, confirm you are in the correct environment, verify that Dataverse and the Copilot features are available, and take an inventory of the connectors your tenant can actually reach.

## Prerequisites

- A training account in the tenant, with a Power Apps licence assigned.
- The environment your trainer names (referred to throughout as **Dev One**) — you will use the same one in every lab.
- A browser signed in to Microsoft 365. No prior lab is required; this is the first lab.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `connector-scan.csv` | The TSC A2 feasibility-scan template. Ten connectors used across this course with their purpose, licence tier, connection status and the constraint that matters (premium licensing, DLP blocking, delegation limits). Overwrite the Status column with what your own tenant actually returns. |

## Steps

1. Open the Power Apps maker portal at make.powerapps.com and sign in with the training account the trainer assigns you.

2. Check the environment picker at the top right — select the Dev One (or trainer-assigned) environment. Every lab in this course uses the same one.

3. Select Tables in the left navigation and confirm Dataverse tables load. If they do not, the environment has no Dataverse database and the trainer must provision one.

4. Select Connections > + New connection and search for Excel Online (Business), SharePoint, Office 365 Users and Outlook. Create each connection.

5. Record each connector's status in mock-data/connector-scan.csv — this is your TSC A2 feasibility scan artefact.

6. Open a blank canvas app and confirm the Copilot pane appears. If it is hidden, enable it from Settings > Updates or the environment's Copilot setting.

## Verify

Tables load in the chosen environment, all four connections show Connected, and connector-scan.csv records the feasibility result for each.

## Troubleshooting

**Problem — The environment picker does not show Dev One, or shows only **Default**.**

*Fix:* Your account has not been added to that environment. In the Power Platform admin centre the trainer must open **Environments > Dev One > Settings > Users + permissions > Users** and add you with at least the Basic User security role. Refresh the maker portal fully (Ctrl+F5) — the picker is cached per session.

**Problem — **Tables** in the left navigation returns "There is no Dataverse database in this environment".**

*Fix:* The environment was created without a database. Only an admin can fix this: **Power Platform admin centre > Environments > Dev One > + Add database**. Provisioning takes a few minutes; nothing in Labs 02, 06 or 21 will work until it completes.

**Problem — Creating the Excel Online (Business) connection returns "Failed to create connection" or loops back to the sign-in prompt.**

*Fix:* This is nearly always a third-party-cookie or a conditional-access block. Try an InPrivate window with cookies allowed for `login.microsoftonline.com`, and confirm you are signing in with the **training account**, not a personal Microsoft account. If it still fails, check the tenant DLP policy — the connector may be in a blocked group, which you should then record in `connector-scan.csv` as a genuine feasibility finding.

---

**Next:** [Lab 02 — Use Copilot to Build a Canvas App from a Description](../lab-02-use-copilot-to-build-a-canvas-app-from-a-description/README.md)
