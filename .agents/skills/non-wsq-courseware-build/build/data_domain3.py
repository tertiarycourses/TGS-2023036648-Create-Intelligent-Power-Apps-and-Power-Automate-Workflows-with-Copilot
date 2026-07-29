"""Topic 3 labs for C903: user inputs, profiles, date logic, calendars, and idempotency."""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Create a Validated User-Driven Follow-Up Flow",
        duration=30,
        objective=(
            "LO3: validate instant-flow inputs, retrieve the invoking user's minimum profile data, "
            "resolve one location variable through both branches, and format a follow-up date"
        ),
        goal=(
            "Let a coordinator request a follow-up for one RequestID and receive a confirmation built from "
            "validated input, a single resolved location value, and a consistently formatted date."
        ),
        workflow=["Define inputs", "Validate early", "Read minimum profile", "Set one location", "Exercise three cases"],
        desc=(
            "You will create an instant flow with RequestID, Follow-up Date, Work Mode, and Use Directory Location "
            "inputs. The flow normalises and validates Work Mode before reading profile data, requires exactly one "
            "SharePoint request, retrieves only Display Name, Mail, and Office Location, and sets one "
            "ResolvedLocation variable in both location branches."
        ),
        build=(
            "An instant cloud flow named C903-05-Create-User-Follow-Up with a four-field input contract, "
            "invalid-input termination, exactly-one lookup, minimum profile retrieval, and one branch-safe variable"
        ),
        services="Power Automate instant flows · SharePoint Online · Office 365 Users · Office 365 Outlook",
        prerequisites=[
            "Use your trainer-assigned isolated SharePoint list and approved Microsoft 365 training account.",
            "C903 Process Requests contains NW-1007 and NW-1008 exactly once.",
            "Know whether the training profile Office Location is populated; do not edit directory properties.",
            "The approved training profile has a populated Mail value. If it does not, stop and ask the trainer to "
            "repair the isolated account before the timed lab.",
            "The trainer has provisioned the inactive C903-05-Create-User-Follow-Up starter from "
            "labs/assets/c903-starter-solution-package-v1.0.md with its inputs, validation branches, lookup, profile, variable, "
            "date Compose, and email placeholders already arranged.",
        ],
        steps=[
            (
                "Open the inactive starter Instant cloud flow C903-05-Create-User-Follow-Up. Configure the existing "
                "Manually trigger a flow card and its four required inputs in this order with the stated guidance.",
                "RequestID - Text - example NW-1007\n"
                "Follow-up Date - Date - intended local calendar date\n"
                "Work Mode - Text - allowed values Office or Remote\n"
                "Use Directory Location - Yes/No - Yes uses a non-empty profile value; No uses Work Mode",
            ),
            (
                "Configure the existing Compose Normalised_work_mode with the expression below and Condition Work_mode_is_allowed to "
                "test whether the output equals office or remote. In the false branch configure Terminate with Status "
                "Cancelled, Code C903_INVALID_WORK_MODE, and message 'Use Office or Remote'. Put every later action "
                "in the valid branch so invalid input retrieves no profile data and sends no email.",
                "Normalisation pattern:\n"
                "toLower(trim(<Work Mode dynamic-content token>))\n\n"
                "Condition expression:\n"
                "or(equals(outputs('Normalised_work_mode'),'office'),equals(outputs('Normalised_work_mode'),'remote'))",
            ),
            (
                "In the valid branch configure the existing SharePoint - Get items Find_request_by_ID with Filter Query "
                "RequestID eq '<RequestID trigger token>'. Configure Condition Exactly_one_request using the array-length expression. "
                "If false, configure Terminate with Status Cancelled, Code C903_REQUEST_COUNT, and a message containing the "
                "actual count. If true, configure Office 365 Users - Get my profile (V2) Get_invoking_user_profile.",
                "Count expression:\n"
                "length(body('Find_request_by_ID')?['value'])\n"
                "Required count: 1\n\n"
                "Get my profile (V2) Select fields: displayName,mail,officeLocation\n"
                "Profile properties used later:\n"
                "Display Name | Mail | Office Location\n"
                "Do not retrieve or expose unrelated profile properties.",
            ),
            (
                "Configure the existing String variable ResolvedLocation with an empty initial value. "
                "Configure Condition Use_directory_location to require Use Directory Location = Yes and Office Location "
                "is not empty. In the true branch Set variable ResolvedLocation to Office Location. In the false branch "
                "Set variable ResolvedLocation to Normalised_work_mode. After the Condition configure Compose "
                "Follow_up_date_display and Send an email (V2).",
                "Date expression:\n"
                "formatDateTime(<Follow-up Date input>,'dd MMM yyyy')\n\n"
                "Subject: Follow-up recorded - <RequestID>\n"
                "Body: Hello <Display Name>; RequestID; RequestTitle; Follow-up Date; ResolvedLocation; "
                "and a note that isolated synthetic training data was used.\n"
                "To: profile Mail",
            ),
            (
                "Save, select Turn on, confirm the flow status is On, and exercise three cases without editing the flow "
                "definition. Record T14-T16 with input, branch, "
                "resolved value, profile properties exposed, final status, and message subject.",
                "T14 NW-1007 | Work Mode Remote | Use Directory Location Yes -> profile Office Location when non-empty, otherwise remote\n"
                "T15 NW-1008 | Work Mode Office | Use Directory Location No -> office\n"
                "T16 NW-1008 | Work Mode Airport | Use Directory Location No -> Cancelled C903_INVALID_WORK_MODE; "
                "profile and email actions do not run",
            ),
        ],
        test=(
            "The trigger must have four required inputs. T14 and T15 must find exactly one request and consume the same "
            "ResolvedLocation variable after the location Condition. T16 must terminate before profile retrieval and send "
            "no email. The two valid messages may expose only Display Name, Mail, resolved location, synthetic request "
            "fields, and the formatted date. No flow logic is edited between tests."
        ),
        checkpoint=(
            "Keep the final flow unchanged after T16 and save T14-T16. Lab 6 reuses the exactly-one RequestID pattern "
            "and adds date-time, duration, calendar, and duplicate validation. To rejoin, rerun T15 and confirm "
            "ResolvedLocation equals office through the real saved branch logic."
        ),
        troubleshooting=[
            (
                "Get items returns zero or more than one row.",
                "Inspect the exact RequestID input and isolated list, then use the count in C903_REQUEST_COUNT to correct the data instead of selecting an arbitrary row.",
            ),
            (
                "The email cannot access a branch-local location value.",
                "Confirm ResolvedLocation is initialised before the Condition and both branches use Set variable rather than separate Compose actions.",
            ),
            (
                "The profile Mail value is empty.",
                "Stop and ask the trainer to repair the isolated training profile. Do not add an unapproved fallback "
                "or retrieve extra profile fields during the timed lab.",
            ),
        ],
        challenge=(
            "Bind Work Mode to an Office/Remote choice control in the pre-provisioned C903 canvas app shell and "
            "explain how allowed values reduce downstream termination cases."
        ),
        reflection="How did early validation and one shared variable make the later email action safer and easier to inspect?",
    ),
    dict(
        num=6,
        topic=3,
        title="Block Calendar Time with Validation and Duplicate Prevention",
        duration=35,
        objective=(
            "LO3: validate request count, local ISO date-time, bounded duration, and future time; create one "
            "calendar event; persist its Event ID; and prove repeated invocation creates no duplicate"
        ),
        goal=(
            "Create one 45-minute follow-up block for NW-1007 and prove valid, repeat, invalid-format, "
            "out-of-range, past-time, and missing-request behaviour."
        ),
        workflow=["Validate request", "Parse safely", "Check range", "Create or reuse", "Count exact events"],
        desc=(
            "You will configure an instant calendar flow with a Try_parse_time scope and a separate Schedule_calendar "
            "scope. The flow requires "
            "exactly one SharePoint request, parses an ISO local start at runtime, enforces a 15-to-120-minute future "
            "window, and creates an Outlook event only when CalendarEventID is empty. Catch reports an invalid date "
            "format, while explicit Terminate actions close invalid count, range, and past-time cases."
        ),
        build=(
            "An instant cloud flow named C903-06-Block-Follow-Up-Time, one calendar event for NW-1007, "
            "a persisted Event ID, and evidence for six validation and duplicate cases"
        ),
        services="Power Automate instant flows · SharePoint Online · Office 365 Outlook Calendar · control scopes",
        prerequisites=[
            "Lab 5 is complete and NW-1007 exists exactly once in your isolated C903 Process Requests list.",
            "The approved training account can create events only in its own isolated calendar.",
            "Clear CalendarEventID on NW-1007 before T17 and choose a future Singapore local time.",
            "The trainer has provisioned the inactive C903-06-Block-Follow-Up-Time starter from "
            "labs/assets/c903-starter-solution-package-v1.0.md in your isolated environment "
            "with the trigger, named validation scope, conditions, calendar actions, and Catch placeholders already "
            "arranged; you configure the exact expressions, mappings, and tests during this 35-minute lab.",
        ],
        steps=[
            (
                "Open the inactive starter Instant cloud flow named C903-06-Block-Follow-Up-Time with required Text inputs RequestID "
                "and Start Local ISO plus required Number input Duration Minutes. Configure the existing SharePoint - Get items "
                "Find_calendar_request using your assigned training Site Address, list C903 Process Requests, and "
                "Filter Query RequestID eq '<RequestID trigger token>'. Configure Condition Exactly_one_calendar_request. In the false branch Terminate "
                "Cancelled with Code C903_REQUEST_COUNT and the returned array length.",
                "RequestID example: NW-1007\n"
                "Start Local ISO format: yyyy-MM-ddTHH:mm:ss\n"
                "Example: 2026-08-03T15:00:00\n"
                "Duration Minutes: 15 through 120\n"
                "Count expression: length(body('Find_calendar_request')?['value'])",
            ),
            (
                "In the valid-count branch configure the existing Scope Try_parse_time. Inside it configure Compose "
                "Start_local_normalised using formatDateTime and Compose Start_UTC and End_UTC using the patterns below. "
                "After Try configure Scope "
                "Catch_invalid_format for failed or timed-out Try only; filter result('Try_parse_time') to the first "
                "non-Succeeded action, record only action name, status, error code, and message, then Terminate "
                "Cancelled with Code C903_INVALID_ISO. After Catch configure Condition Range_and_future to run "
                "only when Catch is skipped, meaning parsing succeeded. Require duration 15-120 and local start later "
                "than the current Singapore time; in false Terminate Cancelled with Code C903_INVALID_WINDOW.",
                "Start_local_normalised:\n"
                "formatDateTime(<Start Local ISO>,'yyyy-MM-ddTHH:mm:ss')\n\n"
                "Start_UTC, no Z because Outlook receives a separate Time zone field:\n"
                "convertTimeZone(outputs('Start_local_normalised'),'Singapore Standard Time','UTC','yyyy-MM-ddTHH:mm:ss')\n\n"
                "End_UTC:\n"
                "addMinutes(outputs('Start_UTC'),int(<Duration Minutes>),'yyyy-MM-ddTHH:mm:ss')\n\n"
                "Range_and_future:\n"
                "and(greaterOrEquals(int(<Duration Minutes>),15),lessOrEquals(int(<Duration Minutes>),120),"
                "greater(ticks(outputs('Start_local_normalised')),ticks(convertTimeZone(utcNow(),'UTC','Singapore Standard Time'))))",
            ),
            (
                "In the valid Range_and_future branch configure the existing Scope Schedule_calendar, then inside it "
                "configure Condition Event_ID_is_empty using the expression below. If empty, configure Office 365 "
                "Scope Create_event_path containing Outlook - Create event (V4) Create_follow_up_event, the SharePoint "
                "update that preserves every existing schema field, and Confirm_event_created. If not empty, configure "
                "Scope Reuse_event_path containing Confirm_event_reused and create nothing. The named scopes make their "
                "leaf actions directly inspectable with result() if a connector fails.",
                "Event_ID_is_empty:\n"
                "empty(first(body('Find_calendar_request')?['value'])?['CalendarEventID'])\n\n"
                "Update item preserves RequestID, RequestTitle, RequesterEmail, Priority, Status, DueDate, "
                "ReminderSent, ApprovalOutcome, ApprovalComments, DataverseRowID, SQLAuditID, DiagnosticDivisor, and sets only "
                "CalendarEventID to the Create event result.\n\n"
                "Subject: C903 follow-up - <RequestID> - <RequestTitle>\n"
                "Start time: Start_UTC | End time: End_UTC | Time zone: UTC\n"
                "Show as: Busy | Attendees: none\n"
                "Body: Synthetic training request; RequestID; SharePoint item link\n"
                "Categories: C903-<RequestID>-FOLLOWUP\n\n"
                "Created and reused confirmations both include RequestID and the stored Event ID.",
            ),
            (
                "Still inside Schedule_calendar, after Event_ID_is_empty, configure Scope Verify_calendar_count. Inside "
                "it configure Get calendar view of events (V3), after the branches reconverge, with "
                "a window from one minute before Start_UTC to one minute after End_UTC. Configure Filter array "
                "Calendar_events_for_request, From = the Get calendar view value array, with advanced condition "
                "@contains(item()?['categories'],'C903-NW-1007-FOLLOWUP'). Then Compose Calendar_event_count with "
                "length(body('Calendar_events_for_request')). This ensures the T17 and T18 run histories both contain "
                "the bounded count evidence.",
                "Verify_calendar_count runs after Event_ID_is_empty succeeds. Its Get calendar view window and category "
                "filter are deliberately bounded to this synthetic request.",
            ),
            (
                "After Schedule_calendar configure the existing Scope Catch_calendar_technical for Schedule failed or timed "
                "out and not success. Filter the union of the three inner-scope results plus Schedule_calendar to failed, "
                "timed-out, or cancelled actions while excluding deliberately skipped branches; compose only "
                "action name, status, error code, and message, update the request to Automation Error while preserving "
                "all other fields, send one internal filtered-error alert, and Terminate Failed with Code "
                "C903_CALENDAR_TECHNICAL. Do not include a raw scope result in the alert. Save, select Turn on, confirm "
                "the flow status is On, and record six cases.",
                "Filter array name: Only_unsuccessful_calendar_actions\n"
                "From: union(result('Create_event_path'),result('Reuse_event_path'),"
                "result('Verify_calendar_count'),result('Schedule_calendar'))\n"
                "Filter condition: @or(equals(item()?['status'],'Failed'),equals(item()?['status'],'TimedOut'),"
                "equals(item()?['status'],'Cancelled'))\n\n"
                "Error_action: first(body('Only_unsuccessful_calendar_actions'))?['name']\n"
                "Error_status: first(body('Only_unsuccessful_calendar_actions'))?['status']\n"
                "Error_code: coalesce(first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['body']?['error']?['code'],"
                "first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['body']?['code'],"
                "first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['error']?['code'],"
                "first(body('Only_unsuccessful_calendar_actions'))?['error']?['code'],'NO_CODE_FROM_ACTION')\n"
                "Error_message: coalesce(first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['body']?['error']?['message'],"
                "first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['body']?['message'],"
                "first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['error']?['message'],"
                "first(body('Only_unsuccessful_calendar_actions'))?['error']?['message'],'No connector message returned')\n"
                "Record only these four values plus RequestID.\n\n"
                "This technical Catch never handles invalid ISO input or an invalid window; those paths terminate "
                "before Schedule_calendar starts.\n\n"
                "T17 NW-1007 | future valid time | 45 -> one created event and stored ID\n"
                "T18 repeat identical inputs -> reused branch; zero new events; filtered calendar count = 1\n"
                "T19 NW-1007 | future valid time | 5 -> Cancelled C903_INVALID_WINDOW\n"
                "T20 NW-1007 | not-a-date | 45 -> Catch -> Cancelled C903_INVALID_ISO\n"
                "T21 NW-1007 | yesterday local time | 45 -> Cancelled C903_INVALID_WINDOW\n"
                "T22 NW-9999 | future valid time | 45 -> Cancelled C903_REQUEST_COUNT\n\n"
                "After T17, open work-c903/C903-Correlation-Register.csv and update only CalendarEventID in the existing "
                "NW-1007 row with the stored SharePoint value; preserve SharePointItemID, DataverseRowID, SQLAuditID, "
                "all four run-time columns, and State. Do not append a duplicate row. After T18, verify the reused flow "
                "output, SharePoint CalendarEventID, Outlook event ID, and register CalendarEventID are identical.",
            ),
        ],
        test=(
            "T17 must create one 45-minute Busy event and persist its Event ID. T18 must reuse the same ID and the "
            "bounded Get calendar view plus category Filter array must return exactly one event. The existing NW-1007 "
            "correlation-register row must remain unique, preserve all ten columns, and carry the same CalendarEventID "
            "shown by T17/T18, SharePoint, and Outlook. T19-T22 must terminate on the stated validation path and create "
            "no event. Create event (V4) must receive date-time strings without Z "
            "and a separate UTC Time zone value. No attendees or non-synthetic request details are added. Before class, "
            "the trainer performs the bounded connector-failure acceptance check in the provisioning checklist; it must "
            "identify the leaf action and produce nonblank Error_code and Error_message (documented fallback text is "
            "acceptable only when the connector returns no structured detail). Learners do not induce this failure."
        ),
        checkpoint=(
            "Keep NW-1007 CalendarEventID populated, keep exactly one NW-1007 correlation-register row with the matching "
            "Event ID and all other columns preserved, and save T17-T22. Lab 7 uses a new NW-1009 record but carries the "
            "same exactly-one lookup and correlation-key discipline into Dataverse and SQL. To rejoin, rerun T18, confirm "
            "the filtered calendar count remains one, and reconcile the same ID across the run, SharePoint, Outlook, and "
            "the register."
        ),
        troubleshooting=[
            (
                "The event appears at the wrong local time.",
                "Inspect Start_local_normalised, Start_UTC, and End_UTC; confirm the source zone is Singapore Standard Time and Create event receives UTC without Z plus Time zone UTC.",
            ),
            (
                "The second run creates another event.",
                "Confirm the first update persisted CalendarEventID and Event_ID_is_empty reads the first returned SharePoint item's stored value before Create event.",
            ),
            (
                "An invalid date bypasses Catch.",
                "Place formatDateTime inside Try_parse_time and configure Catch_invalid_format for failed and timed-out "
                "Try_parse_time outcomes only.",
            ),
        ],
        challenge=(
            "Add a bounded update path that moves the existing event when a new valid start is supplied. Require the "
            "stored Event ID and preserve the correlation category rather than deleting and creating a new event."
        ),
        reflection="Which validation closes each bad-input path, and which stored value makes a repeat request idempotent?",
    ),
]
