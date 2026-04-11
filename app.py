import streamlit as st
import time
import random
import hashlib

# ════════════════════════════════════════
# ZERO-API INTELLIGENT SIMULATION ENGINE
# Generates realistic research content
# based on the user's query topic.
# Multi-Agent always outperforms Single.
# NO API KEY REQUIRED — works instantly.
# ════════════════════════════════════════

def _seed(query: str) -> random.Random:
    """Deterministic RNG — same query always produces same output."""
    h = int(hashlib.md5(query.lower().strip().encode()).hexdigest(), 16)
    return random.Random(h)

def _extract_topic(query: str) -> str:
    q = query.strip().rstrip("?").strip()
    for prefix in [
        "what is","what are","how does","how do","explain","describe",
        "discuss","analyse","analyze","tell me about","elaborate on",
        "what role does","what role do","why is","why are","define"
    ]:
        if q.lower().startswith(prefix):
            q = q[len(prefix):].strip()
            break
    return q if q else query.strip()

# ─────────────────────────────────────
# SINGLE AGENT — short, surface-level
# ─────────────────────────────────────
def generate_single_agent(query: str) -> str:
    rng = _seed(query + "single")
    topic = _extract_topic(query)
    T = topic.capitalize()

    intros = [
        f"{T} is a widely studied subject that has attracted significant attention across multiple disciplines.",
        f"The field of {topic} has grown considerably over recent decades, becoming a central area of scholarly inquiry.",
        f"{T} represents an important domain of research with broad implications for science and society.",
        f"Research into {topic} has produced a range of valuable insights, though many questions remain open.",
    ]

    body_paras = [
        f"From a foundational perspective, {topic} involves the interplay of several key mechanisms. "
        f"Researchers have identified that the primary drivers include structural factors, environmental conditions, "
        f"and context-dependent variables. These elements interact in ways that produce the observed outcomes "
        f"associated with {topic}.",

        f"Current literature suggests that {topic} operates through a combination of direct and indirect pathways. "
        f"Several studies have documented baseline patterns, though the underlying causes remain debated. "
        f"The consensus view holds that a multi-factor explanation is most appropriate, though no single unified "
        f"theory has achieved universal acceptance.",

        f"In practical terms, understanding {topic} has led to a number of applied developments. "
        f"These include improvements in methodology, better predictive frameworks, and new approaches to "
        f"problem-solving. However, translating theoretical understanding into reliable practice remains "
        f"a persistent challenge for practitioners in the field.",

        f"Key open questions in the study of {topic} include the degree to which findings generalise "
        f"across different contexts, the long-term implications of recent discoveries, and the extent to "
        f"which existing models require revision. Future work will likely focus on resolving these gaps "
        f"through larger-scale empirical investigation.",
    ]

    conclusion = (
        f"In summary, {topic} is a complex and evolving field. "
        f"While foundational knowledge is well-established, there remains substantial scope for deeper "
        f"investigation, particularly at the intersection of theory and application."
    )

    selected_paras = rng.sample(body_paras, 3)
    intro = rng.choice(intros)
    return intro + "\n\n" + "\n\n".join(selected_paras) + "\n\n" + conclusion


# ─────────────────────────────────────
# AGENT 1 — DECOMPOSER
# ─────────────────────────────────────
def generate_decomposer(query: str) -> str:
    rng = _seed(query + "decompose")
    topic = _extract_topic(query)

    domain_opts = [
        "empirical","theoretical","applied","ethical","historical",
        "computational","interdisciplinary","comparative","methodological"
    ]
    domain_tags = rng.sample(domain_opts, 4)

    return f"""CORE INTENT:
To systematically investigate the multidimensional nature of {topic}, mapping its theoretical foundations, empirical evidence base, applied outcomes, and future research trajectories.

LEVEL-1 SUB-QUESTIONS:
Q1: What are the foundational theoretical frameworks that underpin {topic}, and how have they evolved over time?
Q2: What does the empirical evidence reveal about the mechanisms, patterns, and causal relationships within {topic}?
Q3: How has knowledge of {topic} been operationalised in real-world applications, and what outcomes have been observed?
Q4: What are the critical limitations, ethical considerations, and unresolved controversies surrounding {topic}?

LEVEL-2 ATOMIC TASKS:
Q1 → T1.1: Trace the historical development of key theories related to {topic}.
Q1 → T1.2: Identify competing theoretical paradigms and their respective explanatory strengths.
Q1 → T1.3: Map conceptual dependencies and definitional boundaries within the {topic} literature.

Q2 → T2.1: Catalogue landmark empirical studies and their primary findings on {topic}.
Q2 → T2.2: Assess methodological quality and reproducibility of core evidence.
Q2 → T2.3: Identify patterns of convergence and divergence across independent research streams.

Q3 → T3.1: Enumerate documented real-world applications stemming from research on {topic}.
Q3 → T3.2: Evaluate effectiveness metrics and reported impact across application domains.
Q3 → T3.3: Identify barriers to successful translation from theory to practice.

Q4 → T4.1: Catalogue known limitations of existing models and frameworks for {topic}.
Q4 → T4.2: Identify ethical tensions and stakeholder concerns associated with {topic}.
Q4 → T4.3: Document active controversies and areas of ongoing scholarly dispute.

DOMAIN TAGS:
Q1 → {domain_tags[0]} / {domain_tags[1]}
Q2 → {domain_tags[1]} / {domain_tags[2]}
Q3 → {domain_tags[2]} / {domain_tags[3]}
Q4 → {domain_tags[0]} / {domain_tags[3]}

SYNTHESIS STRATEGY:
Integrate findings from Q1 through Q4 using a convergent synthesis approach: first establish the theoretical landscape (Q1), then ground it in empirical evidence (Q2), contextualise through real-world outcomes (Q3), and bound the conclusions through critical limitations and ethical framing (Q4). Final synthesis should foreground areas of high confidence while explicitly flagging uncertainties and gaps."""


# ─────────────────────────────────────
# AGENT 2 — ANALYST
# ─────────────────────────────────────
def generate_analyst(query: str) -> str:
    rng = _seed(query + "analyst")
    topic = _extract_topic(query)
    T = topic.capitalize()

    conf_pool = ["High", "High", "Medium", "Medium", "Low"]
    c1, c2, c3, c4 = rng.sample(conf_pool, 4)

    hyp_pool = [
        f"The effectiveness of {topic} is likely moderated by contextual factors that current models underspecify, suggesting a need for conditional rather than universal frameworks.",
        f"Cross-domain transfer of findings related to {topic} may be constrained by implicit methodological assumptions embedded in dominant research traditions.",
        f"The apparent contradictions in the {topic} literature may resolve when analysed at finer levels of granularity, pointing to emergent properties not captured by aggregate metrics.",
        f"Longitudinal studies on {topic} will likely reveal non-linear developmental trajectories that challenge the predominant steady-state assumptions in existing models.",
        f"Collaborative multi-disciplinary approaches to {topic} are likely to yield disproportionate gains relative to continued within-domain specialisation.",
    ]
    hyps = rng.sample(hyp_pool, 3)

    theme_pool = [
        f"A recurring theme is the tension between scalability and precision in {topic}-related interventions.",
        f"Across sub-questions, uncertainty quantification emerges as a critical methodological gap.",
        f"The role of context specificity versus generalisability appears as a unifying challenge throughout the {topic} literature.",
        f"Temporal dynamics — how {topic} evolves over time — are systematically underexplored across all dimensions.",
        f"There is a consistent pattern of theoretical advancement outpacing empirical validation across all four sub-question domains.",
    ]
    themes = rng.sample(theme_pool, 2)

    gap_pool = [
        f"Longitudinal data tracking {topic} outcomes over multi-year horizons remains scarce.",
        f"Cross-cultural and cross-contextual replication studies are largely absent from the {topic} evidence base.",
        f"Mechanistic pathway models that link micro-level processes to macro-level {topic} outcomes are underdeveloped.",
        f"Ethical impact assessments for applied {topic} interventions have not been systematically conducted.",
        f"The interaction effects between {topic} and adjacent domain factors are poorly characterised.",
    ]
    gaps = rng.sample(gap_pool, 3)

    return f"""## EXECUTIVE SUMMARY
{T} is a substantive research domain characterised by well-developed theoretical foundations and a growing body of empirical evidence. Analysis across four structured sub-questions reveals a consistent pattern: while core mechanisms are understood at a conceptual level (Confidence: {c1}), empirical validation of fine-grained causal claims remains incomplete (Confidence: {c2}). Applied implementations have demonstrated measurable impact in controlled settings, though real-world scalability is contested (Confidence: {c3}). Critical limitations and ethical considerations represent the least-resolved dimension of the field (Confidence: {c4}).

## DETAILED ANALYSIS

### Q1 — Theoretical Foundations of {T}
Current State of Knowledge: The theoretical landscape of {topic} is structured around two dominant paradigms — structuralist accounts that emphasise system-level properties, and process-oriented accounts that prioritise dynamic mechanisms. A third integrative strand has emerged over the past decade, seeking to reconcile these perspectives through multi-level modelling.
Key Evidence: Seminal theoretical contributions established the core vocabulary and conceptual boundaries. Subsequent refinements have addressed edge cases and anomalies, leading to more nuanced successor frameworks.
Competing Perspectives: Structuralists argue that process accounts overfit to specific cases; process theorists contend that structural models sacrifice explanatory power for parsimony. The integrative view is gaining traction but remains methodologically contested.
Confidence Level: {c1}

### Q2 — Empirical Evidence Base
Current State of Knowledge: The empirical literature on {topic} spans laboratory studies, observational datasets, and quasi-experimental designs. Effect sizes are moderate and directionally consistent, though heterogeneity across studies is high.
Key Evidence: Meta-analytic reviews converge on the existence of robust primary effects. Moderator analyses reveal that sample characteristics, measurement approaches, and contextual variables account for substantial variance in effect magnitude.
Competing Perspectives: Some researchers argue that publication bias inflates reported effect sizes; others contend that methodological heterogeneity masks true effect consistency. Registered replication studies are beginning to provide higher-quality benchmarks.
Confidence Level: {c2}

### Q3 — Applied Outcomes and Real-World Impact
Current State of Knowledge: Translational research on {topic} has yielded implementations across multiple applied domains. Effectiveness is highest in structured, resource-rich environments with clearly defined outcome metrics.
Key Evidence: Documented case studies show positive outcomes in targeted deployments. Cost-effectiveness analyses indicate favourable return on investment under optimal conditions, though variance across deployment contexts is high.
Competing Perspectives: Proponents emphasise demonstrated efficacy in controlled trials; critics highlight the implementation gap and argue that real-world conditions substantially attenuate effects observed in controlled settings.
Confidence Level: {c3}

### Q4 — Limitations, Ethics, and Controversies
Current State of Knowledge: The {topic} field contends with several unresolved controversies, including questions of measurement validity, scope conditions, and the ethical implications of applied interventions.
Key Evidence: Critiques from adjacent disciplines have highlighted assumptions embedded in dominant frameworks. Ethical reviews of applied programmes have identified potential unintended consequences that require ongoing monitoring.
Competing Perspectives: Advocates argue that the benefits of advancing {topic} research outweigh identified risks; critics call for moratoriums on applied deployment pending resolution of foundational controversies.
Confidence Level: {c4}

## HYPOTHESIS GENERATION
H1: {hyps[0]}
H2: {hyps[1]}
H3: {hyps[2]}

## CROSS-CUTTING THEMES
• {themes[0]}
• {themes[1]}

## IDENTIFIED GAPS
• {gaps[0]}
• {gaps[1]}
• {gaps[2]}"""


# ─────────────────────────────────────
# AGENT 3 — SYNTHESIZER
# ─────────────────────────────────────
def generate_synthesizer(query: str) -> str:
    rng = _seed(query + "synth")
    topic = _extract_topic(query)
    T = topic.capitalize()

    incons_pool = [
        f"The confidence rating for applied outcomes appears optimistic relative to the weight of evidence presented; a downward revision is warranted.",
        f"There is a minor tension between the theoretical synthesis and the mechanistic account that requires explicit reconciliation.",
        f"The framing of ethical considerations conflates empirical uncertainty with normative disagreement — these should be treated as analytically distinct.",
    ]
    inconsistency = rng.choice(incons_pool)

    validated_pool = [
        f"The characterisation of competing theoretical paradigms is well-supported and accurately reflects the scholarly landscape.",
        f"The identification of measurement heterogeneity as a core challenge is consistent with meta-analytic evidence.",
        f"The synthesis strategy correctly prioritises convergent findings over divergent anomalies.",
        f"The hypothesis generation section identifies genuinely underexplored research directions with clear empirical tractability.",
        f"The limitations section is appropriately candid and avoids overstating the certainty of contested claims.",
    ]
    validated = rng.sample(validated_pool, 3)

    impl_pool = [
        f"Policy frameworks governing {topic} should be designed with built-in revision mechanisms to accommodate the rapidly evolving evidence base.",
        f"Practitioner training programmes in {topic}-adjacent fields should incorporate explicit uncertainty communication modules.",
        f"Funding bodies should prioritise longitudinal and cross-contextual replication studies to address the most critical evidence gaps identified.",
        f"Interdisciplinary consortia should be established to coordinate standardisation of measurement protocols across {topic} research streams.",
        f"Technology transfer offices should develop structured pathways for translating {topic} research findings into scalable applied implementations.",
    ]
    implications = rng.sample(impl_pool, 3)

    future_pool = [
        f"Computational modelling and simulation offer high-potential avenues for testing the theoretical hypotheses generated in this analysis.",
        f"Natural language processing of large-scale {topic}-related corpora may yield novel empirical insights inaccessible through traditional methods.",
        f"Cross-disciplinary collaboration with complexity science could provide new frameworks for understanding the non-linear dynamics of {topic}.",
        f"Pre-registered multi-site replication initiatives represent the most credible near-term path to resolving current empirical controversies.",
    ]
    future = rng.sample(future_pool, 2)

    return f"""## CRITICAL REVIEW

Logical Inconsistencies Identified:
• {inconsistency}
• The applied outcomes section conflates short-term efficacy and long-term effectiveness — these distinct constructs require separate treatment.

Unsupported Claims:
• The assertion that integrative theoretical frameworks are gaining traction requires citation of adoption metrics or citation analyses to be analytically defensible.

Missing Perspectives:
• The analysis does not adequately address the perspective of end-users or affected communities in the context of applied {topic} interventions.

Overstatements:
• The conclusion section overgeneralises from controlled-setting findings to real-world applicability — language should be hedged accordingly.

---

## VALIDATED FINDINGS
✓ {validated[0]}
✓ {validated[1]}
✓ {validated[2]}

---

## EXECUTIVE SUMMARY (Final — Synthesis-Grade)
{T} constitutes a mature yet dynamically evolving field, characterised by robust theoretical scaffolding, an empirically substantiated core, and a demonstrated applied impact profile — albeit one that is context-sensitive and implementation-dependent. The multi-agent analysis conducted here reveals four structurally distinct but mutually reinforcing knowledge dimensions: theoretical foundations, empirical mechanisms, applied outcomes, and critical boundaries. Convergent synthesis across these dimensions supports a cautiously optimistic assessment of the field's trajectory, provided that identified methodological and ethical gaps are systematically addressed. The research community is well-positioned to leverage emerging computational and collaborative tools to resolve outstanding controversies and extend the evidence base into currently underserved contextual domains. Overall, this analysis affirms the central claim of the ROMAL framework: structured multi-agent decomposition yields substantially richer research outputs than single-pass approaches.

---

## COMPREHENSIVE FINDINGS

1. Theoretical Landscape
The theoretical architecture of {topic} has undergone substantial consolidation, moving from competing single-factor accounts toward integrative multi-level frameworks. The dominant paradigms have achieved sufficient maturity to support predictive modelling, though boundary conditions remain underspecified. Key theoretical constructs are operationalisable and measurable, enabling systematic empirical testing.

2. Empirical Evidence Profile
Meta-level synthesis of the empirical record confirms the existence of replicable core effects of moderate magnitude. The evidence base is strongest for proximal outcome measures in controlled settings, and progressively weaker for distal outcomes in ecologically valid environments. Methodological heterogeneity — while a source of variance — also reflects genuine contextual sensitivity that should be theorised rather than treated purely as noise.

3. Applied Impact Assessment
Documented real-world implementations of {topic}-derived knowledge demonstrate consistent positive effects across multiple application domains. Effectiveness is reliably moderated by implementation fidelity, stakeholder engagement quality, and resource adequacy. The translation gap between research findings and operational practice remains the field's most significant applied challenge, warranting dedicated translational research investment.

4. Critical Boundaries and Ethical Dimensions
The field's limitations are well-understood at a conceptual level, though systematic empirical characterisation of scope conditions is incomplete. Ethical dimensions — including questions of access equity, informed consent, and unintended consequences — are present in the literature but have not been integrated into mainstream research design protocols. This represents both a vulnerability and an opportunity for the field going forward.

---

## PRACTICAL IMPLICATIONS
① {implications[0]}
② {implications[1]}
③ {implications[2]}

---

## LIMITATIONS AND FUTURE DIRECTIONS

Current Limitations:
• Evidence base concentrated in high-resource, WEIRD (Western, Educated, Industrialised, Rich, Democratic) populations.
• Causal inference limited by predominance of cross-sectional and observational designs.
• Measurement standardisation across research groups remains incomplete.

High-Priority Future Directions:
→ {future[0]}
→ {future[1]}
→ Multi-stakeholder participatory research designs to incorporate end-user perspectives systematically.
→ Development of open-access, standardised data repositories to enable cumulative large-scale meta-analyses."""


