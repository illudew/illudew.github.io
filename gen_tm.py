# -*- coding: utf-8 -*-
"""Generate theoretical-mechanics.html from PDF lecture notes content."""
import json

# ---------- SVG figure library ----------
FIG = {
"pendulum": '''<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg">
<line x1="60" y1="10" x2="60" y2="130" stroke="#475569" stroke-width="2"/>
<circle cx="60" cy="135" r="18" fill="#60a5fa" stroke="#2563eb" stroke-width="2"/>
<path d="M60 10 L40 10 L60 25 Z" fill="#94a3b8"/></svg>''',
"double_pendulum": '''<svg viewBox="0 0 160 200" xmlns="http://www.w3.org/2000/svg">
<line x1="80" y1="10" x2="80" y2="80" stroke="#475569" stroke-width="2"/>
<circle cx="80" cy="85" r="14" fill="#60a5fa" stroke="#2563eb" stroke-width="2"/>
<line x1="80" y1="85" x2="110" y2="160" stroke="#475569" stroke-width="2"/>
<circle cx="110" cy="165" r="14" fill="#34d399" stroke="#059669" stroke-width="2"/>
<path d="M80 10 L60 10 L80 25 Z" fill="#94a3b8"/></svg>''',
"central_force": '''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="100" cy="80" r="8" fill="#f59e0b"/>
<ellipse cx="100" cy="80" rx="70" ry="40" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="160" cy="80" r="7" fill="#ef4444"/>
<line x1="100" y1="80" x2="160" y2="80" stroke="#94a3b8" stroke-dasharray="4 3"/></svg>''',
"rigid_body": '''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="100" cy="80" rx="60" ry="40" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<line x1="40" y1="80" x2="160" y2="80" stroke="#ef4444" stroke-width="2" stroke-dasharray="5 3"/>
<circle cx="100" cy="80" r="4" fill="#1e293b"/>
<text x="105" y="70" font-size="11" fill="#1e293b">ω</text></svg>''',
"euler_angles": '''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="120" x2="180" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="100" y1="20" x2="100" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="100" y1="120" x2="160" y2="60" stroke="#3b82f6" stroke-width="2.5"/>
<line x1="100" y1="120" x2="40" y2="60" stroke="#10b981" stroke-width="2.5"/>
<path d="M130 120 A30 30 0 0 0 116 94" fill="none" stroke="#f59e0b" stroke-width="2"/>
<text x="125" y="100" font-size="11" fill="#f59e0b">φ</text></svg>''',
"phase_space": '''<svg viewBox="0 0 180 140" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="120" x2="170" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="120" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<ellipse cx="95" cy="70" rx="55" ry="35" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="150" cy="70" r="3" fill="#ef4444"/>
<text x="155" y="74" font-size="11" fill="#ef4444">H=E</text></svg>''',
"poisson": '''<svg viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg">
<circle cx="60" cy="60" r="35" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="140" cy="60" r="35" fill="none" stroke="#10b981" stroke-width="2"/>
<text x="50" y="64" font-size="11" fill="#2563eb">f</text>
<text x="130" y="64" font-size="11" fill="#059669">g</text>
<text x="92" y="55" font-size="11" fill="#ef4444">{f,g}</text></svg>''',
"kepler": '''<svg viewBox="0 0 220 140" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="110" cy="70" rx="90" ry="45" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="60" cy="70" r="10" fill="#f59e0b"/>
<circle cx="150" cy="80" r="7" fill="#3b82f6"/>
<line x1="60" y1="70" x2="150" y2="80" stroke="#94a3b8" stroke-dasharray="4 3"/>
<text x="60" y="55" font-size="10" fill="#f59e0b">太阳</text>
<text x="150" y="100" font-size="10" fill="#3b82f6">行星</text></svg>''',
}

# ---------- tag labels ----------
TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

# ---------- helpers ----------
def js_escape(s):
    return s.replace("\\","\\\\").replace("`","\\`").replace("${","\\${")

def defn(t, body):
    return f'<section class="la-kp-sec la-kp-def"><h5>定 义</h5><p><strong>{t}</strong></p>{body}</section>'
def thm(t, body):
    return f'<section class="la-kp-sec la-kp-thm"><h5>定 理 · {t}</h5>{body}</section>'
def der(body):
    return f'<section class="la-kp-sec la-kp-der"><h5>推 导</h5>{body}</section>'
def exa(body):
    return f'<section class="la-kp-sec la-kp-exa"><h5>例 子</h5>{body}</section>'
def app(body):
    return f'<section class="la-kp-sec la-kp-app"><h5>应 用</h5>{body}</section>'
def note(body):
    return f'<section class="la-kp-sec la-kp-note"><h5>备 注</h5>{body}</section>'
def fml(latex, caption=""):
    cap = f'<span class="note">{caption}</span>' if caption else ""
    return f'<div class="la-fml">$${latex}$$ {cap}</div>'
def p(txt):
    return f'<p>{txt}</p>'
def wrap(body):
    return f'<div class="la-kp">{body}</div>'

