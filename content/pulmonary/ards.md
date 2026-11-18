---
title: ARDS
emoji: "🫧"
group: Respiratory failure
order: 2
featured: true
summary: Berlin and 2023 global criteria, the "baby lung", lung-protective ventilation, proning, and real ICU tips from bedside to ECMO.
tags: [ARDS, Berlin, lung-protective ventilation, prone, PEEP, ECMO]
reviewed: 2026-11-18
sources: Berlin definition (JAMA 2012) · 2023 global ARDS definition (AJRCCM 2024) · 2024 ATS ARDS guideline · ARDSNet · PROSEVA
---

:::bottom
- **Vt 6 mL/kg predicted body weight** (from **measured height**), **plateau ≤30**, **driving pressure ≤15**.
- **PEEP by the PEEP/FiO₂ table**; moderate–severe ARDS → **higher PEEP**. No long recruitment maneuvers.
- **P/F <150 on FiO₂ ≥0.6 → prone early, ≥16 h/day.** It is the one rescue therapy with a clear mortality benefit.
- Targets: **SpO₂ 88–95%** (PaO₂ 55–80), **pH ≥7.20** — accept a high PaCO₂.
- **Treat the cause** (sepsis, pneumonia, aspiration, pancreatitis). Look for mimics.
- After shock resolves → **conservative fluids**. Consider **corticosteroids** early.
- Refractory hypoxemia → **call an ECMO center early** (before the patient is too sick to move).
:::

## 🧠 Pathophysiology in 60 seconds

- **Injury** — direct (pneumonia, aspiration) or indirect (sepsis) — damages the **alveolar epithelium** and **capillary endothelium**.
- The barrier leaks → **protein-rich edema**, neutrophils and **hyaline membranes** fill the alveoli. **Surfactant** is lost → alveoli collapse.
- Three results:
    - **Shunt** → hypoxemia that **does not fix with O₂** alone (needs PEEP to re-open alveoli).
    - **Low compliance** → high pressures for small breaths.
    - **Dead space** → high minute ventilation, CO₂ retention.
- **Phases:** exudative (days 0–7) → proliferative (days 7–21) → fibrotic (some patients; prolonged ventilation).

{{fig:ards-alveolus}}

:::analogy
Imagine a sponge where most holes are full of glue. Only a small part still takes air — the "**baby lung**." Push a normal-sized breath into it and it over-stretches and tears.
:::

{{fig:baby-lung}}

### Ventilator-induced lung injury (VILI)

| Type | Cause | Prevention |
|---|---|---|
| **Volutrauma** | Too large a breath for the baby lung | Vt 6 mL/kg PBW |
| **Barotrauma** | High pressure → pneumothorax | Plateau ≤30 |
| **Atelectrauma** | Alveoli open and close every breath | Enough PEEP |
| **Biotrauma** | Stretch releases cytokines → multi-organ failure | All of the above |

## 🔎 Diagnosis — Berlin criteria

| Criterion | Berlin definition (2012) |
|---|---|
| **Timing** | Within **1 week** of a known insult, or new/worse respiratory symptoms |
| **Imaging** | **Bilateral opacities** on CXR/CT, not fully explained by effusion, collapse or nodules |
| **Origin** | Respiratory failure **not fully explained by heart failure or fluid overload** (echo if no risk factor) |
| **Oxygenation** | P/F ratio with **PEEP or CPAP ≥5 cmH₂O** |

| Severity | PaO₂/FiO₂ | Mortality (approx.) |
|---|---|---|
| **Mild** | 201–300 | ~27% |
| **Moderate** | 101–200 | ~32% |
| **Severe** | **≤100** | ~45% |

:::new 2023 global definition — what it adds
- **Non-intubated ARDS:** P/F ≤300 or **SpO₂/FiO₂ ≤315** (SpO₂ ≤97%) on **HFNC ≥30 L/min** or NIV/CPAP ≥5.
- **SpO₂/FiO₂** accepted in place of an ABG (only when SpO₂ ≤97%).
- **Lung ultrasound** accepted for bilateral involvement (trained operator).
- **Resource-limited settings:** PEEP and flow requirements dropped.
- Intubated severity grades unchanged (mild/moderate/severe as Berlin).
:::

### Causes

| Direct (lung) | Indirect (systemic) |
|---|---|
| **Pneumonia** (bacterial, viral incl. influenza/COVID) | **Sepsis** (most common) |
| **Aspiration** of gastric contents | Pancreatitis |
| Inhalation injury, near-drowning | Major trauma, burns |
| Pulmonary contusion | **TRALI**, massive transfusion |
| Vaping (EVALI) | Drugs (overdose, chemotherapy) |

