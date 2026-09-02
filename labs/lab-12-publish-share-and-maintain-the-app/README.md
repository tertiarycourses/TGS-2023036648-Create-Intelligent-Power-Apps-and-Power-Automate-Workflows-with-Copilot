# Lab 12 — Publish, Share and Maintain the App

| | |
|---|---|
| **Learning Unit** | LU2 — Create and Manage Canvas Apps with Power Apps |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A6/A8 — Verify the app functions for other users and manage its versions and permissions. |
| **Duration** | 35 minutes |
| **Services** | Power Apps, Microsoft Entra ID, Dataverse |

## What you will build

A published, shared and exported canvas app with a documented version history.

## Scenario

Publish the canvas app, share it with colleagues at the right permission level, review and restore versions, and export the app package for another environment.

## Prerequisites

- **Labs 07 to 10** completed — you publish and share the finished Booking Request app.
- A **second training account** in the same tenant to share with. Your trainer will pair you up.
- The outcome of this lab feeds fault **F-03** in Lab 26 — keep a note of who you shared with.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `sharing-matrix.csv` | Eight sharing scenarios pairing an app permission with a Dataverse permission and the outcome each combination produces. Rows 3 and 4 are the ones that fail - they are the source of the TSC A7 issue report and of fault F-03 in Lab 26. |

## Steps

1. In the maker portal open Apps, select the Booking Request app and choose Publish, then Publish this version.

2. Select Share, add another training account, and grant Can use (not Co-owner) to test least privilege.

3. Note the data source permission warning — sharing the app does not share the underlying Dataverse rows.

4. Open Details > Versions, review the version list and use Restore to roll back to an earlier version.

5. Select Export package, choose Create as new for the app, and download the .zip package.

6. Record the app's URL from Details and open it in a private browser window signed in as the shared user.

7. Confirm the shared user can open the app and, if their Dataverse permission is missing, capture the error as the TSC A7 issue report.

## Verify

The published app opens from its own URL for a second signed-in user, the version history shows a restore, and the exported .zip downloads.

## Troubleshooting

**Problem — The **Share** dialog cannot find the second training account.**

*Fix:* Search by the full user principal name (`someone@yourtenant.onmicrosoft.com`) rather than the display name. Guest accounts and accounts without a Power Apps licence will not resolve at all — that is the last row in `sharing-matrix.csv`.

**Problem — The shared user opens the app URL and sees "You do not have permission to use this app".**

*Fix:* The share did not save, or they are signed in with a different account. Confirm the user appears under **Apps > Booking Request > Share**, and have them open the URL in an InPrivate window so the browser does not silently reuse another identity.

**Problem — The shared user opens the app but the gallery is empty.**

*Fix:* This is the expected result and the point of the lab: sharing the app does not share the data. Capture the error as your TSC A7 issue report — it becomes fault **F-03** in Lab 26, fixed by assigning a Dataverse security role in the Power Platform admin centre.

---

**Next:** [Lab 13 — Create Cloud Flows — Template, Copilot and Blank](../lab-13-create-cloud-flows-template-copilot-and-blank/README.md)