# =====================================================
#  CHAPTER 1: 拉格朗日力学
# =====================================================
ch1_sections = [

# ---- 1.1 约束与广义坐标 ----
{
"name": "1.1 约束与广义坐标",
"color": "#2563eb",
"desc": "完整约束、非完整约束、广义坐标、虚位移与理想约束",
"items": [
{"id":"tm-c1s1-1","name":"约束的概念","tags":["def","exa"],"brief":"对运动的限制，纯运动学概念。",
 "body": wrap(
    defn("约束", p("约束是对运动的限制，是一个纯运动学的概念。对于 $n$ 个质点组成的体系，约束方程限制了质点坐标之间的关系。"))
    + exa(p("<strong>单摆：</strong>约束方程 $x^2+y^2=L^2$。<br><strong>光滑球形碗内小球：</strong>$x^2+y^2+z^2=R^2$。<br><strong>轻杆连接两质点：</strong>$(x_1-x_2)^2+(y_1-y_2)^2+(z_1-z_2)^2=L^2$。<br><strong>刚体：</strong>任意两点间距固定，$|\\vec r_i-\\vec r_j|=$ 常数。"))
)},
{"id":"tm-c1s1-2","name":"完整约束","tags":["def","thm","exa"],"brief":"仅含坐标与时间的约束。",
 "body": wrap(
    defn("完整约束", p("约束条件只和体系各质点的坐标 $\\vec r_i$ 及时间 $t$ 相关的约束称为完整约束，其约束方程为")+
    fml("f_j(\\vec r_1,\\vec r_2,\\dots,\\vec r_n,t)=0,\\quad 1\\le j\\le k",
        "由约束方程可消去 $k$ 个不独立坐标，独立坐标数目由 $3n$ 减为 $3n-k$，即系统自由度。"))
    + thm("几何意义", p("约束确定了 $3n$ 维欧几里得空间的一个 $3n-k$ 维高维曲面（流形）。"))
    + exa(p("<strong>刚体：</strong>欧几里得空间 $\\mathbb R^{3N}$，曲面为 $\\mathbb R^3\\times SO(3)$，其中 $SO(3)=\\{M|M^T M=I_3,\\det M=1\\}$。"))
)},
{"id":"tm-c1s1-3","name":"广义坐标","tags":["def","exa","note"],"brief":"确定体系构型的独立坐标。",
 "body": wrap(
    defn("广义坐标", p("确定一个力学体系构型所需要的独立坐标称为广义坐标，记为 $q_\\alpha$（$\\alpha=1,\\dots,s$，$s$ 为自由度）。"))
    + exa(p("<strong>球面上运动的小球：</strong>广义坐标为 $(\\theta,\\varphi)$。<br><strong>刚体：</strong>广义坐标为 $(x_0,y_0,z_0)$ 及三个欧拉角。"))
    + note(p("广义坐标选取不唯一；广义坐标与系统构型不一定一一对应（如球面南极点 $\\theta=\\pi$ 对应任意 $\\varphi$），因此高维曲面需要用多个坐标系（图册）覆盖。"))
)},
{"id":"tm-c1s1-4","name":"非完整约束","tags":["def","thm","exa"],"brief":"含速度且不可积的约束。",
 "body": wrap(
    defn("非完整约束", p("形如 $f(\\vec r_1,\\dots,\\vec r_n,\\dot{\\vec r}_1,\\dots,\\dot{\\vec r}_n,t)=0$，且不能化为 $g(\\vec r_1,\\dots,\\vec r_n,t)=0$ 形式的约束称为非完整约束。其特点是无法减少独立坐标数目。"))
    + thm("线性约束可积的充要条件", p("线性微分约束 $\\sum_i(A_i dx_i+B_i dy_i+C_i dz_i)+D\\,dt=0$ 为完整约束的充要条件是可化为全微分形式，即存在 $\\Phi$ 和 $F$ 使左边 $=\\Phi\\,dF$。等价地，$\\omega\\wedge d\\omega=0$，其中 $\\omega$ 为左边的微分形式。"))
    + exa(p("<strong>$x\\dot x+y\\dot y=0$ 是完整约束：</strong>因 $x\\dot x+y\\dot y=\\frac{d(x^2+y^2)}{2dt}=0$，积分得 $x^2+y^2=$ 常数。<br><strong>平面纯滚动圆盘是非完整约束：</strong>$\\dot x=r\\dot\\varphi\\sin\\theta$，$\\dot y=-r\\dot\\varphi\\cos\\theta$，不可积。"))
)},
{"id":"tm-c1s1-5","name":"虚位移与理想约束","tags":["def","thm","der","exa"],"brief":"固定时刻约束允许的无穷小位移；约束力虚功和为零。",
 "body": wrap(
    defn("虚位移", p("固定时刻 $t$，约束所允许的无穷小位移称为虚位移，记为 $(\\delta\\vec r_1,\\delta\\vec r_2,\\dots,\\delta\\vec r_n)$。几何上，构型 $P$ 处所有虚位移张成的线性空间是 $3n-k$ 维流形在 $P$ 点的切空间。"))
    + defn("理想约束", p("约束力虚功和恒为零的约束称为理想约束：")+
    fml("\\sum_{i=1}^{n} \\vec F_{Ni}\\cdot\\delta\\vec r_i = 0",
        "几何意义：约束力沿高维曲面法向（对完整约束）。"))
    + der(p("对于刚性轻杆连接的两质点，$\\vec F_{N1}\\parallel(\\vec r_1-\\vec r_2)$，$\\vec F_{N2}=-\\vec F_{N1}$，则 $\\vec F_{N1}\\cdot\\delta\\vec r_1+\\vec F_{N2}\\cdot\\delta\\vec r_2=\\lambda(\\vec r_1-\\vec r_2)\\cdot\\delta(\\vec r_1-\\vec r_2)=\\frac{\\lambda}{2}\\delta[(\\vec r_1-\\vec r_2)^2]=0$（刚性保证间距不变）。"))
    + exa(p("理想约束实例：光滑曲面、刚性轻杆、刚体、光滑接触表面、纯滚动（完全粗糙）接触。"))
)},
],
},

# ---- 1.2 达朗贝尔方程与拉格朗日方程 ----
{
"name": "1.2 达朗贝尔方程与拉格朗日方程",
"color": "#0d9488",
"desc": "从牛顿力学到拉格朗日力学的核心推导",
"items": [
{"id":"tm-c1s2-1","name":"达朗贝尔方程","tags":["thm","der","note"],"brief":"消去约束力后的动力学方程。",
 "body": wrap(
    thm("达朗贝尔方程", p("对理想约束体系，由牛顿第二定律 $m_i\\ddot{\\vec r}_i=\\vec F_i+\\vec F_{Ni}$，考虑虚位移 $\\delta\\vec r_i$ 并求和，利用理想约束条件 $\\sum\\vec F_{Ni}\\cdot\\delta\\vec r_i=0$，得")+
    fml("\\sum_{i}\\left(\\vec F_i - m_i\\ddot{\\vec r}_i\\right)\\cdot\\delta\\vec r_i = 0",
        "若约束为理想完整约束，独立虚位移数目为 $3n-k$，故上式含 $3n-k$ 个独立方程。"))
    + der(p("该方程实现了从含约束力的牛顿方程到不含约束力方程的转化。"))
)},
{"id":"tm-c1s2-2","name":"经典拉格朗日关系","tags":["thm","der"],"brief":"广义坐标与速度的偏导互换关系。",
 "body": wrap(
    thm("经典拉格朗日关系", p("若把广义坐标 $q_\\alpha$ 与广义速度 $\\dot q_\\alpha$ 视为独立变量，则有")+
    fml("\\frac{\\partial\\dot{\\vec r}_i}{\\partial\\dot q_\\alpha} = \\frac{\\partial\\vec r_i}{\\partial q_\\alpha},\\qquad \\frac{d}{dt}\\frac{\\partial\\vec r_i}{\\partial q_\\alpha} = \\frac{\\partial\\dot{\\vec r}_i}{\\partial q_\\alpha}"))
    + der(p("由链式法则 $\\dot{\\vec r}_i=\\sum_\\alpha\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\dot q_\\alpha+\\frac{\\partial\\vec r_i}{\\partial t}$，对 $\\dot q_\\alpha$ 求偏导即得第一式；对 $q_\\alpha$ 求偏导并与 $\\frac{d}{dt}\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}$ 比较即得第二式。"))
)},
{"id":"tm-c1s2-3","name":"广义力","tags":["def","thm"],"brief":"主动力在广义坐标方向的投影。",
 "body": wrap(
    defn("广义力", p("对应广义坐标 $q_\\alpha$ 的广义力定义为")+
    fml("Q_\\alpha = \\sum_{i=1}^{n} \\vec F_i \\cdot \\frac{\\partial\\vec r_i}{\\partial q_\\alpha}"))
    + thm("保守力的广义力", p("若力为保守力 $\\vec F_i=-\\nabla_i V$，则")+
    fml("Q_\\alpha = -\\sum_i \\frac{\\partial V}{\\partial\\vec r_i}\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha} = -\\frac{\\partial V}{\\partial q_\\alpha}"))
)},
{"id":"tm-c1s2-4","name":"欧拉-拉格朗日方程","tags":["def","thm","der","exa","app"],"brief":"理想完整保守体系的运动方程。",
 "body": wrap(
    defn("拉格朗日函数", p("拉格朗日函数定义为动能减势能：")+
    fml("L = T - V"))
    + thm("欧拉-拉格朗日方程", p("对于理想、完整约束且主动力均为保守力的体系，运动方程为")+
    fml("\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha} - \\frac{\\partial L}{\\partial q_\\alpha} = 0,\\qquad 1\\le\\alpha\\le s",
        "其中 $s=3n-k$ 为自由度。"))
    + der(p("由达朗贝尔方程 $\\sum(\\vec F_i-m_i\\ddot{\\vec r}_i)\\cdot\\delta\\vec r_i=0$，代入 $\\delta\\vec r_i=\\sum_\\alpha\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\delta q_\\alpha$，利用经典拉格朗日关系化简得 $\\frac{d}{dt}\\frac{\\partial T}{\\partial\\dot q_\\alpha}-\\frac{\\partial T}{\\partial q_\\alpha}=Q_\\alpha$。对保守力 $Q_\\alpha=-\\frac{\\partial V}{\\partial q_\\alpha}$，且 $V$ 不含 $\\dot q$，故得欧拉-拉格朗日方程。"))
    + exa(p("<strong>质点+悬挂重物体系：</strong>取 $R,\\varphi$ 为广义坐标，$L=\\frac{1}{2}(m+m')\\dot R^2+\\frac{1}{2}mR^2\\dot\\varphi^2-m'g(R-l)$。代入拉格朗日方程得 $(m+m')\\ddot R-mR\\dot\\varphi^2+m'g=0$ 和 $\\frac{d}{dt}(mR^2\\dot\\varphi)=0$。"))
    + app(p("拉格朗日方程无需分析约束力，只需写出 $T$ 和 $V$ 即可，极大简化求解。"))
)},
{"id":"tm-c1s2-5","name":"拉格朗日函数的不唯一性","tags":["thm","der"],"brief":"全导数项不改变运动方程。",
 "body": wrap(
    thm("规范不变性", p("设 $L'=L+\\frac{df}{dt}$，其中 $f=f(q_1,\\dots,q_s,t)$。若 $q_\\alpha(t)$ 是 $L$ 对应的欧拉-拉格朗日方程的解，则它也是 $L'$ 对应的方程的解。"))
    + der(p("由 $\\frac{df}{dt}=\\sum_\\alpha\\frac{\\partial f}{\\partial q_\\alpha}\\dot q_\\alpha+\\frac{\\partial f}{\\partial t}$，得 $\\frac{\\partial}{\\partial\\dot q_\\alpha}\\frac{df}{dt}=\\frac{\\partial f}{\\partial q_\\alpha}$。进而 $\\frac{d}{dt}\\frac{\\partial}{\\partial\\dot q_\\alpha}\\frac{df}{dt}-\\frac{\\partial}{\\partial q_\\alpha}\\frac{df}{dt}=0$（混合偏导可交换）。"))
)},
{"id":"tm-c1s2-6","name":"循环坐标与守恒量","tags":["def","thm","app"],"brief":"拉格朗日函数中不显含的坐标对应守恒量。",
 "body": wrap(
    defn("循环坐标", p("若拉格朗日函数 $L$ 不显含某个广义坐标 $q_\\alpha$，则称 $q_\\alpha$ 为循环坐标（或可遗坐标）。"))
    + thm("守恒定理", p("循环坐标对应的广义动量守恒：")+
    fml("p_\\alpha = \\frac{\\partial L}{\\partial\\dot q_\\alpha} = \\text{常数}",
        "由拉格朗日方程 $\\dot p_\\alpha=\\frac{\\partial L}{\\partial q_\\alpha}=0$。"))
    + app(p("中心力场中 $\\varphi$ 为循环坐标 $\\Rightarrow$ 角动量守恒；空间平移不变性 $\\Rightarrow$ 动量守恒；时间平移不变性 $\\Rightarrow$ 能量守恒。"))
)},
],
},

# ---- 1.3 变分法与最小作用量原理 ----
{
"name": "1.3 变分法与最小作用量原理",
"color": "#7c3aed",
"desc": "泛函、变分、欧拉-拉格朗日方程、最小作用量原理",
"items": [
{"id":"tm-c1s3-1","name":"泛函的定义","tags":["def","exa"],"brief":"以函数为自变量的映射。",
 "body": wrap(
    defn("泛函", p("设 $\\mathcal F$ 为某函数空间，泛函是从 $\\mathcal F$ 到 $\\mathbb R$ 的映射 $J: \\mathcal F\\to\\mathbb R$，即 $J[x(t)]\\in\\mathbb R$。可视为多元函数在无穷维的推广。"))
    + exa(p("<strong>最速落径问题：</strong>求连接两点的曲线使质点沿其下滑时间最短，$T[y(x)]=\\int_{x_1}^{x_2}\\sqrt{\\frac{1+y'^2}{2gy}}\\,dx$。<br><strong>作用量泛函：</strong>$S[q(t)]=\\int_{t_1}^{t_2}L(q,\\dot q,t)\\,dt$。"))
)},
{"id":"tm-c1s3-2","name":"泛函的变分","tags":["def","thm"],"brief":"泛函增量的线性主部。",
 "body": wrap(
    defn("变分", p("自变函数的增量 $\\delta x(t)=\\tilde x(t)-x(t)$。泛函的增量 $\\Delta J=J[x+\\delta x]-J[x]$ 可分解为线性主部与高阶小量 $\\Delta J=\\delta J+o(\\|\\delta x\\|)$，其中线性主部 $\\delta J$ 称为泛函的变分。"))
    + thm("变分的计算", p("若 $J[x]=\\int_{t_1}^{t_2}F(x,\\dot x,t)\\,dt$，则变分为")+
    fml("\\delta J = \\int_{t_1}^{t_2}\\left(\\frac{\\partial F}{\\partial x}\\delta x + \\frac{\\partial F}{\\partial\\dot x}\\delta\\dot x\\right)dt",
        "变分与微分运算可交换：$\\delta\\dot x=\\frac{d}{dt}\\delta x$。"))
)},
{"id":"tm-c1s3-3","name":"欧拉-拉格朗日方程（变分法）","tags":["thm","der"],"brief":"泛函取极值的必要条件。",
 "body": wrap(
    thm("欧拉-拉格朗日方程", p("泛函 $J[x]=\\int_{t_1}^{t_2}F(x,\\dot x,t)\\,dt$ 取极值的必要条件（$\\delta J=0$）为")+
    fml("\\frac{\\partial F}{\\partial x} - \\frac{d}{dt}\\frac{\\partial F}{\\partial\\dot x} = 0"))
    + der(p("$\\delta J=\\int_{t_1}^{t_2}\\left(\\frac{\\partial F}{\\partial x}\\delta x+\\frac{\\partial F}{\\partial\\dot x}\\delta\\dot x\\right)dt$。对第二项分部积分，端点固定 $\\delta x(t_1)=\\delta x(t_2)=0$，故边界项为零。由 $\\delta x$ 任意性得欧拉-拉格朗日方程。"))
)},
{"id":"tm-c1s3-4","name":"最小作用量原理","tags":["def","thm","app"],"brief":"真实运动使作用量取极值。",
 "body": wrap(
    defn("哈密顿作用量", p("对于拉格朗日函数 $L(q,\\dot q,t)$，定义作用量泛函")+
    fml("S[q(t)] = \\int_{t_1}^{t_2} L(q,\\dot q,t)\\,dt"))
    + thm("哈密顿最小作用量原理", p("体系在 $t_1$ 到 $t_2$ 时刻从 $q^{(1)}$ 到 $q^{(2)}$ 的真实运动，使作用量 $S$ 取极值（变分为零）：")+
    fml("\\delta S = 0",
        "由变分法的欧拉-拉格朗日方程，$\\delta S=0$ 即等价于 $\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha}-\\frac{\\partial L}{\\partial q_\\alpha}=0$。"))
    + app(p("最小作用量原理是力学的第一性原理之一，可作为力学的出发点，由此导出拉格朗日方程。"))
)},
{"id":"tm-c1s3-5","name":"最速落径问题","tags":["exa","der"],"brief":"变分法的经典应用。",
 "body": wrap(
    exa(p("求从 $(0,0)$ 到 $(x_2,y_2)$ 的曲线，使质点从静止出发在重力作用下沿曲线下滑时间最短。"))
    + der(p("时间泛函 $T=\\int\\sqrt{\\frac{1+y'^2}{2gy}}\\,dx$。由于被积函数不显含 $x$，利用首次积分 $F-y'\\frac{\\partial F}{\\partial y'}=$ 常数，化简得 $y(1+y'^2)=2R$。令 $y'=\\cot\\frac{\\theta}{2}$，解得参数方程 $x=R(\\theta-\\sin\\theta)$，$y=R(1-\\cos\\theta)$，即<strong>旋轮线（摆线）</strong>。"))
)},
],
},

# ---- 1.4 电磁场中的拉格朗日函数与诺特定理 ----
{
"name": "1.4 电磁场与诺特定理",
"color": "#c2410c",
"desc": "广义势能、规范变换、诺特定理",
"items": [
{"id":"tm-c1s4-1","name":"广义势能","tags":["def","thm"],"brief":"含速度的势能推广。",
 "body": wrap(
    defn("广义势能", p("若存在函数 $U(q,\\dot q,t)$ 使得广义力可写为")+
    fml("Q_\\alpha = -\\frac{\\partial U}{\\partial q_\\alpha} + \\frac{d}{dt}\\frac{\\partial U}{\\partial\\dot q_\\alpha}",
        "则 $U$ 称为广义势能。此时拉格朗日函数仍为 $L=T-U$，拉格朗日方程形式不变。"))
)},
{"id":"tm-c1s4-2","name":"带电粒子在电磁场中的拉格朗日函数","tags":["def","thm","der","app"],"brief":"洛伦兹力的拉格朗日表述。",
 "body": wrap(
    thm("电磁场广义势能", p("带电粒子在电磁场中受洛伦兹力 $\\vec F=q(\\vec E+\\vec v\\times\\vec B)$。引入标势 $\\phi$ 和矢势 $\\vec A$（$\\vec E=-\\nabla\\phi-\\partial_t\\vec A$，$\\vec B=\\nabla\\times\\vec A$），则广义势能为")+
    fml("U = q\\phi - q\\vec A\\cdot\\vec v"))
    + der(p("拉格朗日函数为 $L=\\frac{1}{2}m\\vec v^2-q\\phi+q\\vec A\\cdot\\vec v$。代入拉格朗日方程可验证得到洛伦兹力方程 $m\\ddot{\\vec r}=q(\\vec E+\\vec v\\times\\vec B)$。"))
    + app(p("该形式在量子力学和场论中有重要应用，$q\\vec A\\cdot\\vec v$ 项是规范势的体现。"))
)},
{"id":"tm-c1s4-3","name":"规范变换","tags":["def","thm"],"brief":"势的变换不改变物理。",
 "body": wrap(
    defn("规范变换", p("电磁场的势可做如下变换而不改变 $\\vec E$ 和 $\\vec B$：")+
    fml("\\vec A \\to \\vec A' = \\vec A + \\nabla\\chi,\\qquad \\phi \\to \\phi' = \\phi - \\frac{\\partial\\chi}{\\partial t}"))
    + thm("拉格朗日函数的规范变换", p("变换后拉格朗日函数变为 $L'=L+q\\frac{d\\chi}{dt}$。由于 $\\frac{d\\chi}{dt}$ 是全导数，运动方程不变，这与拉格朗日函数的不唯一性一致。"))
)},
{"id":"tm-c1s4-4","name":"对称性与守恒量","tags":["def","thm"],"brief":"诺特定理的前置概念。",
 "body": wrap(
    defn("对称性变换", p("若变换 $q\\to q'$ 使拉格朗日函数不变（或差一全导数），则称该变换为系统的对称性变换。"))
    + thm("动量、角动量、能量定理", p("<strong>动量定理：</strong>$\\frac{d}{dt}\\sum_i m_i\\dot{\\vec r}_i=\\sum_i\\vec F_i$，外力和为零时总动量守恒。<br><strong>角动量定理：</strong>$\\frac{d}{dt}\\sum_i\\vec r_i\\times m_i\\dot{\\vec r}_i=\\sum_i\\vec r_i\\times\\vec F_i$，外力矩和为零时总角动量守恒。<br><strong>能量定理：</strong>$\\frac{dE}{dt}=-\\frac{\\partial L}{\\partial t}$，$L$ 不显含时间时能量守恒。"))
)},
{"id":"tm-c1s4-5","name":"诺特定理","tags":["def","thm","der","app"],"brief":"连续对称性对应守恒量。",
 "body": wrap(
    defn("无穷小变换", p("考虑无穷小变换 $q_\\alpha\\to q_\\alpha+\\varepsilon\\eta_\\alpha(q,t)$，$t\\to t+\\varepsilon\\xi(q,t)$，其中 $\\varepsilon$ 为无穷小参数。"))
    + thm("诺特定理", p("若上述无穷小变换是系统的对称变换，则存在守恒量")+
    fml("I = \\sum_\\alpha \\frac{\\partial L}{\\partial\\dot q_\\alpha}\\eta_\\alpha + \\left(L - \\sum_\\alpha\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\dot q_\\alpha\\right)\\xi = \\text{常数}"))
    + der(p("由变换下 $\\delta S=0$，将变分展开并利用欧拉-拉格朗日方程，边界项给出守恒流。简化版（仅坐标变换 $\\xi=0$）：$I=\\sum_\\alpha\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\eta_\\alpha$。"))
    + app(p("<strong>空间平移 $\\eta=1$：</strong>$I=\\sum p_\\alpha=$ 总动量守恒。<br><strong>空间转动 $\\eta=1$：</strong>$I=$ 角动量守恒。<br><strong>时间平移 $\\xi=1$：</strong>$I=L-\\sum p_\\alpha\\dot q_\\alpha=-H$，能量守恒。"))
)},
],
},

# ---- 1.5 非惯性系与傅科摆 ----
{
"name": "1.5 非惯性系与傅科摆",
"color": "#be185d",
"desc": "非惯性系、科里奥利力、离心力、傅科摆",
"items": [
{"id":"tm-c1s5-1","name":"非惯性系","tags":["def","thm","app"],"brief":"加速参考系中的惯性力。",
 "body": wrap(
    defn("非惯性系", p("相对惯性系做加速运动的参考系称为非惯性系。在非惯性系中，牛顿第一定律不成立，需引入惯性力。"))
    + thm("加速平动参考系", p("设非惯性系以加速度 $\\vec a$ 相对惯性系平动，则在非惯性系中质点受力为 $\\vec F'=\\vec F-m\\vec a$，其中 $-m\\vec a$ 为平移惯性力。"))
    + app(p("电梯加速上升时人感觉变重；刹车时人前倾。"))
)},
{"id":"tm-c1s5-2","name":"转动参考系","tags":["thm","der","app"],"brief":"角速度为ω的转动参考系。",
 "body": wrap(
    thm("转动参考系的加速度关系", p("设转动参考系以角速度 $\\vec\\omega$ 绕定点转动，则惯性系中加速度 $\\vec a$ 与转动系中加速度 $\\vec a'$ 的关系为")+
    fml("\\vec a = \\vec a' + 2\\vec\\omega\\times\\vec v' + \\vec\\omega\\times(\\vec\\omega\\times\\vec r') + \\dot{\\vec\\omega}\\times\\vec r'"))
    + der(p("对位置矢量求导：$(\\frac{d}{dt})_{in}=(\\frac{d}{dt})_{rot}+\\vec\\omega\\times$。对速度求导两次即得上式。"))
    + app(p("由此得两种惯性力：<strong>科里奥利力</strong> $\\vec F_C=-2m\\vec\\omega\\times\\vec v'$，<strong>离心力</strong> $\\vec F_{cf}=-m\\vec\\omega\\times(\\vec\\omega\\times\\vec r')$。"))
)},
{"id":"tm-c1s5-3","name":"科里奥利力与离心力","tags":["def","thm","app"],"brief":"转动参考系中的两个惯性力。",
 "body": wrap(
    defn("科里奥利力", p("$\\vec F_C=-2m\\vec\\omega\\times\\vec v'$，与质点相对速度成正比，只改变速度方向不改变大小。"))
    + defn("离心力", p("$\\vec F_{cf}=-m\\vec\\omega\\times(\\vec\\omega\\times\\vec r')$，沿径向外指，大小 $m\\omega^2 r\\sin\\theta$。"))
    + app(p("地球自转导致：北半球河流右岸冲刷严重、气旋逆时针旋转；傅科摆的进动；赤道处重力略小于两极。"))
)},
{"id":"tm-c1s5-4","name":"傅科摆","tags":["exa","der","app"],"brief":"验证地球自转的经典实验。",
 "body": wrap(
    exa(p("傅科摆是验证地球自转的著名实验。长摆悬挂于北半球纬度 $\\lambda$ 处，由于科里奥利力，摆的振动面会缓慢旋转。"))
    + der(p("在小角度近似下，摆锤在水平面内受科里奥利力。科里奥利力的水平分量为 $-2m\\omega\\sin\\lambda\\,\\hat z\\times\\vec v$。解得摆动面以角速度")+
    fml("\\Omega = \\omega\\sin\\lambda",
        "绕竖直轴旋转（北半球顺时针，从上往下看）。"))
    + app(p("在巴黎（$\\lambda\\approx49^\\circ$），傅科摆约 32 小时转一圈；在北极（$\\lambda=90^\\circ$），周期为 24 小时。"))
)},
],
},
]

