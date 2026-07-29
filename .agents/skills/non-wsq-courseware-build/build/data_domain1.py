"""Topic 1 labs for C903: cloud-flow foundations, recurrence, sharing, and diagnosis."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Validate the Northwind Request Intake and Create an Automated Acknowledgement",
        duration=35,
        objective=(
            "LO1: create an automated cloud flow with a SharePoint trigger, explicit dynamic-content "
            "mapping, an Outlook notification, and traceable run evidence"
        ),
        goal=(
            "Validate the isolated request intake and prove that one new SharePoint item produces one "
            "acknowledgement containing the same RequestID."
        ),
        workflow=["Create list", "Load baseline", "Build flow", "Trigger test", "Trace evidence"],
        desc=(
            "You will inspect the pre-provisioned SharePoint list used throughout the course, verify five synthetic "
            "Northwind requests, and build an automated cloud flow that acknowledges every new request. You will rename "
            "the trigger and actions, map values deliberately, create a test request, and trace it from the "
            "SharePoint item through run history to the delivered message."
        ),
        build=(
            "A validated per-learner SharePoint list named C903 Process Requests, an automated cloud flow named "
            "C903-01-Acknowledge-New-Request, and a saved evidence record for RequestID NW-1006"
        ),
        services="SharePoint Online · Power Automate cloud flows · Office 365 Outlook",
        prerequisites=[
            "Sign in to the trainer-designated Microsoft 365 and Power Platform environment.",
            "Use only your trainer-assigned isolated SharePoint site and C903 Process Requests list; every learner has a separate list.",
            "Confirm NW-1001 through NW-1005 are already loaded and you can send an email to your own training mailbox.",
            "Open labs/assets/process-requests.csv and labs/assets/request-schema.md; use only the supplied synthetic records.",
        ],
        steps=[
            (
                "Create a local or approved OneDrive folder named work-c903. Copy labs/assets/test-evidence-template.csv "
                "into it and save the copy as C903-Test-Evidence.csv. Every test row you add must include your learner tag "
                "and its UTC test date; do not add a metadata row above the CSV header.",
                "Required evidence columns:\n"
                "LearnerTag | TestDateUTC | TestID | Flow | RequestID | Input | Expected | Actual | "
                "RunTimeUTC | RunLinkOrTimestamp | Result | RecoveryNote",
            ),
            (
                "On your isolated training SharePoint site, open C903 Process Requests. Compare every column with "
                "request-schema.md, including ApprovalComments and DiagnosticDivisor. Confirm the five NW-1001 through "
                "NW-1005 rows match process-requests.csv. If the list or rows differ, stop and ask the trainer to restore "
                "the supplied provisioning package; do not rebuild a shared class list during the timed lab.",
                "Required columns:\n"
                "RequestID - Single line of text\n"
                "RequestTitle - Single line of text\n"
                "RequesterEmail - Single line of text\n"
                "Priority - Choice: Low, Normal, High\n"
                "Status - Choice: New, Open, Pending Approval, Approved, More Info, Rejected, Scheduled, Closed, Automation Error\n"
                "DueDate - Date only\n"
                "ReminderSent - Yes/No, default No\n"
                "ApprovalOutcome - Single line of text\n"
                "ApprovalComments - Multiple lines of text\n"
                "CalendarEventID - Single line of text\n"
                "DataverseRowID - Single line of text\n"
                "SQLAuditID - Number\n"
                "DiagnosticDivisor - Number, default 1",
            ),
            (
                "In Power Automate, create an Automated cloud flow named C903-01-Acknowledge-New-Request. "
                "Choose SharePoint - When an item is created, select the training Site Address and C903 Process Requests, "
                "and rename the trigger New_request_received.",
                "Trigger contract:\n"
                "Business event: one item is created\n"
                "System of record: SharePoint C903 Process Requests\n"
                "Correlation key: RequestID\n"
                "Expected volume: classroom test records only",
            ),
            (
                "Add Data Operation - Compose, rename it Correlation_key, and set Inputs to RequestID dynamic content. "
                "Add Office 365 Outlook - Send an email (V2), rename it Send_acknowledgement, and map the fields exactly. "
                "Save the flow and resolve any connection prompt with the approved training account.",
                "To: RequesterEmail\n"
                "Subject: Request received - <RequestID> - <RequestTitle>\n"
                "Body:\n"
                "Hello,\n"
                "Northwind received request <RequestID>: <RequestTitle>.\n"
                "Priority: <Priority>\n"
                "Due date: <DueDate>\n"
                "This is an automated training notification.\n"
                "Correlation key: <output of Correlation_key>",
            ),
            (
                "Select Test - Manually, then create one new SharePoint item using the NW-1006 values below. "
                "Open the completed run, expand all three cards, and compare the trigger RequestID, Compose output, "
                "email inputs, and delivered message. Add test T01 to C903-Test-Evidence.csv.",
                "NW-1006 test record:\n"
                "RequestTitle: Prepare weekly service summary\n"
                "RequesterEmail: <YOUR_TRAINING_EMAIL>\n"
                "Priority: Normal\n"
                "Status: New\n"
                "DueDate: <TOMORROW>\n"
                "ReminderSent: No\n\n"
                "Expected: exactly one successful run and one email; every occurrence of the correlation key is NW-1006.",
            ),
        ],
        test=(
            "The isolated SharePoint list must contain NW-1001 through NW-1006 with the exact schema. A single new NW-1006 item "
            "must create one successful run. The trigger input, Correlation_key output, email subject, email body, and "
            "T01 evidence row must all contain NW-1006. The email must show the mapped title, priority, and due date and "
            "must not contain any unrelated list field."
        ),
        checkpoint=(
            "Leave C903-01-Acknowledge-New-Request turned on and save C903-Test-Evidence.csv in work-c903. "
            "Lab 2 uses the same isolated list and adds reminder behaviour. If you need to rejoin, ask the trainer "
            "to restore the provisioned list from request-schema.md and process-requests.csv, then run the NW-1006 check."
        ),
        troubleshooting=[
            (
                "No run appears after the item is created.",
                "Confirm the flow is on, the trigger points to the same site and list, and the item was newly created rather than edited. Wait for the connector polling interval, then inspect the trigger again.",
            ),
            (
                "The email action uses the wrong field.",
                "Open the failed or incorrect run, compare the action input with the trigger output, remove the token, and reselect the exact dynamic-content field by its column name.",
            ),
            (
                "The training email does not arrive.",
                "Verify Send_acknowledgement is green, inspect its To and Subject inputs, record the flow run timestamp, "
                "check the training mailbox junk folder, and match the delivered message subject and received time. "
                "Send an email (V2) does not provide a message ID output.",
            ),
        ],
        challenge=(
            "Add a link to the SharePoint item in the email without hard-coding an item number. Explain which trigger "
            "output supplies the link and how the link remains tied to the same RequestID."
        ),
        reflection="Which run-history value gives the strongest evidence that the email belongs to the correct request, and why?",
    ),
    dict(
        num=2,
        topic=1,
        title="Build a Scheduled Reminder and Diagnose a Controlled Failure",
        duration=30,
        objective=(
            "LO1: build a scheduled cloud flow, filter and iterate SharePoint records, update reminder state, "
            "diagnose a runtime expression failure, retest, and share maintenance ownership"
        ),
        goal=(
            "Send one reminder for each due open request, prevent duplicate reminders, and prove that run history "
            "can locate and recover a deliberately introduced fault."
        ),
        workflow=["Schedule", "Filter", "Remind", "Break safely", "Recover and share"],
        desc=(
            "You will build a scheduled flow that finds open requests due today, sends one reminder, and marks each "
            "item so the next run does not resend it. You will insert a temporary divide-by-zero expression, use run "
            "history to find the first red action, restore the supplied divisor, retest the same expression, and share the flow with a trainer-designated "
            "co-owner for continuity."
        ),
        build=(
            "A scheduled cloud flow named C903-02-Remind-Due-Requests, evidence rows for normal, empty, duplicate, "
            "and controlled-failure cases, and a recorded primary and backup owner"
        ),
        services="Power Automate scheduled flows · SharePoint Online · Office 365 Outlook",
        prerequisites=[
            "Lab 1 is complete and C903 Process Requests contains the baseline data plus NW-1006.",
            "C903-Test-Evidence.csv is available in work-c903.",
            "Obtain the trainer-designated co-owner email; do not share with an unapproved account.",
            "The trainer has provisioned the inactive C903-02-Remind-Due-Requests starter from "
            "labs/assets/c903-starter-solution-package-v1.0.md with its named trigger, loop, Condition, Compose, email, and update "
            "placeholders already arranged.",
        ],
        steps=[
            (
                "Update SharePoint item NW-1002 so Status is Open, DueDate is today, RequesterEmail is your training "
                "email, ReminderSent is No, and DiagnosticDivisor is 1. Set every other item to either a future DueDate "
                "or ReminderSent Yes.",
                "Controlled test state:\n"
                "Qualifying rows = exactly 1\n"
                "Qualifying RequestID = NW-1002\n"
                "Expected first run = one reminder and ReminderSent changes to Yes",
            ),
            (
                "Open the inactive starter Scheduled cloud flow named C903-02-Remind-Due-Requests. Configure the existing "
                "Recurrence to every 1 day, "
                "Time zone to (UTC+08:00) Kuala Lumpur, Singapore, and start time to the next 4:00 pm Singapore slot. "
                "Confirm the trigger is named Daily_1600_SGT. Configure the existing SharePoint Get items "
                "Find_due_open_requests, Apply to each For_each_candidate, and Condition Due_date_is_today with the "
                "exact values below.",
                "Site Address: <TRAINING_SITE>\n"
                "List Name: C903 Process Requests\n"
                "Filter Query:\n"
                "Status eq 'Open' and ReminderSent eq 0\n\n"
                "Condition expression:\n"
                "equals(\n"
                "  formatDateTime(items('For_each_candidate')?['DueDate'],'yyyy-MM-dd'),\n"
                "  formatDateTime(convertTimeZone(utcNow(),'UTC','Singapore Standard Time'),'yyyy-MM-dd')\n"
                ")",
            ),
            (
                "In the matching branch, configure the existing Compose Runtime_diagnostic_check before the message to divide "
                "1 by the current item's DiagnosticDivisor so a supplied zero becomes a runtime test fault rather than an "
                "invalid constant. Configure the existing Send an email (V2) Send_due_reminder and SharePoint - Update "
                "item Mark_reminder_sent. Map the current item's ID, required list fields, and set ReminderSent to Yes. "
                "Save, select Turn on, confirm the flow status is On, and use Test - Manually to execute the scheduled flow immediately.",
                "Runtime expression:\n"
                "div(1,int(items('For_each_candidate')?['DiagnosticDivisor']))\n\n"
                "Email subject: Due today - <RequestID> - <RequestTitle>\n"
                "Body: Request <RequestID> is due today. Open the SharePoint item and update its status.\n\n"
                "Evidence T02 expected:\n"
                "one email for NW-1002; the SharePoint row changes ReminderSent from No to Yes.",
            ),
            (
                "Run the flow a second time without changing the list and record T03 as the duplicate-prevention case. "
                "Then set NW-1002 ReminderSent to No and DueDate to tomorrow, run again, and record T04 as the false-date "
                "case. Confirm the loop runs, Due_date_is_today is false, and no message or update action runs.",
                "Expected T03: Find_due_open_requests returns zero qualifying rows; zero reminder emails.\n"
                "Expected T04: NW-1002 enters the loop but takes the false date branch; zero reminder emails.\n"
                "These are separate evidence rows.",
            ),
            (
                "Set NW-1002 DueDate back to today, ReminderSent to No, and DiagnosticDivisor to 0. Run the flow and record "
                "T05: Runtime_diagnostic_check must be the first red action and no email is sent. Set DiagnosticDivisor to 1, "
                "open the failed run, select Resubmit, and record the successful recovery as T06. Open the flow details page, add the trainer-designated "
                "co-owner, and record the primary owner, backup owner, Outlook connection owner, and monitoring check in "
                "work-c903/C903-Ownership-Record.txt.",
                "Ownership record:\n"
                "Flow: C903-02-Remind-Due-Requests\n"
                "Primary owner: <YOUR_TRAINING_EMAIL>\n"
                "Backup owner: <TRAINER_DESIGNATED_EMAIL>\n"
                "Connection owner: <TRAINING_ACCOUNT>\n"
                "Monitor: check the next scheduled run and investigate any red action\n"
                "Recovery evidence: T05 runtime failure and T06 successful resubmission",
            ),
        ],
        test=(
            "T02 must show one reminder and ReminderSent set to Yes for NW-1002. T03 must prove repeat-run duplicate "
            "prevention, and T04 must prove the false-date branch. T05 must identify Runtime_diagnostic_check as the first "
            "red action with DiagnosticDivisor 0; T06 must resubmit successfully after the divisor is restored to 1 and set "
            "ReminderSent to Yes. The final flow must be on and list the approved primary and backup owners."
        ),
        checkpoint=(
            "Keep NW-1002 as Open with ReminderSent Yes and DiagnosticDivisor 1. Save the ownership record and T02-T06 evidence. "
            "Lab 3 reuses the SharePoint list and adds approval logic for High-priority requests. To rejoin, "
            "confirm Labs 1 and 2 flows are on and a repeated reminder run creates no duplicate message."
        ),
        troubleshooting=[
            (
                "Get items returns more records than expected.",
                "Inspect Status and ReminderSent values in SharePoint, verify the internal field types, and keep the date comparison inside the loop until the exact date format is confirmed.",
            ),
            (
                "Update item clears a required field.",
                "Map the current item's ID and every required column in Update item. Inspect the action inputs before retrying.",
            ),
            (
                "The second run sends another reminder.",
                "Confirm Mark_reminder_sent completed successfully, inspect the stored Yes/No value, and verify Find_due_open_requests filters ReminderSent eq 0.",
            ),
        ],
        challenge=(
            "Replace the loop-level date Condition with a source-side date filter only after you verify the SharePoint "
            "internal column name and ISO date literal. Compare the number of retrieved rows and explain the efficiency trade-off."
        ),
        reflection="How did the symptom tell you whether to inspect the trigger, the first red action, or the data mapping?",
    ),
]
