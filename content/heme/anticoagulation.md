---
title: Anticoagulation — heparin, warfarin, DOACs & bridging
emoji: "💉"
group: Platelets & clotting
order: 2
summary: Heparin doses by indication (weight-based or fixed), LMWH, DOACs, warfarin start and INR tricks, reversal, and who really needs a bridge.
tags: [anticoagulation, heparin, enoxaparin, warfarin, INR, DOAC, bridging, reversal]
reviewed: 2026-11-20
sources: CHEST VTE 2021 · CHEST perioperative 2022 · ACC/AHA AF 2023 · ESC AF 2024 · ACC/AHA valve 2020 · ACC ECDP bleeding 2020 · ISTH obesity 2021 · BRIDGE · PAUSE · FDA Andexxa 2025
---

:::bottom
- **First ask: what is the indication, and for how long?** The indication picks the drug, the dose and the target.
- **IV heparin is not one dose.** VTE = **80 U/kg bolus → 18 U/kg/h**. ACS = **60 U/kg (max 4000) → 12 U/kg/h (max 1000)**. Prophylaxis = **5000 U SC q8–12h** (fixed).
- **Most patients → a DOAC.** Warfarin still wins for **mechanical valves, moderate–severe rheumatic mitral stenosis, triple-positive APS** (and often dialysis, LVAD).
- **Starting warfarin for a clot?** Overlap heparin **≥5 days AND INR ≥2 for 24 h** — the **5-and-2 rule**.
- **High INR, no bleeding → hold doses.** INR >10 → add **vitamin K 2.5–5 mg PO**. **Major bleed → 4F-PCC + vitamin K 5–10 mg IV**.
- **Bridging is the exception.** No bridge for AF or for DOACs. Bridge only the patient in a **VEST** (see below).
- **Andexanet (Andexxa) is gone from the US (Dec 2025).** Xa-inhibitor bleed → **4F-PCC**.
:::

## 🧠 Pathophysiology in 60 seconds

- Clotting is a **relay race** that ends with **thrombin (IIa)** turning fibrinogen into a **fibrin net**.
- **Xa** makes thrombin. Block **Xa** or **IIa** and the net does not form.
- **Heparins** do not act alone. They **turbo-charge antithrombin (AT)**, which then kills Xa and IIa.
    - **UFH:** Xa = IIa (long chains grab both). **LMWH:** mostly Xa. **Fondaparinux:** Xa only.
- **DOACs** block one target **directly** (no AT needed): Xa (apixaban, rivaroxaban, edoxaban) or IIa (dabigatran).
- **Warfarin** blocks **vitamin K recycling** in the liver → the liver makes **non-working II, VII, IX, X** — and also **protein C and S** (the natural anticoagulants).

{{fig:coag-targets}}

:::mnemonic Which test for which drug?
- **WEPT** — **W**arfarin → **E**xtrinsic pathway → **PT**/INR
- **HIP** — **H**eparin → **I**ntrinsic pathway → a**P**TT (or anti-Xa)
- Warfarin factors = **"1972"**: **10, 9, 7, 2** (+ protein C and S).
:::

## 🎯 Who needs it, and for how long?

