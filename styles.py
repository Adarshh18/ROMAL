CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');
:root{--cyan:#00f5ff;--purple:#a855f7;--green:#00ff88;--orange:#ff6b00;--pink:#ff2d95;--dark:#030712;--card:rgba(6,18,42,0.85);--glass:rgba(6,18,42,0.6);--border:rgba(0,245,255,0.12);--t1:#e0f4ff;--t2:rgba(148,190,210,0.85);}
*{box-sizing:border-box;margin:0;padding:0;}
html,body,[data-testid="stAppViewContainer"],.stApp{background:var(--dark)!important;font-family:'Inter',sans-serif;overflow-x:hidden;}
#MainMenu,footer,header,[data-testid="stHeader"]{display:none!important;visibility:hidden!important;height:0!important;}
section[data-testid="stSidebar"]{display:none!important;}
.block-container{padding:0 2rem 2rem!important;max-width:1400px!important;}
[data-testid="stAppViewContainer"]>section>div.block-container{padding-top:0!important;}

/* ═══ BACKGROUND ═══ */
.stApp::before{content:'';position:fixed;inset:0;background:
  radial-gradient(ellipse 80% 50% at 10% 20%,rgba(0,100,255,0.07) 0%,transparent 60%),
  radial-gradient(ellipse 60% 40% at 85% 10%,rgba(168,85,247,0.06) 0%,transparent 50%),
  radial-gradient(ellipse 50% 50% at 50% 95%,rgba(0,245,255,0.04) 0%,transparent 50%);
  z-index:-2;pointer-events:none;animation:bgPulse 15s ease-in-out infinite alternate;}
@keyframes bgPulse{0%{opacity:.6}100%{opacity:1}}
.stApp::after{content:'';position:fixed;inset:0;background-image:
  linear-gradient(rgba(0,245,255,0.015) 1px,transparent 1px),
  linear-gradient(90deg,rgba(0,245,255,0.015) 1px,transparent 1px);
  background-size:80px 80px;z-index:-1;pointer-events:none;animation:gridFade 6s ease-in-out infinite;
  perspective:500px;transform:rotateX(2deg);}
@keyframes gridFade{0%,100%{opacity:.3}50%{opacity:.7}}

/* ═══ 3D CUBE ═══ */
.cube-scene{perspective:800px;width:160px;height:160px;position:relative;margin:0 auto;}
.cube-3d{width:100%;height:100%;position:relative;transform-style:preserve-3d;animation:cubeRotate 20s linear infinite;}
.cube-face{position:absolute;width:160px;height:160px;border:1.5px solid rgba(0,245,255,0.15);background:rgba(0,245,255,0.02);backdrop-filter:blur(2px);}
.cube-face:nth-child(1){transform:translateZ(80px);}
.cube-face:nth-child(2){transform:rotateY(180deg) translateZ(80px);}
.cube-face:nth-child(3){transform:rotateY(90deg) translateZ(80px);}
.cube-face:nth-child(4){transform:rotateY(-90deg) translateZ(80px);}
.cube-face:nth-child(5){transform:rotateX(90deg) translateZ(80px);}
.cube-face:nth-child(6){transform:rotateX(-90deg) translateZ(80px);}
@keyframes cubeRotate{from{transform:rotateX(0) rotateY(0)}to{transform:rotateX(360deg) rotateY(360deg)}}

/* ═══ 3D ORBITS ═══ */
.orbit-wrap{position:relative;width:280px;height:280px;margin:0 auto;transform-style:preserve-3d;perspective:600px;}
.orbit-ring{position:absolute;inset:0;border:1.5px solid transparent;border-radius:50%;transform-style:preserve-3d;}
.orbit-ring:nth-child(1){border-color:rgba(0,245,255,0.2);animation:orbitSpin1 8s linear infinite;}
.orbit-ring:nth-child(2){inset:20px;border-color:rgba(168,85,247,0.2);animation:orbitSpin2 12s linear infinite;}
.orbit-ring:nth-child(3){inset:40px;border-color:rgba(0,255,136,0.15);animation:orbitSpin3 16s linear infinite;}
.orbit-dot{position:absolute;width:6px;height:6px;border-radius:50%;top:-3px;left:50%;transform:translateX(-50%);}
.orbit-dot.d1{background:var(--cyan);box-shadow:0 0 12px var(--cyan);}
.orbit-dot.d2{background:var(--purple);box-shadow:0 0 12px var(--purple);}
.orbit-dot.d3{background:var(--green);box-shadow:0 0 12px var(--green);}
@keyframes orbitSpin1{from{transform:rotateX(70deg) rotateZ(0)}to{transform:rotateX(70deg) rotateZ(360deg)}}
@keyframes orbitSpin2{from{transform:rotateX(55deg) rotateY(30deg) rotateZ(0)}to{transform:rotateX(55deg) rotateY(30deg) rotateZ(-360deg)}}
@keyframes orbitSpin3{from{transform:rotateX(80deg) rotateY(-20deg) rotateZ(0)}to{transform:rotateX(80deg) rotateY(-20deg) rotateZ(360deg)}}

/* ═══ FLOATING 3D SHAPES ═══ */
.float-shape{position:fixed;pointer-events:none;z-index:-1;opacity:0.4;}
.hex{width:30px;height:34px;clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);}
.diamond{width:20px;height:20px;transform:rotate(45deg);}
@keyframes float3d1{0%,100%{transform:perspective(500px) translateY(0) rotateX(0) rotateY(0)}33%{transform:perspective(500px) translateY(-25px) rotateX(20deg) rotateY(15deg)}66%{transform:perspective(500px) translateY(15px) rotateX(-15deg) rotateY(-20deg)}}
@keyframes float3d2{0%,100%{transform:perspective(500px) translateY(0) rotateZ(0) scale(1)}50%{transform:perspective(500px) translateY(-30px) rotateZ(180deg) scale(1.15)}}
@keyframes float3d3{0%,100%{transform:perspective(500px) translateX(0) rotateY(0)}50%{transform:perspective(500px) translateX(20px) rotateY(180deg)}}

