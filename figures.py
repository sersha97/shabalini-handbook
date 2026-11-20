"""Figures for the handbook: drawn ECG strips (SVG) and HTML/CSS diagrams.

Use in Markdown:  {{ecg:af|Caption text}}   or   {{fig:ef-spectrum}}
All ECG strips are schematic teaching drawings, not real tracings.
"""
import math
import random

# ---------- ECG engine ----------
# 25 mm/s, 10 mm/mV. 1 mm = 4 units. 1 s = 100 units. 1 mV = 40 units.
SEC = 100.0
MV = 40.0


def g(t, mu, sd, amp):
    return amp * math.exp(-((t - mu) ** 2) / (2 * sd * sd))


class Beat:
    """One complex. Times in seconds from strip start."""

    def __init__(self, t, p=True, pr=0.16, qrs="narrow", st=0.0, t_amp=0.30,
                 qt=0.36, p_amp=0.15, r_amp=1.1, t_sd=0.05, pr_dep=0.0, conducted=True):
        self.__dict__.update(locals())
        del self.__dict__["self"]

    def value(self, x):
        v = 0.0
        t0 = self.t
        if self.p:
            v += g(x, t0, 0.025, self.p_amp)
        if not self.conducted:
            return v
        q = t0 + self.pr
        if self.pr_dep:
            v -= self.pr_dep * (1 / (1 + math.exp(-(x - t0 - 0.05) / 0.01))) * (1 / (1 + math.exp((x - q + 0.01) / 0.01)))
        if self.qrs == "narrow":
            v += g(x, q, 0.008, -0.10) + g(x, q + 0.025, 0.010, self.r_amp) + g(x, q + 0.050, 0.010, -0.25)
            j = q + 0.065
        else:  # wide
            v += g(x, q + 0.04, 0.025, self.r_amp) + g(x, q + 0.10, 0.025, -0.35)
            j = q + 0.13
        tpk = q + self.qt - 0.08
        if self.st:
            # ST plateau from J point to T wave
            rise = 1 / (1 + math.exp(-(x - j + 0.005) / 0.006))
            fall = 1 / (1 + math.exp((x - tpk - 0.04) / 0.03))
            v += self.st * rise * fall
        v += g(x, tpk, self.t_sd, self.t_amp)
        return v


def render_strip(beats, dur=6.0, baseline=None, height=160, label=None):
    w = dur * SEC
    mid = height * 0.62
    pts = []
    n = int(w * 1.5)
    for i in range(n + 1):
        x = i * dur / n
        v = sum(b.value(x) for b in beats if -0.3 < x - b.t < 0.9)
        if baseline:
            v += baseline(x)
        pts.append((x * SEC, mid - v * MV))
    d = "M" + " L".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    grid = []
    for gx in range(0, int(w) + 1, 4):
        cls = "gM" if gx % 20 == 0 else "gm"
        grid.append(f'<line class="{cls}" x1="{gx}" y1="0" x2="{gx}" y2="{height}"/>')
    for gy in range(0, height + 1, 4):
        cls = "gM" if gy % 20 == 0 else "gm"
        grid.append(f'<line class="{cls}" x1="0" y1="{gy}" x2="{w}" y2="{gy}"/>')
    lab = f'<text x="8" y="16" class="ecglab">{label}</text>' if label else ""
    return (f'<svg class="ecg" viewBox="0 0 {w:.0f} {height}" preserveAspectRatio="xMidYMid meet" role="img" '
            f'aria-label="{label or "ECG strip"}">{"".join(grid)}<path class="trace" d="{d}"/>{lab}</svg>')


def seq(start, rr, n):
    return [start + i * rr for i in range(n)]


