# Lab 3 — Build a Priority Approval with Complete Outcome and Recovery Paths

**Course:** PL-7002 Create and Manage Automated Processes by using Power Automate  
**Course Code:** C903  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Build Approval Flows with Power Automate  
**Maps to:** LO2: create and configure an approval, implement High and non-High paths, persist every custom outcome, exercise an approval timeout, and record filtered technical error details  
**Duration:** 45 minutes  
**Tools:** SharePoint Online · Power Automate Approvals · Office 365 Outlook · conditions and control scopes

---

## Goal

Route only High-priority Northwind requests to a named approver and close every approval, non-approval, default, or timeout path with an explicit SharePoint status, a requester message for handled business outcomes, or a filtered internal alert for technical failure.

## What You Will Do

You will build an automated flow for new SharePoint requests. High priority creates an approval with Approve, Need more information, and Reject responses; other priorities continue without an approval. The flow stores outcome, comments, and status on the same request. A one-minute training timeout exercises Catch, which filters the scope result down to action name, status, error code, and message.

## What You Will Build

An automated cloud flow named C903-03-Approve-High-Priority-Request with explicit non-High actions, three approval cases, a default case, serial Try/Catch/Finally scopes, and five path tests

## Prerequisites

- Labs 1 and 2 are complete in your trainer-assigned isolated SharePoint site.
- C903 Process Requests includes ApprovalOutcome, ApprovalComments, and DiagnosticDivisor from request-schema.md.
- The approved training account can create approvals and update its own isolated list.
- Use your training email as requester and approver unless the trainer supplies a separate isolated approver account.
- The trainer has provisioned the inactive C903-03-Approve-High-Priority-Request starter from labs/assets/c903-starter-solution-package-v1.0.md in your isolated environment with the trigger, named scopes, switch cases, and placeholder actions already arranged; you configure connections, mappings, expressions, run-after settings, and messages during this 45-minute lab.

> **Data note.** Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

## Steps

### 1. Open the inactive starter Automated cloud flow named C903-03-Approve-High-Priority-Request with SharePoint - When an item is created, pointed to your C903 Process Requests list. Rename the trigger Request_for_routing. Configure the existing Condition Is_high_priority and compare Priority Value with High. In the non-High branch configure Update item Continue_without_approval and Send an email (V2) Notify_no_approval_required.

```text
Non-High mapping:
Update the current numeric item ID; map RequestID, RequestTitle, RequesterEmail, Priority, DueDate, ReminderSent, and DiagnosticDivisor from the trigger.
Status = Open
ApprovalOutcome = Not required
ApprovalComments = Priority did not require approval

Email subject: No approval required - <RequestID>
Email body: RequestID; Priority; Status Open; item link.
```

### 2. In the High branch configure the existing Scope Try_approval. Inside it configure the update of the current item to Pending Approval, then configure Approvals - Start and wait for an approval named Request_operations_decision. Choose Custom Responses - Wait for one response and enter the three response labels exactly. In the action Settings set Timeout to PT1M for this isolated training exercise.

```text
Responses, in order:
Approve
Need more information
Reject

Title: <RequestID> - <RequestTitle>
Assigned to: <YOUR_TRAINING_EMAIL>
Details: Priority; DueDate; RequesterEmail; SharePoint item link.
Training timeout: PT1M. A workplace design must use its approved service target.
```

### 3. After the approval, still inside Try_approval, configure the existing Switch Route_decision on the approval Outcome. Create Approve, Need more information, and Reject cases plus a Default case. In every case update the same item, map all required fields, set ApprovalOutcome to the exact response, store the first response Comments in ApprovalComments, and send a matching email.

```text
Approve -> Status Approved; subject Decision: approved - <RequestID>
Need more information -> Status More Info; subject Decision: more information needed - <RequestID>
Reject -> Status Rejected; subject Decision: rejected - <RequestID>
Default -> Status Automation Error; subject Decision response not recognised - <RequestID>

Every decision message includes RequestID, Outcome, Completion date, Comments, and item link.
```

### 4. After Try_approval configure the existing Scope Catch_approval_error to run after Try has failed, timed out, or been skipped, and not after success. Inside Catch configure Filter array Only_unsuccessful_actions with From = result('Try_approval') and the status condition below, excluding deliberately skipped actions. Configure Compose actions Error_action, Error_status, Error_code, and Error_message from the first filtered item using the null-safe expressions below. Update the request to Automation Error and send one internal filtered-error message. Configure Finally_record_completion after Catch and configure it for every Catch outcome, including skipped.

