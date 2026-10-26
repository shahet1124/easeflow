# Prototype guide

`prototype.html` is EaseFlow's main deliverable: the customer's **own product**, in its **own look**, but with EaseFlow's simplified flow. When the founder opens it, they should think "that's our app, but simple", not "that's a mockup".

## 1. Capture the theme

Look for the product's design in this order, and stop once you have each value:

1. **Design tokens:** CSS custom properties (`:root { --primary: … }`), `tailwind.config.*` (`theme.extend.colors`, `fontFamily`, `borderRadius`), theme files (`theme.ts`, MUI `createTheme`, Chakra `extendTheme`, shadcn `globals.css`), SCSS variables.
2. **Components:** the product's Button, Input, Card, Modal and Nav components. Note radius, padding, shadow, border, hover/focus styles, and the button height.
3. **Fonts:** Google Fonts `<link>` tags, `@font-face`, `next/font` calls.
4. **Logo and product name:** `public/`, `assets/`, the header component. Prefer an SVG and inline it.
5. **Voice:** how the product's existing copy speaks (formal, friendly, playful). Keep the voice, but apply R10 and R11 (plain, literal words).
6. **Live mode only:** in the browser, read `getComputedStyle` for `body`, the primary button, an input, a card and the nav. Take a screenshot of the real dashboard and sign-up screens to compare against later.

Save the result as `easeflow-report/theme.json`:

```json
{
  "productName": "Reachly",
  "logo": "<svg …>…</svg>",
  "font": { "family": "Inter, system-ui, sans-serif", "importUrl": "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap", "baseSize": 16 },
  "colors": {
    "primary": "#4f46e5", "onPrimary": "#ffffff",
    "background": "#f8fafc", "surface": "#ffffff",
    "text": "#0f172a", "muted": "#64748b", "border": "#e2e8f0",
    "success": "#16a34a", "danger": "#dc2626"
  },
  "radius": { "control": "8px", "card": "12px" },
  "shadow": "0 1px 3px rgba(15,23,42,.08)",
  "button": { "height": "44px", "weight": 600, "textTransform": "none" },
  "dark": null,
  "voice": "Friendly, second person, short sentences",
  "sources": ["tailwind.config.ts:12", "src/components/ui/button.tsx:8", "app/layout.tsx:5"]
}
```

Rules:
- **Every value has a source.** List where it came from in `sources`. Don't invent a brand. If something isn't found, use a neutral default and say so under "Coverage and limits" in the report.
- **Accessibility wins over brand.** If the brand's text or button colours fall below 4.5:1 contrast, or the base text is under 16px, keep the hue, adjust lightness or size, and note it as an "accessibility adjustment" (R17).
- If the product has a dark theme, capture it under `dark` and support it in the prototype.

## 2. Build the prototype

Start from `assets/prototype-skeleton.html`. It already handles screens, routing, progress, persistence, and the presenter bar. Copy it to `easeflow-report/prototype.html`, then:

1. **Apply the theme:** fill the `:root` variables at the top of the skeleton from `theme.json`, add the font `<link>` if there's an `importUrl`, and put the logo SVG in the header.
2. **Write the screens:** one `<section class="screen" data-screen="…">` per step of the proposed flow, in order, using the **exact copy** from the report's onboarding table and proposed flow.
3. **Match their components:** style buttons, inputs and cards like the product's own (radius, weight, shadow), using the theme variables. Recreate the product's real header/nav look, with only the simplified nav items (R19).

### Screens to include

| Screen | Must show |
|---|---|
| Sign-up | Only the fields R3 allows (usually email + password, or one-click sign-in). |
| Onboarding steps | 3–5 screens, "Step X of Y", one question each, one primary button, "Skip setup" (R7–R9). |
| Commitment screens | Plain one-sentence reason, preview, and a way back for payment, permissions or sending (R14–R16). |
| Core win | The moment of value, with a clear success confirmation and what happens next (R12). |
| Home after setup | The calm everyday screen: at most 5 nav items, one obvious next action, no empty charts (R1, R19, R20). |
| Advanced | Where every moved feature now lives, matching the "Where every feature went" table, so Alex can find them (R5). |
| Returning user | A "Continue where you left off" banner shown when progress exists (R8). The skeleton handles this. |

### Content rules

- **Realistic sample data for this product's domain**, matching the persona walkthroughs (Harold's dental clinics, Ramesh's shop). Never lorem ipsum.
- **Inputs are real and editable**, pre-filled with example values where the flow suggests a default.
- **Show one kind error** on a likely field (for example, an email format), next to the field, in plain words (R13).
- **Simulate integrations honestly.** "Connect my email" goes to a success state with a small note "(simulated in prototype)". No real network calls.
- **No external scripts.** Fonts may load from Google Fonts. Everything else is inline. It must work when opened as a local file.

### Responsiveness and access

- Works at **375px** wide and at **200% zoom** with no horizontal scroll (R18).
- Tap targets at least **44px**, base text at least **16px**, visible focus outlines, every input has a `<label>` (R17).
- Uses the product's dark theme under `prefers-color-scheme: dark` only if the product has one.

## 3. Check before handing it over

Open `prototype.html` in the browser and check every item:

- [ ] Click through from sign-up to the core win using only the primary buttons.
- [ ] "Skip setup" lands on the home screen, and Advanced is reachable from there.
- [ ] Back (in-page and browser) works on every screen.
- [ ] Refresh mid-onboarding shows "Continue where you left off".
- [ ] No horizontal scroll at 375px wide.
- [ ] No console errors.
- [ ] Live mode: compare a screenshot of the prototype's home screen with the real product's. Colours, font, logo and button style should clearly match.
- [ ] Walk it once as Harold and once as the Literal Follower. Every screen has one obvious action, and every label says what it does.

If a check fails, fix it before delivering.
