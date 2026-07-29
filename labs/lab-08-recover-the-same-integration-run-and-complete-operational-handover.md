# Lab 8 — Recover the Same Integration Run and Complete Operational Handover

**Course:** PL-7002 Create and Manage Automated Processes by using Power Automate  
**Course Code:** C903  
**Version:** v1.0 (29 July 2026)  
**Topic 4:** Power Automate's Deep Integration Across Multiple Data Sources  
**Maps to:** LO4: configure serial Try/Catch/Finally scopes, use a runtime-controlled failure, resubmit the same failed Dataverse event after correction, verify exactly-once recovery, and complete ownership and runbook evidence  
**Duration:** 40 minutes  
**Tools:** Power Automate monitoring · run-after scopes · SharePoint · Dataverse · SQL · solution ownership

---

## Goal

Fail NW-1099 safely at runtime, recover that same Dataverse event into one SQL row without another Dataverse row, run a separate NW-1010 regression, and hand over the automation.

## What You Will Do

You will wrap 07B in serial Try, Catch, and Finally scopes. A temporary Compose divides by the runtime Diagnostic Divisor, so NW-1099 value 0 fails only after the flow is saved and triggered. Catch filters error details and records Automation Error. You will remove the temporary action, resubmit the same failed 07B run, prove one Dataverse and one SQL row for NW-1099, and then run NW-1010 as an independent regression.

## What You Will Build

A final 07B flow with tested serial Try/Catch/Finally behaviour, same-record recovery evidence for NW-1099, NW-1010 regression evidence, approved co-owners, and a Reviewed operations runbook

## Prerequisites

- Lab 7 is Reconciled for NW-1009 and both flows use your isolated resources and healthy connection references.
- Copy labs/assets/operations-runbook-template.md to work-c903/C903-Operations-Runbook.md.
- The trainer-designated backup owner has pre-provisioned read and maintenance access to the isolated SharePoint, Dataverse, and SQL resources.
- The Lab 7 starter package already supplied varAuditFailed, Failure_flag_is_true, failed-Terminate, empty Catch_audit_error and Finally_record_run scopes, and named placeholder actions; Lab 8 configures those placeholders and the supplied runbook headings during its 40-minute allocation.

> **Data note.** Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

## Steps

### 1. Edit C90307B_Audit_Dataverse_Request. Before Try_write_audit configure the existing Boolean variable varAuditFailed with initial value false. Confirm the Lab 7 SharePoint lookup, count Condition, and Write_audit_targets scope are already inside Try_write_audit. As the first direct action inside Try, before Find_source_for_audit, configure temporary Compose C903_Runtime_Diagnostic using the Dataverse trigger's Diagnostic Divisor token. Configure the existing Catch_audit_error after Try for failed, timed out, or skipped and not success. Configure the existing Finally_record_run after Catch for successful, failed, timed out, and skipped Catch outcomes.

```text
Runtime expression:
div(1,int(<Dataverse Diagnostic Divisor dynamic-content token>))

Serial run-after contract:
Try -> Catch; Catch runs only when Try is unsuccessful.
Catch -> Finally; Finally accepts every Catch status, including skipped when Try succeeds.
Finally -> Failure_flag_is_true; the Condition runs after successful Finally.
```

### 2. Inside Catch configure Filter array Only_unsuccessful_audit_actions with From = union(result('Write_audit_targets'),result('Try_write_audit')) and filter only Failed, TimedOut, or Cancelled actions so skipped placeholders are excluded. Set varAuditFailed to true. Configure only Error_action, Error_status, Error_code, and Error_message from the first filtered item using the null-safe expressions below. Configure the existing SharePoint Get items Find_failed_source using your assigned training Site Address, list C903 Process Requests, and Filter Query RequestID eq '<Dataverse Request ID token>'. Require equals(length(body('Find_failed_source')?['value']),1); when false, send a count alert and Terminate Cancelled C903_AUDIT_SOURCE_COUNT. When true, update only Status to Automation Error while preserving RequestID, RequestTitle, RequesterEmail, Priority, DueDate, ReminderSent, ApprovalOutcome, ApprovalComments, CalendarEventID, DataverseRowID, SQLAuditID, and DiagnosticDivisor. Send one internal message containing only RequestID, those four filtered error fields, utcNow(), owner, and item link. After Finally configure Condition Failure_flag_is_true with the expression below. In true, Terminate Failed with Code C903_AUDIT_RUNTIME_FAILURE; in false, end normally. This propagates the handled failure only after Finally has recorded completion.

```text
Filter condition:
@or(equals(item()?['status'],'Failed'),equals(item()?['status'],'TimedOut'),equals(item()?['status'],'Cancelled'))

Error_action: first(body('Only_unsuccessful_audit_actions'))?['name']
Error_status: first(body('Only_unsuccessful_audit_actions'))?['status']
Error_code: coalesce(first(body('Only_unsuccessful_audit_actions'))?['outputs']?['body']?['error']?['code'],first(body('Only_unsuccessful_audit_actions'))?['outputs']?['body']?['code'],first(body('Only_unsuccessful_audit_actions'))?['outputs']?['error']?['code'],first(body('Only_unsuccessful_audit_actions'))?['error']?['code'],'NO_CODE_FROM_ACTION')
Error_message: coalesce(first(body('Only_unsuccessful_audit_actions'))?['outputs']?['body']?['error']?['message'],first(body('Only_unsuccessful_audit_actions'))?['outputs']?['body']?['message'],first(body('Only_unsuccessful_audit_actions'))?['outputs']?['error']?['message'],first(body('Only_unsuccessful_audit_actions'))?['error']?['message'],'No connector message returned')

Failure flag condition:
equals(variables('varAuditFailed'),true)

Never place result('Try_write_audit'), raw inputs, raw outputs, connection data, or a full trigger body in the email or runbook.
```

