# Lab 5 — Create a Validated User-Driven Follow-Up Flow

**Course:** PL-7002 Create and Manage Automated Processes by using Power Automate  
**Course Code:** C903  
**Version:** v1.0 (29 July 2026)  
**Topic 3:** Build Flows to Manage User Information  
**Maps to:** LO3: validate instant-flow inputs, retrieve the invoking user's minimum profile data, resolve one location variable through both branches, and format a follow-up date  
**Duration:** 30 minutes  
**Tools:** Power Automate instant flows · SharePoint Online · Office 365 Users · Office 365 Outlook

---

## Goal

Let a coordinator request a follow-up for one RequestID and receive a confirmation built from validated input, a single resolved location value, and a consistently formatted date.

## What You Will Do

You will create an instant flow with RequestID, Follow-up Date, Work Mode, and Use Directory Location inputs. The flow normalises and validates Work Mode before reading profile data, requires exactly one SharePoint request, retrieves only Display Name, Mail, and Office Location, and sets one ResolvedLocation variable in both location branches.

## What You Will Build

An instant cloud flow named C903-05-Create-User-Follow-Up with a four-field input contract, invalid-input termination, exactly-one lookup, minimum profile retrieval, and one branch-safe variable

## Prerequisites

- Use your trainer-assigned isolated SharePoint list and approved Microsoft 365 training account.
- C903 Process Requests contains NW-1007 and NW-1008 exactly once.
- Know whether the training profile Office Location is populated; do not edit directory properties.
- The approved training profile has a populated Mail value. If it does not, stop and ask the trainer to repair the isolated account before the timed lab.
- The trainer has provisioned the inactive C903-05-Create-User-Follow-Up starter from labs/assets/c903-starter-solution-package-v1.0.md with its inputs, validation branches, lookup, profile, variable, date Compose, and email placeholders already arranged.

> **Data note.** Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

## Steps

### 1. Open the inactive starter Instant cloud flow C903-05-Create-User-Follow-Up. Configure the existing Manually trigger a flow card and its four required inputs in this order with the stated guidance.

```text
RequestID - Text - example NW-1007
Follow-up Date - Date - intended local calendar date
Work Mode - Text - allowed values Office or Remote
Use Directory Location - Yes/No - Yes uses a non-empty profile value; No uses Work Mode
```

### 2. Configure the existing Compose Normalised_work_mode with the expression below and Condition Work_mode_is_allowed to test whether the output equals office or remote. In the false branch configure Terminate with Status Cancelled, Code C903_INVALID_WORK_MODE, and message 'Use Office or Remote'. Put every later action in the valid branch so invalid input retrieves no profile data and sends no email.

```text
Normalisation pattern:
toLower(trim(<Work Mode dynamic-content token>))

Condition expression:
or(equals(outputs('Normalised_work_mode'),'office'),equals(outputs('Normalised_work_mode'),'remote'))
```

### 3. In the valid branch configure the existing SharePoint - Get items Find_request_by_ID with Filter Query RequestID eq '<RequestID trigger token>'. Configure Condition Exactly_one_request using the array-length expression. If false, configure Terminate with Status Cancelled, Code C903_REQUEST_COUNT, and a message containing the actual count. If true, configure Office 365 Users - Get my profile (V2) Get_invoking_user_profile.

```text
Count expression:
length(body('Find_request_by_ID')?['value'])
Required count: 1

Get my profile (V2) Select fields: displayName,mail,officeLocation
Profile properties used later:
Display Name | Mail | Office Location
Do not retrieve or expose unrelated profile properties.
```

### 4. Configure the existing String variable ResolvedLocation with an empty initial value. Configure Condition Use_directory_location to require Use Directory Location = Yes and Office Location is not empty. In the true branch Set variable ResolvedLocation to Office Location. In the false branch Set variable ResolvedLocation to Normalised_work_mode. After the Condition configure Compose Follow_up_date_display and Send an email (V2).

```text
Date expression:
formatDateTime(<Follow-up Date input>,'dd MMM yyyy')

Subject: Follow-up recorded - <RequestID>
Body: Hello <Display Name>; RequestID; RequestTitle; Follow-up Date; ResolvedLocation; and a note that isolated synthetic training data was used.
To: profile Mail
```

### 5. Save, select Turn on, confirm the flow status is On, and exercise three cases without editing the flow definition. Record T14-T16 with input, branch, resolved value, profile properties exposed, final status, and message subject.

```text
T14 NW-1007 | Work Mode Remote | Use Directory Location Yes -> profile Office Location when non-empty, otherwise remote
T15 NW-1008 | Work Mode Office | Use Directory Location No -> office
T16 NW-1008 | Work Mode Airport | Use Directory Location No -> Cancelled C903_INVALID_WORK_MODE; profile and email actions do not run
```

## Test It

The trigger must have four required inputs. T14 and T15 must find exactly one request and consume the same ResolvedLocation variable after the location Condition. T16 must terminate before profile retrieval and send no email. The two valid messages may expose only Display Name, Mail, resolved location, synthetic request fields, and the formatted date. No flow logic is edited between tests.

## Checkpoint and Rejoin Point

Keep the final flow unchanged after T16 and save T14-T16. Lab 6 reuses the exactly-one RequestID pattern and adds date-time, duration, calendar, and duplicate validation. To rejoin, rerun T15 and confirm ResolvedLocation equals office through the real saved branch logic.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Get items returns zero or more than one row. | Inspect the exact RequestID input and isolated list, then use the count in C903_REQUEST_COUNT to correct the data instead of selecting an arbitrary row. |
| The email cannot access a branch-local location value. | Confirm ResolvedLocation is initialised before the Condition and both branches use Set variable rather than separate Compose actions. |
| The profile Mail value is empty. | Stop and ask the trainer to repair the isolated training profile. Do not add an unapproved fallback or retrieve extra profile fields during the timed lab. |

## Challenge

Bind Work Mode to an Office/Remote choice control in the pre-provisioned C903 canvas app shell and explain how allowed values reduce downstream termination cases.

## Reflection

How did early validation and one shared variable make the later email action safer and easier to inspect?

---

[← Lab 4](lab-04-create-and-traverse-a-conditional-dataverse-business-process-flow.md) · [Lab 6 →](lab-06-block-calendar-time-with-validation-and-duplicate-prevention.md)
