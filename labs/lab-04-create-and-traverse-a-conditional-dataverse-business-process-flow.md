# Lab 4 — Create and Traverse a Conditional Dataverse Business Process Flow

**Course:** PL-7002 Create and Manage Automated Processes by using Power Automate  
**Course Code:** C903  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Build Approval Flows with Power Automate  
**Maps to:** LO2: create a business process flow on a pre-provisioned Dataverse table, branch by priority, activate it, and traverse one High and one Normal record through every stage in their path  
**Duration:** 40 minutes  
**Tools:** Power Apps maker portal · Microsoft Dataverse · business process flows · model-driven apps

---

## Goal

Give Northwind coordinators a visible lifecycle in which High-priority requests traverse Approval while other requests move from Review directly to Fulfilment, and prove both paths reach Closure.

## What You Will Do

The trainer has pre-provisioned the solution, table, alternate key, main form, active view, and app shell so the timed lab focuses on process design. You will verify the model, create a five-stage business process flow, add a High-priority branch, activate it, and advance NW-1007 and NW-1008 through every expected stage.

## What You Will Build

An active C903 Request Lifecycle business process flow in the C903 Northwind Automation solution, published in C903 Request Manager, with complete High and Normal path evidence

## Prerequisites

- Use your trainer-assigned isolated Power Platform environment with Dataverse maker permissions.
- The trainer has provisioned C903 Northwind Automation, C903 Automation Request, and C903 Request Manager.
- Request ID is an active mandatory alternate key; if the key is absent, stop and ask the trainer to restore provisioning.
- Copy labs/assets/correlation-register-template.csv to work-c903/C903-Correlation-Register.csv.

> **Data note.** Use only the supplied synthetic Northwind data and your trainer-assigned isolated site, environment, calendar, database, and connections. Never place credentials, secrets, personal production data, or raw connection strings in a flow, prompt, lab file, or repository.

## Steps

### 1. At make.powerapps.com select your isolated training environment and open C903 Northwind Automation. Inspect C903 Automation Request and verify the exact columns, types, required settings, Request ID alternate key, main form, active view, and model-driven app page. Do not continue if any item differs.

```text
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

### 2. Inside the solution create Automation - Process - Business process flow named C903 Request Lifecycle for C903 Automation Request. Add stages in order Intake, Review, Approval, Fulfilment, Closure. Add the stated data steps and mark only Request ID and Request Title required in Intake.

```text
Intake: Request ID, Request Title, Requester Email
Review: Priority, Due Date
Approval: Approval Outcome, Request Status
Fulfilment: Request Status
Closure: Request Status
```

### 3. Insert Condition High_priority_route after Review with Priority Equals High. Connect true to Approval then Fulfilment; connect false directly to Fulfilment; connect both to Closure. Select Validate, correct any disconnected component, Save, and Activate.

```text
High path: Intake -> Review -> Approval -> Fulfilment -> Closure
Default path: Intake -> Review -> Fulfilment -> Closure
Every branch must reach Closure.
```

### 4. Add the active C903 Request Lifecycle process to C903 Request Manager if it is not automatically available. Save and Publish the app. Open it and create NW-1007 and NW-1008 using the Lab 3 values, including each source SharePoint numeric item ID and Diagnostic Divisor 1.

```text
NW-1007: High | Approved | Approve supplier onboarding automation
NW-1008: Normal | Open | Send a normal-priority operations update
Use the exact Request ID alternate key; a duplicate create must be rejected.
```

### 5. For NW-1007, record the active stage, complete required values, and select Next Stage through Intake, Review, Approval, Fulfilment, and Closure; set final Request Status Closed. Repeat NW-1008 through Intake, Review, Fulfilment, and Closure. Record T12 and T13 with every observed stage and add both generated Dataverse row IDs to C903-Correlation-Register.csv.

```text
T12 NW-1007 expected: Intake | Review | Approval | Fulfilment | Closure | Closed
T13 NW-1008 expected: Intake | Review | Fulfilment | Closure | Closed

Correlation header, unchanged:
RequestID | SharePointItemID | DataverseRowID | CalendarEventID | SQLAuditID | Flow07ACreatedRunTimeUTC | Flow07AExistingRunTimeUTC | Flow07BInitialRunTimeUTC | Flow07BRecoveryRunTimeUTC | State
```

## Test It

The solution must contain the active five-stage C903 Request Lifecycle with one High-priority branch and an active Request ID alternate key. T12 must show all five stages for NW-1007 and T13 must show the four-stage default path for NW-1008. Both records must reach Closure and end Closed. The correlation register must use the supplied header and store the SharePoint and Dataverse IDs for both RequestIDs.

## Checkpoint and Rejoin Point

Keep the solution and app published and both records Closed. Save T12-T13 and the correlation register. Lab 7 reuses the table, alternate key, solution, and app shell with a new NW-1009 record. To rejoin, open both completed process instances and verify every active-stage transition recorded in the evidence.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The process cannot activate. | Select Validate, connect every stage and branch to Closure, confirm each data step references an existing column, save, and activate again. |
| Both records follow the same branch. | Confirm Priority stores different choice values, inspect the High_priority_route operator and value, then restart the affected isolated process instance. |
| A duplicate Request ID is accepted. | Stop the lab and ask the trainer to activate the Request ID alternate key; downstream exactly-once behaviour depends on it. |

## Challenge

Add a Low-priority branch only if every route still reaches Closure. Draw the result and explain why a small number of explicit paths is easier to operate than deeply nested branching.

## Reflection

What does full stage traversal prove that checking only the first branch decision does not?

---

[← Lab 3](lab-03-build-a-priority-approval-with-complete-outcome-and-recovery-paths.md) · [Lab 5 →](lab-05-create-a-validated-user-driven-follow-up-flow.md)
