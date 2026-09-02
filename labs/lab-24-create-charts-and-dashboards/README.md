# Lab 24 — Create Charts and Dashboards

| | |
|---|---|
| **Learning Unit** | LU4 — Model-Driven Apps with Power Apps and Dataverse |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A6 — Visualise integrated data to verify the platform is reporting correctly. |
| **Duration** | 40 minutes |
| **Services** | Power Apps, Dataverse charts and dashboards |

## What you will build

Two Dataverse charts and a dashboard surfaced in the model-driven app.

## Scenario

Build charts over the Property table and assemble them into an interactive dashboard inside the model-driven app.

## Prerequisites

- **Lab 21** completed — the charts aggregate the eighteen seeded property rows.
- **Lab 22** completed — the dashboard is added as a page in that app.
- A solution to hold the dashboard. Create one now, or create it in **Lab 25** and add the dashboard afterwards.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `chart-definitions.csv` | Four charts to build on the Property table, with the legend (series), horizontal axis (category) and aggregate for each. The lab requires the first two; the last two are extension work for the dashboard. |
| `expected-chart-values.csv` | The exact counts, sums and averages every chart must display, computed from the eighteen rows in Lab 21's properties.csv. Self-check: if your Properties by Status chart does not read 11 / 4 / 3, your import is incomplete. |

## Steps

1. Open the Property table > Charts and select + New chart.

2. Create a column chart named Properties by Status with the legend Count of Property Name and the horizontal axis Status.

3. Create a second chart Average Price by Type using Avg of Asking Price on the legend and Property Type on the axis.

4. Save and publish both charts, then open the app and use the chart pane beside the Property view.

5. In the maker portal select Solutions > your solution > + New > Dashboard > 2-column overview.

6. Add both charts plus a list of Available Properties to the dashboard and name it Sales Overview.

7. Save and publish, then add the dashboard as a page in the model-driven app's navigation.

8. Play the app and select a column in the chart to cross-filter the list beneath it.

## Verify

Both charts render real counts and averages, and selecting a chart segment in the dashboard filters the associated list.

## Troubleshooting

**Problem — **Average Price by Type** shows the count rather than the average.**

*Fix:* The aggregate is chosen on the series (legend) field, not on the axis. Open the series and change the aggregate from *Count (All)* to *Avg*. Against the seeded data the correct values are SGD 2,569,583.33 for Residential and SGD 4,255,000.00 for Commercial — `expected-chart-values.csv` lists them so you can self-check.

**Problem — The chart renders but the numbers do not match `expected-chart-values.csv`.**

*Fix:* Your import is incomplete or the view behind the chart is filtered. Charts aggregate over the **current view**, not the whole table — switch the grid to *All Properties* before reading the chart. Then confirm the table holds exactly 18 rows; Properties by Status must read 11 Available, 4 Under Offer and 3 Sold.

**Problem — Selecting a chart column does not cross-filter the list beneath it.**

*Fix:* Cross-filtering works on an **interactive dashboard** or on the chart pane beside a view, not on a plain 2-column overview dashboard containing static chart components. Add the chart from the view's chart pane, or build the dashboard so the list and the chart are both bound to the same Property view.

---

**Next:** [Lab 25 — Manage Solutions and Move to Another Environment](../lab-25-manage-solutions-and-move-to-another-environment/README.md)
