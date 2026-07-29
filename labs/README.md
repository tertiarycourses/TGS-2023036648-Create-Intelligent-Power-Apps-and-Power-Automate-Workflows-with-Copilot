# PL-7002 Create and Manage Automated Processes by using Power Automate — Hands-On Labs

8 labs across 4 topics · 1 day · 7.5 instructional hours

Work through the labs in order — each one builds on the artifacts you produced in the labs before it.


## Topic 1 — Get Started with Power Automate

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 1 | [Validate the Northwind Request Intake and Create an Automated Acknowledgement](lab-01-validate-the-northwind-request-intake-and-create-an-automated-acknowledgement.md) | SharePoint Online · Power Automate cloud flows · Office 365 Outlook | A validated per-learner SharePoint list named C903 Process Requests, an automated cloud flow named C903-01-Acknowledge-New-Request, and a saved evidence record for RequestID NW-1006 |
| 2 | [Build a Scheduled Reminder and Diagnose a Controlled Failure](lab-02-build-a-scheduled-reminder-and-diagnose-a-controlled-failure.md) | Power Automate scheduled flows · SharePoint Online · Office 365 Outlook | A scheduled cloud flow named C903-02-Remind-Due-Requests, evidence rows for normal, empty, duplicate, and controlled-failure cases, and a recorded primary and backup owner |

## Topic 2 — Build Approval Flows with Power Automate

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 3 | [Build a Priority Approval with Complete Outcome and Recovery Paths](lab-03-build-a-priority-approval-with-complete-outcome-and-recovery-paths.md) | SharePoint Online · Power Automate Approvals · Office 365 Outlook · conditions and control scopes | An automated cloud flow named C903-03-Approve-High-Priority-Request with explicit non-High actions, three approval cases, a default case, serial Try/Catch/Finally scopes, and five path tests |
| 4 | [Create and Traverse a Conditional Dataverse Business Process Flow](lab-04-create-and-traverse-a-conditional-dataverse-business-process-flow.md) | Power Apps maker portal · Microsoft Dataverse · business process flows · model-driven apps | An active C903 Request Lifecycle business process flow in the C903 Northwind Automation solution, published in C903 Request Manager, with complete High and Normal path evidence |

## Topic 3 — Build Flows to Manage User Information

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 5 | [Create a Validated User-Driven Follow-Up Flow](lab-05-create-a-validated-user-driven-follow-up-flow.md) | Power Automate instant flows · SharePoint Online · Office 365 Users · Office 365 Outlook | An instant cloud flow named C903-05-Create-User-Follow-Up with a four-field input contract, invalid-input termination, exactly-one lookup, minimum profile retrieval, and one branch-safe variable |
| 6 | [Block Calendar Time with Validation and Duplicate Prevention](lab-06-block-calendar-time-with-validation-and-duplicate-prevention.md) | Power Automate instant flows · SharePoint Online · Office 365 Outlook Calendar · control scopes | An instant cloud flow named C903-06-Block-Follow-Up-Time, one calendar event for NW-1007, a persisted Event ID, and evidence for six validation and duplicate cases |

## Topic 4 — Power Automate's Deep Integration Across Multiple Data Sources

| # | Lab | Tools | You Build |
|---|-----|-------|-----------|
| 7 | [Build an Idempotent Power Apps, SharePoint, Dataverse, and SQL Integration](lab-07-build-an-idempotent-power-apps-sharepoint-dataverse-and-sql-integration.md) | Power Apps · SharePoint Online · Microsoft Dataverse · SQL Server connector · Power Automate solutions | Two solution-aware guarded cloud flows, a bound C903 Request Launcher app, exactly one Dataverse and SQL row for NW-1009, and a complete supplied-header correlation record |
| 8 | [Recover the Same Integration Run and Complete Operational Handover](lab-08-recover-the-same-integration-run-and-complete-operational-handover.md) | Power Automate monitoring · run-after scopes · SharePoint · Dataverse · SQL · solution ownership | A final 07B flow with tested serial Try/Catch/Finally behaviour, same-record recovery evidence for NW-1099, NW-1010 regression evidence, approved co-owners, and a Reviewed operations runbook |

---

> Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.


_Tertiary Infotech Academy Pte Ltd · C903 · v1.0 (29 July 2026)_
