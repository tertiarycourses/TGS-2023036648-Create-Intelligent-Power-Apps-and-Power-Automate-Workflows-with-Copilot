# PL-7002 Create and Manage Automated Processes by using Power Automate — Learner Guide

**Course Code:** C903  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 29 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Get Started with Power Automate  (Morning foundation · 2 connected labs)](#topic-01--get-started-with-power-automate--morning-foundation--2-connected-labs)
  - [Cloud-Flow Anatomy and Trigger Selection](#cloud-flow-anatomy-and-trigger-selection)
  - [Recurrence, Event Triggers, and Data Mapping](#recurrence-event-triggers-and-data-mapping)
  - [Testing, Run History, Sharing, and Troubleshooting](#testing-run-history-sharing-and-troubleshooting)
  - [Lab 1 — Validate the Northwind Request Intake and Create an Automated Acknowledgement](#lab-1--validate-the-northwind-request-intake-and-create-an-automated-acknowledgement)
  - [Lab 2 — Build a Scheduled Reminder and Diagnose a Controlled Failure](#lab-2--build-a-scheduled-reminder-and-diagnose-a-controlled-failure)
  - [Topic 01 Recap - Mapped to Learning Outcomes](#topic-01-recap---mapped-to-learning-outcomes)
- [Topic 02 — Build Approval Flows with Power Automate  (Midday decisions · 2 connected labs)](#topic-02--build-approval-flows-with-power-automate--midday-decisions--2-connected-labs)
  - [Approval Patterns and Human Decision Points](#approval-patterns-and-human-decision-points)
  - [Conditional Logic, Trigger Conditions, and Run-After Paths](#conditional-logic-trigger-conditions-and-run-after-paths)
  - [Business Process Flows and Conditional Stages](#business-process-flows-and-conditional-stages)
  - [Lab 3 — Build a Priority Approval with Complete Outcome and Recovery Paths](#lab-3--build-a-priority-approval-with-complete-outcome-and-recovery-paths)
  - [Lab 4 — Create and Traverse a Conditional Dataverse Business Process Flow](#lab-4--create-and-traverse-a-conditional-dataverse-business-process-flow)
  - [Topic 02 Recap - Mapped to Learning Outcomes](#topic-02-recap---mapped-to-learning-outcomes)
- [Topic 03 — Build Flows to Manage User Information  (Afternoon personal productivity · 2 connected labs)](#topic-03--build-flows-to-manage-user-information--afternoon-personal-productivity--2-connected-labs)
  - [Instant Flows and User-Input Contracts](#instant-flows-and-user-input-contracts)
  - [Profile, Location, Date, and Time Logic](#profile-location-date-and-time-logic)
  - [Calendar Actions and Duplicate Prevention](#calendar-actions-and-duplicate-prevention)
  - [Lab 5 — Create a Validated User-Driven Follow-Up Flow](#lab-5--create-a-validated-user-driven-follow-up-flow)
  - [Lab 6 — Block Calendar Time with Validation and Duplicate Prevention](#lab-6--block-calendar-time-with-validation-and-duplicate-prevention)
  - [Topic 03 Recap - Mapped to Learning Outcomes](#topic-03-recap---mapped-to-learning-outcomes)
- [Topic 04 — Power Automate's Deep Integration Across Multiple Data Sources  (Afternoon integration and operations · 2 connected labs)](#topic-04--power-automates-deep-integration-across-multiple-data-sources--afternoon-integration-and-operations--2-connected-labs)
  - [Connectors, Connections, Identity, and Policy](#connectors-connections-identity-and-policy)
  - [SharePoint, Power Apps, Dataverse, Dynamics 365, and SQL Patterns](#sharepoint-power-apps-dataverse-dynamics-365-and-sql-patterns)
  - [Monitoring, Ownership, Reliability, and Handover](#monitoring-ownership-reliability-and-handover)
  - [Lab 7 — Build an Idempotent Power Apps, SharePoint, Dataverse, and SQL Integration](#lab-7--build-an-idempotent-power-apps-sharepoint-dataverse-and-sql-integration)
  - [Lab 8 — Recover the Same Integration Run and Complete Operational Handover](#lab-8--recover-the-same-integration-run-and-complete-operational-handover)
  - [Topic 04 Recap - Mapped to Learning Outcomes](#topic-04-recap---mapped-to-learning-outcomes)
- [Wrap-Up - The Complete C903 Automation](#wrap-up---the-complete-c903-automation)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies PL-7002 Create and Manage Automated Processes by using Power Automate (C903). It follows the same four-topic sequence, eight connected labs, four learning outcomes, one-day schedule, and synthetic Northwind Operations scenario as the slide deck, Lesson Plan, and standalone lab files.

Use the guide as a self-contained study text before, during, and after class. Every concept section explains what the capability is, why it matters, how it works, a worked example, and when to use or avoid it. The labs progressively build an observable request-automation system across SharePoint, Outlook, Approvals, Dataverse, Power Apps, Calendar, and SQL.


## Course Learning Outcomes

- LO1: Design, build, test, share, and troubleshoot cloud flows by selecting appropriate triggers, actions, recurrence settings, dynamic content, and run-history evidence.
- LO2: Implement conditional logic, approval patterns, run-after behaviour, and a conditional business process flow for a governed request lifecycle.
- LO3: Create user-driven flows that use explicit inputs, Microsoft 365 user information, date and time logic, and calendar actions while controlling duplicates and data exposure.
- LO4: Integrate SharePoint, Power Apps, Dataverse, Dynamics 365 patterns, and SQL; then monitor, share, own, and document a reliable automated process.


## Before You Start — Preparation

**What you need**

- A Windows or Mac laptop with a current supported browser.
- A trainer-assigned isolated SharePoint site/list, Outlook calendar, Power Platform environment, and SQL database or schema; fixed NW-* identifiers must not be shared across learners.
- A Microsoft 365 organisational account with access to Power Automate, Outlook, SharePoint, and Office 365 Users.
- An isolated Power Platform training environment with maker access to Power Apps and Dataverse.
- A trainer-provided premium SQL Server or Azure SQL connection reference named C903 Training SQL, with gateway/network health and permission to execute the supplied setup script in the isolated database.
- The Power Apps, Dataverse, SQL, and business-process capabilities enabled for the training environment; some require premium licensing.
- A downloaded copy of this repository with labs/assets intact and permission to use only the supplied synthetic Northwind data.

**Verify your setup**

Sign in at make.powerautomate.com, select the trainer-designated environment, and open Connections. Confirm the environment and SharePoint site carry your learner tag, then confirm SharePoint, Office 365 Outlook, Office 365 Users, Microsoft Dataverse, and C903 Training SQL are present or can be created with the training account. Open labs/assets/process-requests.csv and confirm that RequestID NW-1001 through NW-1005 are visible. If a required connection is unavailable, stop before the affected lab and ask the trainer for the approved training connection; do not substitute a personal database or real organisational record.

```bash
Expected local structure:
C903---PL-7002-Create-and-Manage-Automated-Processes-by-using-Power-Automate/
  labs/assets/
  work-c903/
```

**Conventions used in every lab**

- All Northwind names, requests, email addresses, comments, and identifiers are synthetic training material.
- Text between <ANGLE_BRACKETS> is a placeholder; never paste a password, token, client secret, or connection string into a flow note.
- Use RequestID as the cross-system correlation key and keep generated SharePoint, Dataverse, Calendar, and SQL IDs separately.
- Use UTC for stored integration timestamps and Singapore Standard Time for learner-facing dates and calendar events.
- Record a run URL or timestamp, RequestID, expected result, actual result, and recovery action for every Test It check.


## Topic 01 — Get Started with Power Automate  (Morning foundation · 2 connected labs)

Cloud-flow anatomy · automated, instant, and scheduled triggers · dynamic content · testing · sharing · run history · troubleshooting

**Key concepts**

- Trigger — The event or schedule that creates one flow run and supplies the initial data payload.
- Action — A configured operation that reads, transforms, sends, creates, or updates data after the trigger.
- Connection — The authenticated relationship a connector uses to act against a service under an identity.
- Dynamic content — A token that carries a value from a trigger or earlier action into a later field.
- Run history — The evidence trail for trigger input, action input and output, duration, status, and error details.
- Ownership — The people or service identity responsible for editing, licensing, connections, monitoring, and recovery.


### Cloud-Flow Anatomy and Trigger Selection

A cloud flow is an event-driven sequence made of one trigger followed by actions, control steps, and data transformations. Automated flows react to a service event, scheduled flows start from a recurrence, and instant flows start when a person or app invokes them. The trigger creates the run and provides the first payload; every later action consumes values from that payload or from earlier outputs.

Trigger choice determines when work starts, which identity and data are available, how often the service is queried, and whether duplicate events are possible. Starting from the business event instead of from a favourite connector keeps the automation aligned with the process. A good design states the event, system of record, expected volume, latency, and evidence of success.

**How it works**

- Write the business event as: When <event> occurs in <system>, automate <outcome> for <recipient>.
- Choose automated, scheduled, or instant based on who or what controls the start.
- Inspect the trigger schema and identify the stable record ID, timestamps, owner, and business fields.
- Add only the actions needed to reach an observable result, then rename every card by intent.
- Test with a known record and compare trigger input, action output, and target-system evidence.

**Worked example**

- A new item in the Northwind Process Requests SharePoint list starts an automated flow.
- The flow captures Request ID, title, requester, priority, and due date, then sends an acknowledgement.
- The run is successful only when run history is green and the acknowledgement contains the same Request ID.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A repeatable event has a clear owner, stable data source, and observable downstream outcome. | The event is ambiguous, the process changes on every occurrence, or a person must first judge whether work should start. |
| The service connector exposes the required trigger and the running identity is permitted to use it. | The design cannot identify a stable record key or would repeatedly process the same event without a duplicate guard. |

**Practitioner quality lens**

- Event: Name the exact event and the system that owns it.
- Payload: Identify required fields, types, null cases, and one stable correlation key.
- Evidence: Define the target record, message, or run output that proves success.

**Authoritative references**

- https://learn.microsoft.com/en-us/power-automate/flow-types
- https://learn.microsoft.com/en-us/power-automate/get-started-logic-flow
- https://learn.microsoft.com/en-us/training/modules/get-started-flows/

---


### Recurrence, Event Triggers, and Data Mapping

A recurrence trigger creates runs at a configured interval, start time, and time zone. An event trigger reacts when a connected service reports that a record was created or changed. Dynamic content maps fields from the trigger or an earlier action into later actions; expressions transform those values when simple token mapping is not enough.

Scheduled and event-driven patterns solve different timing problems. A recurrence is appropriate for periodic sweeps such as overdue-request reminders, while an event trigger is appropriate for a new request acknowledgement. Explicit data mapping prevents a common defect: a flow that runs successfully but sends the wrong field, formats a date incorrectly, or processes records outside scope.

**How it works**

- For recurrence, set frequency, interval, start time, and the Singapore time zone explicitly.
- For an event trigger, create a fresh test event and allow for the connector's polling behaviour.
- Use Filter Query or trigger conditions to reduce unnecessary runs when the connector supports them.
- Map dynamic content by business meaning, not by a similar-looking display name.
- Use Compose for intermediate values so the run history exposes the value used by later steps.

**Worked example**

- At 4:00 pm every day, a scheduled flow queries Open requests whose ReminderSent flag is No, then checks whether each Due Date is today in Singapore.
- A Runtime diagnostic Compose reads the supplied Diagnostic Divisor before Outlook sends the Request ID and Title reminder and SharePoint marks ReminderSent Yes.
- The designer proves one due item sends once, a repeated run sends nothing, a tomorrow item takes the false path, and a supplied zero creates a controlled runtime failure.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A periodic business rule can query a bounded set and tolerate the chosen interval. | The process requires immediate response but the selected connector uses a long polling interval. |
| An expression or Compose step makes a derived value easier to inspect and reuse. | A broad scheduled query would retrieve an unbounded dataset or resend the same item without a sent flag. |

**Practitioner quality lens**

- Clock: Record time zone, start time, interval, and daylight-saving implications.
- Scope: Filter at the source and define what happens when zero, one, or many rows return.
- Mapping: Trace each dynamic token to its producing trigger or action.

**Authoritative references**

- https://learn.microsoft.com/en-us/training/modules/get-started-flows/
- https://learn.microsoft.com/en-us/power-automate/triggers-introduction
- https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions

---


### Testing, Run History, Sharing, and Troubleshooting

Testing executes a flow with controlled input and records the resulting run. Run history exposes the status, duration, inputs, outputs, retries, and error message for each step. Sharing can make another person a co-owner who can edit and maintain the flow, or a run-only user who can invoke an instant flow without redesigning it.

A green designer is not proof of a reliable process. The flow must be exercised with representative data, branch boundaries, empty values, and expected failures. Troubleshooting begins with the symptom: no run indicates a trigger problem; a red step indicates an action or connection problem; an all-green run with a wrong outcome indicates data mapping or logic. Ownership and connection planning prevent a useful flow from stopping when its maker changes role.

**How it works**

- Save, run a manual test, and capture the run URL or timestamp with the test record ID.
- If no run exists, inspect trigger event, conditions, status, schedule, and connector polling.
- If an action fails, open the first red action and read its inputs, outputs, status code, and connection.
- If the run is green but wrong, compare dynamic content and expressions with the source record.
- Share with the least privilege needed, confirm connections, and record primary and backup owners.

**Worked example**

- A reminder flow saves but no run appears because the recurrence start time is tomorrow.
- After correcting the start time, the Outlook action fails with 401 because its connection expired.
- The maker fixes the connection, retests one known item, and records the successful run before handover.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A controlled test record can be traced from trigger to target without exposing production-sensitive data. | Testing would send real external messages or modify live records without a safe test boundary. |
| A team-owned business process needs documented co-owners, connection responsibilities, and monitoring. | A flow is shared without checking whether recipients can access the underlying connections and data. |

**Practitioner quality lens**

- Coverage: Test normal, boundary, empty, and deliberately failing cases.
- Diagnosis: Locate the first divergence between expected and actual inputs or outputs.
- Continuity: Name owners, connection identity, monitoring cadence, and recovery action.

**Authoritative references**

- https://learn.microsoft.com/en-us/power-automate/troubleshoot-flow-errors
- https://learn.microsoft.com/en-us/power-automate/create-team-flows
- https://learn.microsoft.com/en-us/power-automate/change-cloud-flow-owner

---


### Lab 1 — Validate the Northwind Request Intake and Create an Automated Acknowledgement

Learning outcome: LO1: create an automated cloud flow with a SharePoint trigger, explicit dynamic-content mapping, an Outlook notification, and traceable run evidence.

Goal: Validate the isolated request intake and prove that one new SharePoint item produces one acknowledgement containing the same RequestID.

You will inspect the pre-provisioned SharePoint list used throughout the course, verify five synthetic Northwind requests, and build an automated cloud flow that acknowledges every new request. You will rename the trigger and actions, map values deliberately, create a test request, and trace it from the SharePoint item through run history to the delivered message.

**What you'll build**

A validated per-learner SharePoint list named C903 Process Requests, an automated cloud flow named C903-01-Acknowledge-New-Request, and a saved evidence record for RequestID NW-1006   (Tools: SharePoint Online · Power Automate cloud flows · Office 365 Outlook.)

**Prerequisites**

- Sign in to the trainer-designated Microsoft 365 and Power Platform environment.
- Use only your trainer-assigned isolated SharePoint site and C903 Process Requests list; every learner has a separate list.
- Confirm NW-1001 through NW-1005 are already loaded and you can send an email to your own training mailbox.
- Open labs/assets/process-requests.csv and labs/assets/request-schema.md; use only the supplied synthetic records.

**Step-by-step**

1. Create a local or approved OneDrive folder named work-c903. Copy labs/assets/test-evidence-template.csv into it and save the copy as C903-Test-Evidence.csv. Every test row you add must include your learner tag and its UTC test date; do not add a metadata row above the CSV header.

   ```bash
   Required evidence columns:
LearnerTag | TestDateUTC | TestID | Flow | RequestID | Input | Expected | Actual | RunTimeUTC | RunLinkOrTimestamp | Result | RecoveryNote
   ```

2. On your isolated training SharePoint site, open C903 Process Requests. Compare every column with request-schema.md, including ApprovalComments and DiagnosticDivisor. Confirm the five NW-1001 through NW-1005 rows match process-requests.csv. If the list or rows differ, stop and ask the trainer to restore the supplied provisioning package; do not rebuild a shared class list during the timed lab.

   ```bash
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

3. In Power Automate, create an Automated cloud flow named C903-01-Acknowledge-New-Request. Choose SharePoint - When an item is created, select the training Site Address and C903 Process Requests, and rename the trigger New_request_received.

   ```bash
   Trigger contract:
Business event: one item is created
System of record: SharePoint C903 Process Requests
Correlation key: RequestID
Expected volume: classroom test records only
   ```

4. Add Data Operation - Compose, rename it Correlation_key, and set Inputs to RequestID dynamic content. Add Office 365 Outlook - Send an email (V2), rename it Send_acknowledgement, and map the fields exactly. Save the flow and resolve any connection prompt with the approved training account.

   ```bash
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

5. Select Test - Manually, then create one new SharePoint item using the NW-1006 values below. Open the completed run, expand all three cards, and compare the trigger RequestID, Compose output, email inputs, and delivered message. Add test T01 to C903-Test-Evidence.csv.

   ```bash
   NW-1006 test record:
RequestTitle: Prepare weekly service summary
RequesterEmail: <YOUR_TRAINING_EMAIL>
Priority: Normal
Status: New
DueDate: <TOMORROW>
ReminderSent: No

Expected: exactly one successful run and one email; every occurrence of the correlation key is NW-1006.
   ```


**Test it**

The isolated SharePoint list must contain NW-1001 through NW-1006 with the exact schema. A single new NW-1006 item must create one successful run. The trigger input, Correlation_key output, email subject, email body, and T01 evidence row must all contain NW-1006. The email must show the mapped title, priority, and due date and must not contain any unrelated list field.

**Checkpoint and rejoin point**

Leave C903-01-Acknowledge-New-Request turned on and save C903-Test-Evidence.csv in work-c903. Lab 2 uses the same isolated list and adds reminder behaviour. If you need to rejoin, ask the trainer to restore the provisioned list from request-schema.md and process-requests.csv, then run the NW-1006 check.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| No run appears after the item is created. | Confirm the flow is on, the trigger points to the same site and list, and the item was newly created rather than edited. Wait for the connector polling interval, then inspect the trigger again. |
| The email action uses the wrong field. | Open the failed or incorrect run, compare the action input with the trigger output, remove the token, and reselect the exact dynamic-content field by its column name. |
| The training email does not arrive. | Verify Send_acknowledgement is green, inspect its To and Subject inputs, record the flow run timestamp, check the training mailbox junk folder, and match the delivered message subject and received time. Send an email (V2) does not provide a message ID output. |

**Challenge**

Add a link to the SharePoint item in the email without hard-coding an item number. Explain which trigger output supplies the link and how the link remains tied to the same RequestID.

**Reflection**

Which run-history value gives the strongest evidence that the email belongs to the correct request, and why?

> **Note:** The complete lab and its support-file references are in labs/lab-01-*.md. Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

---


### Lab 2 — Build a Scheduled Reminder and Diagnose a Controlled Failure

Learning outcome: LO1: build a scheduled cloud flow, filter and iterate SharePoint records, update reminder state, diagnose a runtime expression failure, retest, and share maintenance ownership.

Goal: Send one reminder for each due open request, prevent duplicate reminders, and prove that run history can locate and recover a deliberately introduced fault.

You will build a scheduled flow that finds open requests due today, sends one reminder, and marks each item so the next run does not resend it. You will insert a temporary divide-by-zero expression, use run history to find the first red action, restore the supplied divisor, retest the same expression, and share the flow with a trainer-designated co-owner for continuity.

**What you'll build**

A scheduled cloud flow named C903-02-Remind-Due-Requests, evidence rows for normal, empty, duplicate, and controlled-failure cases, and a recorded primary and backup owner   (Tools: Power Automate scheduled flows · SharePoint Online · Office 365 Outlook.)

**Prerequisites**

- Lab 1 is complete and C903 Process Requests contains the baseline data plus NW-1006.
- C903-Test-Evidence.csv is available in work-c903.
- Obtain the trainer-designated co-owner email; do not share with an unapproved account.
- The trainer has provisioned the inactive C903-02-Remind-Due-Requests starter from labs/assets/c903-starter-solution-package-v1.0.md with its named trigger, loop, Condition, Compose, email, and update placeholders already arranged.

**Step-by-step**

1. Update SharePoint item NW-1002 so Status is Open, DueDate is today, RequesterEmail is your training email, ReminderSent is No, and DiagnosticDivisor is 1. Set every other item to either a future DueDate or ReminderSent Yes.

   ```bash
   Controlled test state:
Qualifying rows = exactly 1
Qualifying RequestID = NW-1002
Expected first run = one reminder and ReminderSent changes to Yes
   ```

2. Open the inactive starter Scheduled cloud flow named C903-02-Remind-Due-Requests. Configure the existing Recurrence to every 1 day, Time zone to (UTC+08:00) Kuala Lumpur, Singapore, and start time to the next 4:00 pm Singapore slot. Confirm the trigger is named Daily_1600_SGT. Configure the existing SharePoint Get items Find_due_open_requests, Apply to each For_each_candidate, and Condition Due_date_is_today with the exact values below.

   ```bash
   Site Address: <TRAINING_SITE>
List Name: C903 Process Requests
Filter Query:
Status eq 'Open' and ReminderSent eq 0

Condition expression:
equals(
  formatDateTime(items('For_each_candidate')?['DueDate'],'yyyy-MM-dd'),
  formatDateTime(convertTimeZone(utcNow(),'UTC','Singapore Standard Time'),'yyyy-MM-dd')
)
   ```

3. In the matching branch, configure the existing Compose Runtime_diagnostic_check before the message to divide 1 by the current item's DiagnosticDivisor so a supplied zero becomes a runtime test fault rather than an invalid constant. Configure the existing Send an email (V2) Send_due_reminder and SharePoint - Update item Mark_reminder_sent. Map the current item's ID, required list fields, and set ReminderSent to Yes. Save, select Turn on, confirm the flow status is On, and use Test - Manually to execute the scheduled flow immediately.

   ```bash
   Runtime expression:
div(1,int(items('For_each_candidate')?['DiagnosticDivisor']))

Email subject: Due today - <RequestID> - <RequestTitle>
Body: Request <RequestID> is due today. Open the SharePoint item and update its status.

Evidence T02 expected:
one email for NW-1002; the SharePoint row changes ReminderSent from No to Yes.
   ```

4. Run the flow a second time without changing the list and record T03 as the duplicate-prevention case. Then set NW-1002 ReminderSent to No and DueDate to tomorrow, run again, and record T04 as the false-date case. Confirm the loop runs, Due_date_is_today is false, and no message or update action runs.

   ```bash
   Expected T03: Find_due_open_requests returns zero qualifying rows; zero reminder emails.
Expected T04: NW-1002 enters the loop but takes the false date branch; zero reminder emails.
These are separate evidence rows.
   ```

5. Set NW-1002 DueDate back to today, ReminderSent to No, and DiagnosticDivisor to 0. Run the flow and record T05: Runtime_diagnostic_check must be the first red action and no email is sent. Set DiagnosticDivisor to 1, open the failed run, select Resubmit, and record the successful recovery as T06. Open the flow details page, add the trainer-designated co-owner, and record the primary owner, backup owner, Outlook connection owner, and monitoring check in work-c903/C903-Ownership-Record.txt.

   ```bash
   Ownership record:
Flow: C903-02-Remind-Due-Requests
Primary owner: <YOUR_TRAINING_EMAIL>
Backup owner: <TRAINER_DESIGNATED_EMAIL>
Connection owner: <TRAINING_ACCOUNT>
Monitor: check the next scheduled run and investigate any red action
Recovery evidence: T05 runtime failure and T06 successful resubmission
   ```


**Test it**

T02 must show one reminder and ReminderSent set to Yes for NW-1002. T03 must prove repeat-run duplicate prevention, and T04 must prove the false-date branch. T05 must identify Runtime_diagnostic_check as the first red action with DiagnosticDivisor 0; T06 must resubmit successfully after the divisor is restored to 1 and set ReminderSent to Yes. The final flow must be on and list the approved primary and backup owners.

**Checkpoint and rejoin point**

Keep NW-1002 as Open with ReminderSent Yes and DiagnosticDivisor 1. Save the ownership record and T02-T06 evidence. Lab 3 reuses the SharePoint list and adds approval logic for High-priority requests. To rejoin, confirm Labs 1 and 2 flows are on and a repeated reminder run creates no duplicate message.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Get items returns more records than expected. | Inspect Status and ReminderSent values in SharePoint, verify the internal field types, and keep the date comparison inside the loop until the exact date format is confirmed. |
| Update item clears a required field. | Map the current item's ID and every required column in Update item. Inspect the action inputs before retrying. |
| The second run sends another reminder. | Confirm Mark_reminder_sent completed successfully, inspect the stored Yes/No value, and verify Find_due_open_requests filters ReminderSent eq 0. |

**Challenge**

Replace the loop-level date Condition with a source-side date filter only after you verify the SharePoint internal column name and ISO date literal. Compare the number of retrieved rows and explain the efficiency trade-off.

**Reflection**

How did the symptom tell you whether to inspect the trigger, the first red action, or the data mapping?

> **Note:** The complete lab and its support-file references are in labs/lab-02-*.md. Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

---


### Topic 01 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO1 - Build and Diagnose | Choose a trigger that matches the business event, configure actions with explicit data, test both expected and exceptional paths, and use run history to locate the first failure. |

---


## Topic 02 — Build Approval Flows with Power Automate  (Midday decisions · 2 connected labs)

Approval patterns · conditional logic · custom responses · trigger conditions · run-after paths · business process flows · conditional stages

**Key concepts**

- Approval — A human decision step that records an outcome, responder, comments, and completion time.
- Condition — A two-branch control that evaluates a Boolean comparison after a run has started.
- Trigger condition — An expression evaluated before the run is created, reducing unnecessary executions.
- Run after — A dependency setting that selects which next action runs after success, failure, skip, or timeout.
- Business process flow — A Dataverse-backed stage and step experience that guides a person through a consistent record lifecycle.
- Branching — A rule that changes the next path when data or a human decision meets defined criteria.


### Approval Patterns and Human Decision Points

Power Automate approvals combine an automated flow with a recorded human response. Start and wait for an approval pauses the run until the configured response condition is met. The approval type controls whether the first response, every response, a sequence, or custom response options complete the step. The returned outcome and comments become data for later branches.

An approval is useful where policy requires a named person to accept, reject, or request clarification. It should not be added merely to make a flow look governed. The design must state who decides, what evidence they receive, how long they have, what each outcome means, and what happens if no one responds.

**How it works**

- Define the decision, approver role, evidence, response options, timeout expectation, and audit record.
- Choose first response, all responses, sequential, or custom responses based on the actual rule.
- Build the approval title from a stable Request ID and keep the details concise and traceable.
- Branch on the exact returned Outcome value and persist outcome, responder, comments, and completion time.
- Notify the requester and update the system of record on every designed outcome.

**Worked example**

- A high-priority Northwind request creates an approval for the operations manager.
- The approver chooses Approve, Need more information, or Reject and adds a comment.
- The flow updates SharePoint with the exact outcome and sends the requester a matching message.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A policy or risk decision needs a named responder and durable decision evidence. | The decision can be expressed safely as a deterministic rule with no human judgment. |
| The approver receives enough context and has access to any linked supporting record. | The flow has no designed timeout, escalation, cancellation, or ownership path for unanswered requests. |

**Practitioner quality lens**

- Decision: State one question and define every allowed response.
- Evidence: Include only the facts and secure links the approver needs.
- Closure: Persist outcome and notify the correct people on every path.

**Authoritative references**

- https://learn.microsoft.com/en-us/power-automate/get-started-approvals
- https://learn.microsoft.com/en-us/power-automate/modern-approvals
- https://learn.microsoft.com/en-us/power-automate/create-approval-response-options

---


### Conditional Logic, Trigger Conditions, and Run-After Paths

A Condition action branches after a run begins. A trigger condition is evaluated at the trigger and can prevent an unwanted run from being created. Configure run after changes dependency behaviour so an action can execute after success, failure, skip, or timeout. Together these controls separate business rules from technical recovery behaviour.

Conditions decide what the process should do with valid data; run-after settings decide what the flow should do when a step does not complete normally. Mixing them produces brittle designs. Trigger conditions can reduce noise and request consumption, but an incorrect expression can silently suppress all runs, so the expression and a known qualifying record must be tested together.

**How it works**

- Write each business rule in plain language with field, operator, value, and null behaviour.
- Use a Condition after the trigger when both qualifying and non-qualifying runs need recorded outcomes.
- Use a trigger condition when non-qualifying events should create no run and that absence is acceptable.
- Group critical actions in a Try Scope and configure Catch to run after failure, timeout, or skip.
- Record the error, Request ID, failed step, and recovery owner before sending a controlled alert.

**Worked example**

- Only High-priority requests need human approval; other priorities continue automatically.
- A Try Scope creates the approval and updates SharePoint. Catch runs only if Try fails or times out.
- The Catch path writes an Automation Error status and sends one internal notification with the Request ID.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Branch rules are explicit and test data can exercise both true and false paths. | A trigger condition would hide events that operations still needs to count or explain. |
| A technical failure must create a controlled record and alert instead of silently stopping the process. | Configure run after is used to ignore failure without recording what failed and who will recover it. |

**Practitioner quality lens**

- Rule: Document field type, operator, comparison value, and null case.
- Path: Name branches by business meaning instead of Yes and No.
- Recovery: Capture error context once and route it to a named owner.

**Authoritative references**

- https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions
- https://learn.microsoft.com/en-us/power-automate/triggers-introduction
- https://learn.microsoft.com/en-us/power-automate/guidance/coding-guidelines/error-handling

---


### Business Process Flows and Conditional Stages

A business process flow is a Dataverse-backed, stage-based user experience attached to one or more tables. It guides users through defined stages and data steps while the underlying model-driven app stores the record. Conditional branching can direct a record to different stages based on field values. A business process flow guides interactive work; a cloud flow automates operations around records.

Some processes require people to see the current stage, complete required data, and move the record forward consistently. A cloud flow alone is not a user guidance surface. Combining the two patterns lets the business process flow govern stage progression while cloud flows notify, approve, integrate, and monitor around the record.

**How it works**

- Model the lifecycle as a small number of named stages with an owner and exit evidence for each stage.
- Create the Dataverse table and required columns before designing the stage path.
- Add data steps to stages and mark only genuinely required information as required.
- Add a branch rule on a stable field such as Priority or Approval Required, then validate and activate.
- Test one record through each branch and confirm both the active stage and the stored field values.

**Worked example**

- Northwind uses Intake, Review, Approval, Fulfilment, and Closure stages for automation requests.
- A high-priority record enters Approval after Review; a standard request moves directly to Fulfilment.
- The record ID remains constant while cloud flows update status and notify the request owner.

**Decision guide**

| Use when | Avoid when |
|---|---|
| People need a visible stage path and consistent data capture on a Dataverse record. | The process is entirely system-to-system with no need for an interactive stage experience. |
| The organisation has an environment, table, app, roles, and licensing suitable for the process. | A complex diagram is being reproduced without simplifying stages, ownership, and exit criteria first. |

**Practitioner quality lens**

- Stage: Each stage has a clear purpose, owner, required data, and exit condition.
- Branch: Branch rules use stable values and every path reaches a defined end.
- Integration: Cloud flows reference the same Dataverse record ID and do not duplicate process state.

**Authoritative references**

- https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview
- https://learn.microsoft.com/en-us/power-automate/create-business-process-flow
- https://learn.microsoft.com/en-us/power-automate/enhance-business-process-flows-branching

---


### Lab 3 — Build a Priority Approval with Complete Outcome and Recovery Paths

Learning outcome: LO2: create and configure an approval, implement High and non-High paths, persist every custom outcome, exercise an approval timeout, and record filtered technical error details.

Goal: Route only High-priority Northwind requests to a named approver and close every approval, non-approval, default, or timeout path with an explicit SharePoint status, a requester message for handled business outcomes, or a filtered internal alert for technical failure.

You will build an automated flow for new SharePoint requests. High priority creates an approval with Approve, Need more information, and Reject responses; other priorities continue without an approval. The flow stores outcome, comments, and status on the same request. A one-minute training timeout exercises Catch, which filters the scope result down to action name, status, error code, and message.

**What you'll build**

An automated cloud flow named C903-03-Approve-High-Priority-Request with explicit non-High actions, three approval cases, a default case, serial Try/Catch/Finally scopes, and five path tests   (Tools: SharePoint Online · Power Automate Approvals · Office 365 Outlook · conditions and control scopes.)

**Prerequisites**

- Labs 1 and 2 are complete in your trainer-assigned isolated SharePoint site.
- C903 Process Requests includes ApprovalOutcome, ApprovalComments, and DiagnosticDivisor from request-schema.md.
- The approved training account can create approvals and update its own isolated list.
- Use your training email as requester and approver unless the trainer supplies a separate isolated approver account.
- The trainer has provisioned the inactive C903-03-Approve-High-Priority-Request starter from labs/assets/c903-starter-solution-package-v1.0.md in your isolated environment with the trigger, named scopes, switch cases, and placeholder actions already arranged; you configure connections, mappings, expressions, run-after settings, and messages during this 45-minute lab.

**Step-by-step**

1. Open the inactive starter Automated cloud flow named C903-03-Approve-High-Priority-Request with SharePoint - When an item is created, pointed to your C903 Process Requests list. Rename the trigger Request_for_routing. Configure the existing Condition Is_high_priority and compare Priority Value with High. In the non-High branch configure Update item Continue_without_approval and Send an email (V2) Notify_no_approval_required.

   ```bash
   Non-High mapping:
Update the current numeric item ID; map RequestID, RequestTitle, RequesterEmail, Priority, DueDate, ReminderSent, and DiagnosticDivisor from the trigger.
Status = Open
ApprovalOutcome = Not required
ApprovalComments = Priority did not require approval

Email subject: No approval required - <RequestID>
Email body: RequestID; Priority; Status Open; item link.
   ```

2. In the High branch configure the existing Scope Try_approval. Inside it configure the update of the current item to Pending Approval, then configure Approvals - Start and wait for an approval named Request_operations_decision. Choose Custom Responses - Wait for one response and enter the three response labels exactly. In the action Settings set Timeout to PT1M for this isolated training exercise.

   ```bash
   Responses, in order:
Approve
Need more information
Reject

Title: <RequestID> - <RequestTitle>
Assigned to: <YOUR_TRAINING_EMAIL>
Details: Priority; DueDate; RequesterEmail; SharePoint item link.
Training timeout: PT1M. A workplace design must use its approved service target.
   ```

3. After the approval, still inside Try_approval, configure the existing Switch Route_decision on the approval Outcome. Create Approve, Need more information, and Reject cases plus a Default case. In every case update the same item, map all required fields, set ApprovalOutcome to the exact response, store the first response Comments in ApprovalComments, and send a matching email.

   ```bash
   Approve -> Status Approved; subject Decision: approved - <RequestID>
Need more information -> Status More Info; subject Decision: more information needed - <RequestID>
Reject -> Status Rejected; subject Decision: rejected - <RequestID>
Default -> Status Automation Error; subject Decision response not recognised - <RequestID>

Every decision message includes RequestID, Outcome, Completion date, Comments, and item link.
   ```

4. After Try_approval configure the existing Scope Catch_approval_error to run after Try has failed, timed out, or been skipped, and not after success. Inside Catch configure Filter array Only_unsuccessful_actions with From = result('Try_approval') and the status condition below, excluding deliberately skipped actions. Configure Compose actions Error_action, Error_status, Error_code, and Error_message from the first filtered item using the null-safe expressions below. Update the request to Automation Error and send one internal filtered-error message. Configure Finally_record_completion after Catch and configure it for every Catch outcome, including skipped.

   ```bash
   Filter condition:
@or(equals(item()?['status'],'Failed'),equals(item()?['status'],'TimedOut'),equals(item()?['status'],'Cancelled'))

Filtered fields:
first(body('Only_unsuccessful_actions'))?['name']
first(body('Only_unsuccessful_actions'))?['status']
coalesce(first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['error']?['code'],first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['code'],first(body('Only_unsuccessful_actions'))?['outputs']?['error']?['code'],first(body('Only_unsuccessful_actions'))?['error']?['code'],'NO_CODE_FROM_ACTION')
coalesce(first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['error']?['message'],first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['message'],first(body('Only_unsuccessful_actions'))?['outputs']?['error']?['message'],first(body('Only_unsuccessful_actions'))?['error']?['message'],'No connector message returned')

Internal email includes only RequestID, those four fields, utcNow(), owner, and item link. Do not include result('Try_approval') or a raw action payload in the message.
   ```

5. Save, select Turn on, confirm the flow status is On, and exercise five isolated records one at a time. Respond from the approval centre for the first three High records; do not respond to the timeout record. Record T07-T11 in C903-Test-Evidence.csv with RequestID, Priority, approval created Yes/No, response or timeout, final SharePoint status, ApprovalComments, message subject, and run timestamp.

   ```bash
   Create each record with RequestID | RequestTitle | RequesterEmail | Priority | Status | DueDate | ReminderSent | DiagnosticDivisor, using your training email, Status New, a future due date, No, and 1:
T07 NW-1007 | Approve supplier onboarding automation | <YOUR_TRAINING_EMAIL> | High -> Approve with comment 'Approved for the training route' -> Approved
T08 NW-1011 | Review customer refund approval | <YOUR_TRAINING_EMAIL> | High -> Need more information with comment 'Add the process owner' -> More Info
T09 NW-1012 | Review warehouse exception route | <YOUR_TRAINING_EMAIL> | High -> Reject with comment 'Outside the training scope' -> Rejected
T10 NW-1008 | Send a normal-priority operations update | <YOUR_TRAINING_EMAIL> | Normal -> no approval -> Open
T11 NW-1013 | Exercise the isolated approval timeout | <YOUR_TRAINING_EMAIL> | High -> no response for PT1M -> Catch -> Automation Error

Every RequestID is created once in your isolated list.
   ```


**Test it**

T07-T09 must each create one approval, store the exact outcome and supplied comment, update the expected status, and send one matching decision message. T10 must create no approval and must take the explicit non-High update and message path. T11 must time out, run Catch, store Automation Error, and send only the filtered action name, status, code, and message. Finally must run after both successful and skipped Catch outcomes. Error_code and Error_message must both be nonblank in T11 evidence; use the documented fallback text only when the connector supplies no structured code or message.

**Checkpoint and rejoin point**

Leave NW-1007 Approved, NW-1011 More Info, NW-1012 Rejected, NW-1008 Open, and NW-1013 Automation Error. Save T07-T11, then turn C903-03-Approve-High-Priority-Request off so it cannot intercept the High-priority records created in later labs. Lab 4 reuses NW-1007 and NW-1008 field values in Dataverse. To rejoin, verify all five outcome rows and the filtered timeout message.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The approval is not visible in email. | Open Power Automate Approvals, confirm Assigned to matches the signed-in training account, and respond from the approval centre. |
| The Switch does not match the selected response. | Open the approval output, copy the exact Outcome text, and make the case label match spaces and capitalisation exactly. |
| Catch exposes more data than the four error fields. | Remove the raw scope result from the email, confirm Filter array excludes Succeeded actions, and map only Error_action, Error_status, Error_code, and Error_message. |

**Challenge**

After completing the timed test, change the approval timeout to a realistic organisational service target and document the separate escalation owner and cancellation rule without altering the five recorded training runs.

**Reflection**

Which paths express business decisions, and which path exists only to recover a technical exception?

> **Note:** The complete lab and its support-file references are in labs/lab-03-*.md. Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

---


### Lab 4 — Create and Traverse a Conditional Dataverse Business Process Flow

Learning outcome: LO2: create a business process flow on a pre-provisioned Dataverse table, branch by priority, activate it, and traverse one High and one Normal record through every stage in their path.

Goal: Give Northwind coordinators a visible lifecycle in which High-priority requests traverse Approval while other requests move from Review directly to Fulfilment, and prove both paths reach Closure.

The trainer has pre-provisioned the solution, table, alternate key, main form, active view, and app shell so the timed lab focuses on process design. You will verify the model, create a five-stage business process flow, add a High-priority branch, activate it, and advance NW-1007 and NW-1008 through every expected stage.

**What you'll build**

An active C903 Request Lifecycle business process flow in the C903 Northwind Automation solution, published in C903 Request Manager, with complete High and Normal path evidence   (Tools: Power Apps maker portal · Microsoft Dataverse · business process flows · model-driven apps.)

**Prerequisites**

- Use your trainer-assigned isolated Power Platform environment with Dataverse maker permissions.
- The trainer has provisioned C903 Northwind Automation, C903 Automation Request, and C903 Request Manager.
- Request ID is an active mandatory alternate key; if the key is absent, stop and ask the trainer to restore provisioning.
- Copy labs/assets/correlation-register-template.csv to work-c903/C903-Correlation-Register.csv.

**Step-by-step**

1. At make.powerapps.com select your isolated training environment and open C903 Northwind Automation. Inspect C903 Automation Request and verify the exact columns, types, required settings, Request ID alternate key, main form, active view, and model-driven app page. Do not continue if any item differs.

   ```bash
   Required columns:
Request ID - Text, required, active alternate key
Request Title - Text, required
Requester Email - Email
Priority - Choice: Low, Normal, High
Request Status - Choice: New, Open, Pending Approval, Approved, More Info, Rejected, Fulfilment, Closed
Due Date - Date only
Approval Outcome - Text
SharePoint Item ID - Whole number
Diagnostic Divisor - Whole number, default 1
   ```

2. Inside the solution create Automation - Process - Business process flow named C903 Request Lifecycle for C903 Automation Request. Add stages in order Intake, Review, Approval, Fulfilment, Closure. Add the stated data steps and mark only Request ID and Request Title required in Intake.

   ```bash
   Intake: Request ID, Request Title, Requester Email
Review: Priority, Due Date
Approval: Approval Outcome, Request Status
Fulfilment: Request Status
Closure: Request Status
   ```

3. Insert Condition High_priority_route after Review with Priority Equals High. Connect true to Approval then Fulfilment; connect false directly to Fulfilment; connect both to Closure. Select Validate, correct any disconnected component, Save, and Activate.

   ```bash
   High path: Intake -> Review -> Approval -> Fulfilment -> Closure
Default path: Intake -> Review -> Fulfilment -> Closure
Every branch must reach Closure.
   ```

4. Add the active C903 Request Lifecycle process to C903 Request Manager if it is not automatically available. Save and Publish the app. Open it and create NW-1007 and NW-1008 using the Lab 3 values, including each source SharePoint numeric item ID and Diagnostic Divisor 1.

   ```bash
   NW-1007: High | Approved | Approve supplier onboarding automation
NW-1008: Normal | Open | Send a normal-priority operations update
Use the exact Request ID alternate key; a duplicate create must be rejected.
   ```

5. For NW-1007, record the active stage, complete required values, and select Next Stage through Intake, Review, Approval, Fulfilment, and Closure; set final Request Status Closed. Repeat NW-1008 through Intake, Review, Fulfilment, and Closure. Record T12 and T13 with every observed stage and add both generated Dataverse row IDs to C903-Correlation-Register.csv.

   ```bash
   T12 NW-1007 expected: Intake | Review | Approval | Fulfilment | Closure | Closed
T13 NW-1008 expected: Intake | Review | Fulfilment | Closure | Closed

Correlation header, unchanged:
RequestID | SharePointItemID | DataverseRowID | CalendarEventID | SQLAuditID | Flow07ACreatedRunTimeUTC | Flow07AExistingRunTimeUTC | Flow07BInitialRunTimeUTC | Flow07BRecoveryRunTimeUTC | State
   ```


**Test it**

The solution must contain the active five-stage C903 Request Lifecycle with one High-priority branch and an active Request ID alternate key. T12 must show all five stages for NW-1007 and T13 must show the four-stage default path for NW-1008. Both records must reach Closure and end Closed. The correlation register must use the supplied header and store the SharePoint and Dataverse IDs for both RequestIDs.

**Checkpoint and rejoin point**

Keep the solution and app published and both records Closed. Save T12-T13 and the correlation register. Lab 7 reuses the table, alternate key, solution, and app shell with a new NW-1009 record. To rejoin, open both completed process instances and verify every active-stage transition recorded in the evidence.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The process cannot activate. | Select Validate, connect every stage and branch to Closure, confirm each data step references an existing column, save, and activate again. |
| Both records follow the same branch. | Confirm Priority stores different choice values, inspect the High_priority_route operator and value, then restart the affected isolated process instance. |
| A duplicate Request ID is accepted. | Stop the lab and ask the trainer to activate the Request ID alternate key; downstream exactly-once behaviour depends on it. |

**Challenge**

Add a Low-priority branch only if every route still reaches Closure. Draw the result and explain why a small number of explicit paths is easier to operate than deeply nested branching.

**Reflection**

What does full stage traversal prove that checking only the first branch decision does not?

> **Note:** The complete lab and its support-file references are in labs/lab-04-*.md. Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

---


### Topic 02 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO2 - Approve and Branch | Use an approval only where a person must decide, branch on the returned outcome, configure failure paths deliberately, and distinguish a cloud flow from a stage-based business process flow. |

---


## Topic 03 — Build Flows to Manage User Information  (Afternoon personal productivity · 2 connected labs)

Instant flow inputs · Office 365 Users · location and date values · time-zone conversion · calendar events · privacy · duplicate prevention

**Key concepts**

- Instant input — A typed value supplied by the person or app that invokes an instant cloud flow.
- User profile — Directory information returned by the Microsoft 365 Users connection for an authorised identity.
- Expression — A formula that transforms, validates, combines, or defaults values during a run.
- Time zone — The regional offset and daylight rule needed to interpret a local date and time correctly.
- Idempotency — The property that repeating the same request does not create an unintended duplicate outcome.
- Minimum data — The smallest set of user information needed to achieve the declared automation purpose.


### Instant Flows and User-Input Contracts

An instant cloud flow starts when a person selects a button or when Power Apps invokes the flow. The trigger can define typed inputs such as text, number, Boolean, email, date, or file. Those inputs form a contract between the user interface and the automation: names, required values, allowed values, defaults, and validation must be explicit.

User-driven automation is appropriate when a person decides when work should begin and supplies context that no system event contains. Poor input design moves ambiguity into later actions. A short, typed input contract reduces errors, makes test cases repeatable, and avoids collecting unnecessary personal data.

**How it works**

- Define the user decision and the minimum fields the flow needs to act.
- Name inputs with business terms and include format guidance in the prompt or app.
- Validate required values and allowed options before calling downstream connectors.
- Create a correlation key from the request ID and invocation time or another stable input.
- Return a concise confirmation containing the correlation key and next action.

**Worked example**

- A coordinator runs an instant flow for Request NW-1007 and enters a follow-up date and work mode.
- The flow retrieves the coordinator's profile and selects an office or remote message branch.
- The confirmation contains the Request ID, selected date, and resolved location without exposing extra profile fields or promising a request link.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A person must choose the start moment or provide a small amount of current context. | The process should start automatically from a reliable source-system event. |
| The flow can validate input before creating messages, calendar events, or records. | The trigger asks for sensitive or irrelevant personal information that the process does not need. |

**Practitioner quality lens**

- Contract: Name every input, type, required state, allowed value, and default.
- Validation: Stop early with a useful message when data is missing or malformed.
- Confirmation: Return the correlation key and the exact outcome created.

**Authoritative references**

- https://learn.microsoft.com/en-us/training/modules/manage-user-information/
- https://learn.microsoft.com/en-us/power-automate/button-flow-with-user-input-tokens
- https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows

---


### Profile, Location, Date, and Time Logic

The Office 365 Users connector can retrieve profile properties for the signed-in or named organisational user. Date and time values arrive in specific formats and time zones; expressions such as formatDateTime, addDays, coalesce, and convertTimeZone transform them. Location may come from an explicit input or an authorised directory property and should be used only for the declared purpose.

Personalised flows fail when a display name is used where an email is required, an optional profile field is null, or an unlabelled timestamp is interpreted in the wrong time zone. Explicit types, null handling, and time-zone conversion make the result predictable. Minimum-data design reduces privacy and maintenance risk by retrieving only what later actions use.

**How it works**

- Use the signed-in user's email or object identity as the profile lookup key.
- Inspect which profile fields can be empty and apply coalesce only with a truthful default.
- Keep UTC for system comparison and convert to Singapore Standard Time for local communication.
- Format dates only at the presentation boundary; preserve the original machine-readable value.
- Do not infer sensitive characteristics from office, department, manager, or other profile fields.

**Worked example**

- The flow reads only Mail, Display Name, and Office Location for the invoking user.
- If Office Location is empty, it uses the explicit Work Mode input instead of inventing a location.
- The date-only Follow-up Date input is formatted as dd MMM yyyy at the confirmation boundary.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A directory property is necessary for routing or communication and the user is authorised to retrieve it. | A profile field is being collected for convenience but has no action tied to it. |
| The design records which time zone each timestamp uses and tests a known date. | A missing value would be silently replaced with a misleading default. |

**Practitioner quality lens**

- Identity: Use a stable email or object ID instead of a display name.
- Time: Label UTC and local values and convert with an explicit source and destination zone.
- Privacy: Retrieve, expose, and retain only the properties required by the flow.

**Authoritative references**

- https://learn.microsoft.com/en-us/connectors/office365users/
- https://learn.microsoft.com/en-us/power-automate/convert-time-zone
- https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions

---


### Calendar Actions and Duplicate Prevention

Calendar connector actions create, update, or retrieve events under an authenticated mailbox identity. A reliable calendar flow defines subject, start, end, time zone, attendees, body, and availability. Idempotency prevents the same business request from creating multiple events when a user retries or a connector repeats an operation.

Calendar automation has visible consequences for the user and invited attendees. An incorrect time zone, duration, recipient, or retry can block the wrong time or send duplicate invitations. A deterministic category or correlation key lets the flow search for an existing event before creating a new one and supports later update or cancellation.

**How it works**

- Derive a stable event key such as C903-NW-1007-FOLLOWUP from the request ID and event purpose.
- Calculate end time from the validated start and bounded duration.
- Search the target time window or maintain the created Event ID on the request record.
- If an event already exists, update it or return an Already exists result instead of creating another.
- Confirm subject, time zone, start, end, attendees, and saved Event ID in the run evidence.

**Worked example**

- A coordinator requests a 45-minute follow-up block for NW-1007 at 3:00 pm Singapore time.
- The flow checks the stored CalendarEventID before Create event, persists the returned ID, then uses a bounded category search for C903-NW-1007-FOLLOWUP as count evidence.
- A second invocation detects the stored ID, returns it in the confirmation, and creates no duplicate.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The requester has authority to create the event and the subject and attendees are appropriate. | The automation would invite external attendees or expose request details without an explicit release decision. |
| The process can persist or search a stable key and has a clear update or cancellation rule. | The design relies only on event subject text and cannot distinguish retries from genuinely new events. |

**Practitioner quality lens**

- Time: Validate start, duration, time zone, and working-hours boundary.
- Key: Persist a stable Request ID to Event ID relationship.
- Impact: Check attendees, sensitivity, availability, and notification behaviour.

**Authoritative references**

- https://learn.microsoft.com/en-us/training/modules/manage-user-information/
- https://learn.microsoft.com/en-us/connectors/office365/
- https://learn.microsoft.com/en-us/power-automate/convert-time-zone

---


### Lab 5 — Create a Validated User-Driven Follow-Up Flow

Learning outcome: LO3: validate instant-flow inputs, retrieve the invoking user's minimum profile data, resolve one location variable through both branches, and format a follow-up date.

Goal: Let a coordinator request a follow-up for one RequestID and receive a confirmation built from validated input, a single resolved location value, and a consistently formatted date.

You will create an instant flow with RequestID, Follow-up Date, Work Mode, and Use Directory Location inputs. The flow normalises and validates Work Mode before reading profile data, requires exactly one SharePoint request, retrieves only Display Name, Mail, and Office Location, and sets one ResolvedLocation variable in both location branches.

**What you'll build**

An instant cloud flow named C903-05-Create-User-Follow-Up with a four-field input contract, invalid-input termination, exactly-one lookup, minimum profile retrieval, and one branch-safe variable   (Tools: Power Automate instant flows · SharePoint Online · Office 365 Users · Office 365 Outlook.)

**Prerequisites**

- Use your trainer-assigned isolated SharePoint list and approved Microsoft 365 training account.
- C903 Process Requests contains NW-1007 and NW-1008 exactly once.
- Know whether the training profile Office Location is populated; do not edit directory properties.
- The approved training profile has a populated Mail value. If it does not, stop and ask the trainer to repair the isolated account before the timed lab.
- The trainer has provisioned the inactive C903-05-Create-User-Follow-Up starter from labs/assets/c903-starter-solution-package-v1.0.md with its inputs, validation branches, lookup, profile, variable, date Compose, and email placeholders already arranged.

**Step-by-step**

1. Open the inactive starter Instant cloud flow C903-05-Create-User-Follow-Up. Configure the existing Manually trigger a flow card and its four required inputs in this order with the stated guidance.

   ```bash
   RequestID - Text - example NW-1007
Follow-up Date - Date - intended local calendar date
Work Mode - Text - allowed values Office or Remote
Use Directory Location - Yes/No - Yes uses a non-empty profile value; No uses Work Mode
   ```

2. Configure the existing Compose Normalised_work_mode with the expression below and Condition Work_mode_is_allowed to test whether the output equals office or remote. In the false branch configure Terminate with Status Cancelled, Code C903_INVALID_WORK_MODE, and message 'Use Office or Remote'. Put every later action in the valid branch so invalid input retrieves no profile data and sends no email.

   ```bash
   Normalisation pattern:
toLower(trim(<Work Mode dynamic-content token>))

Condition expression:
or(equals(outputs('Normalised_work_mode'),'office'),equals(outputs('Normalised_work_mode'),'remote'))
   ```

3. In the valid branch configure the existing SharePoint - Get items Find_request_by_ID with Filter Query RequestID eq '<RequestID trigger token>'. Configure Condition Exactly_one_request using the array-length expression. If false, configure Terminate with Status Cancelled, Code C903_REQUEST_COUNT, and a message containing the actual count. If true, configure Office 365 Users - Get my profile (V2) Get_invoking_user_profile.

   ```bash
   Count expression:
length(body('Find_request_by_ID')?['value'])
Required count: 1

Get my profile (V2) Select fields: displayName,mail,officeLocation
Profile properties used later:
Display Name | Mail | Office Location
Do not retrieve or expose unrelated profile properties.
   ```

4. Configure the existing String variable ResolvedLocation with an empty initial value. Configure Condition Use_directory_location to require Use Directory Location = Yes and Office Location is not empty. In the true branch Set variable ResolvedLocation to Office Location. In the false branch Set variable ResolvedLocation to Normalised_work_mode. After the Condition configure Compose Follow_up_date_display and Send an email (V2).

   ```bash
   Date expression:
formatDateTime(<Follow-up Date input>,'dd MMM yyyy')

Subject: Follow-up recorded - <RequestID>
Body: Hello <Display Name>; RequestID; RequestTitle; Follow-up Date; ResolvedLocation; and a note that isolated synthetic training data was used.
To: profile Mail
   ```

5. Save, select Turn on, confirm the flow status is On, and exercise three cases without editing the flow definition. Record T14-T16 with input, branch, resolved value, profile properties exposed, final status, and message subject.

   ```bash
   T14 NW-1007 | Work Mode Remote | Use Directory Location Yes -> profile Office Location when non-empty, otherwise remote
T15 NW-1008 | Work Mode Office | Use Directory Location No -> office
T16 NW-1008 | Work Mode Airport | Use Directory Location No -> Cancelled C903_INVALID_WORK_MODE; profile and email actions do not run
   ```


**Test it**

The trigger must have four required inputs. T14 and T15 must find exactly one request and consume the same ResolvedLocation variable after the location Condition. T16 must terminate before profile retrieval and send no email. The two valid messages may expose only Display Name, Mail, resolved location, synthetic request fields, and the formatted date. No flow logic is edited between tests.

**Checkpoint and rejoin point**

Keep the final flow unchanged after T16 and save T14-T16. Lab 6 reuses the exactly-one RequestID pattern and adds date-time, duration, calendar, and duplicate validation. To rejoin, rerun T15 and confirm ResolvedLocation equals office through the real saved branch logic.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Get items returns zero or more than one row. | Inspect the exact RequestID input and isolated list, then use the count in C903_REQUEST_COUNT to correct the data instead of selecting an arbitrary row. |
| The email cannot access a branch-local location value. | Confirm ResolvedLocation is initialised before the Condition and both branches use Set variable rather than separate Compose actions. |
| The profile Mail value is empty. | Stop and ask the trainer to repair the isolated training profile. Do not add an unapproved fallback or retrieve extra profile fields during the timed lab. |

**Challenge**

Bind Work Mode to an Office/Remote choice control in the pre-provisioned C903 canvas app shell and explain how allowed values reduce downstream termination cases.

**Reflection**

How did early validation and one shared variable make the later email action safer and easier to inspect?

> **Note:** The complete lab and its support-file references are in labs/lab-05-*.md. Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

---


### Lab 6 — Block Calendar Time with Validation and Duplicate Prevention

Learning outcome: LO3: validate request count, local ISO date-time, bounded duration, and future time; create one calendar event; persist its Event ID; and prove repeated invocation creates no duplicate.

Goal: Create one 45-minute follow-up block for NW-1007 and prove valid, repeat, invalid-format, out-of-range, past-time, and missing-request behaviour.

You will configure an instant calendar flow with a Try_parse_time scope and a separate Schedule_calendar scope. The flow requires exactly one SharePoint request, parses an ISO local start at runtime, enforces a 15-to-120-minute future window, and creates an Outlook event only when CalendarEventID is empty. Catch reports an invalid date format, while explicit Terminate actions close invalid count, range, and past-time cases.

**What you'll build**

An instant cloud flow named C903-06-Block-Follow-Up-Time, one calendar event for NW-1007, a persisted Event ID, and evidence for six validation and duplicate cases   (Tools: Power Automate instant flows · SharePoint Online · Office 365 Outlook Calendar · control scopes.)

**Prerequisites**

- Lab 5 is complete and NW-1007 exists exactly once in your isolated C903 Process Requests list.
- The approved training account can create events only in its own isolated calendar.
- Clear CalendarEventID on NW-1007 before T17 and choose a future Singapore local time.
- The trainer has provisioned the inactive C903-06-Block-Follow-Up-Time starter from labs/assets/c903-starter-solution-package-v1.0.md in your isolated environment with the trigger, named validation scope, conditions, calendar actions, and Catch placeholders already arranged; you configure the exact expressions, mappings, and tests during this 35-minute lab.

**Step-by-step**

1. Open the inactive starter Instant cloud flow named C903-06-Block-Follow-Up-Time with required Text inputs RequestID and Start Local ISO plus required Number input Duration Minutes. Configure the existing SharePoint - Get items Find_calendar_request using your assigned training Site Address, list C903 Process Requests, and Filter Query RequestID eq '<RequestID trigger token>'. Configure Condition Exactly_one_calendar_request. In the false branch Terminate Cancelled with Code C903_REQUEST_COUNT and the returned array length.

   ```bash
   RequestID example: NW-1007
Start Local ISO format: yyyy-MM-ddTHH:mm:ss
Example: 2026-08-03T15:00:00
Duration Minutes: 15 through 120
Count expression: length(body('Find_calendar_request')?['value'])
   ```

2. In the valid-count branch configure the existing Scope Try_parse_time. Inside it configure Compose Start_local_normalised using formatDateTime and Compose Start_UTC and End_UTC using the patterns below. After Try configure Scope Catch_invalid_format for failed or timed-out Try only; filter result('Try_parse_time') to the first non-Succeeded action, record only action name, status, error code, and message, then Terminate Cancelled with Code C903_INVALID_ISO. After Catch configure Condition Range_and_future to run only when Catch is skipped, meaning parsing succeeded. Require duration 15-120 and local start later than the current Singapore time; in false Terminate Cancelled with Code C903_INVALID_WINDOW.

   ```bash
   Start_local_normalised:
formatDateTime(<Start Local ISO>,'yyyy-MM-ddTHH:mm:ss')

Start_UTC, no Z because Outlook receives a separate Time zone field:
convertTimeZone(outputs('Start_local_normalised'),'Singapore Standard Time','UTC','yyyy-MM-ddTHH:mm:ss')

End_UTC:
addMinutes(outputs('Start_UTC'),int(<Duration Minutes>),'yyyy-MM-ddTHH:mm:ss')

Range_and_future:
and(greaterOrEquals(int(<Duration Minutes>),15),lessOrEquals(int(<Duration Minutes>),120),greater(ticks(outputs('Start_local_normalised')),ticks(convertTimeZone(utcNow(),'UTC','Singapore Standard Time'))))
   ```

3. In the valid Range_and_future branch configure the existing Scope Schedule_calendar, then inside it configure Condition Event_ID_is_empty using the expression below. If empty, configure Office 365 Scope Create_event_path containing Outlook - Create event (V4) Create_follow_up_event, the SharePoint update that preserves every existing schema field, and Confirm_event_created. If not empty, configure Scope Reuse_event_path containing Confirm_event_reused and create nothing. The named scopes make their leaf actions directly inspectable with result() if a connector fails.

   ```bash
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

4. Still inside Schedule_calendar, after Event_ID_is_empty, configure Scope Verify_calendar_count. Inside it configure Get calendar view of events (V3), after the branches reconverge, with a window from one minute before Start_UTC to one minute after End_UTC. Configure Filter array Calendar_events_for_request, From = the Get calendar view value array, with advanced condition @contains(item()?['categories'],'C903-NW-1007-FOLLOWUP'). Then Compose Calendar_event_count with length(body('Calendar_events_for_request')). This ensures the T17 and T18 run histories both contain the bounded count evidence.

   ```bash
   Verify_calendar_count runs after Event_ID_is_empty succeeds. Its Get calendar view window and category filter are deliberately bounded to this synthetic request.
   ```

5. After Schedule_calendar configure the existing Scope Catch_calendar_technical for Schedule failed or timed out and not success. Filter the union of the three inner-scope results plus Schedule_calendar to failed, timed-out, or cancelled actions while excluding deliberately skipped branches; compose only action name, status, error code, and message, update the request to Automation Error while preserving all other fields, send one internal filtered-error alert, and Terminate Failed with Code C903_CALENDAR_TECHNICAL. Do not include a raw scope result in the alert. Save, select Turn on, confirm the flow status is On, and record six cases.

   ```bash
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


**Test it**

T17 must create one 45-minute Busy event and persist its Event ID. T18 must reuse the same ID and the bounded Get calendar view plus category Filter array must return exactly one event. The existing NW-1007 correlation-register row must remain unique, preserve all ten columns, and carry the same CalendarEventID shown by T17/T18, SharePoint, and Outlook. T19-T22 must terminate on the stated validation path and create no event. Create event (V4) must receive date-time strings without Z and a separate UTC Time zone value. No attendees or non-synthetic request details are added. Before class, the trainer performs the bounded connector-failure acceptance check in the provisioning checklist; it must identify the leaf action and produce nonblank Error_code and Error_message (documented fallback text is acceptable only when the connector returns no structured detail). Learners do not induce this failure.

**Checkpoint and rejoin point**

Keep NW-1007 CalendarEventID populated, keep exactly one NW-1007 correlation-register row with the matching Event ID and all other columns preserved, and save T17-T22. Lab 7 uses a new NW-1009 record but carries the same exactly-one lookup and correlation-key discipline into Dataverse and SQL. To rejoin, rerun T18, confirm the filtered calendar count remains one, and reconcile the same ID across the run, SharePoint, Outlook, and the register.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The event appears at the wrong local time. | Inspect Start_local_normalised, Start_UTC, and End_UTC; confirm the source zone is Singapore Standard Time and Create event receives UTC without Z plus Time zone UTC. |
| The second run creates another event. | Confirm the first update persisted CalendarEventID and Event_ID_is_empty reads the first returned SharePoint item's stored value before Create event. |
| An invalid date bypasses Catch. | Place formatDateTime inside Try_parse_time and configure Catch_invalid_format for failed and timed-out Try_parse_time outcomes only. |

**Challenge**

Add a bounded update path that moves the existing event when a new valid start is supplied. Require the stored Event ID and preserve the correlation category rather than deleting and creating a new event.

**Reflection**

Which validation closes each bad-input path, and which stored value makes a repeat request idempotent?

> **Note:** The complete lab and its support-file references are in labs/lab-06-*.md. Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

---


### Topic 03 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO3 - Personalise and Schedule | Collect the minimum user input, resolve profile and date values predictably, convert time zones, and use a stable identifier to avoid creating duplicate calendar events. |

---


## Topic 04 — Power Automate's Deep Integration Across Multiple Data Sources  (Afternoon integration and operations · 2 connected labs)

Connections and connectors · SharePoint · Power Apps · Dataverse and Dynamics 365 patterns · SQL · gateways · monitoring · ownership · operational handover

**Key concepts**

- Connector — A packaged interface exposing triggers and actions for a service or data source.
- System of record — The authoritative platform that owns a business entity and governs its current state.
- Dataverse — The Power Platform data service for tables, relationships, security roles, and solution-aware components.
- Gateway — A managed bridge that lets cloud services reach supported on-premises data sources.
- Correlation ID — One identifier carried across systems so records and run evidence can be reconciled.
- Operations runbook — A maintained guide for ownership, dependencies, monitoring, common failures, and recovery actions.


### Connectors, Connections, Identity, and Policy

A connector defines available operations for a service; a connection authenticates those operations under a user or service identity. Standard and premium classifications affect licensing. Data policies can restrict which connectors may be used together, and an on-premises data gateway can provide a managed route to supported internal sources such as SQL Server.

A multi-source flow is only as reliable as its identities, permissions, policies, and connection lifecycle. A maker may be allowed to read SharePoint but not write SQL, or a connector combination may be blocked. Design therefore begins with a connection inventory that records system, operation, identity, owner, licence, policy group, environment, and renewal responsibility.

**How it works**

- List each system of record, required trigger or action, data classification, and expected volume.
- Select the connector and confirm whether the required operation is standard or premium.
- Choose a maintainable identity and grant only the permissions the action needs.
- Check environment policy and whether a gateway, firewall rule, or administrator setup is required.
- Record connection owner, recovery contact, and which flows depend on the connection.

**Worked example**

- The Northwind solution reads a SharePoint request, writes a Dataverse row, and inserts one SQL audit record.
- The training SQL connection is premium and is owned by a managed training identity through an approved gateway.
- The runbook records the connection name, owner, table permission, gateway, and reconnection procedure.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The integration inventory is approved and each identity has a documented operational owner. | A personal maker connection would become an undocumented production dependency. |
| The connector and gateway can meet data location, policy, licensing, latency, and volume needs. | The design attempts to bypass data policy, licensing, or network controls. |

**Practitioner quality lens**

- Authority: Name the system that owns each field and status.
- Identity: Record who authenticates, what they can do, and who maintains the connection.
- Policy: Check connector classification, environment, licence, gateway, and data rules.

**Authoritative references**

- https://learn.microsoft.com/en-us/power-automate/add-manage-connections
- https://learn.microsoft.com/en-us/connectors/
- https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem

---


### SharePoint, Power Apps, Dataverse, Dynamics 365, and SQL Patterns

SharePoint lists support collaborative records and document-centred processes. Power Apps can collect validated user input and invoke a flow. Dataverse provides relational tables, security, and solution-aware components used by model-driven apps and Dynamics 365. SQL Server provides relational queries and commands, often through premium connections and, for on-premises systems, a gateway.

Integration should not make every system a competing source of truth. The design assigns ownership: SharePoint holds the original intake, Dataverse holds governed lifecycle state, and SQL holds an append-only integration audit. Power Apps provides the interaction surface. The same Request ID and explicit field map allow the flow to reconcile data without confusing display names, option values, or data types.

**How it works**

- Declare the system of record for request, stage, decision, calendar event, and audit evidence.
- Map source field, type, required state, transformation, target field, and null behaviour.
- Carry Request ID as the correlation key through Power Apps input, SharePoint, Dataverse, and SQL.
- Use parameterised connector fields or stored procedures; never concatenate untrusted input into SQL text.
- Test create, update, duplicate, null, and permission-denied cases with synthetic data.

**Worked example**

- Power Apps sends Request ID and a validated review note to a flow.
- Flow 07A requires exactly one SharePoint item, creates or returns the keyed Dataverse row, and responds with message, Dataverse row ID, and Created/Existing state.
- The Dataverse Added event starts flow 07B, which validates the source again, inserts one SQL audit row, writes identifiers to SharePoint, and is reconciled later with the Created, Added, Existing, and any recovery-run timestamps in their defined columns.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Each system has a distinct role and the field map preserves identifiers and types. | The flow writes the same status independently in several systems without an authority rule. |
| The flow uses approved connections and synthetic or authorised data during testing. | SQL text is built by concatenating user input or a shared connection has broader rights than required. |

**Practitioner quality lens**

- Map: Document source, type, transform, target, required state, and null behaviour.
- Key: Carry one stable Request ID and persist downstream IDs returned by each system.
- Security: Use parameterised actions, least privilege, and approved connection ownership.

**Authoritative references**

- https://learn.microsoft.com/en-us/training/modules/multiple-data-sources/
- https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows
- https://learn.microsoft.com/en-us/power-automate/dataverse/create-update-delete-trigger
- https://learn.microsoft.com/en-us/connectors/sql/

---


### Monitoring, Ownership, Reliability, and Handover

Operational management keeps a flow observable and maintainable after it is built. Run history shows individual executions; analytics and alerts reveal trends; owners and co-owners maintain logic and connections; solutions organise related components for controlled movement. A runbook records purpose, dependencies, service targets, monitoring cadence, common failures, recovery, and change ownership.

A successful classroom run proves only one path at one moment. Production reliability requires ongoing evidence: whether triggers are arriving, actions are succeeding, duration and failure rates are acceptable, connections are healthy, and unresolved errors have owners. A tested Catch path and a concise runbook reduce recovery time and keep the process independent of one maker's memory.

**How it works**

- Define service expectations: schedule, volume, acceptable latency, failure threshold, and retention needs.
- Monitor the trigger count, success rate, duration, connector errors, and business completion record.
- Use Try, Catch, and Finally scopes with run-after settings and one structured error record.
- Assign primary and backup owners and confirm licensing, connection, and underlying-data access.
- Complete a runbook and rehearse one failure, recovery, retest, and communication sequence.

**Worked example**

- A synthetic Diagnostic Divisor makes a Compose action fail at runtime before the SQL insert.
- Catch sets SharePoint Status to Automation Error and sends an internal alert containing only Request ID, failed action, status, error code, message, UTC time, and owner.
- After Finally records completion, a Boolean failure flag terminates the handled run Failed. The owner removes the diagnostic, resubmits that same failed 07B run, and verifies one Dataverse row and one SQL audit row, not duplicates.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A business process needs repeatable monitoring and more than one person can perform recovery. | The flow is handed over without access checks, owner acceptance, or a tested recovery path. |
| The team can define an acceptable service level and retain enough run evidence to diagnose defects. | Alerts send raw connector payloads or personal data to recipients who do not need them. |

**Practitioner quality lens**

- Observe: Track trigger arrival, success, duration, business completion, and connection health.
- Recover: Record the first failure, owner, safe retry rule, and post-recovery verification.
- Own: Name primary and backup owners, review cadence, and change process.

**Authoritative references**

- https://learn.microsoft.com/en-us/power-automate/monitor-manage-processes
- https://learn.microsoft.com/en-us/power-automate/troubleshoot-flow-errors
- https://learn.microsoft.com/en-us/power-automate/change-cloud-flow-owner
- https://learn.microsoft.com/en-us/power-apps/maker/data-platform/solutions-overview

---


### Lab 7 — Build an Idempotent Power Apps, SharePoint, Dataverse, and SQL Integration

Learning outcome: LO4: invoke a flow from Power Apps, require one SharePoint request, enforce a Dataverse duplicate guard, react to the Dataverse add event, write one SQL audit row, and reconcile all identifiers.

Goal: Submit NW-1009 from the canvas app and prove that the same RequestID links exactly one SharePoint item, one Dataverse row and one SQL audit row across three expected runs: 07A Created, 07B Added, and 07A Existing.

You will use per-learner SharePoint, Dataverse, canvas-app, and SQL resources prepared by the trainer. The Power Apps flow rejects zero or multiple SharePoint matches and returns an existing Dataverse row instead of creating a duplicate. A Dataverse-added flow inserts one SQL audit row and writes the target identifiers back to SharePoint. The app disables its button while a submission is running.

**What you'll build**

Two solution-aware guarded cloud flows, a bound C903 Request Launcher app, exactly one Dataverse and SQL row for NW-1009, and a complete supplied-header correlation record   (Tools: Power Apps · SharePoint Online · Microsoft Dataverse · SQL Server connector · Power Automate solutions.)

**Prerequisites**

- Use only the trainer-assigned isolated SharePoint site, Power Platform environment, calendar, and SQL database.
- The trainer has provisioned C903 Northwind Automation, the active Request ID alternate key, and the C903 Request Launcher app shell.
- The same solution contains inactive 07A and 07B starter flows from labs/assets/c903-starter-solution-package-v1.0.md with the named triggers, actions, Try_write_audit/Catch_audit_error/Finally_record_run scopes, and connection-reference placeholders already arranged; complete their exact guards, mappings, formulas, and run-after settings rather than building every card from a blank canvas during this 45-minute lab.
- Your learner and trainer accounts have the required Power Apps/Power Automate premium entitlement for Dataverse and SQL, and the environment DLP policy permits the documented connectors together.
- C903 Training SQL is a trainer-owned premium connection reference to your isolated database; gateway and network health are green.
- Your training identity has permission to run the supplied DDL script and insert/select only dbo.C903AutomationAudit; it has no broader production access.
- Copy the supplied correlation-register template and keep its header unchanged.

**Step-by-step**

1. Open labs/assets/setup-automation-audit.sql in the approved training SQL editor, confirm the selected database name and learner tag with the trainer, execute the idempotent script once, and run the final queries. Confirm the table exists, the index query returns UX_C903AutomationAudit_Request_Event with IsUnique 1, and no NW-1009 row exists. Stop and ask the trainer to repair the package if the unique index is absent. Do not enter or record a connection string.

   ```bash
   Required SQL columns:
AuditID | RequestID | DataverseRowID | EventType | EventTimeUTC | FlowRunNote | CreatedUTC

Preflight query:
SELECT RequestID, COUNT(*) AS RowCount
FROM dbo.C903AutomationAudit
WHERE RequestID = N'NW-1009'
GROUP BY RequestID;

Expected before the test: zero returned groups.
   ```

2. In C903 Northwind Automation open the inactive starter Instant cloud flow C90307A_PowerApps_Submit_Request with Power Apps (V2) required Text input RequestID. Configure the existing SharePoint Get items Find_source_request with the Filter Query shown below and Condition Exactly_one_source. In its false branch configure Respond to a Power App or flow Respond_source_count_error. In the true branch configure Dataverse List rows Find_existing_lifecycle_row and Condition Lifecycle_row_missing.

   ```bash
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

3. In Lifecycle_row_missing Yes, configure the existing Dataverse Add a new row Create_lifecycle_row with the exact field map, then SharePoint Update item Persist_dataverse_ID with the current numeric item ID and every required list field, and Respond to a Power App or flow Respond_created. In No, configure Respond_existing using the first returned Dataverse row ID and create nothing.

   ```bash
   Dataverse mapping:
Request ID <- Power Apps RequestID
Request Title, Requester Email, Priority, Due Date, SharePoint Item ID, Diagnostic Divisor <- first SharePoint row
Request Status <- Open

Persist_dataverse_ID must preserve RequestID, RequestTitle, RequesterEmail, Priority, Status, DueDate, ReminderSent, ApprovalOutcome, ApprovalComments, CalendarEventID, SQLAuditID, and DiagnosticDivisor, and set DataverseRowID = the Row ID returned by Create_lifecycle_row.

Respond_created: message='Created <RequestID>'; dataverseRowID=<new GUID>; state='Created'
Respond_existing: message='Existing <RequestID>'; dataverseRowID=<first existing GUID>; state='Existing'
   ```

4. In the same solution open the inactive starter Automated cloud flow C90307B_Audit_Dataverse_Request with Dataverse When a row is added, modified or deleted: Change type Added, Table C903 Automation Requests, Scope Organization. Inside Try_write_audit configure SharePoint Get items Find_source_for_audit with your assigned training Site Address, list C903 Process Requests, and Filter Query RequestID eq '<Dataverse Request ID token>', then Condition Exactly_one_audit_source. Only in Yes configure Scope Write_audit_targets containing SQL Server Insert row (V2) Insert_audit_row and the SharePoint update with DataverseRowID, returned AuditID, and Status Open. In No send one internal count alert and Terminate Cancelled C903_AUDIT_SOURCE_COUNT without inserting an audit row.

   ```bash
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

5. Open the pre-provisioned C903 Request Launcher app shell. Add 07A from the Power Automate pane. Set the exact formulas, save, and publish. Save both 07A and 07B, select Turn on for each, and confirm both flow statuses are On before invoking the app. Create NW-1009 in your isolated SharePoint list with DiagnosticDivisor 1, play the app, select Submit once, observe that the button becomes disabled, and try to select it again while the first call is still running; the disabled control must prevent the second selection from starting another call. After the first call completes, select Submit once more to exercise the server-side Existing path. Before querying, open 07B run history, identify the NW-1009 Dataverse Added run, and refresh every 10 seconds for at most 2 minutes until its status is Succeeded. If it is still Running after 2 minutes, stop the test, record the run URL and timestamp, and escalate to the trainer; do not record a transient SQL count. After terminal success, record T23, query the three systems, and append one row using the unchanged correlation header.

   ```bash
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


**Test it**

T23 must show one SharePoint NW-1009, one Dataverse row by the active Request ID alternate key, and one SQL row by the count query. The first app response is Created and any repeated submission is Existing with the same Dataverse GUID; no second Dataverse trigger or SQL row occurs. SharePoint DataverseRowID and SQLAuditID must match the targets. Evidence must show exactly three relevant runs (07A Created, 07B Added, 07A Existing), the app button must disable while varSubmitting is true, and the correlation register must use all ten supplied columns. The SQL count is recorded only after the NW-1009 07B run reaches terminal Succeeded.

**Checkpoint and rejoin point**

Leave both solution-aware flows on, the app published, and NW-1009 Reconciled with counts 1/1/1. Lab 8 adds recovery and handover around 07B. To rejoin, repeat the app submission and confirm Existing plus unchanged Dataverse and SQL counts.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Power Apps does not recognise the flow or response fields. | Confirm the app and flow share the same isolated environment, remove and re-add the flow from the Power Automate pane, and let Power Apps insert the Run reference. |
| A repeated submission creates another Dataverse row. | Stop 07A, verify the active Request ID alternate key, inspect Find_existing_lifecycle_row and Lifecycle_row_missing, remove the duplicate synthetic row, then retest before 07B is enabled. |
| SQL Insert row is blocked. | Stop using the connection, verify the per-learner C903 Training SQL connection reference, gateway, network, and insert permission with the trainer; never substitute personal or production SQL. |

**Challenge**

Return the existing SQLAuditID in Respond_existing by querying the SharePoint source after the duplicate guard. Keep the guard mandatory and prove the SQL count remains one.

**Reflection**

Which two controls prevent a double click from creating duplicate Dataverse and SQL records?

> **Note:** The complete lab and its support-file references are in labs/lab-07-*.md. Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

---


### Lab 8 — Recover the Same Integration Run and Complete Operational Handover

Learning outcome: LO4: configure serial Try/Catch/Finally scopes, use a runtime-controlled failure, resubmit the same failed Dataverse event after correction, verify exactly-once recovery, and complete ownership and runbook evidence.

Goal: Fail NW-1099 safely at runtime, recover that same Dataverse event into one SQL row without another Dataverse row, run a separate NW-1010 regression, and hand over the automation.

You will wrap 07B in serial Try, Catch, and Finally scopes. A temporary Compose divides by the runtime Diagnostic Divisor, so NW-1099 value 0 fails only after the flow is saved and triggered. Catch filters error details and records Automation Error. You will remove the temporary action, resubmit the same failed 07B run, prove one Dataverse and one SQL row for NW-1099, and then run NW-1010 as an independent regression.

**What you'll build**

A final 07B flow with tested serial Try/Catch/Finally behaviour, same-record recovery evidence for NW-1099, NW-1010 regression evidence, approved co-owners, and a Reviewed operations runbook   (Tools: Power Automate monitoring · run-after scopes · SharePoint · Dataverse · SQL · solution ownership.)

**Prerequisites**

- Lab 7 is Reconciled for NW-1009 and both flows use your isolated resources and healthy connection references.
- Copy labs/assets/operations-runbook-template.md to work-c903/C903-Operations-Runbook.md.
- The trainer-designated backup owner has pre-provisioned read and maintenance access to the isolated SharePoint, Dataverse, and SQL resources.
- The Lab 7 starter package already supplied varAuditFailed, Failure_flag_is_true, failed-Terminate, empty Catch_audit_error and Finally_record_run scopes, and named placeholder actions; Lab 8 configures those placeholders and the supplied runbook headings during its 40-minute allocation.

**Step-by-step**

1. Edit C90307B_Audit_Dataverse_Request. Before Try_write_audit configure the existing Boolean variable varAuditFailed with initial value false. Confirm the Lab 7 SharePoint lookup, count Condition, and Write_audit_targets scope are already inside Try_write_audit. As the first direct action inside Try, before Find_source_for_audit, configure temporary Compose C903_Runtime_Diagnostic using the Dataverse trigger's Diagnostic Divisor token. Configure the existing Catch_audit_error after Try for failed, timed out, or skipped and not success. Configure the existing Finally_record_run after Catch for successful, failed, timed out, and skipped Catch outcomes.

   ```bash
   Runtime expression:
div(1,int(<Dataverse Diagnostic Divisor dynamic-content token>))

Serial run-after contract:
Try -> Catch; Catch runs only when Try is unsuccessful.
Catch -> Finally; Finally accepts every Catch status, including skipped when Try succeeds.
Finally -> Failure_flag_is_true; the Condition runs after successful Finally.
   ```

2. Inside Catch configure Filter array Only_unsuccessful_audit_actions with From = union(result('Write_audit_targets'),result('Try_write_audit')) and filter only Failed, TimedOut, or Cancelled actions so skipped placeholders are excluded. Set varAuditFailed to true. Configure only Error_action, Error_status, Error_code, and Error_message from the first filtered item using the null-safe expressions below. Configure the existing SharePoint Get items Find_failed_source using your assigned training Site Address, list C903 Process Requests, and Filter Query RequestID eq '<Dataverse Request ID token>'. Require equals(length(body('Find_failed_source')?['value']),1); when false, send a count alert and Terminate Cancelled C903_AUDIT_SOURCE_COUNT. When true, update only Status to Automation Error while preserving RequestID, RequestTitle, RequesterEmail, Priority, DueDate, ReminderSent, ApprovalOutcome, ApprovalComments, CalendarEventID, DataverseRowID, SQLAuditID, and DiagnosticDivisor. Send one internal message containing only RequestID, those four filtered error fields, utcNow(), owner, and item link. After Finally configure Condition Failure_flag_is_true with the expression below. In true, Terminate Failed with Code C903_AUDIT_RUNTIME_FAILURE; in false, end normally. This propagates the handled failure only after Finally has recorded completion.

   ```bash
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

3. Save 07B with the runtime expression. Create NW-1099 in SharePoint with DiagnosticDivisor 0 and submit it once through the app. Record T24A. Confirm one Dataverse row exists, Try fails first at C903_Runtime_Diagnostic, Catch runs, SharePoint becomes Automation Error, one filtered alert is sent, Finally runs, Failure_flag_is_true terminates the overall run Failed, and the SQL count query returns zero.

   ```bash
   NW-1099: Controlled SQL recovery test | <YOUR_TRAINING_EMAIL> | Normal | New | due in 2 days | ReminderSent No | DiagnosticDivisor 0
Expected T24A counts:
SharePoint 1 | Dataverse 1 | SQL 0
Do not click the app again; recovery must reuse this Dataverse event.
   ```

4. Delete only C903_Runtime_Diagnostic, save 07B, open the failed 07B run for NW-1099, and select Resubmit. Record T24B from the resubmitted run. Verify Try and Finally run, Catch is skipped, SharePoint returns to Open with DataverseRowID and SQLAuditID, and counts are SharePoint 1, Dataverse 1, SQL 1. Then create NW-1010 with DiagnosticDivisor 1, submit once through the app, and record T25 as a separate regression.

   ```bash
   T24B safe recovery:
Current corrected flow definition + original NW-1099 trigger data -> one SQL insert; no new Dataverse row.

NW-1010: Publish monthly automation health summary | <YOUR_TRAINING_EMAIL> | Normal | New | due in 10 days | ReminderSent No | DiagnosticDivisor 1
T25 expected: Try and Finally run; Catch skipped; SharePoint 1 | Dataverse 1 | SQL 1.
   ```

5. Inspect the latest 07A and 07B run histories and connection references. Record trigger arrival, success, duration, business completion, controlled failure, same-run resubmission, and connection health. Add the approved backup owner to both flows and verify direct access to every underlying isolated resource. Complete C903-Operations-Runbook.md with systems of record, field map, owners, connection identities, 401/403 recovery, monitor thresholds, duplicate guard, exact safe retry sequence, T24A/T24B/T25 evidence, and Reviewed acceptance. Append explicit NW-1099 and NW-1010 rows to C903-Correlation-Register.csv using the unchanged ten-column header.

   ```bash
   Safe retry sequence:
1. Query SharePoint, Dataverse, and SQL by RequestID.
2. If Dataverse exists and SQL is missing, correct 07B, open that failed 07B run, and select Resubmit once.
3. Requery counts and reconcile returned IDs; do not invoke 07A again.
4. If all target rows exist, do not resubmit.
5. For 401/403, restore the approved connection or permission before resubmission; never broaden access as a shortcut.

NW-1099 correlation row: 07A Created timestamp | 07A Existing blank | T24A failed 07B timestamp in Flow07BInitialRunTimeUTC | T24B resubmitted timestamp in Flow07BRecoveryRunTimeUTC | Reconciled.
NW-1010 correlation row: 07A Created timestamp | 07A Existing blank | T25 successful 07B timestamp in Flow07BInitialRunTimeUTC | recovery blank | Reconciled.
   ```


**Test it**

T24A must show a runtime, not save-time, failure for NW-1099; filtered Catch evidence; and counts 1/1/0. The post-Finally failure flag must make the overall T24A run Failed and therefore resubmittable. T24B must be a resubmission of that same failed 07B run and end with counts 1/1/1, reconciled IDs, Try success, Catch skipped, and Finally success. T25 must independently show 1/1/1 for NW-1010. The final saved 07B must contain no diagnostic action, both flows must have approved primary and backup owners, and the runbook must document exact resubmission, duplicate, timeout, invalid-input, 401/403, and connection-repair paths. The correlation register must include one complete row each for NW-1099 and NW-1010 with initial and recovery 07B timestamps placed in their defined columns. T24A must identify C903_Runtime_Diagnostic as the leaf Error_action and store nonblank Error_code and Error_message; documented fallback text is acceptable only when the action returns no structured detail.

**Checkpoint and rejoin point**

Publish all C903 solution components and save the Reviewed runbook, correlation register, ownership record, and T01-T25 evidence. NW-1099 and NW-1010 must both be Reconciled at 1/1/1. A returning owner can now query one RequestID, locate the exact failed run, apply the safe resubmission rule, and verify recovery without the original maker.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The diagnostic expression prevents the flow from saving. | Confirm the divisor is the Dataverse trigger's runtime Diagnostic Divisor token; do not use the constant expression div(1,0). |
| Finally does not run after Try succeeds. | Place Finally after Catch and allow every Catch status, especially skipped; on Try success Catch is skipped and Finally must accept that state. |
| Resubmission would duplicate an SQL row. | Run the count query first. Resubmit only when Dataverse exists and SQL count is zero; the unique RequestID/EventType index remains the final guard. |

**Challenge**

Build a weekly health summary from bounded run metadata that reports trigger count, success count, controlled failure count, and duration without including raw request payloads.

**Reflection**

Which evidence proves that NW-1099 was recovered rather than replaced by a different successful request?

> **Note:** The complete lab and its support-file references are in labs/lab-08-*.md. Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

---


### Topic 04 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO4 - Integrate and Operate | Select connectors by system of record, identity, licensing, policy, and latency; preserve a shared correlation ID; then hand over the flow with owners, monitoring checks, and a tested recovery path. |

---


## Wrap-Up - The Complete C903 Automation

The finished Northwind solution is a connected, observable process rather than a collection of isolated flow cards. RequestID links the intake, decisions, calendar event, lifecycle record, SQL audit row, run history, and operations runbook.

**Build and decide**

- Choose automated, scheduled, or instant triggers from the business event.
- Map dynamic content and expressions with explicit types and null handling.
- Use approvals for human decisions and conditions for deterministic rules.

**Personalise and integrate**

- Use only the minimum user profile and input data required by the action.
- Convert time zones and use a stable event key before creating calendar items.
- Assign system-of-record ownership and carry RequestID across SharePoint, Dataverse, Power Apps, and SQL.

**Operate and recover**

- Inspect run history and target-system evidence for every normal and exceptional path.
- Use Try, Catch, and Finally scopes with structured, non-sensitive error records.
- Hand over co-owners, connections, monitoring checks, safe retry rules, and a tested runbook.

---


## Next Steps

- Repeat all eight labs from the clean synthetic source files without using completed flow screenshots.
- Adapt the E-D-D-A-E-O design worksheet to one authorised repeated process in your role.
- Create a small connection inventory for identity, permissions, licensing, policy, owner, and recovery.
- Review current Microsoft Learn and connector documentation before delivery because designer labels, limits, and capabilities continue to change.


## Glossary

- **Action** — A configured operation that executes after a trigger or control step.
- **Automated flow** — A cloud flow started by an event in a connected service.
- **Business process flow** — A Dataverse-backed stage experience that guides a person through a record lifecycle.
- **Connection** — An authenticated relationship used by a connector under a user or service identity.
- **Connector** — A packaged interface that exposes triggers and actions for a service.
- **Correlation ID** — A stable identifier carried across systems so records and run evidence can be reconciled.
- **Dataverse** — The Power Platform data service for tables, relationships, security, apps, and solution-aware components.
- **Dynamic content** — A value token produced by a trigger or earlier action.
- **Expression** — A formula used to transform, validate, combine, or default values.
- **Gateway** — A managed bridge between cloud services and supported on-premises data sources.
- **Idempotency** — The property that repeating a request does not create an unintended duplicate outcome.
- **Instant flow** — A cloud flow started by a person, button, or app invocation.
- **Run after** — A dependency setting controlling whether an action runs after success, failure, skip, or timeout.
- **Run history** — The record of flow executions, inputs, outputs, duration, status, and errors.
- **Scheduled flow** — A cloud flow started by a recurrence configuration.
- **System of record** — The authoritative platform that owns a business entity or field.
- **Trigger** — The event, recurrence, or invocation that creates a flow run.
- **Trigger condition** — An expression evaluated before a trigger creates a run.
