"""Topic 4 labs for C903: Power Apps, Dataverse, SQL, monitoring, ownership, and handover."""

DOMAIN4 = [
    dict(
        num=7,
        topic=4,
        title="Build an Idempotent Power Apps, SharePoint, Dataverse, and SQL Integration",
        duration=45,
        objective=(
            "LO4: invoke a flow from Power Apps, require one SharePoint request, enforce a Dataverse duplicate "
            "guard, react to the Dataverse add event, write one SQL audit row, and reconcile all identifiers"
        ),
        goal=(
            "Submit NW-1009 from the canvas app and prove that the same RequestID links exactly one SharePoint item, "
            "one Dataverse row and one SQL audit row across three expected runs: 07A Created, 07B Added, and 07A Existing."
        ),
        workflow=["Preflight isolation", "Build guarded app flow", "Build event flow", "Disable double submit", "Reconcile counts"],
        desc=(
            "You will use per-learner SharePoint, Dataverse, canvas-app, and SQL resources prepared by the trainer. "
            "The Power Apps flow rejects zero or multiple SharePoint matches and returns an existing Dataverse row "
            "instead of creating a duplicate. A Dataverse-added flow inserts one SQL audit row and writes the target "
            "identifiers back to SharePoint. The app disables its button while a submission is running."
        ),
        build=(
            "Two solution-aware guarded cloud flows, a bound C903 Request Launcher app, exactly one Dataverse and "
            "SQL row for NW-1009, and a complete supplied-header correlation record"
        ),
        services="Power Apps · SharePoint Online · Microsoft Dataverse · SQL Server connector · Power Automate solutions",
        prerequisites=[
            "Use only the trainer-assigned isolated SharePoint site, Power Platform environment, calendar, and SQL database.",
            "The trainer has provisioned C903 Northwind Automation, the active Request ID alternate key, and the C903 Request Launcher app shell.",
            "The same solution contains inactive 07A and 07B starter flows from "
            "labs/assets/c903-starter-solution-package-v1.0.md with the named triggers, actions, "
            "Try_write_audit/Catch_audit_error/Finally_record_run scopes, and connection-reference placeholders "
            "already arranged; complete their exact guards, mappings, formulas, and run-after settings rather than "
            "building every card from a blank canvas during this 45-minute lab.",
            "Your learner and trainer accounts have the required Power Apps/Power Automate premium entitlement for "
            "Dataverse and SQL, and the environment DLP policy permits the documented connectors together.",
            "C903 Training SQL is a trainer-owned premium connection reference to your isolated database; gateway and network health are green.",
            "Your training identity has permission to run the supplied DDL script and insert/select only dbo.C903AutomationAudit; it has no broader production access.",
            "Copy the supplied correlation-register template and keep its header unchanged.",
        ],
        steps=[
            (
                "Open labs/assets/setup-automation-audit.sql in the approved training SQL editor, confirm the selected "
                "database name and learner tag with the trainer, execute the idempotent script once, and run the final "
                "queries. Confirm the table exists, the index query returns "
                "UX_C903AutomationAudit_Request_Event with IsUnique 1, and no NW-1009 row exists. Stop and ask the "
                "trainer to repair the package if the unique index is absent. Do not enter or record a connection string.",
                "Required SQL columns:\n"
                "AuditID | RequestID | DataverseRowID | EventType | EventTimeUTC | FlowRunNote | CreatedUTC\n\n"
                "Preflight query:\n"
                "SELECT RequestID, COUNT(*) AS RowCount\n"
                "FROM dbo.C903AutomationAudit\n"
                "WHERE RequestID = N'NW-1009'\n"
                "GROUP BY RequestID;\n\n"
                "Expected before the test: zero returned groups.",
            ),
            (
                "In C903 Northwind Automation open the inactive starter Instant cloud flow "
                "C90307A_PowerApps_Submit_Request with "
                "Power Apps (V2) required Text input RequestID. Configure the existing SharePoint Get items "
                "Find_source_request with the Filter Query shown below and Condition Exactly_one_source. In its false "
                "branch configure Respond to a Power App or flow Respond_source_count_error. In the true branch "
                "configure Dataverse List rows Find_existing_lifecycle_row and Condition Lifecycle_row_missing.",
                "SharePoint Filter Query:\n"
                "RequestID eq '<Power Apps RequestID token>'\n"
                "Exactly_one_source:\n"
                "equals(length(body('Find_source_request')?['value']),1)\n\n"
                "Dataverse Table: C903 Automation Requests\n"
                "Filter rows using provisioned logical name:\n"
                "c903_requestid eq '<Power Apps RequestID token>'\n"
                "Lifecycle_row_missing:\n"
                "equals(length(body('Find_existing_lifecycle_row')?['value']),0)\n\n"
                "Count-error response: message='RequestID must match exactly one SharePoint item'; dataverseRowID=''; state='Rejected'.",
            ),
            (
                "In Lifecycle_row_missing Yes, configure the existing Dataverse Add a new row Create_lifecycle_row "
                "with the exact field map, then SharePoint Update item Persist_dataverse_ID with the current numeric "
                "item ID and every required list field, and Respond to a Power App or flow Respond_created. In No, "
                "configure Respond_existing using the first returned Dataverse row ID and create nothing.",
                "Dataverse mapping:\n"
                "Request ID <- Power Apps RequestID\n"
                "Request Title, Requester Email, Priority, Due Date, SharePoint Item ID, Diagnostic Divisor <- first SharePoint row\n"
                "Request Status <- Open\n\n"
                "Persist_dataverse_ID must preserve RequestID, RequestTitle, RequesterEmail, Priority, Status, DueDate, "
                "ReminderSent, ApprovalOutcome, ApprovalComments, CalendarEventID, SQLAuditID, and DiagnosticDivisor, "
                "and set DataverseRowID = the Row ID returned by Create_lifecycle_row.\n\n"
                "Respond_created: message='Created <RequestID>'; dataverseRowID=<new GUID>; state='Created'\n"
                "Respond_existing: message='Existing <RequestID>'; dataverseRowID=<first existing GUID>; state='Existing'",
            ),
            (
                "In the same solution open the inactive starter Automated cloud flow "
                "C90307B_Audit_Dataverse_Request with Dataverse "
                "When a row is added, modified or deleted: Change type Added, Table C903 Automation Requests, "
                "Scope Organization. Inside Try_write_audit configure SharePoint Get items Find_source_for_audit "
                "with your assigned training Site Address, list C903 Process Requests, and Filter Query "
                "RequestID eq '<Dataverse Request ID token>', then Condition Exactly_one_audit_source. Only in Yes "
                "configure Scope Write_audit_targets containing SQL Server Insert row (V2) Insert_audit_row and the "
                "SharePoint update with DataverseRowID, returned AuditID, and Status Open. "
                "In No send one internal count alert and Terminate Cancelled C903_AUDIT_SOURCE_COUNT without inserting "
                "an audit row.",
                "SQL mapping:\n"
                "RequestID <- Dataverse Request ID\n"
                "DataverseRowID <- Dataverse row unique identifier\n"
                "EventType <- Dataverse Added\n"
                "EventTimeUTC <- utcNow()\n"
                "FlowRunNote <- C90307B isolated training integration\n\n"
                "Exactly_one_audit_source:\n"
                "equals(length(body('Find_source_for_audit')?['value']),1)\n"
                "SharePoint update preserves RequestID, RequestTitle, RequesterEmail, Priority, Status, DueDate, "
                "ReminderSent, ApprovalOutcome, ApprovalComments, CalendarEventID, DataverseRowID, and "
                "DiagnosticDivisor, and sets only SQLAuditID to the Insert row AuditID.",
            ),
            (
                "Open the pre-provisioned C903 Request Launcher app shell. Add 07A from the Power Automate pane. "
                "Set the exact formulas, save, and publish. Save both 07A and 07B, select Turn on for each, and confirm "
                "both flow statuses are On before invoking the app. Create NW-1009 in your isolated SharePoint list with "
                "DiagnosticDivisor 1, play the app, select Submit once, observe that the button becomes disabled, and "
                "try to select it again while the first call is still running; the disabled control must prevent the "
                "second selection from starting another call. After the first call completes, select Submit once more "
                "to exercise the server-side Existing path. Before querying, open 07B run history, identify the NW-1009 "
                "Dataverse Added run, and refresh every 10 seconds for at most 2 minutes until its status is Succeeded. "
                "If it is still Running after 2 minutes, stop the test, record the run URL and timestamp, and escalate "
                "to the trainer; do not record a transient SQL count. After terminal success, record T23, query the "
                "three systems, and append one row using the unchanged correlation header.",
                "txtRequestID.Default = \"NW-1009\"\n"
                "btnSubmit.DisplayMode = If(varSubmitting,DisplayMode.Disabled,DisplayMode.Edit)\n"
                "btnSubmit.OnSelect = Set(varSubmitting,true);"
                "IfError(Set(varResult,C90307A_PowerApps_Submit_Request.Run(txtRequestID.Text)),"
                "Notify(\"Submission error\",NotificationType.Error));Set(varSubmitting,false)\n"
                "lblResult.Text = varResult.message & \" | Dataverse: \" & varResult.dataverseRowID\n\n"
                "NW-1009: Automate customer escalation handoff | <YOUR_TRAINING_EMAIL> | High | New | due in 7 days | "
                "ReminderSent No | DiagnosticDivisor 1\n\n"
                "SQL count query:\n"
                "SELECT RequestID, COUNT(*) AS RowCount FROM dbo.C903AutomationAudit "
                "WHERE RequestID=N'NW-1009' GROUP BY RequestID;\n\n"
                "Correlation header:\n"
                "RequestID | SharePointItemID | DataverseRowID | CalendarEventID | SQLAuditID | "
                "Flow07ACreatedRunTimeUTC | Flow07AExistingRunTimeUTC | Flow07BInitialRunTimeUTC | "
                "Flow07BRecoveryRunTimeUTC | State\n\n"
                "Record the first 07A Created run in Flow07ACreatedRunTimeUTC, the repeated 07A Existing run in "
                "Flow07AExistingRunTimeUTC, and the single Dataverse-added 07B run in Flow07BInitialRunTimeUTC. "
                "Leave Flow07BRecoveryRunTimeUTC blank for NW-1009.",
            ),
        ],
        test=(
            "T23 must show one SharePoint NW-1009, one Dataverse row by the active Request ID alternate key, and one "
            "SQL row by the count query. The first app response is Created and any repeated submission is Existing with "
            "the same Dataverse GUID; no second Dataverse trigger or SQL row occurs. SharePoint DataverseRowID and SQLAuditID "
            "must match the targets. Evidence must show exactly three relevant runs (07A Created, 07B Added, 07A Existing), "
            "the app button must disable while varSubmitting is true, and the correlation register must use all ten "
            "supplied columns. The SQL count is recorded only after the NW-1009 07B run reaches terminal Succeeded."
        ),
        checkpoint=(
            "Leave both solution-aware flows on, the app published, and NW-1009 Reconciled with counts 1/1/1. "
            "Lab 8 adds recovery and handover around 07B. To rejoin, repeat the app submission and confirm Existing "
            "plus unchanged Dataverse and SQL counts."
        ),
        troubleshooting=[
            (
                "Power Apps does not recognise the flow or response fields.",
                "Confirm the app and flow share the same isolated environment, remove and re-add the flow from the Power Automate pane, and let Power Apps insert the Run reference.",
            ),
            (
                "A repeated submission creates another Dataverse row.",
                "Stop 07A, verify the active Request ID alternate key, inspect Find_existing_lifecycle_row and Lifecycle_row_missing, remove the duplicate synthetic row, then retest before 07B is enabled.",
            ),
            (
                "SQL Insert row is blocked.",
                "Stop using the connection, verify the per-learner C903 Training SQL connection reference, gateway, network, and insert permission with the trainer; never substitute personal or production SQL.",
            ),
        ],
        challenge=(
            "Return the existing SQLAuditID in Respond_existing by querying the SharePoint source after the duplicate "
            "guard. Keep the guard mandatory and prove the SQL count remains one."
        ),
        reflection="Which two controls prevent a double click from creating duplicate Dataverse and SQL records?",
    ),
    dict(
        num=8,
        topic=4,
        title="Recover the Same Integration Run and Complete Operational Handover",
        duration=40,
        objective=(
            "LO4: configure serial Try/Catch/Finally scopes, use a runtime-controlled failure, resubmit the same "
            "failed Dataverse event after correction, verify exactly-once recovery, and complete ownership and runbook evidence"
        ),
        goal=(
            "Fail NW-1099 safely at runtime, recover that same Dataverse event into one SQL row without another "
            "Dataverse row, run a separate NW-1010 regression, and hand over the automation."
        ),
        workflow=["Wrap scopes", "Fail NW-1099", "Correct and resubmit", "Run regression", "Hand over"],
        desc=(
            "You will wrap 07B in serial Try, Catch, and Finally scopes. A temporary Compose divides by the runtime "
            "Diagnostic Divisor, so NW-1099 value 0 fails only after the flow is saved and triggered. Catch filters "
            "error details and records Automation Error. You will remove the temporary action, resubmit the same failed "
            "07B run, prove one Dataverse and one SQL row for NW-1099, and then run NW-1010 as an independent regression."
        ),
        build=(
            "A final 07B flow with tested serial Try/Catch/Finally behaviour, same-record recovery evidence for "
            "NW-1099, NW-1010 regression evidence, approved co-owners, and a Reviewed operations runbook"
        ),
        services="Power Automate monitoring · run-after scopes · SharePoint · Dataverse · SQL · solution ownership",
        prerequisites=[
            "Lab 7 is Reconciled for NW-1009 and both flows use your isolated resources and healthy connection references.",
            "Copy labs/assets/operations-runbook-template.md to work-c903/C903-Operations-Runbook.md.",
            "The trainer-designated backup owner has pre-provisioned read and maintenance access to the isolated SharePoint, Dataverse, and SQL resources.",
            "The Lab 7 starter package already supplied varAuditFailed, Failure_flag_is_true, failed-Terminate, empty "
            "Catch_audit_error and Finally_record_run scopes, and named "
            "placeholder actions; Lab 8 configures those placeholders and the supplied runbook headings during its "
            "40-minute allocation.",
        ],
        steps=[
            (
                "Edit C90307B_Audit_Dataverse_Request. Before Try_write_audit configure the existing Boolean variable "
                "varAuditFailed with initial value false. Confirm the Lab 7 SharePoint lookup, count Condition, and "
                "Write_audit_targets scope are already inside Try_write_audit. As the first direct action inside Try, "
                "before Find_source_for_audit, configure temporary Compose C903_Runtime_Diagnostic using the Dataverse "
                "trigger's Diagnostic Divisor token. Configure the "
                "existing Catch_audit_error after Try for failed, timed out, or skipped and not success. Configure the "
                "existing Finally_record_run after Catch for successful, failed, timed out, and skipped Catch outcomes.",
                "Runtime expression:\n"
                "div(1,int(<Dataverse Diagnostic Divisor dynamic-content token>))\n\n"
                "Serial run-after contract:\n"
                "Try -> Catch; Catch runs only when Try is unsuccessful.\n"
                "Catch -> Finally; Finally accepts every Catch status, including skipped when Try succeeds.\n"
                "Finally -> Failure_flag_is_true; the Condition runs after successful Finally.",
            ),
            (
                "Inside Catch configure Filter array Only_unsuccessful_audit_actions with From = "
                "union(result('Write_audit_targets'),result('Try_write_audit')) and filter only Failed, TimedOut, or "
                "Cancelled actions so skipped placeholders are excluded. Set varAuditFailed to true. Configure only "
                "Error_action, Error_status, Error_code, and Error_message from the first filtered item using the "
                "null-safe expressions below. Configure the existing SharePoint Get items Find_failed_source using your assigned training "
                "Site Address, list C903 Process Requests, and Filter Query RequestID eq '<Dataverse Request ID token>'. "
                "Require equals(length(body('Find_failed_source')?['value']),1); when false, send a count alert and "
                "Terminate Cancelled C903_AUDIT_SOURCE_COUNT. When true, update only Status to Automation Error while "
                "preserving RequestID, RequestTitle, RequesterEmail, Priority, DueDate, ReminderSent, ApprovalOutcome, "
                "ApprovalComments, CalendarEventID, DataverseRowID, SQLAuditID, and DiagnosticDivisor. Send one internal "
                "message containing only RequestID, those four filtered error fields, utcNow(), owner, and item link. "
                "After Finally configure Condition Failure_flag_is_true with the expression below. In true, Terminate "
                "Failed with Code C903_AUDIT_RUNTIME_FAILURE; in false, end normally. This propagates the handled "
                "failure only after Finally has recorded completion.",
                "Filter condition:\n"
                "@or(equals(item()?['status'],'Failed'),equals(item()?['status'],'TimedOut'),"
                "equals(item()?['status'],'Cancelled'))\n\n"
                "Error_action: first(body('Only_unsuccessful_audit_actions'))?['name']\n"
                "Error_status: first(body('Only_unsuccessful_audit_actions'))?['status']\n"
                "Error_code: coalesce(first(body('Only_unsuccessful_audit_actions'))?['outputs']?['body']?['error']?['code'],"
                "first(body('Only_unsuccessful_audit_actions'))?['outputs']?['body']?['code'],"
                "first(body('Only_unsuccessful_audit_actions'))?['outputs']?['error']?['code'],"
                "first(body('Only_unsuccessful_audit_actions'))?['error']?['code'],'NO_CODE_FROM_ACTION')\n"
                "Error_message: coalesce(first(body('Only_unsuccessful_audit_actions'))?['outputs']?['body']?['error']?['message'],"
                "first(body('Only_unsuccessful_audit_actions'))?['outputs']?['body']?['message'],"
                "first(body('Only_unsuccessful_audit_actions'))?['outputs']?['error']?['message'],"
                "first(body('Only_unsuccessful_audit_actions'))?['error']?['message'],'No connector message returned')\n\n"
                "Failure flag condition:\n"
                "equals(variables('varAuditFailed'),true)\n\n"
                "Never place result('Try_write_audit'), raw inputs, raw outputs, connection data, or a full trigger body "
                "in the email or runbook.",
            ),
            (
                "Save 07B with the runtime expression. Create NW-1099 in SharePoint with DiagnosticDivisor 0 and submit "
                "it once through the app. Record T24A. Confirm one Dataverse row exists, Try fails first at "
                "C903_Runtime_Diagnostic, Catch runs, SharePoint becomes Automation Error, one filtered alert is sent, "
                "Finally runs, Failure_flag_is_true terminates the overall run Failed, and the SQL count query returns zero.",
                "NW-1099: Controlled SQL recovery test | <YOUR_TRAINING_EMAIL> | Normal | New | due in 2 days | "
                "ReminderSent No | DiagnosticDivisor 0\n"
                "Expected T24A counts:\n"
                "SharePoint 1 | Dataverse 1 | SQL 0\n"
                "Do not click the app again; recovery must reuse this Dataverse event.",
            ),
            (
                "Delete only C903_Runtime_Diagnostic, save 07B, open the failed 07B run for NW-1099, and select Resubmit. "
                "Record T24B from the resubmitted run. Verify Try and Finally run, Catch is skipped, SharePoint returns "
                "to Open with DataverseRowID and SQLAuditID, and counts are SharePoint 1, Dataverse 1, SQL 1. Then create "
                "NW-1010 with DiagnosticDivisor 1, submit once through the app, and record T25 as a separate regression.",
                "T24B safe recovery:\n"
                "Current corrected flow definition + original NW-1099 trigger data -> one SQL insert; no new Dataverse row.\n\n"
                "NW-1010: Publish monthly automation health summary | <YOUR_TRAINING_EMAIL> | Normal | New | "
                "due in 10 days | ReminderSent No | DiagnosticDivisor 1\n"
                "T25 expected: Try and Finally run; Catch skipped; SharePoint 1 | Dataverse 1 | SQL 1.",
            ),
            (
                "Inspect the latest 07A and 07B run histories and connection references. Record trigger arrival, success, "
                "duration, business completion, controlled failure, same-run resubmission, and connection health. Add the "
                "approved backup owner to both flows and verify direct access to every underlying isolated resource. Complete "
                "C903-Operations-Runbook.md with systems of record, field map, owners, connection identities, 401/403 recovery, "
                "monitor thresholds, duplicate guard, exact safe retry sequence, T24A/T24B/T25 evidence, and Reviewed "
                "acceptance. Append explicit NW-1099 and NW-1010 rows to C903-Correlation-Register.csv using the unchanged "
                "ten-column header.",
                "Safe retry sequence:\n"
                "1. Query SharePoint, Dataverse, and SQL by RequestID.\n"
                "2. If Dataverse exists and SQL is missing, correct 07B, open that failed 07B run, and select Resubmit once.\n"
                "3. Requery counts and reconcile returned IDs; do not invoke 07A again.\n"
                "4. If all target rows exist, do not resubmit.\n"
                "5. For 401/403, restore the approved connection or permission before resubmission; never broaden access as a shortcut.\n\n"
                "NW-1099 correlation row: 07A Created timestamp | 07A Existing blank | T24A failed 07B timestamp in "
                "Flow07BInitialRunTimeUTC | T24B resubmitted timestamp in Flow07BRecoveryRunTimeUTC | Reconciled.\n"
                "NW-1010 correlation row: 07A Created timestamp | 07A Existing blank | T25 successful 07B timestamp in "
                "Flow07BInitialRunTimeUTC | recovery blank | Reconciled.",
            ),
        ],
        test=(
            "T24A must show a runtime, not save-time, failure for NW-1099; filtered Catch evidence; and counts 1/1/0. "
            "The post-Finally failure flag must make the overall T24A run Failed and therefore resubmittable. "
            "T24B must be a resubmission of that same failed 07B run and end with counts 1/1/1, reconciled IDs, Try success, "
            "Catch skipped, and Finally success. T25 must independently show 1/1/1 for NW-1010. The final saved 07B must "
            "contain no diagnostic action, both flows must have approved primary and backup owners, and the runbook must "
            "document exact resubmission, duplicate, timeout, invalid-input, 401/403, and connection-repair paths. The "
            "correlation register must include one complete row each for NW-1099 and NW-1010 with initial and recovery "
            "07B timestamps placed in their defined columns. T24A must identify C903_Runtime_Diagnostic as the leaf "
            "Error_action and store nonblank Error_code and Error_message; documented fallback text is acceptable only "
            "when the action returns no structured detail."
        ),
        checkpoint=(
            "Publish all C903 solution components and save the Reviewed runbook, correlation register, ownership record, "
            "and T01-T25 evidence. NW-1099 and NW-1010 must both be Reconciled at 1/1/1. A returning owner can now query "
            "one RequestID, locate the exact failed run, apply the safe resubmission rule, and verify recovery without the original maker."
        ),
        troubleshooting=[
            (
                "The diagnostic expression prevents the flow from saving.",
                "Confirm the divisor is the Dataverse trigger's runtime Diagnostic Divisor token; do not use the constant expression div(1,0).",
            ),
            (
                "Finally does not run after Try succeeds.",
                "Place Finally after Catch and allow every Catch status, especially skipped; on Try success Catch is skipped and Finally must accept that state.",
            ),
            (
                "Resubmission would duplicate an SQL row.",
                "Run the count query first. Resubmit only when Dataverse exists and SQL count is zero; the unique RequestID/EventType index remains the final guard.",
            ),
        ],
        challenge=(
            "Build a weekly health summary from bounded run metadata that reports trigger count, success count, controlled "
            "failure count, and duration without including raw request payloads."
        ),
        reflection="Which evidence proves that NW-1099 was recovered rather than replaced by a different successful request?",
    ),
]
