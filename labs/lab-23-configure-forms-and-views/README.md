# Lab 23 — Configure Forms and Views

| | |
|---|---|
| **Learning Unit** | LU4 — Model-Driven Apps with Power Apps and Dataverse |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3/A6 — Control what each user sees and edits, and verify the layout across the app. |
| **Duration** | 45 minutes |
| **Services** | Power Apps, Dataverse, form and view designers |

## What you will build

A customised main form with a quick view control, plus two custom public views.

## Scenario

Customise the Property main form with tabs, sections and a quick view of the related agent, then build filtered and sorted public views the app's users can select.

## Prerequisites

- **Lab 22** completed — you customise the forms and views that app surfaces.
- **Lab 21**'s Listing Agent table, since the quick view control binds to that lookup.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `view-definitions.csv` | Six public views to build against the Property table. The lab requires the first two; the rest are extension work. Against the eighteen seeded rows, Available Properties returns 11 rows and Commercial Listings returns 6. |

## Steps

1. Open the Property table > Forms and edit the Information main form.

2. Add a second tab named Financials and move Asking Price and Status onto it.

3. On the first tab add a two-column section and arrange Address, Bedrooms and Listed On.

4. Insert a Quick view control bound to the Listing Agent lookup so the agent's email and phone appear inline.

5. Save and Publish the form, then reopen the app and confirm the tabs render.

6. Open the Property table > Views and create a new public view named Available Properties.

7. Add a filter Status equals Available, sort by Asking Price descending, and choose the displayed columns.

8. Create a second view Commercial Listings filtered on Property Type equals Commercial, then Publish.

9. In the running app switch between the views using the view selector.

## Verify

The main form shows both tabs and the agent's details in the quick view, and both custom views appear in the app's view selector with the correct rows.

## Troubleshooting

**Problem — The quick view control shows nothing for the agent's email and phone.**

*Fix:* A quick view control needs a **quick view form** on the *target* table. Open the Listing Agent table > **Forms** > create a Quick View Form containing Email and Phone, publish it, then bind the quick view control on the Property form to the Listing Agent lookup and select that form. Without the quick view form on the related table the control renders empty rather than erroring.

**Problem — The new tab does not appear in the running app.**

*Fix:* Forms must be published separately from the app, and the form must be assigned to a security role. **Save > Publish** the form, then check **Form settings > Security roles** — a form restricted to roles you do not hold is invisible to you even as the maker.

**Problem — The new public view is not in the view selector.**

*Fix:* Either it was saved as a personal view, or it has not been published. Create it from the **Views** area of the table (not with *Save filters as new view* in the grid), then **Publish**. Personal views appear in a separate *My views* section and cannot be shared this way.

---

**Next:** [Lab 24 — Create Charts and Dashboards](../lab-24-create-charts-and-dashboards/README.md)
