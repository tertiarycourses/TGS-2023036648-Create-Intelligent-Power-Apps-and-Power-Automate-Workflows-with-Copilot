# C903 Starter Solution Provisioning Package v1.0

Package ID: `C903-Northwind-Automation-Starter`

Solution version: `1.0.0.0`

Purpose: define the exact inactive Power Platform starter components that the trainer provisions in each learner's isolated environment before class. This definition contains no tenant IDs, credentials, connection strings, or production data.

Learners configure the named cards below. They do not build these flows from a blank canvas during the timed labs.

## Shared solution components

- Solution: `C903 Northwind Automation`
- Dataverse table: `C903 Automation Requests`
- Active alternate key: `Request ID`
- Canvas app shell: `C903 Request Launcher`
- Model-driven app shell: `C903 Request Manager`
- Connection-reference placeholders: SharePoint, Office 365 Outlook, Office 365 Users, Dataverse, Power Apps, and `C903 Training SQL`

## Starter flow inventory

### C903-02-Remind-Due-Requests

State before class: Off

Existing named cards, in order:

1. Recurrence trigger `Daily_1600_SGT`
2. SharePoint Get items `Find_due_open_requests`
3. Apply to each `For_each_candidate`
4. Condition `Due_date_is_today`
5. Compose `Runtime_diagnostic_check` in the matching branch
6. Send an email (V2) `Send_due_reminder`
7. SharePoint Update item `Mark_reminder_sent`

Learner-owned configuration: recurrence values, site/list, filter, expressions, field mappings, message, tests, ownership.

### C903-03-Approve-High-Priority-Request

State before class: Off

Existing named cards, in order:

1. SharePoint trigger `Request_for_routing`
2. Condition `Is_high_priority`
3. Non-High Update item `Continue_without_approval`
4. Non-High Send an email (V2) `Notify_no_approval_required`
5. Scope `Try_approval`
6. Pending-approval Update item
7. Start and wait for an approval `Request_operations_decision`
8. Switch `Route_decision` with Approve, Need more information, Reject, and Default cases
9. One Update item and one Send an email (V2) placeholder per case
10. Scope `Catch_approval_error`
11. Filter array `Only_unsuccessful_actions`
12. Compose `Error_action`, `Error_status`, `Error_code`, and `Error_message`
13. Catch Update item and filtered internal email
14. Scope `Finally_record_completion`

Learner-owned configuration: connections, mappings, responses, timeout, expressions, run-after settings, messages, tests.

### C903-05-Create-User-Follow-Up

State before class: Off

Existing named cards, in order:

1. Manually trigger a flow with four input placeholders
2. Compose `Normalised_work_mode`
3. Condition `Work_mode_is_allowed` and false Terminate
4. SharePoint Get items `Find_request_by_ID`
5. Condition `Exactly_one_request` and false Terminate
6. Get my profile (V2) `Get_invoking_user_profile`
7. String variable `ResolvedLocation`
8. Condition `Use_directory_location` with one Set variable action per branch
9. Compose `Follow_up_date_display`
10. Send an email (V2)

Learner-owned configuration: input contract, exact filter/count, selected profile fields, conditions, variable values, date expression, message, tests.

### C903-06-Block-Follow-Up-Time

State before class: Off

Existing named cards, in order:

1. Manually trigger a flow with three input placeholders
2. SharePoint Get items `Find_calendar_request`
3. Condition `Exactly_one_calendar_request` and false Terminate
4. Scope `Try_parse_time` with `Start_local_normalised`, `Start_UTC`, and `End_UTC`
5. Scope `Catch_invalid_format` with filtered-error placeholders and invalid-ISO Terminate
6. Condition `Range_and_future` and false Terminate
7. Scope `Schedule_calendar`
8. Condition `Event_ID_is_empty`
9. Scope `Create_event_path` with Create event (V4) `Create_follow_up_event`, Update item, and created confirmation
10. Scope `Reuse_event_path` with the reused confirmation
11. Scope `Verify_calendar_count` with Get calendar view of events (V3), Filter array `Calendar_events_for_request`, and Compose `Calendar_event_count`
12. Scope `Catch_calendar_technical` with Filter array `Only_unsuccessful_calendar_actions`, four error Compose actions, Update item, alert, and technical Terminate

Learner-owned configuration: exact site/list/filter, parsing, range, event mapping, preserve-all-fields update, category filter, run-after settings, filtered errors, tests.

### C90307A_PowerApps_Submit_Request

State before class: Off

Existing named cards, in order:

1. Power Apps (V2) trigger with required `RequestID` input
2. SharePoint Get items `Find_source_request`
3. Condition `Exactly_one_source` and response `Respond_source_count_error`
4. Dataverse List rows `Find_existing_lifecycle_row`
5. Condition `Lifecycle_row_missing`
6. Dataverse Add a new row `Create_lifecycle_row`
7. SharePoint Update item `Persist_dataverse_ID`
8. Responses `Respond_created` and `Respond_existing`

Learner-owned configuration: exact filters, alternate-key guard, mappings, new GUID assignment, responses, app binding, tests.

### C90307B_Audit_Dataverse_Request

State before class: Off

Existing named cards, in order:

1. Dataverse Added trigger
2. Boolean variable `varAuditFailed`
3. Scope `Try_write_audit`
4. SharePoint Get items `Find_source_for_audit`
5. Condition `Exactly_one_audit_source`
6. Scope `Write_audit_targets` containing SQL Insert row (V2) `Insert_audit_row` and SharePoint Update item
7. Count-alert and source-count Terminate placeholders
8. Scope `Catch_audit_error`
9. Filter array `Only_unsuccessful_audit_actions`
10. Compose `Error_action`, `Error_status`, `Error_code`, and `Error_message`
11. SharePoint Get items `Find_failed_source`, count Condition, Update item, and filtered alert placeholders
12. Scope `Finally_record_run`
13. Condition `Failure_flag_is_true` and failed Terminate placeholder

Learner-owned configuration: trigger table, exact lookup/count guards, SQL mapping, preserve-all-fields updates, run-after settings, failure flag, diagnostic, recovery, tests, ownership.

## Trainer acceptance

The package is Ready only when the companion `trainer-provisioning-checklist.md` is complete for every learner. If any named component is missing or a flow is on before class, stop and repair provisioning before the timed lab begins.