print(f"Ch1 Lagrangian: {sum(len(s['items']) for s in ch1_sections)} items")

# =====================================================
#  CHAPTER 2: 哈密顿力学
# =====================================================
ch2_sections = [

# ---- 2.1 勒让德变换与哈密顿量 ----
{
"name": "2.1 勒让德变换与哈密顿量",
"color": "#2563eb",
"desc": "勒让德变换、哈密顿量、正则变量",
"items": [
{"id":"tm-c2s1-1","name":"勒让德变换","tags":["def","thm","der"],"brief":"自变量与函数形式同时变换。",
 "body": wrap(
    defn("勒让德变换", p("设 $y=f(x)$ 为下凸函数，令 $p=\\frac{df}{dx}$。由凸性可反解 $x=x(p)$，定义")+
    fml("g(p) = x\\,p - f(x)\\big|_{x=x(p)}",
        "函数 $f(x)$ 到 $g(p)$ 的变换称为勒让德变换，自变量 $x$ 变为 $p$，函数形式 $f$ 变为 $g$。"))
    + thm("全微分", p("$g(p)$ 的全微分为 $dg = x\\,dp$。做两次勒让德变换回到原函数。"))
    + der(p("$dg=x\\,dp+p\\,dx-df=x\\,dp+p\\,dx-p\\,dx=x\\,dp$。对 $g(p)$ 再做勒让德变换：令 $z=\\frac{dg}{dp}=x$，则 $h(z)=zp-g(p)=xp-(xp-f(x))=f(x)=f(z)$。"))
)},
{"id":"tm-c2s1-2","name":"勒让德变换的几何意义","tags":["thm","exa"],"brief":"切线在纵轴上的截距。",
 "body": wrap(
    thm("几何意义", p("$g(p)$ 等于斜率为 $p$ 且与 $y=f(x)$ 相切的直线在纵轴上的截距。切点横坐标 $x=x(p)$ 由 $p=\\frac{df}{dx}$ 决定，截距为 $px(p)-f(x(p))$。"))
)},
{"id":"tm-c2s1-3","name":"正则变量与哈密顿量","tags":["def","thm","der"],"brief":"从拉格朗日函数到哈密顿量。",
 "body": wrap(
    defn("广义动量", p("对每个广义速度 $\\dot q_\\alpha$，定义相应的广义动量（正则动量）")+
    fml("p_\\alpha = \\frac{\\partial L}{\\partial\\dot q_\\alpha},\\qquad 1\\le\\alpha\\le s"))
    + defn("哈密顿量", p("对每个广义速度做勒让德变换，引入哈密顿量")+
    fml("H(p_\\alpha,q_\\alpha,t) = \\sum_\\alpha p_\\alpha\\dot q_\\alpha - L(q_\\alpha,\\dot q_\\alpha,t)",
        "其中 $\\dot q_\\alpha$ 通过反解 $p_\\alpha=\\partial L/\\partial\\dot q_\\alpha$ 表示为 $q,p,t$ 的函数。"))
    + thm("哈密顿量的偏导数", p("由全微分比较得")+
    fml("\\dot q_\\alpha = \\frac{\\partial H}{\\partial p_\\alpha},\\qquad \\frac{\\partial H}{\\partial q_\\alpha} = -\\frac{\\partial L}{\\partial q_\\alpha},\\qquad \\frac{\\partial H}{\\partial t} = -\\frac{\\partial L}{\\partial t}"))
)},
{"id":"tm-c2s1-4","name":"哈密顿量的例子","tags":["exa","der","app"],"brief":"电磁场粒子、谐振子、单摆。",
 "body": wrap(
    exa(p("<strong>带电粒子在电磁场中：</strong>$L=\\frac{1}{2}m\\vec v^2-q\\phi+q\\vec A\\cdot\\vec v$，正则动量 $\\vec p=m\\vec v+q\\vec A$，故")+
    fml("H = \\frac{(\\vec p-q\\vec A)^2}{2m} + q\\phi"))
    + exa(p("<strong>一维谐振子：</strong>$L=\\frac{1}{2}m\\dot x^2-\\frac{1}{2}m\\omega^2 x^2$，$p=m\\dot x$，故")+
    fml("H = \\frac{p^2}{2m} + \\frac{1}{2}m\\omega^2 x^2 = T+V = E"))
    + exa(p("<strong>单摆：</strong>$L=\\frac{1}{2}mR^2\\dot\\theta^2+mgR\\cos\\theta$，$p_\\theta=mR^2\\dot\\theta$，故 $H=\\frac{p_\\theta^2}{2mR^2}-mgR\\cos\\theta$，正则动量 $p_\\theta$ 为角动量。"))
    + app(p("当 $L$ 不显含时间且势能不含速度时，$H=T+V=E$ 即为总能量。"))
)},
],
},

# ---- 2.2 哈密顿正则方程 ----
{
"name": "2.2 哈密顿正则方程",
"color": "#0d9488",
"desc": "正则方程、相空间、哈密顿流",
"items": [
{"id":"tm-c2s2-1","name":"哈密顿正则方程","tags":["def","thm","der"],"brief":"哈密顿形式的运动方程。",
 "body": wrap(
    thm("正则方程", p("利用欧拉-拉格朗日方程 $\\dot p_\\alpha=\\frac{\\partial L}{\\partial q_\\alpha}$ 及勒让德变换关系 $\\frac{\\partial H}{\\partial q_\\alpha}=-\\frac{\\partial L}{\\partial q_\\alpha}$，得哈密顿正则方程")+
    fml("\\dot q_\\alpha = \\frac{\\partial H}{\\partial p_\\alpha},\\qquad \\dot p_\\alpha = -\\frac{\\partial H}{\\partial q_\\alpha},\\qquad 1\\le\\alpha\\le s",
        "共 $2s$ 个一阶微分方程，替代拉格朗日力学中的 $s$ 个二阶方程。"))
    + der(p("由 $p_\\alpha=\\frac{\\partial L}{\\partial\\dot q_\\alpha}$ 及欧拉-拉格朗日方程 $\\frac{d}{dt}p_\\alpha=\\frac{\\partial L}{\\partial q_\\alpha}$，再利用 $\\frac{\\partial H}{\\partial q_\\alpha}=-\\frac{\\partial L}{\\partial q_\\alpha}$ 即得 $\\dot p_\\alpha=-\\frac{\\partial H}{\\partial q_\\alpha}$。"))
)},
{"id":"tm-c2s2-2","name":"相空间","tags":["def","thm","app"],"brief":"正则变量张成的空间。",
 "body": wrap(
    defn("相空间", p("以 $s$ 个广义坐标 $q_\\alpha$ 和 $s$ 个广义动量 $p_\\alpha$ 为坐标的 $2s$ 维空间称为相空间（$\\Gamma$ 空间）。系统的运动状态对应相空间中的一点，运动轨迹为相轨道。"))
    + defn("哈密顿流", p("正则方程在相空间中定义了一个矢量场 $X_H=(\\frac{\\partial H}{\\partial p},-\\frac{\\partial H}{\\partial q})$，称为哈密顿矢量场。其积分曲线即系统的运动轨迹，构成哈密顿流。"))
    + thm("刘维尔定理", p("哈密顿流保持相空间体积元不变：相空间中区域的体积在运动中守恒。"))
    + app(p("相空间方法是统计力学的基础，哈密顿流的保体积性是刘维尔定理的核心。"))
)},
{"id":"tm-c2s2-3","name":"正则方程的例子","tags":["exa","der"],"brief":"从正则方程求解运动。",
 "body": wrap(
    exa(p("<strong>一维谐振子：</strong>$H=\\frac{p^2}{2m}+\\frac{1}{2}m\\omega^2 x^2$。正则方程为")+
    fml("\\dot x = \\frac{\\partial H}{\\partial p} = \\frac{p}{m},\\qquad \\dot p = -\\frac{\\partial H}{\\partial x} = -m\\omega^2 x",
        "消去 $p$ 得 $\\ddot x+\\omega^2 x=0$，解为简谐振动。"))
    + der(p("<strong>中心力场：</strong>$H=\\frac{1}{2m}(p_r^2+\\frac{p_\\varphi^2}{r^2})+V(r)$。$\\varphi$ 为循环坐标 $\\Rightarrow p_\\varphi=l$ 守恒，即角动量守恒。"))
)},
],
},

# ---- 2.3 泊松括号 ----
{
"name": "2.3 泊松括号",
"color": "#7c3aed",
"desc": "泊松括号的定义、性质、辛形式、正则量子化",
"items": [
{"id":"tm-c2s3-1","name":"泊松括号的定义","tags":["def","thm"],"brief":"相空间标量场的时间演化。",
 "body": wrap(
    defn("泊松括号", p("设 $f(q,p,t)$ 和 $g(q,p,t)$ 为相空间上的标量场，它们的泊松括号定义为")+
    fml("\\{f,g\\} = \\sum_{\\alpha=1}^{s}\\left(\\frac{\\partial f}{\\partial q_\\alpha}\\frac{\\partial g}{\\partial p_\\alpha} - \\frac{\\partial f}{\\partial p_\\alpha}\\frac{\\partial g}{\\partial q_\\alpha}\\right)"))
    + thm("时间演化", p("任意力学量 $f(q,p,t)$ 沿运动轨迹的时间导数为")+
    fml("\\frac{df}{dt} = \\frac{\\partial f}{\\partial t} + \\{f,H\\}",
        "特别地，$\\dot q_\\alpha=\\{q_\\alpha,H\\}$，$\\dot p_\\alpha=\\{p_\\alpha,H\\}$。"))
)},
{"id":"tm-c2s3-2","name":"泊松括号的性质","tags":["thm","der"],"brief":"双线性、反对称、雅可比恒等式。",
 "body": wrap(
    thm("基本性质", p("<strong>双线性：</strong>$\\{af+bg,h\\}=a\\{f,h\\}+b\\{g,h\\}$<br><strong>反对称性：</strong>$\\{f,g\\}=-\\{g,f\\}$<br><strong>莱布尼茨法则：</strong>$\\{fg,h\\}=f\\{g,h\\}+\\{f,h\\}g$<br><strong>雅可比恒等式：</strong>$\\{f,\\{g,h\\}\\}+\\{g,\\{h,f\\}\\}+\\{h,\\{f,g\\}\\}=0$"))
    + thm("基本泊松括号", p("$\\{q_\\alpha,q_\\beta\\}=0$，$\\{p_\\alpha,p_\\beta\\}=0$，$\\{q_\\alpha,p_\\beta\\}=\\delta_{\\alpha\\beta}$。"))
    + der(p("由定义直接计算可验证各性质。雅可比恒等式是泊松括号最重要的代数性质，它保证了相空间上的函数构成李代数。"))
)},
{"id":"tm-c2s3-3","name":"辛形式","tags":["def","thm"],"brief":"泊松括号的几何表述。",
 "body": wrap(
    defn("辛形式", p("引入辛矩阵 $J=\\begin{pmatrix}0&I\\\\-I&0\\end{pmatrix}$，泊松括号可写为")+
    fml("\\{f,g\\} = (\\nabla f)^T J (\\nabla g)"))
    + thm("正则方程的辛形式", p("令 $\\xi=(q_1,\\dots,q_s,p_1,\\dots,p_s)^T$，正则方程可写为")+
    fml("\\dot\\xi = J\\nabla H"))
)},
{"id":"tm-c2s3-4","name":"守恒量的判定","tags":["thm","app"],"brief":"用泊松括号判断守恒。",
 "body": wrap(
    thm("守恒判据", p("若力学量 $f$ 不显含时间（$\\frac{\\partial f}{\\partial t}=0$），则 $f$ 为守恒量当且仅当")+
    fml("\\{f,H\\} = 0",
        "即 $f$ 与哈密顿量的泊松括号为零。"))
    + app(p("若 $H$ 不含时，则 $\\{H,H\\}=0$，故能量 $H$ 守恒。角动量各分量满足 $\\{L_x,L_y\\}=L_z$ 等对易关系。"))
)},
{"id":"tm-c2s3-5","name":"正则量子化","tags":["app","note"],"brief":"从泊松括号到量子对易子。",
 "body": wrap(
    thm("正则量子化规则", p("量子力学中，经典泊松括号对应量子对易子：")+
    fml("\\{f,g\\}_{cl} \\longrightarrow \\frac{1}{i\\hbar}[\\hat f,\\hat g]"))
    + app(p("基本泊松括号 $\\{q,p\\}=1$ 对应量子对易关系 $[\\hat q,\\hat p]=i\\hbar$，这是海森堡正则对易关系的来源。"))
    + note(p("正则量子化是从经典力学到量子力学的桥梁，泊松括号的代数结构在量子层面被保持。"))
)},
],
},

# ---- 2.4 正则变换 ----
{
"name": "2.4 正则变换",
"color": "#c2410c",
"desc": "正则变换的定义、充分条件、辛变换",
"items": [
{"id":"tm-c2s4-1","name":"正则变换的概念","tags":["def","thm"],"brief":"保持正则方程形式的变换。",
 "body": wrap(
    defn("正则变换", p("若变换 $(q,p)\\to(Q,P)$ 使正则方程形式不变，即存在新哈密顿量 $K(Q,P,t)$ 使")+
    fml("\\dot Q_\\alpha = \\frac{\\partial K}{\\partial P_\\alpha},\\qquad \\dot P_\\alpha = -\\frac{\\partial K}{\\partial Q_\\alpha}",
        "则称该变换为正则变换。"))
)},
{"id":"tm-c2s4-2","name":"正则变换的充分条件","tags":["thm","der"],"brief":"母函数与全微分条件。",
 "body": wrap(
    thm("正则变换条件", p("变换 $(q,p)\\to(Q,P)$ 为正则变换的充要条件是存在函数 $F$，使得")+
    fml("\\sum_\\alpha p_\\alpha dq_\\alpha - \\sum_\\alpha P_\\alpha dQ_\\alpha + (K-H)dt = dF",
        "即左边为某个函数 $F$ 的全微分。$F$ 称为正则变换的母函数。"))
    + der(p("由哈密顿最小作用量原理，变换前后作用量变分条件应等价，即被积函数之差应为全微分。"))
)},
{"id":"tm-c2s4-3","name":"辛变换","tags":["def","thm"],"brief":"正则变换的矩阵表述。",
 "body": wrap(
    defn("辛变换", p("设变换 $\\xi\\to\\eta$ 的雅可比矩阵为 $M=\\frac{\\partial\\eta}{\\partial\\xi}$，若满足")+
    fml("M^T J M = J",
        "则称该变换为辛变换。$J=\\begin{pmatrix}0&I\\\\-I&0\\end{pmatrix}$ 为辛矩阵。"))
    + thm("等价性", p("变换为正则变换当且仅当它是辛变换。辛变换保持泊松括号不变：$\\{f,g\\}_{q,p}=\\{f,g\\}_{Q,P}$。"))
)},
{"id":"tm-c2s4-4","name":"正则变换的例子","tags":["exa","der"],"brief":"一维谐振子的作用量-角变量。",
 "body": wrap(
    exa(p("<strong>一维谐振子：</strong>$H=\\frac{p^2}{2m}+\\frac{1}{2}m\\omega^2 q^2$。引入作用量变量 $J$ 和角变量 $w$，做正则变换"))
    + der(p("令 $q=\\sqrt{\\frac{2J}{m\\omega}}\\sin(2\\pi w)$，$p=\\sqrt{2m\\omega J}\\cos(2\\pi w)$。新哈密顿量 $K=H=\\omega J$（不显含 $w$）。正则方程给出 $\\dot w=\\frac{\\partial K}{\\partial J}=\\omega$，$\\dot J=-\\frac{\\partial K}{\\partial w}=0$，故 $J$ 守恒，$w=\\omega t+w_0$。"))
)},
],
},

# ---- 2.5 母函数与哈密顿-雅科比方程 ----
{
"name": "2.5 母函数与哈密顿-雅科比方程",
"color": "#be185d",
"desc": "四类母函数、哈密顿-雅科比方程、分离变量法",
"items": [
{"id":"tm-c2s5-1","name":"四类母函数","tags":["def","thm","exa"],"brief":"四种形式的正则变换母函数。",
 "body": wrap(
    thm("四类母函数", p("正则变换的母函数可取四种独立变量组合：")+
    fml("F_1(q,Q,t):\\; p=\\frac{\\partial F_1}{\\partial q},\\; P=-\\frac{\\partial F_1}{\\partial Q}",
        "$F_2(q,P,t):\\; p=\\frac{\\partial F_2}{\\partial q},\\; Q=\\frac{\\partial F_2}{\\partial P}$<br>$F_3(p,Q,t):\\; q=-\\frac{\\partial F_3}{\\partial p},\\; P=-\\frac{\\partial F_3}{\\partial Q}$<br>$F_4(p,P,t):\\; q=-\\frac{\\partial F_4}{\\partial p},\\; Q=\\frac{\\partial F_4}{\\partial P}$"))
    + exa(p("四类母函数之间通过勒让德变换相互联系。例如 $F_2(q,P,t)=F_1(q,Q,t)+PQ$。"))
)},
{"id":"tm-c2s5-2","name":"哈密顿-雅科比方程","tags":["def","thm","der","app"],"brief":"使新哈密顿量为零的正则变换。",
 "body": wrap(
    defn("哈密顿主函数", p("取母函数 $F_2=S(q,P,t)$，要求新哈密顿量 $K=0$，则由 $K=H+\\frac{\\partial S}{\\partial t}=0$ 得")+
    fml("H\\left(q,\\frac{\\partial S}{\\partial q},t\\right) + \\frac{\\partial S}{\\partial t} = 0",
        "此即<strong>哈密顿-雅科比方程</strong>，$S(q,P,t)$ 称为哈密顿主函数。"))
    + thm("完全解", p("若能求得含 $s$ 个独立常数 $\\alpha_1,\\dots,\\alpha_s$ 的完全解 $S(q,\\alpha,t)$，则系统的运动可由")+
    fml("\\beta_i = \\frac{\\partial S}{\\partial\\alpha_i},\\qquad p_i = \\frac{\\partial S}{\\partial q_i}"))
    + der(p("由于 $K=0$，新正则变量 $Q_i=\\beta_i$ 和 $P_i=\\alpha_i$ 均为常数。通过 $\\beta_i=\\partial S/\\partial\\alpha_i$ 反解出 $q_i(t)$，即得运动方程的解。"))
    + app(p("哈密顿-雅科比方程是求解力学系统最有力的方法之一，尤其适用于可分离变量的系统。"))
)},
{"id":"tm-c2s5-3","name":"分离变量法","tags":["thm","der","app"],"brief":"将HJ方程分解为常微分方程。",
 "body": wrap(
    thm("不含时哈密顿量的分离", p("若 $H$ 不显含时间，则 $S=-Et+W(q)$，其中 $W$ 满足")+
    fml("H\\left(q,\\frac{\\partial W}{\\partial q}\\right) = E",
        "$W(q)$ 称为哈密顿特征函数。若 $W$ 可分离为各坐标函数之和 $W=\\sum W_i(q_i)$，则方程分解为 $s$ 个常微分方程。"))
    + app(p("中心力场中，$W(r,\\theta,\\varphi)=W_r(r)+W_\\theta(\\theta)+W_\\varphi(\\varphi)$，可分别求解各坐标的运动。"))
)},
],
},

# ---- 2.6 无穷小正则变换与诺特定理 ----
{
"name": "2.6 无穷小正则变换与守恒量",
"color": "#059669",
"desc": "无穷小正则变换、生成元、哈密顿力学诺特定理",
"items": [
{"id":"tm-c2s6-1","name":"无穷小正则变换","tags":["def","thm","der"],"brief":"无限接近恒等的正则变换。",
 "body": wrap(
    defn("无穷小正则变换", p("考虑无穷小参数 $\\varepsilon$，变换 $q\\to q+\\delta q$，$p\\to p+\\delta p$，其中 $\\delta q,\\delta p$ 为一阶小量。若该变换为正则变换，则称为无穷小正则变换。"))
    + thm("生成元", p("任何无穷小正则变换都由一个生成元函数 $G(q,p,t)$ 生成：")+
    fml("\\delta q_\\alpha = \\varepsilon\\frac{\\partial G}{\\partial p_\\alpha},\\qquad \\delta p_\\alpha = -\\varepsilon\\frac{\\partial G}{\\partial q_\\alpha}",
        "即 $\\delta q=\\varepsilon\\{q,G\\}$，$\\delta p=\\varepsilon\\{p,G\\}$。"))
    + der(p("取母函数 $F_2=\\sum q_\\alpha P_\\alpha+\\varepsilon G(q,P,t)$，展开到 $\\varepsilon$ 一阶即得上述结果。"))
)},
{"id":"tm-c2s6-2","name":"连续正则变换的生成元","tags":["thm","der"],"brief":"有限变换由生成元指数化得到。",
 "body": wrap(
    thm("连续变换", p("有限参数的连续正则变换可由无穷小变换复合得到。设生成元为 $G$，参数为 $u$，则变换可表示为")+
    fml("\\xi(u) = e^{u\\{\\cdot,G\\}}\\xi(0)"))
    + der(p("由 $\\frac{d\\xi}{du}=\\{\\xi,G\\}$ 迭代展开为幂级数即得指数形式。"))
)},
{"id":"tm-c2s6-3","name":"哈密顿力学中的诺特定理","tags":["def","thm","der","app"],"brief":"对称性与守恒量在哈密顿框架中的表述。",
 "body": wrap(
    defn("对称性变换", p("若连续变换使哈密顿量不变（$\\delta H=0$），则称该变换为对称性变换。"))
    + thm("诺特定理（哈密顿形式）", p("若 $G$ 生成的连续变换是对称性变换（即 $\\{H,G\\}=0$），则 $G$ 为守恒量：")+
    fml("\\{H,G\\} = 0 \\Rightarrow \\frac{dG}{dt} = 0",
        "反之，若 $G$ 为守恒量（$\\{H,G\\}=0$），则 $G$ 生成的变换是对称性变换。对称性与守恒量一一对应。"))
    + der(p("由 $\\frac{dG}{dt}=\\frac{\\partial G}{\\partial t}+\\{G,H\\}$。若 $G$ 不显含时间，则 $\\frac{dG}{dt}=\\{G,H\\}=-\\{H,G\\}$。对称性要求 $\\delta H=\\varepsilon\\{H,G\\}=0$，故 $\\frac{dG}{dt}=0$。"))
    + app(p("<strong>动量守恒：</strong>$G=p$ 生成平移 $\\delta q=\\varepsilon$，$\\{H,p\\}=0$ $\\Rightarrow$ 动量守恒。<br><strong>角动量守恒：</strong>$G=L_z$ 生成转动，$\\{H,L_z\\}=0$ $\\Rightarrow$ 角动量守恒。<br><strong>能量守恒：</strong>$G=H$ 生成时间平移，$\\{H,H\\}=0$ $\\Rightarrow$ 能量守恒。"))
)},
{"id":"tm-c2s6-4","name":"对称性代数","tags":["thm","note"],"brief":"守恒量构成李代数。",
 "body": wrap(
    thm("对称性代数", p("若 $G_1$ 和 $G_2$ 都是守恒量（生成对称性变换），则它们的泊松括号 $\\{G_1,G_2\\}$ 也是守恒量。所有守恒量在泊松括号下构成李代数。"))
    + note(p("例如角动量分量满足 $\\{L_x,L_y\\}=L_z$，构成 $so(3)$ 李代数，对应转动群 $SO(3)$ 的李代数。这是对称性与群论联系的基础。"))
)},
],
},
]