| Indication | Usual drug | Duration / target |
|---|---|---|
| **AF / flutter** — CHA₂DS₂-VASc **≥2 (men) / ≥3 (women)** | **DOAC** | Long term (risk does not go away after sinus rhythm) |
| AF — score **1 (men) / 2 (women)** | DOAC reasonable | Shared decision |
| **Cardioversion**, AF ≥48 h or unknown | DOAC or warfarin | **3 weeks before** (or TEE) + **≥4 weeks after** |
| **VTE** provoked by a **major transient** factor (surgery, trauma) | DOAC | **3 months** |
| VTE **unprovoked** or **persistent** risk factor | DOAC | 3 months, then usually **extended** if bleeding risk OK (apixaban 2.5 BID / rivaroxaban 10 daily) |
| **Cancer-associated VTE** | Apixaban, rivaroxaban, edoxaban or LMWH | **≥6 months**, while cancer is active |
| Isolated **distal DVT**, low risk, no symptoms | — | Serial ultrasound × 2 weeks, **or** 3 months |
| **Mechanical aortic valve** (bileaflet, no risk factor) | **Warfarin** | Lifelong, **INR 2.5** (2.0–3.0) |
| **Mechanical mitral** valve, or aortic + risk factor\* | **Warfarin** | Lifelong, **INR 3.0** (2.5–3.5) |
| On-X aortic valve | Warfarin + aspirin | INR 2.5 for 3 months, then **1.5–2.0** |
| Surgical **bioprosthetic** valve | Warfarin (or aspirin) | **3–6 months**, if low bleeding risk |
| **LV thrombus** after MI | Warfarin or DOAC | **3–6 months** → re-image |
| **Triple-positive APS** | **Warfarin** INR 2–3 | Lifelong |
| Superficial vein thrombosis ≥5 cm | Fondaparinux 2.5 mg daily | 45 days |

\*Risk factors for valves: AF, prior thromboembolism, LV dysfunction, hypercoagulable state, older caged-ball or tilting-disc valve.

:::new AF scores in 2023–2024
- **ACC/AHA 2023:** anticoagulate if annual stroke risk **≥2%** — CHA₂DS₂-VASc **≥2 men / ≥3 women**. Score is a start; other risk tools are allowed.
- **ESC 2024:** drops sex → **CHA₂DS₂-VA**. **≥2 → recommended**, **1 → consider**.
- **Never** use aspirin as a "softer" option for stroke prevention in AF.
:::

:::mnemonic WARF — when warfarin still wins over a DOAC
- **W**rong valve for a DOAC: **mechanical** valve, **moderate–severe rheumatic mitral stenosis**
- **A**ntiphospholipid syndrome — **triple-positive** or arterial events
- **R**enal failure — CrCl <15 / dialysis (apixaban is the DOAC alternative)
- **F**ew other options — **LVAD**, strong **inducers** (rifampin, carbamazepine, phenytoin), **bariatric** surgery / poor absorption, **cost**
:::

## 💉 Heparin (UFH) — dose by indication

{{fig:ufh-intensity}}

:::tabs
=== By indication
| Indication | Weight-based? | Bolus | Start rate | Target |
|---|---|---|---|---|
| **VTE treatment** (DVT, PE) | **Yes** — actual weight | **80 U/kg** | **18 U/kg/h** | anti-Xa **0.3–0.7** (aPTT ≈ 1.5–2.5× control) |
| **ACS** (NSTE-ACS, STEMI + lytic) | Yes, **capped** | **60 U/kg (max 4000)** | **12 U/kg/h (max 1000)** | anti-Xa 0.3–0.7 (aPTT ≈ 1.5–2×) |
| **PCI** (cath lab) | Yes | **70–100 U/kg** (50–70 with GP IIb/IIIa) | — | ACT 250–300 (200–250 with GPI) |
| **AF, mechanical valve, LV thrombus, bridging** ("cardiac / low-intensity" nomogram) | Yes | **None or small** — no bolus after a stroke or if bleeding risk | **12–18 U/kg/h** per local nomogram | anti-Xa 0.3–0.7 |
| **VTE prophylaxis** | **No — fixed** | — | **5000 U SC q8h or q12h**; BMI ≥40 → **7500 U SC q8h** | No monitoring |
| VTE treatment, SC, no monitoring (FIDO) | Yes | **333 U/kg SC** | then **250 U/kg SC q12h** | None |
| VTE, old **fixed-dose** IV | No | 5000 U | 1000 U/h | aPTT — weight-based is better |