def ecg(kind):
    random.seed(7)
    if kind == "sinus":
        return render_strip([Beat(t) for t in seq(0.2, 0.8, 8)], label="II · Normal sinus rhythm 75/min")
    if kind == "af":
        times, t = [], 0.15
        for rr in [0.42, 0.61, 0.38, 0.55, 0.47, 0.70, 0.40, 0.52, 0.45, 0.66, 0.39, 0.50, 0.58]:
            times.append(t); t += rr
        beats = [Beat(x, p=False) for x in times if x < 5.9]
        fib = lambda x: 0.05 * math.sin(2 * math.pi * 7.3 * x) + 0.04 * math.sin(2 * math.pi * 5.1 * x + 1) + 0.03 * math.sin(2 * math.pi * 9.7 * x + 2)
        return render_strip(beats, baseline=fib, label="II · AF with RVR — irregularly irregular, no P waves")
    if kind == "flutter":
        def saw(x):
            f = (x * 5.0) % 1.0
            return 0.12 - 0.36 * (f / 0.75) if f < 0.75 else -0.24 + 0.36 * ((f - 0.75) / 0.25)
        beats = [Beat(t, p=False) for t in seq(0.25, 0.40, 15)]
        return render_strip(beats, baseline=saw, label="II · Atrial flutter 2:1 — sawtooth waves, ventricular rate 150")
    if kind == "svt":
        beats = [Beat(t, p=False, t_amp=0.25, qt=0.26) for t in seq(0.15, 0.32, 19)]
        return render_strip(beats, label="II · SVT (AVNRT) — regular, narrow, ~185/min, no visible P")
    if kind == "vt":
        beats = [Beat(t, p=False, qrs="wide", r_amp=1.4, t_amp=-0.45, qt=0.32, t_sd=0.06) for t in seq(0.1, 0.36, 17)]
        return render_strip(beats, label="Monomorphic VT — wide, regular, ~165/min")
    if kind == "torsades":
        def tor(x):
            env = 0.3 + 1.1 * abs(math.sin(math.pi * x / 2.2))
            return env * math.sin(2 * math.pi * 4.2 * x)
        return render_strip([], baseline=tor, label="Torsades de pointes — QRS twists around the baseline")
    if kind == "longqt":
        beats = [Beat(t, qt=0.62, t_sd=0.09, t_amp=0.33) for t in seq(0.2, 1.0, 6)]
        return render_strip(beats, label="II · Long QT — QTc ~560 ms (T wave ends past halfway to next QRS)")
    if kind == "avb1":
        return render_strip([Beat(t, pr=0.32) for t in seq(0.15, 0.9, 7)], label="1st-degree AV block — PR 320 ms, every P conducts")
    if kind == "mobitz1":
        beats, t = [], 0.1
        for cyc in range(2):
            for pr in [0.18, 0.28, 0.36]:
                beats.append(Beat(t, pr=pr)); t += 0.78
            beats.append(Beat(t, conducted=False)); t += 0.78
        return render_strip(beats, label="Mobitz I (Wenckebach) — PR grows longer, then a P with no QRS")
    if kind == "mobitz2":
        beats, t = [], 0.1
        for i in range(8):
            beats.append(Beat(t, pr=0.18, qrs="wide" if True else "narrow", r_amp=0.9, conducted=(i % 3 != 2))); t += 0.74
        return render_strip(beats, label="Mobitz II — fixed PR, sudden dropped QRS (often wide QRS)")
    if kind == "chb":
        beats = [Beat(t, p=True, conducted=False) for t in seq(0.1, 0.62, 10)]
        beats += [Beat(t - 0.16, p=False, qrs="wide", r_amp=1.0, t_amp=-0.35, qt=0.44, t_sd=0.07) for t in seq(0.5, 1.55, 4)]
        return render_strip(beats, label="3rd-degree (complete) AV block — P waves and QRS march separately")
    if kind == "stemi":
        beats = [Beat(t, st=0.45, t_amp=0.55, t_sd=0.07, r_amp=0.9) for t in seq(0.2, 0.85, 7)]
        return render_strip(beats, label="V2–V3 · STEMI — ST elevation, convex 'tombstone' shape")
    if kind == "pericarditis":
        beats = [Beat(t, st=0.22, t_amp=0.36, pr_dep=0.12, r_amp=0.9) for t in seq(0.2, 0.85, 7)]
        return render_strip(beats, label="II · Pericarditis — diffuse concave ST elevation + PR depression")
    if kind == "hyperk":
        beats = [Beat(t, p_amp=0.06, qrs="wide", r_amp=0.9, t_amp=0.85, t_sd=0.035, qt=0.38) for t in seq(0.2, 0.9, 7)]
        return render_strip(beats, label="Hyperkalemia — tall peaked T, flat P, wide QRS")
    if kind == "sinetach":
        beats = [Beat(t, pr=0.14, qt=0.30) for t in seq(0.15, 0.5, 12)]
        return render_strip(beats, label="Sinus tachycardia 120 — a P before every QRS")
    if kind == "paced":
        ts = seq(0.2, 0.86, 7)
        spike = lambda x: sum(g(x, t + 0.16, 0.0025, 1.6) for t in ts)
        beats = [Beat(t, pr=0.17, qrs="wide", r_amp=1.0, t_amp=-0.35, qt=0.42, t_sd=0.07) for t in ts]
        return render_strip(beats, baseline=spike, label="DDD pacing — atrial-sensed, ventricular-paced: spike → wide QRS")
    if kind == "ftc":
        ts = seq(0.2, 0.86, 7)
        spike = lambda x: sum(g(x, t + 0.16, 0.0025, 1.6) for t in ts)
        beats = [Beat(t, pr=0.17, qrs="wide", r_amp=1.0, t_amp=-0.35, qt=0.42, t_sd=0.07, conducted=(i not in (2, 3, 5)))
                 for i, t in enumerate(ts)]
        return render_strip(beats, baseline=spike, label="Failure to capture — pacing spikes with no QRS after them")
    raise KeyError(kind)


# ---------- HTML / SVG diagrams ----------
FIGS = {}


def fig(name):
    def deco(fn):
        FIGS[name] = fn
        return fn
    return deco


@fig("ef-spectrum")
def _():
    return """<div class="efbar">
<div class="efseg r"><b>HFrEF</b><span>EF ≤40%</span><em>4 pillars save lives</em></div>
<div class="efseg m"><b>HFmrEF</b><span>EF 41–49%</span><em>SGLT2i; consider others</em></div>
<div class="efseg p"><b>HFpEF</b><span>EF ≥50%</span><em>SGLT2i + finerenone</em></div>
</div>
<div class="efimp">↗️ <b>HFimpEF</b> = EF was ≤40%, now &gt;40% → <b>keep</b> GDMT. Stopping it lets EF fall again.</div>"""


@fig("hemo-profiles")
def _():
    return """<div class="quad">
<div class="qh"></div><div class="qh">🏜️ Dry</div><div class="qh">🌊 Wet (congested)</div>
<div class="qv">🔥 Warm<br><small>perfused</small></div>
<div class="qc ok"><b>Warm & dry</b>Compensated. Optimize GDMT.</div>
<div class="qc wet"><b>Warm & wet</b>Most common (~70%). <u>Diurese.</u></div>
<div class="qv">🧊 Cold<br><small>low output</small></div>
<div class="qc cold"><b>Cold & dry</b>Rare. Careful fluids; look for other cause.</div>
<div class="qc bad"><b>Cold & wet</b>Worst prognosis. Inotrope ± pressor, then diurese. Think shock.</div>
</div>
<p class="figcap">Congestion: orthopnea, JVD, edema, rales, hepatojugular reflux. Low perfusion: cool limbs, narrow pulse pressure, confusion, rising creatinine/lactate.</p>"""


@fig("acs-spectrum")
def _():
    return """<div class="spec">
<div class="specitem ua"><b>Unstable angina</b><span>ECG: ± ST↓ / T inv</span><span>Troponin: <b>normal</b></span></div>
<div class="specitem nst"><b>NSTEMI</b><span>ECG: ± ST↓ / T inv</span><span>Troponin: <b>↑ with rise/fall</b></span></div>
<div class="specitem st"><b>STEMI</b><span>ECG: <b>ST↑</b> or equivalent</span><span>Troponin: ↑ (do not wait)</span></div>
</div>
<p class="figcap">One disease (plaque rupture → thrombus), three faces. Ischemia grows left → right. STEMI = total occlusion → open the artery now.</p>"""