print(f"Ch2 Hamiltonian: {sum(len(s['items']) for s in ch2_sections)} items")

# =====================================================
#  CHAPTER 3: 力学经典问题
# =====================================================
ch3_sections = [

# ---- 3.1 微振动与简正坐标 ----
{
"name": "3.1 微振动与简正坐标",
"color": "#2563eb",
"desc": "平衡位置、稳定平衡、小振动方程、简正坐标",
"items": [
{"id":"tm-c3s1-1","name":"平衡位置","tags":["def","thm","der"],"brief":"广义力为零的位置。",
 "body": wrap(
    defn("平衡位置", p("若 $\\vec q(t)=\\vec q_0$ 是系统动力学方程的解，则 $\\vec q_0$ 称为系统的一个平衡位置。"))
    + thm("平衡位置的充要条件", p("对于约束和势能均不显含时间的系统，$\\vec q_0$ 为平衡位置的充要条件是广义力为零：")+
    fml("\\frac{\\partial U}{\\partial q_\\alpha}\\bigg|_{\\vec q=\\vec q_0} = 0",
        "即势能在平衡位置处取极值。"))
    + der(p("由欧拉-拉格朗日方程，平衡时 $\\dot q=\\ddot q=0$，故 $\\frac{\\partial L}{\\partial q_\\alpha}=-\\frac{\\partial U}{\\partial q_\\alpha}=0$。反之若广义力为零，$\\vec q(t)=\\vec q_0$ 满足方程。"))
)},
{"id":"tm-c3s1-2","name":"平衡的分类","tags":["def","thm"],"brief":"稳定、不稳定、随遇平衡。",
 "body": wrap(
    defn("稳定平衡", p("对处于平衡位置的系统，若经历小扰动后运动完全局限于平衡位置附近，则称稳定平衡。严格定义：$\\forall\\varepsilon>0,\\exists\\delta>0$，使初始 $|\\vec q(t_0)-\\vec q_0|<\\delta$ 且 $|\\vec p(t_0)|<\\delta$ 时，恒有 $|\\vec q(t)-\\vec q_0|<\\varepsilon$。"))
    + thm("稳定平衡的条件", p("保守系统在平衡位置 $\\vec q_0$ 处稳定的充分条件是势能取严格极小值：")+
    fml("U(\\vec q_0) \\text{ 为严格极小值 } \\Rightarrow \\text{ 稳定平衡}"))
    + defn("不稳定与随遇平衡", p("<strong>不稳定平衡：</strong>小扰动后系统远离平衡位置（势能极大值）。<br><strong>随遇平衡：</strong>扰动后系统处于新的平衡位置（势能平台）。"))
)},
{"id":"tm-c3s1-3","name":"小振动方程","tags":["def","thm","der"],"brief":"在稳定平衡附近的线性化运动。",
 "body": wrap(
    thm("小振动方程", p("在稳定平衡位置附近，将势能展开到二阶")+
    fml("U(\\vec q) \\approx U(\\vec q_0) + \\frac{1}{2}\\sum_{\\alpha\\beta} V_{\\alpha\\beta}\\eta_\\alpha\\eta_\\beta",
        "其中 $\\eta_\\alpha=q_\\alpha-q_{0\\alpha}$ 为偏离平衡的位移，$V_{\\alpha\\beta}=\\frac{\\partial^2 U}{\\partial q_\\alpha\\partial q_\\beta}\\big|_{\\vec q_0}$ 为势能矩阵。"))
    + thm("动能与运动方程", p("动能在平衡附近近似为 $T=\\frac{1}{2}\\sum_{\\alpha\\beta}A_{\\alpha\\beta}\\dot\\eta_\\alpha\\dot\\eta_\\beta$（$A_{\\alpha\\beta}$ 为常数质量矩阵）。由拉格朗日方程得线性运动方程")+
    fml("\\sum_\\beta A_{\\alpha\\beta}\\ddot\\eta_\\beta + \\sum_\\beta V_{\\alpha\\beta}\\eta_\\beta = 0",
        "这是一个二阶线性齐次常微分方程组。"))
    + der(p("由 $L=T-V$ 代入欧拉-拉格朗日方程，忽略高阶小量即得。"))
)},
{"id":"tm-c3s1-4","name":"简正频率与简正坐标","tags":["def","thm","der"],"brief":"广义本征值问题。",
 "body": wrap(
    defn("简正频率", p("设简谐解形式 $\\eta_\\alpha=a_\\alpha\\cos(\\omega t+\\phi)$，代入小振动方程得广义本征值问题")+
    fml("\\det(V - \\omega^2 A) = 0",
        "解得的 $\\omega_i$（$i=1,\\dots,s$）称为简正频率，对应的本征矢量 $\\vec a^{(i)}$ 为简正模式。"))
    + thm("简正坐标", p("通过线性变换 $\\eta_\\alpha=\\sum_i C_{\\alpha i}Q_i$（其中 $C$ 的列为本征矢量），可将运动方程解耦为")+
    fml("\\ddot Q_i + \\omega_i^2 Q_i = 0",
        "$Q_i$ 称为简正坐标，每个简正坐标以单一频率 $\\omega_i$ 做简谐振动。"))
    + der(p("由于 $A$ 和 $V$ 均为对称矩阵且 $A$ 正定，可通过广义本征值问题同时对角化 $A$ 和 $V$，从而使运动方程解耦。"))
)},
{"id":"tm-c3s1-5","name":"双单摆","tags":["exa","der"],"brief":"两个自由度耦合振动的经典例子。",
 "body": wrap(
    exa(p("双单摆由两根轻杆和两个质点组成，质量均为 $m$，杆长均为 $l$。取两杆与竖直方向夹角 $\\theta_1,\\theta_2$ 为广义坐标。"))
    + der(p("小角度近似下，拉格朗日函数为")+
    fml("L = \\frac{1}{2}ml^2(2\\dot\\theta_1^2+\\dot\\theta_2^2+2\\dot\\theta_1\\dot\\theta_2) - \\frac{1}{2}mgl(2\\theta_1^2+\\theta_2^2)")
    + p("代入本征值方程 $\\det(V-\\omega^2 A)=0$，解得两个简正频率")+
    fml("\\omega_1^2 = \\frac{g}{l}(2+\\sqrt{2}),\\qquad \\omega_2^2 = \\frac{g}{l}(2-\\sqrt{2})")
    + p("对应两个简正模式：同相振动（$\\theta_1=\\theta_2$）和反相振动（$\\theta_1=-\\theta_2$）。"))
)},
],
},

# ---- 3.2 中心势场与开普勒问题 ----
{
"name": "3.2 中心势场与开普勒问题",
"color": "#0d9488",
"desc": "两体问题约化、中心势场、开普勒定律",
"items": [
{"id":"tm-c3s2-1","name":"两体问题的单体约化","tags":["def","thm","der"],"brief":"将两体问题化为单体问题。",
 "body": wrap(
    thm("质心与相对运动", p("两体系统的运动可分解为质心的匀速运动和相对运动。设两质点质量为 $m_1,m_2$，位矢为 $\\vec r_1,\\vec r_2$，引入质心坐标 $\\vec R$ 和相对坐标 $\\vec r=\\vec r_2-\\vec r_1$。"))
    + fml("\\mu = \\frac{m_1 m_2}{m_1+m_2}",
        "$\\mu$ 称为约化质量。系统拉格朗日函数为 $L=\\frac{1}{2}(m_1+m_2)\\dot{\\vec R}^2 + \\frac{1}{2}\\mu\\dot{\\vec r}^2 - V(|\\vec r|)$。")
    + der(p("质心运动 $\\ddot{\\vec R}=0$（匀速），可分离。相对运动等价于一个质量为 $\\mu$ 的质点在中心势场 $V(r)$ 中的运动。"))
)},
{"id":"tm-c3s2-2","name":"中心势场的守恒量","tags":["thm","der","app"],"brief":"角动量守恒与有效势能。",
 "body": wrap(
    thm("角动量守恒", p("中心势场 $V(r)$ 中，$\\varphi$ 为循环坐标，故角动量守恒")+
    fml("L = \\mu r^2\\dot\\varphi = \\text{常数}"))
    + thm("有效势能", p("由能量守恒 $E=\\frac{1}{2}\\mu(\\dot r^2+r^2\\dot\\varphi^2)+V(r)$，利用角动量守恒消去 $\\dot\\varphi$，得径向运动方程")+
    fml("\\frac{1}{2}\\mu\\dot r^2 + V_{\\text{eff}}(r) = E,\\qquad V_{\\text{eff}}(r) = V(r) + \\frac{L^2}{2\\mu r^2}",
        "$\\frac{L^2}{2\\mu r^2}$ 称为离心势能。径向运动等效于在有效势 $V_{\\text{eff}}(r)$ 中的一维运动。"))
    + app(p("有效势方法将二维中心力场问题简化为一维径向运动问题。"))
)},
{"id":"tm-c3s2-3","name":"开普勒问题的轨道方程","tags":["thm","der","app"],"brief":"平方反比引力的圆锥曲线轨道。",
 "body": wrap(
    thm("轨道方程", p("对于万有引力势 $V(r)=-\\frac{k}{r}$（$k=Gm_1m_2$），引入 $u=1/r$，由比耐公式得轨道方程")+
    fml("\\frac{1}{r} = \\frac{\\mu k}{L^2}\\left(1+e\\cos(\\varphi-\\varphi_0)\\right)",
        "这是圆锥曲线方程，其中偏心率 $e=\\sqrt{1+\\frac{2EL^2}{\\mu k^2}}$。"))
    + der(p("由角动量守恒 $\\dot\\varphi=L/\\mu r^2$，径向方程化为 $\\frac{d^2u}{d\\varphi^2}+u=\\frac{\\mu k}{L^2}$，其解为圆锥曲线。"))
    + app(p("<strong>椭圆轨道：</strong>$e<1$（$E<0$），对应行星运动。<br><strong>抛物线：</strong>$e=1$（$E=0$）。<br><strong>双曲线：</strong>$e>1$（$E>0$），对应散射。"))
)},
{"id":"tm-c3s2-4","name":"开普勒定律","tags":["thm","der","app"],"brief":"行星运动三大定律的理论推导。",
 "body": wrap(
    thm("开普勒三大定律", p("<strong>第一定律（轨道定律）：</strong>行星沿椭圆轨道绕太阳运动，太阳位于椭圆的一个焦点上。<br><strong>第二定律（面积定律）：</strong>行星与太阳的连线在相等时间内扫过相等面积。<br><strong>第三定律（周期定律）：</strong>行星公转周期的平方与椭圆半长轴的立方成正比。"))
    + der(p("面积定律：$\\frac{dA}{dt}=\\frac{1}{2}r^2\\dot\\varphi=\\frac{L}{2\\mu}=$ 常数，由角动量守恒直接得出。<br>第三定律：由椭圆面积 $A=\\pi ab$ 和 $\\frac{dA}{dt}=L/2\\mu$，得周期 $T=2\\pi ab\\mu/L$。结合 $b=a\\sqrt{1-e^2}$ 和 $L^2=\\mu k a(1-e^2)$，化简得")+
    fml("T^2 = \\frac{4\\pi^2\\mu}{k}a^3"))
    + app(p("开普勒定律是牛顿万有引力定律的实验基础，也是经典力学的伟大胜利。"))
)},
{"id":"tm-c3s2-5","name":"用哈密顿-雅科比方程解开普勒问题","tags":["exa","der"],"brief":"HJ方法的经典应用。",
 "body": wrap(
    exa(p("对于中心势场 $V(r)=-k/r$，哈密顿量为 $H=\\frac{1}{2\\mu}(p_r^2+\\frac{p_\\theta^2}{r^2}+\\frac{p_\\varphi^2}{r^2\\sin^2\\theta})-\\frac{k}{r}$。"))
    + der(p("HJ 方程可分离变量：$S=-Et+\\alpha_\\varphi\\varphi+W_r(r)+W_\\theta(\\theta)$。分离得")+
    fml("p_\\varphi=\\alpha_\\varphi,\\quad p_\\theta^2+\\frac{\\alpha_\\varphi^2}{\\sin^2\\theta}=\\alpha_\\theta^2,\\quad \\frac{1}{2\\mu}(p_r^2+\\frac{\\alpha_\\theta^2}{r^2})-\\frac{k}{r}=E")
    + p("积分 $W_r,W_\\theta$ 后代入 $\\beta_i=\\partial S/\\partial\\alpha_i$，可求得运动方程的解，结果与拉格朗日方法一致。"))
)},
],
},

# ---- 3.3 刚体运动学 ----
{
"name": "3.3 刚体运动学",
"color": "#7c3aed",
"desc": "自由度、欧拉角、角速度、欧拉运动学方程",
"items": [
{"id":"tm-c3s3-1","name":"刚体运动的自由度","tags":["def","thm"],"brief":"刚体有6个自由度。",
 "body": wrap(
    defn("刚体", p("刚体是任意两点间距固定不变的质点系。刚体的一般运动可分解为质心的平动和绕质心的转动。"))
    + thm("自由度", p("刚体的自由度为 6：3 个平动自由度（质心位置）+ 3 个转动自由度（取向）。")+
    fml("\\text{独立坐标数} = 3n - (3n-6) = 6",
        "$n$ 个质点有 $3n$ 个坐标，刚体约束给出 $3n-6$ 个独立约束方程。"))
)},
{"id":"tm-c3s3-2","name":"欧拉角","tags":["def","thm","exa"],"brief":"描述刚体取向的三个角。",
 "body": wrap(
    defn("欧拉角", p("刚体的取向可用三个欧拉角 $(\\varphi,\\theta,\\psi)$ 描述，通过三次连续转动实现：")+
    fml("R = R_z(\\psi)\\,R_x(\\theta)\\,R_z(\\varphi)",
        "（zxz 约定）先绕固定 $z$ 轴转 $\\varphi$（进动角），再绕节线（$x'$ 轴）转 $\\theta$（章动角），最后绕刚体 $z''$ 轴转 $\\psi$（自转角）。"))
    + thm("适用范围", p("欧拉角在 $\\theta=0$ 或 $\\pi$ 处存在奇点（万向锁），此时 $\\varphi$ 和 $\\psi$ 不可区分。在这些奇异性附近需使用其他参数化（如四元数）。"))
)},
{"id":"tm-c3s3-3","name":"刚体的角速度","tags":["def","thm","der"],"brief":"欧拉角速率与角速度的关系。",
 "body": wrap(
    defn("角速度矢量", p("刚体的角速度 $\\vec\\omega$ 可分解为三个欧拉角速率的贡献：")+
    fml("\\vec\\omega = \\dot\\varphi\\,\\hat z + \\dot\\theta\\,\\hat n + \\dot\\psi\\,\\hat z''",
        "其中 $\\hat z$ 为固定系 $z$ 轴，$\\hat n$ 为节线方向，$\\hat z''$ 为刚体 $z$ 轴。"))
    + thm("刚体主轴坐标系下的分量", p("在刚体主轴坐标系中，角速度分量为")+
    fml("\\omega_1 = \\dot\\varphi\\sin\\theta\\sin\\psi + \\dot\\theta\\cos\\psi")
    + fml("\\omega_2 = \\dot\\varphi\\sin\\theta\\cos\\psi - \\dot\\theta\\sin\\psi")
    + fml("\\omega_3 = \\dot\\varphi\\cos\\theta + \\dot\\psi"))
)},
{"id":"tm-c3s3-4","name":"欧拉运动学方程","tags":["thm","der"],"brief":"角速度到欧拉角速率的逆变换。",
 "body": wrap(
    thm("欧拉运动学方程", p("由角速度分量反解欧拉角速率，得欧拉运动学方程")+
    fml("\\dot\\varphi = \\frac{\\omega_1\\sin\\psi+\\omega_2\\cos\\psi}{\\sin\\theta}")
    + fml("\\dot\\theta = \\omega_1\\cos\\psi - \\omega_2\\sin\\psi")
    + fml("\\dot\\psi = \\omega_3 - (\\omega_1\\sin\\psi+\\omega_2\\cos\\psi)\\cot\\theta"))
    + der(p("由 $\\vec\\omega$ 在主轴系的分量表达式解出 $\\dot\\varphi,\\dot\\theta,\\dot\\psi$ 即得。注意 $\\theta=0,\\pi$ 时方程退化。"))
)},
],
},

# ---- 3.4 刚体动力学 ----
{
"name": "3.4 刚体动力学",
"color": "#c2410c",
"desc": "转动惯量张量、惯量主轴、欧拉动力学方程、陀螺",
"items": [
{"id":"tm-c3s4-1","name":"转动惯量张量","tags":["def","thm"],"brief":"描述刚体转动惯性的二阶张量。",
 "body": wrap(
    defn("转动惯量张量", p("刚体的转动动能 $T=\\frac{1}{2}\\vec\\omega^T I\\vec\\omega$，其中 $I$ 为转动惯量张量")+
    fml("I_{ij} = \\int\\rho(\\vec r)(r^2\\delta_{ij}-x_i x_j)\\,dV",
        "对角元 $I_{xx}=\\int\\rho(y^2+z^2)dV$ 等为转动惯量，非对角元 $I_{xy}=-\\int\\rho xy\\,dV$ 等为惯量积。"))
    + thm("角动量", p("刚体的角动量 $\\vec L=I\\vec\\omega$，即 $L_i=\\sum_j I_{ij}\\omega_j$。"))
)},
{"id":"tm-c3s4-2","name":"惯量主轴","tags":["def","thm","der"],"brief":"使惯量张量对角化的坐标系。",
 "body": wrap(
    defn("惯量主轴", p("若坐标系的三个轴是惯量张量的本征矢量方向，则称为惯量主轴。在主轴坐标系中，惯量张量对角化：")+
    fml("I = \\begin{pmatrix} I_1 & 0 & 0 \\\\ 0 & I_2 & 0 \\\\ 0 & 0 & I_3 \\end{pmatrix}",
        "$I_1,I_2,I_3$ 称为主转动惯量。"))
    + thm("对称刚体", p("<strong>球对称陀螺：</strong>$I_1=I_2=I_3$。<br><strong>对称陀螺：</strong>$I_1=I_2\\neq I_3$。<br><strong>不对称陀螺：</strong>$I_1\\neq I_2\\neq I_3$。"))
    + der(p("惯量张量是实对称矩阵，可通过正交变换（转动坐标系）对角化。本征值即为主转动惯量。"))
)},
{"id":"tm-c3s4-3","name":"欧拉动力学方程","tags":["def","thm","der"],"brief":"刚体转动的动力学方程。",
 "body": wrap(
    thm("欧拉动力学方程", p("在刚体主轴坐标系中，刚体转动的动力学方程为")+
    fml("I_1\\dot\\omega_1 + (I_3-I_2)\\omega_2\\omega_3 = N_1")
    + fml("I_2\\dot\\omega_2 + (I_1-I_3)\\omega_3\\omega_1 = N_2")
    + fml("I_3\\dot\\omega_3 + (I_2-I_1)\\omega_1\\omega_2 = N_3",
        "其中 $N_1,N_2,N_3$ 为外力矩在主轴系的分量。"))
    + der(p("由角动量定理 $\\frac{d\\vec L}{dt}=\\vec N$，利用转动系中时间导数关系 $(\\frac{d\\vec L}{dt})_{in}=(\\frac{d\\vec L}{dt})_{rot}+\\vec\\omega\\times\\vec L$，取主轴系分量即得。"))
)},
{"id":"tm-c3s4-4","name":"拉格朗日陀螺","tags":["exa","der","app"],"brief":"对称重刚体的定点运动。",
 "body": wrap(
    defn("拉格朗日陀螺", p("对称陀螺（$I_1=I_2\\neq I_3$）在重力作用下绕固定点的运动，重心在对称轴上距定点 $l$ 处。这是可积系统。"))
    + thm("守恒量", p("拉格朗日陀螺有三个守恒量：<br><strong>能量：</strong>$E=\\frac{1}{2}(I_1\\omega_1^2+I_2\\omega_2^2+I_3\\omega_3^2)+Mgl\\cos\\theta$<br><strong>角动量 $z$ 分量：</strong>$L_z=I_1\\dot\\varphi\\sin^2\\theta+I_3(\\dot\\psi+\\dot\\varphi\\cos\\theta)\\cos\\theta$<br><strong>角动量 $z''$ 分量：</strong>$L_{z''}=I_3(\\dot\\psi+\\dot\\varphi\\cos\\theta)$"))
    + der(p("由拉格朗日函数 $L=\\frac{1}{2}I_1(\\dot\\theta^2+\\dot\\varphi^2\\sin^2\\theta)+\\frac{1}{2}I_3(\\dot\\psi+\\dot\\varphi\\cos\\theta)^2-Mgl\\cos\\theta$，$\\varphi$ 和 $\\psi$ 为循环坐标，故 $p_\\varphi=L_z$ 和 $p_\\psi=L_{z''}$ 守恒。"))
    + app(p("拉格朗日陀螺的运动表现为进动、章动和自转的合成，是陀螺仪表的理论基础。"))
)},
{"id":"tm-c3s4-5","name":"欧拉陀螺","tags":["exa","thm","der"],"brief":"无力矩对称刚体的自由转动。",
 "body": wrap(
    defn("欧拉陀螺", p("不受外力矩（$\\vec N=0$）的刚体定点转动。对于对称欧拉陀螺（$I_1=I_2\\neq I_3$），运动可解析求解。"))
    + thm("自由对称陀螺的解", p("欧拉方程在 $\\vec N=0$ 时为")+
    fml("I_1\\dot\\omega_1+(I_3-I_1)\\omega_2\\omega_3=0,\\quad I_1\\dot\\omega_2+(I_1-I_3)\\omega_3\\omega_1=0,\\quad I_3\\dot\\omega_3=0")
    + p("解得 $\\omega_3=$ 常数，且 $\\omega_1,\\omega_2$ 以频率 $\\Omega=\\frac{|I_3-I_1|}{I_1}\\omega_3$ 绕 $z''$ 轴进动。刚体对称轴在空间中绕固定角动量方向做规则进动。"))
    + der(p("由 $\\dot\\omega_3=0$ 知 $\\omega_3$ 守恒。令 $\\omega_\\pm=\\omega_1\\pm i\\omega_2$，则 $\\dot\\omega_\\pm=\\mp i\\Omega\\omega_\\pm$，解得 $\\omega_\\pm=A_\\pm e^{\\mp i\\Omega t}$，即 $\\omega_1,\\omega_2$ 做简谐振动。"))
)},
{"id":"tm-c3s4-6","name":"惯量椭球与潘索描述","tags":["def","thm","note"],"brief":"欧拉陀螺运动的几何描述。",
 "body": wrap(
    defn("惯量椭球", p("在主轴坐标系中，由 $\\sum I_i x_i^2=1$ 定义的椭球称为惯量椭球。角速度矢量端点在惯量椭球上的运动轨迹称为本体极迹。"))
    + thm("潘索描述", p("自由刚体的运动等价于惯量椭球在固定平面（不变平面）上的无滑动滚动。椭球中心到不变平面的距离为 $\\sqrt{2T}/|\\vec L|$，角速度矢量端点在固定平面上的轨迹称为空间极迹。"))
    + note(p("潘索描述给出了欧拉陀螺运动的直观几何图像，是刚体动力学的经典几何方法。"))
)},
],
},
]