- **Weight:** use **actual body weight**. Many protocols **cap** the VTE bolus (~10,000 U) and start rate (~2000 U/h) — follow your nomogram.
- **When to choose UFH over LMWH/DOAC:** CrCl <30, may need **lysis** or a **procedure soon** (short half-life ~60–90 min), very high bleeding risk, hemodynamically unstable PE.
=== Nomogram (VTE example)
**Raschke weight-based nomogram** — aPTT checked **6 h** after start and after every change.

| aPTT | Bolus | Rate change |
|---|---|---|
| <1.2× control (<35 s) | **80 U/kg** | ↑ **4 U/kg/h** |
| 1.2–1.5× (35–45 s) | **40 U/kg** | ↑ **2 U/kg/h** |
| 1.5–2.3× (46–70 s) | — | No change |
| 2.3–3× (71–90 s) | — | ↓ **2 U/kg/h** |
| >3× (>90 s) | **Hold 1 h** | ↓ **3 U/kg/h** |

- The seconds come from the original study. **Your lab's therapeutic range is different** — use the hospital nomogram.
- Two therapeutic values in a row → check **daily**.
=== aPTT vs anti-Xa
| Problem | aPTT | Anti-Xa |
|---|---|---|
| **Recent apixaban / rivaroxaban** (last 2–3 days) | ✅ Use it | ❌ **Falsely high** — the DOAC is an Xa inhibitor |
| Lupus anticoagulant, factor XII deficiency, warfarin overlap | ❌ Falsely high | ✅ Use it |
| Acute illness, **high factor VIII / fibrinogen** | ❌ Falsely low → "resistance" | ✅ Use it |
| High bilirubin or triglycerides | ✅ | ⚠️ Can read low |

**"Heparin resistance"** = needs **>35,000 U/day**. Check **anti-Xa** first (often already therapeutic), then **antithrombin** level.
=== Safety
- **Platelets:** baseline, then every 2–3 days on days 4–14 → think **[HIT](hit.html)** if they fall **>50%**.
- **Stop** 4–6 h before a procedure. Restart (no bolus) 12–24 h after, when hemostasis is OK.
- **Reversal — protamine:** **1 mg per 100 U** of heparin given in the **last 2–3 h** (max **50 mg**), slow IV (hypotension, anaphylaxis — fish allergy, NPH insulin, vasectomy).
:::

## 💉 LMWH & fondaparinux

| Use | Enoxaparin | CrCl <30 | Notes |
|---|---|---|---|
| **VTE prophylaxis** | **40 mg SC daily** (30 mg BID ortho/trauma) | **30 mg daily** | BMI ≥40 → **40 mg BID** (or 0.5 mg/kg daily) |
| **VTE treatment** | **1 mg/kg q12h** | **1 mg/kg daily** | 1.5 mg/kg daily is OK in simple VTE — **not** in cancer or obesity |
| **NSTE-ACS** | **1 mg/kg q12h** | 1 mg/kg daily | |
| **STEMI + lytic, age <75** | **30 mg IV** + 1 mg/kg SC q12h (max **100 mg** first 2 doses) | 1 mg/kg daily | |
| **STEMI + lytic, age ≥75** | **No bolus**, **0.75 mg/kg** q12h (max **75 mg** first 2 doses) | 1 mg/kg daily | |

- **Weight-based** on **actual weight**. No label maximum — check **anti-Xa** if **>150 kg**, **pregnant**, **CrCl <30**, or **<45 kg**.
- **Anti-Xa** = **4 h after the 3rd or 4th dose**. Target **0.6–1.0** (BID) or **1.0–2.0** (daily).
- **Dalteparin** (cancer VTE, CLOT): **200 U/kg daily × 1 month → 150 U/kg daily**.
- **Fondaparinux** (Xa only, no HIT risk): prophylaxis **2.5 mg daily**. Treatment by weight: **<50 kg 5 mg · 50–100 kg 7.5 mg · >100 kg 10 mg** daily. **Avoid CrCl <30.** No antidote.
- **Protamine for enoxaparin** (only ~60% reversal): given **<8 h** → **1 mg per 1 mg** enoxaparin; **8–12 h** → **0.5 mg per 1 mg**.

