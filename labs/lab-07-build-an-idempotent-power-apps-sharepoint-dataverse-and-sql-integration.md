# Lab 7 — Build an Idempotent Power Apps, SharePoint, Dataverse, and SQL Integration

**Course:** PL-7002 Create and Manage Automated Processes by using Power Automate  
**Course Code:** C903  
**Version:** v1.0 (29 July 2026)  
**Topic 4:** Power Automate's Deep Integration Across Multiple Data Sources  
**Maps to:** LO4: invoke a flow from Power Apps, require one SharePoint request, enforce a Dataverse duplicate guard, react to the Dataverse add event, write one SQL audit row, and reconcile all identifiers  
**Duration:** 45 minutes  
**Tools:** Power Apps · SharePoint Online · Microsoft Dataverse · SQL Server connector · Power Automate solutions

---

## Goal

Submit NW-1009 from the canvas app and prove that the same RequestID links exactly one SharePoint item, one Dataverse row and one SQL audit row across three expected runs: 07A Created, 07B Added, and 07A Existing.

## What You Will Do

You will use per-learner SharePoint, Dataverse, canvas-app, and SQL resources prepared by the trainer. The Power Apps flow rejects zero or multiple SharePoint matches and returns an existing Dataverse row instead of creating a duplicate. A Dataverse-added flow inserts one SQL audit row and writes the target identifiers back to SharePoint. The app disables its button while a submission is running.

## What You Will Build

Two solution-aware guarded cloud flows, a bound C903 Request Launcher app, exactly one Dataverse and SQL row for NW-1009, and a complete supplied-header correlation record

## Prerequisites

- Use only the trainer-assigned isolated SharePoint site, Power Platform environment, calendar, and SQL database.
- The trainer has provisioned C903 Northwind Automation, the active Request ID alternate key, and the C903 Request Launcher app shell.
- The same solution contains inactive 07A and 07B starter flows from labs/assets/c903-starter-solution-package-v1.0.md with the named triggers, actions, Try_write_audit/Catch_audit_error/Finally_record_run scopes, and connection-reference placeholders already arranged; complete their exact guards, mappings, formulas, and run-after settings rather than building every card from a blank canvas during this 45-minute lab.
- Your learner and trainer accounts have the required Power Apps/Power Automate premium entitlement for Dataverse and SQL, and the environment DLP policy permits the documented connectors together.
- C903 Training SQL is a trainer-owned premium connection reference to your isolated database; gateway and network health are green.
- Your training identity has permission to run the supplied DDL script and insert/select only dbo.C903AutomationAudit; it has no broader production access.
- Copy the supplied correlation-register template and keep its header unchanged.

> **Data note.** Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

## Steps

### 1. Open labs/assets/setup-automation-audit.sql in the approved training SQL editor, confirm the selected database name and learner tag with the trainer, execute the idempotent script once, and run the final queries. Confirm the table exists, the index query returns UX_C903AutomationAudit_Request_Event with IsUnique 1, and no NW-1009 row exists. Stop and ask the trainer to repair the package if the unique index is absent. Do not enter or record a connection string.

```text
Required SQL columns:
AuditID | RequestID | DataverseRowID | EventType | EventTimeUTC | FlowRunNote | CreatedUTC

Preflight query:
SELECT RequestID, COUNT(*) AS RowCount
FROM dbo.C903AutomationAudit
WHERE RequestID = N'NW-1009'
GROUP BY RequestID;

Expected before the test: zero returned groups.
```

### 2. In C903 Northwind Automation open the inactive starter Instant cloud flow C90307A_PowerApps_Submit_Request with Power Apps (V2) required Text input RequestID. Configure the existing SharePoint Get items Find_source_request with the Filter Query shown below and Condition Exactly_one_source. In its false branch configure Respond to a Power App or flow Respond_source_count_error. In the true branch configure Dataverse List rows Find_existing_lifecycle_row and Condition Lifecycle_row_missing.

```text
SharePoint Filter Query:
RequestID eq '<Power Apps RequestID token>'
Exactly_one_source:
equals(length(body('Find_source_request')?['value']),1)

Dataverse Table: C903 Automation Requests
Filter rows using provisioned logical name:
c903_requestid eq '<Power Apps RequestID token>'
Lifecycle_row_missing:
equals(length(body('Find_existing_lifecycle_row')?['value']),0)

Count-error response: message='RequestID must match exactly one SharePoint item'; dataverseRowID=''; state='Rejected'.
```

### 3. In Lifecycle_row_missing Yes, configure the existing Dataverse Add a new row Create_lifecycle_row with the exact field map, then SharePoint Update item Persist_dataverse_ID with the current numeric item ID and every required list field, and Respond to a Power App or flow Respond_created. In No, configure Respond_existing using the first returned Dataverse row ID and create nothing.

```text
Dataverse mapping:
Request ID <- Power Apps RequestID
Request Title, Requester Email, Priority, Due Date, SharePoint Item ID, Diagnostic Divisor <- first SharePoint row
Request Status <- Open

Persist_dataverse_ID must preserve RequestID, RequestTitle, RequesterEmail, Priority, Status, DueDate, ReminderSent, ApprovalOutcome, ApprovalComments, CalendarEventID, SQLAuditID, and DiagnosticDivisor, and set DataverseRowID = the Row ID returned by Create_lifecycle_row.

Respond_created: message='Created <RequestID>'; dataverseRowID=<new GUID>; state='Created'
Respond_existing: message='Existing <RequestID>'; dataverseRowID=<first existing GUID>; state='Existing'
```