### 3. Save 07B with the runtime expression. Create NW-1099 in SharePoint with DiagnosticDivisor 0 and submit it once through the app. Record T24A. Confirm one Dataverse row exists, Try fails first at C903_Runtime_Diagnostic, Catch runs, SharePoint becomes Automation Error, one filtered alert is sent, Finally runs, Failure_flag_is_true terminates the overall run Failed, and the SQL count query returns zero.

```text
NW-1099: Controlled SQL recovery test | <YOUR_TRAINING_EMAIL> | Normal | New | due in 2 days | ReminderSent No | DiagnosticDivisor 0
Expected T24A counts:
SharePoint 1 | Dataverse 1 | SQL 0
Do not click the app again; recovery must reuse this Dataverse event.
```

### 4. Delete only C903_Runtime_Diagnostic, save 07B, open the failed 07B run for NW-1099, and select Resubmit. Record T24B from the resubmitted run. Verify Try and Finally run, Catch is skipped, SharePoint returns to Open with DataverseRowID and SQLAuditID, and counts are SharePoint 1, Dataverse 1, SQL 1. Then create NW-1010 with DiagnosticDivisor 1, submit once through the app, and record T25 as a separate regression.

```text
T24B safe recovery:
Current corrected flow definition + original NW-1099 trigger data -> one SQL insert; no new Dataverse row.

NW-1010: Publish monthly automation health summary | <YOUR_TRAINING_EMAIL> | Normal | New | due in 10 days | ReminderSent No | DiagnosticDivisor 1
T25 expected: Try and Finally run; Catch skipped; SharePoint 1 | Dataverse 1 | SQL 1.
```

### 5. Inspect the latest 07A and 07B run histories and connection references. Record trigger arrival, success, duration, business completion, controlled failure, same-run resubmission, and connection health. Add the approved backup owner to both flows and verify direct access to every underlying isolated resource. Complete C903-Operations-Runbook.md with systems of record, field map, owners, connection identities, 401/403 recovery, monitor thresholds, duplicate guard, exact safe retry sequence, T24A/T24B/T25 evidence, and Reviewed acceptance. Append explicit NW-1099 and NW-1010 rows to C903-Correlation-Register.csv using the unchanged ten-column header.

```text
Safe retry sequence:
1. Query SharePoint, Dataverse, and SQL by RequestID.
2. If Dataverse exists and SQL is missing, correct 07B, open that failed 07B run, and select Resubmit once.
3. Requery counts and reconcile returned IDs; do not invoke 07A again.
4. If all target rows exist, do not resubmit.
5. For 401/403, restore the approved connection or permission before resubmission; never broaden access as a shortcut.

NW-1099 correlation row: 07A Created timestamp | 07A Existing blank | T24A failed 07B timestamp in Flow07BInitialRunTimeUTC | T24B resubmitted timestamp in Flow07BRecoveryRunTimeUTC | Reconciled.
NW-1010 correlation row: 07A Created timestamp | 07A Existing blank | T25 successful 07B timestamp in Flow07BInitialRunTimeUTC | recovery blank | Reconciled.
```

## Test It

T24A must show a runtime, not save-time, failure for NW-1099; filtered Catch evidence; and counts 1/1/0. The post-Finally failure flag must make the overall T24A run Failed and therefore resubmittable. T24B must be a resubmission of that same failed 07B run and end with counts 1/1/1, reconciled IDs, Try success, Catch skipped, and Finally success. T25 must independently show 1/1/1 for NW-1010. The final saved 07B must contain no diagnostic action, both flows must have approved primary and backup owners, and the runbook must document exact resubmission, duplicate, timeout, invalid-input, 401/403, and connection-repair paths. The correlation register must include one complete row each for NW-1099 and NW-1010 with initial and recovery 07B timestamps placed in their defined columns. T24A must identify C903_Runtime_Diagnostic as the leaf Error_action and store nonblank Error_code and Error_message; documented fallback text is acceptable only when the action returns no structured detail.

## Checkpoint and Rejoin Point

Publish all C903 solution components and save the Reviewed runbook, correlation register, ownership record, and T01-T25 evidence. NW-1099 and NW-1010 must both be Reconciled at 1/1/1. A returning owner can now query one RequestID, locate the exact failed run, apply the safe resubmission rule, and verify recovery without the original maker.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The diagnostic expression prevents the flow from saving. | Confirm the divisor is the Dataverse trigger's runtime Diagnostic Divisor token; do not use the constant expression div(1,0). |
| Finally does not run after Try succeeds. | Place Finally after Catch and allow every Catch status, especially skipped; on Try success Catch is skipped and Finally must accept that state. |
| Resubmission would duplicate an SQL row. | Run the count query first. Resubmit only when Dataverse exists and SQL count is zero; the unique RequestID/EventType index remains the final guard. |

## Challenge

Build a weekly health summary from bounded run metadata that reports trigger count, success count, controlled failure count, and duration without including raw request payloads.

## Reflection

Which evidence proves that NW-1099 was recovered rather than replaced by a different successful request?

---

[← Lab 7](lab-07-build-an-idempotent-power-apps-sharepoint-dataverse-and-sql-integration.md) · [Labs index →](README.md)
