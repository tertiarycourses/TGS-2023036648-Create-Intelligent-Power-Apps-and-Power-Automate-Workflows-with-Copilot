# Lab 11 — Extend the App with a Code Component (PCF)

| | |
|---|---|
| **Learning Unit** | LU2 — Create and Manage Canvas Apps with Power Apps |
| **Course** | Create Intelligent Power Apps and Power Automate Workflows with Copilot (TGS-2023036648) |
| **Objective** | A4/A8 — Support API-level integration by building a custom control and modifying the platform's UI layer. |
| **Duration** | 75 minutes |
| **Services** | Power Platform CLI, Node.js, TypeScript, Power Apps Component Framework, Dataverse solutions |

## What you will build

A packaged PCF code component imported as a solution and used inside the canvas app.

## Scenario

Use the Power Apps Component Framework to build, test and package a custom code component, then import it into the environment and place it on a canvas app screen.

## Prerequisites

- Node.js LTS, the .NET SDK and the Power Platform CLI (`pac`) installed locally. Verify with `pac --version` in step 1.
- **Lab 01** completed — you import the solution into the same environment.
- **Lab 07** completed — the canvas app you insert the finished component into.
- Local admin rights to run `npm install` and `dotnet build`.

## Mock data

All files live in this lab's `mock-data/` folder.

| File | What it contains |
|---|---|
| `RatingControl/ControlManifest.Input.xml` | A complete field-control manifest for TertiaryInfotech.RatingControl. Declares the bound property ratingValue of type Whole.None plus an optional maxRating input. Copy over the manifest that `pac pcf init` scaffolds. |
| `RatingControl/index.ts` | A working StandardControl<IInputs, IOutputs> implementation with init, updateView, getOutputs and destroy. Renders a 1-5 star rating, calls notifyOutputChanged on click, respects the disabled and read-only state, and removes its listeners in destroy. |
| `RatingControl/RatingControl.css` | The stylesheet referenced by the manifest's <css> resource. Save it to css/RatingControl.css inside the scaffolded project. |

## Steps

1. Verify the toolchain is installed — Node.js LTS, .NET SDK and the Power Platform CLI.

   ```bash
   pac --version
   ```

2. Create a folder for the component and scaffold a field-type control.

   ```bash
   mkdir RatingControl && cd RatingControl && pac pcf init --namespace TertiaryInfotech --name RatingControl --template field
   ```

3. Install the npm dependencies the template declares.

   ```bash
   npm install
   ```

4. Open ControlManifest.Input.xml and declare a bound property named ratingValue of type Whole.None, then edit index.ts to render the control.

5. Run the local test harness and interact with the control in the browser.

   ```bash
   npm start watch
   ```

6. Create a solution project alongside the component and add a reference to it.

   ```bash
   pac solution init --publisher-name TertiaryInfotech --publisher-prefix tic
   ```

7. Add the component reference and build the managed solution package.

   ```bash
   pac solution add-reference --path ../RatingControl && dotnet build
   ```

8. Import the generated solution zip from bin/Debug into your environment via make.powerapps.com > Solutions > Import.

9. In the canvas app enable code components in Settings > General, then Insert > Get more components > Code and add RatingControl to a screen.

## Verify

npm start watch renders the control in the harness, the solution imports without error, and the component can be inserted onto a canvas app screen.

## Troubleshooting

**Problem — `pac --version` returns "command not found".**

*Fix:* The Power Platform CLI is not on the PATH. Install it with `dotnet tool install --global Microsoft.PowerApps.CLI.Tool`, then open a **new** terminal — an existing shell does not pick up the new PATH entry. On Windows the Visual Studio Code Power Platform Tools extension installs a separate copy that only works inside its own terminal.

**Problem — `npm start watch` opens the harness but the control area is blank, or the console shows a TypeScript error about `IInputs`.**

*Fix:* `generated/ManifestTypes.d.ts` is regenerated from the manifest at build time. If you edited `ControlManifest.Input.xml` while the watcher was running, stop it, run `npm run build` once to regenerate the types, then `npm start watch` again. A property name mismatch between the manifest's `ratingValue` and `getOutputs()` produces exactly this error.

**Problem — The solution imports but **Get more components > Code** is empty in the canvas app.**

*Fix:* Two separate switches. First, in the app: **Settings > General > Code components** must be on. Second, in the environment: **Power Platform admin centre > Environments > Settings > Product > Features > Power Apps component framework for canvas apps** must be on. Republish the app after enabling either one.

---

**Next:** [Lab 12 — Publish, Share and Maintain the App](../lab-12-publish-share-and-maintain-the-app/README.md)
