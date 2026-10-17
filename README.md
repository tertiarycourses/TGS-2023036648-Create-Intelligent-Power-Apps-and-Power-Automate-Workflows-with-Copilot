# Create Intelligent Power Apps and Power Automate Workflows with Copilot

[![WSQ](https://img.shields.io/badge/WSQ-TGS--2023036648-1F6FEB?style=for-the-badge)](https://www.tertiarycourses.com.sg/wsq-create-intelligent-power-apps-and-power-automate-workflows-with-copilot.html)
[![Duration](https://img.shields.io/badge/Duration-4%20days%20%C2%B7%2032%20hours-10B981?style=for-the-badge)](#lesson-plan)
[![Labs](https://img.shields.io/badge/Hands--on%20Labs-26-7C3AED?style=for-the-badge)](labs/README.md)
[![Funding](https://img.shields.io/badge/SkillsFuture-Up%20to%2070%25%20funded-F59E0B?style=for-the-badge)](#funding)

Official courseware for the SkillsFuture WSQ course **“Create Intelligent Power Apps and Power
Automate Workflows with Copilot”** (TGS-2023036648), delivered by
[Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg) (UEN 201200696W).

Four days of hands-on Microsoft Power Platform: build canvas and model-driven apps with
**Power Apps**, automate business processes with **Power Automate**, ground and govern agents in the
new **Copilot Studio** agent designer, and model data in **Microsoft Dataverse** — using **Copilot**
throughout as an accelerator.

> **[📋 Register for this course →](https://www.tertiarycourses.com.sg/wsq-create-intelligent-power-apps-and-power-automate-workflows-with-copilot.html)**

---

## Learning outcomes

By the end of the course you will be able to:

| | Outcome |
|---|---|
| **LO1** | Identify opportunities for creating connections in Microsoft Power Platform and perform feasibility scans. |
| **LO2** | Utilise Power Apps to integrate data and functions across programs and API-level integration. |
| **LO3** | Execute tests in Power Automate to verify the connections between disparate programs and their functioning across platforms. |
| **LO4** | Resolve technical issues in Power Platform and implement modifications to Power Platform middleware. |

Aligned to Skills Framework TSC **Applications Integration** (`ICT-DIT-3003-1.1`), abilities A1–A8 and
knowledge K1–K5.

---

## Course structure

| Learning Unit | Topics | Labs | Day |
|---|---|---|---|
| **LU1** — Get Started with Copilot for Microsoft Power Platform | 1–4 | [1–4](labs/README.md) | 1 |
| **LU2** — Create and Manage Canvas Apps with Power Apps | 5–10 | [5–12](labs/README.md) | 1–2 |
| **LU3** — Automated Processes with Power Automate and Copilot Studio Agents | 11–14 | [13–20](labs/README.md) | 2–3 |
| **LU4** — Model-Driven Apps with Power Apps and Dataverse | 15–19 | [21–26](labs/README.md) | 4 |

### What you build

```
LU1  Copilot           →  feasibility scan · Copilot-built app · Copilot-built flow · Power Pages site
LU2  Canvas apps       →  Excel app · Dataverse model · gallery + forms · SharePoint + Patch
                          PCF code component · published, shared, versioned app
LU3  Automation        →  3 flows · approval with a human in the loop · button + scheduled flows
                          trigger filters · grounded agent · agent tool · structured output · multi-agent
LU4  Model-driven      →  Dataverse tables · model-driven app · forms & views · charts & dashboards
                          managed solution · troubleshooting by layer
```

---

## Hands-on labs

**26 labs, each in its own folder with its own mock data.** Every lab has a `README.md` with the full
click-by-click procedure, a verification step and three troubleshooting fixes, plus a `mock-data/`
folder so the lab is runnable without hunting for sample data.

> **[📂 Browse all 26 labs →](labs/README.md)**

```
labs/
├── README.md                                   ← index of all 26 labs
├── lab-01-validate-the-lab-environment-and-explore-copilot/
│   ├── README.md
│   └── mock-data/connector-scan.csv
├── lab-06-build-the-dataverse-data-model/
│   ├── README.md
│   └── mock-data/{booking-requests.csv, kennels.csv}
├── lab-11-extend-the-app-with-a-code-component-pcf/
│   ├── README.md
│   └── mock-data/RatingControl/{ControlManifest.Input.xml, index.ts, RatingControl.css}
├── lab-17-build-your-first-copilot-studio-agent/
│   ├── README.md
│   └── mock-data/{hr-policies/*.md, probe-questions.csv}
└── … 22 more
```

The mock data is internally consistent — foreign keys resolve, and Lab 24's expected chart values are
computed from Lab 21's property data, so learners can self-verify.

---

## Courseware

| Artifact | Format | Notes |
|---|---|---|
| **Trainer Slides** | `courseware/Create Intelligent Power Apps and Power Automate Workflows with Copilot-v12.0.pptx` + PDF | 204 slides, all-white house style, concept-first |
| **Lesson Plan** | `courseware/LP-Create Intelligent Power Apps and Power Automate Workflows with Copilot.docx` + PDF | 4 days × 8 training hours, 9:30am–6:30pm, with slide references |
| **Learner Guide** | `courseware/LG-Create Intelligent Power Apps and Power Automate Workflows with Copilot.docx` + PDF | Full step-by-step for all 26 labs, with UI walkthroughs |
| **Learner Guide (Markdown)** | `LG-*.md` | Same content, readable on GitHub |

**The slide deck deliberately contains no step-by-step procedures.** Slides teach concepts,
comparisons, decision maps and the product interfaces; the click-by-click steps live in the Learner
Guide and the lab folders, so the two can never drift apart.

The deck includes 11 generated Power Platform UI walkthroughs — Power Apps Studio, the Power Automate
designer, run history, the new Copilot Studio agent designer, the Agent node with structured output,
Teams approvals, the Dataverse table designer, a model-driven app, the delegation warning and the PCF
harness — each with a numbered key.

---

## Lesson plan

| Day | Theme |
|---|---|
| **1** | Copilot for Power Platform & first canvas apps |
| **2** | Canvas apps: UI, external data, forms & publishing |
| **3** | Power Automate flows & Copilot Studio agents |
| **4** | Model-driven apps, Dataverse, solutions & assessment |

Each day runs **9:30am–6:30pm** — 8 training hours after a 1-hour lunch, with tea breaks counted
within. Assessment is on Day 4 from 4:00pm.

---

## Assessment

- **Written Assessment (WA)** — 5 open-ended short-answer questions, 1 hour, open book.
- **Practical Performance (PP)** — 4 hands-on build tasks, 90 minutes, open book.

Both are open book: slides, Learner Guide and lab folders are permitted. A minimum of **75%
attendance** is required to be eligible for assessment and funding.

> Assessment papers and answer keys are **confidential** and are not published in this repository.

---

## Prerequisites

- A Microsoft 365 account with a Power Platform licence (or a Developer Plan environment).
- One environment with a **Dataverse** database provisioned — every lab uses the same one.
- A modern browser. For Lab 11 only: Node.js LTS, the .NET SDK and the Power Platform CLI (`pac`).

> **The single most important setting:** confirm the environment picker shows the *same* environment
> in every portal before you build. Apps, flows, tables and agents can only see each other inside one
> environment.

---

## Funding

| Learner | Subsidy | Nett fee |
|---|---|---|
| Full fee | — | $1,744 (incl. GST) |
| Singaporean / PR, age 21+ | 50% | **$944** |
| Singaporean, age 40+ / MCES / SME | 70% | **$624** |

Also claimable via **SkillsFuture Credit**, **SFEC**, **UTAP**, **PSEA** and **Absentee Payroll**.

Eligibility and terms apply; see the [course page](https://www.tertiarycourses.com.sg/wsq-create-intelligent-power-apps-and-power-automate-workflows-with-copilot.html) for current fees and funding.

---

## Reference material

Labs are grounded in Microsoft's official learning content:

- [PL-7001 — Create and manage canvas apps with Power Apps](https://github.com/MicrosoftLearning/PL-7001-Create-and-manage-canvas-apps-with-Power-Apps)
- [PL-7002 — Create and manage automated processes by using Power Automate](https://github.com/MicrosoftLearning/PL-7002-Create-and-Manage-Automated-Processes-by-using-Power-Automate)
- [microsoft/PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) — PCF and Dataverse samples
- [PL-400 Lab 07 — Power Apps Component Framework](https://microsoftlearning.github.io/PL-400_Microsoft-Power-Platform-Developer/Instructions/Labs/LAB%5BPL-400%5D_Lab07_PCF.html)

---

## About

**Tertiary Infotech Academy Pte Ltd** · UEN 201200696W · Approved Training Organisation
Microsoft Learning Partner (Org ID 5238476)

📧 [enquiry@tertiaryinfotech.com](mailto:enquiry@tertiaryinfotech.com) · ☎ +65 6100 0613 ·
🌐 [tertiarycourses.com.sg](https://www.tertiarycourses.com.sg) ·
🎓 [LMS](https://lms-tms.tertiaryinfotech.com)

© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.
