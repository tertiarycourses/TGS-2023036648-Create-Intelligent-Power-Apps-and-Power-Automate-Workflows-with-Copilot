# Lab 22 — Build a Model-Driven App

| | |
|---|---|
| **Learning Unit** | LU4 — Model-Driven Apps with Power Apps and Dataverse |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3 — Generate an application from the data model rather than drawing screens. |
| **Duration** | 35 minutes |
| **Services** | Power Apps, Microsoft Dataverse, modern app designer |

## What you will build

A running model-driven app with a two-area site map over the property data model.

## Scenario

Create a model-driven app in the modern app designer, add the Property and Listing Agent tables to its navigation, configure the site map, and run the app.

## Prerequisites

- **Lab 21** completed — both tables must exist and hold the imported rows.
- The Listing Agent lookup must resolve, or the generated main form will show a blank related record.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `properties.csv` | The same eighteen rows imported in Lab 21, copied here so the lab folder is self-contained. Use it to confirm the model-driven app's Property grid shows all eighteen rows, and pick a nineteenth property of your own to create from the app's + New command. |

## Steps

1. Select + Create > Blank app > Blank app based on Dataverse, name it Contoso Real Estate and select Create.

2. In the app designer select + Add page > Table based view and form, then choose the Property table.

3. Add a second table page for Listing Agent.

4. Open the Navigation pane, rename the group to Sales and reorder Property above Listing Agent.

5. Select Save, then Publish, then Play to open the running app.

6. In the running app open the Property area, select a row and observe the generated main form.

7. Create a new property record from the app's + New command and confirm it saves to Dataverse.

## Verify

The published app opens with Property and Listing Agent in the navigation, and a record created in the app appears in the Dataverse table.

## Troubleshooting

**Problem — **Blank app based on Dataverse** is not offered on the Create page.**

*Fix:* You are in an environment without a Dataverse database, or in the classic designer. Confirm the environment picker shows Dev One, then use **+ Create > Blank app > Blank app based on Dataverse > Create**. If the modern designer does not load, append `?pagetype=entitylist` diagnostics aside, simply clear the browser cache and retry — a stale designer bundle is a common cause.

**Problem — The Property page is added but the running app shows "No records found".**

*Fix:* Almost always the wrong view is selected, not missing data. In the app designer select the Property page and check which view it points at; if you have already built the filtered views from Lab 23, the default may be one that excludes your rows. Switch it to *Active Properties* and republish.

**Problem — Changes do not appear when you press **Play**.**

*Fix:* Model-driven apps serve the last **published** version. Save then Publish then Play — in that order — and if the running app is already open in another tab, hard-refresh it (Ctrl+F5). The Play button reuses the existing tab and its cached metadata.

---

**Next:** [Lab 23 — Configure Forms and Views](../lab-23-configure-forms-and-views/README.md)