@fig("af-bouncer")
def _():
    return """<svg viewBox="0 0 640 230" class="diag" role="img" aria-label="AV node as bouncer">
<rect x="10" y="40" width="190" height="150" rx="18" class="b1"/><text x="105" y="75" class="t1">ATRIA</text>
<text x="105" y="100" class="t2">350–600 chaotic</text><text x="105" y="120" class="t2">impulses / min</text><text x="105" y="160" class="emo">🎉🎉🎉</text>
<path d="M205 115 L255 115" class="arr"/><circle cx="320" cy="115" r="62" class="b2"/>
<text x="320" y="100" class="t1">AV NODE</text><text x="320" y="122" class="t2">"the bouncer"</text><text x="320" y="150" class="emo">🕴️</text>
<path d="M385 115 L435 115" class="arr"/><rect x="440" y="40" width="190" height="150" rx="18" class="b3"/>
<text x="535" y="75" class="t1">VENTRICLES</text><text x="535" y="100" class="t2">irregular</text><text x="535" y="120" class="t2">100–180 / min</text><text x="535" y="160" class="emo">💓</text>
<path d="M320 185 C320 225, 535 225, 535 195" class="arr dash"/><text x="420" y="225" class="t3">WPW: side door with no bouncer</text>
</svg>
<p class="figcap">Rate control makes the bouncer stricter (β-blocker, diltiazem, digoxin). In pre-excited AF, block the front door and the crowd rushes the side door → VF.</p>"""


@fig("hfref-pillars")
def _():
    return """<div class="pillars">
<div class="pil"><span>🛡️</span><b>ARNI</b><small>sacubitril/valsartan<br>(or ACEi/ARB)</small></div>
<div class="pil"><span>🐢</span><b>β-blocker</b><small>carvedilol, metoprolol succinate, bisoprolol</small></div>
<div class="pil"><span>🧲</span><b>MRA</b><small>spironolactone / eplerenone</small></div>
<div class="pil"><span>🍬</span><b>SGLT2i</b><small>dapagliflozin / empagliflozin</small></div>
</div>
<div class="roof">🏛️ Start all four early — low doses together beat one drug at max dose.</div>"""


@fig("sepsis-hour1")
def _():
    return """<ol class="timeline">
<li><b>0 min</b> 🚨 Recognize: NEWS2 / MEWS / SIRS (not qSOFA alone)</li>
<li><b>≤ 1 h</b> 🧫 Blood cultures ×2 → 💊 antibiotics (shock or probable sepsis)</li>
<li><b>≤ 1 h</b> 🧪 Lactate; repeat if &gt;2</li>
<li><b>≤ 3 h</b> 💧 ≥30 mL/kg balanced crystalloid if hypoperfused (ideal/adjusted weight if BMI &gt;30)</li>
<li><b>Early</b> 💉 Norepinephrine to MAP ≥65 (60–65 if age ≥65) — peripheral OK to start</li>
<li><b>Ongoing</b> 🔍 Source control · reassess with dynamic tests (PLR, CRT) · steroids if still on pressors</li>
</ol>"""


@fig("acid-base")
def _():
    return """<ol class="steps">
<li><b>1. pH</b> — &lt;7.35 acidemia · &gt;7.45 alkalemia</li>
<li><b>2. Primary process</b> — HCO₃ moves with pH = metabolic · PaCO₂ moves opposite = respiratory</li>
<li><b>3. Compensation</b> — Winter's: expected PaCO₂ = 1.5×HCO₃ + 8 ± 2</li>
<li><b>4. Anion gap</b> — Na − (Cl + HCO₃); correct for albumin (+2.5 per 1 g/dL below 4)</li>
<li><b>5. Delta–delta</b> — ΔAG ÷ ΔHCO₃: &lt;1 extra NAGMA · &gt;2 extra metabolic alkalosis</li>
<li><b>6. Osmolar gap</b> — if AG high and no clear cause → toxic alcohols</li>
</ol>"""


@fig("hypona-algo")
def _():
    return """<div class="tree">
<div class="node top">🧂 Na &lt;135 → check <b>serum osm</b></div>
<div class="row3">
<div class="node">High/normal osm<br><small>glucose, mannitol, pseudo (lipids/protein)</small></div>
<div class="node hl"><b>Low osm (&lt;275)</b><br><small>true hypotonic</small></div>
<div class="node">→ next: <b>urine osm</b></div></div>
<div class="row2">
<div class="node">U-osm &lt;100<br><small>primary polydipsia, beer potomania, tea & toast</small></div>
<div class="node hl">U-osm &gt;100 → <b>urine Na</b></div></div>
<div class="row2">
<div class="node">U-Na &lt;30<br><small>low effective volume: GI loss, HF, cirrhosis, nephrotic</small></div>
<div class="node">U-Na &gt;30<br><small>SIADH, diuretics, adrenal insufficiency, hypothyroid, salt wasting</small></div></div>
</div>"""


@fig("cirrhosis-map")
def _():
    return """<div class="hexgrid">
<div class="hx">💧<b>Ascites</b><small>Na 2 g, spironolactone:furosemide 100:40</small></div>
<div class="hx">🦠<b>SBP</b><small>PMN ≥250 → ceftriaxone + albumin</small></div>
<div class="hx">🧠<b>HE</b><small>lactulose → 2–3 soft BMs; + rifaximin</small></div>
<div class="hx">🩸<b>Varices</b><small>octreotide + ceftriaxone + EGD ≤12 h</small></div>
<div class="hx">🫘<b>HRS-AKI</b><small>albumin → terlipressin + albumin</small></div>
<div class="hx">🎯<b>HCC</b><small>US ± AFP q6 months</small></div>
</div>"""


@fig("pe-risk")
def _():
    return """<div class="spec">
<div class="specitem ua"><b>Low risk</b><span>sPESI 0, normal RV</span><span>➡️ DOAC, early discharge</span></div>
<div class="specitem nst"><b>Intermediate</b><span>RV strain ± troponin↑</span><span>➡️ heparin, watch closely</span></div>
<div class="specitem st"><b>High risk (massive)</b><span>SBP &lt;90 ≥15 min / shock</span><span>➡️ systemic lysis or catheter / surgery</span></div>
</div>"""


