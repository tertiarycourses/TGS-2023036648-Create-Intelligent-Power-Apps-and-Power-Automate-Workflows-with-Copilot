# Lab 6 — Block Calendar Time with Validation and Duplicate Prevention

**Course:** PL-7002 Create and Manage Automated Processes by using Power Automate  
**Course Code:** C903  
**Version:** v1.0 (29 July 2026)  
**Topic 3:** Build Flows to Manage User Information  
**Maps to:** LO3: validate request count, local ISO date-time, bounded duration, and future time; create one calendar event; persist its Event ID; and prove repeated invocation creates no duplicate  
**Duration:** 35 minutes  
**Tools:** Power Automate instant flows · SharePoint Online · Office 365 Outlook Calendar · control scopes

---

## Goal

Create one 45-minute follow-up block for NW-1007 and prove valid, repeat, invalid-format, out-of-range, past-time, and missing-request behaviour.

## What You Will Do

You will configure an instant calendar flow with a Try_parse_time scope and a separate Schedule_calendar scope. The flow requires exactly one SharePoint request, parses an ISO local start at runtime, enforces a 15-to-120-minute future window, and creates an Outlook event only when CalendarEventID is empty. Catch reports an invalid date format, while explicit Terminate actions close invalid count, range, and past-time cases.

## What You Will Build

An instant cloud flow named C903-06-Block-Follow-Up-Time, one calendar event for NW-1007, a persisted Event ID, and evidence for six validation and duplicate cases

## Prerequisites

- Lab 5 is complete and NW-1007 exists exactly once in your isolated C903 Process Requests list.
- The approved training account can create events only in its own isolated calendar.
- Clear CalendarEventID on NW-1007 before T17 and choose a future Singapore local time.
- The trainer has provisioned the inactive C903-06-Block-Follow-Up-Time starter from labs/assets/c903-starter-solution-package-v1.0.md in your isolated environment with the trigger, named validation scope, conditions, calendar actions, and Catch placeholders already arranged; you configure the exact expressions, mappings, and tests during this 35-minute lab.

> **Data note.** Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

## Steps

### 1. Open the inactive starter Instant cloud flow named C903-06-Block-Follow-Up-Time with required Text inputs RequestID and Start Local ISO plus required Number input Duration Minutes. Configure the existing SharePoint - Get items Find_calendar_request using your assigned training Site Address, list C903 Process Requests, and Filter Query RequestID eq '<RequestID trigger token>'. Configure Condition Exactly_one_calendar_request. In the false branch Terminate Cancelled with Code C903_REQUEST_COUNT and the returned array length.

```text
RequestID example: NW-1007
Start Local ISO format: yyyy-MM-ddTHH:mm:ss
Example: 2026-08-03T15:00:00
Duration Minutes: 15 through 120
Count expression: length(body('Find_calendar_request')?['value'])
```

### 2. In the valid-count branch configure the existing Scope Try_parse_time. Inside it configure Compose Start_local_normalised using formatDateTime and Compose Start_UTC and End_UTC using the patterns below. After Try configure Scope Catch_invalid_format for failed or timed-out Try only; filter result('Try_parse_time') to the first non-Succeeded action, record only action name, status, error code, and message, then Terminate Cancelled with Code C903_INVALID_ISO. After Catch configure Condition Range_and_future to run only when Catch is skipped, meaning parsing succeeded. Require duration 15-120 and local start later than the current Singapore time; in false Terminate Cancelled with Code C903_INVALID_WINDOW.

```text
Start_local_normalised:
formatDateTime(<Start Local ISO>,'yyyy-MM-ddTHH:mm:ss')

Start_UTC, no Z because Outlook receives a separate Time zone field:
convertTimeZone(outputs('Start_local_normalised'),'Singapore Standard Time','UTC','yyyy-MM-ddTHH:mm:ss')

End_UTC:
addMinutes(outputs('Start_UTC'),int(<Duration Minutes>),'yyyy-MM-ddTHH:mm:ss')

Range_and_future:
and(greaterOrEquals(int(<Duration Minutes>),15),lessOrEquals(int(<Duration Minutes>),120),greater(ticks(outputs('Start_local_normalised')),ticks(convertTimeZone(utcNow(),'UTC','Singapore Standard Time'))))
```

### 3. In the valid Range_and_future branch configure the existing Scope Schedule_calendar, then inside it configure Condition Event_ID_is_empty using the expression below. If empty, configure Office 365 Scope Create_event_path containing Outlook - Create event (V4) Create_follow_up_event, the SharePoint update that preserves every existing schema field, and Confirm_event_created. If not empty, configure Scope Reuse_event_path containing Confirm_event_reused and create nothing. The named scopes make their leaf actions directly inspectable with result() if a connector fails.

```text
Event_ID_is_empty:
empty(first(body('Find_calendar_request')?['value'])?['CalendarEventID'])

Update item preserves RequestID, RequestTitle, RequesterEmail, Priority, Status, DueDate, ReminderSent, ApprovalOutcome, ApprovalComments, DataverseRowID, SQLAuditID, DiagnosticDivisor, and sets only CalendarEventID to the Create event result.

Subject: C903 follow-up - <RequestID> - <RequestTitle>
Start time: Start_UTC | End time: End_UTC | Time zone: UTC
Show as: Busy | Attendees: none
Body: Synthetic training request; RequestID; SharePoint item link
Categories: C903-<RequestID>-FOLLOWUP

Created and reused confirmations both include RequestID and the stored Event ID.
```

