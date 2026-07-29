"""Single source of truth for the C903 non-WSQ courseware package."""

TITLE = "PL-7002 Create and Manage Automated Processes by using Power Automate"
SHORT_TITLE = "PL-7002 Create and Manage Automated Processes by using Power Automate"
COURSE_CODE = "C903"
COURSE_PAGE = (
    "https://www.tertiarycourses.com.sg/"
    "pl-7002-create-and-manage-automated-processes-by-using-power-automate.html"
)
VERSION = "v1.0"
VERSION_DATE = "29 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Assigned Tertiary Infotech Academy Trainer"
DAYS = 1
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led demonstrations with eight connected hands-on labs"
DAILY_TIMING = (
    "9:30 am - 6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

TRAINER_TEAM = [
    (
        "Assigned Tertiary Infotech Academy Trainer",
        "Power Platform practitioner experienced in cloud-flow design, business-process automation, "
        "data integration, monitoring, and operational handover.",
    ),
]

TRAINER_PREPARATION = [
    "Use labs/assets/c903-starter-solution-package-v1.0.md and "
    "labs/assets/trainer-provisioning-checklist.md as the authoritative pre-class provisioning contract.",
    "Prepare one isolated SharePoint site/list, Power Platform environment, Outlook calendar, and SQL database or "
    "schema per learner; label every resource with the assigned learner tag.",
    "In solution C903 Northwind Automation version 1.0.0.0, provision the inactive starter flows named "
    "C903-02-Remind-Due-Requests, C903-03-Approve-High-Priority-Request, "
    "C903-05-Create-User-Follow-Up, C903-06-Block-Follow-Up-Time, "
    "C90307A_PowerApps_Submit_Request, and C90307B_Audit_Dataverse_Request.",
    "Verify every named trigger, scope, condition, switch case, placeholder action, input, and response against the "
    "versioned starter package; learners configure existing cards rather than building blank flows.",
    "Bind only the approved per-learner SharePoint, Outlook, Office 365 Users, Dataverse, Power Apps, and SQL "
    "connection references; confirm the SQL gateway and least-privilege DDL/DML rights are healthy.",
    "Confirm every learner and trainer account has the required Power Apps/Power Automate premium entitlement for "
    "Dataverse and SQL, and confirm the environment DLP policy permits the documented connectors together.",
    "Provision the C903 Request Launcher app shell, C903 Automation Requests table, active Request ID alternate key, "
    "business-process prerequisites (table, form, and model-driven app), synthetic SharePoint baseline, and "
    "trainer-designated backup owner. Learners create the conditional business process flow in Lab 4.",
    "In a disposable trainer copy of C903-06-Block-Follow-Up-Time, perform the checklist's bounded Outlook "
    "connector-failure acceptance check, verify the Catch records a leaf action plus nonblank error code and message, "
    "then restore the Calendar ID, retest the success path, and discard the copy.",
    "Before class, keep all starter flows off, clear CalendarEventID/DataverseRowID/SQLAuditID test values, confirm "
    "DiagnosticDivisor defaults to 1, and complete every Ready check in the trainer checklist.",
]

ICE_BREAKER = [
    "Your name, organisation, and role.",
    "One repeated task you would like to automate.",
    "The event that should start the automation.",
    "The evidence that would prove the automation worked.",
]

LEARNING_OUTCOMES = [
    (
        "LO1: Design, build, test, share, and troubleshoot cloud flows by selecting appropriate "
        "triggers, actions, recurrence settings, dynamic content, and run-history evidence."
    ),
    (
        "LO2: Implement conditional logic, approval patterns, run-after behaviour, and a conditional "
        "business process flow for a governed request lifecycle."
    ),
    (
        "LO3: Create user-driven flows that use explicit inputs, Microsoft 365 user information, "
        "date and time logic, and calendar actions while controlling duplicates and data exposure."
    ),
    (
        "LO4: Integrate SharePoint, Power Apps, Dataverse, Dynamics 365 patterns, and SQL; then "
        "monitor, share, own, and document a reliable automated process."
    ),
]

LO_TITLES = [
    "Build & Diagnose",
    "Approve & Branch",
    "Personalise & Schedule",
    "Integrate & Operate",
]

TOPIC_RECAPS = {
    1: [
        (
            "LO1 - Build and Diagnose",
            "Choose a trigger that matches the business event, configure actions with explicit data, "
            "test both expected and exceptional paths, and use run history to locate the first failure.",
        ),
    ],
    2: [
        (
            "LO2 - Approve and Branch",
            "Use an approval only where a person must decide, branch on the returned outcome, configure "
            "failure paths deliberately, and distinguish a cloud flow from a stage-based business process flow.",
        ),
    ],
    3: [
        (
            "LO3 - Personalise and Schedule",
            "Collect the minimum user input, resolve profile and date values predictably, convert time zones, "
            "and use a stable identifier to avoid creating duplicate calendar events.",
        ),
    ],
    4: [
        (
            "LO4 - Integrate and Operate",
            "Select connectors by system of record, identity, licensing, policy, and latency; preserve a shared "
            "correlation ID; then hand over the flow with owners, monitoring checks, and a tested recovery path.",
        ),
    ],
}

TOPICS = [
    dict(
        num=1,
        code="01",
        title="Get Started with Power Automate",
        subtitle=(
            "Cloud-flow anatomy · automated, instant, and scheduled triggers · dynamic content · "
            "testing · sharing · run history · troubleshooting"
        ),
        weighting="Morning foundation · 2 connected labs",
        concepts=[
            (
                "Trigger",
                "The event or schedule that creates one flow run and supplies the initial data payload.",
            ),
            (
                "Action",
                "A configured operation that reads, transforms, sends, creates, or updates data after the trigger.",
            ),
            (
                "Connection",
                "The authenticated relationship a connector uses to act against a service under an identity.",
            ),
            (
                "Dynamic content",
                "A token that carries a value from a trigger or earlier action into a later field.",
            ),
            (
                "Run history",
                "The evidence trail for trigger input, action input and output, duration, status, and error details.",
            ),
            (
                "Ownership",
                "The people or service identity responsible for editing, licensing, connections, monitoring, and recovery.",
            ),
        ],
        sections=[
            dict(
                title="Cloud-Flow Anatomy and Trigger Selection",
                definition=(
                    "A cloud flow is an event-driven sequence made of one trigger followed by actions, control "
                    "steps, and data transformations. Automated flows react to a service event, scheduled flows "
                    "start from a recurrence, and instant flows start when a person or app invokes them. The trigger "
                    "creates the run and provides the first payload; every later action consumes values from that "
                    "payload or from earlier outputs."
                ),
                why=(
                    "Trigger choice determines when work starts, which identity and data are available, how often "
                    "the service is queried, and whether duplicate events are possible. Starting from the business "
                    "event instead of from a favourite connector keeps the automation aligned with the process. "
                    "A good design states the event, system of record, expected volume, latency, and evidence of success."
                ),
                how=[
                    "Write the business event as: When <event> occurs in <system>, automate <outcome> for <recipient>.",
                    "Choose automated, scheduled, or instant based on who or what controls the start.",
                    "Inspect the trigger schema and identify the stable record ID, timestamps, owner, and business fields.",
                    "Add only the actions needed to reach an observable result, then rename every card by intent.",
                    "Test with a known record and compare trigger input, action output, and target-system evidence.",
                ],
                example=[
                    "A new item in the Northwind Process Requests SharePoint list starts an automated flow.",
                    "The flow captures Request ID, title, requester, priority, and due date, then sends an acknowledgement.",
                    "The run is successful only when run history is green and the acknowledgement contains the same Request ID.",
                ],
                use_when=[
                    "A repeatable event has a clear owner, stable data source, and observable downstream outcome.",
                    "The service connector exposes the required trigger and the running identity is permitted to use it.",
                ],
                avoid_when=[
                    "The event is ambiguous, the process changes on every occurrence, or a person must first judge whether work should start.",
                    "The design cannot identify a stable record key or would repeatedly process the same event without a duplicate guard.",
                ],
                quality=[
                    ("Event", "Name the exact event and the system that owns it."),
                    ("Payload", "Identify required fields, types, null cases, and one stable correlation key."),
                    ("Evidence", "Define the target record, message, or run output that proves success."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/power-automate/flow-types",
                    "https://learn.microsoft.com/en-us/power-automate/get-started-logic-flow",
                    "https://learn.microsoft.com/en-us/training/modules/get-started-flows/",
                ],
            ),
            dict(
                title="Recurrence, Event Triggers, and Data Mapping",
                definition=(
                    "A recurrence trigger creates runs at a configured interval, start time, and time zone. An event "
                    "trigger reacts when a connected service reports that a record was created or changed. Dynamic "
                    "content maps fields from the trigger or an earlier action into later actions; expressions transform "
                    "those values when simple token mapping is not enough."
                ),
                why=(
                    "Scheduled and event-driven patterns solve different timing problems. A recurrence is appropriate "
                    "for periodic sweeps such as overdue-request reminders, while an event trigger is appropriate for a "
                    "new request acknowledgement. Explicit data mapping prevents a common defect: a flow that runs "
                    "successfully but sends the wrong field, formats a date incorrectly, or processes records outside scope."
                ),
                how=[
                    "For recurrence, set frequency, interval, start time, and the Singapore time zone explicitly.",
                    "For an event trigger, create a fresh test event and allow for the connector's polling behaviour.",
                    "Use Filter Query or trigger conditions to reduce unnecessary runs when the connector supports them.",
                    "Map dynamic content by business meaning, not by a similar-looking display name.",
                    "Use Compose for intermediate values so the run history exposes the value used by later steps.",
                ],
                example=[
                    "At 4:00 pm every day, a scheduled flow queries Open requests whose ReminderSent flag is No, "
                    "then checks whether each Due Date is today in Singapore.",
                    "A Runtime diagnostic Compose reads the supplied Diagnostic Divisor before Outlook sends the "
                    "Request ID and Title reminder and SharePoint marks ReminderSent Yes.",
                    "The designer proves one due item sends once, a repeated run sends nothing, a tomorrow item takes "
                    "the false path, and a supplied zero creates a controlled runtime failure.",
                ],
                use_when=[
                    "A periodic business rule can query a bounded set and tolerate the chosen interval.",
                    "An expression or Compose step makes a derived value easier to inspect and reuse.",
                ],
                avoid_when=[
                    "The process requires immediate response but the selected connector uses a long polling interval.",
                    "A broad scheduled query would retrieve an unbounded dataset or resend the same item without a sent flag.",
                ],
                quality=[
                    ("Clock", "Record time zone, start time, interval, and daylight-saving implications."),
                    ("Scope", "Filter at the source and define what happens when zero, one, or many rows return."),
                    ("Mapping", "Trace each dynamic token to its producing trigger or action."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/training/modules/get-started-flows/",
                    "https://learn.microsoft.com/en-us/power-automate/triggers-introduction",
                    "https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions",
                ],
            ),
            dict(
                title="Testing, Run History, Sharing, and Troubleshooting",
                definition=(
                    "Testing executes a flow with controlled input and records the resulting run. Run history exposes "
                    "the status, duration, inputs, outputs, retries, and error message for each step. Sharing can make "
                    "another person a co-owner who can edit and maintain the flow, or a run-only user who can invoke an "
                    "instant flow without redesigning it."
                ),
                why=(
                    "A green designer is not proof of a reliable process. The flow must be exercised with representative "
                    "data, branch boundaries, empty values, and expected failures. Troubleshooting begins with the symptom: "
                    "no run indicates a trigger problem; a red step indicates an action or connection problem; an all-green "
                    "run with a wrong outcome indicates data mapping or logic. Ownership and connection planning prevent "
                    "a useful flow from stopping when its maker changes role."
                ),
                how=[
                    "Save, run a manual test, and capture the run URL or timestamp with the test record ID.",
                    "If no run exists, inspect trigger event, conditions, status, schedule, and connector polling.",
                    "If an action fails, open the first red action and read its inputs, outputs, status code, and connection.",
                    "If the run is green but wrong, compare dynamic content and expressions with the source record.",
                    "Share with the least privilege needed, confirm connections, and record primary and backup owners.",
                ],
                example=[
                    "A reminder flow saves but no run appears because the recurrence start time is tomorrow.",
                    "After correcting the start time, the Outlook action fails with 401 because its connection expired.",
                    "The maker fixes the connection, retests one known item, and records the successful run before handover.",
                ],
                use_when=[
                    "A controlled test record can be traced from trigger to target without exposing production-sensitive data.",
                    "A team-owned business process needs documented co-owners, connection responsibilities, and monitoring.",
                ],
                avoid_when=[
                    "Testing would send real external messages or modify live records without a safe test boundary.",
                    "A flow is shared without checking whether recipients can access the underlying connections and data.",
                ],
                quality=[
                    ("Coverage", "Test normal, boundary, empty, and deliberately failing cases."),
                    ("Diagnosis", "Locate the first divergence between expected and actual inputs or outputs."),
                    ("Continuity", "Name owners, connection identity, monitoring cadence, and recovery action."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/power-automate/troubleshoot-flow-errors",
                    "https://learn.microsoft.com/en-us/power-automate/create-team-flows",
                    "https://learn.microsoft.com/en-us/power-automate/change-cloud-flow-owner",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Build Approval Flows with Power Automate",
        subtitle=(
            "Approval patterns · conditional logic · custom responses · trigger conditions · "
            "run-after paths · business process flows · conditional stages"
        ),
        weighting="Midday decisions · 2 connected labs",
        concepts=[
            (
                "Approval",
                "A human decision step that records an outcome, responder, comments, and completion time.",
            ),
            (
                "Condition",
                "A two-branch control that evaluates a Boolean comparison after a run has started.",
            ),
            (
                "Trigger condition",
                "An expression evaluated before the run is created, reducing unnecessary executions.",
            ),
            (
                "Run after",
                "A dependency setting that selects which next action runs after success, failure, skip, or timeout.",
            ),
            (
                "Business process flow",
                "A Dataverse-backed stage and step experience that guides a person through a consistent record lifecycle.",
            ),
            (
                "Branching",
                "A rule that changes the next path when data or a human decision meets defined criteria.",
            ),
        ],
        sections=[
            dict(
                title="Approval Patterns and Human Decision Points",
                definition=(
                    "Power Automate approvals combine an automated flow with a recorded human response. Start and wait "
                    "for an approval pauses the run until the configured response condition is met. The approval type "
                    "controls whether the first response, every response, a sequence, or custom response options complete "
                    "the step. The returned outcome and comments become data for later branches."
                ),
                why=(
                    "An approval is useful where policy requires a named person to accept, reject, or request clarification. "
                    "It should not be added merely to make a flow look governed. The design must state who decides, what "
                    "evidence they receive, how long they have, what each outcome means, and what happens if no one responds."
                ),
                how=[
                    "Define the decision, approver role, evidence, response options, timeout expectation, and audit record.",
                    "Choose first response, all responses, sequential, or custom responses based on the actual rule.",
                    "Build the approval title from a stable Request ID and keep the details concise and traceable.",
                    "Branch on the exact returned Outcome value and persist outcome, responder, comments, and completion time.",
                    "Notify the requester and update the system of record on every designed outcome.",
                ],
                example=[
                    "A high-priority Northwind request creates an approval for the operations manager.",
                    "The approver chooses Approve, Need more information, or Reject and adds a comment.",
                    "The flow updates SharePoint with the exact outcome and sends the requester a matching message.",
                ],
                use_when=[
                    "A policy or risk decision needs a named responder and durable decision evidence.",
                    "The approver receives enough context and has access to any linked supporting record.",
                ],
                avoid_when=[
                    "The decision can be expressed safely as a deterministic rule with no human judgment.",
                    "The flow has no designed timeout, escalation, cancellation, or ownership path for unanswered requests.",
                ],
                quality=[
                    ("Decision", "State one question and define every allowed response."),
                    ("Evidence", "Include only the facts and secure links the approver needs."),
                    ("Closure", "Persist outcome and notify the correct people on every path."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/power-automate/get-started-approvals",
                    "https://learn.microsoft.com/en-us/power-automate/modern-approvals",
                    "https://learn.microsoft.com/en-us/power-automate/create-approval-response-options",
                ],
            ),
            dict(
                title="Conditional Logic, Trigger Conditions, and Run-After Paths",
                definition=(
                    "A Condition action branches after a run begins. A trigger condition is evaluated at the trigger and "
                    "can prevent an unwanted run from being created. Configure run after changes dependency behaviour so an "
                    "action can execute after success, failure, skip, or timeout. Together these controls separate business "
                    "rules from technical recovery behaviour."
                ),
                why=(
                    "Conditions decide what the process should do with valid data; run-after settings decide what the flow "
                    "should do when a step does not complete normally. Mixing them produces brittle designs. Trigger "
                    "conditions can reduce noise and request consumption, but an incorrect expression can silently suppress "
                    "all runs, so the expression and a known qualifying record must be tested together."
                ),
                how=[
                    "Write each business rule in plain language with field, operator, value, and null behaviour.",
                    "Use a Condition after the trigger when both qualifying and non-qualifying runs need recorded outcomes.",
                    "Use a trigger condition when non-qualifying events should create no run and that absence is acceptable.",
                    "Group critical actions in a Try Scope and configure Catch to run after failure, timeout, or skip.",
                    "Record the error, Request ID, failed step, and recovery owner before sending a controlled alert.",
                ],
                example=[
                    "Only High-priority requests need human approval; other priorities continue automatically.",
                    "A Try Scope creates the approval and updates SharePoint. Catch runs only if Try fails or times out.",
                    "The Catch path writes an Automation Error status and sends one internal notification with the Request ID.",
                ],
                use_when=[
                    "Branch rules are explicit and test data can exercise both true and false paths.",
                    "A technical failure must create a controlled record and alert instead of silently stopping the process.",
                ],
                avoid_when=[
                    "A trigger condition would hide events that operations still needs to count or explain.",
                    "Configure run after is used to ignore failure without recording what failed and who will recover it.",
                ],
                quality=[
                    ("Rule", "Document field type, operator, comparison value, and null case."),
                    ("Path", "Name branches by business meaning instead of Yes and No."),
                    ("Recovery", "Capture error context once and route it to a named owner."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions",
                    "https://learn.microsoft.com/en-us/power-automate/triggers-introduction",
                    "https://learn.microsoft.com/en-us/power-automate/guidance/coding-guidelines/error-handling",
                ],
            ),
            dict(
                title="Business Process Flows and Conditional Stages",
                definition=(
                    "A business process flow is a Dataverse-backed, stage-based user experience attached to one or more "
                    "tables. It guides users through defined stages and data steps while the underlying model-driven app "
                    "stores the record. Conditional branching can direct a record to different stages based on field values. "
                    "A business process flow guides interactive work; a cloud flow automates operations around records."
                ),
                why=(
                    "Some processes require people to see the current stage, complete required data, and move the record "
                    "forward consistently. A cloud flow alone is not a user guidance surface. Combining the two patterns lets "
                    "the business process flow govern stage progression while cloud flows notify, approve, integrate, and "
                    "monitor around the record."
                ),
                how=[
                    "Model the lifecycle as a small number of named stages with an owner and exit evidence for each stage.",
                    "Create the Dataverse table and required columns before designing the stage path.",
                    "Add data steps to stages and mark only genuinely required information as required.",
                    "Add a branch rule on a stable field such as Priority or Approval Required, then validate and activate.",
                    "Test one record through each branch and confirm both the active stage and the stored field values.",
                ],
                example=[
                    "Northwind uses Intake, Review, Approval, Fulfilment, and Closure stages for automation requests.",
                    "A high-priority record enters Approval after Review; a standard request moves directly to Fulfilment.",
                    "The record ID remains constant while cloud flows update status and notify the request owner.",
                ],
                use_when=[
                    "People need a visible stage path and consistent data capture on a Dataverse record.",
                    "The organisation has an environment, table, app, roles, and licensing suitable for the process.",
                ],
                avoid_when=[
                    "The process is entirely system-to-system with no need for an interactive stage experience.",
                    "A complex diagram is being reproduced without simplifying stages, ownership, and exit criteria first.",
                ],
                quality=[
                    ("Stage", "Each stage has a clear purpose, owner, required data, and exit condition."),
                    ("Branch", "Branch rules use stable values and every path reaches a defined end."),
                    ("Integration", "Cloud flows reference the same Dataverse record ID and do not duplicate process state."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview",
                    "https://learn.microsoft.com/en-us/power-automate/create-business-process-flow",
                    "https://learn.microsoft.com/en-us/power-automate/enhance-business-process-flows-branching",
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Build Flows to Manage User Information",
        subtitle=(
            "Instant flow inputs · Office 365 Users · location and date values · "
            "time-zone conversion · calendar events · privacy · duplicate prevention"
        ),
        weighting="Afternoon personal productivity · 2 connected labs",
        concepts=[
            (
                "Instant input",
                "A typed value supplied by the person or app that invokes an instant cloud flow.",
            ),
            (
                "User profile",
                "Directory information returned by the Microsoft 365 Users connection for an authorised identity.",
            ),
            (
                "Expression",
                "A formula that transforms, validates, combines, or defaults values during a run.",
            ),
            (
                "Time zone",
                "The regional offset and daylight rule needed to interpret a local date and time correctly.",
            ),
            (
                "Idempotency",
                "The property that repeating the same request does not create an unintended duplicate outcome.",
            ),
            (
                "Minimum data",
                "The smallest set of user information needed to achieve the declared automation purpose.",
            ),
        ],
        sections=[
            dict(
                title="Instant Flows and User-Input Contracts",
                definition=(
                    "An instant cloud flow starts when a person selects a button or when Power Apps invokes the flow. "
                    "The trigger can define typed inputs such as text, number, Boolean, email, date, or file. Those inputs "
                    "form a contract between the user interface and the automation: names, required values, allowed values, "
                    "defaults, and validation must be explicit."
                ),
                why=(
                    "User-driven automation is appropriate when a person decides when work should begin and supplies context "
                    "that no system event contains. Poor input design moves ambiguity into later actions. A short, typed input "
                    "contract reduces errors, makes test cases repeatable, and avoids collecting unnecessary personal data."
                ),
                how=[
                    "Define the user decision and the minimum fields the flow needs to act.",
                    "Name inputs with business terms and include format guidance in the prompt or app.",
                    "Validate required values and allowed options before calling downstream connectors.",
                    "Create a correlation key from the request ID and invocation time or another stable input.",
                    "Return a concise confirmation containing the correlation key and next action.",
                ],
                example=[
                    "A coordinator runs an instant flow for Request NW-1007 and enters a follow-up date and work mode.",
                    "The flow retrieves the coordinator's profile and selects an office or remote message branch.",
                    "The confirmation contains the Request ID, selected date, and resolved location without exposing "
                    "extra profile fields or promising a request link.",
                ],
                use_when=[
                    "A person must choose the start moment or provide a small amount of current context.",
                    "The flow can validate input before creating messages, calendar events, or records.",
                ],
                avoid_when=[
                    "The process should start automatically from a reliable source-system event.",
                    "The trigger asks for sensitive or irrelevant personal information that the process does not need.",
                ],
                quality=[
                    ("Contract", "Name every input, type, required state, allowed value, and default."),
                    ("Validation", "Stop early with a useful message when data is missing or malformed."),
                    ("Confirmation", "Return the correlation key and the exact outcome created."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/training/modules/manage-user-information/",
                    "https://learn.microsoft.com/en-us/power-automate/button-flow-with-user-input-tokens",
                    "https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows",
                ],
            ),
            dict(
                title="Profile, Location, Date, and Time Logic",
                definition=(
                    "The Office 365 Users connector can retrieve profile properties for the signed-in or named organisational "
                    "user. Date and time values arrive in specific formats and time zones; expressions such as formatDateTime, "
                    "addDays, coalesce, and convertTimeZone transform them. Location may come from an explicit input or an "
                    "authorised directory property and should be used only for the declared purpose."
                ),
                why=(
                    "Personalised flows fail when a display name is used where an email is required, an optional profile field "
                    "is null, or an unlabelled timestamp is interpreted in the wrong time zone. Explicit types, null handling, "
                    "and time-zone conversion make the result predictable. Minimum-data design reduces privacy and maintenance "
                    "risk by retrieving only what later actions use."
                ),
                how=[
                    "Use the signed-in user's email or object identity as the profile lookup key.",
                    "Inspect which profile fields can be empty and apply coalesce only with a truthful default.",
                    "Keep UTC for system comparison and convert to Singapore Standard Time for local communication.",
                    "Format dates only at the presentation boundary; preserve the original machine-readable value.",
                    "Do not infer sensitive characteristics from office, department, manager, or other profile fields.",
                ],
                example=[
                    "The flow reads only Mail, Display Name, and Office Location for the invoking user.",
                    "If Office Location is empty, it uses the explicit Work Mode input instead of inventing a location.",
                    "The date-only Follow-up Date input is formatted as dd MMM yyyy at the confirmation boundary.",
                ],
                use_when=[
                    "A directory property is necessary for routing or communication and the user is authorised to retrieve it.",
                    "The design records which time zone each timestamp uses and tests a known date.",
                ],
                avoid_when=[
                    "A profile field is being collected for convenience but has no action tied to it.",
                    "A missing value would be silently replaced with a misleading default.",
                ],
                quality=[
                    ("Identity", "Use a stable email or object ID instead of a display name."),
                    ("Time", "Label UTC and local values and convert with an explicit source and destination zone."),
                    ("Privacy", "Retrieve, expose, and retain only the properties required by the flow."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/connectors/office365users/",
                    "https://learn.microsoft.com/en-us/power-automate/convert-time-zone",
                    "https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions",
                ],
            ),
            dict(
                title="Calendar Actions and Duplicate Prevention",
                definition=(
                    "Calendar connector actions create, update, or retrieve events under an authenticated mailbox identity. "
                    "A reliable calendar flow defines subject, start, end, time zone, attendees, body, and availability. "
                    "Idempotency prevents the same business request from creating multiple events when a user retries or a "
                    "connector repeats an operation."
                ),
                why=(
                    "Calendar automation has visible consequences for the user and invited attendees. An incorrect time zone, "
                    "duration, recipient, or retry can block the wrong time or send duplicate invitations. A deterministic "
                    "category or correlation key lets the flow search for an existing event before creating a new one and "
                    "supports later update or cancellation."
                ),
                how=[
                    "Derive a stable event key such as C903-NW-1007-FOLLOWUP from the request ID and event purpose.",
                    "Calculate end time from the validated start and bounded duration.",
                    "Search the target time window or maintain the created Event ID on the request record.",
                    "If an event already exists, update it or return an Already exists result instead of creating another.",
                    "Confirm subject, time zone, start, end, attendees, and saved Event ID in the run evidence.",
                ],
                example=[
                    "A coordinator requests a 45-minute follow-up block for NW-1007 at 3:00 pm Singapore time.",
                    "The flow checks the stored CalendarEventID before Create event, persists the returned ID, then "
                    "uses a bounded category search for C903-NW-1007-FOLLOWUP as count evidence.",
                    "A second invocation detects the stored ID, returns it in the confirmation, and creates no duplicate.",
                ],
                use_when=[
                    "The requester has authority to create the event and the subject and attendees are appropriate.",
                    "The process can persist or search a stable key and has a clear update or cancellation rule.",
                ],
                avoid_when=[
                    "The automation would invite external attendees or expose request details without an explicit release decision.",
                    "The design relies only on event subject text and cannot distinguish retries from genuinely new events.",
                ],
                quality=[
                    ("Time", "Validate start, duration, time zone, and working-hours boundary."),
                    ("Key", "Persist a stable Request ID to Event ID relationship."),
                    ("Impact", "Check attendees, sensitivity, availability, and notification behaviour."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/training/modules/manage-user-information/",
                    "https://learn.microsoft.com/en-us/connectors/office365/",
                    "https://learn.microsoft.com/en-us/power-automate/convert-time-zone",
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="Power Automate's Deep Integration Across Multiple Data Sources",
        subtitle=(
            "Connections and connectors · SharePoint · Power Apps · Dataverse and Dynamics 365 patterns · "
            "SQL · gateways · monitoring · ownership · operational handover"
        ),
        weighting="Afternoon integration and operations · 2 connected labs",
        concepts=[
            (
                "Connector",
                "A packaged interface exposing triggers and actions for a service or data source.",
            ),
            (
                "System of record",
                "The authoritative platform that owns a business entity and governs its current state.",
            ),
            (
                "Dataverse",
                "The Power Platform data service for tables, relationships, security roles, and solution-aware components.",
            ),
            (
                "Gateway",
                "A managed bridge that lets cloud services reach supported on-premises data sources.",
            ),
            (
                "Correlation ID",
                "One identifier carried across systems so records and run evidence can be reconciled.",
            ),
            (
                "Operations runbook",
                "A maintained guide for ownership, dependencies, monitoring, common failures, and recovery actions.",
            ),
        ],
        sections=[
            dict(
                title="Connectors, Connections, Identity, and Policy",
                definition=(
                    "A connector defines available operations for a service; a connection authenticates those operations "
                    "under a user or service identity. Standard and premium classifications affect licensing. Data policies "
                    "can restrict which connectors may be used together, and an on-premises data gateway can provide a "
                    "managed route to supported internal sources such as SQL Server."
                ),
                why=(
                    "A multi-source flow is only as reliable as its identities, permissions, policies, and connection lifecycle. "
                    "A maker may be allowed to read SharePoint but not write SQL, or a connector combination may be blocked. "
                    "Design therefore begins with a connection inventory that records system, operation, identity, owner, "
                    "licence, policy group, environment, and renewal responsibility."
                ),
                how=[
                    "List each system of record, required trigger or action, data classification, and expected volume.",
                    "Select the connector and confirm whether the required operation is standard or premium.",
                    "Choose a maintainable identity and grant only the permissions the action needs.",
                    "Check environment policy and whether a gateway, firewall rule, or administrator setup is required.",
                    "Record connection owner, recovery contact, and which flows depend on the connection.",
                ],
                example=[
                    "The Northwind solution reads a SharePoint request, writes a Dataverse row, and inserts one SQL audit record.",
                    "The training SQL connection is premium and is owned by a managed training identity through an approved gateway.",
                    "The runbook records the connection name, owner, table permission, gateway, and reconnection procedure.",
                ],
                use_when=[
                    "The integration inventory is approved and each identity has a documented operational owner.",
                    "The connector and gateway can meet data location, policy, licensing, latency, and volume needs.",
                ],
                avoid_when=[
                    "A personal maker connection would become an undocumented production dependency.",
                    "The design attempts to bypass data policy, licensing, or network controls.",
                ],
                quality=[
                    ("Authority", "Name the system that owns each field and status."),
                    ("Identity", "Record who authenticates, what they can do, and who maintains the connection."),
                    ("Policy", "Check connector classification, environment, licence, gateway, and data rules."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/power-automate/add-manage-connections",
                    "https://learn.microsoft.com/en-us/connectors/",
                    "https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem",
                ],
            ),
            dict(
                title="SharePoint, Power Apps, Dataverse, Dynamics 365, and SQL Patterns",
                definition=(
                    "SharePoint lists support collaborative records and document-centred processes. Power Apps can collect "
                    "validated user input and invoke a flow. Dataverse provides relational tables, security, and solution-aware "
                    "components used by model-driven apps and Dynamics 365. SQL Server provides relational queries and commands, "
                    "often through premium connections and, for on-premises systems, a gateway."
                ),
                why=(
                    "Integration should not make every system a competing source of truth. The design assigns ownership: "
                    "SharePoint holds the original intake, Dataverse holds governed lifecycle state, and SQL holds an append-only "
                    "integration audit. Power Apps provides the interaction surface. The same Request ID and explicit field map "
                    "allow the flow to reconcile data without confusing display names, option values, or data types."
                ),
                how=[
                    "Declare the system of record for request, stage, decision, calendar event, and audit evidence.",
                    "Map source field, type, required state, transformation, target field, and null behaviour.",
                    "Carry Request ID as the correlation key through Power Apps input, SharePoint, Dataverse, and SQL.",
                    "Use parameterised connector fields or stored procedures; never concatenate untrusted input into SQL text.",
                    "Test create, update, duplicate, null, and permission-denied cases with synthetic data.",
                ],
                example=[
                    "Power Apps sends Request ID and a validated review note to a flow.",
                    "Flow 07A requires exactly one SharePoint item, creates or returns the keyed Dataverse row, and "
                    "responds with message, Dataverse row ID, and Created/Existing state.",
                    "The Dataverse Added event starts flow 07B, which validates the source again, inserts one SQL audit "
                    "row, writes identifiers to SharePoint, and is reconciled later with the Created, Added, Existing, "
                    "and any recovery-run timestamps in their defined columns.",
                ],
                use_when=[
                    "Each system has a distinct role and the field map preserves identifiers and types.",
                    "The flow uses approved connections and synthetic or authorised data during testing.",
                ],
                avoid_when=[
                    "The flow writes the same status independently in several systems without an authority rule.",
                    "SQL text is built by concatenating user input or a shared connection has broader rights than required.",
                ],
                quality=[
                    ("Map", "Document source, type, transform, target, required state, and null behaviour."),
                    ("Key", "Carry one stable Request ID and persist downstream IDs returned by each system."),
                    ("Security", "Use parameterised actions, least privilege, and approved connection ownership."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/training/modules/multiple-data-sources/",
                    "https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows",
                    "https://learn.microsoft.com/en-us/power-automate/dataverse/create-update-delete-trigger",
                    "https://learn.microsoft.com/en-us/connectors/sql/",
                ],
            ),
            dict(
                title="Monitoring, Ownership, Reliability, and Handover",
                definition=(
                    "Operational management keeps a flow observable and maintainable after it is built. Run history shows "
                    "individual executions; analytics and alerts reveal trends; owners and co-owners maintain logic and connections; "
                    "solutions organise related components for controlled movement. A runbook records purpose, dependencies, "
                    "service targets, monitoring cadence, common failures, recovery, and change ownership."
                ),
                why=(
                    "A successful classroom run proves only one path at one moment. Production reliability requires ongoing "
                    "evidence: whether triggers are arriving, actions are succeeding, duration and failure rates are acceptable, "
                    "connections are healthy, and unresolved errors have owners. A tested Catch path and a concise runbook reduce "
                    "recovery time and keep the process independent of one maker's memory."
                ),
                how=[
                    "Define service expectations: schedule, volume, acceptable latency, failure threshold, and retention needs.",
                    "Monitor the trigger count, success rate, duration, connector errors, and business completion record.",
                    "Use Try, Catch, and Finally scopes with run-after settings and one structured error record.",
                    "Assign primary and backup owners and confirm licensing, connection, and underlying-data access.",
                    "Complete a runbook and rehearse one failure, recovery, retest, and communication sequence.",
                ],
                example=[
                    "A synthetic Diagnostic Divisor makes a Compose action fail at runtime before the SQL insert.",
                    "Catch sets SharePoint Status to Automation Error and sends an internal alert containing only "
                    "Request ID, failed action, status, error code, message, UTC time, and owner.",
                    "After Finally records completion, a Boolean failure flag terminates the handled run Failed. The "
                    "owner removes the diagnostic, resubmits that same failed 07B run, and verifies one "
                    "Dataverse row and one SQL audit row, not duplicates.",
                ],
                use_when=[
                    "A business process needs repeatable monitoring and more than one person can perform recovery.",
                    "The team can define an acceptable service level and retain enough run evidence to diagnose defects.",
                ],
                avoid_when=[
                    "The flow is handed over without access checks, owner acceptance, or a tested recovery path.",
                    "Alerts send raw connector payloads or personal data to recipients who do not need them.",
                ],
                quality=[
                    ("Observe", "Track trigger arrival, success, duration, business completion, and connection health."),
                    ("Recover", "Record the first failure, owner, safe retry rule, and post-recovery verification."),
                    ("Own", "Name primary and backup owners, review cadence, and change process."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/power-automate/monitor-manage-processes",
                    "https://learn.microsoft.com/en-us/power-automate/troubleshoot-flow-errors",
                    "https://learn.microsoft.com/en-us/power-automate/change-cloud-flow-owner",
                    "https://learn.microsoft.com/en-us/power-apps/maker/data-platform/solutions-overview",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Build, govern, integrate, and operate one connected Northwind service-request automation",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                (
                    "9:30",
                    "9:50",
                    20,
                    "admin",
                    "Welcome, learning outcomes, environment check, scenario, and flow-design ground rules",
                ),
                (
                    "9:50",
                    "10:25",
                    35,
                    "topic",
                    "Topic 1 - cloud-flow anatomy, trigger types, data mapping, testing, sharing, and diagnosis",
                ),
                ("10:25", "11:00", 35, "lab", "Hands-on: " + lab_titles([1])),
                ("11:00", "11:15", 15, "break", "Tea break"),
                ("11:15", "11:45", 30, "lab", "Hands-on: " + lab_titles([2])),
                (
                    "11:45",
                    "12:15",
                    30,
                    "topic",
                    "Topic 2 - approval patterns, conditions, run-after paths, and business process flows",
                ),
                ("12:15", "13:00", 45, "lab", "Hands-on: " + lab_titles([3])),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                ("14:00", "14:40", 40, "lab", "Hands-on: " + lab_titles([4])),
                (
                    "14:40",
                    "15:05",
                    25,
                    "topic",
                    "Topic 3 - instant inputs, user profiles, date and time logic, calendars, and duplicate control",
                ),
                ("15:05", "15:35", 30, "lab", "Hands-on: " + lab_titles([5])),
                ("15:35", "15:50", 15, "break", "Tea break"),
                ("15:50", "16:25", 35, "lab", "Hands-on: " + lab_titles([6])),
                (
                    "16:25",
                    "16:55",
                    30,
                    "topic",
                    "Topic 4 - SharePoint, Power Apps, Dataverse, Dynamics 365 patterns, SQL, monitoring, and ownership",
                ),
                ("16:55", "17:40", 45, "lab", "Hands-on: " + lab_titles([7])),
                ("17:40", "18:20", 40, "lab", "Hands-on: " + lab_titles([8])),
                (
                    "18:20",
                    "18:30",
                    10,
                    "recap",
                    "Topic recaps mapped to LO1-LO4, continuing-practice plan, and questions",
                ),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="The Observable Automation Loop",
    concepts_title="Keep Six Design Questions Visible",
    concepts=[
        ("Event", "What exact event or user decision creates one run?"),
        ("Data", "Which system owns each field, type, and record identifier?"),
        ("Decision", "Which rules are deterministic and which require a person?"),
        ("Action", "What will be created, updated, sent, or returned?"),
        ("Evidence", "Which run output and target record prove the outcome?"),
        ("Owner", "Who monitors, recovers, changes, and reconnects the automation?"),
    ],
    framework_title="E-D-D-A-E-O Design Framework",
    framework=[
        ("Event", "Trigger type, source, timing, volume, and qualifying rule."),
        ("Data", "Source schema, types, required values, nulls, and correlation key."),
        ("Decision", "Conditions, approval outcomes, branch rules, and timeouts."),
        ("Action", "Connector operation, identity, target, and side effect."),
        ("Evidence", "Run history, target-system record, test case, and expected result."),
        ("Owner", "Primary and backup owner, connection, monitor, and recovery path."),
    ],
    statement=dict(
        headline="A flow is complete only when its trigger, result, and recovery path are observable.",
        body=(
            "Build the normal path, prove the boundary paths, and hand over the identities, "
            "evidence, and recovery actions that keep the automation operating."
        ),
        kicker="C903 OPERATING PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Request layer", ["SharePoint intake", "Dataverse lifecycle record", "Power Apps input contract"]),
        ("Automation layer", ["acknowledgement", "reminder", "approval", "calendar and integration flows"]),
        ("Operations layer", ["run evidence", "SQL audit row", "error record", "handover runbook"]),
    ],
    arc_title="The Learning Arc in Every Lab",
    arc=[
        "Open the previous checkpoint and state the expected outcome.",
        "Build the bounded trigger, actions, data map, and branch.",
        "Test with the supplied synthetic Request ID and inspect run evidence.",
        "Save the checkpoint and record what the next lab is allowed to use.",
    ],
    deep_dives=[
        dict(
            title="The C903 Flow Release Gate",
            kicker="BEFORE A FLOW IS HANDED OVER",
            items=[
                ("Trigger", "Does one qualifying event create one intended run?"),
                ("Data", "Are types, nulls, identities, time zones, and correlation keys explicit?"),
                ("Logic", "Have normal, false, empty, failure, timeout, and duplicate paths been exercised?"),
                ("Security", "Are connections, permissions, data policies, and recipients appropriate?"),
                ("Evidence", "Can a reviewer trace the test record through run history to every target outcome?"),
                ("Ownership", "Are primary and backup owners, monitoring, reconnection, and recovery documented?"),
            ],
        ),
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide accompanies PL-7002 Create and Manage Automated Processes by using Power "
    "Automate (C903). It follows the same four-topic sequence, eight connected labs, four learning "
    "outcomes, one-day schedule, and synthetic Northwind Operations scenario as the slide deck, "
    "Lesson Plan, and standalone lab files."
)

LG_INTRO2 = (
    "Use the guide as a self-contained study text before, during, and after class. Every concept "
    "section explains what the capability is, why it matters, how it works, a worked example, and "
    "when to use or avoid it. The labs progressively build an observable request-automation system "
    "across SharePoint, Outlook, Approvals, Dataverse, Power Apps, Calendar, and SQL."
)

LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a current supported browser.",
        "A trainer-assigned isolated SharePoint site/list, Outlook calendar, Power Platform environment, and SQL database or schema; fixed NW-* identifiers must not be shared across learners.",
        "A Microsoft 365 organisational account with access to Power Automate, Outlook, SharePoint, and Office 365 Users.",
        "An isolated Power Platform training environment with maker access to Power Apps and Dataverse.",
        "A trainer-provided premium SQL Server or Azure SQL connection reference named C903 Training SQL, with gateway/network health and permission to execute the supplied setup script in the isolated database.",
        "The Power Apps, Dataverse, SQL, and business-process capabilities enabled for the training environment; some require premium licensing.",
        "A downloaded copy of this repository with labs/assets intact and permission to use only the supplied synthetic Northwind data.",
    ],
    verify_text=(
        "Sign in at make.powerautomate.com, select the trainer-designated environment, and open Connections. "
        "Confirm the environment and SharePoint site carry your learner tag, then confirm SharePoint, Office 365 "
        "Outlook, Office 365 Users, Microsoft Dataverse, and C903 Training SQL "
        "are present or can be created with the training account. Open labs/assets/process-requests.csv and "
        "confirm that RequestID NW-1001 through NW-1005 are visible. If a required connection is unavailable, "
        "stop before the affected lab and ask the trainer for the approved training connection; do not substitute "
        "a personal database or real organisational record."
    ),
    verify_code=(
        "Expected local structure:\n"
        "C903---PL-7002-Create-and-Manage-Automated-Processes-by-using-Power-Automate/\n"
        "  labs/assets/\n"
        "  work-c903/"
    ),
    conventions=[
        "All Northwind names, requests, email addresses, comments, and identifiers are synthetic training material.",
        "Text between <ANGLE_BRACKETS> is a placeholder; never paste a password, token, client secret, or connection string into a flow note.",
        "Use RequestID as the cross-system correlation key and keep generated SharePoint, Dataverse, Calendar, and SQL IDs separately.",
        "Use UTC for stored integration timestamps and Singapore Standard Time for learner-facing dates and calendar events.",
        "Record a run URL or timestamp, RequestID, expected result, actual result, and recovery action for every Test It check.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, "
    "database, and connections. Never place "
    "credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository."
)

LG_WRAPUP = dict(
    title="Wrap-Up - The Complete C903 Automation",
    intro=(
        "The finished Northwind solution is a connected, observable process rather than a collection "
        "of isolated flow cards. RequestID links the intake, decisions, calendar event, lifecycle record, "
        "SQL audit row, run history, and operations runbook."
    ),
    sections=[
        dict(
            title="Build and decide",
            bullets=[
                "Choose automated, scheduled, or instant triggers from the business event.",
                "Map dynamic content and expressions with explicit types and null handling.",
                "Use approvals for human decisions and conditions for deterministic rules.",
            ],
        ),
        dict(
            title="Personalise and integrate",
            bullets=[
                "Use only the minimum user profile and input data required by the action.",
                "Convert time zones and use a stable event key before creating calendar items.",
                "Assign system-of-record ownership and carry RequestID across SharePoint, Dataverse, Power Apps, and SQL.",
            ],
        ),
        dict(
            title="Operate and recover",
            bullets=[
                "Inspect run history and target-system evidence for every normal and exceptional path.",
                "Use Try, Catch, and Finally scopes with structured, non-sensitive error records.",
                "Hand over co-owners, connections, monitoring checks, safe retry rules, and a tested runbook.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Repeat all eight labs from the clean synthetic source files without using completed flow screenshots.",
    "Adapt the E-D-D-A-E-O design worksheet to one authorised repeated process in your role.",
    "Create a small connection inventory for identity, permissions, licensing, policy, owner, and recovery.",
    "Review current Microsoft Learn and connector documentation before delivery because designer labels, limits, and capabilities continue to change.",
]

LG_GLOSSARY = [
    ("Action", "A configured operation that executes after a trigger or control step."),
    ("Automated flow", "A cloud flow started by an event in a connected service."),
    ("Business process flow", "A Dataverse-backed stage experience that guides a person through a record lifecycle."),
    ("Connection", "An authenticated relationship used by a connector under a user or service identity."),
    ("Connector", "A packaged interface that exposes triggers and actions for a service."),
    ("Correlation ID", "A stable identifier carried across systems so records and run evidence can be reconciled."),
    ("Dataverse", "The Power Platform data service for tables, relationships, security, apps, and solution-aware components."),
    ("Dynamic content", "A value token produced by a trigger or earlier action."),
    ("Expression", "A formula used to transform, validate, combine, or default values."),
    ("Gateway", "A managed bridge between cloud services and supported on-premises data sources."),
    ("Idempotency", "The property that repeating a request does not create an unintended duplicate outcome."),
    ("Instant flow", "A cloud flow started by a person, button, or app invocation."),
    ("Run after", "A dependency setting controlling whether an action runs after success, failure, skip, or timeout."),
    ("Run history", "The record of flow executions, inputs, outputs, duration, status, and errors."),
    ("Scheduled flow", "A cloud flow started by a recurrence configuration."),
    ("System of record", "The authoritative platform that owns a business entity or field."),
    ("Trigger", "The event, recurrence, or invocation that creates a flow run."),
    ("Trigger condition", "An expression evaluated before a trigger creates a run."),
]

NEXT_STEPS = dict(
    title="Continue Building Observable Automations",
    items=[
        "Apply E-D-D-A-E-O to one small, authorised business process.",
        "Carry one stable correlation key through every system and evidence record.",
        "Test the normal, empty, false, failure, timeout, and duplicate paths.",
        "Review current Microsoft guidance whenever connectors or designer controls change.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now design, build, integrate, test, share, monitor, and hand over "
        "Power Automate processes with observable results and controlled recovery."
    ),
    kicker="PL-7002 POWER AUTOMATE · C903",
)

VERSION_HISTORY = [
    (
        "1.0",
        VERSION_DATE,
        "Initial aligned release of PPT, Learner Guide, Lesson Plan, and eight connected labs.",
        TRAINER,
    ),
]