print(f"Ch3 Classical: {sum(len(s['items']) for s in ch3_sections)} items")

# =====================================================
#  ASSEMBLE CHAPTERS
# =====================================================
CHAPTERS = [
    {"id":"tm-ch1","num":"第一章","title":"拉格朗日力学","en":"LAGRANGIAN MECHANICS",
     "desc":"从约束与广义坐标出发，经达朗贝尔方程到欧拉-拉格朗日方程，再以变分法与最小作用量原理重构力学，最后讨论电磁场中的拉格朗日函数、诺特定理与非惯性系。",
     "sections": ch1_sections},
    {"id":"tm-ch2","num":"第二章","title":"哈密顿力学","en":"HAMILTONIAN MECHANICS",
     "desc":"通过勒让德变换从拉格朗日力学过渡到哈密顿力学，研究正则方程、泊松括号、正则变换与母函数、哈密顿-雅科比方程，以及无穷小变换与诺特定理。",
     "sections": ch2_sections},
    {"id":"tm-ch3","num":"第三章","title":"力学经典问题","en":"CLASSICAL PROBLEMS",
     "desc":"应用拉格朗日与哈密顿力学求解经典问题：微振动与简正坐标、中心势场中的开普勒问题、刚体运动学与动力学（欧拉角、欧拉方程、陀螺）。",
     "sections": ch3_sections},
]