@fig("stroke-time")
def _():
    return """<ol class="timeline">
<li><b>0–4.5 h</b> 💉 IV tenecteplase 0.25 mg/kg (max 25 mg) <i>or</i> alteplase 0.9 mg/kg — if disabling deficit and no contraindication</li>
<li><b>0–24 h</b> 🧲 LVO on CTA → thrombectomy (EVT); lysis and EVT planned in parallel</li>
<li><b>4.5–24 h</b> 🖼️ Selected patients with salvageable tissue on advanced imaging may still get lysis</li>
<li><b>After</b> 🩺 BP &lt;180/105 for 24 h after lysis; swallow screen; antiplatelet at 24 h (if no lysis bleed)</li>
</ol>"""


@fig("ards-alveolus")
def _():
    return """<div class="alvpair">
<svg viewBox="0 0 340 320" class="diag ards" role="img" aria-label="Normal alveolus">
<text x="170" y="22" class="t1">NORMAL ALVEOLUS</text>
<circle cx="170" cy="145" r="98" fill="#eaf4fb" stroke="#7fb3d5" stroke-width="4"/>
<circle cx="170" cy="145" r="91" fill="none" stroke="#f2b134" stroke-width="3" stroke-dasharray="3 3"/>
<text x="170" y="130" class="t2">air-filled</text><text x="170" y="150" class="t2">thin wall →</text><text x="170" y="168" class="t2">fast O₂ transfer</text>
<text x="170" y="41" class="t3" style="fill:#b7860b">surfactant keeps it open</text>
<rect x="62" y="256" width="216" height="26" rx="13" fill="#d64545" opacity=".85"/>
<circle cx="110" cy="269" r="7" fill="#fff" opacity=".8"/><circle cx="170" cy="269" r="7" fill="#fff" opacity=".8"/><circle cx="230" cy="269" r="7" fill="#fff" opacity=".8"/>
<text x="170" y="305" class="t2">capillary · tight endothelium</text>
</svg>
<div class="alvarrow">⚡ injury<span>→</span></div>
<svg viewBox="0 0 340 320" class="diag ards" role="img" aria-label="ARDS alveolus">
<defs><pattern id="fluid" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#f4c7a1"/><circle cx="2" cy="2" r="1" fill="#e8a46e"/></pattern></defs>
<text x="170" y="22" class="t1" style="fill:#c0392b">ARDS — EXUDATIVE PHASE</text>
<circle cx="170" cy="145" r="98" fill="#eaf4fb" stroke="#c0392b" stroke-width="4" stroke-dasharray="10 5"/>
<path d="M75 170 A98 98 0 0 0 265 170 Z" fill="url(#fluid)"/>
<path d="M82 196 Q170 226 258 196" stroke="#7a4a2a" stroke-width="5" fill="none"/>
<text x="170" y="118" class="t2">less air · no surfactant</text>
<text x="170" y="138" class="t2">→ alveoli collapse</text>
<text x="170" y="192" class="t2">protein-rich edema</text>
<text x="170" y="214" class="t3">hyaline membrane</text>
<circle cx="135" cy="232" r="9" fill="#9b59b6"/><circle cx="205" cy="230" r="9" fill="#9b59b6"/>
<text x="170" y="250" class="t3" style="fill:#7d3c98">neutrophils</text>
<rect x="62" y="256" width="216" height="26" rx="13" fill="#d64545" opacity=".85"/>
<path d="M110 256 L106 238 M230 256 L235 238" stroke="#d64545" stroke-width="3"/>
<text x="170" y="305" class="t2" style="fill:#c0392b">leaky capillary → fluid floods in</text>
</svg>
</div>
<p class="figcap">Injury to the alveolar epithelium and capillary endothelium → protein-rich fluid, neutrophils and hyaline membranes fill the air space; surfactant is lost, so alveoli collapse. Result: <b>shunt</b> (blood passes unventilated alveoli), <b>stiff lungs</b> (low compliance) and <b>dead space</b>.</p>"""


@fig("baby-lung")
def _():
    return """<div class="babylung">
<div class="bl">
<b>🛌 Supine</b>
<div class="zone air">Aerated "baby lung"<small>(often only 20–30% of normal size)</small></div>
<div class="zone mid">Recruitable — opens with PEEP</div>
<div class="zone col">Collapsed / consolidated<small>(dependent, toward the bed)</small></div>
<div class="bed">bed</div>
</div>
<div class="bl">
<b>🔄 Prone</b>
<div class="zone air">Aeration spreads more evenly</div>
<div class="zone mid">Back (dorsal) lung re-opens — most of the lung mass</div>
<div class="zone air2">Better V/Q match, less overdistension</div>
<div class="bed">bed</div>
</div>
</div>
<p class="figcap">ARDS lungs are not stiff — they are <b>small</b>. A "normal" 10 mL/kg breath goes into a baby-sized lung → overdistension. That is why we set tidal volume by predicted body weight (6 mL/kg) and watch driving pressure. Proning makes ventilation more even and lowers mortality in severe ARDS (PROSEVA).</p>"""