### 4. In the same solution open the inactive starter Automated cloud flow C90307B_Audit_Dataverse_Request with Dataverse When a row is added, modified or deleted: Change type Added, Table C903 Automation Requests, Scope Organization. Inside Try_write_audit configure SharePoint Get items Find_source_for_audit with your assigned training Site Address, list C903 Process Requests, and Filter Query RequestID eq '<Dataverse Request ID token>', then Condition Exactly_one_audit_source. Only in Yes configure Scope Write_audit_targets containing SQL Server Insert row (V2) Insert_audit_row and the SharePoint update with DataverseRowID, returned AuditID, and Status Open. In No send one internal count alert and Terminate Cancelled C903_AUDIT_SOURCE_COUNT without inserting an audit row.

```text
SQL mapping:
RequestID <- Dataverse Request ID
DataverseRowID <- Dataverse row unique identifier
EventType <- Dataverse Added
EventTimeUTC <- utcNow()
FlowRunNote <- C90307B isolated training integration

Exactly_one_audit_source:
equals(length(body('Find_source_for_audit')?['value']),1)
SharePoint update preserves RequestID, RequestTitle, RequesterEmail, Priority, Status, DueDate, ReminderSent, ApprovalOutcome, ApprovalComments, CalendarEventID, DataverseRowID, and DiagnosticDivisor, and sets only SQLAuditID to the Insert row AuditID.
```

### 5. Open the pre-provisioned C903 Request Launcher app shell. Add 07A from the Power Automate pane. Set the exact formulas, save, and publish. Save both 07A and 07B, select Turn on for each, and confirm both flow statuses are On before invoking the app. Create NW-1009 in your isolated SharePoint list with DiagnosticDivisor 1, play the app, select Submit once, observe that the button becomes disabled, and try to select it again while the first call is still running; the disabled control must prevent the second selection from starting another call. After the first call completes, select Submit once more to exercise the server-side Existing path. Before querying, open 07B run history, identify the NW-1009 Dataverse Added run, and refresh every 10 seconds for at most 2 minutes until its status is Succeeded. If it is still Running after 2 minutes, stop the test, record the run URL and timestamp, and escalate to the trainer; do not record a transient SQL count. After terminal success, record T23, query the three systems, and append one row using the unchanged correlation header.

```text
txtRequestID.Default = "NW-1009"
btnSubmit.DisplayMode = If(varSubmitting,DisplayMode.Disabled,DisplayMode.Edit)
btnSubmit.OnSelect = Set(varSubmitting,true);IfError(Set(varResult,C90307A_PowerApps_Submit_Request.Run(txtRequestID.Text)),Notify("Submission error",NotificationType.Error));Set(varSubmitting,false)
lblResult.Text = varResult.message & " | Dataverse: " & varResult.dataverseRowID

NW-1009: Automate customer escalation handoff | <YOUR_TRAINING_EMAIL> | High | New | due in 7 days | ReminderSent No | DiagnosticDivisor 1

SQL count query:
SELECT RequestID, COUNT(*) AS RowCount FROM dbo.C903AutomationAudit WHERE RequestID=N'NW-1009' GROUP BY RequestID;

Correlation header:
RequestID | SharePointItemID | DataverseRowID | CalendarEventID | SQLAuditID | Flow07ACreatedRunTimeUTC | Flow07AExistingRunTimeUTC | Flow07BInitialRunTimeUTC | Flow07BRecoveryRunTimeUTC | State

Record the first 07A Created run in Flow07ACreatedRunTimeUTC, the repeated 07A Existing run in Flow07AExistingRunTimeUTC, and the single Dataverse-added 07B run in Flow07BInitialRunTimeUTC. Leave Flow07BRecoveryRunTimeUTC blank for NW-1009.
```

## Test It

T23 must show one SharePoint NW-1009, one Dataverse row by the active Request ID alternate key, and one SQL row by the count query. The first app response is Created and any repeated submission is Existing with the same Dataverse GUID; no second Dataverse trigger or SQL row occurs. SharePoint DataverseRowID and SQLAuditID must match the targets. Evidence must show exactly three relevant runs (07A Created, 07B Added, 07A Existing), the app button must disable while varSubmitting is true, and the correlation register must use all ten supplied columns. The SQL count is recorded only after the NW-1009 07B run reaches terminal Succeeded.

## Checkpoint and Rejoin Point

Leave both solution-aware flows on, the app published, and NW-1009 Reconciled with counts 1/1/1. Lab 8 adds recovery and handover around 07B. To rejoin, repeat the app submission and confirm Existing plus unchanged Dataverse and SQL counts.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Power Apps does not recognise the flow or response fields. | Confirm the app and flow share the same isolated environment, remove and re-add the flow from the Power Automate pane, and let Power Apps insert the Run reference. |
| A repeated submission creates another Dataverse row. | Stop 07A, verify the active Request ID alternate key, inspect Find_existing_lifecycle_row and Lifecycle_row_missing, remove the duplicate synthetic row, then retest before 07B is enabled. |
| SQL Insert row is blocked. | Stop using the connection, verify the per-learner C903 Training SQL connection reference, gateway, network, and insert permission with the trainer; never substitute personal or production SQL. |

## Challenge

Return the existing SQLAuditID in Respond_existing by querying the SharePoint source after the duplicate guard. Keep the guard mandatory and prove the SQL count remains one.

## Reflection

Which two controls prevent a double click from creating duplicate Dataverse and SQL records?

---

[← Lab 6](lab-06-block-calendar-time-with-validation-and-duplicate-prevention.md) · [Lab 8 →](lab-08-recover-the-same-integration-run-and-complete-operational-handover.md)
