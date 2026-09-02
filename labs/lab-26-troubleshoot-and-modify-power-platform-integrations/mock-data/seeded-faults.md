# Seeded Faults — Trainer Setup Notes for Lab 26

These notes are for the **trainer**. Seed all four faults before the LU4 troubleshooting session so that each learner opens a broken environment and has something real to diagnose. Do not share this file with learners until the debrief — `troubleshooting-log.csv` is what they work from.

Seed the faults in the order below. Faults 3 and 4 depend on work the learner completed in Labs 12 and 25.

---

## Fault F-01 — Delegation warning (Application layer)

**What the learner sees:** a blue delegation warning triangle on the browse gallery, and only the first 500 Booking Request rows are searchable.

**How to seed it:**

1. Open the **Booking Request** canvas app from Lab 7 in Power Apps Studio.
2. Select the browse gallery and set its `Items` property to a non-delegable expression:
   ```
   Filter('Booking Requests', Len('Pet Name') > 3)
   ```
3. Confirm the blue warning icon appears on the property and in **App Checker > Delegation**.
4. To make the truncation visible, import enough rows that the table exceeds the delegation limit — duplicate `booking-requests.csv` until the table holds more than 500 rows, or set **Settings > General > Data row limit for non-delegable queries** to 100 so the cut-off shows with the seeded 15 rows.
5. Save and publish, but do **not** clear the warning.

**Expected learner fix:** replace `Len()` with the delegable `StartsWith()`, verify the warning clears and App Checker shows no delegation issue.

---

## Fault F-02 — Failed flow action (Automation layer)

**What the learner sees:** the Booking Approval flow from Lab 14 has a **Failed** run; the *Update a row* action returns HTTP 400 with "A required property is missing".

**How to seed it:**

1. Open the **Booking Approval** flow from Lab 14 in edit mode.
2. In the **If yes** branch, open the **Update a row** action and **clear the Row ID field** — delete the dynamic-content token that references the trigger's Booking Request unique identifier. Leave the Status column mapping intact so only one thing is wrong.
3. Save the flow.
4. Create one Booking Request row in Dataverse and approve it from Teams so the flow reaches the broken action and fails. Verify a red **Failed** run is visible in **Run history** before the session starts.

**Expected learner fix:** re-insert the trigger's row identifier with the dynamic-content picker (never typed), save, then **Resubmit** the failed run and confirm it turns green.

---

## Fault F-03 — Missing security role (Security layer)

**What the learner sees:** the second training account from Lab 12 opens the shared app to an empty gallery and the message "You do not have permission to read records of type Booking Request".

**How to seed it:**

1. In **make.powerapps.com > Apps**, confirm the Booking Request app is still shared with the second training account at **Can use** (this was done in Lab 12 — do not remove the share).
2. In the **Power Platform admin centre > Environments > Dev One > Settings > Users + permissions > Users**, open that second account.
3. **Remove every security role except Basic User.** In particular remove any custom role granting Read on the Booking Request table.
4. Sign in as that account in a private browser window and confirm the empty gallery plus the permission error appear. Capture nothing — the learner must capture the evidence themselves.

**Expected learner fix:** assign the **Kennel Supervisor** (or equivalent) security role with Read/Write on Booking Request, then refresh the browser and confirm the gallery populates.

---

## Fault F-04 — Broken connection reference (Deployment layer)

**What the learner sees:** in the **Test** environment the imported managed solution shows the Booking Approval flow turned **off** and marked "Connection not configured".

**How to seed it:**

1. Complete the Lab 25 export/import into the **Test** environment.
2. During the import, **skip** the step that binds the Dataverse connection reference — click through the connections page without selecting a connection. If your tenant forces a selection, complete the import and then delete the Dataverse connection in Test afterwards.
3. Confirm the flow appears in **Solutions > Contoso Real Estate > Objects** with the connection reference showing no connection, and that the flow is switched off.

**Expected learner fix:** create a Dataverse connection in the Test environment, edit the connection reference to point at it, turn the flow on, and run a smoke test that creates one row.

---

## Debrief pointers

- Insist that learners name the **layer** before they name the fix. Most wrong diagnoses come from jumping to the automation layer when the symptom is really security.
- F-01 and F-03 both look like "no data", but the evidence is different: F-01 shows a blue warning at design time; F-03 shows an HTTP 403 at runtime for one user only.
- F-02 and F-04 both stop a flow, but F-02 fails at run time on one action while F-04 never starts because the flow is off.
- Every learner's `troubleshooting-log.csv` should have all four rows completed with evidence quoted from the product, not paraphrased.