@fig("ces-anatomy")
def _():
    roots = "".join(
        f'<path d="M{x0} 168 C{x0} 250, {x1} 290, {x1} 410" class="root"/>'
        for x0, x1 in [(171,141),(175,151),(179,161),(183,171),(187,181),(191,191),(195,201),(199,211)])
    return f"""<svg viewBox="0 0 360 440" class="diag ces" role="img" aria-label="Cauda equina anatomy and disc compression">
<text x="180" y="20" class="t1">CORD ENDS → "HORSE TAIL" BEGINS</text>
<rect x="132" y="34" width="90" height="390" rx="34" class="canal"/>
<path d="M165 36 L165 130 Q185 182 205 130 L205 36 Z" class="cord"/>
<text x="185" y="90" class="t2 wht">cord</text>
{roots}
<g class="vert"><rect x="236" y="56" width="70" height="42" rx="8"/><rect x="236" y="130" width="70" height="42" rx="8"/><rect x="236" y="204" width="70" height="42" rx="8"/><rect x="236" y="278" width="70" height="42" rx="8"/><rect x="236" y="352" width="70" height="42" rx="8"/></g>
<text x="271" y="82" class="t2">T12</text><text x="271" y="156" class="t2">L1–L2</text><text x="271" y="230" class="t2">L3</text><text x="271" y="304" class="t2">L4</text><text x="271" y="378" class="t2">L5–S1</text>
<ellipse cx="212" cy="336" rx="36" ry="14" class="disc"/>
<text x="118" y="164" class="lab" text-anchor="end">Conus</text><text x="118" y="182" class="sm" text-anchor="end">cord tip</text><path d="M122 168 L178 170" class="lead"/>
<text x="118" y="250" class="lab" text-anchor="end">Cauda</text><text x="118" y="268" class="sm" text-anchor="end">equina</text><text x="118" y="284" class="sm" text-anchor="end">(roots)</text><path d="M122 256 L160 256" class="lead"/>
<text x="118" y="334" class="lab red" text-anchor="end">Disc</text><text x="118" y="352" class="sm" text-anchor="end">herniation</text><path d="M122 338 L178 336" class="lead red"/>
</svg>
<div class="rootmap">
<div><span>🦵</span><b>L2–S1</b> legs: power, reflexes</div>
<div><span>🪑</span><b>S2–S5</b> saddle sensation</div>
<div><span>🚽</span><b>S2–S4</b> bladder</div>
<div><span>💩</span><b>S2–S4</b> anal sphincter, bowel</div>
<div><span>❤️</span><b>S2–S4</b> erection, genital feeling</div>
<div class="hl">🎯 S2–S4 roots run in the <b>middle</b> → a central disc hits them first</div>
</div>
<p class="figcap">The spinal cord ends at <b>L1–L2</b> (conus medullaris). Below that, the canal holds only nerve roots — the cauda equina (Latin: "horse's tail"). Roots are <b>peripheral nerves</b>, so damage gives <b>lower motor neuron</b> signs: weak, floppy, no reflexes. Memory hook: "S2, 3, 4 keeps the poo off the floor."</p>"""


@fig("ces-redflags")
def _():
    return """<div class="hexgrid">
<div class="hx">🪑<b>Saddle numbness</b><small>perineum, perianal, inner thighs — "toilet paper feels different"</small></div>
<div class="hx">🚽<b>Bladder change</b><small>hesitancy, weak stream, can't feel urine pass, retention</small></div>
<div class="hx">💩<b>Bowel change</b><small>new incontinence, can't feel stool, ↓ anal tone</small></div>
<div class="hx">❤️<b>Sexual change</b><small>new erectile dysfunction, ↓ genital sensation</small></div>
<div class="hx">🦵🦵<b>Bilateral sciatica</b><small>pain, numbness or weakness in both legs</small></div>
<div class="hx">📉<b>Progressive weakness</b><small>foot drop, new trouble walking</small></div>
</div>
<p class="figcap">Any one of these + back or leg pain (new, within ~2 weeks) = <b>emergency MRI</b>. Patients rarely volunteer them — you must <b>ask</b> about each one.</p>"""


@fig("ces-stages")
def _():
    return """<div class="spec">
<div class="specitem ua"><b>CES-S / CES-I</b><span>Symptoms ± signs, bladder still under voluntary control</span><span>➡️ <b>best window</b> — decompress now</span></div>
<div class="specitem nst"><b>CES-R</b><span>Painless urinary retention + overflow</span><span>➡️ outcome much worse</span></div>
<div class="specitem st"><b>CES-C</b><span>Complete: no saddle sensation, no bladder or anal control</span><span>➡️ often permanent</span></div>
</div>
<p class="figcap">S = suspected · I = incomplete · R = retention · C = complete. The goal is to <b>operate before CES-R</b>. Once the bladder is gone, surgery often cannot bring it back.</p>"""



# ---------- Conduction system heart (ported from jPoint EP Lab, core/heart.js) ----------
# Anatomic frontal view, as you face the patient: patient's RIGHT is on the viewer's LEFT.
JP = {
    "SVC": "M98 6 L98 72 L134 72 L134 6",
    "IVC": "M70 196 C60 214 56 230 52 250 L80 250 C82 234 86 220 96 204 Z",
    "RA": "M98 70 C64 80 54 120 58 160 C60 182 70 198 86 204 L190 207 L193 98 C176 76 150 68 134 70 Z",
    "LA": "M200 98 C226 72 300 70 330 92 C350 120 348 170 334 200 L206 207 Z",
    "RV": "M84 214 L196 214 C200 262 226 312 268 350 C222 360 160 342 116 300 C92 276 82 246 84 214 Z",
    "IVS": "M196 214 L214 214 C222 262 248 306 290 348 L278 356 C236 316 206 268 196 214 Z",
    "LV": "M214 214 L338 212 C356 252 348 316 300 358 L290 350 C250 310 224 266 214 214 Z",
    "PV": "M236 78 L226 50 M262 72 L258 44 M318 84 L340 62 M338 112 L366 104",
    "TV": "M86 210 L192 210", "MV": "M216 210 L336 208",
    "CFB": "M193 204 h18 v10 h-18 Z",
    "crista": "M108 82 C80 108 72 156 92 198",
    "bachmann": "M126 76 C170 58 236 64 300 84",
    "internodal": "M124 80 C160 110 178 150 184 178",
    "AVN_fast": "M193 128 C190 150 188 166 186 178", "AVN_slow": "M162 192 C170 188 178 184 184 182",
    "AVN": "M178 176 C182 174 190 176 192 182 C190 188 182 190 178 186 Z",
    "HIS": "M188 184 L202 214 L206 224",
    "LBB": "M206 224 L224 234",
    "LAF": "M224 234 C248 232 278 226 306 230",
    "LPF": "M224 234 C238 262 254 292 276 316",
    "RBB": "M204 224 C206 254 220 290 238 316",
    "MB": "M238 316 C206 324 170 316 136 296",
    "purk": "M306 230 l14 -6 M306 230 l10 10 M276 316 l14 4 M276 316 l2 14 M136 296 l-10 -10 M136 296 l-6 12 M238 316 l8 14 M262 340 l-10 8",
}
# label: x, y, text, anchor, strong
JP_LABELS = [
    (106, 24, "SVC", "start", 0), (22, 246, "IVC", "start", 0), (112, 124, "RA", "start", 0), (262, 124, "LA", "start", 0),
    (132, 262, "RV", "start", 0), (300, 284, "LV", "start", 0), (344, 56, "PVs", "start", 0),
    (104, 78, "SA node", "end", 1), (150, 58, "Bachmann", "start", 1), (172, 168, "AV node", "end", 1),
    (212, 198, "His", "start", 1), (250, 254, "LBB", "start", 1), (310, 226, "LAF", "start", 1), (282, 328, "LPF", "start", 1),
    (176, 338, "RBB / moderator band", "middle", 1),
]
# where to draw the red X for each block level
JP_BLOCK = {"avn": ("AVN", (185, 182), ["HIS", "LBB", "LAF", "LPF", "RBB", "MB"]),
            "his": ("HIS", (199, 210), ["LBB", "LAF", "LPF", "RBB", "MB"]),
            "rbb": ("RBB", (214, 272), ["MB"]),
            "lbb": ("LBB", (215, 229), ["LAF", "LPF"]),
            "laf": ("LAF", (266, 230), []),
            "lpf": ("LPF", (246, 284), [])}