## 💊 DOACs

| Drug | AF | VTE treatment | Extended VTE (after 6 mo) | Dose cut |
|---|---|---|---|---|
| **Apixaban** | **5 mg BID** | **10 mg BID × 7 d** → 5 mg BID | 2.5 mg BID | AF: **2.5 BID** if **2 of 3**: age ≥80, weight ≤60 kg, Cr ≥1.5 |
| **Rivaroxaban** | **20 mg daily** with evening meal | **15 mg BID × 21 d** → 20 mg daily | 10 mg daily | AF: **15 mg** if CrCl 15–50. **Take 15/20 mg with food** |
| **Dabigatran** | **150 mg BID** | 5–10 d parenteral → 150 mg BID | 150 mg BID | US AF: 75 mg BID if CrCl 15–30. Do not open capsules |
| **Edoxaban** | **60 mg daily** | 5–10 d parenteral → 60 mg daily | — | **30 mg** if CrCl 15–50, weight ≤60 kg, or some P-gp inhibitors. AF: **avoid if CrCl >95** |

:::mnemonic Apixaban "80 – 60 – 1.5: two strikes → 2.5"
Age **≥80**, weight **≤60 kg**, creatinine **≥1.5**. **Two of three** → 2.5 mg BID. One alone → keep 5 mg BID. (This rule is for **AF** only — VTE doses do not change.)
:::