:::warn ARDS mimics — look before you label
- **Cardiogenic edema** (echo, BNP) · **diffuse alveolar hemorrhage** (falling Hb, BAL bloody) · **acute eosinophilic pneumonia** (BAL eos >25%, steroid-responsive) · **acute interstitial pneumonia / ILD flare** · **cryptogenic organizing pneumonia** · **PJP** in the immunocompromised · drug-induced pneumonitis (amiodarone, checkpoint inhibitors).
- No clear risk factor → **bronchoscopy with BAL** often changes therapy.
:::

## 🧪 Workup

- **ABG** (P/F), CXR, **CT chest** if the cause is unclear (and safe to travel).
- **Echo**: LV function, RV failure (acute cor pulmonale in ~20% of severe ARDS), filling pressures.
- **Infection:** blood + respiratory cultures, viral PCR, *Legionella*/pneumococcal urine antigen, procalcitonin.
- Lipase, CBC, lactate, BNP; BAL if no obvious cause.
- **Every day:** P/F, plateau pressure, driving pressure, fluid balance.

## 💊 Management

:::flow
Q: Intubated with ARDS? Set the vent lung-protective from minute one.
Y: AC/VC · Vt 6 mL/kg PBW · RR up to 35 to keep pH ≥7.20 · PEEP/FiO₂ table · SpO₂ 88–95%
Q: Plateau >30 or driving pressure >15?
Y: Lower Vt to 5 → 4 mL/kg PBW. Accept higher PaCO₂.
Q: P/F <150 on FiO₂ ≥0.6 and PEEP ≥5?
Y: Prone ≥16 h/day. Consider neuromuscular blockade (cisatracurium) if dyssynchronous, 24–48 h.
Q: Still P/F <80 for >6 h, P/F <50 for >3 h, or pH <7.25 with PaCO₂ ≥60 for >6 h?
Y: VV-ECMO referral (EOLIA criteria). Inhaled NO or epoprostenol only as a bridge.
:::

:::tabs
=== Vent settings
**Predicted body weight (use measured height):**
- Men: 50 + 2.3 × (height in inches − 60)
- Women: 45.5 + 2.3 × (height in inches − 60)

| Parameter | Target |
|---|---|
| Tidal volume | **6 mL/kg PBW** (range 4–8) |
| Plateau pressure | **≤30 cmH₂O** (inspiratory hold 0.5 s) |
| Driving pressure (Pplat − PEEP) | **≤15** |
| RR | Up to 35 |
| pH | ≥7.20–7.25 (permissive hypercapnia) |
| SpO₂ / PaO₂ | 88–95% / 55–80 mmHg |

**ARDSNet lower PEEP/FiO₂ table:**

| FiO₂ | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|---|---|---|---|---|---|---|---|---|
| PEEP | 5 | 5–8 | 8–10 | 10 | 10–14 | 14 | 14–18 | 18–24 |

Moderate–severe ARDS: the **higher PEEP/FiO₂ table** is suggested (2024 ATS) — check that plateau and driving pressure stay in range and BP holds.
=== Proning
- **Who:** P/F <150, FiO₂ ≥0.6, PEEP ≥5 — after 12–24 h of stabilization. Earlier is better.
- **How long:** **≥16 h/day**; continue daily until P/F ≥150 with PEEP ≤10, FiO₂ ≤0.6 for ≥4 h supine.
- **Benefit:** 28-day mortality 16% vs 33% (PROSEVA).
- **Team of 5:** airway person at the head leads. Secure ETT, lines, chest tubes. Pre-oxygenate 100%.
- **Prevent harm:** eye care (lubricant, taping), pressure-point padding (face, knees, chest), arms in "swimmer" position, tube feeds can continue (reverse Trendelenburg).
- Relative contraindications: unstable spine, open abdomen/chest, raised ICP, late pregnancy, massive hemoptysis.
=== Drugs & fluids
- **Corticosteroids** (2024 ATS, conditional): early moderate–severe ARDS. Options: **dexamethasone 20 mg IV daily ×5 d → 10 mg ×5 d** (DEXA-ARDS) or methylprednisolone ~1 mg/kg/day with taper. Avoid starting late (>14 days). Screen for strongyloides in endemic exposure.
- **Neuromuscular blockade** (conditional): early severe ARDS with dyssynchrony despite deep sedation — cisatracurium, 24–48 h. Not routine (ROSE).
- **Conservative fluids** once out of shock (FACTT): diuretics to even/negative balance → more ventilator-free days.
- **No** benefit: routine inhaled NO, β-agonists, statins, surfactant.
- **Treat the cause**: antibiotics, source control, stop the offending drug.
=== Sedation & liberation
- Target **light sedation** once stable (RASS 0 to −2); propofol/dexmedetomidine over benzodiazepines; analgesia first (fentanyl).
- Deep sedation only for proning, NMB, severe dyssynchrony.
- **Daily SAT + SBT** once FiO₂ ≤0.5 and PEEP ≤8.
- Early mobility, delirium screen (CAM-ICU), VAP bundle (head of bed 30°, oral care, subglottic suction).
:::