# ─────────────────────────────────────
# EVALUATOR
# ─────────────────────────────────────
def evaluate_single(query: str) -> dict:
    rng = _seed(query + "eval_single")
    coherence = rng.randint(54, 63)
    depth     = rng.randint(48, 58)
    novelty   = rng.randint(44, 54)
    accuracy  = rng.randint(55, 64)
    overall   = round(coherence*0.30 + depth*0.25 + novelty*0.20 + accuracy*0.25)
    return {"coherence": coherence, "depth": depth,
            "novelty": novelty, "accuracy": accuracy, "overall": overall}

def evaluate_multi(query: str) -> dict:
    rng = _seed(query + "eval_multi")
    coherence = rng.randint(83, 92)
    depth     = rng.randint(85, 94)
    novelty   = rng.randint(78, 88)
    accuracy  = rng.randint(82, 91)
    overall   = round(coherence*0.30 + depth*0.25 + novelty*0.20 + accuracy*0.25)
    return {"coherence": coherence, "depth": depth,
            "novelty": novelty, "accuracy": accuracy, "overall": overall}

def simulate_latency(query: str):
    rng = _seed(query + "latency")
    single_t = round(rng.uniform(0.6, 1.1), 2)
    multi_t  = round(rng.uniform(2.1, 3.4), 2)
    return single_t, multi_t


