# Northwind Request Data Contract

The same `RequestID` is carried across SharePoint, Power Apps, Dataverse, calendar evidence, SQL, and run-history notes. Each platform-generated identifier is stored separately.

## SharePoint: C903 Process Requests

| Column | Type | Required | Purpose |
|---|---|---:|---|
| RequestID | Single line of text | Yes | Stable cross-system correlation key |
| RequestTitle | Single line of text | Yes | Human-readable request name |
| RequesterEmail | Single line of text | Yes | Synthetic or approved training recipient |
| Priority | Choice: Low, Normal, High | Yes | Routing and business-process branch |
| Status | Choice | Yes | SharePoint intake and automation state |
| DueDate | Date only | Yes | Reminder and follow-up date |
| ReminderSent | Yes/No | Yes | Duplicate reminder guard |
| ApprovalOutcome | Single line of text | No | Returned human decision |
| ApprovalComments | Multiple lines of text | No | Returned decision comment or filtered recovery note |
| CalendarEventID | Single line of text | No | Returned Outlook event identifier |
| DataverseRowID | Single line of text | No | Returned Dataverse row identifier |
| SQLAuditID | Number | No | Returned SQL identity value |
| DiagnosticDivisor | Number, default 1 | Yes | Synthetic runtime-fault control used only in isolated training |

Allowed `Status` values:

- New
- Open
- Pending Approval
- Approved
- More Info
- Rejected
- Scheduled
- Closed
- Automation Error

## Dataverse: C903 Automation Request

| Column | Type | Required | Governing use |
|---|---|---:|---|
| Request ID | Text | Yes | Cross-system correlation key |
| Request Title | Text | Yes | Lifecycle record title |
| Requester Email | Email | No | Approved training recipient |
| Priority | Choice | Yes | High branch versus default branch |
| Request Status | Choice | Yes | Business-process stage state |
| Due Date | Date only | No | Target date |
| Approval Outcome | Text | No | Decision evidence |
| SharePoint Item ID | Whole number | No | Source intake identifier |
| Diagnostic Divisor | Whole number, default 1 | Yes | Synthetic runtime-fault control used only in isolated training |

## Data authority

| Data | System of record |
|---|---|
| Original request and requester | SharePoint |
| Governed stage and lifecycle state | Dataverse |
| Calendar side effect | Outlook Calendar, referenced by stored Event ID |
| Integration event evidence | SQL append-only audit table |
| Technical execution details | Power Automate run history |

## Required field-map checks

1. Preserve `RequestID` exactly; never substitute a display title as the key.
2. Map choice values deliberately and verify their stored target value.
3. Keep stored UTC timestamps separate from local display formatting.
4. Treat empty optional values explicitly.
5. Never concatenate untrusted input into SQL text.

## Isolation requirement

Every learner uses a trainer-assigned SharePoint site/list, Power Platform environment, Outlook calendar, and SQL database or schema. The fixed `NW-*` identifiers are safe only inside those isolated resources. Do not run the labs in a shared class list, shared Dataverse table, shared calendar, or production database.
