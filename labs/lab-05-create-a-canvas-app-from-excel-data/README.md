# Lab 05 — Create a Canvas App from Excel Data

| | |
|---|---|
| **Learning Unit** | LU2 — Create and Manage Canvas Apps with Power Apps |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3 — Utilise a connector as middleware to integrate Excel data into an application. |
| **Duration** | 40 minutes |
| **Services** | Power Apps, Excel Online (Business), OneDrive for Business |

## What you will build

A three-screen canvas app (browse, detail, edit) over an Excel table in OneDrive.

## Scenario

Upload an Excel workbook to OneDrive for Business, connect Power Apps to its table through the Excel Online (Business) connector, and generate a three-screen canvas app from that data.

## Prerequisites

- **Lab 01** completed — the Excel Online (Business) connection must show Connected.
- OneDrive for Business provisioned for the training account (open it once from the app launcher so the drive is created).
- Python 3 and `openpyxl` if you want to regenerate the workbook; otherwise use the supplied `CoffeeMachineData.xlsx` as-is.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `CoffeeMachineData.csv` | Fifteen coffee machines across six Singapore office locations, with model, status, last-serviced date and daily cup count. Source data only - Power Apps does not read the CSV. |
| `make_xlsx.py` | Converts the CSV into CoffeeMachineData.xlsx using openpyxl, wrapping the rows in a formatted Excel table named CoffeeMachines. Run `pip install openpyxl && python3 make_xlsx.py` if you need to regenerate it. |
| `CoffeeMachineData.xlsx` | The workbook you upload to OneDrive for Business. It contains the named table CoffeeMachines - Power Apps can only bind to a named table, never to a bare worksheet range. |

## Steps

1. Open mock-data/CoffeeMachineData.xlsx from the lab folder and note the named table inside it — Power Apps can only bind to a formatted Excel table.

2. In the Power Apps maker portal select the App launcher, open OneDrive, then + Create or upload > Files upload and upload CoffeeMachineData.xlsx.

3. Return to make.powerapps.com, confirm the Dev One environment, and select + Create.

4. Choose the Excel Online (Business) tile under Start from data; a connection is created for you.

5. Expand OneDrive for Business > OneDrive > CoffeeMachineData.xlsx and select the table inside the workbook, then Create app.

6. Wait for the three generated screens — BrowseScreen1, DetailScreen1 and EditScreen1 — and rename the app Coffee Machines.

7. Press F5 to preview, select a record to open the detail screen, then edit and save it.

8. Reopen the workbook in OneDrive and confirm your edit was written back to the Excel row.

## Verify

The app previews with data from Excel, and an edit made in the app appears in the Excel workbook in OneDrive.

## Troubleshooting

**Problem — The Excel connector shows the workbook but the table list is empty.**

*Fix:* Power Apps binds only to a **named Excel table**, never to a worksheet or a plain range. Open the workbook, select the data, press Ctrl+T, tick *My table has headers*, then name the table `CoffeeMachines` in **Table Design > Table Name**. The supplied `CoffeeMachineData.xlsx` already has this; if you rebuilt it from the CSV yourself, run `make_xlsx.py` rather than saving a range.

**Problem — The workbook does not appear under **OneDrive for Business** in the data picker.**

*Fix:* Either it was uploaded to SharePoint rather than OneDrive, or OneDrive has not finished provisioning for the account. Open OneDrive once from the app launcher, confirm the file is in the root (not in a shared folder), wait a minute, then reopen the picker. Files in *Shared with me* are never listed.

**Problem — An edit made in the app does not appear in the workbook.**

*Fix:* Excel Online writes are eventually consistent and the workbook caches aggressively. Close the workbook completely and reopen it from OneDrive rather than refreshing the browser tab. If the write genuinely failed, check that the workbook is not open in the desktop Excel app with a file lock — the connector cannot write to a locked workbook and the app shows no error.

---

**Next:** [Lab 06 — Build the Dataverse Data Model](../lab-06-build-the-dataverse-data-model/README.md)
