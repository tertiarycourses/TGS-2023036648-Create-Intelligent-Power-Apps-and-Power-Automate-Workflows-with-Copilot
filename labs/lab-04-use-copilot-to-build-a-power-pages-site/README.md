# Lab 04 — Use Copilot to Build a Power Pages Site

| | |
|---|---|
| **Learning Unit** | LU1 — Get Started with Copilot for Microsoft Power Platform |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A1/A4 — Generate an external-facing site and connect it to Dataverse data through its API layer. |
| **Duration** | 45 minutes |
| **Services** | Power Pages, Copilot for Power Pages, Dataverse |

## What you will build

A published Power Pages site with a Dataverse-backed page and a working form.

## Scenario

Describe a public-facing site to Copilot in Power Pages, review the theming, pages and AI-generated content it produces, then add a Dataverse-backed form so the site reads and writes real data.

## Prerequisites

- **Lab 02** completed — the Dataverse table Copilot generated is the table this site binds to.
- A Power Pages trial or licence in the same environment.
- Rights to create a site in the environment. If **+ Create a site** is greyed out, the trainer must grant the Power Pages maker role.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `courses.csv` | Eight WSQ courses with SGD fees and seat counts. Import into the Dataverse table behind the Power Pages site so the public course list has something to render, and so the request form has a real course to point at. |

## Steps

1. Open make.powerpages.microsoft.com and select + Create a site.

2. Describe the site to Copilot: a site where staff can browse available training courses and submit a request to attend.

3. Review the pages, theme and AI-generated images Copilot proposes; edit the site name and the hero heading.

4. Select Edit site, then use the Data workspace to add a list bound to the Dataverse table you created in Lab 2.

5. Add a form component to the request page bound to the same table, and set its mode to Insert.

6. Set the page permissions so anonymous users can read the course list but must sign in to submit a request.

7. Preview the site and submit one request; confirm the row lands in the Dataverse table.

## Verify

The previewed site lists courses from Dataverse and a submitted request creates a new row in the Dataverse table.

## Troubleshooting

**Problem — **+ Create a site** is greyed out, or the site creation fails with a capacity error.**

*Fix:* Power Pages needs an available site capacity in the environment, and you need the *Power Pages maker* role. Ask the trainer to check **Power Platform admin centre > Resources > Power Pages sites**; trial tenants are commonly capped at one or two sites, so an existing site may need deleting first.

**Problem — The list or form component shows "No data" even though the Dataverse table has rows.**

*Fix:* Table permissions, not data. In the **Set up** workspace open **Table permissions**, create a permission for the table with the *Read* (and *Create* for the form) privileges, and attach it to the **Anonymous Users** or **Authenticated Users** web role. A Power Pages component always renders empty until a table permission grants access — it does not error.

**Problem — The submitted form returns "You do not have permission to perform this action".**

*Fix:* The form's table permission is missing the *Create* privilege, or the page requires sign-in but the web role has no permission attached. Set the permission to *Global* scope with Read and Create, attach it to Authenticated Users, then **Sync configuration** and restart the site preview — permission changes are not picked up until the site restarts.

---

**Next:** [Lab 05 — Create a Canvas App from Excel Data](../lab-05-create-a-canvas-app-from-excel-data/README.md)
