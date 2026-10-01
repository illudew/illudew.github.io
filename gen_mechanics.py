# -*- coding: utf-8 -*-
"""Generate newtonian-mechanics.html with 5 chapters: 运动学/动力学/功能/刚体/振动与波."""
import json

# ---------- SVG figure library ----------
FIG = {
"trajectory": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="140" x2="230" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="10" y1="140" x2="10" y2="10" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M 10 130 Q 120 10 230 100" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<circle cx="10" cy="130" r="4" fill="#ef4444"/>
<circle cx="120" cy="40" r="4" fill="#ef4444"/>
<circle cx="230" cy="100" r="4" fill="#ef4444"/>
<line x1="120" y1="40" x2="145" y2="35" stroke="#10b981" stroke-width="2"/>
<polygon points="145,35 135,33 138,41" fill="#10b981"/>
<text x="148" y="32" font-size="11" fill="#10b981">v</text>
<text x="215" y="155" font-size="11" fill="#475569">x</text>
<text x="2" y="14" font-size="11" fill="#475569">y</text></svg>''',
"projectile": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="140" x2="230" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="10" y1="140" x2="10" y2="10" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M 10 140 Q 120 10 230 140" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<line x1="10" y1="140" x2="60" y2="110" stroke="#ef4444" stroke-width="2.5"/>
<polygon points="60,110 50,112 55,120" fill="#ef4444"/>
<text x="62" y="108" font-size="11" fill="#ef4444">v₀</text>
<line x1="10" y1="140" x2="55" y2="140" stroke="#f59e0b" stroke-width="1.5"/>
<polygon points="55,140 47,136 47,144" fill="#f59e0b"/>
<text x="30" y="152" font-size="10" fill="#f59e0b">v₀cosθ</text>
<line x1="10" y1="140" x2="10" y2="115" stroke="#10b981" stroke-width="1.5"/>
<polygon points="10,115 6,123 14,123" fill="#10b981"/>
<text x="-4" y="125" font-size="10" fill="#10b981">v₀sinθ</text>
<text x="55" y="135" font-size="10" fill="#475569">θ</text></svg>''',
"circular": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="55" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="120" cy="80" r="3" fill="#475569"/>
<circle cx="175" cy="80" r="5" fill="#ef4444"/>
<line x1="120" y1="80" x2="175" y2="80" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3 3"/>
<text x="140" y="74" font-size="11" fill="#475569">r</text>
<line x1="175" y1="80" x2="175" y2="40" stroke="#10b981" stroke-width="2.5"/>
<polygon points="175,40 169,50 181,50" fill="#10b981"/>
<text x="180" y="42" font-size="11" fill="#10b981">v</text>
<line x1="175" y1="80" x2="120" y2="80" stroke="#ef4444" stroke-width="2.5"/>
<polygon points="120,80 130,74 130,86" fill="#ef4444"/>
<text x="122" y="72" font-size="11" fill="#ef4444">aₙ</text></svg>''',
"fbd": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="90" y="60" width="60" height="50" rx="6" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<line x1="120" y1="110" x2="120" y2="150" stroke="#ef4444" stroke-width="2.5"/>
<polygon points="120,150 114,140 126,140" fill="#ef4444"/>
<text x="126" y="145" font-size="11" fill="#ef4444">mg</text>
<line x1="120" y1="60" x2="120" y2="20" stroke="#10b981" stroke-width="2.5"/>
<polygon points="120,20 114,30 126,30" fill="#10b981"/>
<text x="126" y="28" font-size="11" fill="#10b981">N</text>
<line x1="150" y1="85" x2="190" y2="85" stroke="#f59e0b" stroke-width="2.5"/>
<polygon points="190,85 180,79 180,91" fill="#f59e0b"/>
<text x="162" y="78" font-size="11" fill="#f59e0b">F</text></svg>''',
"inclined": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="140" x2="220" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="140" x2="200" y2="40" stroke="#64748b" stroke-width="3"/>
<rect x="100" y="78" width="36" height="26" rx="3" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5" transform="rotate(-30 118 91)"/>
<line x1="118" y1="104" x2="118" y2="138" stroke="#ef4444" stroke-width="2"/>
<polygon points="118,138 112,128 124,128" fill="#ef4444"/>
<text x="122" y="134" font-size="10" fill="#ef4444">mg</text>
<line x1="118" y1="91" x2="100" y2="60" stroke="#10b981" stroke-width="2"/>
<polygon points="100,60 106,70 112,62" fill="#10b981"/>
<text x="82" y="58" font-size="10" fill="#10b981">N</text>
<line x1="118" y1="91" x2="160" y2="115" stroke="#f59e0b" stroke-width="2"/>
<polygon points="160,115 150,110 152,120" fill="#f59e0b"/>
<text x="140" y="125" font-size="10" fill="#f59e0b">f</text></svg>''',
"pendulum": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="120" y1="10" x2="120" y2="130" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="120" y1="10" x2="165" y2="100" stroke="#475569" stroke-width="2"/>
<circle cx="165" cy="100" r="10" fill="#3b82f6"/>
<line x1="165" y1="100" x2="165" y2="135" stroke="#ef4444" stroke-width="2"/>
<polygon points="165,135 159,125 171,125" fill="#ef4444"/>
<text x="170" y="128" font-size="11" fill="#ef4444">mg</text>
<path d="M 120 50 A 40 40 0 0 1 165 100" fill="none" stroke="#94a3b8" stroke-width="1"/>
<text x="122" y="45" font-size="11" fill="#475569">θ</text>
<text x="138" y="60" font-size="10" fill="#64748b">L</text></svg>''',
"wave": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 10 80 Q 40 30 70 80 T 130 80 T 190 80 T 230 80" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<line x1="70" y1="30" x2="70" y2="80" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 3"/>
<text x="60" y="55" font-size="10" fill="#ef4444">A</text>
<line x1="10" y1="120" x2="130" y2="120" stroke="#10b981" stroke-width="1.5"/>
<polygon points="10,120 16,116 16,124" fill="#10b981"/>
<polygon points="130,120 124,116 124,124" fill="#10b981"/>
<text x="60" y="115" font-size="10" fill="#10b981">λ</text></svg>''',
"shm": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M 10 80 Q 40 30 70 80 T 130 80 T 190 80 T 230 80" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="70" cy="30" r="4" fill="#ef4444"/>
<circle cx="190" cy="130" r="4" fill="#ef4444"/>
<text x="74" y="26" font-size="10" fill="#ef4444">+A</text>
<text x="194" y="140" font-size="10" fill="#ef4444">-A</text>
<text x="100" y="70" font-size="10" fill="#475569">O</text></svg>''',
"rotation": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="50" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" opacity="0.5"/>
<circle cx="120" cy="80" r="3" fill="#475569"/>
<circle cx="160" cy="80" r="5" fill="#ef4444"/>
<line x1="120" y1="80" x2="160" y2="80" stroke="#94a3b8" stroke-width="1.5"/>
<text x="135" y="74" font-size="10" fill="#475569">r</text>
<path d="M 120 30 A 50 50 0 0 1 170 80" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4 3"/>
<text x="155" y="42" font-size="11" fill="#10b981">ω</text>
<line x1="160" y1="80" x2="160" y2="45" stroke="#3b82f6" stroke-width="2"/>
<polygon points="160,45 154,55 166,55" fill="#3b82f6"/>
<text x="165" y="50" font-size="11" fill="#3b82f6">v</text></svg>''',
"collision": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="100" x2="230" y2="100" stroke="#94a3b8" stroke-width="1.5"/>
<circle cx="70" cy="90" r="18" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<text x="62" y="94" font-size="11" fill="#1e293b">m₁</text>
<circle cx="170" cy="90" r="18" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
<text x="162" y="94" font-size="11" fill="#1e293b">m₂</text>
<line x1="88" y1="90" x2="110" y2="90" stroke="#3b82f6" stroke-width="2"/>
<polygon points="110,90 102,86 102,94" fill="#3b82f6"/>
<text x="92" y="82" font-size="10" fill="#3b82f6">v₁</text>
<line x1="152" y1="90" x2="130" y2="90" stroke="#f59e0b" stroke-width="2"/>
<polygon points="130,90 138,86 138,94" fill="#f59e0b"/>
<text x="130" y="82" font-size="10" fill="#f59e0b">v₂</text></svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

# ---------- 核心公式清单 ----------
CORE_FORMULAS = [
    ("速度定义", "\\mathbf{v} = \\frac{d\\mathbf{r}}{dt}", "位置矢量对时间的导数"),
    ("加速度定义", "\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{d^2\\mathbf{r}}{dt^2}", "速度对时间的导数"),
    ("匀变速直线运动", "v = v_0 + at,\\quad x = x_0 + v_0 t + \\tfrac{1}{2}at^2", "加速度恒定的运动学方程"),
    ("速度-位移关系", "v^2 - v_0^2 = 2a(x-x_0)", "不含时间的运动学关系"),
    ("抛体运动轨迹", "y = x\\tan\\theta - \\frac{g x^2}{2 v_0^2 \\cos^2\\theta}", "抛物线轨迹方程"),
    ("向心加速度", "a_n = \\frac{v^2}{r} = \\omega^2 r", "匀速圆周运动的法向加速度"),
    ("牛顿第二定律", "\\mathbf{F} = m\\mathbf{a} = \\frac{d\\mathbf{p}}{dt}", "力等于动量变化率"),
    ("动量", "\\mathbf{p} = m\\mathbf{v}", "质量与速度的乘积"),
    ("冲量", "\\mathbf{I} = \\int_{t_1}^{t_2} \\mathbf{F}\\,dt = \\Delta\\mathbf{p}", "冲量等于动量变化"),
    ("动量守恒", "\\sum m_i \\mathbf{v}_i = \\text{常量} \\quad (\\sum \\mathbf{F}_{ext}=0)", "合外力为零时动量守恒"),
    ("功", "W = \\int_{a}^{b} \\mathbf{F}\\cdot d\\mathbf{r}", "力沿路径的线积分"),
    ("动能", "E_k = \\frac{1}{2} m v^2", "运动物体具有的能量"),
    ("动能定理", "W_{\\text{合}} = \\Delta E_k = \\tfrac{1}{2}mv^2 - \\tfrac{1}{2}mv_0^2", "合外力做功等于动能变化"),
    ("功率", "P = \\mathbf{F}\\cdot\\mathbf{v} = \\frac{dW}{dt}", "做功的快慢"),
    ("重力势能", "E_p = mgh", "重力场中的势能"),
    ("弹性势能", "E_p = \\frac{1}{2} k x^2", "弹簧形变储存的势能"),
    ("机械能守恒", "E_k + E_p = \\text{常量} \\quad (\\text{只有保守力做功})", "动能与势能之和不变"),
    ("转动惯量", "I = \\sum m_i r_i^2 = \\int r^2 dm", "刚体转动惯性的量度"),
    ("转动定律", "M = I\\beta = \\frac{dL}{dt}", "合外力矩等于角动量变化率"),
    ("角动量", "L = I\\omega = \\mathbf{r}\\times m\\mathbf{v}", "转动惯性与角速度的乘积"),
    ("角动量守恒", "L = I\\omega = \\text{常量} \\quad (\\sum M_{ext}=0)", "合外力矩为零时角动量守恒"),
    ("转动动能", "E_k = \\frac{1}{2} I \\omega^2", "刚体转动动能"),
    ("简谐振动方程", "x = A\\cos(\\omega t + \\varphi)", "简谐振动的位移表达式"),
    ("角频率", "\\omega = \\sqrt{\\frac{k}{m}} = 2\\pi f = \\frac{2\\pi}{T}", "弹簧振子的固有角频率"),
    ("单摆周期", "T = 2\\pi\\sqrt{\\frac{L}{g}}", "小角度近似下单摆周期"),
    ("波速", "v = \\lambda f = \\frac{\\lambda}{T}", "波长、频率与波速的关系"),
    ("简谐波方程", "y = A\\cos\\left[\\omega\\left(t - \\frac{x}{v}\\right) + \\varphi\\right]", "沿 x 正方向传播的简谐波"),
    ("驻波方程", "y = 2A\\cos\\frac{2\\pi x}{\\lambda}\\cos\\omega t", "两列反向行波叠加形成驻波"),
]

# ---------- helper functions ----------
def js_escape(s):
    return s.replace("\\","\\\\").replace("`","\\`").replace("${","\\${")
def defn(t, body): return f'<section class="la-kp-sec la-kp-def"><h5>定 义</h5><p><strong>{t}</strong></p>{body}</section>'
def thm(t, body): return f'<section class="la-kp-sec la-kp-thm"><h5>定 理 · {t}</h5>{body}</section>'
def der(body): return f'<section class="la-kp-sec la-kp-der"><h5>推 导</h5>{body}</section>'
def exa(body): return f'<section class="la-kp-sec la-kp-exa"><h5>例 子</h5>{body}</section>'
def app(body): return f'<section class="la-kp-sec la-kp-app"><h5>应 用</h5>{body}</section>'
def note(body): return f'<section class="la-kp-sec la-kp-note"><h5>备 注</h5>{body}</section>'
def fml(latex, caption=""):
    cap = f'<span class="note">{caption}</span>' if caption else ""
    return f'<div class="la-fml">$${latex}$$ {cap}</div>'
def p(txt): return f'<p>{txt}</p>'
def wrap(body): return f'<div class="la-kp">{body}</div>'

# =====================================================
#  CHAPTER 1: 质点运动学
# =====================================================
ch1_sections = [
# ---- 1.1 位置、位移与速度 ----
{
"name": "1.1 位置矢量与位移",
"color": "#2563eb",
"desc": "位置矢量、位移矢量、速度的定义与性质",
"items": [
{"id":"c1s1-1","name":"位置矢量与位移","tags":["def","der"],"brief":"用矢量描述质点的空间位置及其变化。",
 "fig":"trajectory","figCap":"质点的运动轨迹与位置矢量",
 "body": wrap(
   defn("位置矢量",p("设参考点为原点 $O$，质点在时刻 $t$ 的位置由从 $O$ 指向质点的矢量 $\\mathbf{r}(t)$ 描述，称为<strong>位置矢量</strong>（位矢）。在直角坐标系中：")+
   fml("\\mathbf{r}(t) = x(t)\\,\\mathbf{i} + y(t)\\,\\mathbf{j} + z(t)\\,\\mathbf{k}"))+
   defn("位移矢量",p("质点从位置 $\\mathbf{r}_1$ 到 $\\mathbf{r}_2$ 的<strong>位移</strong>为：")+
   fml("\\Delta\\mathbf{r} = \\mathbf{r}_2 - \\mathbf{r}_1 = \\Delta x\\,\\mathbf{i}+\\Delta y\\,\\mathbf{j}+\\Delta z\\,\\mathbf{k}"))+
   note(p("位移是矢量，只取决于始末位置，与路径无关。路程（标量）是实际轨迹长度，$\\Delta s \\ge |\\Delta\\mathbf{r}|$，仅当单向直线运动时取等号。"))+
   defn("速度",p("速度是位矢对时间的变化率，描述运动的快慢和方向：")+
   fml("\\mathbf{v} = \\lim_{\\Delta t\\to 0}\\frac{\\Delta\\mathbf{r}}{\\Delta t} = \\frac{d\\mathbf{r}}{dt}"))+
   der(p("<strong>速度的分量形式：</strong>将 $\\mathbf{r}=x\\mathbf{i}+y\\mathbf{j}+z\\mathbf{k}$ 代入速度定义，注意 $\\mathbf{i},\\mathbf{j},\\mathbf{k}$ 为常矢量（方向不变）：")+
   fml("\\mathbf{v} = \\frac{dx}{dt}\\mathbf{i}+\\frac{dy}{dt}\\mathbf{j}+\\frac{dz}{dt}\\mathbf{k} = v_x\\mathbf{i}+v_y\\mathbf{j}+v_z\\mathbf{k}")+
   p("速率 $v=|\\mathbf{v}|=\\sqrt{v_x^2+v_y^2+v_z^2}$。瞬时速度的方向沿轨迹切线方向。"))
 )},
{"id":"c1s1-2","name":"加速度","tags":["def","der"],"brief":"速度的变化率，描述速度改变的快慢。",
 "body": wrap(
   defn("加速度",p("加速度是速度对时间的变化率：")+
   fml("\\mathbf{a} = \\lim_{\\Delta t\\to 0}\\frac{\\Delta\\mathbf{v}}{\\Delta t} = \\frac{d\\mathbf{v}}{dt} = \\frac{d^2\\mathbf{r}}{dt^2}"))+
   der(p("<strong>分量形式：</strong>")+
   fml("\\mathbf{a} = \\frac{dv_x}{dt}\\mathbf{i}+\\frac{dv_y}{dt}\\mathbf{j}+\\frac{dv_z}{dt}\\mathbf{k} = a_x\\mathbf{i}+a_y\\mathbf{j}+a_z\\mathbf{k}")+
   p("加速度的方向是速度矢量变化 $\\Delta\\mathbf{v}$ 的极限方向，<strong>不一定</strong>沿速度方向。"))
 )},
]},
# ---- 1.2 匀变速直线运动 ----
{
"name": "1.2 匀变速直线运动",
"color": "#2563eb",
"desc": "加速度恒定的一维运动方程推导",
"items": [
{"id":"c1s2-1","name":"匀变速直线运动公式","tags":["thm","der"],"brief":"由加速度定义积分推出三大运动学公式。",
 "body": wrap(
   thm("匀变速直线运动",p("若质点做直线运动且加速度 $a$ 恒定，初速度 $v_0$，初始位置 $x_0$，则：")+
   fml("v = v_0 + at")+fml("x = x_0 + v_0 t + \\tfrac{1}{2} a t^2")+fml("v^2 - v_0^2 = 2a(x-x_0)"))+
   der(p("<strong>推导（积分法）：</strong>由 $a=\\frac{dv}{dt}$，分离变量 $dv=a\\,dt$，从 $t=0$ 到 $t$ 积分：")+
   fml("\\int_{v_0}^{v} dv = a\\int_0^t dt \\implies v - v_0 = at \\implies v = v_0 + at")+
   p("再由 $v=\\frac{dx}{dt}=v_0+at$，积分得位置：")+
   fml("\\int_{x_0}^{x} dx = \\int_0^t (v_0+at)\\,dt \\implies x-x_0 = v_0 t + \\tfrac{1}{2}at^2")+
   p("<strong>消去 $t$ 得速度-位移关系：</strong>由 $t=\\frac{v-v_0}{a}$ 代入位移公式：")+
   fml("x-x_0 = v_0\\cdot\\frac{v-v_0}{a} + \\tfrac{1}{2}a\\left(\\frac{v-v_0}{a}\\right)^2 = \\frac{v_0(v-v_0)}{a} + \\frac{(v-v_0)^2}{2a}")+
   fml("= \\frac{2v_0(v-v_0)+(v-v_0)^2}{2a} = \\frac{v^2-v_0^2}{2a}")+
   p("整理即得 $v^2-v_0^2=2a(x-x_0)$。"))
 )},
]},
# ---- 1.3 抛体运动 ----
{
"name": "1.3 抛体运动",
"color": "#2563eb",
"desc": "斜抛运动的轨迹、射程与最大高度推导",
"items": [
{"id":"c1s3-1","name":"抛体运动方程与轨迹","tags":["thm","der"],"brief":"将运动分解为水平匀速与竖直匀变速。",
 "fig":"projectile","figCap":"斜抛运动的速度分解与轨迹",
 "body": wrap(
   thm("抛体运动",p("设初速度 $v_0$ 与水平方向成 $\\theta$ 角，忽略空气阻力，则：")+
   fml("x = v_0\\cos\\theta\\cdot t,\\quad y = v_0\\sin\\theta\\cdot t - \\tfrac{1}{2}gt^2")+
   fml("\\text{轨迹：}\\quad y = x\\tan\\theta - \\frac{g x^2}{2 v_0^2\\cos^2\\theta}"))+
   der(p("<strong>运动分解：</strong>水平方向 $a_x=0$（匀速），竖直方向 $a_y=-g$（匀变速）。")+
   p("初速度分量：$v_{0x}=v_0\\cos\\theta$，$v_{0y}=v_0\\sin\\theta$。")+
   fml("x(t) = v_0\\cos\\theta\\cdot t,\\qquad y(t) = v_0\\sin\\theta\\cdot t - \\tfrac{1}{2}gt^2")+
   p("<strong>轨迹方程：</strong>由第一式解出 $t=\\frac{x}{v_0\\cos\\theta}$，代入 $y(t)$：")+
   fml("y = v_0\\sin\\theta\\cdot\\frac{x}{v_0\\cos\\theta} - \\tfrac{1}{2}g\\left(\\frac{x}{v_0\\cos\\theta}\\right)^2 = x\\tan\\theta - \\frac{g x^2}{2v_0^2\\cos^2\\theta}")+
   p("此为抛物线方程，故抛体运动轨迹为抛物线。"))+
   der(p("<strong>射程 $R$：</strong>令 $y=0$，除 $x=0$ 外的解为：")+
   fml("0 = x\\tan\\theta - \\frac{g x^2}{2v_0^2\\cos^2\\theta} \\implies x = \\frac{2v_0^2\\cos^2\\theta\\tan\\theta}{g} = \\frac{v_0^2\\sin 2\\theta}{g}")+
   p("当 $\\theta=45°$ 时射程最大 $R_{\\max}=\\frac{v_0^2}{g}$。")+
   p("<strong>最大高度 $H$：</strong>竖直方向速度为零时 $v_y=v_0\\sin\\theta-gt=0$，$t=\\frac{v_0\\sin\\theta}{g}$，代入 $y(t)$：")+
   fml("H = v_0\\sin\\theta\\cdot\\frac{v_0\\sin\\theta}{g} - \\tfrac{1}{2}g\\left(\\frac{v_0\\sin\\theta}{g}\\right)^2 = \\frac{v_0^2\\sin^2\\theta}{2g}"))
 )},
]},
# ---- 1.4 圆周运动 ----
{
"name": "1.4 圆周运动",
"color": "#2563eb",
"desc": "角量描述、向心加速度、切向加速度",
"items": [
{"id":"c1s4-1","name":"圆周运动的加速度","tags":["thm","der"],"brief":"法向（向心）加速度与切向加速度的推导。",
 "fig":"circular","figCap":"圆周运动的速度与向心加速度",
 "body": wrap(
   defn("角量描述",p("角速度 $\\omega=\\frac{d\\theta}{dt}$，角加速度 $\\beta=\\frac{d\\omega}{dt}$。线量与角量关系：")+
   fml("v = r\\omega,\\quad a_t = r\\beta,\\quad a_n = r\\omega^2"))+
   thm("向心加速度",p("匀速圆周运动中，加速度大小为 $a_n=\\frac{v^2}{r}=\\omega^2 r$，方向指向圆心。"))+
   der(p("<strong>向心加速度推导（矢量法）：</strong>设质点做半径为 $r$ 的匀速圆周运动，$t$ 时刻速度 $\\mathbf{v}$，$t+\\Delta t$ 时刻速度 $\\mathbf{v}'$，二者大小均为 $v$，夹角为 $\\Delta\\theta$。")+
   p("速度变化量 $|\\Delta\\mathbf{v}|=2v\\sin\\frac{\\Delta\\theta}{2}\\approx v\\Delta\\theta$（小角度近似）。")+
   fml("a_n = \\lim_{\\Delta t\\to 0}\\frac{|\\Delta\\mathbf{v}|}{\\Delta t} = \\lim_{\\Delta t\\to 0}\\frac{v\\Delta\\theta}{\\Delta t} = v\\frac{d\\theta}{dt} = v\\omega = \\frac{v^2}{r}")+
   p("当 $\\Delta t\\to 0$ 时，$\\Delta\\mathbf{v}$ 的方向趋于垂直于 $\\mathbf{v}$ 并指向圆心，故 $\\mathbf{a}_n$ 指向圆心。")+
   p("<strong>变速圆周运动：</strong>速度大小也变化，存在切向加速度 $a_t=\\frac{dv}{dt}=r\\beta$（沿切线方向），总加速度：")+
   fml("\\mathbf{a} = \\mathbf{a}_t + \\mathbf{a}_n,\\quad a = \\sqrt{a_t^2+a_n^2}"))
 )},
]},
# ---- 1.5 相对运动 ----
{
"name": "1.5 相对运动",
"color": "#2563eb",
"desc": "伽利略变换下的速度与加速度合成",
"items": [
{"id":"c1s5-1","name":"伽利略速度变换","tags":["thm","der"],"brief":"低速运动参考系间的速度合成法则。",
 "body": wrap(
   thm("伽利略变换",p("设 $S'$ 系相对 $S$ 系以速度 $\\mathbf{u}$ 平动，则质点在两系中的位矢、速度、加速度满足：")+
   fml("\\mathbf{r} = \\mathbf{r}' + \\mathbf{u} t,\\quad \\mathbf{v} = \\mathbf{v}' + \\mathbf{u},\\quad \\mathbf{a} = \\mathbf{a}'"))+
   der(p("<strong>推导：</strong>对 $\\mathbf{r}=\\mathbf{r}'+\\mathbf{u}t$ 求时间导数（$\\mathbf{u}$ 为常矢量）：")+
   fml("\\frac{d\\mathbf{r}}{dt} = \\frac{d\\mathbf{r}'}{dt} + \\mathbf{u} \\implies \\mathbf{v} = \\mathbf{v}' + \\mathbf{u}")+
   p("再求导得加速度：$\\mathbf{a}=\\frac{d\\mathbf{v}}{dt}=\\frac{d\\mathbf{v}'}{dt}=\\mathbf{a}'$，故加速度在伽利略变换下不变——这是牛顿力学的基础。"))+
   note(p("伽利略变换仅适用于低速（$v\\ll c$）情形，高速时需用洛伦兹变换。"))
 )},
]},
]

# =====================================================
#  CHAPTER 2: 质点动力学
# =====================================================
ch2_sections = [
# ---- 2.1 牛顿三大定律 ----
{
"name": "2.1 牛顿三大定律",
"color": "#0d9488",
"desc": "牛顿运动定律的表述与惯性系",
"items": [
{"id":"c2s1-1","name":"牛顿运动定律","tags":["thm","note"],"brief":"经典力学的三大基本定律。",
 "fig":"fbd","figCap":"自由体受力分析示意",
 "body": wrap(
   defn("第一定律（惯性定律）",p("任何物体都保持静止或匀速直线运动状态，直到外力迫使它改变这种状态为止。")+
   p("数学表达：$\\mathbf{F}=0 \\implies \\mathbf{v}=$ 常矢量。"))+
   defn("第二定律",p("物体动量的变化率与所受合外力成正比，方向沿合外力方向：")+
   fml("\\mathbf{F} = \\frac{d\\mathbf{p}}{dt} = \\frac{d(m\\mathbf{v})}{dt}")+
   p("当质量 $m$ 为常量时，$\\mathbf{F}=m\\mathbf{a}$。"))+
   defn("第三定律（作用与反作用）",p("两个物体间的作用力 $\\mathbf{F}_{12}$ 与反作用力 $\\mathbf{F}_{21}$ 大小相等、方向相反、作用在同一直线上：")+
   fml("\\mathbf{F}_{12} = -\\mathbf{F}_{21}"))+
   note(p("<strong>惯性系：</strong>牛顿第一定律成立的参考系称为惯性系。一切相对惯性系做匀速直线运动的参考系都是惯性系。地球可近似为惯性系。"))+
   note(p("第二定律的原始形式 $\\mathbf{F}=\\frac{d\\mathbf{p}}{dt}$ 比 $\\mathbf{F}=m\\mathbf{a}$ 更普遍，后者仅在质量不变时成立。在相对论中质量随速度变化，但 $\\mathbf{F}=\\frac{d\\mathbf{p}}{dt}$ 仍成立。"))
 )},
]},
# ---- 2.2 常见力 ----
{
"name": "2.2 常见力的分析",
"color": "#0d9488",
"desc": "重力、弹力、摩擦力的规律与受力分析",
"items": [
{"id":"c2s2-1","name":"重力、弹力与摩擦力","tags":["def","exa"],"brief":"力学中三种最基本的力。",
 "fig":"inclined","figCap":"斜面上物体的受力分析",
 "body": wrap(
   defn("重力",p("地球对物体的万有引力（近似），方向竖直向下：$G=mg$，其中 $g\\approx 9.8\\,\\text{m/s}^2$。"))+
   defn("弹力（胡克定律）",p("弹簧在弹性限度内，弹力大小与形变量成正比，方向指向原长位置：")+
   fml("F = -kx")+
   p("负号表示弹力方向与位移方向相反。"))+
   defn("摩擦力",p("<strong>静摩擦力</strong>：$0\\le f_s \\le f_{s\\max}=\\mu_s N$，方向与相对运动趋势相反。<br><strong>滑动摩擦力</strong>：$f_k=\\mu_k N$，方向与相对运动方向相反。"))+
   exa(p("<strong>斜面物体：</strong>倾角 $\\theta$，重力分解为沿斜面分量 $mg\\sin\\theta$ 和垂直斜面分量 $mg\\cos\\theta$。法向力 $N=mg\\cos\\theta$。若物体匀速下滑，则 $\\mu_k=\\tan\\theta$。"))
 )},
]},
# ---- 2.3 动量与冲量 ----
{
"name": "2.3 动量与冲量",
"color": "#0d9488",
"desc": "动量定理与冲量的定义",
"items": [
{"id":"c2s3-1","name":"动量定理","tags":["thm","der"],"brief":"合外力的冲量等于动量的变化。",
 "body": wrap(
   defn("动量",p("质点的动量定义为质量与速度的乘积：$\\mathbf{p}=m\\mathbf{v}$，是矢量。"))+
   defn("冲量",p("力在时间上的积累称为冲量：")+
   fml("\\mathbf{I} = \\int_{t_1}^{t_2} \\mathbf{F}\\,dt"))+
   thm("动量定理",p("质点所受合外力的冲量等于其动量的变化量：")+
   fml("\\mathbf{I} = \\Delta\\mathbf{p} = \\mathbf{p}_2 - \\mathbf{p}_1"))+
   der(p("<strong>推导：</strong>由牛顿第二定律 $\\mathbf{F}=\\frac{d\\mathbf{p}}{dt}$，两边乘以 $dt$ 并从 $t_1$ 到 $t_2$ 积分：")+
   fml("\\int_{t_1}^{t_2} \\mathbf{F}\\,dt = \\int_{\\mathbf{p}_1}^{\\mathbf{p}_2} d\\mathbf{p} = \\mathbf{p}_2 - \\mathbf{p}_1 = \\Delta\\mathbf{p}"))+
   note(p("动量定理是矢量方程，可分解为分量形式：$I_x=\\Delta p_x$，$I_y=\\Delta p_y$，$I_z=\\Delta p_z$。"))
 )},
]},
# ---- 2.4 动量守恒定律 ----
{
"name": "2.4 动量守恒定律",
"color": "#0d9488",
"desc": "系统动量守恒的条件与推导",
"items": [
{"id":"c2s4-1","name":"动量守恒定律","tags":["thm","der"],"brief":"系统不受外力时总动量保持不变。",
 "fig":"collision","figCap":"两体碰撞示意",
 "body": wrap(
   thm("动量守恒定律",p("当系统所受合外力为零时，系统的总动量保持不变：")+
   fml("\\sum_{i} m_i \\mathbf{v}_i = \\text{常量}"))+
   der(p("<strong>推导（两体系统）：</strong>设两质点质量 $m_1,m_2$，相互作用力 $\\mathbf{F}_{12}$ 和 $\\mathbf{F}_{21}$，由牛顿第三定律 $\\mathbf{F}_{12}=-\\mathbf{F}_{21}$。")+
   p("对两质点分别应用牛顿第二定律：")+
   fml("\\mathbf{F}_{12} = \\frac{d\\mathbf{p}_1}{dt},\\qquad \\mathbf{F}_{21} = \\frac{d\\mathbf{p}_2}{dt}")+
   p("两式相加：")+
   fml("\\mathbf{F}_{12}+\\mathbf{F}_{21} = \\frac{d}{dt}(\\mathbf{p}_1+\\mathbf{p}_2)")+
   p("由牛顿第三定律，左边为零，故：")+
   fml("\\frac{d}{dt}(\\mathbf{p}_1+\\mathbf{p}_2)=0 \\implies \\mathbf{p}_1+\\mathbf{p}_2 = \\text{常量}")+
   p("推广到多质点系统，内力成对抵消，合外力为零时总动量守恒。"))
 )},
]},
# ---- 2.5 碰撞 ----
{
"name": "2.5 碰撞问题",
"color": "#0d9488",
"desc": "弹性碰撞、非弹性碰撞与恢复系数",
"items": [
{"id":"c2s5-1","name":"弹性碰撞与恢复系数","tags":["thm","der"],"brief":"碰撞过程的动量与能量分析。",
 "body": wrap(
   defn("恢复系数",p("碰撞后相对速度与碰撞前相对速度之比的负值：")+
   fml("e = \\frac{v_2'-v_1'}{v_1-v_2}")+
   p("$e=1$ 为完全弹性碰撞，$e=0$ 为完全非弹性碰撞，$0<e<1$ 为非弹性碰撞。"))+
   thm("一维弹性碰撞",p("动量守恒 + 动能守恒：")+
   fml("m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'")+
   fml("\\tfrac{1}{2}m_1 v_1^2 + \\tfrac{1}{2}m_2 v_2^2 = \\tfrac{1}{2}m_1 v_1'^2 + \\tfrac{1}{2}m_2 v_2'^2"))+
   der(p("<strong>弹性碰撞速度公式推导：</strong>由动量守恒和动能守恒：")+
   fml("m_1(v_1-v_1') = m_2(v_2'-v_2) \\quad (1)")+
   fml("m_1(v_1^2-v_1'^2) = m_2(v_2'^2-v_2^2) \\implies m_1(v_1-v_1')(v_1+v_1') = m_2(v_2'-v_2)(v_2'+v_2)")+
   p("将 (1) 代入，约去 $m_1(v_1-v_1')=m_2(v_2'-v_2)$（非零情形）：")+
   fml("v_1+v_1' = v_2+v_2' \\implies v_1-v_2 = v_2'-v_1'")+
   p("即弹性碰撞中恢复系数 $e=1$。联立动量守恒解得：")+
   fml("v_1' = \\frac{(m_1-m_2)v_1+2m_2 v_2}{m_1+m_2},\\qquad v_2' = \\frac{(m_2-m_1)v_2+2m_1 v_1}{m_1+m_2}")+
   p("<strong>特例</strong>：若 $m_1=m_2$，则 $v_1'=v_2$，$v_2'=v_1$（速度交换）；若 $m_2\\gg m_1$ 且 $v_2=0$，则 $v_1'\\approx -v_1$，$v_2'\\approx 0$。"))
 )},
]},
]

# =====================================================
#  CHAPTER 3: 功能关系
# =====================================================
ch3_sections = [
# ---- 3.1 功与功率 ----
{
"name": "3.1 功与功率",
"color": "#059669",
"desc": "功的定义、变力做功、功率",
"items": [
{"id":"c3s1-1","name":"功的定义","tags":["def","der"],"brief":"力对空间的积累效应。",
 "body": wrap(
   defn("恒力的功",p("恒力 $\\mathbf{F}$ 作用下质点发生位移 $\\Delta\\mathbf{r}$，力所做的功为：")+
   fml("W = \\mathbf{F}\\cdot\\Delta\\mathbf{r} = F|\\Delta\\mathbf{r}|\\cos\\theta"))+
   defn("变力的功",p("变力沿曲线做功为力沿路径的线积分：")+
   fml("W = \\int_{a}^{b} \\mathbf{F}\\cdot d\\mathbf{r} = \\int_{a}^{b} F\\cos\\theta\\,ds"))+
   der(p("<strong>分量形式（直角坐标）：</strong>")+
   fml("W = \\int_{x_1}^{x_2} F_x\\,dx + \\int_{y_1}^{y_2} F_y\\,dy + \\int_{z_1}^{z_2} F_z\\,dz"))+
   defn("功率",p("功率是单位时间内做的功：")+
   fml("P = \\frac{dW}{dt} = \\mathbf{F}\\cdot\\mathbf{v}"))
 )},
]},
# ---- 3.2 动能定理 ----
{
"name": "3.2 动能定理",
"color": "#059669",
"desc": "合外力做功等于动能变化的推导",
"items": [
{"id":"c3s2-1","name":"动能定理","tags":["thm","der"],"brief":"功是能量变化的量度。",
 "body": wrap(
   defn("动能",p("质点的动能：$E_k=\\frac{1}{2}mv^2$。"))+
   thm("动能定理",p("合外力对质点做的功等于质点动能的增量：")+
   fml("W_{\\text{合}} = \\Delta E_k = \\tfrac{1}{2}mv^2 - \\tfrac{1}{2}mv_0^2"))+
   der(p("<strong>推导：</strong>由牛顿第二定律 $\\mathbf{F}=m\\mathbf{a}=m\\frac{d\\mathbf{v}}{dt}$，合外力做功：")+
   fml("W = \\int \\mathbf{F}\\cdot d\\mathbf{r} = \\int m\\frac{d\\mathbf{v}}{dt}\\cdot d\\mathbf{r} = \\int m\\,d\\mathbf{v}\\cdot\\frac{d\\mathbf{r}}{dt} = \\int m\\mathbf{v}\\cdot d\\mathbf{v}")+
   p("利用 $\\mathbf{v}\\cdot d\\mathbf{v}=d\\left(\\tfrac{1}{2}v^2\\right)$（因为 $d(v^2)=d(\\mathbf{v}\\cdot\\mathbf{v})=2\\mathbf{v}\\cdot d\\mathbf{v}$）：")+
   fml("W = m\\int_{v_0}^{v} d\\left(\\tfrac{1}{2}v^2\\right) = \\tfrac{1}{2}mv^2 - \\tfrac{1}{2}mv_0^2 = \\Delta E_k"))+
   note(p("动能定理是标量方程，适用于惯性系。合外力做正功动能增加，做负功动能减少。"))
 )},
]},
# ---- 3.3 保守力与势能 ----
{
"name": "3.3 保守力与势能",
"color": "#059669",
"desc": "保守力的判据、势能的定义与计算",
"items": [
{"id":"c3s3-1","name":"保守力与势能","tags":["thm","der"],"brief":"做功与路径无关的力可以引入势能。",
 "body": wrap(
   defn("保守力",p("若力做功只与始末位置有关，与路径无关，则该力为<strong>保守力</strong>。等价判据：沿任意闭合路径做功为零，即 $\\oint\\mathbf{F}\\cdot d\\mathbf{r}=0$。"))+
   defn("势能",p("保守力做功等于势能的减少：")+
   fml("W_{\\text{保}} = E_{p1} - E_{p2} = -\\Delta E_p")+
   p("势能的定义式（取 $r_0$ 为势能零点）：")+
   fml("E_p(\\mathbf{r}) = -\\int_{\\mathbf{r}_0}^{\\mathbf{r}} \\mathbf{F}_{\\text{保}}\\cdot d\\mathbf{r}"))+
   der(p("<strong>重力势能：</strong>取地面 $y=0$ 为零点，重力 $\\mathbf{F}=-mg\\mathbf{j}$：")+
   fml("E_p = -\\int_0^h (-mg)\\,dy = mgh")+
   p("<strong>弹性势能：</strong>取原长 $x=0$ 为零点，弹力 $F=-kx$：")+
   fml("E_p = -\\int_0^x (-kx')\\,dx' = \\tfrac{1}{2}kx^2"))+
   thm("保守力与势能的关系",p("保守力等于势能的负梯度：")+
   fml("\\mathbf{F}_{\\text{保}} = -\\nabla E_p = -\\left(\\frac{\\partial E_p}{\\partial x}\\mathbf{i}+\\frac{\\partial E_p}{\\partial y}\\mathbf{j}+\\frac{\\partial E_p}{\\partial z}\\mathbf{k}\\right)"))
 )},
]},
# ---- 3.4 机械能守恒 ----
{
"name": "3.4 机械能守恒定律",
"color": "#059669",
"desc": "只有保守力做功时机械能守恒的推导",
"items": [
{"id":"c3s4-1","name":"机械能守恒定律","tags":["thm","der"],"brief":"动能与势能之和保持不变。",
 "body": wrap(
   thm("机械能守恒",p("当系统只有保守力做功时，系统的机械能（动能+势能）保持不变：")+
   fml("E = E_k + E_p = \\text{常量}"))+
   der(p("<strong>推导：</strong>将质点所受的力分为保守力 $\\mathbf{F}_{\\text{保}}$ 和非保守力 $\\mathbf{F}_{\\text{非保}}$。由动能定理：")+
   fml("W_{\\text{保}} + W_{\\text{非保}} = \\Delta E_k")+
   p("由保守力做功与势能的关系 $W_{\\text{保}}=-\\Delta E_p$，代入得：")+
   fml("-\\Delta E_p + W_{\\text{非保}} = \\Delta E_k \\implies W_{\\text{非保}} = \\Delta(E_k+E_p)")+
   p("若无非保守力做功（$W_{\\text{非保}}=0$），则 $\\Delta(E_k+E_p)=0$，即 $E_k+E_p=$ 常量。"))+
   note(p("机械能守恒的条件是<strong>只有保守力做功</strong>，而非不受外力。非保守力（如摩擦力）做功会导致机械能转化为其他形式能量（如热能）。"))
 )},
]},
# ---- 3.5 功能原理 ----
{
"name": "3.5 功能原理",
"color": "#059669",
"desc": "系统功能原理与能量转化",
"items": [
{"id":"c3s5-1","name":"系统的功能原理","tags":["thm","note"],"brief":"外力和非保守内力做功改变系统机械能。",
 "body": wrap(
   thm("功能原理",p("系统所受外力做功与非保守内力做功之和等于系统机械能的增量：")+
   fml("W_{\\text{外}} + W_{\\text{非保内}} = \\Delta E = \\Delta(E_k+E_p)"))+
   note(p("与质点动能定理的区别：功能原理将内力分为保守内力和非保守内力，保守内力做功已被势能变化吸收，不再出现在方程左边。")+
   p("若 $W_{\\text{外}}=0$ 且 $W_{\\text{非保内}}=0$，则机械能守恒。若有摩擦力等非保守内力做功，机械能减少，转化为热能等其他形式能量，这就是<strong>能量守恒定律</strong>的体现。"))
 )},
]},
]

# =====================================================
#  CHAPTER 4: 刚体动力学
# =====================================================
ch4_sections = [
# ---- 4.1 刚体的运动描述 ----
{
"name": "4.1 刚体的运动描述",
"color": "#0891b2",
"desc": "刚体的平动、转动与平面运动",
"items": [
{"id":"c4s1-1","name":"刚体的运动形式","tags":["def","note"],"brief":"刚体运动的基本类型与角量描述。",
 "fig":"rotation","figCap":"刚体绕定轴转动",
 "body": wrap(
   defn("刚体",p("在外力作用下形状和大小都保持不变的物体，即任意两质点间距离不变的质点系。"))+
   defn("平动与转动",p("<strong>平动</strong>：刚体上任意两点连线方向不变，各点运动状态相同，可简化为质点运动。<br><strong>定轴转动</strong>：刚体上各点都绕同一固定轴做圆周运动。"))+
   defn("角量",p("角位移 $\\Delta\\theta$，角速度 $\\omega=\\frac{d\\theta}{dt}$，角加速度 $\\beta=\\frac{d\\omega}{dt}$。"))+
   der(p("<strong>线量与角量关系：</strong>距转轴 $r$ 处质点的线速度、切向加速度、法向加速度：")+
   fml("v = r\\omega,\\quad a_t = r\\beta,\\quad a_n = r\\omega^2"))
 )},
]},
# ---- 4.2 转动惯量 ----
{
"name": "4.2 转动惯量",
"color": "#0891b2",
"desc": "转动惯量的定义、计算与平行轴定理",
"items": [
{"id":"c4s2-1","name":"转动惯量与平行轴定理","tags":["def","thm","der"],"brief":"刚体转动惯性的量度。",
 "body": wrap(
   defn("转动惯量",p("刚体对某轴的转动惯量为各质元质量到转轴距离平方的加权和：")+
   fml("I = \\sum_i m_i r_i^2 = \\int r^2\\,dm"))+
   thm("平行轴定理",p("设 $I_c$ 为刚体对通过质心的轴的转动惯量，$I$ 为对与该轴平行且相距 $d$ 的另一轴的转动惯量，则：")+
   fml("I = I_c + md^2"))+
   der(p("<strong>平行轴定理推导：</strong>设质心轴为 $z_c$，平行轴为 $z$，两轴间距 $d$。对质心系，质元位置 $\\mathbf{r}_i'$，质心系原点在质心，故 $\\sum m_i\\mathbf{r}_i'=0$。")+
   p("对 $z$ 轴，$r_i^2 = (x_i'+d)^2 + y_i'^2 = r_i'^2 + 2dx_i' + d^2$，则：")+
   fml("I = \\sum m_i r_i^2 = \\sum m_i r_i'^2 + 2d\\sum m_i x_i' + d^2\\sum m_i = I_c + 0 + md^2")+
   p("其中 $\\sum m_i x_i'=0$ 是因为质心系中质心在原点。"))+
   exa(p("<strong>常用转动惯量：</strong><br>细杆（过中心垂直轴）$I=\\frac{1}{12}mL^2$，（过端点）$I=\\frac{1}{3}mL^2$<br>圆盘（过中心垂直轴）$I=\\frac{1}{2}mR^2$<br>圆环（过中心垂直轴）$I=mR^2$<br>球体（过球心）$I=\\frac{2}{5}mR^2$"))
 )},
]},
# ---- 4.3 转动定律 ----
{
"name": "4.3 转动定律",
"color": "#0891b2",
"desc": "力矩、转动定律的推导",
"items": [
{"id":"c4s3-1","name":"力矩与转动定律","tags":["thm","der"],"brief":"刚体转动的牛顿第二定律。",
 "body": wrap(
   defn("力矩",p("力 $\\mathbf{F}$ 对转轴的力矩大小为 $M=rF\\sin\\theta$，矢量式：")+
   fml("\\mathbf{M} = \\mathbf{r}\\times\\mathbf{F}"))+
   thm("转动定律",p("刚体绕定轴转动时，合外力矩等于转动惯量乘以角加速度：")+
   fml("M = I\\beta"))+
   der(p("<strong>推导：</strong>将刚体视为质点系，第 $i$ 个质元受外力 $\\mathbf{F}_i$，切向分量 $F_{it}=m_i a_{it}=m_i r_i\\beta$。对转轴的力矩：")+
   fml("M_i = r_i F_{it} = m_i r_i^2 \\beta")+
   p("对所有质元求和，内力矩成对抵消（牛顿第三定律），仅外力矩贡献：")+
   fml("M_{\\text{合外}} = \\sum_i M_i = \\left(\\sum_i m_i r_i^2\\right)\\beta = I\\beta"))+
   note(p("转动定律 $M=I\\beta$ 与平动的牛顿第二定律 $F=ma$ 形式对应：力矩 $\\leftrightarrow$ 力，转动惯量 $\\leftrightarrow$ 质量，角加速度 $\\leftrightarrow$ 加速度。"))
 )},
]},
# ---- 4.4 角动量与守恒 ----
{
"name": "4.4 角动量与角动量守恒",
"color": "#0891b2",
"desc": "角动量定理与守恒定律",
"items": [
{"id":"c4s4-1","name":"角动量定理与守恒","tags":["thm","der"],"brief":"转动中的动量守恒对应物。",
 "body": wrap(
   defn("角动量",p("质点对转轴的角动量 $L=mrv$（垂直情形）。刚体绕定轴转动的角动量：")+
   fml("L = I\\omega"))+
   thm("角动量定理",p("合外力矩的冲量矩等于角动量的变化：")+
   fml("\\int_{t_1}^{t_2} M\\,dt = \\Delta L = I\\omega_2 - I\\omega_1"))+
   der(p("<strong>角动量定理推导：</strong>由转动定律 $M=I\\beta=I\\frac{d\\omega}{dt}=\\frac{d(I\\omega)}{dt}=\\frac{dL}{dt}$，积分得：")+
   fml("\\int M\\,dt = \\int dL = \\Delta L"))+
   thm("角动量守恒定律",p("当系统所受合外力矩为零时，系统角动量守恒：")+
   fml("L = I\\omega = \\text{常量}"))+
   der(p("<strong>角动量守恒推导：</strong>由 $M=\\frac{dL}{dt}$，若 $M=0$，则 $\\frac{dL}{dt}=0$，即 $L=$ 常量。")+
   p("注意：角动量守恒时 $I$ 和 $\\omega$ 可以各自变化，但乘积不变。例如花样滑冰运动员收回手臂时 $I$ 减小，$\\omega$ 增大。"))
 )},
]},
# ---- 4.5 刚体的平衡 ----
{
"name": "4.5 刚体的平衡",
"color": "#0891b2",
"desc": "刚体平衡的条件与稳定性",
"items": [
{"id":"c4s5-1","name":"刚体的平衡条件","tags":["thm","note"],"brief":"合力为零且合力矩为零。",
 "body": wrap(
   thm("刚体平衡条件",p("刚体处于平衡状态（静止或匀速直线运动 + 匀速转动）的充要条件：")+
   fml("\\sum \\mathbf{F}_i = 0,\\qquad \\sum \\mathbf{M}_i = 0")+
   p("即合外力为零，对任意转轴的合外力矩为零。"))+
   note(p("对平面力系，平衡条件为三个标量方程：")+
   fml("\\sum F_x=0,\\quad \\sum F_y=0,\\quad \\sum M_O=0")+
   p("其中 $O$ 为任意选定的矩心。求解时可灵活选取矩心以简化计算。"))
 )},
]},
]

# =====================================================
#  CHAPTER 5: 简谐振动与机械波
# =====================================================
ch5_sections = [
# ---- 5.1 简谐振动 ----
{
"name": "5.1 简谐振动",
"color": "#be185d",
"desc": "简谐振动的微分方程、解与能量",
"items": [
{"id":"c5s1-1","name":"简谐振动的运动方程","tags":["thm","der"],"brief":"弹簧振子的运动规律推导。",
 "fig":"shm","figCap":"简谐振动的位移-时间曲线",
 "body": wrap(
   defn("简谐振动",p("物体所受回复力与位移成正比且方向相反时的运动：$F=-kx$。"))+
   thm("简谐振动方程",p("简谐振动的位移随时间变化为：")+
   fml("x = A\\cos(\\omega t + \\varphi)")+
   p("其中 $A$ 为振幅，$\\omega$ 为角频率，$\\varphi$ 为初相位。"))+
   der(p("<strong>微分方程推导：</strong>弹簧振子受回复力 $F=-kx$，由牛顿第二定律：")+
   fml("m\\frac{d^2x}{dt^2} = -kx \\implies \\frac{d^2x}{dt^2} + \\omega^2 x = 0,\\quad \\omega^2=\\frac{k}{m}")+
   p("这是二阶常系数线性齐次微分方程，特征方程 $r^2+\\omega^2=0$，根 $r=\\pm i\\omega$，通解为：")+
   fml("x = C_1\\cos\\omega t + C_2\\sin\\omega t = A\\cos(\\omega t+\\varphi)")+
   p("其中 $A=\\sqrt{C_1^2+C_2^2}$，$\\tan\\varphi=-\\frac{C_2}{C_1}$。初始条件 $x(0)=x_0$，$v(0)=v_0$ 确定 $A$ 和 $\\varphi$：")+
   fml("A=\\sqrt{x_0^2+\\left(\\frac{v_0}{\\omega}\\right)^2},\\quad \\tan\\varphi=-\\frac{v_0}{\\omega x_0}"))+
   der(p("<strong>能量分析：</strong>动能 $E_k=\\frac{1}{2}mv^2$，势能 $E_p=\\frac{1}{2}kx^2$，总机械能：")+
   fml("E = E_k+E_p = \\tfrac{1}{2}m\\omega^2 A^2\\sin^2(\\omega t+\\varphi) + \\tfrac{1}{2}kA^2\\cos^2(\\omega t+\\varphi)")+
   p("利用 $\\omega^2=k/m$，即 $m\\omega^2=k$：")+
   fml("E = \\tfrac{1}{2}kA^2[\\sin^2(\\omega t+\\varphi)+\\cos^2(\\omega t+\\varphi)] = \\tfrac{1}{2}kA^2 = \\text{常量}")+
   p("简谐振动中机械能守恒，动能与势能相互转化。"))
 )},
]},
# ---- 5.2 单摆与复摆 ----
{
"name": "5.2 单摆与复摆",
"color": "#be185d",
"desc": "单摆、复摆的周期公式推导",
"items": [
{"id":"c5s2-1","name":"单摆与复摆周期","tags":["thm","der"],"brief":"小角度近似下的摆动周期。",
 "fig":"pendulum","figCap":"单摆的受力分析",
 "body": wrap(
   thm("单摆周期",p("小角度（$\\theta\\ll 1$ rad）下，单摆周期为：")+
   fml("T = 2\\pi\\sqrt{\\frac{L}{g}}"))+
   der(p("<strong>单摆推导：</strong>摆球受重力和拉力，切向合力 $F_t=-mg\\sin\\theta$。由牛顿第二定律切向分量 $ma_t=-mg\\sin\\theta$，而 $a_t=L\\beta=L\\frac{d^2\\theta}{dt^2}$：")+
   fml("mL\\frac{d^2\\theta}{dt^2} = -mg\\sin\\theta \\implies \\frac{d^2\\theta}{dt^2}+\\frac{g}{L}\\sin\\theta=0")+
   p("小角度时 $\\sin\\theta\\approx\\theta$，化为简谐振动方程 $\\frac{d^2\\theta}{dt^2}+\\omega^2\\theta=0$，其中 $\\omega=\\sqrt{g/L}$，故：")+
   fml("T = \\frac{2\\pi}{\\omega} = 2\\pi\\sqrt{\\frac{L}{g}}"))+
   thm("复摆周期",p("绕水平轴摆动的刚体（复摆），小角度下周期：")+
   fml("T = 2\\pi\\sqrt{\\frac{I}{mgd}}")+
   p("其中 $I$ 为对转轴的转动惯量，$d$ 为质心到转轴距离。"))+
   der(p("<strong>复摆推导：</strong>由转动定律 $M=I\\beta$，重力矩 $M=-mgd\\sin\\theta\\approx -mgd\\theta$：")+
   fml("I\\frac{d^2\\theta}{dt^2} = -mgd\\theta \\implies \\frac{d^2\\theta}{dt^2}+\\frac{mgd}{I}\\theta=0")+
   p("故 $\\omega=\\sqrt{mgd/I}$，$T=2\\pi\\sqrt{I/(mgd)}$。"))
 )},
]},
# ---- 5.3 阻尼与受迫振动 ----
{
"name": "5.3 阻尼振动与受迫振动",
"color": "#be185d",
"desc": "阻尼振动、受迫振动与共振",
"items": [
{"id":"c5s3-1","name":"阻尼振动与共振","tags":["thm","note"],"brief":"阻尼对振动的影响与共振现象。",
 "body": wrap(
   defn("阻尼振动",p("存在粘滞阻力 $f=-\\gamma v$ 时，运动方程为：")+
   fml("m\\frac{d^2x}{dt^2}+\\gamma\\frac{dx}{dt}+kx=0")+
   p("令 $\\beta=\\frac{\\gamma}{2m}$（阻尼因子），$\\omega_0=\\sqrt{k/m}$（固有频率），当 $\\beta<\\omega_0$（欠阻尼）时解为：")+
   fml("x = A_0 e^{-\\beta t}\\cos(\\omega t+\\varphi),\\quad \\omega=\\sqrt{\\omega_0^2-\\beta^2}"))+
   thm("受迫振动与共振",p("受周期性外力 $F=F_0\\cos\\omega_d t$ 作用时，稳态解为同频率简谐振动，振幅为：")+
   fml("A = \\frac{F_0/m}{\\sqrt{(\\omega_0^2-\\omega_d^2)^2+(2\\beta\\omega_d)^2}}")+
   p("当 $\\omega_d=\\sqrt{\\omega_0^2-2\\beta^2}$ 时振幅最大，发生<strong>共振</strong>。"))+
   note(p("共振在工程中既有应用（如乐器共鸣、核磁共振），也需避免（如桥梁共振、建筑抗震）。阻尼越小，共振峰越尖锐。"))
 )},
]},
# ---- 5.4 机械波 ----
{
"name": "5.4 机械波的描述",
"color": "#be185d",
"desc": "波的产生、描述与波方程",
"items": [
{"id":"c5s4-1","name":"机械波与波动方程","tags":["def","thm","der"],"brief":"振动的传播形成波。",
 "fig":"wave","figCap":"简谐波的波形与波长、振幅",
 "body": wrap(
   defn("机械波",p("机械振动在介质中的传播形成机械波。波传播的是振动状态和能量，介质本身不随波迁移。"))+
   defn("波的特征量",p("波长 $\\lambda$、周期 $T$、频率 $f$、波速 $v$ 满足：$v=\\lambda f=\\lambda/T$。"))+
   thm("简谐波方程",p("沿 $x$ 正方向传播的平面简谐波：")+
   fml("y(x,t) = A\\cos\\left[\\omega\\left(t-\\frac{x}{v}\\right)+\\varphi\\right]")+
   p("等价形式：$y=A\\cos(\\omega t-kx+\\varphi)$，其中 $k=\\frac{2\\pi}{\\lambda}$ 为波数。"))+
   der(p("<strong>波动方程推导：</strong>考虑沿绳传播的横波，取线元 $\\Delta x$，两端张力 $T$ 的横向分量差提供恢复力。由牛顿第二定律：")+
   fml("T\\left(\\left.\\frac{\\partial y}{\\partial x}\\right|_{x+\\Delta x}-\\left.\\frac{\\partial y}{\\partial x}\\right|_x\\right) = \\mu\\Delta x\\frac{\\partial^2 y}{\\partial t^2}")+
   p("其中 $\\mu$ 为线密度。左边除以 $\\Delta x$ 取极限得 $T\\frac{\\partial^2 y}{\\partial x^2}$：")+
   fml("\\frac{\\partial^2 y}{\\partial t^2} = \\frac{T}{\\mu}\\frac{\\partial^2 y}{\\partial x^2} = v^2\\frac{\\partial^2 y}{\\partial x^2},\\quad v=\\sqrt{\\frac{T}{\\mu}}")+
   p("这是一维波动方程，简谐波 $y=A\\cos(\\omega t-kx)$ 是其解，代入可验证 $v=\\omega/k$。"))
 )},
]},
# ---- 5.5 波的干涉与驻波 ----
{
"name": "5.5 波的叠加、干涉与驻波",
"color": "#be185d",
"desc": "波的叠加原理、干涉条件、驻波",
"items": [
{"id":"c5s5-1","name":"波的干涉与驻波","tags":["thm","der"],"brief":"两列波叠加产生干涉和驻波。",
 "body": wrap(
   thm("波的叠加原理",p("几列波在同一介质中传播时，各自保持原有特性独立传播；在相遇区域，任一质点的位移为各列波单独引起位移的矢量和。"))+
   thm("干涉条件",p("两列波频率相同、振动方向相同、相位差恒定，叠加后产生稳定的干涉图样。"))+
   der(p("<strong>干涉极值条件：</strong>两列波 $y_1=A_1\\cos(\\omega t-kr_1+\\varphi_1)$，$y_2=A_2\\cos(\\omega t-kr_2+\\varphi_2)$ 叠加，相位差 $\\Delta\\varphi=(\\varphi_2-\\varphi_1)-k(r_2-r_1)$。")+
   p("当 $\\Delta\\varphi=2n\\pi$ 时，合振幅最大 $A=A_1+A_2$（加强）；当 $\\Delta\\varphi=(2n+1)\\pi$ 时，合振幅最小 $A=|A_1-A_2|$（减弱）。")+
   fml("\\Delta r = r_2-r_1 = n\\lambda \\quad(\\text{加强}),\\qquad \\Delta r = (n+\\tfrac{1}{2})\\lambda \\quad(\\text{减弱})"))+
   thm("驻波",p("两列振幅相同、沿相反方向传播的相干波叠加形成驻波：")+
   fml("y = 2A\\cos\\frac{2\\pi x}{\\lambda}\\cos\\omega t"))+
   der(p("<strong>驻波推导：</strong>$y_1=A\\cos(\\omega t-kx)$，$y_2=A\\cos(\\omega t+kx)$，叠加：")+
   fml("y = A[\\cos(\\omega t-kx)+\\cos(\\omega t+kx)] = 2A\\cos(kx)\\cos(\\omega t)")+
   p("其中 $k=2\\pi/\\lambda$。当 $\\cos\\frac{2\\pi x}{\\lambda}=0$ 时 $y=0$（波节）；当 $|\\cos\\frac{2\\pi x}{\\lambda}|=1$ 时振幅最大（波腹）。波节间距 $\\lambda/2$。"))
 )},
]},
]

# ---------- CHAPTERS ----------
CHAPTERS = [
    {"id":"m-ch1","num":"第一章","title":"质点运动学","en":"KINEMATICS",
     "desc":"位置、速度、加速度的矢量描述，匀变速直线运动公式，抛体运动轨迹，圆周运动的向心加速度，以及伽利略变换下的相对运动。",
     "sections": ch1_sections},
    {"id":"m-ch2","num":"第二章","title":"质点动力学","en":"DYNAMICS",
     "desc":"牛顿三大定律与惯性系，重力、弹力、摩擦力的分析，动量与冲量，动量守恒定律的推导，以及弹性碰撞与恢复系数。",
     "sections": ch2_sections},
    {"id":"m-ch3","num":"第三章","title":"功能关系","en":"WORK & ENERGY",
     "desc":"功与功率的定义，动能定理的推导，保守力与势能（重力势能、弹性势能），机械能守恒定律，以及系统的功能原理。",
     "sections": ch3_sections},
    {"id":"m-ch4","num":"第四章","title":"刚体动力学","en":"RIGID BODY",
     "desc":"刚体的平动与转动，转动惯量与平行轴定理，转动定律（力矩=转动惯量×角加速度），角动量定理与角动量守恒，刚体平衡条件。",
     "sections": ch4_sections},
    {"id":"m-ch5","num":"第五章","title":"简谐振动与机械波","en":"OSCILLATIONS & WAVES",
     "desc":"简谐振动的微分方程与解，单摆与复摆周期，阻尼振动与受迫振动共振，机械波的波动方程，波的干涉与驻波。",
     "sections": ch5_sections},
]

total_items = sum(sum(len(s["items"]) for s in ch["sections"]) for ch in CHAPTERS)
print(f"Total items: {total_items}")

def gen_html():
    data_lines = []
    for ch in CHAPTERS:
        sec_strs = []
        for sec in ch["sections"]:
            item_strs = []
            for it in sec["items"]:
                tags_js = json.dumps(it["tags"], ensure_ascii=False)
                body_esc = js_escape(it["body"])
                fig_field = f",fig:{json.dumps(it.get('fig',''),ensure_ascii=False)}" if it.get("fig") else ""
                figcap_field = f",figCap:{json.dumps(it.get('figCap',''),ensure_ascii=False)}" if it.get("figCap") else ""
                item_strs.append(
                    f"{{id:'{it['id']}',name:{json.dumps(it['name'],ensure_ascii=False)},"
                    f"tags:{tags_js},brief:{json.dumps(it['brief'],ensure_ascii=False)},"
                    f"body:`{body_esc}`{fig_field}{figcap_field}}}"
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

    fig_entries = []
    for k, v in FIG.items():
        fig_entries.append(f"{json.dumps(k)}:`{js_escape(v)}`")
    fig_js = "{" + ",".join(fig_entries) + "}"
    tag_label_js = json.dumps(TAG_LABEL, ensure_ascii=False)

    nav_tabs = "".join(
        f'<a class="la-nav-tab c{i+1}" href="#{ch["id"]}">{ch["num"]} · {ch["title"]}</a>'
        for i, ch in enumerate(CHAPTERS)
    )

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
  .la-nav-tab.c4{color:#0e7490;border-color:#a5f3fc}
  .la-nav-tab.c5{color:#be185d;border-color:#fbcfe8}
  .la-engagement-bar{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:26px 0 10px}
  .la-stat-item{display:inline-flex;align-items:center;gap:8px;padding:8px 16px;border-radius:999px;background:#fff;border:1px solid #e2e8f0;font-size:13px;color:#334155;font-weight:600}
  .la-stat-value{color:#6366f1;font-weight:800;font-size:15px}
  .la-stat-link{cursor:pointer;text-decoration:none;transition:.2s}
  .la-stat-link:hover{background:#eef2ff;border-color:#c7d2fe}
  .la-legend{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:0 0 24px;font-size:12px;color:#64748b}
  .la-legend-title{font-weight:700;margin-right:4px}
  .la-arc-badge{font-size:11px;padding:3px 10px;border-radius:999px;font-weight:700;letter-spacing:.04em}
  .la-arc-def{background:#dbeafe;color:#1e40af}
  .la-arc-thm{background:#ede9fe;color:#6d28d9}
  .la-arc-der{background:#e0f2fe;color:#0369a1}
  .la-arc-exa{background:#dcfce7;color:#15803d}
  .la-arc-app{background:#fef3c7;color:#b45309}
  .la-arc-note{background:#fee2e2;color:#b91c1c}
  .la-roadmap{padding:30px 0}
  .la-phase-title{font-size:24px;color:#1e293b;margin:40px 0 6px 18px;display:flex;align-items:center;gap:12px}
  .la-phase-title::before{content:"";width:6px;height:26px;border-radius:4px}
  .la-phase-title.m-ch1::before{background:#2563eb}
  .la-phase-title.m-ch2::before{background:#0d9488}
  .la-phase-title.m-ch3::before{background:#059669}
  .la-phase-title.m-ch4::before{background:#0891b2}
  .la-phase-title.m-ch5::before{background:#be185d}
  .la-phase-en{font-size:11px;letter-spacing:.36em;color:#94a3b8;font-weight:700;text-transform:uppercase;margin:0 0 12px 18px;font-style:italic}
  .la-phase-desc{color:var(--la-muted);font-size:14px;margin:0 0 24px 18px;line-height:1.8;max-width:960px}
  .la-domain{margin-bottom:26px;padding:16px 18px 18px 22px;position:relative;background:rgba(255,255,255,.6);border-radius:18px;border:1px solid #e5ebf2}
  .la-domain::before{content:"";position:absolute;left:6px;top:16px;bottom:16px;width:5px;border-radius:5px;background:var(--domain-color,#2563eb);box-shadow:0 0 12px rgba(37,99,235,.25)}
  .la-domain-header{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}
  .la-domain-header h3{margin:0;font-size:17px;color:#1e293b}
  .la-domain-count{font-size:11px;padding:2px 10px;border-radius:999px;background:#eef2ff;color:#4f46e5;font-weight:700}
  .la-domain-desc{font-size:12px;color:#94a3b8}
  .la-domain-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
  .la-course-card{background:#fff;border:1px solid #e5ebf2;border-radius:14px;padding:14px 16px;cursor:pointer;transition:.22s;box-shadow:var(--la-shadow)}
  .la-course-card:hover{transform:translateY(-3px);border-color:#c7d2fe;box-shadow:0 16px 40px rgba(37,99,235,.12)}
  .la-course-card h4{margin:6px 0;font-size:15px;color:#1e293b}
  .la-course-card p{margin:4px 0 0;font-size:12.5px;color:#64748b;line-height:1.6}
  .la-arc-badges{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:2px}
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
  .la-fml{margin:16px 0;padding:14px 18px;background:linear-gradient(135deg,#f8fafc,#eef4fb);border-left:4px solid #93b4e8;border-radius:10px;overflow-x:auto;font-size:16px;color:#0f172a}
  .la-fml .note{display:block;font-size:12.5px;color:#8496ad;margin-top:8px;line-height:1.6;font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
  .la-fml mjx-container[display="true"]{margin:0 !important}
  mjx-container, mjx-container *{color:#0f172a !important;opacity:1 !important}
  mjx-mi{font-style:italic !important}
  mjx-mo{color:#0f172a !important}
  .la-modal-body mjx-container, .la-modal-body mjx-container *{color:#0f172a !important;opacity:1 !important}
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
  .la-kp-sec p:last-child{margin-bottom:0}
  .la-modal-close{margin-top:22px;background:#0f172a;color:white;border-color:#0f172a;padding:10px 20px;font-weight:bold}
  .la-footer{padding:34px 0 50px;color:var(--la-muted);text-align:center;font-size:13px;line-height:1.9}
  .la-core-fmls{margin:40px 0 20px;padding:28px 24px;background:linear-gradient(135deg,#f0f4ff,#faf7ff);border:1px solid #e0e7ff;border-radius:18px}
  .la-core-fmls h3{font-size:18px;color:#1e293b;margin:0 0 20px;text-align:center;letter-spacing:.04em}
  .la-core-fmls h3 .la-core-count{display:inline-block;background:#6366f1;color:#fff;font-size:13px;padding:2px 10px;border-radius:20px;margin-left:8px;vertical-align:middle}
  .la-core-item{display:flex;gap:12px;margin:0 0 14px;padding:12px 16px;background:#fff;border-radius:12px;border-left:3px solid #6366f1;align-items:flex-start}
  .la-core-num{flex-shrink:0;width:26px;height:26px;border-radius:50%;background:#6366f1;color:#fff;font-size:13px;display:flex;align-items:center;justify-content:center;font-weight:bold}
  .la-core-body{flex:1;min-width:0}
  .la-core-body .la-core-name{font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px}
  .la-core-body .la-fml{margin:6px 0 0;padding:8px 14px;font-size:15px}
  .la-back-top{display:inline-block;margin-top:20px;padding:10px 28px;background:#1e293b;color:#fff;border:none;border-radius:25px;font-size:14px;cursor:pointer;letter-spacing:.04em;transition:background .2s}
  .la-back-top:hover{background:#334155}
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
  document.getElementById('laKCount').textContent = kCount;
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
<meta name="description" content="力学知识体系：质点运动学、质点动力学、功能关系、刚体动力学、简谐振动与机械波">
<title>力学 · 知识体系</title>
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
    <div class="la-eyebrow">NEWTONIAN MECHANICS · KNOWLEDGE MAP</div>
    <h1>力学 · 知识体系</h1>
    <p class="la-subtitle">质点运动学 · 质点动力学 · 功能关系 · 刚体动力学 · 简谐振动与机械波</p>
    <div class="back-bar"><a class="back-btn" href="index.html">← 返回总览</a></div>
    <div class="la-nav-tabs">{nav_tabs}</div>
    <div class="la-engagement-bar">
      <div class="la-stat-item"><span>📘</span><span class="la-stat-value" id="laKCount">--</span><span>个知识点</span></div>
      <a class="la-stat-item la-stat-link" href="#laCoreFmls" onclick="event.preventDefault();document.getElementById('laCoreFmls').scrollIntoView({{behavior:'smooth',block:'start'}})"><span>🧮</span><span class="la-stat-value">{len(CORE_FORMULAS)}</span><span>条核心公式 · 点击速查</span></a>
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
  <section class="la-core-fmls" id="laCoreFmls">
    <h3>核心公式速查 <span class="la-core-count">{len(CORE_FORMULAS)} 条</span></h3>
{chr(10).join(f'    <div class="la-core-item"><div class="la-core-num">{i+1}</div><div class="la-core-body"><div class="la-core-name">{name}</div><div class="la-fml">$${latex}$$</div><div class="note" style="font-size:12px;color:#8496ad;margin-top:4px">{desc}</div></div></div>' for i,(name,latex,desc) in enumerate(CORE_FORMULAS))}
  </section>
  <footer class="la-footer">
    <div>力学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于经典力学核心知识体系整理</div>
    <button class="la-back-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑ 回到顶部</button>
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
    with open("/workspace/newtonian-mechanics.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated newtonian-mechanics.html ({len(html)} chars)")
