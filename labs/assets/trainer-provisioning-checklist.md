# C903 Trainer Pre-Class Provisioning Checklist

Use with `c903-starter-solution-package-v1.0.md`.

Course: PL-7002 Create and Manage Automated Processes by using Power Automate

Course code: C903

Starter package: C903-Northwind-Automation-Starter v1.0 / solution 1.0.0.0

Learner tag: ____________________

Trainer: ____________________

Verification date (UTC): ____________________

## Isolation

- [ ] Assigned SharePoint site/list is isolated to this learner.
- [ ] Assigned Power Platform environment and C903 solution are isolated to this learner.
- [ ] Assigned Outlook calendar is isolated to this learner.
- [ ] Assigned SQL database or schema is isolated to this learner.
- [ ] No production data, personal connector, shared class table, or shared calendar is in use.

## SharePoint and evidence

- [ ] `C903 Process Requests` matches `request-schema.md`.
- [ ] Baseline rows match `process-requests.csv`.
- [ ] `DiagnosticDivisor` defaults to 1.
- [ ] `CalendarEventID`, `DataverseRowID`, and `SQLAuditID` are clear for the designated tests.
- [ ] Evidence and correlation templates are present and writable.

## Power Platform components

- [ ] Solution `C903 Northwind Automation` reports version 1.0.0.0.
- [ ] Dataverse table and active Request ID alternate key are present.
- [ ] `C903 Request Launcher` and `C903 Request Manager` shells open.
- [ ] Business-process prerequisites (Dataverse table, form, and model-driven app) are present; no learner BPF has been pre-created.
- [ ] All six starter flows exactly match the versioned package inventory.
- [ ] Every starter flow is Off.
- [ ] Every learner-editable placeholder is named exactly as documented.

## Connections and permissions

- [ ] Every learner and the trainer account have the required Power Apps/Power Automate premium entitlement for Dataverse and the SQL Server connector.
- [ ] The environment DLP policy permits the documented SharePoint, Outlook, Office 365 Users, Dataverse, Power Apps, and SQL connectors together in the approved business-data group.
- [ ] No tenant policy, connector block, or environment routing rule prevents the six starter flows from being saved, turned on, or run.
- [ ] SharePoint, Outlook, Office 365 Users, Dataverse, Power Apps, and SQL connection references prompt for or use only the approved training identity.
- [ ] SQL gateway and network status are green.
- [ ] Learner has only the documented DDL/DML rights on `dbo.C903AutomationAudit`.
- [ ] Trainer-designated backup owner has the documented maintenance access.
- [ ] Training profile `Mail` is populated; Office Location state is known.

## Timed-lab readiness

- [ ] Lab 2 starter saves with its placeholders and is Off.
- [ ] Lab 3 starter saves with its placeholders and is Off.
- [ ] Lab 5 starter saves with its placeholders and is Off.
- [ ] Lab 6 starter saves with its placeholders and is Off.
- [ ] Lab 7 starters 07A and 07B save with their placeholders and are Off.
- [ ] Lab 8 failure flag, Catch, Finally, and post-Finally Terminate placeholders are present.
- [ ] Trainer has rehearsed T01-T25 using a disposable isolated learner bundle.
- [ ] In a disposable copy of `C903-06-Block-Follow-Up-Time`, the trainer temporarily sets `Create_follow_up_event` Calendar ID to `C903-NONEXISTENT-CALENDAR`, runs the valid T17 input, and verifies `Catch_calendar_technical` records `Create_follow_up_event`, a failed/timed-out/cancelled status, and nonblank `Error_code` and `Error_message`.
- [ ] After that bounded failure check, the trainer restores the approved learner Calendar ID, saves, reruns the valid path successfully, deletes the disposable event and flow copy, and confirms the learner starter remains Off and unchanged.
- [ ] Any failed rehearsal data has been reset before learner access.

Ready for class: Yes / No

Trainer initials: ____________________

Notes: ______________________________________________________________________