def heart_svg(labels=True, block=None, title=None, small=False):
    P = JP
    blocked, mark, down = (None, None, [])
    if block:
        blocked, mark, down = JP_BLOCK[block]

    def cls(key, base):
        c = base
        if key == blocked:
            c += " blk"
        elif key in down:
            c += " dim"
        return c
    lab = ""
    if labels:
        lab = "".join(f'<text x="{x}" y="{y}" text-anchor="{a}" class="hl{" sp" if s else ""}">{t}</text>'
                      for x, y, t, a, s in JP_LABELS)
    xm = ""
    if mark:
        x, y = mark
        xm = (f'<g class="xm" transform="translate({x} {y})"><circle r="11"/>'
              f'<path d="M-5 -5 L5 5 M5 -5 L-5 5"/></g>')
    ttl = f'<text x="200" y="368" text-anchor="middle" class="jtitle">{title}</text>' if title else ""
    vb = "0 0 400 376" if title else "0 0 400 364"
    return f'''<svg viewBox="{vb}" class="jph{" sm" if small else ""}" role="img" aria-label="Frontal view of the heart and conduction system{(" — " + title) if title else ""}">
<g class="vessels"><path d="{P['SVC']}" class="vessel"/><path d="{P['IVC']}" class="vessel"/><path d="{P['PV']}" class="pv"/></g>
<path d="{P['RA']}" class="ch rt"/><path d="{P['LA']}" class="ch lt"/>
<path d="{P['RV']}" class="ch rt"/><path d="{P['LV']}" class="ch lt"/><path d="{P['IVS']}" class="ch sep"/>
<line x1="194" y1="98" x2="194" y2="206" class="ias"/>
<path d="{P['TV']}" class="annulus"/><path d="{P['MV']}" class="annulus"/><path d="{P['CFB']}" class="cfb"/>
<path d="{P['crista']}" class="faint"/><path d="{P['internodal']}" class="faint"/><path d="{P['bachmann']}" class="bach"/>
<path d="{P['AVN_fast']}" class="avp"/><path d="{P['AVN_slow']}" class="avp"/>
<path d="{P['AVN']}" class="{cls('AVN', 'avn')}"/>
<path d="{P['HIS']}" class="{cls('HIS', 'his')}"/><path d="{P['LBB']}" class="{cls('LBB', 'bb')}"/>
<path d="{P['LAF']}" class="{cls('LAF', 'bb')}"/><path d="{P['LPF']}" class="{cls('LPF', 'bb')}"/>
<path d="{P['RBB']}" class="{cls('RBB', 'bb')}"/><path d="{P['MB']}" class="{cls('MB', 'bb')}"/>
<path d="{P['purk']}" class="purk"/>
<ellipse cx="118" cy="74" rx="9" ry="6" class="san"/>
{xm}{lab}{ttl}
</svg>'''


@fig("conduction-heart")
def _():
    return f'''<div class="jpwrap">{heart_svg()}</div>
<div class="jplegend"><span><i class="k san"></i>SA node — pacemaker, 60–100/min</span><span><i class="k avn"></i>AV node — the delay (PR)</span><span><i class="k hp"></i>His–Purkinje — the fast highway (QRS)</span></div>
<p class="figcap">Frontal view, as you face the patient (patient's right is on your left). Order of the impulse: <b>SA node → atria</b> (Bachmann's bundle to the LA) <b>→ AV node</b> (slow, makes the PR) <b>→ His bundle</b> (crosses the fibrous skeleton) <b>→ right bundle</b> (thin cord down the septum, then the moderator band) and <b>left bundle</b> (short trunk that fans into the <b>anterior</b> and <b>posterior fascicles</b>) <b>→ Purkinje fibers</b>. Diagram adapted from the jPoint EP Lab model.</p>'''


@fig("block-levels")
def _():
    items = [("avn", "AV node", "1° / Mobitz I · narrow escape 40–60 · usually benign"),
             ("his", "His / infra-His", "Mobitz II / CHB · wide escape 20–40 · pace"),
             ("rbb", "Right bundle", "RBBB · rSR′ in V1"),
             ("lbb", "Left bundle", "LBBB · broad R in V6, QS in V1"),
             ("laf", "Left anterior fascicle", "LAFB · axis −45° or more left"),
             ("lpf", "Left posterior fascicle", "LPFB · right axis (rare)")]
    cards = "".join(f'<div class="blk-card">{heart_svg(labels=False, block=k, small=True)}<b>{n}</b><small>{s}</small></div>'
                    for k, n, s in items)
    return f'''<div class="blkgrid">{cards}</div>
<p class="figcap"><b>Where is the block?</b> Red ✕ = the block. Grey = the parts that now fill late, by slow muscle-to-muscle spread. Above the His (node) → narrow QRS, often vagal or drugs. Below the His → wide QRS, unstable escape, needs a pacemaker.</p>'''


def _qrs_svg(path, lead, color="#d64545"):
    return (f'<svg viewBox="0 0 120 110" class="qrs" role="img" aria-label="{lead}">'
            f'<line x1="0" y1="62" x2="120" y2="62" class="base"/><path d="{path}" style="stroke:{color}"/>'
            f'<text x="6" y="16" class="ld">{lead}</text></svg>')