/* ═══ FIXED NAVBAR ═══ */
.nav-fixed{position:fixed;top:0;left:0;right:0;z-index:999999;background:rgba(3,7,18,0.92);backdrop-filter:blur(20px) saturate(1.4);border-bottom:1px solid rgba(0,245,255,0.1);padding:0.6rem 2.5rem;display:flex;align-items:center;justify-content:space-between;}
.nav-fixed::after{content:'';position:absolute;bottom:0;left:-100%;width:60%;height:1px;background:linear-gradient(90deg,transparent,var(--cyan),var(--purple),transparent);animation:navScan 5s linear infinite;}
@keyframes navScan{to{left:200%}}
.nav-brand{font-family:'Orbitron',monospace;font-weight:900;font-size:1.15rem;background:linear-gradient(135deg,var(--cyan),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:.12em;display:flex;align-items:center;gap:.5rem;}
.nav-brand .dot{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 10px var(--green);animation:dotPulse 2s infinite;}
@keyframes dotPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(.7)}}
.nav-links{display:flex;gap:.2rem;}
.nav-status{font-family:'Space Mono',monospace;font-size:.52rem;color:rgba(148,190,210,0.4);letter-spacing:.2em;}
.nav-spacer{height:52px;}

/* Streamlit nav buttons */
div[data-testid="stHorizontalBlock"] .stButton>button{
  font-family:'Space Mono',monospace!important;font-size:.58rem!important;letter-spacing:.14em!important;
  padding:.4rem 1.1rem!important;border-radius:6px!important;border:1px solid rgba(0,245,255,0.1)!important;
  background:transparent!important;color:rgba(148,190,210,0.7)!important;text-transform:uppercase!important;
  transition:all .25s cubic-bezier(.4,0,.2,1)!important;white-space:nowrap!important;min-width:100px!important;}
div[data-testid="stHorizontalBlock"] .stButton>button:hover{
  border-color:var(--cyan)!important;color:var(--cyan)!important;background:rgba(0,245,255,0.06)!important;
  box-shadow:0 0 20px rgba(0,245,255,0.15)!important;transform:translateY(-1px)!important;}