:::warn DOAC — do not use
- **Mechanical valve** (RE-ALIGN: more clots and bleeds with dabigatran) · **moderate–severe rheumatic mitral stenosis**
- **Triple-positive APS** · **pregnancy / breastfeeding** → LMWH
- **Strong P-gp + CYP3A4 inducers** (rifampin, carbamazepine, phenytoin, St John's wort)
- CrCl **<15** (apixaban is the exception — check with pharmacy) · early after **bariatric** surgery
- **Obesity is not a reason to avoid:** ISTH 2021 — **apixaban or rivaroxaban** are fine for VTE at any weight/BMI. Avoid dabigatran and edoxaban if BMI >40 or weight >120 kg.
:::

### Switching between drugs

| From → To | How |
|---|---|
| **IV UFH → DOAC** | Start the DOAC **when you stop the drip** |
| **LMWH → DOAC** | Start the DOAC **when the next LMWH dose is due** |
| **DOAC → UFH / LMWH** | Start **when the next DOAC dose is due** (UFH: **no bolus**; monitor by **aPTT**, not anti-Xa) |
| **Warfarin → DOAC** | Stop warfarin. Start when INR **<2** (apixaban, dabigatran), **<3** (rivaroxaban), **≤2.5** (edoxaban) |
| **DOAC → warfarin** | Overlap until INR **≥2**. Check INR **just before** the next DOAC dose (DOACs raise the INR) |

## 🟣 Warfarin — start, steer, stay in range

### Starting warfarin

- **Baseline:** CBC, **PT/INR**, aPTT, LFTs, creatinine, pregnancy test, **full drug list**.
- **Start dose:** **5 mg** daily for most inpatients.
    - **2.5 mg** (or less): age >75, frail, low weight, **liver disease**, **HF**, poor intake/NPO, hyperthyroid, **amiodarone** or other interacting drugs, Asian ancestry, known CYP2C9/VKORC1 variants.
    - **10 mg × 2 days** only in healthy, stable **outpatients** with VTE (CHEST).
- **INR daily** in hospital. After discharge: **3–5 days**, then weekly until stable, then every 4 weeks (up to **12 weeks** if very stable).

{{fig:warfarin-lag}}

:::mnemonic The "5-and-2" rule (any acute clot)
Heparin/LMWH + warfarin together for **at least 5 days** **AND** until **INR ≥2 for 24 h** (two INRs ≥2 on two days). Both conditions — not one.
:::

:::analogy
Warfarin **closes the factory**. It does not empty the **warehouse**. Factor VII sells out in a day — so the **INR rises on day 2** — but **prothrombin (II)** takes 3 days just to drop by half. Until the old II is gone, the INR **lies**: the number looks therapeutic, the patient is **not** protected. And protein C (the "guard") leaves first → a short **pro-clot** window → **warfarin skin necrosis**, **venous limb gangrene** in HIT.
:::

- **AF (no acute clot):** start warfarin **alone** — no heparin overlap needed.
- **Mechanical valve after surgery, or acute VTE:** overlap with UFH or LMWH (5-and-2).
- **Day 3 rule of thumb:** INR jumps **≥1 unit in a day**, or is **>2 by day 3** → sensitive patient → **cut the dose**.

### Maintenance — change the weekly dose, not the daily dose

{{fig:warfarin-pills}}

| INR (target 2–3) | Action |
|---|---|
| **<1.5** | ↑ weekly dose **10–20%** (consider 1 extra dose) |
| **1.5–1.9** | ↑ weekly dose **5–10%** |
| **2.0–3.0** | No change |
| **3.1–3.9** | ↓ weekly dose **5–10%** |
| **4.0–4.9** | **Hold 1 dose**, then ↓ **10%** |
| **≥5** | See **High INR** below |

- **Single** INR off by **≤0.5** with a clear reason (missed dose, one antibiotic course) in a stable patient → **no dose change**, recheck in 1–2 weeks.
- After a dose change, the new INR settles in **~5–7 days** — do not chase it every day in clinic.

:::pearl Weekly-dose math (makes changes easy)
- **5 mg daily = 35 mg/week.** +10% ≈ **37.5 mg** → "5 mg daily, **7.5 mg on Mondays**."
- −10% ≈ **32.5 mg** → "5 mg daily, **2.5 mg on Mondays**."
- Keep **one tablet strength** (cut in half if needed). Two strengths at home = dosing errors.
:::

### INR detective — why did it change?

Ask the **"INR interview"**: missed or extra doses · **new drugs** (antibiotics!) · diet (greens, shakes, tube feeds) · alcohol · illness (diarrhea, fever, **HF congestion** → liver) · thyroid.

:::mnemonic Drugs that push INR UP — "FAT MAC"
**F**luconazole (all azoles) · **A**miodarone · **T**MP-SMX · **M**etronidazole · **A**cetaminophen (>2 g/day for days) · **C**iprofloxacin / clarithromycin
- **Amiodarone:** cut warfarin **25–50%** when you start it. Effect builds over **weeks** → weekly INR for 6–8 weeks.
- **Metronidazole, fluconazole, TMP-SMX:** consider a **10–25% cut** and an INR in **3–5 days**.
:::

**INR goes DOWN with:** rifampin (huge), carbamazepine, phenytoin, phenobarbital, St John's wort, **more vitamin K** (greens, Ensure-type shakes, **tube feeds**), missed doses. **Vitamin K diet = steady, not zero.**

## 🚨 High INR & bleeding — reversal

{{fig:inr-ladder}}

:::tabs
=== Warfarin
- **4F-PCC (Kcentra)** — works in minutes:

| INR | Dose | Max |
|---|---|---|
| 2 to <4 | **25 U/kg** | 2500 U |
| 4–6 | **35 U/kg** | 3500 U |
| >6 | **50 U/kg** | 5000 U |

  Many hospitals use a **fixed dose** (e.g. **1000–1500 U**, **2000 U** for ICH). Recheck INR **15–60 min** after.
- **Always add vitamin K 5–10 mg IV** (slow, over 20–30 min). PCC lasts only ~6–8 h; vitamin K keeps the INR down.
- **Vitamin K route:** **IV** acts in ~4–6 h (full ~24 h) · **PO** in ~24 h · **avoid SC** (unpredictable) and **IM** (hematoma).
- **FFP** only if no PCC: ~10–15 mL/kg — big volume, slow, partial.
- **Surgery tomorrow** and INR still >1.5 → **vitamin K 1–2.5 mg PO** today.
=== DOACs
| Drug | Reversal |
|---|---|
| **Dabigatran** | **Idarucizumab 5 g IV** (2 × 2.5 g). Dialysis also removes it |
| **Apixaban, rivaroxaban, edoxaban** | **4F-PCC** 50 U/kg (or fixed 2000 U per protocol). **Andexanet: withdrawn from the US Dec 2025** (more thrombosis in ANNEXA-I) |
| Any DOAC taken **<2–4 h** ago | **Activated charcoal** if airway safe |

- **Last dose and CrCl** tell you how much drug is left. Normal PT/aPTT does **not** prove a DOAC is gone. Drug-specific anti-Xa (apixaban/rivaroxaban) or **dilute thrombin time** (dabigatran) if available.
=== Heparins
| Drug | Reversal |
|---|---|
| **UFH** | **Protamine 1 mg / 100 U** given in the last 2–3 h (max 50 mg) |
| **Enoxaparin** | Protamine **1 mg / 1 mg** (<8 h) · **0.5 mg / 1 mg** (8–12 h) — partial |
| **Fondaparinux** | No antidote — supportive; PCC/rFVIIa in extreme cases |
| **Argatroban / bivalirudin** | Stop — short half-life (≈45 min / 25 min) |
:::

:::warn Restart after a bleed
Most patients **need** their anticoagulant again. Discuss early with GI/neurosurgery. Typical timing: GI bleed **~7–14 days**, ICH **~4–8 weeks** (case by case). Not restarting is also a risk — strokes and clots.
:::

## 🌉 Bridging & procedures

{{fig:vest}}

:::flow
Q: Is the procedure minimal-bleeding (dental, cataract, skin, pacemaker/ICD implant, many endoscopies)?
Y: Usually **continue** warfarin (check INR in range). DOAC: hold only the morning dose or continue. Pacemaker/ICD on warfarin → **continue** (BRUISE CONTROL — strong CHEST recommendation).
Q: On a DOAC?
Y: **Never bridge.** Hold by drug, bleeding risk and CrCl (PAUSE table). Short half-life does the work.
Q: On warfarin — is the patient in a VEST (very high clot risk)?
Y: Bridge with **therapeutic LMWH** (or UFH if CrCl <30).
N: **No bridge.** Stop warfarin 5 days before, restart 12–24 h after. AF → no bridge (BRIDGE: same clots, ~2.5× more major bleeds with bridging).
:::

### Warfarin interruption — the timeline

{{fig:bridge-timeline}}

- **Stop warfarin 5 days before** (last dose on day −6). **INR on day −1** → if **>1.5**, give **vitamin K 1–2 mg PO**.
- **LMWH bridge** (only VEST patients): start **day −3** (therapeutic **1 mg/kg q12h**). **Last dose 24 h before** surgery = **half of the daily total** (morning dose only).
- **UFH bridge** (CrCl <30): start when INR <2. **Stop 4–6 h** before surgery.
- **After surgery:** warfarin **evening of surgery or next day** (usual dose). Therapeutic LMWH: **24 h** after low/moderate-bleed surgery, **48–72 h** after high-bleed surgery. Stop LMWH when **INR ≥2**.
- **PERIOP2 (2021):** post-op bridging in AF/mechanical valve patients gave **no benefit** — another reason to be choosy.

### DOAC interruption (PAUSE) — no bridging, no levels

| Drug | Low/moderate bleed risk | High bleed risk (incl. neuraxial) | Restart |
|---|---|---|---|
| **Apixaban, rivaroxaban, edoxaban** | Skip **1 day** (last dose day −2) | Skip **2 days** (last dose day −3) | **24 h** (low) · **48–72 h** (high) |
| **Dabigatran, CrCl ≥50** | Skip **1 day** | Skip **2 days** | same |
| **Dabigatran, CrCl 30–49** | Skip **2 days** | Skip **4 days** | same |

- High-bleed procedures: major cancer, cardiac, intracranial/spinal surgery, joint replacement, **neuraxial** anesthesia, kidney/liver biopsy, polypectomy >1 cm.
- After high-bleed surgery, give **prophylactic** dose LMWH/UFH until the full dose restarts.

:::dose
Doses are typical adult doses. Check renal and hepatic function, weight, drug interactions and your hospital nomograms. Heparin targets depend on **your lab** — use the local anti-Xa/aPTT range.
:::

## 🏥 Real-life ward tips

- **Write the indication and target** in every order and note: "Heparin — **PE** — anti-Xa 0.3–0.7". A wrong nomogram (VTE vs ACS) is a common error.
- **No bolus** after an ischemic stroke, a fresh post-op wound, or a recent bleed — start the drip at the rate only.
- **Patient came in on apixaban and you start heparin?** Use **aPTT** for 2–3 days — the anti-Xa will read falsely high and the drip gets turned down for nothing.
- **"Heparin resistance" on aPTT?** Send an **anti-Xa** before you go above 35,000 U/day. High factor VIII in sick patients makes the aPTT look low.
- **Platelets dropping on day 5–10 of heparin** → 4Ts score → **[HIT](hit.html)**. Do not "just switch to enoxaparin" — it cross-reacts.
- **Admitted with INR 6 and no bleeding?** Hold warfarin. Do **not** reflexively give vitamin K 10 mg IV — you will make the patient warfarin-resistant for a week.
- **INR suddenly high on antibiotics?** It is usually the antibiotic plus poor intake. Hold one dose, recheck, and tell the clinic **at discharge**.
- **Discharge on warfarin:** write the **weekly dose**, the tablet strength, the **next INR date (3–5 days)**, and **who** follows it. No follow-up plan = no warfarin.
- **DOAC at discharge:** check the **dose against the indication** (VTE loading dose done? AF reduction criteria?) and **CrCl with actual weight**. Check insurance cost **before** the patient leaves.
- **Elderly fallers:** a patient must fall **~295 times a year** for the subdural risk to outweigh the stroke benefit of warfarin in AF (Man-Son-Hing 1999). Falls alone are not a contraindication.
- **Liver disease:** the INR shows liver **synthesis**, not bleeding risk. Do not "correct" an INR of 2 with FFP before a paracentesis.
- **Combined with antiplatelets** (after PCI): keep **triple therapy short** (often ≤1 week), then DOAC + clopidogrel. Add a **PPI**.

## ⚠️ Pitfalls

- Using the **ACS nomogram** for a PE (under-treats) or the **VTE nomogram** for ACS (over-treats).
- Stopping heparin when the **INR hits 2 on day 3** — the 5-and-2 rule needs **both**.
- **Warfarin started alone** for an acute VTE, or in HIT before platelets recover.
- **Bridging AF patients** — more bleeding, no fewer strokes.
- **Bridging DOACs** — never needed.
- Apixaban **2.5 mg BID** for AF because of **one** criterion (age or Cr) → under-dosing → strokes.
- Rivaroxaban 15/20 mg **without food** (about one-third less absorbed).
- **DOAC for a mechanical valve** or triple-positive APS.
- Forgetting to restart anticoagulation after the procedure ("held for surgery" stays on the MAR for a week).
- **SC vitamin K** — slow and unpredictable.

## 🎓 Board corner

| Stem | Answer |
|---|---|
| New PE, 90 kg, IV heparin — bolus and rate? | 80 U/kg (7200 U) → 18 U/kg/h (1600 U/h) |
| NSTEMI, 110 kg, IV heparin bolus? | 60 U/kg but **max 4000 U** |
| On warfarin day 3 for DVT, INR 2.4 — stop enoxaparin? | **No** — needs ≥5 days and INR ≥2 for 24 h |
| Painful dark skin on the breast/thigh, day 4 of warfarin | Warfarin skin necrosis — protein C deficiency |
| INR 7, no bleeding | Hold warfarin, no routine vitamin K |
| INR 12, no bleeding | Hold + vitamin K 2.5–5 mg **PO** |
| INR 4, intracranial hemorrhage | 4F-PCC + vitamin K 10 mg IV |
| Bleeding on dabigatran | Idarucizumab |
| Life-threatening bleed on apixaban (US, 2026) | 4F-PCC (andexanet withdrawn) |
| AF, CHA₂DS₂-VASc 4, warfarin, colon resection — bridge? | **No** (BRIDGE trial) |
| Mechanical mitral valve, hip surgery | Stop warfarin 5 d, **bridge** with LMWH |
| Apixaban, hip replacement (high bleed) | Last dose 3 days before (skip 2 days); no bridge |
| AF + mechanical valve — best drug? | Warfarin (DOACs harm — RE-ALIGN) |
| Triple-positive APS + DVT | Warfarin INR 2–3 |
| Started amiodarone, INR rises from 2.5 to 4.8 | CYP2C9 inhibition → cut warfarin 25–50% |
| On rifampin, INR stuck at 1.3 on 15 mg/day | CYP induction → much higher warfarin dose or change the antibiotic (DOACs also interact) |
| Pregnant woman with new DVT | LMWH (warfarin teratogenic, DOAC not used) |
| aPTT does not rise on 40,000 U/day heparin | Check anti-Xa, then antithrombin level |

## 📚 References

- Stevens SM, et al. Antithrombotic therapy for VTE disease: second update of the CHEST guideline. *Chest.* 2021;160:e545.
- Douketis JD, et al. Perioperative management of antithrombotic therapy: an ACCP clinical practice guideline. *Chest.* 2022;162:e207.
- Joglar JA, et al. 2023 ACC/AHA/ACCP/HRS guideline for the diagnosis and management of atrial fibrillation. *Circulation.* 2024;149:e1.
- Van Gelder IC, et al. 2024 ESC guidelines for the management of atrial fibrillation. *Eur Heart J.* 2024;45:3314.
- Otto CM, et al. 2020 ACC/AHA guideline for the management of valvular heart disease. *Circulation.* 2021;143:e72.
- Tomaselli GF, et al. 2020 ACC expert consensus decision pathway on management of bleeding in patients on oral anticoagulants. *JACC.* 2020;76:594.
- Holbrook A, et al. Evidence-based management of anticoagulant therapy (CHEST 9th ed.). *Chest.* 2012;141:e152S.
- Martin KA, et al. Use of DOACs in patients with obesity: updated ISTH guidance. *J Thromb Haemost.* 2021;19:1874.
- Raschke RA, et al. The weight-based heparin dosing nomogram compared with a "standard care" nomogram. *Ann Intern Med.* 1993;119:874.
- Douketis JD, et al. BRIDGE — perioperative bridging anticoagulation in AF. *NEJM.* 2015;373:823.
- Douketis JD, et al. PAUSE — perioperative management of patients with AF receiving a DOAC. *JAMA Intern Med.* 2019;179:1469.
- Kovacs MJ, et al. PERIOP2 — postoperative LMWH bridging. *BMJ.* 2021;373:n1205.
- Birnie DH, et al. BRUISE CONTROL. *NEJM.* 2013;368:2084.
- Eikelboom JW, et al. RE-ALIGN — dabigatran in mechanical heart valves. *NEJM.* 2013;369:1206.
- Connolly SJ, et al. ANNEXA-I — andexanet for factor Xa inhibitor–associated ICH. *NEJM.* 2024;390:1745.
- FDA Safety Communication: Update on the safety of Andexxa (US sales ended Dec 22, 2025).
- Man-Son-Hing M, et al. Choosing antithrombotic therapy for elderly patients with AF who are at risk for falls. *Arch Intern Med.* 1999;159:677.
