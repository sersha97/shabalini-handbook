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


def render_fig(name):
    return f'<figure class="hbfig">{FIGS[name]()}</figure>'


def render_ecg(kind, caption=None):
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="hbfig ecgfig"><div class="ecgwrap">{ecg(kind)}</div>{cap}<div class="ecgnote">Schematic drawing · 25 mm/s · 10 mm/mV · swipe ↔</div></figure>'