@fig("bbb-qrs")
def _():
    # schematic QRS shapes (baseline y=62)
    rbbb_v1 = "M8 62 L28 62 L33 50 L39 72 L50 16 L60 62 L70 62 C80 72 92 74 104 62 L112 62"
    rbbb_v6 = "M8 62 L30 62 L33 66 L40 16 L48 62 L54 74 C62 80 68 70 74 62 L80 62 C90 50 100 50 108 62 L112 62"
    lbbb_v1 = "M8 62 L30 62 L34 58 L44 100 L58 100 L66 62 L82 52 C92 46 100 56 112 62"
    lbbb_v6 = "M8 62 L30 62 L36 26 L44 16 L50 24 L56 14 L66 62 L80 76 C92 82 100 70 112 62"
    rb = _qrs_svg(rbbb_v1, "V1") + _qrs_svg(rbbb_v6, "V6")
    lb = _qrs_svg(lbbb_v1, "V1", "#2b7bb9") + _qrs_svg(lbbb_v6, "V6", "#2b7bb9")
    return f'''<div class="bbbpair">
<div class="bbbcol r"><b>RBBB — "bunny ears" in V1</b><div class="qrow">{rb}</div><small>rSR′ in V1–V2 · wide slurred S in I and V6 · QRS ≥120 ms</small></div>
<div class="bbbcol l"><b>LBBB — "the tall notched R"</b><div class="qrow">{lb}</div><small>QS or rS in V1 · broad notched R in I, aVL, V6 · no septal q · ST–T opposite the QRS</small></div>
</div>
<p class="figcap">Memory hook: <b>WiLLiaM MaRRoW</b> — LBBB looks like a <b>W</b> in V1 and an <b>M</b> in V6; RBBB looks like an <b>M</b> in V1 and a <b>W</b> in V6. Schematic shapes, not real tracings.</p>'''


@fig("autoreg")
def _():
    return '''<svg viewBox="0 0 420 250" class="diag autoreg" role="img" aria-label="Cerebral autoregulation curve shifts right in chronic hypertension">
<line x1="50" y1="210" x2="400" y2="210" class="ax"/><line x1="50" y1="210" x2="50" y2="20" class="ax"/>
<text x="225" y="240" class="t2">Mean arterial pressure →</text>
<text x="18" y="115" class="t2" transform="rotate(-90 18 115)">Brain blood flow →</text>
<path d="M60 190 C80 120 90 110 110 110 L210 110 C240 110 250 60 280 30" class="cv n"/>
<path d="M120 195 C150 122 160 116 180 116 L300 116 C330 116 340 60 370 30" class="cv h"/>
<text x="150" y="96" class="t3n">Normal</text><text x="250" y="138" class="t3h">Chronic HTN</text>
<circle cx="141" cy="150" r="6" class="dot"/>
<text x="152" y="172" class="t2 sm" text-anchor="start">"Normal" BP on a shifted curve</text><text x="152" y="188" class="t2 sm red" text-anchor="start">= low flow, ischemia</text>
</svg>
<p class="figcap">The brain (and kidney, heart) keep flow stable across a range of pressures. After years of high BP, that range <b>moves to the right</b>. A "normal" BP can now be <b>too low for this patient</b> → stroke, MI, AKI. That is why we lower BP <b>in steps</b>, not to normal in one hour.</p>'''


@fig("htn-steps")
def _():
    return '''<div class="steps4">
<div class="st s1"><b>⏱️ First hour</b><span>SBP ↓ by <b>no more than 25%</b></span></div>
<div class="st s2"><b>🕑 Next 2–6 h</b><span>If stable → <b>&lt;160/100</b></span></div>
<div class="st s3"><b>📅 24–48 h</b><span>Cautiously → <b>130–140</b> systolic, start oral meds</span></div>
</div>
<div class="steps4 exc">
<div class="st x1"><b>🧵 Aortic dissection</b><span>SBP <b>&lt;120</b> and HR <b>&lt;60</b> within the first hour (as fast as tolerated)</span></div>
<div class="st x2"><b>🤰 Preeclampsia · 🧪 pheo</b><span>SBP <b>&lt;140</b> in the first hour</span></div>
<div class="st x3"><b>🧠 Stroke / ICH</b><span>Own targets — see Management</span></div>
</div>
<p class="figcap">Top: no compelling condition (2025 AHA/ACC). Bottom: <b>compelling conditions</b> — here faster and lower is the goal.</p>'''


@fig("aorta-types")
def _():
    def aorta(kind):
        flap = ('<path d="M92 210 C86 150 92 100 130 74" class="flap"/><path d="M146 66 C190 50 230 60 252 96 L262 150" class="flap"/>'
                if kind == "A" else '<path d="M256 112 L262 160 L264 230" class="flap"/>')
        tag = "Stanford A" if kind == "A" else "Stanford B"
        sub = "involves the ascending aorta" if kind == "A" else "starts after the left subclavian"
        act = "→ emergency surgery" if kind == "A" else "→ medical ± TEVAR"
        return f'''<svg viewBox="0 0 320 352" class="diag aorta" role="img" aria-label="{tag} aortic dissection">
<path d="M80 250 L80 140 C80 70 120 40 170 40 C230 40 272 70 272 130 L272 280 L240 280 L240 132 C240 92 210 72 170 72 C132 72 112 96 112 140 L112 250 Z" class="wall"/>
<path d="M140 46 L134 10 M170 40 L170 6 M196 44 L204 10" class="branch"/>
<text x="210" y="16" class="sm">L subclavian</text>
<ellipse cx="96" cy="262" rx="26" ry="9" class="valve"/>
{flap}
<text x="160" y="304" class="t1 {"red" if kind=="A" else "blue"}">{tag}</text>
<text x="160" y="324" class="t2">{sub}</text>
<text x="160" y="344" class="t2 b">{act}</text>
</svg>'''
    return f'''<div class="aopair">{aorta("A")}{aorta("B")}</div>
<p class="figcap">Red line = the intimal flap. <b>Type A</b> (any ascending involvement, wherever the tear starts) can rupture into the pericardium (tamponade), tear the aortic valve (acute AR) or dissect a coronary — usually the <b>RCA</b> → inferior STEMI. <b>Type B</b> threatens what branches off downstream: gut, kidneys, spinal cord, legs.</p>'''