/* ═══ HERO ═══ */
.hero-wrap{text-align:center;padding:3rem 1rem 1rem;position:relative;}
.hero-tag{font-family:'Space Mono',monospace;color:var(--cyan);font-size:.65rem;letter-spacing:.5em;text-transform:uppercase;margin-bottom:1rem;animation:tagGlow 3s ease-in-out infinite;}
@keyframes tagGlow{0%,100%{opacity:.5;text-shadow:none}50%{opacity:1;text-shadow:0 0 20px rgba(0,245,255,.3)}}
.hero-title{font-family:'Orbitron',monospace;font-size:clamp(2.8rem,6vw,5rem);font-weight:900;line-height:1.05;
  background:linear-gradient(135deg,var(--cyan) 0%,#ffffff 40%,var(--purple) 70%,var(--pink) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-size:200% auto;
  animation:titleShimmer 4s linear infinite;filter:drop-shadow(0 0 40px rgba(0,245,255,.3));}
@keyframes titleShimmer{0%{background-position:0% center}100%{background-position:200% center}}
.hero-sub{font-family:'Inter',sans-serif;color:var(--t2);font-size:1.2rem;letter-spacing:.06em;margin-top:.7rem;font-weight:300;}
.hero-line{width:60%;max-width:400px;height:2px;margin:1.5rem auto;background:linear-gradient(90deg,transparent,var(--cyan),var(--purple),transparent);border-radius:2px;animation:lineExpand 4s ease-in-out infinite;}
@keyframes lineExpand{0%,100%{transform:scaleX(.6);opacity:.4}50%{transform:scaleX(1.1);opacity:1}}
.hero-badges{display:flex;justify-content:center;gap:.7rem;flex-wrap:wrap;margin:1.2rem 0 2rem;}
.hbadge{font-family:'Space Mono',monospace;font-size:.56rem;letter-spacing:.15em;padding:.3rem .9rem;border-radius:20px;
  border:1px solid;text-transform:uppercase;animation:badgePop .5s cubic-bezier(.175,.885,.32,1.275) both;
  transition:all .3s ease;cursor:default;}
.hbadge:hover{transform:translateY(-3px) scale(1.05)!important;}
.hb-c{color:var(--cyan);border-color:rgba(0,245,255,.3);background:rgba(0,245,255,.06);}
.hb-p{color:var(--purple);border-color:rgba(168,85,247,.3);background:rgba(168,85,247,.06);}
.hb-g{color:var(--green);border-color:rgba(0,255,136,.3);background:rgba(0,255,136,.06);}
.hb-o{color:var(--orange);border-color:rgba(255,107,0,.3);background:rgba(255,107,0,.06);}
.hbadge:nth-child(1){animation-delay:.1s}.hbadge:nth-child(2){animation-delay:.2s}.hbadge:nth-child(3){animation-delay:.3s}.hbadge:nth-child(4){animation-delay:.4s}
@keyframes badgePop{from{opacity:0;transform:scale(.6) translateY(10px)}to{opacity:1;transform:scale(1) translateY(0)}}

/* ═══ 3D CARDS ═══ */
.card-3d{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:1.8rem;
  backdrop-filter:blur(20px);transition:all .4s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;
  transform:perspective(800px) rotateX(0) rotateY(0);transform-style:preserve-3d;}
.card-3d::before{content:'';position:absolute;top:0;left:-100%;width:60%;height:1px;
  background:linear-gradient(90deg,transparent,var(--cyan),transparent);animation:cardSweep 6s linear infinite;}
@keyframes cardSweep{to{left:200%}}
.card-3d::after{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(0,245,255,0.03),transparent,rgba(168,85,247,0.03));opacity:0;transition:opacity .4s;}
.card-3d:hover{border-color:rgba(0,245,255,0.3);box-shadow:0 20px 60px rgba(0,0,0,.4),0 0 40px rgba(0,245,255,0.08);
  transform:perspective(800px) rotateX(2deg) rotateY(-2deg) translateY(-8px) scale(1.01);}
.card-3d:hover::after{opacity:1;}
.card-icon{font-size:2.5rem;margin-bottom:1rem;display:block;animation:iconFloat 5s ease-in-out infinite;}
@keyframes iconFloat{0%,100%{transform:translateY(0) rotateY(0)}50%{transform:translateY(-8px) rotateY(10deg)}}
.card-title{font-family:'Orbitron',monospace;font-size:.78rem;font-weight:700;color:var(--cyan);letter-spacing:.1em;margin-bottom:.5rem;}
.card-desc{font-family:'Inter',sans-serif;font-size:.92rem;color:var(--t2);line-height:1.7;}

