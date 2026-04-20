<sub>MAXWELL COLLINS</sub>

I build production software with AI coding agents. Over ten thousand hours and twenty-plus projects, I have developed a methodology for keeping AI-generated code correct at scale — **Domain-Rules-Driven Development**. I am not an engineer by training. I am a systems architect who specifies what software must do, verifies that it does it, and enforces that it cannot do otherwise.

I am the founder of [**Code-Rescue**](mailto:max@code-rescue.com), a firm that rebuilds legacy software ecosystems using AI-augmented engineering. My publication is at **[maxwellacollins.com](https://maxwellacollins.com)** — the methodology, the rule set that implements it, the enforcement stack, and the engineering field notes.

---

<sub>METHODOLOGY · VERSION 2</sub>

## Domain-Rules-Driven Development

A specification is commonly treated as an input to code generation. That expectation is wrong. A specification treated as an input is read once, referenced imperfectly, and quietly overruled by the code written against it. The gap is not closed by writing better specifications. It is closed by changing what a specification is.

| | |
| --- | --- |
| **Machine-testable rules** | over prose specifications |
| **Mechanical enforcement** | over agent compliance |
| **Source-of-truth authority** | over reconciliation |
| **Monotonic rule sets** | over revisable specifications |

The items on the right are not rejected. They are insufficient for software produced by agents that are not themselves bound by the specification.

→ [Read the full manifesto](https://maxwellacollins.com/manifesto) · [Browse the rule set](https://maxwellacollins.com/rules)

---

<sub>THE TWELVE RULES</sub>

Every domain rule in the methodology satisfies twelve properties. The properties are the methodology.

| | Rule | Tagline |
| :---: | --- | --- |
| **I** | Machine-Testability | Every rule is expressible as an assertion. |
| **II** | Three Layers | Every rule belongs to spec, consistency, or adversarial. |
| **III** | Authority Hierarchy | The rule is truth. The code is not evidence. |
| **IV** | Monotonicity | Rules grow. They do not shrink. |
| **V** | Origin Citation | Every rule names the decision that produced it. |
| **VI** | Incident Capture | Every failure becomes a rule that prevents its recurrence. |
| **VII** | Mechanical Enforcement | Advisory rules decay. Mechanical rules don't. |
| **VIII** | Specification Completeness | Unspecified behavior is a violation. |
| **IX** | Adversarial Coverage | Every external surface has an adversarial rule. |
| **X** | Shared Vocabulary | Cross-cutting concerns have canonical owners. |
| **XI** | Zero Deferral | Known violations are resolved before the domain closes. |
| **XII** | Gate as Specification | The quality gate is the rule set in executable form. |

---

<sub>ANATOMY OF A DOMAIN RULE</sub>

A worked specimen. The following rule is canonical and governs approximately every entity access in a cross-organizationally scoped system.

> **AUTH-5 — Cross-organization access** · `adversarial` · Locked 2026-04-07
>
> Every single-entity fetch MUST include `organizationId = ctx.session.activeOrganizationId` in the SQL WHERE clause. If the query returns zero rows, throw `NOT_FOUND "<Entity> not found"`. Never use `FORBIDDEN "Access denied"` — that error leaks entity existence.

```ts
// Testable assertion — applies to any request crossing an organization boundary,
// regardless of whether the entity exists, is soft-deleted, or belongs to another org:
expect(error.code).toBe("NOT_FOUND");
expect(error.message).toBe("<Entity> not found");
```

**Enforcement.** Write-time hook blocks the violating string. Gate-time static analysis requires the predicate in every WHERE clause touching an org-scoped table. Runtime middleware verifies session active organization before procedure body executes.

**Violation closed.** Three distinct failure cases — entity does not exist, entity was soft-deleted, entity belongs to another organization — collapse into a single indistinguishable response. Enumeration across organizational boundaries ceases to be possible.

→ [See the full rule](https://maxwellacollins.com/rules/auth-5) · [Browse all rules](https://maxwellacollins.com/rules)

---

<sub>RECENT FIELD NOTES</sub>

Engineering field notes on AI-augmented software development. Each is a distilled incident.

| Date | Title |
| --- | --- |
| 2026-04-12 | [The Zero Deferral Policy](https://maxwellacollins.com/writing/zero-deferral-policy) |
| 2026-04-07 | [The Session 35 Breakthrough](https://maxwellacollins.com/writing/session-35-breakthrough) |
| 2026-04-01 | [The 4,800 Fake Tests Weekend](https://maxwellacollins.com/writing/fake-tests-weekend) |
| 2026-03-25 | [Why I Stopped Using Feature Branches](https://maxwellacollins.com/writing/feature-branches) |
| 2026-03-19 | [The Worktree Disaster](https://maxwellacollins.com/writing/worktree-disaster) |

→ [All writing](https://maxwellacollins.com/writing) · [RSS](https://maxwellacollins.com/feed.xml)

---

<sub>NOW</sub>

**Building.** Domain-Rules-Driven Development. Methodology stabilized over three rebuilds and twelve thousand hours of AI-augmented engineering. Next: open-sourcing the enforcement toolkit.

**Working on.** Active rebuild of a four-application legacy ecosystem for a private client. Six months in. Forty-two domain files, ~4,000 rules. Current stage: front-end implementation. Expected ship: summer 2026.

**Available for.** Short-engagement architecture reviews on AI-augmented rebuilds for private clients.

→ [/now](https://maxwellacollins.com/now)

---

<sub>CONTACT</sub>

- Site — [maxwellacollins.com](https://maxwellacollins.com)
- Email — [max@code-rescue.com](mailto:max@code-rescue.com)
- RSS — [maxwellacollins.com/feed.xml](https://maxwellacollins.com/feed.xml)

> [!NOTE]
> This profile publishes in plain prose. No hero banners. No typing animations. No skill grids. No visitor counters. The methodology is the signal.