```text
Filter condition:
@or(equals(item()?['status'],'Failed'),equals(item()?['status'],'TimedOut'),equals(item()?['status'],'Cancelled'))

Filtered fields:
first(body('Only_unsuccessful_actions'))?['name']
first(body('Only_unsuccessful_actions'))?['status']
coalesce(first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['error']?['code'],first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['code'],first(body('Only_unsuccessful_actions'))?['outputs']?['error']?['code'],first(body('Only_unsuccessful_actions'))?['error']?['code'],'NO_CODE_FROM_ACTION')
coalesce(first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['error']?['message'],first(body('Only_unsuccessful_actions'))?['outputs']?['body']?['message'],first(body('Only_unsuccessful_actions'))?['outputs']?['error']?['message'],first(body('Only_unsuccessful_actions'))?['error']?['message'],'No connector message returned')

Internal email includes only RequestID, those four fields, utcNow(), owner, and item link. Do not include result('Try_approval') or a raw action payload in the message.
```

### 5. Save, select Turn on, confirm the flow status is On, and exercise five isolated records one at a time. Respond from the approval centre for the first three High records; do not respond to the timeout record. Record T07-T11 in C903-Test-Evidence.csv with RequestID, Priority, approval created Yes/No, response or timeout, final SharePoint status, ApprovalComments, message subject, and run timestamp.

```text
Create each record with RequestID | RequestTitle | RequesterEmail | Priority | Status | DueDate | ReminderSent | DiagnosticDivisor, using your training email, Status New, a future due date, No, and 1:
T07 NW-1007 | Approve supplier onboarding automation | <YOUR_TRAINING_EMAIL> | High -> Approve with comment 'Approved for the training route' -> Approved
T08 NW-1011 | Review customer refund approval | <YOUR_TRAINING_EMAIL> | High -> Need more information with comment 'Add the process owner' -> More Info
T09 NW-1012 | Review warehouse exception route | <YOUR_TRAINING_EMAIL> | High -> Reject with comment 'Outside the training scope' -> Rejected
T10 NW-1008 | Send a normal-priority operations update | <YOUR_TRAINING_EMAIL> | Normal -> no approval -> Open
T11 NW-1013 | Exercise the isolated approval timeout | <YOUR_TRAINING_EMAIL> | High -> no response for PT1M -> Catch -> Automation Error

Every RequestID is created once in your isolated list.
```

## Test It

T07-T09 must each create one approval, store the exact outcome and supplied comment, update the expected status, and send one matching decision message. T10 must create no approval and must take the explicit non-High update and message path. T11 must time out, run Catch, store Automation Error, and send only the filtered action name, status, code, and message. Finally must run after both successful and skipped Catch outcomes. Error_code and Error_message must both be nonblank in T11 evidence; use the documented fallback text only when the connector supplies no structured code or message.

## Checkpoint and Rejoin Point

Leave NW-1007 Approved, NW-1011 More Info, NW-1012 Rejected, NW-1008 Open, and NW-1013 Automation Error. Save T07-T11, then turn C903-03-Approve-High-Priority-Request off so it cannot intercept the High-priority records created in later labs. Lab 4 reuses NW-1007 and NW-1008 field values in Dataverse. To rejoin, verify all five outcome rows and the filtered timeout message.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The approval is not visible in email. | Open Power Automate Approvals, confirm Assigned to matches the signed-in training account, and respond from the approval centre. |
| The Switch does not match the selected response. | Open the approval output, copy the exact Outcome text, and make the case label match spaces and capitalisation exactly. |
| Catch exposes more data than the four error fields. | Remove the raw scope result from the email, confirm Filter array excludes Succeeded actions, and map only Error_action, Error_status, Error_code, and Error_message. |

## Challenge

After completing the timed test, change the approval timeout to a realistic organisational service target and document the separate escalation owner and cancellation rule without altering the five recorded training runs.

## Reflection

Which paths express business decisions, and which path exists only to recover a technical exception?

---

[← Lab 2](lab-02-build-a-scheduled-reminder-and-diagnose-a-controlled-failure.md) · [Lab 4 →](lab-04-create-and-traverse-a-conditional-dataverse-business-process-flow.md)