@fig("duke-iscvid")
def _():
    return '''<div class="duke">
<div class="dcol maj"><h4>MAJOR</h4>
<div class="di"><b>🧫 Microbiology</b><small>Typical organism in ≥2 separate cultures (S. aureus, S. lugdunensis, E. faecalis, viridans/most strep, HACEK, Granulicatella, Abiotrophia, Gemella) · non-typical in ≥3 sets · Coxiella (culture or phase I IgG &gt;1:800) · positive PCR/sequencing</small></div>
<div class="di"><b>🖥️ Imaging</b><small>Echo or cardiac CT: vegetation, perforation, abscess, pseudoaneurysm, fistula, new prosthetic dehiscence · <b>PET/CT</b>: abnormal uptake at valve, graft or leads (NEW)</small></div>
<div class="di"><b>🔪 Surgery</b><small>IE seen by the surgeon at operation (NEW)</small></div>
</div>
<div class="dcol min"><h4>MINOR</h4>
<div class="di">🫀 Predisposition (prior IE, prosthetic valve, IDU, CIED, congenital/valve disease)</div>
<div class="di">🌡️ Fever &gt;38.0 °C</div>
<div class="di">🩸 Vascular: emboli, septic pulmonary infarcts, mycotic aneurysm, ICH, conjunctival hemorrhage, <b>Janeway</b> lesions, imaging-only emboli</div>
<div class="di">🧬 Immunologic: GN, <b>Osler</b> nodes, <b>Roth</b> spots, RF+</div>
<div class="di">🧪 Micro that falls short of major</div>
<div class="di">🖥️ PET uptake &lt;3 months after prosthesis · 🩺 new regurgitant murmur if no echo</div>
</div>
</div>
<div class="dres"><span class="def">✅ <b>Definite</b> = 2 major · 1 major + 3 minor · 5 minor · or pathology</span><span class="pos">❓ <b>Possible</b> = 1 major + 1 minor · or 3 minor</span></div>
<p class="figcap">2023 Duke-ISCVID criteria, simplified. These are classification criteria — a strong clinical picture still gets treated.</p>'''


@fig("as-door")
def _():
    return '''<svg viewBox="0 0 440 210" class="diag asg" role="img" aria-label="Pressure gradient across a stenotic aortic valve">
<line x1="40" y1="180" x2="420" y2="180" class="ax"/><line x1="40" y1="180" x2="40" y2="14" class="ax"/>
<text x="230" y="202" class="t2">Systole →</text><text x="16" y="100" class="t2" transform="rotate(-90 16 100)">Pressure</text>
<path d="M60 170 C90 168 96 40 160 30 C230 22 270 34 300 90 C320 140 330 168 360 172" class="lvp"/>
<path d="M60 120 C100 120 110 112 140 100 C180 86 230 84 280 100 C310 112 330 118 360 122" class="aop"/>
<path d="M140 100 C96 40 160 30 160 30 C230 22 270 34 280 100 C230 84 180 86 140 100 Z" class="grad"/>
<text x="210" y="62" class="t3">gradient</text>
<text x="372" y="168" class="sm l">LV</text><text x="372" y="124" class="sm a">Aorta</text>
</svg>
<div class="hexgrid as4">
<div class="hx">⛽<b>Keep the tank full</b><small>Preload-dependent. Diurese gently. Treat bleeding and vomiting fast.</small></div>
<div class="hx">🐢<b>Keep the rate slow</b><small>Tachycardia shortens diastole → less filling and coronary flow. AF poorly tolerated.</small></div>
<div class="hx">🎯<b>Keep the afterload up</b><small>Big vasodilator drops (nitro, hydralazine, sedation) → BP crash. Hypotension → phenylephrine or norepinephrine.</small></div>
<div class="hx">🎻<b>Keep the rhythm</b><small>The stiff LV needs the atrial kick. Cardiovert unstable AF early.</small></div>
</div>
<p class="figcap">A calcified valve is a <b>fixed, narrow door</b>. The LV must push much harder (the shaded gap is the gradient). Cardiac output cannot rise much — so anything that drops filling or BP can cause collapse.</p>'''


@fig("nbg-code")
def _():
    return '''<div class="nbg">
<div class="nl"><span class="big">D</span><b>Chamber paced</b><small>A · V · D (both) · O</small></div>
<div class="nl"><span class="big">D</span><b>Chamber sensed</b><small>A · V · D · O (none)</small></div>
<div class="nl"><span class="big">D</span><b>Response to sensing</b><small>I = inhibit · T = trigger · D = both · O = none</small></div>
<div class="nl opt"><span class="big">R</span><b>Rate response</b><small>Sensor speeds up with activity</small></div>
</div>
<div class="magnet">
<div class="mg pm"><b>🧲 Magnet on a pacemaker</b><span>→ <b>asynchronous pacing</b> (VOO/DOO) at the magnet rate. Pacing does <b>not</b> stop. Use: stop EMI inhibition in surgery, end pacemaker-mediated tachycardia.</span></div>
<div class="mg icd"><b>🧲 Magnet on an ICD</b><span>→ <b>shocks and ATP suspended</b>. Pacing is <b>unchanged</b> (still inhibited by noise). Remove magnet → therapies come back.</span></div>
<div class="mg ll"><b>💊 Leadless pacemaker</b><span>Most have <b>no magnet response</b> — call the device team to reprogram.</span></div>
</div>
<p class="figcap">DDD = paces and senses both chambers, inhibits or triggers. VVI = paces and senses the ventricle, inhibits if it sees a native beat. Magnet response differs by vendor and programming — confirm with the device clinic.</p>'''


def render_fig(name):
    return f'<figure class="hbfig">{FIGS[name]()}</figure>'


def render_ecg(kind, caption=None):
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="hbfig ecgfig"><div class="ecgwrap">{ecg(kind)}</div>{cap}<div class="ecgnote">Schematic drawing · 25 mm/s · 10 mm/mV · swipe ↔</div></figure>'
