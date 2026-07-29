# Lab 2 — Build a Scheduled Reminder and Diagnose a Controlled Failure

**Course:** PL-7002 Create and Manage Automated Processes by using Power Automate  
**Course Code:** C903  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Get Started with Power Automate  
**Maps to:** LO1: build a scheduled cloud flow, filter and iterate SharePoint records, update reminder state, diagnose a runtime expression failure, retest, and share maintenance ownership  
**Duration:** 30 minutes  
**Tools:** Power Automate scheduled flows · SharePoint Online · Office 365 Outlook

---

## Goal

Send one reminder for each due open request, prevent duplicate reminders, and prove that run history can locate and recover a deliberately introduced fault.

## What You Will Do

You will build a scheduled flow that finds open requests due today, sends one reminder, and marks each item so the next run does not resend it. You will insert a temporary divide-by-zero expression, use run history to find the first red action, restore the supplied divisor, retest the same expression, and share the flow with a trainer-designated co-owner for continuity.

## What You Will Build

A scheduled cloud flow named C903-02-Remind-Due-Requests, evidence rows for normal, empty, duplicate, and controlled-failure cases, and a recorded primary and backup owner

## Prerequisites

- Lab 1 is complete and C903 Process Requests contains the baseline data plus NW-1006.
- C903-Test-Evidence.csv is available in work-c903.
- Obtain the trainer-designated co-owner email; do not share with an unapproved account.
- The trainer has provisioned the inactive C903-02-Remind-Due-Requests starter from labs/assets/c903-starter-solution-package-v1.0.md with its named trigger, loop, Condition, Compose, email, and update placeholders already arranged.

> **Data note.** Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

## Steps

### 1. Update SharePoint item NW-1002 so Status is Open, DueDate is today, RequesterEmail is your training email, ReminderSent is No, and DiagnosticDivisor is 1. Set every other item to either a future DueDate or ReminderSent Yes.

```text
Controlled test state:
Qualifying rows = exactly 1
Qualifying RequestID = NW-1002
Expected first run = one reminder and ReminderSent changes to Yes
```

### 2. Open the inactive starter Scheduled cloud flow named C903-02-Remind-Due-Requests. Configure the existing Recurrence to every 1 day, Time zone to (UTC+08:00) Kuala Lumpur, Singapore, and start time to the next 4:00 pm Singapore slot. Confirm the trigger is named Daily_1600_SGT. Configure the existing SharePoint Get items Find_due_open_requests, Apply to each For_each_candidate, and Condition Due_date_is_today with the exact values below.

```text
Site Address: <TRAINING_SITE>
List Name: C903 Process Requests
Filter Query:
Status eq 'Open' and ReminderSent eq 0

Condition expression:
equals(
  formatDateTime(items('For_each_candidate')?['DueDate'],'yyyy-MM-dd'),
  formatDateTime(convertTimeZone(utcNow(),'UTC','Singapore Standard Time'),'yyyy-MM-dd')
)
```

### 3. In the matching branch, configure the existing Compose Runtime_diagnostic_check before the message to divide 1 by the current item's DiagnosticDivisor so a supplied zero becomes a runtime test fault rather than an invalid constant. Configure the existing Send an email (V2) Send_due_reminder and SharePoint - Update item Mark_reminder_sent. Map the current item's ID, required list fields, and set ReminderSent to Yes. Save, select Turn on, confirm the flow status is On, and use Test - Manually to execute the scheduled flow immediately.

```text
Runtime expression:
div(1,int(items('For_each_candidate')?['DiagnosticDivisor']))

Email subject: Due today - <RequestID> - <RequestTitle>
Body: Request <RequestID> is due today. Open the SharePoint item and update its status.

Evidence T02 expected:
one email for NW-1002; the SharePoint row changes ReminderSent from No to Yes.
```

### 4. Run the flow a second time without changing the list and record T03 as the duplicate-prevention case. Then set NW-1002 ReminderSent to No and DueDate to tomorrow, run again, and record T04 as the false-date case. Confirm the loop runs, Due_date_is_today is false, and no message or update action runs.

```text
Expected T03: Find_due_open_requests returns zero qualifying rows; zero reminder emails.
Expected T04: NW-1002 enters the loop but takes the false date branch; zero reminder emails.
These are separate evidence rows.
```

### 5. Set NW-1002 DueDate back to today, ReminderSent to No, and DiagnosticDivisor to 0. Run the flow and record T05: Runtime_diagnostic_check must be the first red action and no email is sent. Set DiagnosticDivisor to 1, open the failed run, select Resubmit, and record the successful recovery as T06. Open the flow details page, add the trainer-designated co-owner, and record the primary owner, backup owner, Outlook connection owner, and monitoring check in work-c903/C903-Ownership-Record.txt.

```text
Ownership record:
Flow: C903-02-Remind-Due-Requests
Primary owner: <YOUR_TRAINING_EMAIL>
Backup owner: <TRAINER_DESIGNATED_EMAIL>
Connection owner: <TRAINING_ACCOUNT>
Monitor: check the next scheduled run and investigate any red action
Recovery evidence: T05 runtime failure and T06 successful resubmission
```

## Test It

T02 must show one reminder and ReminderSent set to Yes for NW-1002. T03 must prove repeat-run duplicate prevention, and T04 must prove the false-date branch. T05 must identify Runtime_diagnostic_check as the first red action with DiagnosticDivisor 0; T06 must resubmit successfully after the divisor is restored to 1 and set ReminderSent to Yes. The final flow must be on and list the approved primary and backup owners.

## Checkpoint and Rejoin Point

Keep NW-1002 as Open with ReminderSent Yes and DiagnosticDivisor 1. Save the ownership record and T02-T06 evidence. Lab 3 reuses the SharePoint list and adds approval logic for High-priority requests. To rejoin, confirm Labs 1 and 2 flows are on and a repeated reminder run creates no duplicate message.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Get items returns more records than expected. | Inspect Status and ReminderSent values in SharePoint, verify the internal field types, and keep the date comparison inside the loop until the exact date format is confirmed. |
| Update item clears a required field. | Map the current item's ID and every required column in Update item. Inspect the action inputs before retrying. |
| The second run sends another reminder. | Confirm Mark_reminder_sent completed successfully, inspect the stored Yes/No value, and verify Find_due_open_requests filters ReminderSent eq 0. |

## Challenge

Replace the loop-level date Condition with a source-side date filter only after you verify the SharePoint internal column name and ISO date literal. Compare the number of retrieved rows and explain the efficiency trade-off.

## Reflection

How did the symptom tell you whether to inspect the trigger, the first red action, or the data mapping?

---

[← Lab 1](lab-01-validate-the-northwind-request-intake-and-create-an-automated-acknowledgement.md) · [Lab 3 →](lab-03-build-a-priority-approval-with-complete-outcome-and-recovery-paths.md)
