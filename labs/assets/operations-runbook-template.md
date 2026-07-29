# C903 Northwind Automation Operations Runbook

## Document Control

| Field | Value |
|---|---|
| Version | 1.0 |
| Owner | `<PRIMARY_OWNER>` |
| Backup owner | `<BACKUP_OWNER>` |
| Last reviewed | `<YYYY-MM-DD>` |
| State | Draft / Reviewed |

## Purpose and Business Outcome

- Process:
- Intended users:
- Triggering event:
- Observable completion:
- Out of scope:

## Components

| Component | Type | Purpose | Owner |
|---|---|---|---|
| C903 Process Requests | SharePoint list | Intake and automation state | |
| C90307A_PowerApps_Submit_Request | Instant cloud flow | App submission and Dataverse creation | |
| C903 Automation Request | Dataverse table | Governed lifecycle record | |
| C90307B_Audit_Dataverse_Request | Automated cloud flow | Dataverse event to SQL audit | |
| dbo.C903AutomationAudit | SQL table | Append-only integration evidence | |
| C903 Request Launcher | Canvas app | Validated user invocation | |

## Trigger Contracts

### 07A Power Apps trigger

- Required inputs:
- Validation:
- Correlation key:
- Response fields:

### 07B Dataverse trigger

- Table:
- Change type:
- Scope:
- Qualifying rule:
- Correlation key:

## Systems of Record and Field Map

| Business data | Source | Type | Transform | Target | Null rule |
|---|---|---|---|---|---|
| RequestID | | | | | |
| RequestTitle | | | | | |
| Priority | | | | | |
| DueDate | | | | | |
| DataverseRowID | | | | | |
| SQLAuditID | | | | | |

## Connections and Dependencies

| Connection or dependency | Identity | Permission needed | Owner | Recovery |
|---|---|---|---|---|
| SharePoint | | | | |
| Dataverse | | | | |
| SQL | | | | |
| Power Apps | | | | |

Never record passwords, tokens, secrets, or connection strings in this runbook.

## Monitoring

| Check | Evidence | Frequency | Threshold | Owner |
|---|---|---|---|---|
| Trigger arrivals | | | | |
| Run success | | | | |
| Duration | | | | |
| Business completion | | | | |
| Connection health | | | | |
| Duplicate count | | | | |

## Common Failures and Recovery

| Symptom | First place to inspect | Likely cause | Recovery | Verification |
|---|---|---|---|---|
| No run | | | | |
| First red action | | | | |
| Green run, wrong result | | | | |
| SQL write missing | | | | |
| Duplicate target record | | | | |
| Connection invalid | | | | |

## Safe Retry Rule

1. Query SharePoint, Dataverse, and `dbo.C903AutomationAudit` by `RequestID`.
2. If both target rows exist, reconcile identifiers and do not resubmit.
3. If Dataverse exists but SQL does not, correct the Dataverse-to-SQL flow, open that failed run, and select **Resubmit** once. Do not invoke the Power Apps flow again.
4. If neither target exists, submit once through the approved app.
5. Requery SharePoint, Dataverse, and SQL; verify counts, run statuses, and all returned identifiers.
6. For 401 or 403 errors, restore the approved connection or permission before resubmission; never broaden access as a shortcut.

## Tested Evidence

| Test | RequestID | Expected | Actual | Run evidence | Reviewer |
|---|---|---|---|---|---|
| T24A controlled failure | NW-1099 | | | | |
| T24B same-run recovery | NW-1099 | | | | |
| T25 regression success | NW-1010 | | | | |

## Ownership Acceptance

| Role | Name | Access verified | Runbook reviewed | Date |
|---|---|---|---|---|
| Primary owner | | | | |
| Backup owner | | | | |

## Change Log

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | `<YYYY-MM-DD>` | Initial C903 training runbook | `<NAME>` |