/* ═══ SECTION STYLES ═══ */
.sec-t{font-family:'Orbitron',monospace;font-size:1.5rem;font-weight:700;color:var(--t1);letter-spacing:.08em;margin-bottom:.35rem;
  background:linear-gradient(135deg,var(--cyan),var(--t1));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.sec-s{font-family:'Inter',sans-serif;color:var(--t2);font-size:1rem;margin-bottom:1.8rem;font-weight:300;}
.sec-label{font-family:'Space Mono',monospace;color:var(--cyan);font-size:.62rem;letter-spacing:.25em;text-transform:uppercase;
  margin-bottom:1rem;padding-bottom:.4rem;border-bottom:1px solid rgba(0,245,255,0.1);display:flex;align-items:center;gap:.5rem;}
.sec-label::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,rgba(0,245,255,.15),transparent);}
.divider{height:2px;margin:2.5rem 0;background:linear-gradient(90deg,transparent,var(--cyan),var(--purple),transparent);opacity:.25;border-radius:2px;}

/* ═══ STATS ═══ */
.stat-card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.5rem 1rem;text-align:center;
  transition:all .35s cubic-bezier(.4,0,.2,1);transform:perspective(600px) rotateX(0);position:relative;overflow:hidden;}
.stat-card:hover{transform:perspective(600px) rotateX(5deg) translateY(-5px);border-color:rgba(0,245,255,.3);
  box-shadow:0 15px 40px rgba(0,0,0,.3),0 0 30px rgba(0,245,255,.1);}
.stat-val{font-family:'Orbitron',monospace;font-size:2.4rem;font-weight:900;line-height:1;}
.stat-lbl{font-family:'Space Mono',monospace;font-size:.55rem;letter-spacing:.2em;color:var(--t2);margin-top:.4rem;text-transform:uppercase;}

/* ═══ TIMELINE ═══ */
.tl-item{display:flex;gap:1.2rem;padding:1.2rem 0;position:relative;animation:tlSlide .5s ease both;}
@keyframes tlSlide{from{opacity:0;transform:translateX(-20px)}to{opacity:1;transform:translateX(0)}}
.tl-num{font-family:'Orbitron',monospace;font-size:1.6rem;font-weight:900;color:rgba(0,245,255,.15);flex-shrink:0;width:2.5rem;
  position:relative;}
.tl-num::after{content:'';position:absolute;left:50%;top:100%;width:1px;height:calc(100% + 1rem);background:rgba(0,245,255,.08);}
.tl-head{font-family:'Space Mono',monospace;font-size:.65rem;letter-spacing:.12em;color:var(--cyan);margin-bottom:.3rem;}
.tl-body{font-family:'Inter',sans-serif;font-size:.95rem;color:var(--t2);line-height:1.7;}

/* ═══ QUERY BOX ═══ */
.qbox{background:var(--card);border:1px solid rgba(0,245,255,0.2);border-radius:18px;padding:2rem;margin-bottom:1.2rem;
  position:relative;overflow:hidden;animation:qboxIn .6s cubic-bezier(.175,.885,.32,1.275) both;}