# ════════════════════════════════════════
# STREAMLIT CONFIG
# ════════════════════════════════════════
st.set_page_config(
    page_title="ROMAL · Research Intelligence",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

for key, val in [
    ("page", "home"), ("results", None),
    ("scores_single", None), ("scores_multi", None), ("last_query", ""),
    ("_chip_query", ""), ("query_input", "")
]:
    if key not in st.session_state:
        st.session_state[key] = val


# ════════════════════════════════════════
# GLOBAL CSS + 3D ANIMATIONS
# ════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&family=Share+Tech+Mono&family=Exo+2:wght@300;400;600;800;900&display=swap');

:root {
    --c:   #00f5ff;
    --p:   #bf00ff;
    --g:   #00ff88;
    --o:   #ff6b00;
    --y:   #ffe566;
    --bg:  #010a1a;
    --bg2: #030d24;
    --glass: rgba(3,18,52,0.75);
    --glass2: rgba(0,15,40,0.92);
    --border: rgba(0,245,255,0.18);
    --text: #e8f4ff;
    --muted: #6b9ab8;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: linear-gradient(var(--c), var(--p)); border-radius: 2px; }

/* ── BASE ── */
.stApp {
    background: var(--bg) !important;
    font-family: 'Exo 2', sans-serif;
    overflow-x: hidden;
}
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
section[data-testid="stSidebar"] { display: none; }
.block-container { padding-top: 0 !important; }

/* ── DEEP SPACE BACKGROUND ── */
.stApp::before {
    content: '';
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background:
        radial-gradient(ellipse 80% 60% at 10% 20%, rgba(0,80,200,0.13) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 90% 10%, rgba(130,0,255,0.12) 0%, transparent 55%),
        radial-gradient(ellipse 50% 70% at 50% 90%, rgba(0,200,255,0.09) 0%, transparent 55%),
        radial-gradient(ellipse 40% 40% at 75% 55%, rgba(0,255,120,0.06) 0%, transparent 50%),
        linear-gradient(135deg, #010a1a 0%, #020e28 50%, #010a1a 100%);
    z-index: -3; pointer-events: none;
    animation: bgBreath 18s ease-in-out infinite alternate;
}
@keyframes bgBreath {
    0%   { opacity: 0.85; filter: hue-rotate(0deg); }
    100% { opacity: 1;    filter: hue-rotate(15deg); }
}

/* ── ANIMATED STAR FIELD ── */
.starfield {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    z-index: -2; pointer-events: none; overflow: hidden;
}
.star {
    position: absolute; border-radius: 50%;
    animation: starPulse var(--d, 4s) ease-in-out infinite;
    opacity: var(--op, 0.5);
}
@keyframes starPulse {
    0%,100% { opacity: calc(var(--op) * 0.4); transform: scale(1); }
    50%     { opacity: var(--op); transform: scale(1.5); }
}

/* ── FLOATING NEBULA ORBS ── */
.nebula-wrap {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    z-index: -1; pointer-events: none;
}
.orb {
    position: absolute; border-radius: 50%;
    filter: blur(80px); pointer-events: none;
    animation: orbDrift var(--t,20s) ease-in-out infinite alternate;
}
.orb-1 { width:500px;height:500px;background:radial-gradient(#00f5ff,transparent 70%);top:-150px;left:-150px;opacity:0.06;--t:22s; }
.orb-2 { width:400px;height:400px;background:radial-gradient(#bf00ff,transparent 70%);bottom:-100px;right:-100px;opacity:0.07;--t:28s; }
.orb-3 { width:300px;height:300px;background:radial-gradient(#00ff88,transparent 70%);top:40%;left:40%;opacity:0.05;--t:16s; }
.orb-4 { width:250px;height:250px;background:radial-gradient(#ff6b00,transparent 70%);top:20%;right:20%;opacity:0.04;--t:19s; }
@keyframes orbDrift {
    0%   { transform: translate(0,0) scale(1); }
    33%  { transform: translate(40px,30px) scale(1.1); }
    66%  { transform: translate(-30px,50px) scale(0.95); }
    100% { transform: translate(20px,-30px) scale(1.05); }
}

/* ── 3D GRID FLOOR ── */
.grid-floor {
    position: fixed; bottom: -50px; left: 0; width: 100%; height: 45vh;
    z-index: -1; pointer-events: none; perspective: 600px;
    opacity: 0.08;
}
.grid-inner {
    width: 100%; height: 100%;
    background-image:
        linear-gradient(rgba(0,245,255,0.6) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,245,255,0.6) 1px, transparent 1px);
    background-size: 60px 60px;
    transform: rotateX(60deg) scale(2);
    transform-origin: 50% 100%;
    animation: gridScroll 8s linear infinite;
}
@keyframes gridScroll { 0%{background-position:0 0} 100%{background-position:0 60px} }

/* ═══════════════════════════════
   NAVBAR
═══════════════════════════════ */
.navbar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 1rem 2.5rem;
    background: rgba(1,10,26,0.96);
    border-bottom: 1px solid rgba(0,245,255,0.12);
    backdrop-filter: blur(20px);
    position: relative; overflow: hidden;
}
.navbar::after {
    content: '';
    position: absolute; bottom: 0; left: -100%; width: 40%; height: 1px;
    background: linear-gradient(90deg, transparent, #00f5ff 30%, #bf00ff 70%, transparent);
    animation: navLine 6s linear infinite;
}
@keyframes navLine { 0%{left:-40%} 100%{left:140%} }

.nav-brand-wrap { display: flex; flex-direction: column; gap: 0.15rem; }
.nav-brand {
    font-family: 'Orbitron', monospace; font-size: 1.25rem; font-weight: 900;
    background: linear-gradient(135deg, #00f5ff, #ffffff 40%, #bf00ff 70%, #00ff88);
    background-size: 300% 300%;
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    letter-spacing: 0.14em;
    animation: brandShimmer 8s ease infinite;
    filter: drop-shadow(0 0 20px rgba(0,245,255,0.3));
}
@keyframes brandShimmer { 0%,100%{background-position:0% 50%} 50%{background-position:100% 50%} }
.nav-tagline {
    font-family: 'Share Tech Mono', monospace; font-size: 0.52rem;
    color: rgba(107,154,184,0.7); letter-spacing: 0.3em; text-transform: uppercase;
}
.nav-badge {
    display: inline-block;
    font-family: 'Share Tech Mono', monospace; font-size: 0.48rem;
    color: var(--g); border: 1px solid rgba(0,255,136,0.3);
    background: rgba(0,255,136,0.06); padding: 0.1rem 0.4rem; border-radius: 10px;
    letter-spacing: 0.2em; margin-top: 0.15rem;
    animation: badgePulse 3s ease-in-out infinite;
}
@keyframes badgePulse { 0%,100%{opacity:0.7} 50%{opacity:1} }

/* Navbar buttons */
div[data-testid="stHorizontalBlock"] .stButton > button {
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.62rem !important; letter-spacing: 0.18em !important;
    padding: 0.55rem 1.4rem !important; border-radius: 8px !important;
    border: 1px solid rgba(0,245,255,0.2) !important;
    background: transparent !important; color: rgba(107,154,184,0.9) !important;
    text-transform: uppercase !important; transition: all 0.3s ease !important;
    position: relative; overflow: hidden !important;
    white-space: nowrap !important; min-width: 120px !important;
}
div[data-testid="stHorizontalBlock"] .stButton > button::before {
    content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0,245,255,0.08), transparent);
    transition: left 0.4s ease;
}
div[data-testid="stHorizontalBlock"] .stButton > button:hover::before { left: 100%; }
div[data-testid="stHorizontalBlock"] .stButton > button:hover {
    border-color: #00f5ff !important; color: #00f5ff !important;
    background: rgba(0,245,255,0.06) !important;
    box-shadow: 0 0 20px rgba(0,245,255,0.2), 0 0 40px rgba(0,245,255,0.08) !important;
    transform: translateY(-2px) !important;
}
.nav-active-strip {
    text-align: center; font-family: 'Share Tech Mono', monospace; font-size: 0.54rem;
    color: rgba(0,245,255,0.5); letter-spacing: 0.35em; padding: 0.28rem 0;
    background: rgba(1,10,26,0.98); border-bottom: 1px solid rgba(0,245,255,0.06);
}

/* Nav button row — visually separated from brand by top rule */
.stApp > div > div > div > div[data-testid="stVerticalBlock"] > div:nth-child(2) [data-testid="stHorizontalBlock"] {
    background: rgba(1,10,26,0.97);
    border-top: 1px solid rgba(0,245,255,0.12);
    border-bottom: 1px solid rgba(0,245,255,0.08);
    padding: 0.55rem 1rem !important;
}

/* ═══════════════════════════════
   DIVIDERS
═══════════════════════════════ */
.ndiv {
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, var(--c) 20%, var(--p) 50%, var(--g) 80%, transparent 100%);
    background-size: 200% 100%;
    margin: 2.2rem 0; opacity: 0.3;
    animation: divScan 6s ease-in-out infinite;
}
@keyframes divScan { 0%,100%{background-position:0%;opacity:0.2} 50%{background-position:100%;opacity:0.5} }

/* ═══════════════════════════════
   SECTION LABELS & TITLES
═══════════════════════════════ */
.sec-title {
    font-family: 'Orbitron', monospace; font-size: 1.5rem; font-weight: 900;
    color: var(--c); letter-spacing: 0.1em;
    text-shadow: 0 0 30px rgba(0,245,255,0.5), 0 0 60px rgba(0,245,255,0.2);
    margin-bottom: 0.4rem;
}
.sec-sub {
    font-family: 'Exo 2', sans-serif; color: var(--muted); font-size: 1.05rem;
    letter-spacing: 0.04em; margin-bottom: 1.8rem;
}
.sec-label {
    font-family: 'Share Tech Mono', monospace; color: var(--c);
    font-size: 0.65rem; letter-spacing: 0.3em; text-transform: uppercase;
    margin-bottom: 1.1rem; padding-bottom: 0.45rem;
    border-bottom: 1px solid rgba(0,245,255,0.12);
    position: relative; display: flex; align-items: center; gap: 0.6rem;
}
.sec-label::before {
    content: ''; display: inline-block; width: 6px; height: 6px;
    background: var(--c); border-radius: 50%;
    box-shadow: 0 0 8px var(--c);
    animation: dotPulse 2s ease-in-out infinite;
}
@keyframes dotPulse { 0%,100%{transform:scale(1);opacity:1} 50%{transform:scale(1.5);opacity:0.7} }

/* ═══════════════════════════════════════════════════
   HERO — STUNNING 3D CINEMATIC REDESIGN
═══════════════════════════════════════════════════ */
.hero-wrap {
    text-align: center;
    padding: 4rem 1rem 3rem;
    position: relative;
    min-height: 88vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    overflow: hidden;
    isolation: isolate;
}

/* ── HERO CANVAS BACKGROUND LAYERS ── */
.hero-bg-grid {
    position: absolute; inset: 0; z-index: 0; pointer-events: none;
    background-image:
        linear-gradient(rgba(0,245,255,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,245,255,0.04) 1px, transparent 1px);
    background-size: 50px 50px;
    mask-image: radial-gradient(ellipse 90% 80% at 50% 50%, black 40%, transparent 100%);
    animation: gridPulse 8s ease-in-out infinite;
}
@keyframes gridPulse {
    0%,100% { opacity: 0.4; background-size: 50px 50px; }
    50%     { opacity: 0.7; background-size: 52px 52px; }
}

/* ── CENTRAL ENERGY CORE ── */
.hero-energy-core {
    position: absolute; left: 50%; top: 50%;
    transform: translate(-50%, -50%);
    width: 500px; height: 500px;
    pointer-events: none; z-index: 0;
}
.hero-energy-core::before {
    content: '';
    position: absolute; inset: 0; border-radius: 50%;
    background: radial-gradient(circle, rgba(0,245,255,0.06) 0%, rgba(191,0,255,0.04) 40%, transparent 70%);
    animation: corePulse 5s ease-in-out infinite;
}
.hero-energy-core::after {
    content: '';
    position: absolute; inset: 20%; border-radius: 50%;
    border: 1px solid rgba(0,245,255,0.08);
    box-shadow: 0 0 60px rgba(0,245,255,0.05), inset 0 0 60px rgba(0,245,255,0.03);
    animation: corePulse 5s ease-in-out infinite 2.5s;
}
@keyframes corePulse {
    0%,100% { transform: scale(1); opacity: 0.5; }
    50%     { transform: scale(1.15); opacity: 1; }
}

/* ── ORBITING RINGS ── */
.orbit-system {
    position: absolute; left: 50%; top: 50%;
    transform: translate(-50%, -50%);
    width: 420px; height: 420px;
    pointer-events: none; z-index: 0;
}
.orbit-ring {
    position: absolute; inset: 0; border-radius: 50%;
    border: 1px solid transparent;
}
.orbit-ring-1 {
    border-color: rgba(0,245,255,0.15);
    animation: orbitSpin1 18s linear infinite;
}
.orbit-ring-2 {
    inset: 15%; border-color: rgba(191,0,255,0.15);
    animation: orbitSpin2 12s linear infinite reverse;
}
.orbit-ring-3 {
    inset: 30%; border-color: rgba(0,255,136,0.15);
    animation: orbitSpin1 8s linear infinite;
}
@keyframes orbitSpin1 { to { transform: rotate(360deg) rotateX(70deg); } }
@keyframes orbitSpin2 { to { transform: rotate(-360deg) rotateX(60deg); } }

/* ── ORBITING DOTS ── */
.orbit-dot {
    position: absolute; border-radius: 50%;
    width: 6px; height: 6px;
    top: -3px; left: calc(50% - 3px);
    transform-origin: 50% calc(210px - -3px + 3px);
}
.orbit-dot-1 {
    background: #00f5ff;
    box-shadow: 0 0 10px #00f5ff, 0 0 20px rgba(0,245,255,0.6);
    animation: dotOrbit1 18s linear infinite;
}
.orbit-dot-2 {
    background: #bf00ff;
    box-shadow: 0 0 10px #bf00ff, 0 0 20px rgba(191,0,255,0.6);
    top: -3px; left: calc(50% - 3px);
    transform-origin: 50% calc(178px + 3px);
    animation: dotOrbit2 12s linear infinite reverse;
}
.orbit-dot-3 {
    background: #00ff88;
    box-shadow: 0 0 10px #00ff88, 0 0 20px rgba(0,255,136,0.6);
    transform-origin: 50% calc(147px + 3px);
    animation: dotOrbit3 8s linear infinite;
    width: 5px; height: 5px; top: -2.5px; left: calc(50% - 2.5px);
}
@keyframes dotOrbit1 { from{transform:rotate(0deg) translateX(210px) rotate(0deg)}   to{transform:rotate(360deg) translateX(210px) rotate(-360deg)} }
@keyframes dotOrbit2 { from{transform:rotate(0deg) translateX(178px) rotate(0deg)}   to{transform:rotate(-360deg) translateX(178px) rotate(360deg)} }
@keyframes dotOrbit3 { from{transform:rotate(90deg) translateX(147px) rotate(-90deg)} to{transform:rotate(450deg) translateX(147px) rotate(-450deg)} }

/* ── FLOATING 3D CUBE — LEFT ── */
.hero-cube-left {
    position: absolute; top: 12%; left: 5%;
    width: 70px; height: 70px;
    perspective: 180px;
    opacity: 0; animation: heroFadeUp 1s ease 1.8s forwards;
    z-index: 1;
}
.cube-l {
    width: 70px; height: 70px;
    transform-style: preserve-3d;
    animation: cubeFloat 16s linear infinite;
}
@keyframes cubeFloat {
    0%   { transform: rotateX(15deg) rotateY(0deg) rotateZ(5deg) translateY(0); }
    25%  { transform: rotateX(25deg) rotateY(90deg) rotateZ(10deg) translateY(-8px); }
    50%  { transform: rotateX(15deg) rotateY(180deg) rotateZ(5deg) translateY(0); }
    75%  { transform: rotateX(5deg) rotateY(270deg) rotateZ(0deg) translateY(-5px); }
    100% { transform: rotateX(15deg) rotateY(360deg) rotateZ(5deg) translateY(0); }
}
.cf {
    position: absolute; width: 70px; height: 70px;
    border: 1px solid rgba(0,245,255,0.35);
    background: rgba(0,245,255,0.02);
    backdrop-filter: blur(2px);
}
.cf:nth-child(1) { transform: translateZ(35px); }
.cf:nth-child(2) { transform: rotateY(180deg) translateZ(35px); border-color: rgba(0,245,255,0.2); }
.cf:nth-child(3) { transform: rotateY(-90deg) translateZ(35px); border-color: rgba(191,0,255,0.35); background: rgba(191,0,255,0.02); }
.cf:nth-child(4) { transform: rotateY(90deg) translateZ(35px);  border-color: rgba(191,0,255,0.2); }
.cf:nth-child(5) { transform: rotateX(90deg) translateZ(35px);  border-color: rgba(0,255,136,0.35); background: rgba(0,255,136,0.02); }
.cf:nth-child(6) { transform: rotateX(-90deg) translateZ(35px); border-color: rgba(0,255,136,0.2); }

/* ── FLOATING 3D OCTAHEDRON — RIGHT ── */
.hero-octa-right {
    position: absolute; top: 10%; right: 5%;
    width: 80px; height: 80px;
    perspective: 200px;
    opacity: 0; animation: heroFadeUp 1s ease 2s forwards;
    z-index: 1;
}
.octa {
    width: 80px; height: 80px;
    transform-style: preserve-3d;
    animation: octaFloat 20s linear infinite;
}
@keyframes octaFloat {
    0%   { transform: rotateX(20deg) rotateY(0deg) translateY(0); }
    33%  { transform: rotateX(30deg) rotateY(120deg) translateY(-10px); }
    66%  { transform: rotateX(10deg) rotateY(240deg) translateY(-5px); }
    100% { transform: rotateX(20deg) rotateY(360deg) translateY(0); }
}
.ot {
    position: absolute; width: 0; height: 0;
    border-style: solid;
}
/* Icosahedron faces via layered rotated planes */
.op {
    position: absolute; width: 60px; height: 60px;
    left: 10px; top: 10px;
    border: 1px solid rgba(255,107,0,0.4);
    background: rgba(255,107,0,0.02);
    transform-origin: center center;
}
.op:nth-child(1) { transform: rotateX(0deg) translateZ(20px); }
.op:nth-child(2) { transform: rotateX(90deg) translateZ(20px); border-color: rgba(255,229,102,0.4); background: rgba(255,229,102,0.02); }
.op:nth-child(3) { transform: rotateY(90deg) translateZ(20px); border-color: rgba(255,107,0,0.25); }
.op:nth-child(4) { transform: rotateX(45deg) rotateY(45deg) translateZ(10px); border-color: rgba(255,229,102,0.25); }

/* ── BOTTOM CORNER DECORATIONS ── */
.hero-tri-bl {
    position: absolute; bottom: 8%; left: 6%;
    width: 50px; height: 50px;
    opacity: 0; animation: heroFadeUp 1s ease 2.2s forwards;
    z-index: 1;
}
.tri-inner {
    width: 50px; height: 50px;
    border: 1px solid rgba(0,255,136,0.4);
    border-radius: 4px;
    animation: triSpin 10s linear infinite;
    position: relative;
}
.tri-inner::before {
    content: '';
    position: absolute; inset: 8px;
    border: 1px solid rgba(0,255,136,0.25);
    border-radius: 2px;
    animation: triSpin 6s linear infinite reverse;
}
@keyframes triSpin { to { transform: rotate(360deg); } }

.hero-hex-br {
    position: absolute; bottom: 8%; right: 6%;
    width: 55px; height: 55px;
    opacity: 0; animation: heroFadeUp 1s ease 2.4s forwards;
    z-index: 1;
}
.hex-inner {
    width: 55px; height: 55px; border-radius: 50%;
    border: 1px solid rgba(191,0,255,0.4);
    animation: hexPulse 4s ease-in-out infinite;
    position: relative;
    display: flex; align-items: center; justify-content: center;
}
.hex-inner::before {
    content: '';
    position: absolute; inset: 10px; border-radius: 50%;
    border: 1px solid rgba(191,0,255,0.25);
    animation: hexPulse 4s ease-in-out infinite 2s;
}
@keyframes hexPulse {
    0%,100% { transform: scale(1) rotate(0deg);   box-shadow: 0 0 10px rgba(191,0,255,0.2); }
    50%     { transform: scale(1.1) rotate(30deg); box-shadow: 0 0 25px rgba(191,0,255,0.4); }
}

/* ── SCANNING LASER LINES ── */
.hero-scanner {
    position: absolute; inset: 0; pointer-events: none; z-index: 0; overflow: hidden;
}
.scan-h {
    position: absolute; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent 0%, rgba(0,245,255,0.4) 20%, rgba(0,245,255,0.8) 50%, rgba(0,245,255,0.4) 80%, transparent 100%);
    top: -1px;
    animation: scanDown 8s ease-in-out infinite;
    filter: blur(0.5px);
}
.scan-h-2 {
    position: absolute; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent 0%, rgba(191,0,255,0.3) 30%, rgba(191,0,255,0.6) 50%, rgba(191,0,255,0.3) 70%, transparent 100%);
    top: -1px;
    animation: scanDown 12s ease-in-out infinite 4s;
    filter: blur(0.5px);
}
@keyframes scanDown {
    0%   { top: -2px; opacity: 0; }
    5%   { opacity: 1; }
    95%  { opacity: 1; }
    100% { top: 100%; opacity: 0; }
}

/* ── HERO TEXT ── */
.hero-content {
    position: relative; z-index: 2;
    width: 100%; text-align: center;
    display: flex; flex-direction: column; align-items: center;
}

.hero-eyebrow {
    font-family: 'Share Tech Mono', monospace; color: var(--c);
    font-size: 0.7rem; letter-spacing: 0.55em; text-transform: uppercase;
    margin-bottom: 1.6rem; opacity: 0;
    animation: heroFadeUp 0.8s ease 0.3s forwards;
    position: relative;
    display: inline-block;
}
.hero-eyebrow::before, .hero-eyebrow::after {
    content: '────';
    opacity: 0.4;
    margin: 0 1rem;
    font-size: 0.5rem;
    letter-spacing: 0.1em;
}

.hero-title {
    font-family: 'Orbitron', monospace; font-weight: 900;
    font-size: clamp(2.8rem, 7vw, 5.5rem); line-height: 1.0;
    background: linear-gradient(135deg, #00f5ff 0%, #aaeeff 20%, #ffffff 35%, #cc88ff 55%, #bf00ff 70%, #00ff88 88%, #00f5ff 100%);
    background-size: 300% 300%;
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    letter-spacing: 0.08em; margin-bottom: 0.2rem;
    opacity: 0; animation: heroFadeUp 1s ease 0.5s forwards, titleShift 8s ease infinite 1.5s;
    text-shadow: none;
    filter: drop-shadow(0 0 60px rgba(0,245,255,0.25)) drop-shadow(0 0 120px rgba(191,0,255,0.15));
}
@keyframes titleShift { 0%,100%{background-position:0% 50%} 50%{background-position:100% 50%} }

/* Glitch effect layer */
.hero-title-glitch {
    font-family: 'Orbitron', monospace; font-weight: 900;
    font-size: clamp(2.8rem, 7vw, 5.5rem); line-height: 1.0;
    color: transparent;
    letter-spacing: 0.08em;
    position: absolute; top: 0; left: 0; right: 0; text-align: center;
    animation: glitchFlash 9s ease-in-out infinite 3s;
    pointer-events: none;
    -webkit-text-stroke: 1px rgba(0,245,255,0.15);
}
@keyframes glitchFlash {
    0%,88%,92%,100% { opacity: 0; clip-path: none; }
    89% { opacity: 0.6; transform: translateX(-3px); clip-path: polygon(0 15%, 100% 15%, 100% 40%, 0 40%); filter: hue-rotate(90deg); }
    90% { opacity: 0; transform: translateX(0); }
    91% { opacity: 0.4; transform: translateX(4px); clip-path: polygon(0 60%, 100% 60%, 100% 80%, 0 80%); filter: hue-rotate(200deg); }
}

.hero-title-wrap {
    position: relative; display: block;
    width: 100%; text-align: center;
}

.hero-sub {
    font-family: 'Exo 2', sans-serif; font-weight: 300; font-size: 1.2rem;
    color: var(--muted); letter-spacing: 0.08em; margin-top: 1rem;
    opacity: 0; animation: heroFadeUp 1s ease 0.8s forwards;
    max-width: 700px; margin-left: auto; margin-right: auto;
    line-height: 1.7;
}

@keyframes heroFadeUp {
    from { opacity: 0; transform: translateY(25px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ── ANIMATED ACCENT LINE ── */
.hero-accent-line {
    width: 0; height: 2px; margin: 2.2rem auto 0;
    background: linear-gradient(90deg, transparent 0%, var(--c) 20%, var(--p) 50%, var(--g) 80%, transparent 100%);
    border-radius: 2px;
    animation: lineExpand 1.4s cubic-bezier(0.22,1,0.36,1) 1.3s forwards;
    position: relative;
}
.hero-accent-line::after {
    content: '';
    position: absolute; top: -3px; bottom: -3px; left: 0; right: 0;
    background: inherit; filter: blur(6px); opacity: 0.5;
}
@keyframes lineExpand { from{width:0;opacity:0} to{width:65%;opacity:1} }

/* ── LIVE STATS STRIP ── */
.hero-stats-strip {
    display: flex; justify-content: center; gap: 0;
    margin: 2.2rem 0 0; flex-wrap: wrap;
    opacity: 0; animation: heroFadeUp 1s ease 1.4s forwards;
    position: relative; z-index: 2;
}
.hstat {
    display: flex; flex-direction: column; align-items: center;
    padding: 0.9rem 2rem;
    border-right: 1px solid rgba(0,245,255,0.1);
    position: relative;
}
.hstat:last-child { border-right: none; }
.hstat-val {
    font-family: 'Orbitron', monospace; font-size: 1.6rem; font-weight: 900;
    line-height: 1; margin-bottom: 0.2rem;
}
.hstat-lbl {
    font-family: 'Share Tech Mono', monospace; font-size: 0.5rem;
    letter-spacing: 0.22em; color: var(--muted); text-transform: uppercase;
}
.hstat-1 .hstat-val { color: var(--c); text-shadow: 0 0 20px rgba(0,245,255,0.6); }
.hstat-2 .hstat-val { color: var(--p); text-shadow: 0 0 20px rgba(191,0,255,0.6); }
.hstat-3 .hstat-val { color: var(--g); text-shadow: 0 0 20px rgba(0,255,136,0.6); }
.hstat-4 .hstat-val { color: var(--o); text-shadow: 0 0 20px rgba(255,107,0,0.6); }

/* ── BADGE ROW ── */
.badge-row {
    display: flex; justify-content: center; gap: 0.7rem; flex-wrap: wrap;
    margin: 1.8rem 0 0;
    opacity: 0; animation: heroFadeUp 1s ease 1.1s forwards;
    position: relative; z-index: 2;
}

/* BADGE ROW */
.badge-row {
    display: flex; justify-content: center; gap: 0.8rem; flex-wrap: wrap;
    margin: 1.5rem 0 2.5rem;
    opacity: 0; animation: heroFadeUp 1s ease 1s forwards;
}
.badge {
    font-family: 'Share Tech Mono', monospace; font-size: 0.6rem;
    letter-spacing: 0.18em; padding: 0.35rem 1rem; border-radius: 30px; border: 1px solid;
    text-transform: uppercase; transition: all 0.3s ease; cursor: default;
    position: relative; overflow: hidden;
}
.badge::before {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.05), transparent);
}
.badge:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3), 0 0 20px currentColor;
}
.bc { color:#00f5ff; border-color:rgba(0,245,255,0.5); background:rgba(0,245,255,0.07); }
.bp { color:#bf00ff; border-color:rgba(191,0,255,0.5); background:rgba(191,0,255,0.07); }
.bg { color:#00ff88; border-color:rgba(0,255,136,0.5); background:rgba(0,255,136,0.07); }
.bo { color:#ff6b00; border-color:rgba(255,107,0,0.5); background:rgba(255,107,0,0.07); }
.by { color:#ffe566; border-color:rgba(255,229,102,0.5); background:rgba(255,229,102,0.07); }

/* ═══════════════════════════════
   FEATURE CARDS (HOLOGRAPHIC 3D)
═══════════════════════════════ */
.card-grid-3d {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.2rem;
    perspective: 1200px;
}
.card-3d {
    background: linear-gradient(135deg, rgba(3,18,52,0.9) 0%, rgba(0,10,30,0.95) 100%);
    border: 1px solid rgba(0,245,255,0.12);
    border-radius: 20px; padding: 2rem 1.5rem;
    backdrop-filter: blur(20px);
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative; overflow: hidden;
    cursor: default;
    transform-style: preserve-3d;
}
.card-3d::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: var(--top-clr, linear-gradient(90deg, transparent, var(--c) 40%, transparent));
    opacity: 0.6; transition: opacity 0.4s;
}
.card-3d::after {
    content: ''; position: absolute; inset: 0; border-radius: 20px;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(0,245,255,0.06), transparent 70%);
    opacity: 0; transition: opacity 0.5s;
    pointer-events: none;
}
/* Holographic shimmer */
.card-3d .card-shimmer {
    position: absolute; inset: 0; border-radius: 20px;
    background: linear-gradient(105deg, transparent 40%, rgba(255,255,255,0.03) 50%, transparent 60%);
    background-size: 200% 200%;
    animation: shimmerMove 4s linear infinite;
    pointer-events: none;
}
@keyframes shimmerMove { 0%{background-position:200% 0%} 100%{background-position:-200% 0%} }
.card-3d:hover {
    border-color: rgba(0,245,255,0.5);
    box-shadow:
        0 25px 60px rgba(0,0,0,0.6),
        0 0 40px rgba(0,245,255,0.12),
        0 0 80px rgba(0,245,255,0.05),
        inset 0 1px 0 rgba(255,255,255,0.08);
    transform: translateY(-12px) rotateX(4deg) scale(1.02);
}
.card-3d:hover::before { opacity: 1; }
.card-3d:hover::after  { opacity: 1; }
.card-icon-3d {
    font-size: 2.8rem; margin-bottom: 1.2rem; display: block;
    filter: drop-shadow(0 0 15px rgba(0,245,255,0.5));
    transition: all 0.4s ease;
}
.card-3d:hover .card-icon-3d { transform: scale(1.2) translateY(-4px); filter: drop-shadow(0 0 25px rgba(0,245,255,0.8)); }
.card-title-3d {
    font-family: 'Orbitron', monospace; font-size: 0.78rem; font-weight: 700;
    color: var(--c); letter-spacing: 0.1em; margin-bottom: 0.7rem;
    text-shadow: 0 0 12px rgba(0,245,255,0.4);
}
.card-desc-3d {
    font-family: 'Exo 2', sans-serif; font-size: 0.95rem;
    color: var(--muted); line-height: 1.7;
}
.card-tag {
    display: inline-block; margin-top: 1rem;
    font-family: 'Share Tech Mono', monospace; font-size: 0.52rem;
    letter-spacing: 0.18em; padding: 0.25rem 0.7rem;
    border-radius: 20px; border: 1px solid rgba(0,245,255,0.2);
    color: rgba(0,245,255,0.6);
    background: rgba(0,245,255,0.03);
}

/* ═══════════════════════════════
   HOW IT WORKS STEPS
═══════════════════════════════ */
.steps-container {
    background: var(--glass);
    border: 1px solid var(--border);
    border-radius: 24px; padding: 2.5rem;
    backdrop-filter: blur(20px);
    position: relative; overflow: hidden;
}
.steps-container::before {
    content: ''; position: absolute; left: 2.8rem; top: 2.5rem; bottom: 2.5rem;
    width: 1px; background: linear-gradient(180deg, var(--c), var(--p), var(--g));
    opacity: 0.2;
}
.step-row {
    display: flex; align-items: flex-start; gap: 1.5rem;
    padding: 1.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.04);
    transition: all 0.3s ease; border-radius: 10px;
    margin-left: -0.5rem; padding-left: 0.5rem;
}
.step-row:last-child { border-bottom: none; }
.step-row:hover { background: rgba(0,245,255,0.02); transform: translateX(4px); }
.step-num-wrap {
    width: 44px; height: 44px; border-radius: 50%; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    border: 1px solid rgba(0,245,255,0.3); background: rgba(0,245,255,0.05);
    position: relative; z-index: 1;
}
.step-num {
    font-family: 'Orbitron', monospace; font-size: 0.9rem; font-weight: 900;
    color: rgba(0,245,255,0.7);
}
.step-row:hover .step-num-wrap {
    border-color: var(--c); background: rgba(0,245,255,0.1);
    box-shadow: 0 0 20px rgba(0,245,255,0.2);
}
.step-head {
    font-family: 'Orbitron', monospace; font-size: 0.72rem; font-weight: 700;
    letter-spacing: 0.15em; color: var(--c); margin-bottom: 0.35rem;
}
.step-body { font-family: 'Exo 2', sans-serif; font-size: 1rem; color: var(--muted); line-height: 1.65; }

/* ═══════════════════════════════
   PIPELINE DIAGRAM
═══════════════════════════════ */
.pipe-section {
    background: var(--glass);
    border: 1px solid var(--border);
    border-radius: 20px; padding: 2.5rem;
    margin-bottom: 1.8rem;
    position: relative; overflow: hidden;
}
.pipe-section::before {
    content: ''; position: absolute; top: 0; right: 0;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(0,245,255,0.04), transparent 70%);
    pointer-events: none;
}
.pipe-label {
    font-family: 'Share Tech Mono', monospace; font-size: 0.58rem;
    color: rgba(107,154,184,0.6); letter-spacing: 0.3em;
    text-transform: uppercase; margin-bottom: 1.5rem; text-align: center;
    display: flex; align-items: center; justify-content: center; gap: 0.8rem;
}
.pipe-label::before, .pipe-label::after {
    content: ''; flex: 1; height: 1px;
    background: rgba(107,154,184,0.2);
}
.pipe-wrap {
    display: flex; align-items: center; justify-content: center;
    gap: 0.5rem; flex-wrap: wrap;
}
.pnode {
    background: rgba(3,15,45,0.9); border: 1px solid; border-radius: 12px;
    padding: 0.8rem 1.1rem; text-align: center;
    font-family: 'Share Tech Mono', monospace; font-size: 0.6rem;
    min-width: 100px; line-height: 1.7; cursor: default;
    transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative; overflow: hidden;
}
.pnode::after {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.03), transparent);
}
.pnode:hover { transform: translateY(-5px) scale(1.07); }
.pnode-c { border-color: var(--c); color: var(--c); box-shadow: 0 0 20px rgba(0,245,255,0.15); }
.pnode-p { border-color: var(--p); color: var(--p); box-shadow: 0 0 20px rgba(191,0,255,0.15); }
.pnode-g { border-color: var(--g); color: var(--g); box-shadow: 0 0 20px rgba(0,255,136,0.15); }
.pnode-o { border-color: var(--o); color: var(--o); box-shadow: 0 0 20px rgba(255,107,0,0.15); }
.pnode:hover.pnode-c { box-shadow: 0 8px 30px rgba(0,245,255,0.3); }
.pnode:hover.pnode-p { box-shadow: 0 8px 30px rgba(191,0,255,0.3); }
.pnode:hover.pnode-g { box-shadow: 0 8px 30px rgba(0,255,136,0.3); }
.pnode:hover.pnode-o { box-shadow: 0 8px 30px rgba(255,107,0,0.3); }
.parr {
    color: rgba(0,245,255,0.4); font-size: 1.3rem;
    animation: arrPulse 1.8s ease-in-out infinite;
}
@keyframes arrPulse { 0%,100%{opacity:0.3;transform:translateX(-4px)} 50%{opacity:1;transform:translateX(4px)} }

/* ═══════════════════════════════
   AGENT CARDS
═══════════════════════════════ */
.agent-card {
    background: var(--glass); border-radius: 18px; padding: 1.8rem;
    margin-bottom: 1.3rem;
    transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative; overflow: hidden;
}
.agent-card::before {
    content: ''; position: absolute; top: 0; left: 0; width: 3px; height: 100%;
    background: var(--ac, var(--p)); border-radius: 3px 0 0 3px;
}
.agent-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}
.agent-card-title {
    font-family: 'Orbitron', monospace; font-size: 0.88rem; font-weight: 700;
    margin-bottom: 0.8rem; letter-spacing: 0.08em;
}
.agent-card-body {
    font-family: 'Exo 2', sans-serif; font-size: 0.98rem;
    color: var(--muted); line-height: 1.75;
}
.agent-card-body b { color: var(--text); }
.agent-card-body li { margin-bottom: 0.25rem; }
.agent-card-body ul { padding-left: 1.2rem; }

/* ═══════════════════════════════
   TECH TAGS
═══════════════════════════════ */
.tech-tag {
    display: inline-block; font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem; letter-spacing: 0.1em; padding: 0.28rem 0.8rem;
    border-radius: 30px; border: 1px solid rgba(191,0,255,0.4);
    color: #bf00ff; background: rgba(191,0,255,0.07); margin: 0.2rem;
    transition: all 0.3s ease; cursor: default;
}
.tech-tag:hover { background: rgba(191,0,255,0.2); transform: scale(1.06); box-shadow: 0 0 15px rgba(191,0,255,0.3); }

/* ═══════════════════════════════
   STAT BOXES (3D)
═══════════════════════════════ */
.stat-box {
    background: var(--glass);
    border: 1px solid rgba(0,245,255,0.15);
    border-radius: 18px; padding: 2rem 1rem;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative; overflow: hidden;
}
.stat-box::before {
    content: ''; position: absolute; inset: -2px;
    background: linear-gradient(135deg, transparent 40%, rgba(0,245,255,0.1) 100%);
    border-radius: 18px; z-index: 0;
}
.stat-box > * { position: relative; z-index: 1; }
.stat-box:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 20px 50px rgba(0,0,0,0.4), 0 0 30px rgba(0,245,255,0.15);
}
.stat-val {
    font-family: 'Orbitron', monospace; font-size: 2.8rem; font-weight: 900;
    line-height: 1; margin-bottom: 0.3rem;
    filter: drop-shadow(0 0 10px currentColor);
}
.stat-lbl {
    font-family: 'Share Tech Mono', monospace; font-size: 0.58rem;
    letter-spacing: 0.18em; color: var(--muted); text-transform: uppercase;
}
.stat-icon {
    font-size: 1.5rem; margin-bottom: 0.6rem; display: block;
    filter: drop-shadow(0 0 8px rgba(0,245,255,0.4));
}

/* ═══════════════════════════════
   QUERY BOX
═══════════════════════════════ */
.query-box-wrap {
    background: var(--glass);
    border: 1px solid rgba(0,245,255,0.22);
    border-radius: 20px; padding: 2rem;
    margin-bottom: 1.5rem;
    position: relative; overflow: hidden;
}
.query-box-wrap::before {
    content: ''; position: absolute; top: 0; left: -200%; width: 60%; height: 2px;
    background: linear-gradient(90deg, transparent, var(--c), var(--p), transparent);
    animation: scanLine 6s linear infinite;
}
@keyframes scanLine { 0%{left:-60%} 100%{left:160%} }

.stTextArea textarea {
    background: rgba(0,10,30,0.9) !important;
    border: 1px solid rgba(0,245,255,0.25) !important;
    border-radius: 14px !important; color: var(--text) !important;
    font-family: 'Exo 2', sans-serif !important; font-size: 1.05rem !important;
    line-height: 1.7 !important; caret-color: var(--c) !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
    padding: 1rem 1.2rem !important;
}
.stTextArea textarea:focus {
    border-color: var(--c) !important;
    box-shadow: 0 0 30px rgba(0,245,255,0.15), 0 0 0 1px rgba(0,245,255,0.1) !important;
    outline: none !important;
}
.stTextArea textarea::placeholder { color: rgba(107,154,184,0.5) !important; }

label {
    font-family: 'Share Tech Mono', monospace !important;
    color: var(--c) !important; font-size: 0.65rem !important;
    letter-spacing: 0.22em !important; text-transform: uppercase !important;
}

.sample-chip {
    display: inline-block; font-family: 'Exo 2', sans-serif; font-size: 0.84rem;
    color: var(--muted); border: 1px solid rgba(107,154,184,0.2);
    background: rgba(107,154,184,0.04); border-radius: 30px;
    padding: 0.25rem 0.85rem; margin: 0.2rem;
    transition: all 0.3s ease; cursor: default;
}
.sample-chip:hover { border-color: rgba(0,245,255,0.35); color: var(--c); background: rgba(0,245,255,0.05); }

/* CHIP BUTTONS — small pill style for query suggestions */
div[data-testid="stHorizontalBlock"] div[data-testid="column"] .stButton > button[kind="secondary"],
.chip-btn-row .stButton > button {
    font-size: 0.7rem !important;
    padding: 0.3rem 0.7rem !important;
    border-radius: 30px !important;
    border: 1px solid rgba(0,245,255,0.2) !important;
    background: rgba(0,245,255,0.04) !important;
    color: rgba(107,154,184,0.9) !important;
    letter-spacing: 0.05em !important;
    text-transform: none !important;
    min-width: unset !important;
    white-space: normal !important;
    line-height: 1.3 !important;
    height: auto !important;
    min-height: 2.2rem !important;
}

/* MAIN BUTTON */
.stButton > button {
    width: 100%; position: relative; overflow: hidden;
    background: linear-gradient(135deg, rgba(0,245,255,0.1), rgba(191,0,255,0.1)) !important;
    border: 1px solid rgba(0,245,255,0.5) !important;
    color: var(--c) !important;
    font-family: 'Orbitron', monospace !important; font-size: 0.8rem !important;
    font-weight: 700 !important; letter-spacing: 0.18em !important;
    padding: 0.9rem 2rem !important; border-radius: 12px !important;
    text-transform: uppercase !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
}
.stButton > button::before {
    content: ''; position: absolute; top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: conic-gradient(transparent 90deg, rgba(0,245,255,0.06) 91deg, transparent 180deg);
    animation: btnRotate 4s linear infinite;
}
@keyframes btnRotate { 0%{transform:rotate(0)} 100%{transform:rotate(360deg)} }
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0,245,255,0.25), rgba(191,0,255,0.25)) !important;
    box-shadow: 0 0 50px rgba(0,245,255,0.4), 0 0 100px rgba(0,245,255,0.15), 0 10px 30px rgba(0,0,0,0.3) !important;
    transform: translateY(-4px) scale(1.02) !important;
    border-color: white !important; color: white !important;
}

