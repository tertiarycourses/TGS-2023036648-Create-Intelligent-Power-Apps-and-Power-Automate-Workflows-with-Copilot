# Lab 1 — Validate the Northwind Request Intake and Create an Automated Acknowledgement

**Course:** PL-7002 Create and Manage Automated Processes by using Power Automate  
**Course Code:** C903  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Get Started with Power Automate  
**Maps to:** LO1: create an automated cloud flow with a SharePoint trigger, explicit dynamic-content mapping, an Outlook notification, and traceable run evidence  
**Duration:** 35 minutes  
**Tools:** SharePoint Online · Power Automate cloud flows · Office 365 Outlook

---

## Goal

Validate the isolated request intake and prove that one new SharePoint item produces one acknowledgement containing the same RequestID.

## What You Will Do

You will inspect the pre-provisioned SharePoint list used throughout the course, verify five synthetic Northwind requests, and build an automated cloud flow that acknowledges every new request. You will rename the trigger and actions, map values deliberately, create a test request, and trace it from the SharePoint item through run history to the delivered message.

## What You Will Build

A validated per-learner SharePoint list named C903 Process Requests, an automated cloud flow named C903-01-Acknowledge-New-Request, and a saved evidence record for RequestID NW-1006

## Prerequisites

- Sign in to the trainer-designated Microsoft 365 and Power Platform environment.
- Use only your trainer-assigned isolated SharePoint site and C903 Process Requests list; every learner has a separate list.
- Confirm NW-1001 through NW-1005 are already loaded and you can send an email to your own training mailbox.
- Open labs/assets/process-requests.csv and labs/assets/request-schema.md; use only the supplied synthetic records.

> **Data note.** Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

## Steps

### 1. Create a local or approved OneDrive folder named work-c903. Copy labs/assets/test-evidence-template.csv into it and save the copy as C903-Test-Evidence.csv. Every test row you add must include your learner tag and its UTC test date; do not add a metadata row above the CSV header.

```text
Required evidence columns:
LearnerTag | TestDateUTC | TestID | Flow | RequestID | Input | Expected | Actual | RunTimeUTC | RunLinkOrTimestamp | Result | RecoveryNote
```

### 2. On your isolated training SharePoint site, open C903 Process Requests. Compare every column with request-schema.md, including ApprovalComments and DiagnosticDivisor. Confirm the five NW-1001 through NW-1005 rows match process-requests.csv. If the list or rows differ, stop and ask the trainer to restore the supplied provisioning package; do not rebuild a shared class list during the timed lab.

```text
Required columns:
RequestID - Single line of text
RequestTitle - Single line of text
RequesterEmail - Single line of text
Priority - Choice: Low, Normal, High
Status - Choice: New, Open, Pending Approval, Approved, More Info, Rejected, Scheduled, Closed, Automation Error
DueDate - Date only
ReminderSent - Yes/No, default No
ApprovalOutcome - Single line of text
ApprovalComments - Multiple lines of text
CalendarEventID - Single line of text
DataverseRowID - Single line of text
SQLAuditID - Number
DiagnosticDivisor - Number, default 1
```

### 3. In Power Automate, create an Automated cloud flow named C903-01-Acknowledge-New-Request. Choose SharePoint - When an item is created, select the training Site Address and C903 Process Requests, and rename the trigger New_request_received.

```text
Trigger contract:
Business event: one item is created
System of record: SharePoint C903 Process Requests
Correlation key: RequestID
Expected volume: classroom test records only
```

### 4. Add Data Operation - Compose, rename it Correlation_key, and set Inputs to RequestID dynamic content. Add Office 365 Outlook - Send an email (V2), rename it Send_acknowledgement, and map the fields exactly. Save the flow and resolve any connection prompt with the approved training account.

```text
To: RequesterEmail
Subject: Request received - <RequestID> - <RequestTitle>
Body:
Hello,
Northwind received request <RequestID>: <RequestTitle>.
Priority: <Priority>
Due date: <DueDate>
This is an automated training notification.
Correlation key: <output of Correlation_key>
```

### 5. Select Test - Manually, then create one new SharePoint item using the NW-1006 values below. Open the completed run, expand all three cards, and compare the trigger RequestID, Compose output, email inputs, and delivered message. Add test T01 to C903-Test-Evidence.csv.

```text
NW-1006 test record:
RequestTitle: Prepare weekly service summary
RequesterEmail: <YOUR_TRAINING_EMAIL>
Priority: Normal
Status: New
DueDate: <TOMORROW>
ReminderSent: No

Expected: exactly one successful run and one email; every occurrence of the correlation key is NW-1006.
```

## Test It

The isolated SharePoint list must contain NW-1001 through NW-1006 with the exact schema. A single new NW-1006 item must create one successful run. The trigger input, Correlation_key output, email subject, email body, and T01 evidence row must all contain NW-1006. The email must show the mapped title, priority, and due date and must not contain any unrelated list field.

## Checkpoint and Rejoin Point

Leave C903-01-Acknowledge-New-Request turned on and save C903-Test-Evidence.csv in work-c903. Lab 2 uses the same isolated list and adds reminder behaviour. If you need to rejoin, ask the trainer to restore the provisioned list from request-schema.md and process-requests.csv, then run the NW-1006 check.

## Troubleshooting

| If this happens | Fix |
|---|---|
| No run appears after the item is created. | Confirm the flow is on, the trigger points to the same site and list, and the item was newly created rather than edited. Wait for the connector polling interval, then inspect the trigger again. |
| The email action uses the wrong field. | Open the failed or incorrect run, compare the action input with the trigger output, remove the token, and reselect the exact dynamic-content field by its column name. |
| The training email does not arrive. | Verify Send_acknowledgement is green, inspect its To and Subject inputs, record the flow run timestamp, check the training mailbox junk folder, and match the delivered message subject and received time. Send an email (V2) does not provide a message ID output. |

## Challenge

Add a link to the SharePoint item in the email without hard-coding an item number. Explain which trigger output supplies the link and how the link remains tied to the same RequestID.

## Reflection

Which run-history value gives the strongest evidence that the email belongs to the correct request, and why?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-build-a-scheduled-reminder-and-diagnose-a-controlled-failure.md)
