import { IInputs, IOutputs } from "./generated/ManifestTypes";

/**
 * TertiaryInfotech.RatingControl
 *
 * A bound field control that renders a 1..N star rating (N defaults to 5).
 * Clicking a star sets the value and raises notifyOutputChanged() so the
 * framework pulls the new value through getOutputs().
 */
export class RatingControl
    implements ComponentFramework.StandardControl<IInputs, IOutputs> {

    // Assigned in init(), which the framework always calls before any other
    // member. The ! tells TypeScript's strict mode that this is guaranteed.
    private _container!: HTMLDivElement;
    private _context!: ComponentFramework.Context<IInputs>;
    private _notifyOutputChanged!: () => void;

    /** Current rating held by the control. 0 means "not rated". */
    private _value = 0;

    /** Number of stars to render. */
    private _maxRating = 5;

    /** The star elements, index 0 == star 1. */
    private _stars: HTMLButtonElement[] = [];

    /** Bound once so the same reference can be removed in destroy(). */
    private readonly _onStarClick = (event: Event): void => {
        const target = event.currentTarget as HTMLButtonElement;
        const clicked = Number(target.getAttribute("data-rating"));

        // Clicking the current rating again clears it back to 0.
        this._value = this._value === clicked ? 0 : clicked;

        this.renderStars();
        this._notifyOutputChanged();
    };

    constructor() {
        // Intentionally empty - the framework calls init().
    }

    /**
     * Called once when the control is created.
     */
    public init(
        context: ComponentFramework.Context<IInputs>,
        notifyOutputChanged: () => void,
        state: ComponentFramework.Dictionary,
        container: HTMLDivElement
    ): void {
        this._context = context;
        this._notifyOutputChanged = notifyOutputChanged;
        this._container = container;

        this._container.classList.add("tic-rating");

        const raw = context.parameters.maxRating?.raw;
        if (raw !== null && raw !== undefined && raw > 0) {
            this._maxRating = raw;
        }

        this.buildStars();
        this.applyValueFromContext(context);
        this.renderStars();
    }

    /**
     * Called by the framework whenever any bound value, layout size or
     * mode (disabled / visible) changes.
     */
    public updateView(context: ComponentFramework.Context<IInputs>): void {
        this._context = context;
        this.applyValueFromContext(context);
        this.renderStars();
    }

    /**
     * Return the control's value to the framework. The property names must
     * match the bound properties declared in ControlManifest.Input.xml.
     */
    public getOutputs(): IOutputs {
        return {
            ratingValue: this._value
        };
    }

    /**
     * Called when the control is removed from the DOM. Detach every listener
     * added in buildStars() so nothing leaks.
     */
    public destroy(): void {
        for (const star of this._stars) {
            star.removeEventListener("click", this._onStarClick);
        }
        this._stars = [];
        this._container.innerHTML = "";
    }

    // ------------------------------------------------------------ internals

    private buildStars(): void {
        for (let i = 1; i <= this._maxRating; i++) {
            const star = document.createElement("button");
            star.type = "button";
            star.className = "tic-rating__star";
            star.setAttribute("data-rating", String(i));
            star.setAttribute("aria-label", `Rate ${i} of ${this._maxRating}`);
            star.innerText = "☆"; // hollow star; filled in renderStars()
            star.addEventListener("click", this._onStarClick);

            this._stars.push(star);
            this._container.appendChild(star);
        }
    }

    private applyValueFromContext(context: ComponentFramework.Context<IInputs>): void {
        const raw = context.parameters.ratingValue.raw;
        this._value = raw === null || raw === undefined ? 0 : raw;

        if (this._value < 0) {
            this._value = 0;
        }
        if (this._value > this._maxRating) {
            this._value = this._maxRating;
        }
    }

    private renderStars(): void {
        const readOnly =
            this._context.mode.isControlDisabled ||
            this._context.parameters.ratingValue.security?.editable === false;

        this._stars.forEach((star, index) => {
            const filled = index < this._value;
            star.innerText = filled ? "★" : "☆";
            star.classList.toggle("tic-rating__star--on", filled);
            star.disabled = readOnly;
            star.setAttribute("aria-pressed", String(filled));
        });

        this._container.setAttribute("role", "radiogroup");
        this._container.setAttribute(
            "aria-label",
            `Rating ${this._value} of ${this._maxRating}`
        );
    }
}