total_items = sum(sum(len(s["items"]) for s in ch["sections"]) for ch in CHAPTERS)
print(f"Total items: {total_items}")

# =====================================================
#  HTML GENERATION
# =====================================================
def gen_html():
    # Build LA_DATA as JS object string
    data_lines = []
    for ch in CHAPTERS:
        sec_strs = []
        for sec in ch["sections"]:
            item_strs = []
            for it in sec["items"]:
                tags_js = json.dumps(it["tags"], ensure_ascii=False)
                body_esc = js_escape(it["body"])
                item_strs.append(
                    f"{{id:'{it['id']}',name:{json.dumps(it['name'],ensure_ascii=False)},"
                    f"tags:{tags_js},brief:{json.dumps(it['brief'],ensure_ascii=False)},"
                    f"body:`{body_esc}`}}"
                )
            sec_strs.append(
                f"{{name:{json.dumps(sec['name'],ensure_ascii=False)},"
                f"color:'{sec['color']}',desc:{json.dumps(sec['desc'],ensure_ascii=False)},"
                f"items:[{','.join(item_strs)}]}}"
            )
        data_lines.append(
            f"{{id:'{ch['id']}',num:{json.dumps(ch['num'],ensure_ascii=False)},"
            f"title:{json.dumps(ch['title'],ensure_ascii=False)},en:'{ch['en']}',"
            f"desc:{json.dumps(ch['desc'],ensure_ascii=False)},"
            f"sections:[{','.join(sec_strs)}]}}"
        )
    la_data = "[" + ",".join(data_lines) + "]"

    # Build LA_FIG (only include used figures)
    used_figs = set()
    for ch in CHAPTERS:
        for sec in ch["sections"]:
            for it in sec["items"]:
                if "fig" in it:
                    used_figs.add(it["fig"])
    fig_entries = []
    for k, v in FIG.items():
        if k in used_figs or True:  # include all for simplicity
            fig_entries.append(f"{json.dumps(k)}:`{js_escape(v)}`")
    fig_js = "{" + ",".join(fig_entries) + "}"

    tag_label_js = json.dumps(TAG_LABEL, ensure_ascii=False)

    # Nav tabs
    nav_tabs = "".join(
        f'<a class="la-nav-tab c{i+1}" href="#{ch["id"]}">{ch["num"]} · {ch["title"]}</a>'
        for i, ch in enumerate(CHAPTERS)
    )

    # chapter color classes exist in CSS: la-ch1..la-ch6
    # CSS
    css = '''  :root{--la-bg:#f4f7fb;--la-card:#ffffff;--la-ink:#152033;--la-muted:#607089;--la-shadow:0 12px 32px rgba(20,36,60,.09);}
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;color:var(--la-ink);background:radial-gradient(circle at 10% 10%,rgba(37,99,235,.08),transparent 28%),radial-gradient(circle at 90% 10%,rgba(124,58,237,.08),transparent 28%),var(--la-bg);line-height:1.7}
  a{color:inherit}
  .la-wrap{width:min(1400px,94vw);margin:auto}
  .la-header{padding:52px 0 20px;text-align:center}
  .la-eyebrow{font-size:13px;letter-spacing:.22em;color:var(--la-muted);font-weight:700;text-transform:uppercase}
  h1{margin:10px 0 8px;font-size:clamp(30px,5vw,54px);line-height:1.08;letter-spacing:-.03em}
  .la-subtitle{margin:0 auto;color:var(--la-muted);font-size:16px;max-width:820px;line-height:1.8}
  .back-bar{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:22px 0 6px}
  .back-btn{display:inline-flex;align-items:center;gap:8px;padding:10px 22px;border-radius:999px;text-decoration:none;font-size:14px;font-weight:800;background:#fff;color:#1e3a8a;border:1px solid #c7d7ee;box-shadow:0 8px 20px rgba(20,36,60,.08);transition:.25s;cursor:pointer}
  .back-btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px rgba(20,36,60,.14);color:#4c1d95;border-color:#ddd6fe}
  .la-nav-tabs{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:22px 0 8px}
  .la-nav-tab{padding:8px 16px;border-radius:999px;text-decoration:none;font-weight:700;font-size:13px;border:1px solid #d5deea;background:#fff;transition:.25s;color:#334155}
  .la-nav-tab:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(20,36,60,.1)}
  .la-nav-tab.c1{color:#1e40af;border-color:#bfdbfe}
  .la-nav-tab.c2{color:#0f766e;border-color:#99f6e4}
  .la-nav-tab.c3{color:#047857;border-color:#a7f3d0}
  .la-nav-tab.c4{color:#c2410c;border-color:#fed7aa}
  .la-nav-tab.c5{color:#6d28d9;border-color:#ddd6fe}
  .la-nav-tab.c6{color:#be185d;border-color:#fbcfe8}
  .la-toolbar{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:16px 0 8px}
  button{border:1px solid #d5deea;background:#fff;color:var(--la-ink);border-radius:999px;padding:9px 14px;font:inherit;cursor:pointer;transition:.2s ease}
  button:hover{transform:translateY(-1px);box-shadow:0 8px 20px rgba(20,36,60,.08)}
  .la-engagement-bar{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:10px 0 0}
  .la-stat-item{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;background:#fff;border:1px solid #d5deea;border-radius:999px;font-size:14px;font-weight:600;color:#475569}
  .la-stat-value{color:#2563eb;font-weight:800}
  .la-legend{margin:26px auto 0;max-width:1100px;background:rgba(255,255,255,.8);border:1px solid #dde5ef;border-radius:20px;padding:16px 22px;display:flex;gap:14px;flex-wrap:wrap;justify-content:center;box-shadow:var(--la-shadow)}
  .la-legend-title{font-size:12px;font-weight:800;letter-spacing:.16em;color:#94a3b8;align-self:center;margin-right:6px}
  .la-arc-badge{display:inline-flex;align-items:center;font-size:10px;font-weight:800;padding:3px 8px;border-radius:6px;letter-spacing:.03em;white-space:nowrap}
  .la-arc-def{background:#dbeafe;color:#1e40af}
  .la-arc-thm{background:#d1fae5;color:#065f46}
  .la-arc-der{background:#ede9fe;color:#5b21b6}
  .la-arc-exa{background:#cffafe;color:#155e75}
  .la-arc-app{background:#ffedd5;color:#9a3412}
  .la-arc-his{background:#f1f5f9;color:#475569}
  .la-arc-note{background:#fee2e2;color:#b91c1c}
  .la-roadmap{margin-top:30px;background:rgba(255,255,255,.74);border:1px solid rgba(189,201,218,.7);box-shadow:var(--la-shadow);border-radius:28px;padding:34px}
  .la-phase-title{font-size:24px;font-weight:800;margin:60px 0 4px;display:flex;align-items:center;gap:12px;color:#1e293b;letter-spacing:-.01em}
  .la-phase-title:first-child{margin-top:0}
  .la-phase-title::before{content:"";display:block;width:6px;height:30px;border-radius:4px;background:#2563eb;flex-shrink:0}
  .la-phase-title.la-ch1::before{background:#2563eb}
  .la-phase-title.la-ch2::before{background:#0d9488}
  .la-phase-title.la-ch3::before{background:#059669}
  .la-phase-title.la-ch4::before{background:#c2410c}
  .la-phase-title.la-ch5::before{background:#7c3aed}
  .la-phase-title.la-ch6::before{background:#be185d}
  .la-phase-en{font-size:11px;letter-spacing:.36em;color:#94a3b8;font-weight:700;text-transform:uppercase;margin:0 0 12px 18px;font-style:italic}
  .la-phase-desc{color:var(--la-muted);font-size:14px;margin:0 0 24px 18px;line-height:1.8;max-width:960px}
  .la-domain{margin-bottom:26px;padding:16px 18px 18px 22px;position:relative;background:rgba(255,255,255,.6);border-radius:18px;border:1px solid #e5ebf2}
  .la-domain::before{content:"";position:absolute;left:6px;top:16px;bottom:16px;width:5px;border-radius:5px;background:var(--domain-color,#2563eb);box-shadow:0 0 12px rgba(37,99,235,.25)}
  .la-domain-header{display:flex;align-items:center;gap:10px;margin-bottom:14px;padding-left:6px;flex-wrap:wrap}
  .la-domain-header h3{margin:0;font-size:18px;color:#1e293b}
  .la-domain-count{font-size:11px;padding:3px 10px;border-radius:999px;background:#f1f5f9;color:#64748b;font-weight:600}
  .la-domain-desc{font-size:12px;color:#94a3b8;margin-left:auto;font-style:italic}
  .la-domain-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}
  .la-course-card{background:#fff;border:1px solid #dbe3ee;border-radius:14px;padding:14px;cursor:pointer;transition:.25s;position:relative;overflow:hidden}
  .la-course-card:hover{transform:translateY(-3px);box-shadow:0 10px 20px rgba(25,44,75,.1);border-color:#aabbd0}
  .la-course-card h4{margin:0 0 8px;font-size:14.5px;line-height:1.35;color:#1e293b}
  .la-course-card p{margin:0;font-size:11.5px;color:var(--la-muted);line-height:1.6}
  .la-arc-badges{display:flex;flex-wrap:wrap;gap:3px;margin-bottom:8px}
  .la-overlay{position:fixed;inset:0;background:rgba(15,23,42,.5);display:none;align-items:center;justify-content:center;padding:18px;z-index:60;backdrop-filter:blur(2px)}
  .la-overlay.show{display:flex}
  .la-modal{width:min(820px,96vw);background:white;border-radius:24px;padding:30px;box-shadow:0 24px 80px rgba(0,0,0,.28);animation:laPopIn .3s;max-height:90vh;overflow-y:auto}
  @keyframes laPopIn{from{transform:scale(.94);opacity:0}to{transform:scale(1);opacity:1}}
  .la-modal h2{margin:0 0 10px;font-size:23px;color:#1e293b;line-height:1.35}
  .la-modal .la-crumbs{font-size:12px;color:#94a3b8;margin:0 0 14px;font-weight:600;letter-spacing:.02em}
  .la-modal .la-arc-badges{margin:0 0 16px}
  .la-modal-body{color:#334155;font-size:15px;line-height:1.9}
  .la-modal-body p{margin:0 0 12px}
  .la-modal-body strong{color:#0f172a}
  .la-modal-body ul{margin:0 0 12px;padding-left:22px}
  .la-modal-body li{margin-bottom:6px}
  .la-fml{margin:16px 0;padding:14px 18px;background:linear-gradient(135deg,#f8fafc,#eef4fb);border-left:4px solid #93b4e8;border-radius:10px;overflow-x:auto;font-size:16px}
  .la-fml .note{display:block;font-size:12.5px;color:#8496ad;margin-top:8px;line-height:1.6;font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
  .la-fml mjx-container[display="true"]{margin:0 !important}
  .la-fig{margin:18px auto;padding:14px 16px 10px;background:#fafcff;border:1px solid #e2ebf7;border-radius:14px;display:flex;flex-direction:column;align-items:center;max-width:600px}
  .la-fig svg{display:block;width:100%;height:auto;max-width:560px}
  .la-fig .la-fig-cap{font-size:12px;color:#8496ad;margin-top:8px;text-align:center;letter-spacing:.02em}
  .la-callout{margin:14px 0;padding:12px 16px;background:#fffbeb;border-left:3px solid #fbbf24;border-radius:8px;font-size:13.5px;color:#78350f;line-height:1.8}
  .la-kp-sec{margin:0 0 18px;padding:14px 16px;border-radius:12px;background:#f8fafc;border:1px solid #eef2f7}
  .la-kp-sec h5{margin:0 0 10px;font-size:14px;color:#1e293b;letter-spacing:.04em;display:flex;align-items:center;gap:8px}
  .la-kp-sec h5::before{content:"";width:4px;height:14px;border-radius:2px;background:var(--la-accent,#3b82f6)}
  .la-kp-def{border-left:3px solid #3b82f6}
  .la-kp-thm{border-left:3px solid #8b5cf6;background:#faf7ff}
  .la-kp-der{border-left:3px solid #0ea5e9;background:#f0f9ff}
  .la-kp-exa{border-left:3px solid #10b981;background:#f0fdf4}
  .la-kp-app{border-left:3px solid #f59e0b;background:#fffbeb}
  .la-kp-note{border-left:3px solid #ef4444;background:#fef2f2}
  .la-kp-his{border-left:3px solid #64748b;background:#f8fafc}
  .la-kp-ext{border-left:3px solid #ec4899;background:#fdf2f8}
  .la-kp-sec p:last-child{margin-bottom:0}
  .la-modal-close{margin-top:22px;background:#0f172a;color:white;border-color:#0f172a;padding:10px 20px;font-weight:bold}
  .la-footer{padding:34px 0 50px;color:var(--la-muted);text-align:center;font-size:13px;line-height:1.9}
  @media(max-width:900px){.la-wrap{width:min(94vw,720px)}.la-roadmap{padding:20px}.la-phase-title{font-size:19px}.la-phase-en{font-size:10px;letter-spacing:.26em}.la-domain-desc{display:none}.la-domain-grid{grid-template-columns:repeat(auto-fill,minmax(160px,1fr))}.la-modal{padding:22px}}'''

    js = f'''const LA_DATA = {la_data};
const LA_TAG_LABEL = {tag_label_js};
const LA_FIG = {fig_js};
const LA_KP = {{}};
function laBuildCard(item){{
  const tags = item.tags.map(t => `<span class="la-arc-badge la-arc-${{t}}">${{LA_TAG_LABEL[t]}}</span>`).join('');
  return `<div class="la-course-card" onclick="showLaItem('${{item.id}}')"><div class="la-arc-badges">${{tags}}</div><h4>${{item.name}}</h4><p>${{item.brief}}</p></div>`;
}}
function renderLa(){{
  const root = document.getElementById('laRoadmap');
  let html = '';
  LA_DATA.forEach(ch => {{
    html += `<h2 class="la-phase-title ${{ch.id}}" id="${{ch.id}}">${{ch.num}} · ${{ch.title}}</h2>`;
    html += `<div class="la-phase-en">${{ch.en}}</div>`;
    html += `<p class="la-phase-desc">${{ch.desc}}</p>`;
    ch.sections.forEach(sec => {{
      html += `<div class="la-domain" style="--domain-color:${{sec.color}};"><div class="la-domain-header"><h3>${{sec.name}}</h3><span class="la-domain-count">${{sec.items.length}} 个知识点</span><span class="la-domain-desc">${{sec.desc}}</span></div><div class="la-domain-grid">`;
      sec.items.forEach(it => {{ html += laBuildCard(it); LA_KP[it.id] = {{item: it, section: sec.name, chapter: `${{ch.num}} · ${{ch.title}}`}}; }});
      html += `</div></div>`;
    }});
  }});
  root.innerHTML = html;
  const kCount = Object.keys(LA_KP).length;
  const fCount = (root.innerHTML.match(/\\$\\$/g) || []).length;
  document.getElementById('laKCount').textContent = kCount;
  document.getElementById('laFCount').textContent = Math.round(fCount / 2);
}}
function showLaItem(id){{
  const rec = LA_KP[id];
  if(!rec) return;
  const it = rec.item;
  document.getElementById('laCrumbs').textContent = rec.chapter + ' ／ ' + rec.section;
  document.getElementById('laTitle').textContent = it.name;
  document.getElementById('laTags').innerHTML = it.tags.map(t => `<span class="la-arc-badge la-arc-${{t}}">${{LA_TAG_LABEL[t]}}</span>`).join('');
  let bodyHtml = it.body;
  if (it.fig && LA_FIG[it.fig]) {{
    const figHtml = `<div class="la-fig">${{LA_FIG[it.fig]}}<div class="la-fig-cap">${{it.figCap || ''}}</div></div>`;
    bodyHtml = figHtml + bodyHtml;
  }}
  document.getElementById('laBody').innerHTML = bodyHtml;
  document.getElementById('laOverlay').classList.add('show');
  document.querySelector('.la-modal').scrollTop = 0;
  if (window.MathJax && window.MathJax.typesetPromise) {{ window.MathJax.typesetPromise([document.getElementById('laBody')]).catch(()=>{{}}); }}
}}
function hideLaInfo(){{ document.getElementById('laOverlay').classList.remove('show'); }}
function closeLaInfo(e){{ if(e.target.id === 'laOverlay') hideLaInfo(); }}
document.addEventListener('keydown', e => {{ if(e.key === 'Escape') hideLaInfo(); }});
document.addEventListener('DOMContentLoaded', () => {{
  renderLa();
  if (window.MathJax && window.MathJax.typesetPromise) {{ window.MathJax.typesetPromise([document.getElementById('laRoadmap')]).catch(()=>{{}}); }}
}});'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="理论力学知识体系：拉格朗日力学、哈密顿力学、力学经典问题">
<title>理论力学 · 知识体系</title>
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['$','$'], ['\\\\(','\\\\)']],
    displayMath: [['$$','$$'], ['\\\\[','\\\\]']],
    processEscapes: true,
    packages: {{'[+]': ['ams','boldsymbol']}}
  }},
  options: {{
    skipHtmlTags: ['script','noscript','style','textarea','pre','code'],
    ignoreHtmlClass: 'tex2jax_ignore'
  }},
  svg: {{ fontCache: 'global' }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="MathJax-script" async></script>
<style>
{css}
</style>
</head>
<body>
<div class="la-wrap">
  <header class="la-header">
    <div class="la-eyebrow">THEORETICAL MECHANICS · KNOWLEDGE MAP</div>
    <h1>理论力学 · 知识体系</h1>
    <p class="la-subtitle">拉格朗日力学 · 哈密顿力学 · 力学经典问题</p>
    <div class="back-bar"><a class="back-btn" href="index.html">← 返回总览</a></div>
    <div class="la-nav-tabs">{nav_tabs}</div>
    <div class="la-toolbar">
      <button onclick="window.scrollTo({{top:0,behavior:'smooth'}})">回到顶部</button>
    </div>
    <div class="la-engagement-bar">
      <div class="la-stat-item"><span>📘</span><span class="la-stat-value" id="laKCount">--</span><span>个知识点</span></div>
      <div class="la-stat-item"><span>🧮</span><span class="la-stat-value" id="laFCount">--</span><span>条核心公式</span></div>
    </div>
  </header>
  <div class="la-legend">
    <span class="la-legend-title">知识记号</span>
    <span class="la-arc-badge la-arc-def">定 义</span>
    <span class="la-arc-badge la-arc-thm">定 理</span>
    <span class="la-arc-badge la-arc-der">推 导</span>
    <span class="la-arc-badge la-arc-exa">例 子</span>
    <span class="la-arc-badge la-arc-app">应 用</span>
    <span class="la-arc-badge la-arc-note">备 注</span>
  </div>
  <main class="la-roadmap" id="laRoadmap"></main>
  <footer class="la-footer">
    <div>理论力学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于南开大学物理学院理论力学讲义整理</div>
  </footer>
</div>
<div class="la-overlay" id="laOverlay" onclick="closeLaInfo(event)">
  <div class="la-modal" onclick="event.stopPropagation()">
    <p class="la-crumbs" id="laCrumbs"></p>
    <h2 id="laTitle">知识点</h2>
    <div class="la-arc-badges" id="laTags"></div>
    <div class="la-modal-body" id="laBody"></div>
    <button class="la-modal-close" onclick="hideLaInfo()">关 闭</button>
  </div>
</div>
<script>
{js}
</script>
</body>
</html>'''
    return html

if __name__ == "__main__":
    html = gen_html()
    with open("/workspace/theoretical-mechanics.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated theoretical-mechanics.html ({len(html)} chars)")