@keyframes qboxIn{from{opacity:0;transform:translateY(25px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.qbox::before{content:'';position:absolute;top:0;left:-100%;width:50%;height:2px;
  background:linear-gradient(90deg,transparent,var(--cyan),var(--purple),transparent);animation:navScan 4s linear infinite;}
.chip{display:inline-block;font-family:'Inter',sans-serif;font-size:.8rem;color:var(--t2);border:1px solid rgba(148,190,210,0.15);
  background:rgba(148,190,210,0.04);border-radius:20px;padding:.22rem .75rem;margin:.18rem;transition:all .25s;cursor:pointer;}
.chip:hover{border-color:var(--cyan);color:var(--cyan);background:rgba(0,245,255,.05);transform:translateY(-2px);}

/* ═══ INPUTS ═══ */
.stTextArea textarea{background:rgba(3,7,18,.9)!important;border:1px solid rgba(0,245,255,.18)!important;border-radius:12px!important;
  color:var(--t1)!important;font-family:'Inter',sans-serif!important;font-size:1rem!important;caret-color:var(--cyan)!important;
  transition:all .3s!important;}
.stTextArea textarea:focus{border-color:var(--cyan)!important;box-shadow:0 0 30px rgba(0,245,255,.1)!important;}
label{font-family:'Space Mono',monospace!important;color:var(--cyan)!important;font-size:.6rem!important;letter-spacing:.2em!important;text-transform:uppercase!important;}

/* ═══ MAIN CTA BUTTON ═══ */
.stButton>button{width:100%;background:linear-gradient(135deg,rgba(0,245,255,.1),rgba(168,85,247,.1))!important;
  border:1px solid var(--cyan)!important;color:var(--cyan)!important;font-family:'Orbitron',monospace!important;
  font-size:.75rem!important;font-weight:700!important;letter-spacing:.12em!important;padding:.8rem 2rem!important;
  border-radius:10px!important;text-transform:uppercase!important;transition:all .35s cubic-bezier(.4,0,.2,1)!important;
  position:relative!important;overflow:hidden!important;}
.stButton>button:hover{background:linear-gradient(135deg,rgba(0,245,255,.22),rgba(168,85,247,.22))!important;
  box-shadow:0 0 40px rgba(0,245,255,.3),0 0 80px rgba(168,85,247,.12)!important;
  transform:translateY(-3px)!important;border-color:#fff!important;color:#fff!important;}

/* ═══ STATUS LINE ═══ */
.sline{font-family:'Space Mono',monospace;font-size:.68rem;color:var(--cyan);letter-spacing:.08em;padding:.4rem 0;
  display:flex;align-items:center;gap:.5rem;animation:slideIn .4s ease both;}
@keyframes slideIn{from{opacity:0;transform:translateX(-12px)}to{opacity:1;transform:translateX(0)}}
.blink{animation:blnk .9s step-end infinite;}
@keyframes blnk{0%,100%{opacity:1}50%{opacity:0}}

/* ═══ WINNER BANNER ═══ */
.winner{background:linear-gradient(135deg,rgba(0,255,136,.06),rgba(0,245,255,.06));border:1px solid var(--green);
  border-radius:14px;padding:1.2rem 2rem;text-align:center;margin:2rem 0;position:relative;overflow:hidden;
  animation:winPop .6s cubic-bezier(.175,.885,.32,1.275) both,winGlow 2.5s .6s ease-in-out infinite;}
@keyframes winPop{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:scale(1)}}
@keyframes winGlow{0%,100%{box-shadow:0 0 20px rgba(0,255,136,.12)}50%{box-shadow:0 0 60px rgba(0,255,136,.35)}}
.winner::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(0,255,136,.03),transparent);animation:winSweep 3s linear infinite;}
@keyframes winSweep{from{transform:translateX(-100%)}to{transform:translateX(100%)}}
.win-t{font-family:'Orbitron',monospace;font-size:1rem;font-weight:900;color:var(--green);letter-spacing:.12em;}
.win-s{font-family:'Inter',sans-serif;color:var(--t2);font-size:.85rem;margin-top:.3rem;}

/* ═══ RESULT CARDS ═══ */
.rcard{background:var(--card);border-radius:16px;padding:1.8rem;backdrop-filter:blur(20px);position:relative;overflow:hidden;
  transition:all .4s ease;animation:rcardIn .5s cubic-bezier(.175,.885,.32,1.275) both;}
@keyframes rcardIn{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
.rcard:hover{transform:translateY(-5px);}
.rcard-s{border:1px solid rgba(77,169,255,.35);box-shadow:0 0 30px rgba(77,169,255,.08);}
.rcard-m{border:1px solid rgba(0,255,136,.35);box-shadow:0 0 30px rgba(0,255,136,.08);}
.rcard-s::after,.rcard-m::after{content:'';position:absolute;top:0;left:0;right:0;height:2px;}
.rcard-s::after{background:linear-gradient(90deg,transparent,#4da9ff,transparent);}
.rcard-m::after{background:linear-gradient(90deg,transparent,var(--green),transparent);}
.rcard-hdr{display:flex;align-items:center;gap:.8rem;margin-bottom:1.2rem;padding-bottom:.8rem;border-bottom:1px solid rgba(255,255,255,.05);}
.rcard-icon{font-size:1.5rem;}.rcard-title{font-family:'Orbitron',monospace;font-size:.78rem;font-weight:700;letter-spacing:.1em;}
.rcard-tb{color:#4da9ff;}.rcard-tg{color:var(--green);}
.rcard-body{font-family:'Inter',sans-serif;font-size:.92rem;color:var(--t1);line-height:1.75;white-space:pre-wrap;}
.lat-chip{display:inline-block;font-family:'Space Mono',monospace;font-size:.55rem;padding:.18rem .55rem;border-radius:20px;border:1px solid;}
.lat-b{color:#4da9ff;border-color:rgba(77,169,255,.35);background:rgba(77,169,255,.06);}
.lat-g{color:var(--green);border-color:rgba(0,255,136,.35);background:rgba(0,255,136,.06);}

/* ═══ AGENT STEPS ═══ */
.ast{background:rgba(3,7,18,.6);border-left:2px solid;border-radius:0 10px 10px 0;padding:.75rem 1rem;margin-bottom:.6rem;transition:all .3s;}
.ast:hover{background:rgba(6,18,42,.9);transform:translateX(4px);}
.ast-1{border-color:var(--purple);}.ast-2{border-color:var(--cyan);}.ast-3{border-color:var(--green);}
.ast-lbl{font-family:'Space Mono',monospace;font-size:.55rem;letter-spacing:.1em;color:var(--t2);margin-bottom:.25rem;}
.ast-txt{font-family:'Inter',sans-serif;font-size:.88rem;color:var(--t1);line-height:1.55;}

/* ═══ METRIC BARS ═══ */
.mwrap{margin-top:1.4rem;padding-top:1.1rem;border-top:1px solid rgba(255,255,255,.05);}
.mrow{display:flex;align-items:center;gap:.7rem;margin-bottom:.65rem;}
.mlbl{font-family:'Space Mono',monospace;font-size:.55rem;color:var(--t2);letter-spacing:.08em;width:82px;flex-shrink:0;}
.mtrack{flex:1;height:5px;background:rgba(255,255,255,.05);border-radius:3px;overflow:hidden;}
.mfill{height:100%;border-radius:3px;animation:barGrow 1.2s cubic-bezier(.4,0,.2,1) both;}
@keyframes barGrow{from{width:0!important}}
.mval{font-family:'Orbitron',monospace;font-size:.62rem;font-weight:700;width:36px;text-align:right;flex-shrink:0;}

/* ═══ PIPELINE NODES ═══ */
.pwrap{display:flex;align-items:center;justify-content:center;gap:.5rem;flex-wrap:wrap;margin:1.2rem 0;}
.pnode{background:var(--card);border:1px solid;border-radius:10px;padding:.6rem .9rem;text-align:center;
  font-family:'Space Mono',monospace;font-size:.58rem;min-width:92px;line-height:1.5;transition:all .35s;
  transform:perspective(600px) rotateX(0);}
.pnode:hover{transform:perspective(600px) rotateX(8deg) translateY(-6px) scale(1.05);}
.pnc{border-color:var(--cyan);color:var(--cyan);box-shadow:0 0 15px rgba(0,245,255,.1);}
.pnp{border-color:var(--purple);color:var(--purple);box-shadow:0 0 15px rgba(168,85,247,.1);}
.png{border-color:var(--green);color:var(--green);box-shadow:0 0 15px rgba(0,255,136,.1);}
.pno{border-color:var(--orange);color:var(--orange);box-shadow:0 0 15px rgba(255,107,0,.1);}
.parr{color:rgba(0,245,255,.35);font-size:1.2rem;animation:arrBounce 1.5s ease-in-out infinite;}
@keyframes arrBounce{0%,100%{transform:translateX(-4px);opacity:.3}50%{transform:translateX(4px);opacity:1}}

/* ═══ ARCH CARDS ═══ */
.acard{background:var(--card);border-radius:14px;padding:1.6rem;margin-bottom:1.1rem;transition:all .35s;border:1px solid;
  transform:perspective(600px) rotateX(0);overflow:hidden;position:relative;}
.acard:hover{transform:perspective(600px) rotateX(3deg) translateY(-5px);box-shadow:0 15px 40px rgba(0,0,0,.3);}
.acard::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,currentColor,transparent);opacity:.3;}
.acard-t{font-family:'Orbitron',monospace;font-size:.82rem;font-weight:700;margin-bottom:.6rem;letter-spacing:.08em;}
.acard-b{font-family:'Inter',sans-serif;font-size:.92rem;color:var(--t2);line-height:1.7;}
.acard-b b{color:var(--t1);}.acard-b ul{margin:.4rem 0 .4rem 1.2rem;}.acard-b li{margin-bottom:.2rem;}
.ttag{display:inline-block;font-family:'Space Mono',monospace;font-size:.55rem;letter-spacing:.1em;padding:.22rem .7rem;
  border-radius:20px;border:1px solid rgba(168,85,247,.3);color:var(--purple);background:rgba(168,85,247,.05);
  margin:.18rem;transition:all .25s;}
.ttag:hover{border-color:var(--cyan);color:var(--cyan);background:rgba(0,245,255,.05);transform:translateY(-2px);}

/* ═══ ABOUT BLOCKS ═══ */
.ab{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:2.2rem;margin-bottom:1.8rem;
  transform:perspective(600px) rotateX(0);transition:all .35s;}
.ab:hover{transform:perspective(600px) rotateX(2deg) translateY(-4px);box-shadow:0 15px 40px rgba(0,0,0,.3);}
.ab-h{font-family:'Orbitron',monospace;font-size:1rem;font-weight:700;color:var(--cyan);margin-bottom:.9rem;letter-spacing:.08em;}
.ab-p{font-family:'Inter',sans-serif;font-size:1rem;line-height:1.85;margin-bottom:.9rem;color:var(--t2);}
.feat-item{display:flex;align-items:flex-start;gap:.6rem;padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.03);
  font-family:'Inter',sans-serif;font-size:.92rem;color:var(--t2);transition:all .2s;}
.feat-item:hover{color:var(--t1);padding-left:.4rem;}
.feat-item:last-child{border-bottom:none;}

/* ═══ EXPANDER ═══ */
.streamlit-expanderHeader{background:rgba(6,18,42,.7)!important;border:1px solid rgba(0,245,255,.1)!important;border-radius:10px!important;
  color:var(--cyan)!important;font-family:'Space Mono',monospace!important;font-size:.63rem!important;}

/* ═══ SCROLLBAR ═══ */
::-webkit-scrollbar{width:5px;}::-webkit-scrollbar-track{background:var(--dark);}
::-webkit-scrollbar-thumb{background:linear-gradient(var(--cyan),var(--purple));border-radius:3px;}

/* ═══ FOOTER ═══ */
.footer{text-align:center;padding:2rem 1rem;opacity:.3;font-family:'Space Mono',monospace;font-size:.5rem;
  color:var(--t2);letter-spacing:.25em;line-height:2.2;}
</style>
"""

PARTICLES = """
<div class="nav-fixed">
  <div class="nav-brand"><span class="dot"></span> ROMAL</div>
  <div class="nav-status">RESEARCH INTELLIGENCE v2.0</div>
</div>
<div class="nav-spacer"></div>

<div class="float-shape hex" style="left:5%;top:15%;background:rgba(0,245,255,0.08);animation:float3d1 12s ease-in-out infinite;"></div>
<div class="float-shape diamond" style="left:90%;top:25%;background:rgba(168,85,247,0.08);border:1px solid rgba(168,85,247,0.15);animation:float3d2 15s ease-in-out infinite;"></div>
<div class="float-shape hex" style="left:80%;top:60%;background:rgba(0,255,136,0.06);animation:float3d3 18s ease-in-out infinite;"></div>
<div class="float-shape diamond" style="left:12%;top:70%;background:rgba(0,245,255,0.06);border:1px solid rgba(0,245,255,0.1);animation:float3d1 20s ease-in-out infinite 2s;"></div>
<div class="float-shape hex" style="left:50%;top:40%;background:rgba(255,45,149,0.05);animation:float3d2 14s ease-in-out infinite 1s;"></div>
<div class="float-shape diamond" style="left:35%;top:85%;background:rgba(168,85,247,0.05);border:1px solid rgba(168,85,247,0.1);animation:float3d3 16s ease-in-out infinite 3s;"></div>
"""

CUBE_HTML = """
<div class="orbit-wrap">
  <div class="orbit-ring"><div class="orbit-dot d1"></div></div>
  <div class="orbit-ring"><div class="orbit-dot d2"></div></div>
  <div class="orbit-ring"><div class="orbit-dot d3"></div></div>
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">
    <div class="cube-scene">
      <div class="cube-3d">
        <div class="cube-face"></div><div class="cube-face"></div><div class="cube-face"></div>
        <div class="cube-face"></div><div class="cube-face"></div><div class="cube-face"></div>
      </div>
    </div>
  </div>
</div>
"""
