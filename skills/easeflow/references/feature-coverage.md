# Feature coverage

EaseFlow changes **how** a product is presented and used, never **what** it can do. Every feature that exists today must have a clear home in the new design. This file explains how to find every feature, organise them around what users are trying to get done, and prove nothing was lost.

## 1. Build the feature inventory

Sweep **every** source below. Whatever the product can do, if a user can trigger it, see it or configure it, it's a feature.

| Source | What to collect |
|---|---|
| Routes / screens / views | Every page, modal, drawer, tab, wizard step |
| Navigation | Every sidebar, menu, tab bar, context menu, command palette entry |
| Actions | Every button, link, bulk action, keyboard shortcut, drag-and-drop |
| Forms and settings | Every form and every setting, including per-item and per-account settings |
| Data objects | Every model/entity the user creates, views or edits (Patient, Invoice, Project…) |
| Roles and permissions | What each role can see and do |
| Integrations | Connections to other services, imports, exports, webhooks, API keys |
| Notifications | Emails, push, in-app alerts, digests the user receives or configures |
| Background work with visible results | Scheduled jobs, reports, syncs, automations |
| Billing and account | Plans, payment, invoices, team members, security, deletion |
| API endpoints the UI calls | Cross-check: an endpoint with no matching feature means a feature was missed |

Give each feature a row in `easeflow-report/feature-ledger.md`:

| ID | Feature (product's name) | Plain name | What it does for the user | Object | Who uses it | Evidence |
|---|---|---|---|---|---|---|
| F001 | Bulk reschedule | Move many appointments at once | Shifts a group of appointments to a new day | Appointment | Front desk, daily | `src/routes/schedule/bulk.tsx:12` |

### Big systems

When the product has more than about 15 screens or 60 features, split the sweep **by module** (by top-level folder, route group or nav section) and run one subagent per module in parallel. Each returns its rows in the same format. Merge, de-duplicate, and number them.

### Completeness check

Before moving on, reconcile counts and record them at the top of the ledger:

- routes/screens found vs. screens referenced in the ledger
- UI-called API endpoints vs. features that use them
- settings found vs. settings in the ledger
- nav items found vs. nav items in the ledger

Every gap is either added as a feature or explained (for example, "internal health-check endpoint, not user-facing"). Don't continue with unexplained gaps.

## 2. Find the objects

List the product's **core objects**: the nouns users think in (Patient, Appointment, Invoice; Product, Order, Customer; Course, Lesson, Student). Usually 3–8. Note how they relate ("a Patient has many Appointments"). This is the object-oriented UX approach: objects become the backbone of simple navigation, because users understand nouns from their own world better than system functions.

## 3. Group features into jobs

A **job** is something a user is trying to get done, in their words, as a verb phrase: "Book a patient in", "Get paid for a visit", "See how this month went", "Change my opening hours". Group every feature under the job it serves. One feature can support several jobs; record its primary one.

## 4. Tier the jobs

Products follow a "long neck" pattern: a handful of tasks make up most of what people come to do. Tier jobs into:

| Tier | What it means | Typical count | How it's presented |
|---|---|---|---|
| **Core** | What most users do most often, and what they pay for | 3–7 | Front and centre; one click from home |
| **Regular** | Used now and then, by many users | Varies | Reachable from the object or job it belongs to |
| **Advanced** | Used rarely, or by experts, admins or power users | Varies | Behind "More options", an Advanced section, an admin area, or Advanced mode |

Base tiers on evidence, in this order: real usage data if the project has analytics; the pricing page and marketing (what's sold); onboarding and docs (what's emphasised); how deep the code puts it; and judgement. Record the reason for each tier in the ledger.

## 5. Give every feature a home

After the redesign (SKILL.md Phase 5), complete the ledger with each feature's new location and disclosure level:

| Disclosure level | Meaning |
|---|---|
| **Automatic** | No longer needs the user. A smart default or automation does it, and it can still be changed (say where). |
| **Visible** | On the screen where its job happens. |
| **In context** | Appears when relevant (for example, "Refund" shows on a paid invoice). |
| **More options** | One click away on the same screen. |
| **Advanced** | In the Advanced section for that area, or in Advanced mode. |
| **Admin** | In the admin/owner area, shown only to that role. |
| **Merged** | Combined with another feature (name it). Both capabilities must still work. |
| **Needs your decision** | EaseFlow suggests removing it, with a reason. The user decides. It is never removed silently. |

| ID | Plain name | Job | Tier | New location | Disclosure | Clicks from home | Reason |
|---|---|---|---|---|---|---|---|

## 6. Coverage gate

The redesign isn't finished until:

- **100% of features** have a new location and disclosure level.
- **0 features** are lost. "Needs your decision" counts as kept until the user decides.
- **Every core job** can be completed in the proposed flow.
- **Every Advanced feature** is reachable within **3 clicks from home**, from a place someone would think to look (the object or job it belongs to, or the Advanced section).

Report the coverage numbers in the report and showcase.
