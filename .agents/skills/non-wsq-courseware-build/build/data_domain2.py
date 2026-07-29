"""Topic 2 labs for C903: approvals, conditional logic, recovery, and business process flows."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Build a Priority Approval with Complete Outcome and Recovery Paths",
        duration=45,
        objective=(
            "LO2: create and configure an approval, implement High and non-High paths, persist every custom "
            "outcome, exercise an approval timeout, and record filtered technical error details"
        ),
        goal=(
            "Route only High-priority Northwind requests to a named approver and close every approval, "
            "non-approval, default, or timeout path with an explicit SharePoint status, a requester message for "
            "handled business outcomes, or a filtered internal alert for technical failure."
        ),
        workflow=["Qualify", "Request decision", "Route every outcome", "Filter errors", "Exercise five paths"],
        desc=(
            "You will build an automated flow for new SharePoint requests. High priority creates an approval with "
            "Approve, Need more information, and Reject responses; other priorities continue without an approval. "
            "The flow stores outcome, comments, and status on the same request. A one-minute training timeout "
            "exercises Catch, which filters the scope result down to action name, status, error code, and message."
        ),
        build=(
            "An automated cloud flow named C903-03-Approve-High-Priority-Request with explicit non-High actions, "
            "three approval cases, a default case, serial Try/Catch/Finally scopes, and five path tests"
        ),
        services="SharePoint Online · Power Automate Approvals · Office 365 Outlook · conditions and control scopes",
        prerequisites=[
            "Labs 1 and 2 are complete in your trainer-assigned isolated SharePoint site.",
            "C903 Process Requests includes ApprovalOutcome, ApprovalComments, and DiagnosticDivisor from request-schema.md.",
            "The approved training account can create approvals and update its own isolated list.",
            "Use your training email as requester and approver unless the trainer supplies a separate isolated approver account.",
            "The trainer has provisioned the inactive C903-03-Approve-High-Priority-Request starter from "
            "labs/assets/c903-starter-solution-package-v1.0.md in your isolated environment "
            "with the trigger, named scopes, switch cases, and placeholder actions already arranged; you configure "
            "connections, mappings, expressions, run-after settings, and messages during this 45-minute lab.",
        ],
        steps=[
            (
                "Open the inactive starter Automated cloud flow named C903-03-Approve-High-Priority-Request with SharePoint - "
                "When an item is created, pointed to your C903 Process Requests list. Rename the trigger "
                "Request_for_routing. Configure the existing Condition Is_high_priority and compare Priority Value with High. "
                "In the non-High branch configure Update item Continue_without_approval and Send an email (V2) "
                "Notify_no_approval_required.",
                "Non-High mapping:\n"
                "Update the current numeric item ID; map RequestID, RequestTitle, RequesterEmail, Priority, "
                "DueDate, ReminderSent, and DiagnosticDivisor from the trigger.\n"
                "Status = Open\n"
                "ApprovalOutcome = Not required\n"
                "ApprovalComments = Priority did not require approval\n\n"
                "Email subject: No approval required - <RequestID>\n"
                "Email body: RequestID; Priority; Status Open; item link.",
            ),
            (
                "In the High branch configure the existing Scope Try_approval. Inside it configure the update of the "
                "current item to Pending Approval, then configure Approvals - Start and wait for an approval named "
                "Request_operations_decision. Choose "
                "Custom Responses - Wait for one response and enter the three response labels exactly. In the action "
                "Settings set Timeout to PT1M for this isolated training exercise.",
                "Responses, in order:\n"
                "Approve\n"
                "Need more information\n"
                "Reject\n\n"
                "Title: <RequestID> - <RequestTitle>\n"
                "Assigned to: <YOUR_TRAINING_EMAIL>\n"
                "Details: Priority; DueDate; RequesterEmail; SharePoint item link.\n"
                "Training timeout: PT1M. A workplace design must use its approved service target.",
            ),
            (
                "After the approval, still inside Try_approval, configure the existing Switch Route_decision on the approval Outcome. "
                "Create Approve, Need more information, and Reject cases plus a Default case. In every case update "
                "the same item, map all required fields, set ApprovalOutcome to the exact response, store the first "
                "response Comments in ApprovalComments, and send a matching email.",
                "Approve -> Status Approved; subject Decision: approved - <RequestID>\n"
                "Need more information -> Status More Info; subject Decision: more information needed - <RequestID>\n"
                "Reject -> Status Rejected; subject Decision: rejected - <RequestID>\n"
                "Default -> Status Automation Error; subject Decision response not recognised - <RequestID>\n\n"
                "Every decision message includes RequestID, Outcome, Completion date, Comments, and item link.",
            ),
            (
                "After Try_approval configure the existing Scope Catch_approval_error to run after Try has failed, timed out, "
                "or been skipped, and not after success. Inside Catch configure Filter array Only_unsuccessful_actions "
                "with From = result('Try_approval') and the status condition below, excluding deliberately skipped "
                "actions. Configure Compose actions Error_action, Error_status, Error_code, and Error_message from the "
                "first filtered item using the null-safe expressions below. Update the request to "
                "Automation Error and send one internal filtered-error message. Configure Finally_record_completion after "
                "Catch and configure it for every Catch outcome, including skipped.",
                "Filter condition:\n"
                "@or(equals(item()?['status'],'Failed'),equals(item()?['status'],'TimedOut'),"
                "equals(item()?['status'],'Cancelled'))\n\n"
                "Filtered fields:\n"
                "first(body('Only_unsuccessful_actions'))?['name']\n"
                "first(body('Only_unsuccessful_actions'))?['status']\n"
                "coalesce(first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['error']?['code'],"
                "first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['code'],"
                "first(body('Only_unsuccessful_actions'))?['outputs']?['error']?['code'],"
                "first(body('Only_unsuccessful_actions'))?['error']?['code'],'NO_CODE_FROM_ACTION')\n"
                "coalesce(first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['error']?['message'],"
                "first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['message'],"
                "first(body('Only_unsuccessful_actions'))?['outputs']?['error']?['message'],"
                "first(body('Only_unsuccessful_actions'))?['error']?['message'],'No connector message returned')\n\n"
                "Internal email includes only RequestID, those four fields, utcNow(), owner, and item link. "
                "Do not include result('Try_approval') or a raw action payload in the message.",
            ),
            (
                "Save, select Turn on, confirm the flow status is On, and exercise five isolated records one at a time. "
                "Respond from the approval centre for the "
                "first three High records; do not respond to the timeout record. Record T07-T11 in C903-Test-Evidence.csv "
                "with RequestID, Priority, approval created Yes/No, response or timeout, final SharePoint status, "
                "ApprovalComments, message subject, and run timestamp.",
                "Create each record with RequestID | RequestTitle | RequesterEmail | Priority | Status | DueDate | "
                "ReminderSent | DiagnosticDivisor, using your training email, Status New, a future due date, No, and 1:\n"
                "T07 NW-1007 | Approve supplier onboarding automation | <YOUR_TRAINING_EMAIL> | High -> "
                "Approve with comment 'Approved for the training route' -> Approved\n"
                "T08 NW-1011 | Review customer refund approval | <YOUR_TRAINING_EMAIL> | High -> "
                "Need more information with comment 'Add the process owner' -> More Info\n"
                "T09 NW-1012 | Review warehouse exception route | <YOUR_TRAINING_EMAIL> | High -> "
                "Reject with comment 'Outside the training scope' -> Rejected\n"
                "T10 NW-1008 | Send a normal-priority operations update | <YOUR_TRAINING_EMAIL> | Normal -> "
                "no approval -> Open\n"
                "T11 NW-1013 | Exercise the isolated approval timeout | <YOUR_TRAINING_EMAIL> | High -> "
                "no response for PT1M -> Catch -> Automation Error\n\n"
                "Every RequestID is created once in your isolated list.",
            ),
        ],
        test=(
            "T07-T09 must each create one approval, store the exact outcome and supplied comment, update the expected "
            "status, and send one matching decision message. T10 must create no approval and must take the explicit "
            "non-High update and message path. T11 must time out, run Catch, store Automation Error, and send only the "
            "filtered action name, status, code, and message. Finally must run after both successful and skipped Catch outcomes."
            " Error_code and Error_message must both be nonblank in T11 evidence; use the documented fallback text only "
            "when the connector supplies no structured code or message."
        ),
        checkpoint=(
            "Leave NW-1007 Approved, NW-1011 More Info, NW-1012 Rejected, NW-1008 Open, and NW-1013 Automation Error. "
            "Save T07-T11, then turn C903-03-Approve-High-Priority-Request off so it cannot intercept the High-priority records "
            "created in later labs. Lab 4 reuses NW-1007 and NW-1008 field values in Dataverse. "
            "To rejoin, verify all five outcome rows and the filtered timeout message."
        ),
        troubleshooting=[
            (
                "The approval is not visible in email.",
                "Open Power Automate Approvals, confirm Assigned to matches the signed-in training account, and respond from the approval centre.",
            ),
            (
                "The Switch does not match the selected response.",
                "Open the approval output, copy the exact Outcome text, and make the case label match spaces and capitalisation exactly.",
            ),
            (
                "Catch exposes more data than the four error fields.",
                "Remove the raw scope result from the email, confirm Filter array excludes Succeeded actions, and map only Error_action, Error_status, Error_code, and Error_message.",
            ),
        ],
        challenge=(
            "After completing the timed test, change the approval timeout to a realistic organisational service target "
            "and document the separate escalation owner and cancellation rule without altering the five recorded training runs."
        ),
        reflection="Which paths express business decisions, and which path exists only to recover a technical exception?",
    ),
    dict(
        num=4,
        topic=2,
        title="Create and Traverse a Conditional Dataverse Business Process Flow",
        duration=40,
        objective=(
            "LO2: create a business process flow on a pre-provisioned Dataverse table, branch by priority, "
            "activate it, and traverse one High and one Normal record through every stage in their path"
        ),
        goal=(
            "Give Northwind coordinators a visible lifecycle in which High-priority requests traverse Approval "
            "while other requests move from Review directly to Fulfilment, and prove both paths reach Closure."
        ),
        workflow=["Verify model", "Design stages", "Branch priority", "Publish process", "Traverse both paths"],
        desc=(
            "The trainer has pre-provisioned the solution, table, alternate key, main form, active view, and app shell "
            "so the timed lab focuses on process design. You will verify the model, create a five-stage business process "
            "flow, add a High-priority branch, activate it, and advance NW-1007 and NW-1008 through every expected stage."
        ),
        build=(
            "An active C903 Request Lifecycle business process flow in the C903 Northwind Automation solution, "
            "published in C903 Request Manager, with complete High and Normal path evidence"
        ),
        services="Power Apps maker portal · Microsoft Dataverse · business process flows · model-driven apps",
        prerequisites=[
            "Use your trainer-assigned isolated Power Platform environment with Dataverse maker permissions.",
            "The trainer has provisioned C903 Northwind Automation, C903 Automation Request, and C903 Request Manager.",
            "Request ID is an active mandatory alternate key; if the key is absent, stop and ask the trainer to restore provisioning.",
            "Copy labs/assets/correlation-register-template.csv to work-c903/C903-Correlation-Register.csv.",
        ],
        steps=[
            (
                "At make.powerapps.com select your isolated training environment and open C903 Northwind Automation. "
                "Inspect C903 Automation Request and verify the exact columns, types, required settings, Request ID "
                "alternate key, main form, active view, and model-driven app page. Do not continue if any item differs.",
                "Required columns:\n"
                "Request ID - Text, required, active alternate key\n"
                "Request Title - Text, required\n"
                "Requester Email - Email\n"
                "Priority - Choice: Low, Normal, High\n"
                "Request Status - Choice: New, Open, Pending Approval, Approved, More Info, Rejected, Fulfilment, Closed\n"
                "Due Date - Date only\n"
                "Approval Outcome - Text\n"
                "SharePoint Item ID - Whole number\n"
                "Diagnostic Divisor - Whole number, default 1",
            ),
            (
                "Inside the solution create Automation - Process - Business process flow named C903 Request Lifecycle "
                "for C903 Automation Request. Add stages in order Intake, Review, Approval, Fulfilment, Closure. "
                "Add the stated data steps and mark only Request ID and Request Title required in Intake.",
                "Intake: Request ID, Request Title, Requester Email\n"
                "Review: Priority, Due Date\n"
                "Approval: Approval Outcome, Request Status\n"
                "Fulfilment: Request Status\n"
                "Closure: Request Status",
            ),
            (
                "Insert Condition High_priority_route after Review with Priority Equals High. Connect true to Approval "
                "then Fulfilment; connect false directly to Fulfilment; connect both to Closure. Select Validate, correct "
                "any disconnected component, Save, and Activate.",
                "High path: Intake -> Review -> Approval -> Fulfilment -> Closure\n"
                "Default path: Intake -> Review -> Fulfilment -> Closure\n"
                "Every branch must reach Closure.",
            ),
            (
                "Add the active C903 Request Lifecycle process to C903 Request Manager if it is not automatically "
                "available. Save and Publish the app. Open it and create NW-1007 and NW-1008 using the Lab 3 values, "
                "including each source SharePoint numeric item ID and Diagnostic Divisor 1.",
                "NW-1007: High | Approved | Approve supplier onboarding automation\n"
                "NW-1008: Normal | Open | Send a normal-priority operations update\n"
                "Use the exact Request ID alternate key; a duplicate create must be rejected.",
            ),
            (
                "For NW-1007, record the active stage, complete required values, and select Next Stage through Intake, "
                "Review, Approval, Fulfilment, and Closure; set final Request Status Closed. Repeat NW-1008 through Intake, "
                "Review, Fulfilment, and Closure. Record T12 and T13 with every observed stage and add both generated "
                "Dataverse row IDs to C903-Correlation-Register.csv.",
                "T12 NW-1007 expected: Intake | Review | Approval | Fulfilment | Closure | Closed\n"
                "T13 NW-1008 expected: Intake | Review | Fulfilment | Closure | Closed\n\n"
                "Correlation header, unchanged:\n"
                "RequestID | SharePointItemID | DataverseRowID | CalendarEventID | SQLAuditID | "
                "Flow07ACreatedRunTimeUTC | Flow07AExistingRunTimeUTC | Flow07BInitialRunTimeUTC | "
                "Flow07BRecoveryRunTimeUTC | State",
            ),
        ],
        test=(
            "The solution must contain the active five-stage C903 Request Lifecycle with one High-priority branch and "
            "an active Request ID alternate key. T12 must show all five stages for NW-1007 and T13 must show the four-stage "
            "default path for NW-1008. Both records must reach Closure and end Closed. The correlation register must use "
            "the supplied header and store the SharePoint and Dataverse IDs for both RequestIDs."
        ),
        checkpoint=(
            "Keep the solution and app published and both records Closed. Save T12-T13 and the correlation register. "
            "Lab 7 reuses the table, alternate key, solution, and app shell with a new NW-1009 record. To rejoin, "
            "open both completed process instances and verify every active-stage transition recorded in the evidence."
        ),
        troubleshooting=[
            (
                "The process cannot activate.",
                "Select Validate, connect every stage and branch to Closure, confirm each data step references an existing column, save, and activate again.",
            ),
            (
                "Both records follow the same branch.",
                "Confirm Priority stores different choice values, inspect the High_priority_route operator and value, then restart the affected isolated process instance.",
            ),
            (
                "A duplicate Request ID is accepted.",
                "Stop the lab and ask the trainer to activate the Request ID alternate key; downstream exactly-once behaviour depends on it.",
            ),
        ],
        challenge=(
            "Add a Low-priority branch only if every route still reaches Closure. Draw the result and explain why "
            "a small number of explicit paths is easier to operate than deeply nested branching."
        ),
        reflection="What does full stage traversal prove that checking only the first branch decision does not?",
    ),
]
