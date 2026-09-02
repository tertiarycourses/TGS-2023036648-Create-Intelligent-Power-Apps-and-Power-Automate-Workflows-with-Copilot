# Lab 08 — Build and Theme the User Interface

| | |
|---|---|
| **Learning Unit** | LU2 — Create and Manage Canvas Apps with Power Apps |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A3/A6 — Build a consistent, branded UI and verify it renders correctly across screens. |
| **Duration** | 35 minutes |
| **Services** | Power Apps, Power Fx, Office 365 Users |

## What you will build

A themed, branded canvas app that greets the signed-in user by name.

## Scenario

Apply a theme to the app, brand individual controls, and personalise the screen with the signed-in user's details from the Office 365 Users connector.

## Prerequisites

- **Lab 07** completed — you extend the same Booking Request canvas app.
- **Lab 01** completed — the Office 365 Users connection must show Connected.
- A profile photo set on your training account, or be ready for `UserPhotoV2` to error (that is a teachable moment, not a mistake).

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `users.csv` | Eight training-tenant accounts. Use the Email values when testing Office365Users.UserPhotoV2 - accounts with no profile photo make the Image control error, which is exactly the case you wrap in IfError. |

## Steps

1. Open the Booking Request app for editing and select Settings > Theme; choose a theme and observe every control restyle.

2. Select the header label and set Fill, Color and Font individually to override the theme for that control.

3. Insert an Icon (for example the Home icon) into the header and set its Color to match the brand colour.

4. Add the Office 365 Users connector from the Data pane.

5. Insert a Label for the greeting and set its Text property to use the signed-in user's given name.

   ```powerfx
   "Welcome, " & User().FullName
   ```

6. Insert an Image control and bind it to the signed-in user's photo.

   ```powerfx
   Office365Users.UserPhotoV2(User().Email)
   ```

7. Group the header controls and set their X/Y so the layout holds when the screen resizes.

8. Preview and confirm the greeting and photo resolve for your training account.

## Verify

The app opens themed and branded, and the header greets the signed-in user by name with their profile photo.

## Troubleshooting

**Problem — The theme changes the controls but the header label keeps its old colour.**

*Fix:* Once you set `Fill` or `Color` explicitly on a control, that control opts out of the theme for that property. That is the point of the step — to see the override. To hand a control back to the theme, delete the property value so it returns to its inherited expression rather than typing the theme colour in by hand.

**Problem — `Office365Users.UserPhotoV2(User().Email)` shows a red error or a broken image.**

*Fix:* The account has no profile photo, and the connector throws rather than returning blank. Wrap it: `IfError(Office365Users.UserPhotoV2(User().Email), SampleImage)`. Also confirm the Office 365 Users connection is added to the app (Data pane), not merely created in the portal — they are separate steps.

**Problem — `User().FullName` returns blank in Preview.**

*Fix:* Preview occasionally resolves `User()` late. Press Ctrl+F5 to reload the studio, or re-open Preview. If it is still blank, use `Office365Users.MyProfileV2().displayName` instead — that is an explicit connector call rather than a context value, and it forces the lookup.

---

**Next:** [Lab 09 — Work with External Data — SharePoint, Collections and Patch](../lab-09-work-with-external-data-sharepoint-collections-and-patch/README.md)