:::dose
Doses are typical adult doses. Adjust sedatives and steroids for organ function, and follow your ICU protocol.
:::

## 🏥 Real-life ICU tips

- **Measure the height.** Do not trust the stated or estimated height. A 4-inch error changes Vt by ~50 mL. Write the **Vt in mL** in the order, not just "6 mL/kg."
- **Check a plateau every shift** and after every vent change — not just peak pressure. Peak high + plateau normal = **airway** problem (secretions, kink, bronchospasm). Both high = **lung/chest wall** problem (worse ARDS, pneumothorax, abdominal compartment, mainstem intubation).
- **Driving pressure tells you more than P/F.** If raising PEEP lowers driving pressure → you recruited lung. If driving pressure rises → you overdistended.
- **Double-triggering** (two breaths stacked, Vt doubles) is common at 6 mL/kg: deepen sedation/analgesia, increase inspiratory time, or allow Vt up to 7–8 if plateau is still ≤30.
- **Sudden desaturation?** Bag on 100% → **DOPE** (Displacement, Obstruction, Pneumothorax, Equipment) → check ETT depth, suction, POCUS for lung sliding.
- **High PaCO₂ is OK** if pH ≥7.20 and no raised ICP, RV failure or severe acidosis. Raise RR before raising Vt; shorten the circuit (remove HME/extra tubing → less dead space).
- **Watch the RV.** Hypercapnia, high PEEP and hypoxia stress the RV. Echo: dilated RV, septal flattening → lower PEEP/plateau, fix CO₂, prone, consider inhaled pulmonary vasodilator, norepinephrine.
- **Prone before the CT.** Transport of a severe ARDS patient is dangerous. Do not delay proning for imaging.
- **Call ECMO early.** The referral is a phone call — not a commitment. Patients >7 days on high pressures or with multi-organ failure do worse.
- **Talk to the family early:** ARDS survivors often have weakness, cognitive problems and PTSD (post-ICU syndrome). Plan follow-up.

## ⚠️ Pitfalls

- Using **actual body weight** for tidal volume (obese patients get huge breaths).
- Chasing P/F with FiO₂ 100% for days instead of PEEP/proning.
- **Liberal fluids** after shock is over.
- Missing a **mimic** (DAH, eosinophilic pneumonia, PJP) that has a specific treatment.
- Prolonged **recruitment maneuvers** (staircase) — harm in ART trial.
- Forgetting **VAP**, pneumothorax, and **acute cor pulmonale** as causes of deterioration.

## 🎓 Board corner

| Stem | Answer |
|---|---|
| Sepsis day 2, bilateral infiltrates, P/F 140 on PEEP 10, normal echo | Moderate ARDS |
| Best evidence-based ventilation strategy | Vt 6 mL/kg PBW, plateau ≤30 |
| ARDS, P/F 90 on FiO₂ 0.8, PEEP 14 | Prone positioning |
| Hypoxemia not improving with 100% O₂ | Shunt — needs PEEP/recruitment |
| Peak 45, plateau 22 | Airway resistance (mucus plug, kink, bronchospasm) |
| Peak 45, plateau 38 | Low compliance / pneumothorax |
| Bilateral infiltrates within 6 h of transfusion, no volume overload | TRALI |
| Smoker started recently, BAL eosinophils 40% | Acute eosinophilic pneumonia → steroids |
| Which therapy improves oxygenation but NOT survival? | Inhaled nitric oxide |

## 📚 References

- ARDS Definition Task Force. Acute respiratory distress syndrome: the Berlin Definition. *JAMA.* 2012;307:2526.
- Matthay MA, et al. A new global definition of ARDS. *Am J Respir Crit Care Med.* 2024;209:37.
- Qadir N, et al. An Update on Management of Adult Patients with ARDS: An Official ATS Clinical Practice Guideline. *Am J Respir Crit Care Med.* 2024;209:24.
- ARDS Network. Lower tidal volumes. *NEJM.* 2000;342:1301.
- Guérin C, et al. PROSEVA. *NEJM.* 2013;368:2159.
- Combes A, et al. EOLIA (ECMO). *NEJM.* 2018;378:1965.
- Villar J, et al. DEXA-ARDS. *Lancet Respir Med.* 2020;8:267.
- Wiedemann HP, et al. FACTT (fluids). *NEJM.* 2006;354:2564.
- Amato MBP, et al. Driving pressure and survival. *NEJM.* 2015;372:747.
- Gattinoni L, Pesenti A. The concept of "baby lung." *Intensive Care Med.* 2005;31:776.