### 4. Still inside Schedule_calendar, after Event_ID_is_empty, configure Scope Verify_calendar_count. Inside it configure Get calendar view of events (V3), after the branches reconverge, with a window from one minute before Start_UTC to one minute after End_UTC. Configure Filter array Calendar_events_for_request, From = the Get calendar view value array, with advanced condition @contains(item()?['categories'],'C903-NW-1007-FOLLOWUP'). Then Compose Calendar_event_count with length(body('Calendar_events_for_request')). This ensures the T17 and T18 run histories both contain the bounded count evidence.

```text
Verify_calendar_count runs after Event_ID_is_empty succeeds. Its Get calendar view window and category filter are deliberately bounded to this synthetic request.
```

### 5. After Schedule_calendar configure the existing Scope Catch_calendar_technical for Schedule failed or timed out and not success. Filter the union of the three inner-scope results plus Schedule_calendar to failed, timed-out, or cancelled actions while excluding deliberately skipped branches; compose only action name, status, error code, and message, update the request to Automation Error while preserving all other fields, send one internal filtered-error alert, and Terminate Failed with Code C903_CALENDAR_TECHNICAL. Do not include a raw scope result in the alert. Save, select Turn on, confirm the flow status is On, and record six cases.

```text
Filter array name: Only_unsuccessful_calendar_actions
From: union(result('Create_event_path'),result('Reuse_event_path'),result('Verify_calendar_count'),result('Schedule_calendar'))
Filter condition: @or(equals(item()?['status'],'Failed'),equals(item()?['status'],'TimedOut'),equals(item()?['status'],'Cancelled'))

Error_action: first(body('Only_unsuccessful_calendar_actions'))?['name']
Error_status: first(body('Only_unsuccessful_calendar_actions'))?['status']
Error_code: coalesce(first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['body']?['error']?['code'],first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['body']?['code'],first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['error']?['code'],first(body('Only_unsuccessful_calendar_actions'))?['error']?['code'],'NO_CODE_FROM_ACTION')
Error_message: coalesce(first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['body']?['error']?['message'],first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['body']?['message'],first(body('Only_unsuccessful_calendar_actions'))?['outputs']?['error']?['message'],first(body('Only_unsuccessful_calendar_actions'))?['error']?['message'],'No connector message returned')
Record only these four values plus RequestID.

This technical Catch never handles invalid ISO input or an invalid window; those paths terminate before Schedule_calendar starts.

T17 NW-1007 | future valid time | 45 -> one created event and stored ID
T18 repeat identical inputs -> reused branch; zero new events; filtered calendar count = 1
T19 NW-1007 | future valid time | 5 -> Cancelled C903_INVALID_WINDOW
T20 NW-1007 | not-a-date | 45 -> Catch -> Cancelled C903_INVALID_ISO
T21 NW-1007 | yesterday local time | 45 -> Cancelled C903_INVALID_WINDOW
T22 NW-9999 | future valid time | 45 -> Cancelled C903_REQUEST_COUNT

After T17, open work-c903/C903-Correlation-Register.csv and update only CalendarEventID in the existing NW-1007 row with the stored SharePoint value; preserve SharePointItemID, DataverseRowID, SQLAuditID, all four run-time columns, and State. Do not append a duplicate row. After T18, verify the reused flow output, SharePoint CalendarEventID, Outlook event ID, and register CalendarEventID are identical.
```

## Test It

T17 must create one 45-minute Busy event and persist its Event ID. T18 must reuse the same ID and the bounded Get calendar view plus category Filter array must return exactly one event. The existing NW-1007 correlation-register row must remain unique, preserve all ten columns, and carry the same CalendarEventID shown by T17/T18, SharePoint, and Outlook. T19-T22 must terminate on the stated validation path and create no event. Create event (V4) must receive date-time strings without Z and a separate UTC Time zone value. No attendees or non-synthetic request details are added. Before class, the trainer performs the bounded connector-failure acceptance check in the provisioning checklist; it must identify the leaf action and produce nonblank Error_code and Error_message (documented fallback text is acceptable only when the connector returns no structured detail). Learners do not induce this failure.

## Checkpoint and Rejoin Point

Keep NW-1007 CalendarEventID populated, keep exactly one NW-1007 correlation-register row with the matching Event ID and all other columns preserved, and save T17-T22. Lab 7 uses a new NW-1009 record but carries the same exactly-one lookup and correlation-key discipline into Dataverse and SQL. To rejoin, rerun T18, confirm the filtered calendar count remains one, and reconcile the same ID across the run, SharePoint, Outlook, and the register.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The event appears at the wrong local time. | Inspect Start_local_normalised, Start_UTC, and End_UTC; confirm the source zone is Singapore Standard Time and Create event receives UTC without Z plus Time zone UTC. |
| The second run creates another event. | Confirm the first update persisted CalendarEventID and Event_ID_is_empty reads the first returned SharePoint item's stored value before Create event. |
| An invalid date bypasses Catch. | Place formatDateTime inside Try_parse_time and configure Catch_invalid_format for failed and timed-out Try_parse_time outcomes only. |

## Challenge

Add a bounded update path that moves the existing event when a new valid start is supplied. Require the stored Event ID and preserve the correlation category rather than deleting and creating a new event.

## Reflection

Which validation closes each bad-input path, and which stored value makes a repeat request idempotent?

---

[← Lab 5](lab-05-create-a-validated-user-driven-follow-up-flow.md) · [Lab 7 →](lab-07-build-an-idempotent-power-apps-sharepoint-dataverse-and-sql-integration.md)
