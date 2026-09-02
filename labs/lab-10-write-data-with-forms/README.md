# Lab 10 — Write Data with Forms

| | |
|---|---|
| **Learning Unit** | LU2 — Create and Manage Canvas Apps with Power Apps |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3/A5 — Use Form controls to display, edit and create records, and verify each write. |
| **Duration** | 50 minutes |
| **Services** | Power Apps, Microsoft Dataverse, Power Fx |

## What you will build

A three-screen app with working display, edit, create and delete behaviour over Dataverse.

## Scenario

Add detail and edit screens, wire navigation between them, then use Display and Edit forms with SubmitForm and NewForm to read, update and create Dataverse records.

## Prerequisites

- **Lab 07** completed — the browse screen and its gallery must already exist.
- **Lab 06**'s Booking Request table, including the Business required setting on Owner Name (test case TC-03 depends on it).

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `form-test-cases.csv` | Ten form test cases covering the happy path, required-column failures, a currency format check and the Pick Up before Drop Off gap. Work through them in order in Preview and record any deviation - TC-06 is a deliberate platform gap to carry into Lab 26. |

## Steps

1. Add two screens named DetailScreen and EditScreen to the Booking Request app.

2. On the browse gallery's chevron set OnSelect to open the detail screen for the selected record.

   ```powerfx
   Navigate(DetailScreen, ScreenTransition.Cover)
   ```

3. On DetailScreen insert a Display form, set DataSource to Booking Request and Item to the gallery's selection.

   ```powerfx
   Gallery1.Selected
   ```

4. Add an Edit icon whose OnSelect navigates to EditScreen.

   ```powerfx
   Navigate(EditScreen, ScreenTransition.Cover)
   ```

5. On EditScreen insert an Edit form with the same DataSource and Item, then add a Save button.

   ```powerfx
   SubmitForm(Form2)
   ```

6. Set the Edit form's OnSuccess to return to the detail screen.

   ```powerfx
   Back()
   ```

7. Add a + New icon on the browse screen that opens a blank edit form.

   ```powerfx
   NewForm(Form2); Navigate(EditScreen)
   ```

8. Add a Delete icon on DetailScreen that removes the record and returns.

   ```powerfx
   Remove('Booking Requests', Gallery1.Selected); Back()
   ```

9. Preview: create a new booking, edit it, then delete it, checking the Dataverse table after each action.

## Verify

A record created in the app appears in Dataverse, an edit updates the same row, and Delete removes it — verified in the table's Data tab.

## Troubleshooting

**Problem — `SubmitForm(Form2)` appears to do nothing and no error is shown.**

*Fix:* A required card is failing validation silently. Add a label with `Form2.Error` (and check `Form2.Valid`) so the reason surfaces, then work through `form-test-cases.csv` — TC-02 and TC-03 are the two required-column failures this lab deliberately produces.

**Problem — The Edit form opens blank when you navigate from the gallery.**

*Fix:* The form's `Item` property is bound to the wrong control. It must reference the **browse gallery's** selection, `Gallery1.Selected`, not the detail form. If DetailScreen and EditScreen use different galleries, set both forms' `Item` to the same `Gallery1.Selected`.

**Problem — `Remove('Booking Requests', Gallery1.Selected)` fails with a permission or "record not found" error.**

*Fix:* Either the row was already deleted in another tab, or the account lacks Delete on the table. Check **Power Platform admin centre > Users > security roles** for a role with the Delete privilege on Booking Request. Add `Back()` only after the `Remove` succeeds — put them in one formula separated by `;` as shown, so navigation does not race the delete.

---

**Next:** [Lab 11 — Extend the App with a Code Component (PCF)](../lab-11-extend-the-app-with-a-code-component-pcf/README.md)