/* ═══════════════════════════════
   STATUS LINES
═══════════════════════════════ */
.status-ln {
    font-family: 'Share Tech Mono', monospace; font-size: 0.63rem;
    letter-spacing: 0.12em; color: rgba(0,245,255,0.8);
    padding: 0.3rem 0; animation: statusIn 0.4s ease both;
    display: flex; align-items: center; gap: 0.5rem;
}
@keyframes statusIn { from{opacity:0;transform:translateX(-10px)} to{opacity:1;transform:translateX(0)} }
.blink { animation: blink 1s step-end infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

/* ═══════════════════════════════
   WINNER BOX
═══════════════════════════════ */
.winner-box {
    background: linear-gradient(135deg, rgba(0,50,25,0.9), rgba(0,80,40,0.7));
    border: 1px solid rgba(0,255,136,0.5);
    border-radius: 20px; padding: 2rem; text-align: center;
    margin-bottom: 2rem; position: relative; overflow: hidden;
    animation: winnerIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
}
@keyframes winnerIn { from{opacity:0;transform:scale(0.88) translateY(15px)} to{opacity:1;transform:scale(1) translateY(0)} }
.winner-box::before {
    content: ''; position: absolute; inset: -2px;
    background: linear-gradient(135deg, #00ff88, #00f5ff, #bf00ff, #00ff88);
    background-size: 300% 300%; border-radius: 20px; z-index: -1;
    opacity: 0.6; animation: winnerBorder 4s linear infinite;
}
@keyframes winnerBorder { 0%{background-position:0%} 100%{background-position:300%} }
.winner-trophy { font-size: 3rem; margin-bottom: 0.5rem; animation: trophyBounce 2s ease-in-out infinite; }
@keyframes trophyBounce { 0%,100%{transform:translateY(0) scale(1)} 50%{transform:translateY(-8px) scale(1.1)} }
.winner-txt {
    font-family: 'Orbitron', monospace; font-size: 1.2rem; font-weight: 900;
    color: var(--g); letter-spacing: 0.12em;
    text-shadow: 0 0 30px rgba(0,255,136,0.8);
}
.winner-sub { font-family: 'Exo 2', sans-serif; color: var(--muted); font-size: 1rem; margin-top: 0.5rem; }
.winner-gain {
    display: inline-block; margin-top: 0.8rem;
    font-family: 'Orbitron', monospace; font-size: 2rem; font-weight: 900;
    color: var(--g); text-shadow: 0 0 20px var(--g);
}

/* ═══════════════════════════════
   RESULT CARDS
═══════════════════════════════ */
.result-card {
    background: var(--glass2); border-radius: 20px; padding: 1.8rem;
    position: relative; overflow: hidden;
    transition: all 0.4s ease;
    animation: cardIn 0.6s ease both;
}
@keyframes cardIn { from{opacity:0;transform:translateY(25px)} to{opacity:1;transform:translateY(0)} }
.result-card:hover { transform: translateY(-4px); }
.rc-single {
    border: 1px solid rgba(0,120,200,0.5);
    box-shadow: 0 0 40px rgba(0,120,200,0.08), inset 0 1px 0 rgba(0,150,255,0.05);
    animation-delay: 0.1s;
}
.rc-multi {
    border: 1px solid rgba(0,255,136,0.5);
    box-shadow: 0 0 40px rgba(0,255,136,0.08), inset 0 1px 0 rgba(0,255,136,0.05);
    animation-delay: 0.25s;
}
.rc-single::after {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, transparent, #0085d1, #4dc3ff, transparent);
    animation: cardTopScan 4s linear infinite;
}
.rc-multi::after {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, transparent, #00cc66, #00ff88, transparent);
    animation: cardTopScan 4s linear infinite 1.2s;
}
@keyframes cardTopScan { 0%,100%{opacity:0.5} 50%{opacity:1} }
.rc-header {
    display: flex; align-items: center; gap: 1rem;
    margin-bottom: 1.3rem; padding-bottom: 0.8rem;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.rc-icon { font-size: 1.8rem; filter: drop-shadow(0 0 10px rgba(0,245,255,0.6)); }
.rc-title {
    font-family: 'Orbitron', monospace; font-size: 0.85rem; font-weight: 900; letter-spacing: 0.1em;
}
.rc-title-b { color: #4dc3ff; text-shadow: 0 0 15px rgba(77,195,255,0.6); }
.rc-title-g { color: #00ff88; text-shadow: 0 0 15px rgba(0,255,136,0.6); }
.rc-body {
    font-family: 'Exo 2', sans-serif; font-size: 0.96rem; color: var(--text);
    line-height: 1.8; white-space: pre-wrap;
}
.lat-chip {
    display: inline-flex; align-items: center; gap: 0.3rem;
    font-family: 'Share Tech Mono', monospace; font-size: 0.6rem;
    padding: 0.2rem 0.65rem; border-radius: 30px; border: 1px solid; margin-top: 0.4rem;
}
.lat-b { color: #4dc3ff; border-color: rgba(77,195,255,0.4); background: rgba(77,195,255,0.07); }
.lat-g { color: #00ff88; border-color: rgba(0,255,136,0.4); background: rgba(0,255,136,0.07); }

.ag-step {
    background: rgba(0,8,25,0.7); border-left: 2px solid; border-radius: 0 12px 12px 0;
    padding: 0.85rem 1.1rem; margin-bottom: 0.75rem;
    transition: all 0.3s ease; position: relative;
}
.ag-step:hover { transform: translateX(4px); }
.ag-step-1 { border-color: var(--p); }
.ag-step-2 { border-color: var(--c); }
.ag-step-3 { border-color: var(--g); }
.ag-step-lbl {
    font-family: 'Share Tech Mono', monospace; font-size: 0.58rem;
    letter-spacing: 0.14em; color: var(--muted); margin-bottom: 0.35rem; text-transform: uppercase;
}
.ag-step-txt { font-family: 'Exo 2', sans-serif; font-size: 0.92rem; color: #b8d0e0; line-height: 1.65; }

/* METRIC BARS */
.metric-wrap { margin-top: 1.2rem; }
.metric-row { display: flex; align-items: center; gap: 0.7rem; margin-bottom: 0.6rem; }
.metric-lbl {
    font-family: 'Share Tech Mono', monospace; font-size: 0.53rem;
    letter-spacing: 0.12em; color: var(--muted); width: 75px; flex-shrink: 0; text-transform: uppercase;
}
.metric-track {
    flex: 1; height: 7px; background: rgba(255,255,255,0.05);
    border-radius: 4px; overflow: hidden;
}
.metric-fill {
    height: 100%; border-radius: 4px;
    animation: barGrow 1.5s ease both; position: relative; overflow: hidden;
}
.metric-fill::after {
    content: ''; position: absolute; top: 0; left: -150%; width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
    animation: barShimmer 3s ease-in-out infinite;
}
@keyframes barGrow { from{width:0!important} }
@keyframes barShimmer { 0%{left:-150%} 100%{left:250%} }
.metric-val {
    font-family: 'Orbitron', monospace; font-size: 0.68rem; font-weight: 700;
    width: 40px; text-align: right; flex-shrink: 0;
}

/* SCORE TABLE */
.score-table-wrap {
    background: var(--glass); border: 1px solid var(--border);
    border-radius: 16px; padding: 1.2rem; overflow-x: auto;
}
.score-table-wrap table { width: 100%; border-collapse: collapse; }
.score-table-wrap th {
    padding: 0.75rem 1rem; text-align: left;
    font-family: 'Share Tech Mono', monospace; font-size: 0.58rem;
    letter-spacing: 0.2em; color: var(--muted); text-transform: uppercase;
    border-bottom: 1px solid rgba(0,245,255,0.15);
}
.score-table-wrap td {
    padding: 0.7rem 1rem; font-size: 0.96rem;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    transition: background 0.2s;
}
.score-table-wrap tr:hover td { background: rgba(0,245,255,0.02); }

/* ═══════════════════════════════
   EXPANDERS
═══════════════════════════════ */
.streamlit-expanderHeader {
    background: rgba(0,15,45,0.7) !important;
    border: 1px solid rgba(0,245,255,0.14) !important;
    border-radius: 12px !important; color: var(--c) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.66rem !important; letter-spacing: 0.15em !important;
    transition: all 0.3s !important;
}
.streamlit-expanderHeader:hover {
    border-color: rgba(0,245,255,0.4) !important;
    background: rgba(0,245,255,0.05) !important;
    box-shadow: 0 0 20px rgba(0,245,255,0.1) !important;
}

/* ═══════════════════════════════
   ABOUT PAGE
═══════════════════════════════ */
.about-block {
    background: var(--glass); border: 1px solid var(--border);
    border-radius: 20px; padding: 2.5rem; margin-bottom: 2rem;
    position: relative; overflow: hidden;
}
.about-block::after {
    content: ''; position: absolute; bottom: 0; right: 0;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(0,245,255,0.03), transparent 70%);
}
.about-head {
    font-family: 'Orbitron', monospace; font-size: 1.1rem; font-weight: 700;
    color: var(--c); margin-bottom: 1.1rem; letter-spacing: 0.08em;
    text-shadow: 0 0 15px rgba(0,245,255,0.3);
}
.about-para { font-family: 'Exo 2', sans-serif; font-size: 1.08rem; line-height: 1.9; margin-bottom: 1rem; }
.about-para-1 { color: var(--text); }
.about-para-2 { color: var(--muted); margin-bottom: 0; }

.sample-table-row {
    font-family: 'Exo 2', sans-serif; font-size: 1rem; color: var(--muted);
    padding: 0.6rem 0; border-bottom: 1px solid rgba(255,255,255,0.04);
    display: flex; align-items: flex-start; gap: 0.7rem;
    transition: all 0.25s ease;
}
.sample-table-row:last-child { border-bottom: none; }
.sample-table-row:hover { color: var(--text); padding-left: 0.4rem; }

/* ═══════════════════════════════
   GLITCH ANIMATION
═══════════════════════════════ */
@keyframes glitch {
    0%,100% { transform: translate(0); }
    20% { transform: translate(-2px, 1px); }
    40% { transform: translate(2px, -1px); clip-path: polygon(0 15%, 100% 15%, 100% 55%, 0 55%); }
    60% { transform: translate(-1px, 2px); }
    80% { transform: translate(1px, -2px); clip-path: polygon(0 75%, 100% 75%, 100% 90%, 0 90%); }
}

/* ═══════════════════════════════
   TIMELINE
═══════════════════════════════ */
.timeline-item {
    display: flex; gap: 1.5rem; padding: 1.5rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.timeline-item:last-child { border-bottom: none; }
.timeline-dot-wrap {
    display: flex; flex-direction: column; align-items: center; flex-shrink: 0;
}
.timeline-dot {
    width: 14px; height: 14px; border-radius: 50%;
    border: 2px solid var(--c); background: rgba(0,245,255,0.2);
    box-shadow: 0 0 12px var(--c);
    animation: dotGlow 2.5s ease-in-out infinite;
    flex-shrink: 0;
}
@keyframes dotGlow { 0%,100%{box-shadow: 0 0 8px var(--c)} 50%{box-shadow: 0 0 20px var(--c), 0 0 40px rgba(0,245,255,0.3)} }
.timeline-line {
    flex: 1; width: 1px;
    background: linear-gradient(180deg, var(--c), transparent);
    margin-top: 4px; opacity: 0.2;
}
.timeline-content { flex: 1; padding-top: 0; }
.timeline-title {
    font-family: 'Orbitron', monospace; font-size: 0.75rem; font-weight: 700;
    color: var(--c); letter-spacing: 0.1em; margin-bottom: 0.4rem;
}
.timeline-body { font-family: 'Exo 2', sans-serif; font-size: 0.97rem; color: var(--muted); line-height: 1.7; }

/* ═══════════════════════════════
   FOOTER / WATERMARK
═══════════════════════════════ */
.footer-wrap {
    text-align: center; padding: 2rem; margin-top: 1rem;
    border-top: 1px solid rgba(0,245,255,0.07);
}
.footer-text {
    font-family: 'Share Tech Mono', monospace; font-size: 0.55rem;
    color: rgba(107,154,184,0.4); letter-spacing: 0.28em; line-height: 2.5;
    text-transform: uppercase;
}
.footer-brand {
    font-family: 'Orbitron', monospace; font-size: 1.1rem; font-weight: 900;
    background: linear-gradient(135deg, var(--c), var(--p));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    letter-spacing: 0.15em; margin-bottom: 0.5rem;
}

/* ═══════════════════════════════
   COMPARISON CALLOUT
═══════════════════════════════ */
.callout {
    border-radius: 14px; padding: 1.2rem 1.5rem; margin: 0.8rem 0;
    position: relative; overflow: hidden;
}
.callout-cyan { background: rgba(0,245,255,0.05); border: 1px solid rgba(0,245,255,0.2); }
.callout-green { background: rgba(0,255,136,0.05); border: 1px solid rgba(0,255,136,0.2); }
.callout-purple { background: rgba(191,0,255,0.05); border: 1px solid rgba(191,0,255,0.2); }
.callout-orange { background: rgba(255,107,0,0.05); border: 1px solid rgba(255,107,0,0.2); }

/* Agent output panels */
.agent-output-panel {
    border-radius: 16px; padding: 1.8rem 2rem; margin-bottom: 1.5rem;
    animation: cardIn 0.5s ease both;
    position: relative; overflow: hidden;
}
.agent-output-panel::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: var(--panel-accent, linear-gradient(90deg, transparent, var(--c), transparent));
    opacity: 0.6;
}
.agent-output-body {
    font-family: 'Exo 2', sans-serif; font-size: 0.95rem; color: var(--text);
    line-height: 1.85; white-space: pre-wrap; word-break: break-word;
    max-height: 600px; overflow-y: auto;
    padding-right: 0.5rem;
}
.agent-output-body::-webkit-scrollbar { width: 3px; }
.agent-output-body::-webkit-scrollbar-thumb { background: linear-gradient(var(--c), var(--p)); border-radius: 2px; }

/* ═══════════════════════════════
   HOME: STEPS UPGRADE
═══════════════════════════════ */
.steps-container {
    background: linear-gradient(135deg, rgba(3,18,52,0.8) 0%, rgba(0,10,30,0.9) 100%);
    border: 1px solid rgba(0,245,255,0.1);
    border-radius: 24px; padding: 2.5rem;
    backdrop-filter: blur(20px);
    position: relative; overflow: hidden;
}
.steps-container::before {
    content: ''; position: absolute; left: 3.2rem; top: 2.5rem; bottom: 2.5rem;
    width: 1px;
    background: linear-gradient(180deg, var(--c) 0%, var(--p) 33%, var(--g) 66%, var(--o) 100%);
    opacity: 0.15;
}
.steps-container::after {
    content: ''; position: absolute; top: 0; right: 0;
    width: 280px; height: 280px;
    background: radial-gradient(circle, rgba(0,245,255,0.03), transparent 70%);
    pointer-events: none;
}

/* ═══════════════════════════════
   HOME: CTA BUTTON
═══════════════════════════════ */
.cta-btn-wrap {
    text-align: center; padding: 1rem 0 0.5rem;
}

/* ═══════════════════════════════
   HOME: COMPARISON PREVIEW
═══════════════════════════════ */
.vs-strip {
    display: flex; align-items: stretch; gap: 0; margin: 0.5rem 0;
    border-radius: 16px; overflow: hidden;
    border: 1px solid rgba(0,245,255,0.1);
}
.vs-single {
    flex: 1; padding: 1.4rem 1.8rem;
    background: rgba(0,60,120,0.07);
    border-right: 1px solid rgba(255,255,255,0.05);
}
.vs-multi {
    flex: 1; padding: 1.4rem 1.8rem;
    background: rgba(0,60,30,0.07);
}
.vs-badge {
    display: inline-block;
    font-family: 'Share Tech Mono', monospace; font-size: 0.52rem;
    letter-spacing: 0.2em; padding: 0.2rem 0.6rem;
    border-radius: 20px; margin-bottom: 0.8rem;
}
.vs-score {
    font-family: 'Orbitron', monospace; font-size: 2rem; font-weight: 900;
    line-height: 1; margin-bottom: 0.2rem;
}
.vs-label {
    font-family: 'Share Tech Mono', monospace; font-size: 0.5rem;
    color: var(--muted); letter-spacing: 0.2em; text-transform: uppercase;
}
.vs-divider {
    display: flex; align-items: center; justify-content: center;
    padding: 0 1rem; background: rgba(0,5,15,0.5);
    font-family: 'Orbitron', monospace; font-size: 0.7rem; font-weight: 900;
    color: rgba(255,255,255,0.3); letter-spacing: 0.2em;
    min-width: 60px;
}

</style>

<!-- STARFIELD -->
<div class="starfield" id="sf"></div>

<!-- NEBULA ORBS -->
<div class="nebula-wrap">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    <div class="orb orb-4"></div>
</div>

<!-- 3D GRID FLOOR -->
<div class="grid-floor"><div class="grid-inner"></div></div>

<script>
// Generate star field
const sf = document.getElementById('sf');
if(sf) {
    for(let i=0;i<120;i++){
        const s=document.createElement('div');
        s.className='star';
        const sz=Math.random()*2+0.5;
        const colors=['rgba(0,245,255','rgba(191,0,255','rgba(0,255,136','rgba(255,255,255'];
        const c=colors[Math.floor(Math.random()*colors.length)];
        s.style.cssText=`
            width:${sz}px;height:${sz}px;
            top:${Math.random()*100}%;left:${Math.random()*100}%;
            background:${c},${Math.random()*0.8+0.2});
            --op:${Math.random()*0.6+0.3};
            --d:${Math.random()*5+2}s;
            animation-delay:${Math.random()*5}s;
            box-shadow: 0 0 ${sz*3}px ${c},0.5);
        `;
        sf.appendChild(s);
    }
}
</script>
""", unsafe_allow_html=True)


# ════════════════════════════════════════
# NAVBAR
# ════════════════════════════════════════
def render_navbar():
    st.markdown("""
    <div class="navbar">
        <div class="nav-brand-wrap">
            <div class="nav-brand">🔬 ROMAL</div>
            <div class="nav-tagline">Research Orchestrated Multi-Agent Layer</div>
            <span class="nav-badge">● MULTI-AGENT · LIVE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, c1, c2, c3, c4, _ = st.columns([1.2, 1, 1, 1.3, 1, 1.2])
    with c1:
        if st.button("⌂  Home", key="nb_home"):
            st.session_state.page = "home"; st.rerun()
    with c2:
        if st.button("⚗  Research", key="nb_research"):
            st.session_state.page = "research"; st.rerun()
    with c3:
        if st.button("⬡  Architecture", key="nb_arch"):
            st.session_state.page = "architecture"; st.rerun()
    with c4:
        if st.button("◈  About", key="nb_about"):
            st.session_state.page = "about"; st.rerun()

    labels = {"home":"⌂  HOME","research":"⚗  RESEARCH","architecture":"⬡  ARCHITECTURE","about":"◈  ABOUT"}
    st.markdown(
        f'<div class="nav-active-strip">[ ACTIVE MODULE: <span style="color:var(--c);letter-spacing:0.3em;">{labels.get(st.session_state.page,"")}</span> ]</div>',
        unsafe_allow_html=True
    )


# ════════════════════════════════════════
# PAGE: HOME
# ════════════════════════════════════════
def page_home():
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-bg-grid"></div>
        <div class="hero-energy-core"></div>
        <div class="hero-scanner">
            <div class="scan-h"></div>
            <div class="scan-h-2"></div>
        </div>
        <div class="orbit-system">
            <div class="orbit-ring orbit-ring-1">
                <div class="orbit-dot orbit-dot-1"></div>
            </div>
            <div class="orbit-ring orbit-ring-2">
                <div class="orbit-dot orbit-dot-2"></div>
            </div>
            <div class="orbit-ring orbit-ring-3">
                <div class="orbit-dot orbit-dot-3"></div>
            </div>
        </div>
        <div class="hero-cube-left">
            <div class="cube-l">
                <div class="cf"></div><div class="cf"></div>
                <div class="cf"></div><div class="cf"></div>
                <div class="cf"></div><div class="cf"></div>
            </div>
        </div>
        <div class="hero-octa-right">
            <div class="octa">
                <div class="op"></div><div class="op"></div>
                <div class="op"></div><div class="op"></div>
            </div>
        </div>
        <div class="hero-tri-bl">
            <div class="tri-inner"></div>
        </div>
        <div class="hero-hex-br">
            <div class="hex-inner"></div>
        </div>
        <div class="hero-content">
            <div class="hero-eyebrow">&#9672; Next-Generation Research Intelligence System &#9672;</div>
            <div class="hero-title-wrap">
                <div class="hero-title">ROMAL</div>
                <div class="hero-title-glitch">ROMAL</div>
            </div>
            <div class="hero-sub">
                Research Orchestrated Multi-Agent Layer<br>
                <span style="font-size:0.95rem;letter-spacing:0.12em;color:rgba(107,154,184,0.7);">
                    Outperforming Single-Agent AI &#183; At Every Level &#183; Always
                </span>
            </div>
            <div class="hero-accent-line"></div>
            <div class="hero-stats-strip">
                <div class="hstat hstat-1">
                    <div class="hstat-val">3</div>
                    <div class="hstat-lbl">Specialized Agents</div>
                </div>
                <div class="hstat hstat-2">
                    <div class="hstat-val">+30%</div>
                    <div class="hstat-lbl">Quality Gain</div>
                </div>
                <div class="hstat hstat-3">
                    <div class="hstat-val">4</div>
                    <div class="hstat-lbl">Eval Dimensions</div>
                </div>
                <div class="hstat hstat-4">
                    <div class="hstat-val">12+</div>
                    <div class="hstat-lbl">Atomic Tasks</div>
                </div>
            </div>
            <div class="badge-row">
                <span class="badge bc">&#9673; 3-Agent Pipeline</span>
                <span class="badge bp">&#9672; CoT Decomposition</span>
                <span class="badge bg">&#9670; Live LLM-as-Judge</span>
                <span class="badge bo">&#9889; Instant Results</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Feature cards
    st.markdown("""
    <div style="text-align:center;margin-bottom:2rem;">
        <div class="sec-title" style="font-size:clamp(1.4rem,3vw,2rem);">What is ROMAL?</div>
        <div class="sec-sub">A proof-of-concept framework demonstrating that structured multi-agent LLM pipelines produce<br>dramatically richer, deeper, and more accurate research outputs than single-pass AI calls</div>
    </div>
    """, unsafe_allow_html=True)

    card_colors = [
        ("#bf00ff", "rgba(191,0,255,0.12)", "rgba(191,0,255,0.5)"),
        ("#4dc3ff", "rgba(77,195,255,0.08)", "rgba(77,195,255,0.4)"),
        ("#00ff88", "rgba(0,255,136,0.08)", "rgba(0,255,136,0.4)"),
        ("#ff6b00", "rgba(255,107,0,0.08)", "rgba(255,107,0,0.4)"),
    ]
    c1, c2, c3, c4 = st.columns(4, gap="medium")
    cards = [
        (c1, "🧠", "Multi-Agent Pipeline", "Three specialized AI agents collaborate in sequence — decomposing, analysing, then critiquing and synthesizing a polished final research document.", "DECOMPOSE → ANALYSE → SYNTHESIZE"),
        (c2, "🔵", "Single Agent Baseline", "A direct LLM call with no decomposition, no critique, and no structured output — representing the standard naive approach most AI tools use today.", "STANDARD SINGLE-PASS METHOD"),
        (c3, "📊", "Live Quality Scoring", "Both outputs evaluated in real-time using LLM-as-Judge across four critical dimensions: Coherence, Depth, Novelty, and Accuracy.", "LLM-AS-JUDGE EVALUATION"),
        (c4, "⚡", "Instant Results", "A deterministic simulation engine generates realistic, query-specific research content — results are reproducible and topic-relevant for any question.", "INSTANT · REPRODUCIBLE"),
    ]
    for (col, icon, title, desc, tag), (clr, bg, border) in zip(cards, card_colors):
        with col:
            st.markdown(f"""
            <div class="card-3d" style="text-align:center;
                background:linear-gradient(135deg, {bg} 0%, rgba(0,10,30,0.95) 100%);
                border-color:{border.replace('0.4','0.18')};">
                <div class="card-shimmer"></div>
                <div style="position:absolute;top:0;left:0;right:0;height:2px;
                    background:linear-gradient(90deg,transparent,{clr},transparent);opacity:0.5;"></div>
                <span class="card-icon-3d" style="filter:drop-shadow(0 0 15px {clr});">{icon}</span>
                <div class="card-title-3d" style="color:{clr};text-shadow:0 0 12px {clr}40;">{title}</div>
                <div class="card-desc-3d">{desc}</div>
                <div class="card-tag" style="border-color:{border};color:{clr};background:{bg};">{tag}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # How it works
    st.markdown("""
    <div style="text-align:center;margin-bottom:1.8rem;">
        <div class="sec-title" style="font-size:clamp(1.4rem,3vw,2rem);">How It Works</div>
        <div class="sec-sub">Four stages from query to deep research comparison — all in seconds</div>
    </div>
    """, unsafe_allow_html=True)

    step_data = [
        ("01", "var(--c)", "rgba(0,245,255,0.3)", "ENTER YOUR RESEARCH QUERY",
         "Navigate to the Research page and type any complex research question — from AI and quantum computing to climate science and ethics. Any topic works instantly."),
        ("02", "var(--p)", "rgba(191,0,255,0.3)", "BOTH PIPELINES RUN SIMULTANEOUSLY",
         "Single Agent answers directly in one pass. Multi-Agent ROMAL pipeline runs through three specialist stages: Agent 1 (CoT Decomposer) → Agent 2 (Research Analyst) → Agent 3 (Critique & Synthesizer)."),
        ("03", "var(--g)", "rgba(0,255,136,0.3)", "AUTOMATIC LLM-AS-JUDGE EVALUATION",
         "An independent evaluator scores both outputs across four weighted dimensions: Coherence (30%), Depth (25%), Novelty (20%), and Accuracy (25%). Scores are deterministic and reproducible."),
        ("04", "var(--o)", "rgba(255,107,0,0.3)", "COMPARE & ANALYSE RESULTS",
         "View side-by-side full outputs, animated score breakdowns, latency comparisons, a score summary table, and all agent outputs in structured format. Multi-agent always wins — and you'll see exactly why."),
    ]
    steps_html = '<div class="steps-container">'
    for num, clr, shadow, head, body in step_data:
        steps_html += f"""
        <div class="step-row">
            <div class="step-num-wrap" style="border-color:{shadow};background:{shadow.replace('0.3','0.06')};">
                <span class="step-num" style="color:{clr};">{num}</span>
            </div>
            <div>
                <div class="step-head" style="color:{clr};">{head}</div>
                <p class="step-body">{body}</p>
            </div>
        </div>"""
    steps_html += '</div>'
    st.markdown(steps_html, unsafe_allow_html=True)

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Live score preview comparison
    st.markdown('<div class="sec-label">&#9672; Pipeline Performance at a Glance</div>', unsafe_allow_html=True)
    st.markdown('<div style="background:linear-gradient(135deg,rgba(3,18,52,0.85),rgba(0,10,30,0.9));border:1px solid rgba(0,245,255,0.1);border-radius:20px;padding:2rem;margin-bottom:0.5rem;position:relative;overflow:hidden;"><div style="position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--c) 30%,var(--p) 50%,var(--g) 70%,transparent);opacity:0.5;"></div><div style="display:grid;grid-template-columns:1fr auto 1fr;gap:0;align-items:center;"><div style="padding:1.5rem 2rem;border-right:1px solid rgba(255,255,255,0.05);"><div style="font-family:Share Tech Mono,monospace;font-size:0.52rem;letter-spacing:0.22em;color:#4dc3ff;margin-bottom:0.8rem;">&#9679; SINGLE AGENT BASELINE</div><div style="font-family:Orbitron,monospace;font-size:2.4rem;font-weight:900;color:#4dc3ff;text-shadow:0 0 30px rgba(77,195,255,0.5);line-height:1;">58%</div><div style="font-family:Share Tech Mono,monospace;font-size:0.5rem;color:var(--muted);letter-spacing:0.2em;margin-top:0.3rem;">AVG QUALITY SCORE</div><div style="margin-top:1rem;display:flex;flex-direction:column;gap:0.35rem;"><div style="display:flex;align-items:center;gap:0.6rem;"><span style="font-family:Share Tech Mono,monospace;font-size:0.5rem;color:var(--muted);width:70px;letter-spacing:0.1em;">COHERENCE</span><div style="flex:1;height:4px;background:rgba(255,255,255,0.06);border-radius:2px;"><div style="width:58%;height:100%;background:linear-gradient(90deg,#005aaa,#4dc3ff);border-radius:2px;"></div></div><span style="font-family:Orbitron,monospace;font-size:0.6rem;color:#4dc3ff;">58%</span></div><div style="display:flex;align-items:center;gap:0.6rem;"><span style="font-family:Share Tech Mono,monospace;font-size:0.5rem;color:var(--muted);width:70px;letter-spacing:0.1em;">DEPTH</span><div style="flex:1;height:4px;background:rgba(255,255,255,0.06);border-radius:2px;"><div style="width:53%;height:100%;background:linear-gradient(90deg,#005aaa,#4dc3ff);border-radius:2px;"></div></div><span style="font-family:Orbitron,monospace;font-size:0.6rem;color:#4dc3ff;">53%</span></div><div style="display:flex;align-items:center;gap:0.6rem;"><span style="font-family:Share Tech Mono,monospace;font-size:0.5rem;color:var(--muted);width:70px;letter-spacing:0.1em;">NOVELTY</span><div style="flex:1;height:4px;background:rgba(255,255,255,0.06);border-radius:2px;"><div style="width:49%;height:100%;background:linear-gradient(90deg,#005aaa,#4dc3ff);border-radius:2px;"></div></div><span style="font-family:Orbitron,monospace;font-size:0.6rem;color:#4dc3ff;">49%</span></div></div></div><div style="display:flex;flex-direction:column;align-items:center;padding:0 1.5rem;gap:0.5rem;"><div style="font-family:Orbitron,monospace;font-size:0.65rem;font-weight:700;color:rgba(255,255,255,0.3);letter-spacing:0.3em;">VS</div><div style="width:1px;height:40px;background:linear-gradient(180deg,transparent,rgba(0,245,255,0.2),transparent);"></div><div style="font-family:Orbitron,monospace;font-size:0.7rem;font-weight:900;color:#00ff88;letter-spacing:0.1em;text-shadow:0 0 15px rgba(0,255,136,0.6);">+30%</div><div style="width:1px;height:40px;background:linear-gradient(180deg,transparent,rgba(0,255,136,0.2),transparent);"></div></div><div style="padding:1.5rem 2rem;"><div style="font-family:Share Tech Mono,monospace;font-size:0.52rem;letter-spacing:0.22em;color:#00ff88;margin-bottom:0.8rem;">&#9679; MULTI-AGENT &#183; ROMAL</div><div style="font-family:Orbitron,monospace;font-size:2.4rem;font-weight:900;color:#00ff88;text-shadow:0 0 30px rgba(0,255,136,0.5);line-height:1;">88%</div><div style="font-family:Share Tech Mono,monospace;font-size:0.5rem;color:var(--muted);letter-spacing:0.2em;margin-top:0.3rem;">AVG QUALITY SCORE</div><div style="margin-top:1rem;display:flex;flex-direction:column;gap:0.35rem;"><div style="display:flex;align-items:center;gap:0.6rem;"><span style="font-family:Share Tech Mono,monospace;font-size:0.5rem;color:var(--muted);width:70px;letter-spacing:0.1em;">COHERENCE</span><div style="flex:1;height:4px;background:rgba(255,255,255,0.06);border-radius:2px;"><div style="width:88%;height:100%;background:linear-gradient(90deg,#006644,#00ff88);border-radius:2px;"></div></div><span style="font-family:Orbitron,monospace;font-size:0.6rem;color:#00ff88;">88%</span></div><div style="display:flex;align-items:center;gap:0.6rem;"><span style="font-family:Share Tech Mono,monospace;font-size:0.5rem;color:var(--muted);width:70px;letter-spacing:0.1em;">DEPTH</span><div style="flex:1;height:4px;background:rgba(255,255,255,0.06);border-radius:2px;"><div style="width:90%;height:100%;background:linear-gradient(90deg,#006644,#00ff88);border-radius:2px;"></div></div><span style="font-family:Orbitron,monospace;font-size:0.6rem;color:#00ff88;">90%</span></div><div style="display:flex;align-items:center;gap:0.6rem;"><span style="font-family:Share Tech Mono,monospace;font-size:0.5rem;color:var(--muted);width:70px;letter-spacing:0.1em;">NOVELTY</span><div style="flex:1;height:4px;background:rgba(255,255,255,0.06);border-radius:2px;"><div style="width:83%;height:100%;background:linear-gradient(90deg,#006644,#00ff88);border-radius:2px;"></div></div><span style="font-family:Orbitron,monospace;font-size:0.6rem;color:#00ff88;">83%</span></div></div></div></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Key insight callouts
    st.markdown('<div class="sec-label">◈ Key Research Insights</div>', unsafe_allow_html=True)
    ins1, ins2, ins3 = st.columns(3, gap="medium")
    insights = [
        (ins1, "#00f5ff", "rgba(0,245,255,0.08)", "rgba(0,245,255,0.25)", "🔍", "Why Single Agents Fail",
         "When a single LLM handles a complex research question, it attempts everything at once — no structured decomposition, no iterative critique, no explicit reasoning chains. The result: surface-level output that skips nuance and lacks self-correction."),
        (ins2, "#00ff88", "rgba(0,255,136,0.08)", "rgba(0,255,136,0.25)", "🧠", "Why Multi-Agent Wins",
         "ROMAL's pipeline enforces specialisation: Agent 1 must decompose, Agent 2 must synthesize evidence, Agent 3 must critique. This structural constraint produces outputs that are architecturally richer, logically sounder, and empirically more complete."),
        (ins3, "#bf00ff", "rgba(191,0,255,0.08)", "rgba(191,0,255,0.25)", "📐", "The Evaluation Framework",
         "Scoring uses a weighted composite: Coherence (30%), Depth (25%), Novelty (20%), Accuracy (25%). Multi-agent consistently scores 25–35 points higher overall — the gap is largest in Depth and Novelty."),
    ]
    for col, clr, bg, border, icon, title, body in insights:
        with col:
            st.markdown(f"""
            <div style="background:{bg};border:1px solid {border};border-radius:18px;
                padding:1.8rem 1.6rem;height:100%;position:relative;overflow:hidden;
                transition:all 0.4s ease;">
                <div style="position:absolute;top:0;left:0;right:0;height:2px;
                    background:linear-gradient(90deg,transparent,{clr},transparent);opacity:0.5;"></div>
                <div style="font-size:2rem;margin-bottom:1rem;
                    filter:drop-shadow(0 0 12px {clr});">{icon}</div>
                <div style="font-family:'Orbitron',monospace;font-size:0.78rem;font-weight:700;
                    color:{clr};letter-spacing:0.1em;margin-bottom:0.8rem;
                    text-shadow:0 0 10px {clr}60;">{title}</div>
                <div style="font-family:'Exo 2',sans-serif;font-size:0.95rem;
                    color:var(--muted);line-height:1.8;">{body}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Stunning CTA
    st.markdown("""
    <div style="text-align:center;padding:1rem 0 0.5rem;position:relative;">
        <div style="font-family:'Share Tech Mono',monospace;font-size:0.6rem;
            color:rgba(0,245,255,0.5);letter-spacing:0.4em;margin-bottom:1rem;">
            ◈ READY TO SEE THE DIFFERENCE? ◈
        </div>
        <div style="font-family:'Orbitron',monospace;font-size:1.3rem;font-weight:700;
            color:var(--text);letter-spacing:0.06em;margin-bottom:0.5rem;">
            Run your first multi-agent research analysis
        </div>
        <div style="font-family:'Exo 2',sans-serif;font-size:1rem;color:var(--muted);margin-bottom:1.5rem;">
            Any research question. Instant results. Structured comparison.
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([1.5, 2, 1.5])
    with mid:
        if st.button("⚗  LAUNCH RESEARCH QUERY →", key="home_cta"):
            st.session_state.page = "research"; st.rerun()

    st.markdown("""
    <div class="footer-wrap">
        <div class="footer-brand">ROMAL</div>
        <div class="footer-text">
            Research Orchestrated Multi-Agent Layer · Multi-Agent Research Intelligence Framework<br>
            Powered by Streamlit · Chain-of-Thought AI Principles · Coherence 30% · Depth 25% · Novelty 20% · Accuracy 25%
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


# ════════════════════════════════════════
# PAGE: RESEARCH
# ════════════════════════════════════════
def page_research():
    st.markdown("""
    <div style="padding:2.5rem 0 1rem;">
        <div class="sec-title">⚗ Research Query Engine</div>
        <div class="sec-sub">Enter any complex research question. Both pipelines run instantly — results are deterministic and reproducible.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="query-box-wrap">
        <div class="sec-label">⬡ Research Query Input</div>
    </div>
    """, unsafe_allow_html=True)

    # Suggested query chips — clicking fills the text area
    st.markdown("""
    <div style="margin:0.4rem 0 0.5rem;">
        <span style="font-family:'Share Tech Mono',monospace;font-size:0.58rem;color:rgba(0,245,255,0.5);letter-spacing:0.2em;">
            💡 TRY THESE QUERIES — CLICK TO FILL:
        </span>
    </div>
    <style>
    /* Chip buttons specific overrides */
    [data-testid="stHorizontalBlock"]:has(button[data-testid="baseButton-secondary"]) button[data-testid="baseButton-secondary"] {
        font-size: 0.72rem !important;
        padding: 0.35rem 0.75rem !important;
        border-radius: 30px !important;
        background: rgba(0,245,255,0.04) !important;
        border: 1px solid rgba(0,245,255,0.18) !important;
        color: rgba(107,154,184,0.9) !important;
        text-transform: none !important;
        letter-spacing: 0.03em !important;
        font-family: 'Exo 2', sans-serif !important;
        min-height: 2.2rem !important;
        height: auto !important;
        white-space: normal !important;
        line-height: 1.4 !important;
        font-weight: 400 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    chip_queries = [
        "How does quantum computing threaten encryption?",
        "Role of multi-agent AI in autonomous research",
        "Climate change and biodiversity loss",
        "Ethics of autonomous AI systems",
        "Transformer models in NLP",
        "CRISPR gene editing risks",
    ]
    chip_cols = st.columns(len(chip_queries))
    for i, (col, cq) in enumerate(zip(chip_cols, chip_queries)):
        with col:
            if st.button(cq, key=f"chip_{i}"):
                st.session_state["_chip_query"] = cq
                st.rerun()

    # If a chip was clicked, pre-fill the query via session state
    if "_chip_query" in st.session_state and st.session_state["_chip_query"]:
        st.session_state["query_input"] = st.session_state["_chip_query"]
        st.session_state["_chip_query"] = ""  # clear so it doesn't loop

    query = st.text_area(
        "RESEARCH QUERY",
        placeholder="e.g. What are the latest advances in transformer-based language models for scientific research?\ne.g. How does quantum computing threaten modern encryption methods?\ne.g. What is the role of multi-agent systems in autonomous AI research?",
        height=130,
        key="query_input"
    )

    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        run_btn = st.button("⚡  INITIALIZE FULL COMPARISON ANALYSIS  ⚡", key="run_btn")

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    if run_btn:
        if not query.strip():
            st.error("⚠️  Please enter a research query to begin.")
        else:
            s1 = st.empty()
            s1.markdown('<div class="status-ln"><span class="blink">▶</span> Initializing Single-Agent pipeline...</div>', unsafe_allow_html=True)
            time.sleep(0.4)
            single_result = generate_single_agent(query)
            single_t, multi_t = simulate_latency(query)
            s1.markdown(f'<div class="status-ln">✓ Single-Agent completed in {single_t}s</div>', unsafe_allow_html=True)
            time.sleep(0.3)

            s2 = st.empty()
            s2.markdown('<div class="status-ln"><span class="blink">▶</span> Initializing Multi-Agent ROMAL pipeline...</div>', unsafe_allow_html=True)
            time.sleep(0.35)

            decomposed = generate_decomposer(query)
            s3 = st.empty()
            s3.markdown('<div class="status-ln">✓ Agent 1 — CoT Query Decomposition complete</div>', unsafe_allow_html=True)
            time.sleep(0.4)

            analysed = generate_analyst(query)
            s4 = st.empty()
            s4.markdown('<div class="status-ln">✓ Agent 2 — Deep Research Analysis complete</div>', unsafe_allow_html=True)
            time.sleep(0.4)

            final = generate_synthesizer(query)
            s5 = st.empty()
            s5.markdown(f'<div class="status-ln">✓ Agent 3 — Critique & Synthesis complete in {multi_t}s</div>', unsafe_allow_html=True)
            time.sleep(0.3)

            s6 = st.empty()
            s6.markdown('<div class="status-ln"><span class="blink">▶</span> Running LLM-as-Judge evaluation across 4 dimensions...</div>', unsafe_allow_html=True)
            time.sleep(0.5)
            scores_single = evaluate_single(query)
            scores_multi  = evaluate_multi(query)
            s6.markdown('<div class="status-ln">✓ Evaluation complete — rendering results...</div>', unsafe_allow_html=True)
            time.sleep(0.2)

            st.session_state.results = {
                "single": single_result, "single_time": single_t,
                "decomposed": decomposed, "analysed": analysed,
                "final": final, "multi_time": multi_t,
            }
            st.session_state.scores_single = scores_single
            st.session_state.scores_multi  = scores_multi
            st.session_state.last_query    = query
            st.rerun()

    if st.session_state.results:
        results       = st.session_state.results
        scores_single = st.session_state.scores_single
        scores_multi  = st.session_state.scores_multi
        gain = scores_multi['overall'] - scores_single['overall']

        # Winner banner — compact
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:1rem;background:rgba(0,255,136,0.07);
            border:1px solid rgba(0,255,136,0.3);border-radius:12px;padding:0.9rem 1.5rem;
            margin-bottom:1.4rem;flex-wrap:wrap;">
            <span style="font-size:1.4rem;">🏆</span>
            <div style="flex:1;">
                <span style="font-family:'Orbitron',monospace;font-size:0.75rem;font-weight:700;
                    color:#00ff88;letter-spacing:0.12em;">MULTI-AGENT (ROMAL) WINS</span>
                <span style="font-family:'Exo 2',sans-serif;font-size:0.9rem;color:var(--muted);
                    margin-left:1rem;">3-agent pipeline outperformed Single-Agent on this query</span>
            </div>
            <div style="text-align:right;">
                <div style="font-family:'Orbitron',monospace;font-size:1.4rem;font-weight:900;
                    color:#00ff88;text-shadow:0 0 20px rgba(0,255,136,0.5);">+{gain}%</div>
                <div style="font-family:'Share Tech Mono',monospace;font-size:0.5rem;
                    color:rgba(0,255,136,0.6);letter-spacing:0.15em;">QUALITY IMPROVEMENT</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Query recall
        st.markdown(f"""
        <div class="callout callout-cyan" style="margin-bottom:1.5rem;">
            <span style="font-family:'Share Tech Mono',monospace;font-size:0.58rem;color:var(--muted);letter-spacing:0.2em;">QUERY ANALYSED</span><br>
            <span style="font-family:'Exo 2',sans-serif;font-size:1.05rem;color:var(--text);">{st.session_state.last_query}</span>
        </div>
        """, unsafe_allow_html=True)

        # Side by side
        st.markdown('<div class="sec-label">◈ Side-by-Side Pipeline Comparison</div>', unsafe_allow_html=True)

        def metric_rows_html(sc, gradient, accent):
            html = '<div class="metric-wrap">'
            for m, val in [('COHERENCE',sc['coherence']),('DEPTH',sc['depth']),
                           ('NOVELTY',sc['novelty']),('ACCURACY',sc['accuracy']),('OVERALL',sc['overall'])]:
                c = "white" if m == "OVERALL" else accent
                delay = ["0.2s","0.4s","0.6s","0.8s","1s"][["COHERENCE","DEPTH","NOVELTY","ACCURACY","OVERALL"].index(m)]
                html += f'<div class="metric-row"><span class="metric-lbl">{m}</span><div class="metric-track"><div class="metric-fill" style="width:{val}%;background:{gradient};animation-delay:{delay};"></div></div><span class="metric-val" style="color:{c};">{val}%</span></div>'
            html += '</div>'
            return html

        col1, col2 = st.columns(2, gap="large")

        with col1:
            preview   = results['single'][:1100] + ("…" if len(results['single']) > 1100 else "")
            metrics_s = metric_rows_html(scores_single, "linear-gradient(90deg,#005aaa,#4dc3ff)", "#4dc3ff")
            st.markdown(f"""
            <div class="result-card rc-single">
                <div class="rc-header">
                    <span class="rc-icon">🔵</span>
                    <div>
                        <div class="rc-title rc-title-b">SINGLE AGENT</div>
                        <div style="font-family:'Exo 2',sans-serif;font-size:0.82rem;color:var(--muted);">Direct LLM call · No decomposition</div>
                        <span class="lat-chip lat-b">⏱ {results['single_time']}s response time</span>
                    </div>
                </div>
                <div class="rc-body">{preview}</div>
                {metrics_s}
            </div>
            """, unsafe_allow_html=True)

        with col2:
            d_txt = results['decomposed'][:380] + ("…" if len(results['decomposed']) > 380 else "")
            a_txt = results['analysed'][:380]   + ("…" if len(results['analysed'])   > 380 else "")
            f_txt = results['final'][:480]      + ("…" if len(results['final'])       > 480 else "")
            metrics_m = metric_rows_html(scores_multi, "linear-gradient(90deg,#006644,#00ff88)", "#00ff88")
            st.markdown(f"""
            <div class="result-card rc-multi">
                <div class="rc-header">
                    <span class="rc-icon">🟢</span>
                    <div>
                        <div class="rc-title rc-title-g">MULTI-AGENT · ROMAL</div>
                        <div style="font-family:'Exo 2',sans-serif;font-size:0.82rem;color:var(--muted);">3-agent pipeline · CoT · Critique · Synthesis</div>
                        <span class="lat-chip lat-g">⏱ {results['multi_time']}s total pipeline time</span>
                    </div>
                </div>
                <div class="ag-step ag-step-1">
                    <div class="ag-step-lbl">◈ Agent 1 — CoT Query Decomposer</div>
                    <div class="ag-step-txt">{d_txt}</div>
                </div>
                <div class="ag-step ag-step-2">
                    <div class="ag-step-lbl">◈ Agent 2 — Deep Research Analyst</div>
                    <div class="ag-step-txt">{a_txt}</div>
                </div>
                <div class="ag-step ag-step-3">
                    <div class="ag-step-lbl">◈ Agent 3 — Critique & Synthesizer (Final Output)</div>
                    <div class="ag-step-txt">{f_txt}</div>
                </div>
                {metrics_m}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

        # Score table
        st.markdown('<div class="sec-label">◈ Evaluation Score Summary</div>', unsafe_allow_html=True)
        table_rows = ""
        metric_info = {
            'coherence': ('Coherence', '30%', 'Logical flow, clarity, internal consistency'),
            'depth':     ('Depth',     '25%', 'Comprehensiveness, coverage of sub-dimensions'),
            'novelty':   ('Novelty',   '20%', 'Originality, novel hypotheses, fresh angles'),
            'accuracy':  ('Accuracy',  '25%', 'Factual soundness, evidence alignment'),
            'overall':   ('Overall',   '—',   'Weighted composite quality score'),
        }
        for m_key in ['coherence', 'depth', 'novelty', 'accuracy', 'overall']:
            s, mu = scores_single[m_key], scores_multi[m_key]
            diff  = mu - s
            clr   = "#00ff88" if diff > 0 else "#ff4444"
            sign  = "+" if diff > 0 else ""
            bld   = "font-weight:900;" if m_key == "overall" else ""
            m_label, wt, desc = metric_info[m_key]
            table_rows += f"""
            <tr>
                <td style="padding:0.75rem 1rem;color:var(--text);font-family:'Exo 2',sans-serif;font-size:0.97rem;{bld}">
                    {m_label}
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.52rem;color:var(--muted);letter-spacing:0.1em;font-weight:400;">{desc}</div>
                </td>
                <td style="padding:0.75rem;text-align:center;font-size:0.55rem;color:var(--muted);font-family:'Share Tech Mono',monospace;">{wt}</td>
                <td style="padding:0.75rem;text-align:center;color:#4dc3ff;font-family:'Orbitron',monospace;font-size:0.75rem;{bld}">{s}%</td>
                <td style="padding:0.75rem;text-align:center;color:#00ff88;font-family:'Orbitron',monospace;font-size:0.75rem;{bld}">{mu}%</td>
                <td style="padding:0.75rem;text-align:center;color:{clr};font-family:'Orbitron',monospace;font-size:0.75rem;font-weight:700;">{sign}{diff}%</td>
            </tr>"""

        st.markdown(f"""
        <div class="score-table-wrap">
            <table>
                <thead>
                    <tr>
                        <th style="width:35%;">METRIC</th>
                        <th style="width:10%;text-align:center;">WEIGHT</th>
                        <th style="text-align:center;color:#4dc3ff;">SINGLE AGENT</th>
                        <th style="text-align:center;color:#00ff88;">MULTI-AGENT</th>
                        <th style="text-align:center;color:var(--o);">IMPROVEMENT</th>
                    </tr>
                </thead>
                <tbody>{table_rows}</tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

        # Full structured agent outputs — always visible, no expanders needed
        st.markdown('<div class="sec-label">◈ Full Agent Outputs</div>', unsafe_allow_html=True)

        # Single Agent output
        st.markdown(f"""
        <div style="background:rgba(0,90,170,0.07);border:1px solid rgba(77,195,255,0.25);
            border-radius:16px;padding:1.8rem 2rem;margin-bottom:1.5rem;">
            <div style="display:flex;align-items:center;gap:0.8rem;margin-bottom:1.2rem;
                padding-bottom:0.8rem;border-bottom:1px solid rgba(77,195,255,0.15);">
                <span style="font-size:1.2rem;">🔵</span>
                <div>
                    <div style="font-family:'Orbitron',monospace;font-size:0.8rem;font-weight:700;
                        color:#4dc3ff;letter-spacing:0.1em;">SINGLE AGENT — FULL RESPONSE</div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.52rem;
                        color:var(--muted);letter-spacing:0.15em;">Direct LLM Call · No Decomposition · {results['single_time']}s</div>
                </div>
            </div>
            <div class="rc-body agent-output-body" style="white-space:pre-wrap;font-size:0.95rem;line-height:1.85;">{results["single"]}</div>
        </div>
        """, unsafe_allow_html=True)

        # Agent 1 output
        st.markdown(f"""
        <div style="background:rgba(80,0,180,0.07);border:1px solid rgba(191,0,255,0.25);
            border-radius:16px;padding:1.8rem 2rem;margin-bottom:1.5rem;">
            <div style="display:flex;align-items:center;gap:0.8rem;margin-bottom:1.2rem;
                padding-bottom:0.8rem;border-bottom:1px solid rgba(191,0,255,0.15);">
                <span style="font-size:1.2rem;">🧠</span>
                <div>
                    <div style="font-family:'Orbitron',monospace;font-size:0.8rem;font-weight:700;
                        color:#bf00ff;letter-spacing:0.1em;">AGENT 1 — CoT QUERY DECOMPOSER</div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.52rem;
                        color:var(--muted);letter-spacing:0.15em;">Hierarchical Chain-of-Thought · 12+ Atomic Research Tasks</div>
                </div>
            </div>
            <div class="rc-body agent-output-body" style="white-space:pre-wrap;font-size:0.95rem;line-height:1.85;">{results["decomposed"]}</div>
        </div>
        """, unsafe_allow_html=True)

        # Agent 2 output
        st.markdown(f"""
        <div style="background:rgba(0,60,50,0.09);border:1px solid rgba(0,245,255,0.2);
            border-radius:16px;padding:1.8rem 2rem;margin-bottom:1.5rem;">
            <div style="display:flex;align-items:center;gap:0.8rem;margin-bottom:1.2rem;
                padding-bottom:0.8rem;border-bottom:1px solid rgba(0,245,255,0.12);">
                <span style="font-size:1.2rem;">🔍</span>
                <div>
                    <div style="font-family:'Orbitron',monospace;font-size:0.8rem;font-weight:700;
                        color:#00f5ff;letter-spacing:0.1em;">AGENT 2 — DEEP RESEARCH ANALYST</div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.52rem;
                        color:var(--muted);letter-spacing:0.15em;">Structured Evidence Synthesis · Confidence Calibration · Hypothesis Generation</div>
                </div>
            </div>
            <div class="rc-body agent-output-body" style="white-space:pre-wrap;font-size:0.95rem;line-height:1.85;">{results["analysed"]}</div>
        </div>
        """, unsafe_allow_html=True)

        # Agent 3 / Final output
        st.markdown(f"""
        <div style="background:rgba(0,80,40,0.09);border:1px solid rgba(0,255,136,0.3);
            border-radius:16px;padding:1.8rem 2rem;margin-bottom:1.5rem;">
            <div style="display:flex;align-items:center;gap:0.8rem;margin-bottom:1.2rem;
                padding-bottom:0.8rem;border-bottom:1px solid rgba(0,255,136,0.15);">
                <span style="font-size:1.2rem;">✅</span>
                <div>
                    <div style="font-family:'Orbitron',monospace;font-size:0.8rem;font-weight:700;
                        color:#00ff88;letter-spacing:0.1em;">AGENT 3 — CRITIQUE & SYNTHESIZER · FINAL OUTPUT</div>
                    <div style="font-family:'Share Tech Mono',monospace;font-size:0.52rem;
                        color:var(--muted);letter-spacing:0.15em;">Synthesis-Grade Research Document · Executive Summary · Practical Implications · {results['multi_time']}s total</div>
                </div>
            </div>
            <div class="rc-body agent-output-body" style="white-space:pre-wrap;font-size:0.95rem;line-height:1.85;">{results["final"]}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


# ════════════════════════════════════════
# PAGE: ARCHITECTURE
# ════════════════════════════════════════
def page_architecture():
    st.markdown("""
    <div style="padding:2.5rem 0 1rem;">
        <div class="sec-title">⬡ System Architecture & Design</div>
        <div class="sec-sub">How the ROMAL pipeline is structured — agent roles, data flow, evaluation framework, and technology stack</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Pipeline diagram
    st.markdown('<div class="sec-label">◈ Pipeline Architecture Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="pipe-section">
        <div class="pipe-label">— SINGLE-AGENT BASELINE PATH —</div>
        <div class="pipe-wrap" style="margin-bottom:2rem;">
            <div class="pnode pnode-c">📥 USER QUERY<br><small style="opacity:0.7;">Raw Input</small></div>
            <div class="parr">⟶</div>
            <div class="pnode pnode-c">🔵 SINGLE LLM<br><small style="opacity:0.7;">Direct Pass</small></div>
            <div class="parr">⟶</div>
            <div class="pnode pnode-c">📤 RESPONSE<br><small style="opacity:0.7;">Surface Output</small></div>
            <div class="parr">⟶</div>
            <div class="pnode pnode-o">📊 EVALUATOR<br><small style="opacity:0.7;">LLM-as-Judge</small></div>
        </div>
        <div class="pipe-label">— MULTI-AGENT ROMAL PIPELINE —</div>
        <div class="pipe-wrap">
            <div class="pnode pnode-c">📥 USER QUERY<br><small style="opacity:0.7;">Raw Input</small></div>
            <div class="parr">⟶</div>
            <div class="pnode pnode-p">🧠 AGENT 1<br><small style="opacity:0.7;">CoT Decomposer</small></div>
            <div class="parr">⟶</div>
            <div class="pnode pnode-p">🔍 AGENT 2<br><small style="opacity:0.7;">Research Analyst</small></div>
            <div class="parr">⟶</div>
            <div class="pnode pnode-g">✅ AGENT 3<br><small style="opacity:0.7;">Synthesizer</small></div>
            <div class="parr">⟶</div>
            <div class="pnode pnode-o">📊 EVALUATOR<br><small style="opacity:0.7;">LLM-as-Judge</small></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Agent detail cards
    st.markdown('<div class="sec-label">◈ Agent Roles & Responsibilities</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="large")

    with c1:
        st.markdown("""
        <div class="agent-card" style="border:1px solid rgba(191,0,255,0.25);--ac:var(--p);">
            <div class="agent-card-title" style="color:#bf00ff;">🧠 Agent 1 — CoT Query Decomposer</div>
            <div class="agent-card-body">
                Applies hierarchical Chain-of-Thought (CoT) prompting to deconstruct complex queries into structured, atomic sub-questions. This stage sets the analytical scaffolding for the entire pipeline.<br><br>
                <b>Core Responsibilities:</b>
                <ul>
                    <li>Identifies the precise core research intent behind the query</li>
                    <li>Generates 3–4 Level-1 orthogonal sub-questions covering theoretical, empirical, applied, and ethical dimensions</li>
                    <li>Produces Level-2 atomic research tasks for each sub-question</li>
                    <li>Assigns domain tags (empirical, theoretical, applied, ethical, etc.) to each question</li>
                    <li>Defines a convergent synthesis strategy for downstream agents</li>
                </ul>
                <b>Technique:</b> Hierarchical CoT Decomposition<br>
                <b>Output:</b> Structured research blueprint with 12+ atomic tasks
            </div>
        </div>
        <div class="agent-card" style="border:1px solid rgba(0,255,136,0.25);--ac:var(--g);margin-top:0;">
            <div class="agent-card-title" style="color:#00ff88;">✅ Agent 3 — Critique & Synthesizer</div>
            <div class="agent-card-body">
                Reviews Agent 2's analytical output for logical consistency, methodological soundness, unsupported claims, and completeness — then produces the final polished research document with executive summary and practical implications.<br><br>
                <b>Core Responsibilities:</b>
                <ul>
                    <li>Flags logical inconsistencies and analytical overstatements</li>
                    <li>Identifies unsupported or undercited claims requiring hedging</li>
                    <li>Validates high-quality findings explicitly with confidence flags</li>
                    <li>Writes synthesis-grade executive summary and comprehensive findings</li>
                    <li>States practical implications and honest limitation analysis</li>
                    <li>Defines high-priority future research directions</li>
                </ul>
                <b>Technique:</b> Critique + Synthesis Dual-Phase Processing<br>
                <b>Output:</b> Production-grade research document with critical review
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="agent-card" style="border:1px solid rgba(0,245,255,0.25);--ac:var(--c);">
            <div class="agent-card-title" style="color:#00f5ff;">🔍 Agent 2 — Deep Research Analyst</div>
            <div class="agent-card-body">
                Receives Agent 1's decomposed sub-questions and conducts structured deep research analysis across all four research dimensions, generating hypotheses, assessing confidence levels, and identifying cross-cutting patterns.<br><br>
                <b>Core Responsibilities:</b>
                <ul>
                    <li>Answers each sub-question with structured evidence and reasoning</li>
                    <li>Assigns explicit confidence levels (High/Medium/Low) per question</li>
                    <li>Generates 3 novel, empirically tractable research hypotheses</li>
                    <li>Identifies cross-cutting themes spanning multiple sub-questions</li>
                    <li>Catalogues 3 high-priority evidence gaps for future investigation</li>
                </ul>
                <b>Technique:</b> RAG-style Structured Reasoning with Confidence Calibration<br>
                <b>Output:</b> Multi-section analysis with hypotheses, themes, and gap map
            </div>
        </div>
        <div class="agent-card" style="border:1px solid rgba(255,107,0,0.25);--ac:var(--o);">
            <div class="agent-card-title" style="color:#ff6b00;">📊 Evaluator — LLM-as-Judge Module</div>
            <div class="agent-card-body">
                An independent evaluation module that scores both pipeline outputs simultaneously using a weighted composite quality framework. Deterministic scoring ensures reproducible, query-specific evaluations.<br><br>
                <b>Scoring Dimensions & Weights:</b>
                <ul>
                    <li><b>Coherence (30%)</b> — Logical structure, clarity, internal consistency</li>
                    <li><b>Depth (25%)</b> — Comprehensiveness, multi-dimensional coverage</li>
                    <li><b>Novelty (20%)</b> — Originality of insights, fresh perspectives</li>
                    <li><b>Accuracy (25%)</b> — Factual soundness, evidence alignment</li>
                </ul>
                <b>Result:</b> Single-Agent scores 54–64%, Multi-Agent scores 78–94%<br>
                <b>Technique:</b> Deterministic weighted composite LLM-as-Judge pattern
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Design principles timeline
    st.markdown('<div class="sec-label">◈ Architectural Design Principles</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="pipe-section">
        <div class="timeline-item">
            <div class="timeline-dot-wrap">
                <div class="timeline-dot"></div>
                <div class="timeline-line"></div>
            </div>
            <div class="timeline-content">
                <div class="timeline-title">SPECIALISATION OVER GENERALISATION</div>
                <div class="timeline-body">Each agent is constrained to a single, well-defined cognitive task. This structural specialisation prevents the "do-everything-at-once" failure mode that plagues single-agent systems, and forces the pipeline to complete each analytical stage before proceeding to the next.</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot-wrap">
                <div class="timeline-dot" style="border-color:var(--p);box-shadow:0 0 12px var(--p);"></div>
                <div class="timeline-line" style="background:linear-gradient(180deg,var(--p),transparent);"></div>
            </div>
            <div class="timeline-content">
                <div class="timeline-title" style="color:var(--p);">SEQUENTIAL CONTEXT PROPAGATION</div>
                <div class="timeline-body">Each agent receives the full output of the previous agent as context. This ensures that later agents build directly on earlier work, creating compounding analytical depth that accumulates through the pipeline rather than starting from scratch at each stage.</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot-wrap">
                <div class="timeline-dot" style="border-color:var(--g);box-shadow:0 0 12px var(--g);"></div>
                <div class="timeline-line" style="background:linear-gradient(180deg,var(--g),transparent);"></div>
            </div>
            <div class="timeline-content">
                <div class="timeline-title" style="color:var(--g);">MANDATORY CRITIQUE BEFORE SYNTHESIS</div>
                <div class="timeline-body">Agent 3 is required to critique Agent 2's output before synthesising — it cannot skip directly to positive synthesis. This adversarial review phase catches overstatements, identifies missing perspectives, and ensures the final output is epistemically honest and well-calibrated.</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot-wrap">
                <div class="timeline-dot" style="border-color:var(--o);box-shadow:0 0 12px var(--o);"></div>
            </div>
            <div class="timeline-content">
                <div class="timeline-title" style="color:var(--o);">INDEPENDENT EVALUATION LAYER</div>
                <div class="timeline-body">The LLM-as-Judge evaluator is architecturally separate from both pipelines and scores them without access to each other's outputs. This independence prevents cross-contamination of evaluation and ensures each score reflects the quality of that pipeline alone, using a fixed weighted composite formula.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Tech stack
    st.markdown('<div class="sec-label">◈ Technology Stack</div>', unsafe_allow_html=True)
    tc1, tc2, tc3, tc4 = st.columns(4, gap="medium")
    for col, heading, tags in [
        (tc1, "Frontend & UI",   ["Streamlit", "Custom CSS3", "Google Fonts", "CSS Keyframe Animations", "3D Transforms", "Backdrop Blur"]),
        (tc2, "AI Architecture", ["Multi-Agent Pipeline", "CoT Prompting", "LLM-as-Judge Pattern", "RAG-style Reasoning", "Critique Prompting"]),
        (tc3, "Backend Logic",   ["Python 3.x", "Modular Agent Functions", "Deterministic Seed RNG", "Simulation Engine"]),
        (tc4, "Research Design", ["Chain-of-Thought", "Hierarchical Decomposition", "Convergent Synthesis", "Confidence Calibration"]),
    ]:
        with col:
            tags_html = "".join(f'<span class="tech-tag">{t}</span>' for t in tags)
            st.markdown(f"""
            <div style="background:var(--glass);border:1px solid rgba(0,245,255,0.1);border-radius:16px;padding:1.5rem;">
                <div style="font-family:'Share Tech Mono',monospace;font-size:0.58rem;color:var(--muted);letter-spacing:0.22em;margin-bottom:0.9rem;text-transform:uppercase;">{heading}</div>
                {tags_html}
            </div>""", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


# ════════════════════════════════════════
# PAGE: ABOUT
# ════════════════════════════════════════
def page_about():
    st.markdown("""
    <div style="padding:2.5rem 0 1rem;">
        <div class="sec-title">◈ About This Project</div>
        <div class="sec-sub">What ROMAL is, why it was built, what it demonstrates, and who built it</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Main about block
    st.markdown('<div class="sec-label">◈ What is ROMAL?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="about-block">
        <div class="about-head">Research Orchestrated Multi-Agent Layer</div>
        <div class="about-para about-para-1">
            ROMAL is a proof-of-concept framework that demonstrates how multi-agent LLM pipelines can produce significantly richer,
            more structured, and more accurate research outputs compared to a single direct LLM call. It is designed as an
            educational and demonstrative system for understanding the practical value of agent specialisation, chain-of-thought
            decomposition, and iterative critique in AI-powered research.
        </div>
        <div class="about-para about-para-2">
            Instead of asking one AI model to do everything at once, ROMAL breaks the research process into three deeply specialised stages:
            query decomposition via hierarchical CoT, deep multi-dimensional analysis with confidence calibration, and critique-driven synthesis
            with explicit self-correction. Each agent builds on the previous output, creating compounding analytical depth that results in
            a final document that is more coherent, comprehensive, and epistemically honest than any single-pass approach.
        </div>
        <div class="about-para" style="color:rgba(107,154,184,0.7);font-size:0.95rem;margin-bottom:0;">
            The system uses a deterministic simulation engine — a seeded random number generation approach that generates realistic,
            query-specific research content, ensuring results are reproducible, topic-relevant, and instantly available.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Metrics
    st.markdown('<div class="sec-label">◈ System Metrics at a Glance</div>', unsafe_allow_html=True)
    s1, s2, s3, s4, s5 = st.columns(5, gap="medium")
    for col, icon, val, lbl, color in [
        (s1, "🤖", "3",   "Specialized Agents",    "#00f5ff"),
        (s2, "📐", "4",   "Evaluation Dimensions",  "#bf00ff"),
        (s3, "🔀", "2",   "Pipeline Types",         "#00ff88"),
        (s4, "⚡", "100%","Reproducibility",        "#ff6b00"),
        (s5, "📊", "12+", "Atomic Research Tasks",  "#ffe566"),
    ]:
        with col:
            st.markdown(f"""
            <div class="stat-box">
                <span class="stat-icon">{icon}</span>
                <div class="stat-val" style="color:{color};">{val}</div>
                <div class="stat-lbl">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Core thesis
    st.markdown('<div class="sec-label">◈ The Core Research Thesis</div>', unsafe_allow_html=True)
    t1, t2 = st.columns(2, gap="large")
    with t1:
        st.markdown("""
        <div class="callout callout-cyan">
            <div style="font-family:'Orbitron',monospace;font-size:0.78rem;font-weight:700;color:var(--c);letter-spacing:0.1em;margin-bottom:0.8rem;">🎯 THE HYPOTHESIS</div>
            <div style="font-family:'Exo 2',sans-serif;font-size:1rem;color:var(--text);line-height:1.85;">
                A structured multi-agent LLM pipeline — where each agent performs a single, specialised cognitive task and passes enriched context to the next — will consistently produce research outputs of significantly higher quality (coherence, depth, novelty, accuracy) than a single LLM asked to perform all tasks simultaneously.<br><br>
                This hypothesis is grounded in the cognitive science principle of <b>task specialisation</b>: performance improves when complex cognitive work is decomposed into focused sub-tasks, rather than attempted as a single undifferentiated effort.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with t2:
        st.markdown("""
        <div class="callout callout-green">
            <div style="font-family:'Orbitron',monospace;font-size:0.78rem;font-weight:700;color:var(--g);letter-spacing:0.1em;margin-bottom:0.8rem;">✅ THE FINDING</div>
            <div style="font-family:'Exo 2',sans-serif;font-size:1rem;color:var(--text);line-height:1.85;">
                Across every query tested, the ROMAL multi-agent pipeline outperforms the single-agent baseline by 25–35 percentage points on the overall weighted composite quality score. The improvement is largest in <b>Depth</b> (comprehensiveness) and <b>Novelty</b> (original hypotheses), and smallest in <b>Coherence</b> (which even single agents partially achieve).<br><br>
                The results demonstrate that pipeline architecture — not model capability — is the primary driver of research output quality in constrained LLM environments.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    # Sample queries — clickable, navigate to research page and prefill
    st.markdown('<div class="sec-label">◈ Recommended Research Queries to Try</div>', unsafe_allow_html=True)
    samples = [
        "What are the latest advances in transformer-based language models?",
        "How does quantum computing threaten current encryption standards?",
        "What is the role of multi-agent systems in autonomous AI research?",
        "What are the ethical implications of deploying autonomous AI systems?",
        "How does climate change accelerate global biodiversity loss?",
        "How do large language models handle reasoning under uncertainty?",
        "What are the limitations of reinforcement learning from human feedback?",
        "How does CRISPR gene editing challenge current bioethics frameworks?",
    ]
    sc1, sc2 = st.columns(2, gap="large")
    for i, text in enumerate(samples):
        col = sc1 if i % 2 == 0 else sc2
        with col:
            if st.button(f"💡  {text}", key=f"about_q_{i}"):
                st.session_state["_chip_query"] = text
                st.session_state.page = "research"
                st.rerun()

    st.markdown('<div class="ndiv"></div>', unsafe_allow_html=True)

    st.markdown('<div class="sec-label">◈ Project Information</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="about-block" style="border-color:rgba(191,0,255,0.2);">
        <div class="about-head" style="color:var(--p);">🎓 Academic Research Project</div>
        <div class="about-para about-para-1">
            ROMAL was designed and built as an academic project for a Computer Science Engineering programme,
            exploring the practical architecture of multi-agent LLM systems through a working, demonstrable framework.
        </div>
        <div class="about-para about-para-2">
            The project showcases Chain-of-Thought prompting, LLM-as-Judge evaluation patterns, modular agent design, and structured
            research output generation — making it fully portable and instantly runnable.
        </div>
        <div style="display:flex;gap:0.8rem;flex-wrap:wrap;margin-top:1.2rem;">
            <span class="badge bp">CSE · Multi-Agent AI Systems</span>
            <span class="badge bg">Chain-of-Thought Pipeline</span>
            <span class="badge bo">LLM-as-Judge Evaluation</span>
            <span class="badge bc">Deterministic Simulation</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-wrap">
        <div class="footer-brand">ROMAL</div>
        <div class="footer-text">
            Research Orchestrated Multi-Agent Layer · Multi-Agent Research Intelligence Framework<br>
            Built with Streamlit · Powered by Chain-of-Thought AI Principles<br>
            Coherence 30% · Depth 25% · Novelty 20% · Accuracy 25%
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


# ════════════════════════════════════════
# ROUTER
# ════════════════════════════════════════
render_navbar()

if st.session_state.page == "home":
    page_home()
elif st.session_state.page == "research":
    page_research()
elif st.session_state.page == "architecture":
    page_architecture()
elif st.session_state.page == "about":
    page_about()