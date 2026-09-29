# -*- coding: utf-8 -*-
"""全部学科的知识内容数据。由 gen.py 渲染为 HTML。"""
from gen import write_subject

def item(id, name, tags, brief, body, fig=None, figCap=None):
    d = {"id": id, "name": name, "tags": tags, "brief": brief, "body": body}
    if fig: d["fig"] = fig
    if figCap: d["figCap"] = figCap
    return d

SUBJECTS = []

# ============================================================
# 1. 初等数学 elementary-math
# ============================================================
SUBJECTS.append({
  "filename":"elementary-math.html",
  "title":"初等数学",
  "eyebrow":"ELEMENTARY MATHEMATICS",
  "subtitle":"反三角函数 · 极坐标 · 向量叉乘 · 数列 · 不等式 · 解析几何",
  "meta_desc":"初等数学知识体系：反三角函数、极坐标、向量、数列、不等式、解析几何",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"三角函数与反三角","en":"TRIGONOMETRY","sub":"角度与弧度、三角恒等式","desc":"三角函数是初等数学的核心工具。本章复习角度制与弧度制、基本恒等式、和差化积与反三角函数。","sections":[
      {"name":"1.1 角度与弧度","color":"#2563eb","desc":"两种度量方式的换算","items":[
        item("la-k1-1","弧度制",["def","exa"],"$180^\\circ = \\pi$ 弧度，弧长 $l=r\\theta$。","<p><strong>定义</strong>　在半径为 $r$ 的圆中，弧长等于半径的圆心角为 1 弧度（rad）。</p><div class=\"la-fml\">$$\\theta(\\text{rad}) = \\frac{\\pi}{180^\\circ}\\theta(^\\circ)$$</div><p>常见换算：$30^\\circ=\\pi/6$，$45^\\circ=\\pi/4$，$60^\\circ=\\pi/3$，$90^\\circ=\\pi/2$。</p>"),
        item("la-k1-2","基本恒等式",["thm"],"$\\sin^2\\theta+\\cos^2\\theta=1$，商数与倒数关系。","<p><strong>定理</strong>　对任意角 $\\theta$：</p><div class=\"la-fml\">$$\\sin^2\\theta+\\cos^2\\theta=1,\\quad \\tan\\theta=\\frac{\\sin\\theta}{\\cos\\theta},\\quad \\cot\\theta=\\frac{\\cos\\theta}{\\sin\\theta}$$</div>"),
      ]},
      {"name":"1.2 和差角与倍角","color":"#7c3aed","desc":"三角恒等变换的核心公式","items":[
        item("la-k1-3","和差角公式",["thm","der"],"$\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta$。","<p><strong>推导</strong>　利用单位圆上两点距离可证：</p><div class=\"la-fml\">$$\\cos(\\alpha-\\beta)=\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta$$</div><p>由此推出和差角正弦、余弦、正切公式。</p>"),
        item("la-k1-4","二倍角与半角",["thm"],"$\\sin2\\theta=2\\sin\\theta\\cos\\theta$，$\\cos2\\theta=\\cos^2\\theta-\\sin^2\\theta$。","<p>令 $\\alpha=\\beta=\\theta$ 即得二倍角公式。半角公式：</p><div class=\"la-fml\">$$\\sin\\frac{\\theta}{2}=\\pm\\sqrt{\\frac{1-\\cos\\theta}{2}},\\quad \\cos\\frac{\\theta}{2}=\\pm\\sqrt{\\frac{1+\\cos\\theta}{2}}$$</div>"),
      ]},
      {"name":"1.3 反三角函数","color":"#0f766e","desc":"三角方程的解与主值","items":[
        item("la-k1-5","反正弦与反余弦",["def"],"$\\arcsin x\\in[-\\pi/2,\\pi/2]$，$\\arccos x\\in[0,\\pi]$。","<p><strong>定义</strong>　$y=\\arcsin x$ 是 $y=\\sin x$ 在 $[-\\pi/2,\\pi/2]$ 上的反函数；$y=\\arccos x$ 是 $y=\\cos x$ 在 $[0,\\pi]$ 上的反函数。</p><div class=\"la-fml\">$$\\arcsin x+\\arccos x=\\frac{\\pi}{2}\\quad(|x|\\le 1)$$</div>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"向量与极坐标","en":"VECTORS & POLAR","sub":"向量运算、坐标系转换","desc":"向量是描述物理量的基本语言。本章复习向量的加减、点积、叉乘，以及极坐标与直角坐标的换算。","sections":[
      {"name":"2.1 向量代数","color":"#2563eb","desc":"线性运算、点积、叉乘","items":[
        item("la-k2-1","向量的线性运算",["def","exa"],"加法满足平行四边形法则，数乘缩放长度。","<p><strong>定义</strong>　向量 $\\boldsymbol{a}=(a_1,a_2,a_3)$，数乘 $\\lambda\\boldsymbol{a}=(\\lambda a_1,\\lambda a_2,\\lambda a_3)$。</p><div class=\"la-fml\">$$|\\lambda\\boldsymbol{a}|=|\\lambda|\\,|\\boldsymbol{a}|$$</div>"),
        item("la-k2-2","点积与叉乘",["def","thm"],"$\\boldsymbol{a}\\cdot\\boldsymbol{b}=|a||b|\\cos\\theta$，叉乘垂直于两向量。","<p><strong>点积</strong>：$\\boldsymbol{a}\\cdot\\boldsymbol{b}=a_1b_1+a_2b_2+a_3b_3$，结果为标量。</p><p><strong>叉乘</strong>：$\\boldsymbol{a}\\times\\boldsymbol{b}=(a_2b_3-a_3b_2,\\,a_3b_1-a_1b_3,\\,a_1b_2-a_2b_1)$，方向由右手定则确定。</p><div class=\"la-fml\">$$|\\boldsymbol{a}\\times\\boldsymbol{b}|=|a||b|\\sin\\theta$$</div>"),
      ]},
      {"name":"2.2 极坐标","color":"#7c3aed","desc":"平面点的另一种表示","items":[
        item("la-k2-3","极坐标与直角坐标",["def","exa"],"$x=r\\cos\\theta$，$y=r\\sin\\theta$。","<p>极坐标用 $(r,\\theta)$ 表示平面点，与直角坐标互换：</p><div class=\"la-fml\">$$r=\\sqrt{x^2+y^2},\\quad \\theta=\\arctan\\frac{y}{x}$$</div>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"数列与不等式","en":"SEQUENCES & INEQUALITIES","sub":"等差等比数列、均值不等式","desc":"数列是函数的离散形式，不等式是估计与证明的工具。","sections":[
      {"name":"3.1 数列","color":"#0f766e","desc":"等差、等比与求和","items":[
        item("la-k3-1","等差数列",["def","thm"],"$a_n=a_1+(n-1)d$，$S_n=\\frac{n(a_1+a_n)}{2}$。","<p>公差为 $d$ 的等差数列，通项与前 $n$ 项和：</p><div class=\"la-fml\">$$a_n=a_1+(n-1)d,\\quad S_n=na_1+\\frac{n(n-1)}{2}d$$</div>"),
        item("la-k3-2","等比数列",["def","thm"],"$a_n=a_1q^{n-1}$，$S_n=a_1\\frac{1-q^n}{1-q}$。","<p>公比为 $q$ 的等比数列。当 $|q|<1$ 时无穷级数收敛：</p><div class=\"la-fml\">$$S=\\lim_{n\\to\\infty}S_n=\\frac{a_1}{1-q}$$</div>"),
      ]},
      {"name":"3.2 重要不等式","color":"#c2410c","desc":"均值不等式与柯西","items":[
        item("la-k3-3","均值不等式",["thm"],"$\\frac{a+b}{2}\\ge\\sqrt{ab}\\ge\\frac{2ab}{a+b}$。","<p>对正数 $a,b$，调和平均 $\\le$ 几何平均 $\\le$ 算术平均：</p><div class=\"la-fml\">$$\\frac{2}{\\frac{1}{a}+\\frac{1}{b}}\\le\\sqrt{ab}\\le\\frac{a+b}{2}$$</div>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"解析几何","en":"ANALYTIC GEOMETRY","sub":"直线、圆锥曲线","desc":"用代数方法研究几何图形。直线、圆、椭圆、双曲线、抛物线。","sections":[
      {"name":"4.1 直线与圆","color":"#2563eb","desc":"直线方程与圆的方程","items":[
        item("la-k4-1","直线方程",["def","exa"],"点斜式 $y-y_0=k(x-x_0)$，一般式 $Ax+By+C=0$。","<p>斜率 $k=\\tan\\alpha$，两点 $(x_1,y_1),(x_2,y_2)$ 连线斜率：</p><div class=\"la-fml\">$$k=\\frac{y_2-y_1}{x_2-x_1}$$</div>"),
        item("la-k4-2","圆的方程",["def","thm"],"$(x-a)^2+(y-b)^2=r^2$。","<p>圆心 $(a,b)$、半径 $r$ 的圆。一般方程 $x^2+y^2+Dx+Ey+F=0$，圆心 $(-D/2,-E/2)$。</p>"),
      ]},
      {"name":"4.2 圆锥曲线","color":"#7c3aed","desc":"椭圆、双曲线、抛物线","items":[
        item("la-k4-3","椭圆",["def","thm"],"$\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1$，离心率 $e=c/a<1$。","<p>到两焦点距离之和为定值 $2a$ 的点轨迹。$c^2=a^2-b^2$。</p>"),
        item("la-k4-4","双曲线与抛物线",["def"],"双曲线 $e>1$，抛物线 $e=1$。","<p>双曲线：$\\frac{x^2}{a^2}-\\frac{y^2}{b^2}=1$，$c^2=a^2+b^2$。抛物线：$y^2=2px$，焦点 $(p/2,0)$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 2. 微积分（高等数学） advanced-math
# ============================================================
SUBJECTS.append({
  "filename":"advanced-math.html",
  "title":"微积分",
  "eyebrow":"CALCULUS",
  "subtitle":"极限 · 导数 · 积分 · 微分方程 · 多元微积分 · 无穷级数",
  "meta_desc":"微积分知识体系：极限、导数、积分、微分方程、多元微积分、无穷级数",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"极限与连续","en":"LIMITS & CONTINUITY","sub":"极限定义、收敛准则、连续函数","desc":"微积分的基石是极限。本章建立数列极限与函数极限的严格定义，讨论连续性与闭区间上连续函数的性质。","sections":[
      {"name":"1.1 极限","color":"#2563eb","desc":"$\\varepsilon$-$\\delta$ 语言","items":[
        item("la-k1-1","数列极限",["def","thm"],"$\\forall\\varepsilon>0,\\exists N,\\forall n>N:|a_n-A|<\\varepsilon$。","<p><strong>定义</strong>　数列 $\\{a_n\\}$ 收敛于 $A$：对任意 $\\varepsilon>0$，存在正整数 $N$，当 $n>N$ 时 $|a_n-A|<\\varepsilon$。</p>"),
        item("la-k1-2","两个重要极限",["thm","exa"],"$\\lim_{x\\to0}\\frac{\\sin x}{x}=1$，$\\lim_{x\\to\\infty}(1+\\frac1x)^x=e$。","<p>这两个极限是导数定义的基础。第二个定义了自然常数 $e\\approx2.71828$。</p>"),
      ]},
      {"name":"1.2 连续","color":"#7c3aed","desc":"连续函数的性质","items":[
        item("la-k1-3","函数连续",["def","thm"],"$\\lim_{x\\to a}f(x)=f(a)$。","<p>函数在 $a$ 连续要求：极限存在、$f(a)$ 有定义、二者相等。闭区间上连续函数有最值定理、介值定理、零点定理。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"导数与微分","en":"DERIVATIVES","sub":"导数定义、求导法则、微分中值定理","desc":"导数刻画瞬时变化率，微分中值定理连接导数与函数值。","sections":[
      {"name":"2.1 导数","color":"#2563eb","desc":"变化率与切线斜率","items":[
        item("la-k2-1","导数定义",["def"],"$f'(x)=\\lim_{\\Delta x\\to0}\\frac{f(x+\\Delta x)-f(x)}{\\Delta x}$。","<p>导数即切线斜率。基本求导公式：$(x^n)'=nx^{n-1}$，$(\\sin x)'=\\cos x$，$(e^x)'=e^x$，$(\\ln x)'=1/x$。</p>"),
        item("la-k2-2","求导法则",["thm"],"$(uv)'=u'v+uv'$，$(u/v)'=(u'v-uv')/v^2$，链式法则。","<p>链式法则：若 $y=f(u),u=g(x)$，则 $y'=f'(u)\\cdot g'(x)$。</p>"),
      ]},
      {"name":"2.2 中值定理","color":"#0f766e","desc":"罗尔、拉格朗日、柯西","items":[
        item("la-k2-3","拉格朗日中值定理",["thm"],"$\\exists\\xi\\in(a,b):f(b)-f(a)=f'(\\xi)(b-a)$。","<p>若 $f$ 在 $[a,b]$ 连续、$(a,b)$ 可导，则存在 $\\xi$ 使切线平行于割线。罗尔定理是其 $f(a)=f(b)$ 的特例。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"积分","en":"INTEGRALS","sub":"不定积分、定积分、牛顿-莱布尼茨公式","desc":"积分是微分的逆运算。牛顿-莱布尼茨公式将定积分与原函数联系起来。","sections":[
      {"name":"3.1 不定积分","color":"#7c3aed","desc":"原函数与积分公式","items":[
        item("la-k3-1","不定积分",["def","exa"],"$\\int f(x)\\,dx=F(x)+C$，$F'=f$。","<p>基本公式：$\\int x^n dx=\\frac{x^{n+1}}{n+1}+C$，$\\int \\frac1x dx=\\ln|x|+C$，$\\int e^x dx=e^x+C$。</p>"),
        item("la-k3-2","换元与分部积分",["thm","der"],"$\\int f(g(x))g'(x)dx=\\int f(u)du$，$\\int u\\,dv=uv-\\int v\\,du$。","<p>换元积分用于复合函数，分部积分用于乘积：选择 $u$ 按 LIATE 法则（对数、反三角、代数、三角、指数）。</p>"),
      ]},
      {"name":"3.2 定积分","color":"#c2410c","desc":"黎曼和与微积分基本定理","items":[
        item("la-k3-3","牛顿-莱布尼茨公式",["thm"],"$\\int_a^b f(x)dx=F(b)-F(a)$。","<p>微积分基本定理：若 $F'=f$，则定积分等于原函数的差值。这是微分与积分的桥梁。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"微分方程","en":"DIFFERENTIAL EQUATIONS","sub":"一阶、二阶常微分方程","desc":"微分方程描述变化规律。本章覆盖可分离变量、一阶线性、二阶常系数线性方程。","sections":[
      {"name":"4.1 一阶方程","color":"#2563eb","desc":"可分离变量与一阶线性","items":[
        item("la-k4-1","可分离变量",["def","exa"],"$\\frac{dy}{dx}=f(x)g(y)\\Rightarrow\\int\\frac{dy}{g(y)}=\\int f(x)dx$。","<p>形如 $y'=f(x)g(y)$ 的方程可分离变量后两边积分。</p>"),
        item("la-k4-2","一阶线性方程",["thm","der"],"$y'+P(x)y=Q(x)$，积分因子 $\\mu=e^{\\int Pdx}$。","<p>通解公式：</p><div class=\"la-fml\">$$y=e^{-\\int Pdx}\\left(\\int Qe^{\\int Pdx}dx+C\\right)$$</div>"),
      ]},
      {"name":"4.2 二阶常系数线性","color":"#0f766e","desc":"齐次与非齐次","items":[
        item("la-k4-3","二阶常系数齐次",["thm"],"$y''+py'+qy=0$，特征方程 $r^2+pr+q=0$。","<p>根据特征根 $r_1,r_2$：</p><ul><li>两不等实根：$y=C_1e^{r_1x}+C_2e^{r_2x}$</li><li>重根：$y=(C_1+C_2x)e^{rx}$</li><li>共轭复根 $\\alpha\\pm i\\beta$：$y=e^{\\alpha x}(C_1\\cos\\beta x+C_2\\sin\\beta x)$</li></ul>"),
      ]},
    ]},
    {"id":"la-ch5","num":"第五章","title":"多元微积分与级数","en":"MULTIVARIABLE & SERIES","sub":"偏导数、重积分、级数收敛","desc":"将微积分推广到多元函数，并引入无穷级数作为函数表示工具。","sections":[
      {"name":"5.1 多元函数微分","color":"#7c3aed","desc":"偏导数、全微分、链式法则","items":[
        item("la-k5-1","偏导数",["def"],"$f_x=\\frac{\\partial f}{\\partial x}$，固定其他变量对 $x$ 求导。","<p>偏导数 $f_x$ 刻画函数沿 $x$ 方向的变化率。混合偏导在连续时相等：$f_{xy}=f_{yx}$。</p>"),
        item("la-k5-2","全微分",["def","thm"],"$dz=\\frac{\\partial z}{\\partial x}dx+\\frac{\\partial z}{\\partial y}dy$。","<p>全微分是多元函数线性增量的主部。可微要求偏导数存在且连续。</p>"),
      ]},
      {"name":"5.2 无穷级数","color":"#c2410c","desc":"数项级数、幂级数、泰勒级数","items":[
        item("la-k5-3","级数收敛",["def","thm"],"$\\sum a_n$ 收敛 $\\iff$ 部分和 $S_n$ 收敛。","<p>判别法：比值判别 $\\lim|a_{n+1}/a_n|$，根值判别 $\\lim\\sqrt[n]{|a_n|}$，比较判别，莱布尼茨交错级数判别。</p>"),
        item("la-k5-4","泰勒级数",["thm","app"],"$f(x)=\\sum_{n=0}^\\infty\\frac{f^{(n)}(a)}{n!}(x-a)^n$。","<p>常用展开：$e^x=\\sum x^n/n!$，$\\sin x=\\sum(-1)^n x^{2n+1}/(2n+1)!$，$\\frac1{1-x}=\\sum x^n$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 3. 概率论与数理统计 probability-statistics
# ============================================================
SUBJECTS.append({
  "filename":"probability-statistics.html",
  "title":"概率论与数理统计",
  "eyebrow":"PROBABILITY & STATISTICS",
  "subtitle":"随机事件 · 随机变量 · 分布 · 数字特征 · 参数估计 · 假设检验",
  "meta_desc":"概率论与数理统计知识体系：随机事件、随机变量、分布、数字特征、参数估计、假设检验",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"概率论基础","en":"PROBABILITY FOUNDATIONS","sub":"随机事件、概率公理化、条件概率","desc":"概率是不确定性的数学语言。本章从古典概型出发，建立概率的公理化定义，讨论条件概率、独立性与全概率公式。","sections":[
      {"name":"1.1 概率公理","color":"#2563eb","desc":"柯尔莫哥洛夫公理","items":[
        item("la-k1-1","概率公理",["def","thm"],"非负性、规范性、可列可加性。","<p><strong>定义</strong>　概率 $P$ 是样本空间 $\\Omega$ 上事件域到 $[0,1]$ 的映射，满足：$P(A)\\ge0$，$P(\\Omega)=1$，对互斥事件 $P(\\bigcup A_i)=\\sum P(A_i)$。</p>"),
        item("la-k1-2","条件概率与独立性",["def","thm"],"$P(A|B)=P(AB)/P(B)$，独立 $P(AB)=P(A)P(B)$。","<p>全概率公式：$P(B)=\\sum P(A_i)P(B|A_i)$。贝叶斯公式：$P(A_i|B)=\\frac{P(A_i)P(B|A_i)}{P(B)}$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"随机变量与分布","en":"RANDOM VARIABLES","sub":"分布函数、常见分布","desc":"随机变量将随机事件数值化。本章讨论离散型与连续型随机变量及其分布。","sections":[
      {"name":"2.1 离散型分布","color":"#7c3aed","desc":"二项、泊松、几何","items":[
        item("la-k2-1","二项分布",["def","thm"],"$X\\sim B(n,p)$，$P(X=k)=C_n^k p^k(1-p)^{n-k}$。","<p>$n$ 次独立伯努利试验中成功次数。期望 $np$，方差 $np(1-p)$。</p>"),
        item("la-k2-2","泊松分布",["def","thm"],"$P(X=k)=\\frac{\\lambda^k}{k!}e^{-\\lambda}$，$E(X)=\\lambda$。","<p>稀有事件计数模型。当 $n$ 大 $p$ 小时，$B(n,p)\\approx P(np)$。</p>"),
      ]},
      {"name":"2.2 连续型分布","color":"#0f766e","desc":"均匀、指数、正态","items":[
        item("la-k2-3","正态分布",["def","thm","app"],"$f(x)=\\frac1{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$。","<p>$X\\sim N(\\mu,\\sigma^2)$，标准化 $Z=(X-\\mu)/\\sigma\\sim N(0,1)$。中心极限定理使正态分布无处不在。</p>"),
        item("la-k2-4","指数分布",["def","thm"],"$f(x)=\\lambda e^{-\\lambda x}(x>0)$，无记忆性。","<p>等待时间模型。$P(X>s+t|X>s)=P(X>t)$。期望 $1/\\lambda$。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"数字特征","en":"MOMENTS","sub":"期望、方差、协方差、矩","desc":"数字特征概括分布的关键信息：中心位置、离散程度、相关关系。","sections":[
      {"name":"3.1 期望与方差","color":"#c2410c","desc":"均值与波动","items":[
        item("la-k3-1","数学期望",["def","thm"],"$E(X)=\\int x f(x)dx$，线性性 $E(aX+b)=aE(X)+b$。","<p>期望即加权平均。对函数 $g(X)$，$E[g(X)]=\\int g(x)f(x)dx$。</p>"),
        item("la-k3-2","方差",["def","thm"],"$D(X)=E[(X-EX)^2]=E(X^2)-(EX)^2$。","<p>方差刻画离散程度。$D(aX+b)=a^2D(X)$。标准差 $\\sigma=\\sqrt{D(X)}$。</p>"),
      ]},
      {"name":"3.2 协方差与相关系数","color":"#7c3aed","desc":"两个变量的线性关系","items":[
        item("la-k3-3","相关系数",["def","thm"],"$\\rho=\\frac{\\text{Cov}(X,Y)}{\\sigma_X\\sigma_Y}$，$|\\rho|\\le1$。","<p>$\\text{Cov}(X,Y)=E(XY)-E(X)E(Y)$。$\\rho=\\pm1$ 表示完全线性相关。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"数理统计","en":"MATHEMATICAL STATISTICS","sub":"抽样分布、参数估计、假设检验","desc":"数理统计从样本推断总体。本章覆盖参数估计与假设检验。","sections":[
      {"name":"4.1 参数估计","color":"#2563eb","desc":"点估计与区间估计","items":[
        item("la-k4-1","矩估计与极大似然",["def","der"],"矩估计用样本矩代替总体矩；MLE 最大化似然函数。","<p>极大似然估计：$\\hat\\theta=\\arg\\max L(\\theta)=\\arg\\max\\prod f(x_i;\\theta)$。</p>"),
      ]},
      {"name":"4.2 假设检验","color":"#0f766e","desc":"显著性检验","items":[
        item("la-k4-2","假设检验",["def","thm"],"原假设 $H_0$ vs 备择 $H_1$，$p$ 值判断。","<p>第一类错误（弃真）概率为显著性水平 $\\alpha$。当 $p<\\alpha$ 拒绝 $H_0$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 4. 群论 group-theory
# ============================================================
SUBJECTS.append({
  "filename":"group-theory.html",
  "title":"群论",
  "eyebrow":"GROUP THEORY",
  "subtitle":"群的定义 · 子群 · 同态 · 表示论 · 对称性",
  "meta_desc":"群论知识体系：群的定义、子群、同态、表示论、对称性",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"群的基本概念","en":"GROUPS","sub":"群公理、子群、陪集","desc":"群是描述对称性的代数结构。本章建立群的公理体系，讨论子群、陪集与拉格朗日定理。","sections":[
      {"name":"1.1 群公理","color":"#2563eb","desc":"封闭性、结合律、单位元、逆元","items":[
        item("la-k1-1","群的定义",["def","exa"],"$(G,\\cdot)$ 满足封闭、结合、单位元、逆元。","<p><strong>定义</strong>　群 $G$ 是一个集合配以二元运算 $\\cdot$，满足：封闭性、结合律、存在单位元 $e$、每个元素有逆元 $g^{-1}$。</p><p>例子：整数加法群 $\\mathbb{Z}$，$n$ 阶循环群 $\\mathbb{Z}_n$，对称群 $S_n$。</p>"),
        item("la-k1-2","子群与陪集",["def","thm"],"$H\\le G$，左陪集 $gH=\\{gh|h\\in H\\}$。","<p>子群对运算封闭且含逆元。拉格朗日定理：有限群 $|G|=[G:H]\\cdot|H|$，子群阶整除群阶。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"同态与正规子群","en":"HOMOMORPHISMS","sub":"群同态、商群、同构定理","desc":"同态保持群运算。正规子群使商群成为群，同构定理揭示群的结构。","sections":[
      {"name":"2.1 同态","color":"#7c3aed","desc":"保持运算的映射","items":[
        item("la-k2-1","群同态",["def","thm"],"$\\phi(ab)=\\phi(a)\\phi(b)$，核 $\\ker\\phi$，像 $\\text{Im}\\phi$。","<p>同构第一定理：$G/\\ker\\phi\\cong\\text{Im}\\phi$。核是正规子群。</p>"),
        item("la-k2-2","正规子群与商群",["def","thm"],"$N\\triangleleft G$ 若 $gNg^{-1}=N$，商群 $G/N$。","<p>正规子群的左陪集与右陪集重合，可定义商群乘法 $(aN)(bN)=abN$。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"群作用与表示","en":"ACTIONS & REPRESENTATIONS","sub":"群作用、轨道、表示论","desc":"群通过作用于集合来体现对称性。表示论将群元素映射为矩阵。","sections":[
      {"name":"3.1 群作用","color":"#0f766e","desc":"置换表示","items":[
        item("la-k3-1","群作用",["def","thm"],"$G\\times X\\to X$，轨道-稳定化子定理。","<p>轨道 $\\mathcal{O}_x=\\{g\\cdot x|g\\in G\\}$，稳定化子 $G_x=\\{g|g\\cdot x=x\\}$。$|\\mathcal{O}_x|=[G:G_x]$。</p>"),
      ]},
      {"name":"3.2 表示论","color":"#c2410c","desc":"线性表示、特征标","items":[
        item("la-k3-2","群表示",["def","thm"],"$\\rho:G\\to GL(V)$，特征标 $\\chi(g)=\\text{tr}\\rho(g)$。","<p>不可约表示是表示的基本砖块。特征标正交关系：$\\frac1{|G|}\\sum_g\\chi_i(g)\\overline{\\chi_j(g)}=\\delta_{ij}$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 5. 数学物理方法 mathematical-methods
# ============================================================
SUBJECTS.append({
  "filename":"mathematical-methods.html",
  "title":"数学物理方法",
  "eyebrow":"MATHEMATICAL METHODS",
  "subtitle":"复变函数 · 积分变换 · 偏微分方程 · 特殊函数",
  "meta_desc":"数学物理方法知识体系：复变函数、积分变换、偏微分方程、特殊函数",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"复变函数","en":"COMPLEX ANALYSIS","sub":"解析函数、复积分、留数","desc":"复变函数是物理中强大的计算工具。本章讨论解析性、柯西定理与留数计算。","sections":[
      {"name":"1.1 解析函数","color":"#2563eb","desc":"柯西-黎曼条件","items":[
        item("la-k1-1","解析函数",["def","thm"],"$u_x=v_y$，$u_y=-v_x$，解析 $\\iff$ 可微且 C-R 条件。","<p>$f(z)=u(x,y)+iv(x,y)$ 在区域内可微 $\\iff$ $u,v$ 可微且满足 C-R 方程。解析函数无限次可微。</p>"),
        item("la-k1-2","柯西积分公式",["thm"],"$f^{(n)}(z_0)=\\frac{n!}{2\\pi i}\\oint_C\\frac{f(z)}{(z-z_0)^{n+1}}dz$。","<p>若 $f$ 在围道 $C$ 内解析，则 $f(z_0)=\\frac1{2\\pi i}\\oint\\frac{f(z)}{z-z_0}dz$。解析函数由边界值完全确定。</p>"),
      ]},
      {"name":"1.2 留数定理","color":"#7c3aed","desc":"奇点与留数计算","items":[
        item("la-k1-3","留数定理",["thm","app"],"$\\oint_C f(z)dz=2\\pi i\\sum\\text{Res}(f,a_k)$。","<p>一阶极点留数：$\\text{Res}(f,a)=\\lim_{z\\to a}(z-a)f(z)$。留数定理可计算大量实积分。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"积分变换","en":"INTEGRAL TRANSFORMS","sub":"傅里叶、拉普拉斯变换","desc":"积分变换将微分方程化为代数方程，是求解 PDE 的利器。","sections":[
      {"name":"2.1 傅里叶变换","color":"#0f766e","desc":"频域分析","items":[
        item("la-k2-1","傅里叶变换",["def","thm"],"$\\tilde f(k)=\\int_{-\\infty}^\\infty f(x)e^{-ikx}dx$。","<p>逆变换：$f(x)=\\frac1{2\\pi}\\int\\tilde f(k)e^{ikx}dk$。微分性质：$\\mathcal{F}[f']=ik\\tilde f$。</p>"),
        item("la-k2-2","卷积定理",["thm"],"$\\mathcal{F}[f*g]=\\tilde f\\cdot\\tilde g$。","<p>卷积 $(f*g)(x)=\\int f(x-y)g(y)dy$。时域卷积对应频域乘积。</p>"),
      ]},
      {"name":"2.2 拉普拉斯变换","color":"#c2410c","desc":"初值问题求解","items":[
        item("la-k2-3","拉普拉斯变换",["def","app"],"$F(s)=\\int_0^\\infty f(t)e^{-st}dt$。","<p>微分性质：$\\mathcal{L}[f']=sF(s)-f(0)$。将 ODE 初值问题化为代数方程。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"偏微分方程","en":"PDEs","sub":"分离变量、波动方程、热方程","desc":"三类典型方程：波动、热传导、拉普拉斯方程，用分离变量法求解。","sections":[
      {"name":"3.1 分离变量法","color":"#2563eb","desc":"将 PDE 化为 ODE","items":[
        item("la-k3-1","分离变量",["def","der"],"设 $u(x,t)=X(x)T(t)$，代入 PDE 分离出本征值问题。","<p>以波动方程 $u_{tt}=a^2u_{xx}$ 为例，代入得 $T''/a^2T=X''/X=-\\lambda$，分别求解常微分方程。</p>"),
        item("la-k3-2","本征函数展开",["thm","app"],"解为 $\\sum C_n\\sin\\frac{n\\pi x}{L}\\cos\\frac{n\\pi at}{L}$。","<p>利用初始条件确定系数 $C_n$，即傅里叶正弦展开。</p>"),
      ]},
      {"name":"3.2 格林函数","color":"#7c3aed","desc":"点源响应","items":[
        item("la-k3-3","格林函数",["def","thm"],"$LG(x,x')=\\delta(x-x')$，解为 $\\int Gf\\,dx'$。","<p>格林函数是算子 $L$ 在点源 $\\delta$ 下的响应。非齐次方程 $Lu=f$ 的解由卷积给出。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 6. 特殊函数 special-functions
# ============================================================
SUBJECTS.append({
  "filename":"special-functions.html",
  "title":"特殊函数",
  "eyebrow":"SPECIAL FUNCTIONS",
  "subtitle":"勒让德 · 贝塞尔 · 球谐函数 · 伽马函数 · 椭圆积分",
  "meta_desc":"特殊函数知识体系：勒让德、贝塞尔、球谐函数、伽马函数、椭圆积分",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"勒让德函数","en":"LEGENDRE","sub":"勒让德方程、多项式、递推","desc":"勒让德多项式出现在球坐标拉普拉斯方程中。本章讨论其生成函数、正交性与递推关系。","sections":[
      {"name":"1.1 勒让德多项式","color":"#2563eb","desc":"罗德里格斯公式与生成函数","items":[
        item("la-k1-1","勒让德多项式",["def","thm"],"$P_n(x)=\\frac1{2^n n!}\\frac{d^n}{dx^n}(x^2-1)^n$。","<p>满足 $(1-x^2)y''-2xy'+n(n+1)y=0$。前几例：$P_0=1$，$P_1=x$，$P_2=\\frac12(3x^2-1)$。</p>"),
        item("la-k1-2","正交归一",["thm"],"$\\int_{-1}^1 P_mP_n dx=\\frac{2}{2n+1}\\delta_{mn}$。","<p>勒让德多项式在 $[-1,1]$ 上正交，可展开任意平方可积函数。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"贝塞尔函数","en":"BESSEL","sub":"贝塞尔方程、递推、渐近","desc":"贝塞尔函数在柱坐标中出现，描述径向振荡。本章讨论第一类、第二类贝塞尔函数及其性质。","sections":[
      {"name":"2.1 贝塞尔函数","color":"#7c3aed","desc":"级数解与递推","items":[
        item("la-k2-1","第一类贝塞尔函数",["def","thm"],"$J_n(x)=\\sum_{k=0}^\\infty\\frac{(-1)^k}{k!(k+n)!}\\left(\\frac x2\\right)^{2k+n}$。","<p>满足 $x^2y''+xy'+(x^2-n^2)y=0$。递推：$J_{n-1}+J_{n+1}=\\frac{2n}{x}J_n$。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"球谐函数与伽马","en":"SPHERICAL HARMONICS","sub":"球谐函数、伽马函数","desc":"球谐函数是球面上的正交基，伽马函数是阶乘的解析延拓。","sections":[
      {"name":"3.1 球谐函数","color":"#0f766e","desc":"角向本征函数","items":[
        item("la-k3-1","球谐函数",["def","thm"],"$Y_l^m(\\theta,\\phi)=N_{lm}P_l^m(\\cos\\theta)e^{im\\phi}$。","<p>是角动量 $L^2,L_z$ 的共同本征函数：$L^2Y_l^m=l(l+1)Y_l^m$，$L_zY_l^m=mY_l^m$。正交归一 $\\int Y_{l'}^*{}^{m'}Y_l^m d\\Omega=\\delta_{ll'}\\delta_{mm'}$。</p>"),
      ]},
      {"name":"3.2 伽马函数","color":"#c2410c","desc":"阶乘的延拓","items":[
        item("la-k3-2","伽马函数",["def","thm"],"$\\Gamma(z)=\\int_0^\\infty t^{z-1}e^{-t}dt$，$\\Gamma(n+1)=n!$。","<p>性质：$\\Gamma(z+1)=z\\Gamma(z)$，$\\Gamma(1/2)=\\sqrt\\pi$，余元公式 $\\Gamma(z)\\Gamma(1-z)=\\pi/\\sin\\pi z$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 7. 矢量分析 vector-analysis
# ============================================================
SUBJECTS.append({
  "filename":"vector-analysis.html",
  "title":"矢量分析",
  "eyebrow":"VECTOR CALCULUS",
  "subtitle":"梯度 · 散度 · 旋度 · 高斯定理 · 斯托克斯定理",
  "meta_desc":"矢量分析知识体系：梯度、散度、旋度、高斯定理、斯托克斯定理",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"矢量场微分","en":"VECTOR DIFFERENTIAL","sub":"梯度、散度、旋度","desc":"矢量分析研究标量场与矢量场的微分运算。梯度、散度、旋度是三个基本算子。","sections":[
      {"name":"1.1 梯度","color":"#2563eb","desc":"标量场的方向导数","items":[
        item("la-k1-1","梯度",["def","thm"],"$\\nabla\\phi=(\\partial_x\\phi,\\partial_y\\phi,\\partial_z\\phi)$。","<p>梯度指向标量场增长最快的方向，其模为最大方向导数。$\\nabla\\phi\\cdot\\hat{n}$ 是沿 $\\hat{n}$ 方向的方向导数。</p>"),
      ]},
      {"name":"1.2 散度与旋度","color":"#7c3aed","desc":"矢量场的源与涡","items":[
        item("la-k1-2","散度",["def","thm"],"$\\nabla\\cdot\\boldsymbol{A}=\\partial_x A_x+\\partial_y A_y+\\partial_z A_z$。","<p>散度描述矢量场的“源”强度。$\\nabla\\cdot\\boldsymbol{A}>0$ 为源，$<0$ 为汇。</p>"),
        item("la-k1-3","旋度",["def","thm"],"$\\nabla\\times\\boldsymbol{A}$，描述场的旋转。","<p>旋度方向沿旋转轴，模为旋转强度。$\\nabla\\times\\boldsymbol{A}=0$ 的场为保守场，可表为标量梯度。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"积分定理","en":"INTEGRAL THEOREMS","sub":"高斯、斯托克斯、格林","desc":"积分定理将场的体积分、面积分、线积分联系起来，是电磁场理论的基础。","sections":[
      {"name":"2.1 高斯散度定理","color":"#0f766e","desc":"体积分与面积分","items":[
        item("la-k2-1","高斯定理",["thm"],"$\\int_V\\nabla\\cdot\\boldsymbol{A}\\,dV=\\oint_S\\boldsymbol{A}\\cdot d\\boldsymbol{S}$。","<p>矢量场的散度在体积内的积分等于其穿过闭合曲面的通量。这是电磁场高斯定律的数学基础。</p>"),
      ]},
      {"name":"2.2 斯托克斯定理","color":"#c2410c","desc":"面积分与线积分","items":[
        item("la-k2-2","斯托克斯定理",["thm"],"$\\int_S(\\nabla\\times\\boldsymbol{A})\\cdot d\\boldsymbol{S}=\\oint_C\\boldsymbol{A}\\cdot d\\boldsymbol{l}$。","<p>旋度穿过曲面的通量等于矢量沿闭合曲线的环量。法拉第定律的数学基础。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 8. 计算物理 computational-physics
# ============================================================
SUBJECTS.append({
  "filename":"computational-physics.html",
  "title":"计算物理",
  "eyebrow":"COMPUTATIONAL PHYSICS",
  "subtitle":"数值微分 · 数值积分 · 线性方程组 · ODE 求解 · 蒙特卡洛",
  "meta_desc":"计算物理知识体系：数值微分、数值积分、线性方程组、ODE求解、蒙特卡洛",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"数值微分与积分","en":"NUMERICAL CALCULUS","sub":"差分、求积公式","desc":"用离散近似连续运算。本章介绍有限差分与牛顿-科茨求积公式。","sections":[
      {"name":"1.1 数值微分","color":"#2563eb","desc":"有限差分","items":[
        item("la-k1-1","有限差分",["def","der"],"前向 $f'(x)\\approx[f(x+h)-f(x)]/h$，中心差分二阶精度。","<p>中心差分：$f'(x)\\approx\\frac{f(x+h)-f(x-h)}{2h}+O(h^2)$。截断误差与舍入误差需平衡。</p>"),
      ]},
      {"name":"1.2 数值积分","color":"#7c3aed","desc":"梯形、辛普森","items":[
        item("la-k1-2","辛普森公式",["thm","der"],"$\\int_a^b f\\,dx\\approx\\frac{h}{3}[f_0+4f_1+2f_2+\\cdots+4f_{n-1}+f_n]$。","<p>梯形公式 $O(h^2)$，辛普森公式 $O(h^4)$。高斯求积用最优节点达更高精度。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"线性方程组与矩阵","en":"LINEAR SYSTEMS","sub":"直接法与迭代法","desc":"求解 $A\\boldsymbol{x}=\\boldsymbol{b}$。直接法（高斯消元、LU）与迭代法（雅可比、共轭梯度）。","sections":[
      {"name":"2.1 直接法","color":"#0f766e","desc":"高斯消元与 LU 分解","items":[
        item("la-k2-1","高斯消元",["def","der"],"行变换化上三角，回代求解。","<p>LU 分解将 $A=LU$，则解 $Ly=b$ 与 $Ux=y$。复杂度 $O(n^3)$。</p>"),
      ]},
      {"name":"2.2 迭代法","color":"#c2410c","desc":"雅可比、高斯-赛德尔、CG","items":[
        item("la-k2-2","共轭梯度法",["thm","app"],"适用于对称正定矩阵，$n$ 步内精确收敛。","<p>CG 法利用 Krylov 子空间，对大型稀疏矩阵效率远高于直接法。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"ODE 与蒙特卡洛","en":"ODE & MONTE CARLO","sub":"龙格-库塔、随机采样","desc":"常微分方程数值求解与蒙特卡洛随机方法。","sections":[
      {"name":"3.1 ODE 求解","color":"#2563eb","desc":"欧拉、龙格-库塔","items":[
        item("la-k3-1","四阶龙格-库塔",["def","thm"],"RK4 精度 $O(h^4)$，每步计算 4 个斜率。","<p>$y_{n+1}=y_n+\\frac h6(k_1+2k_2+2k_3+k_4)$，$k_i$ 为各点斜率。经典且稳健。</p>"),
      ]},
      {"name":"3.2 蒙特卡洛","color":"#7c3aed","desc":"随机采样积分","items":[
        item("la-k3-2","蒙特卡洛积分",["def","thm","app"],"$\\int f\\,dx\\approx\\frac1N\\sum f(x_i)$，误差 $O(N^{-1/2})$。","<p>高维积分中蒙特卡洛优于网格法。Metropolis-Hastings 与 MCMC 可采样复杂分布。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 9. 理论力学 theoretical-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"theoretical-mechanics.html",
  "title":"理论力学",
  "eyebrow":"THEORETICAL MECHANICS",
  "subtitle":"拉格朗日方程 · 哈密顿原理 · 正则方程 · 刚体 · 微振动",
  "meta_desc":"理论力学知识体系：拉格朗日方程、哈密顿原理、正则方程、刚体、微振动",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"拉格朗日力学","en":"LAGRANGIAN MECHANICS","sub":"广义坐标、拉氏方程","desc":"从牛顿力学到拉格朗日力学，用能量而非力描述系统。","sections":[
      {"name":"1.1 约束与广义坐标","color":"#2563eb","desc":"自由度与拉氏量","items":[
        item("la-k1-1","拉格朗日量",["def","thm"],"$L=T-V$，拉氏方程 $\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_i}-\\frac{\\partial L}{\\partial q_i}=0$。","<p>广义坐标 $q_i$ 描述系统位形。拉氏方程对任意广义坐标成立，无需分析约束力。</p>"),
        item("la-k1-2","最小作用量原理",["thm","his"],"$\\delta S=0$，$S=\\int L\\,dt$。","<p>真实运动使作用量 $S$ 取极值。由此可导出拉氏方程，是力学的变分原理表述。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"哈密顿力学","en":"HAMILTONIAN MECHANICS","sub":"正则方程、泊松括号","desc":"哈密顿力学以动量和坐标为独立变量，相空间描述更对称。","sections":[
      {"name":"2.1 正则方程","color":"#7c3aed","desc":"勒让德变换","items":[
        item("la-k2-1","哈密顿量",["def","thm"],"$H=\\sum p_i\\dot q_i-L$，$\\dot q_i=\\partial H/\\partial p_i$，$\\dot p_i=-\\partial H/\\partial q_i$。","<p>正则方程是一阶方程组，对称优美。$H$ 守恒当且仅当 $\\partial H/\\partial t=0$（能量守恒）。</p>"),
        item("la-k2-2","泊松括号",["def","thm"],"$\\{f,g\\}=\\sum(\\partial_q f\\partial_p g-\\partial_p f\\partial_q g)$。","<p>$\\dot f=\\{f,H\\}+\\partial_t f$。泊松括号是量子力学对易子的经典对应。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"刚体与微振动","en":"RIGID BODIES","sub":"欧拉方程、简正模","desc":"刚体转动与小振动系统的处理。","sections":[
      {"name":"3.1 刚体转动","color":"#0f766e","desc":"惯量张量与欧拉方程","items":[
        item("la-k3-1","欧拉方程",["def","thm"],"$I_i\\dot\\omega_i-(I_j-I_k)\\omega_j\\omega_k=M_i$。","<p>沿惯量主轴的转动方程。对称陀螺可解析求解，引出章动与进动。</p>"),
      ]},
      {"name":"3.2 微振动","color":"#c2410c","desc":"简正模","items":[
        item("la-k3-2","简正模",["def","thm","der"],"本征频率由 $\\det(K-\\omega^2 M)=0$ 确定。","<p>小振动可解耦为独立简正模。质量矩阵 $M$ 与刚度矩阵 $K$ 的广义本征值问题。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 10. 流体力学 fluid-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"fluid-mechanics.html",
  "title":"流体力学",
  "eyebrow":"FLUID MECHANICS",
  "subtitle":"连续性方程 · 欧拉方程 · Navier-Stokes · 伯努利 · 湍流",
  "meta_desc":"流体力学知识体系：连续性方程、欧拉方程、Navier-Stokes、伯努利、湍流",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"流体基本方程","en":"FLUID EQUATIONS","sub":"连续性、欧拉、NS","desc":"流体作为连续介质，其运动由质量、动量、能量守恒方程描述。","sections":[
      {"name":"1.1 连续性与欧拉方程","color":"#2563eb","desc":"理想流体","items":[
        item("la-k1-1","连续性方程",["def","thm"],"$\\partial_t\\rho+\\nabla\\cdot(\\rho\\boldsymbol{v})=0$。","<p>质量守恒的微分形式。不可压缩流体 $\\nabla\\cdot\\boldsymbol{v}=0$。</p>"),
        item("la-k1-2","欧拉方程",["def","thm"],"$\\rho(\\partial_t\\boldsymbol{v}+\\boldsymbol{v}\\cdot\\nabla\\boldsymbol{v})=-\\nabla p+\\rho\\boldsymbol{f}$。","<p>理想流体（无粘）的动量方程。对流项 $\\boldsymbol{v}\\cdot\\nabla\\boldsymbol{v}$ 使方程非线性。</p>"),
      ]},
      {"name":"1.2 Navier-Stokes 方程","color":"#7c3aed","desc":"粘性流体","items":[
        item("la-k1-3","NS 方程",["def","thm"],"$\\rho(\\partial_t\\boldsymbol{v}+\\boldsymbol{v}\\cdot\\nabla\\boldsymbol{v})=-\\nabla p+\\mu\\nabla^2\\boldsymbol{v}+\\rho\\boldsymbol{f}$。","<p>引入粘性应力 $\\mu\\nabla^2\\boldsymbol{v}$。NS 方程的解析解极少，千禧年难题之一。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"伯努利与湍流","en":"BERNOULLI & TURBULENCE","sub":"能量积分、雷诺数","desc":"伯努利方程是定常无粘流的能量积分；湍流由雷诺数表征。","sections":[
      {"name":"2.1 伯努利方程","color":"#0f766e","desc":"沿流线守恒","items":[
        item("la-k2-1","伯努利方程",["thm","der"],"$\\frac12\\rho v^2+p+\\rho gz=\\text{常数}$（沿流线）。","<p>定常、无粘、不可压缩、沿流线成立。动能+压强能+势能守恒。</p>"),
      ]},
      {"name":"2.2 湍流","color":"#c2410c","desc":"雷诺数与雷诺平均","items":[
        item("la-k2-2","雷诺数",["def","thm","app"],"$Re=\\rho vL/\\mu$，$Re>Re_c$ 转捩湍流。","<p>雷诺数是惯性力与粘性力之比。湍流需用雷诺平均 NS（RANS）或大涡模拟（LES）处理。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 11. 固体力学 solid-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"solid-mechanics.html",
  "title":"固体力学",
  "eyebrow":"SOLID MECHANICS",
  "subtitle":"应力 · 应变 · 胡克定律 · 本构关系 · 有限元",
  "meta_desc":"固体力学知识体系：应力、应变、胡克定律、本构关系、有限元",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"应力与应变","en":"STRESS & STRAIN","sub":"张量描述","desc":"固体在外力下的变形用应力张量和应变张量描述。","sections":[
      {"name":"1.1 应力张量","color":"#2563eb","desc":"面力与应力","items":[
        item("la-k1-1","应力张量",["def","thm"],"$\\sigma_{ij}$ 为二阶对称张量，$\\sigma_{ij}=\\sigma_{ji}$。","<p>应力 $\\sigma_{ij}$ 表示 $j$ 方向面元上 $i$ 方向的力。平衡方程：$\\partial_j\\sigma_{ij}+f_i=0$。</p>"),
      ]},
      {"name":"1.2 应变张量","color":"#7c3aed","desc":"小变形","items":[
        item("la-k1-2","应变张量",["def","thm"],"$\\varepsilon_{ij}=\\frac12(\\partial_i u_j+\\partial_j u_i)$。","<p>小变形下应变是位移梯度的对称部分。体积应变 $\\varepsilon_{kk}=\\nabla\\cdot\\boldsymbol{u}$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"本构关系与有限元","en":"CONSTITUTIVE & FEM","sub":"胡克定律、数值方法","desc":"线弹性本构关系与有限元离散方法。","sections":[
      {"name":"2.1 胡克定律","color":"#0f766e","desc":"线弹性","items":[
        item("la-k2-1","广义胡克定律",["def","thm"],"$\\sigma_{ij}=C_{ijkl}\\varepsilon_{kl}$，各向同性简化为 $\\lambda,\\mu$。","<p>各向同性弹性体仅需两个独立常数（拉梅常数 $\\lambda,\\mu$）。杨氏模量 $E$、泊松比 $\\nu$ 可与之换算。</p>"),
      ]},
      {"name":"2.2 有限元方法","color":"#c2410c","desc":"离散化求解","items":[
        item("la-k2-2","有限元原理",["def","app"],"变分形式 + 分片多项式插值，求解 $K\\boldsymbol{u}=\\boldsymbol{F}$。","<p>将连续体离散为有限单元，在单元内用形函数插值位移，组装整体刚度矩阵求解。工程仿真的核心方法。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 12. 计算流体力学 cfd
# ============================================================
SUBJECTS.append({
  "filename":"cfd.html",
  "title":"计算流体力学",
  "eyebrow":"COMPUTATIONAL FLUID DYNAMICS",
  "subtitle":"有限差分 · 有限体积 · 有限元 · 谱方法 · 湍流模型",
  "meta_desc":"计算流体力学知识体系：有限差分、有限体积、有限元、谱方法、湍流模型",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"离散化方法","en":"DISCRETIZATION","sub":"FDM、FVM、FEM","desc":"将 NS 方程在空间离散为代数方程组。本章介绍三大离散方法。","sections":[
      {"name":"1.1 有限体积法","color":"#2563eb","desc":"守恒性最好","items":[
        item("la-k1-1","有限体积法",["def","thm"],"对控制体积分，数值通量 $F_{i+1/2}$ 近似面通量。","<p>FVM 天然满足守恒律，是 CFD 主流方法。关键是数值通量格式（Roe、HLLC 等）。</p>"),
      ]},
      {"name":"1.2 时间推进","color":"#7c3aed","desc":"显式与隐式","items":[
        item("la-k1-2","CFL 条件",["def","thm"],"$\\Delta t\\le C\\Delta x/|v|$，显式格式稳定性条件。","<p>CFL 数限制显式格式时间步。隐式格式（如 LU-SGS）可放大步长但每步更贵。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"湍流模型","en":"TURBULENCE MODELING","sub":"RANS、LES、DNS","desc":"湍流计算需建模。RANS 用雷诺平均，LES 解大涡模小涡。","sections":[
      {"name":"2.1 RANS 模型","color":"#0f766e","desc":"$k-\\epsilon$、$k-\\omega$","items":[
        item("la-k2-1","$k-\\epsilon$ 模型",["def","app"],"两方程模型，$\\mu_t=\\rho C_\\mu k^2/\\epsilon$。","<p>工业界最常用的湍流模型。$k$ 为湍动能，$\\epsilon$ 为耗散率。SST $k-\\omega$ 在近壁更优。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 13. 电磁学 electromagnetism
# ============================================================
SUBJECTS.append({
  "filename":"electromagnetism.html",
  "title":"电磁学",
  "eyebrow":"ELECTROMAGNETISM",
  "subtitle":"静电场 · 静磁场 · 电磁感应 · 麦克斯韦方程组 · 电磁波",
  "meta_desc":"电磁学知识体系：静电场、静磁场、电磁感应、麦克斯韦方程组、电磁波",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"静电场","en":"ELECTROSTATICS","sub":"库仑定律、高斯定律、电势","desc":"静电场由静止电荷产生。本章从库仑定律出发，讨论电场、电势与导体。","sections":[
      {"name":"1.1 电场与高斯定律","color":"#2563eb","desc":"场的通量与源","items":[
        item("la-k1-1","库仑定律",["def","thm"],"$\\boldsymbol{F}=\\frac{1}{4\\pi\\varepsilon_0}\\frac{q_1q_2}{r^2}\\hat{\\boldsymbol{r}}$。","<p>点电荷间作用力。电场 $\\boldsymbol{E}=\\boldsymbol{F}/q_0$。</p>"),
        item("la-k1-2","高斯定律",["thm"],"$\\oint\\boldsymbol{E}\\cdot d\\boldsymbol{S}=Q_{\\text{enclosed}}/\\varepsilon_0$。","<p>电通量正比于闭合面内电荷。微分形式 $\\nabla\\cdot\\boldsymbol{E}=\\rho/\\varepsilon_0$。</p>"),
      ]},
      {"name":"1.2 电势","color":"#7c3aed","desc":"保守场的标量势","items":[
        item("la-k1-3","电势",["def","thm"],"$\\boldsymbol{E}=-\\nabla\\varphi$，$\\varphi=\\frac1{4\\pi\\varepsilon_0}\\int\\frac{\\rho}{r}dV$。","<p>静电场无旋，可表为电势梯度。电势满足泊松方程 $\\nabla^2\\varphi=-\\rho/\\varepsilon_0$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"静磁场","en":"MAGNETOSTATICS","sub":"毕奥-萨伐尔、安培定律","desc":"稳恒电流产生磁场。本章讨论磁场的计算与安培环路定律。","sections":[
      {"name":"2.1 磁场定律","color":"#0f766e","desc":"电流的磁效应","items":[
        item("la-k2-1","毕奥-萨伐尔定律",["def","thm"],"$d\\boldsymbol{B}=\\frac{\\mu_0}{4\\pi}\\frac{I d\\boldsymbol{l}\\times\\hat{\\boldsymbol{r}}}{r^2}$。","<p>电流元产生的磁场。磁场是无源场：$\\nabla\\cdot\\boldsymbol{B}=0$。</p>"),
        item("la-k2-2","安培定律",["thm"],"$\\oint\\boldsymbol{B}\\cdot d\\boldsymbol{l}=\\mu_0 I_{\\text{enclosed}}$。","<p>磁场环量正比于穿过的电流。微分形式 $\\nabla\\times\\boldsymbol{B}=\\mu_0\\boldsymbol{J}$。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"电磁感应与电磁波","en":"INDUCTION & EM WAVES","sub":"法拉第定律、麦克斯韦方程组","desc":"变化的磁场产生电场，变化的电场产生磁场，形成电磁波。","sections":[
      {"name":"3.1 电磁感应","color":"#c2410c","desc":"法拉第定律","items":[
        item("la-k3-1","法拉第定律",["def","thm"],"$\\mathcal{E}=-\\frac{d\\Phi_B}{dt}$，$\\nabla\\times\\boldsymbol{E}=-\\partial_t\\boldsymbol{B}$。","<p>感应电动势等于磁通量变化率的负值。负号体现楞次定律。</p>"),
      ]},
      {"name":"3.2 麦克斯韦方程组","color":"#7c3aed","desc":"电磁理论的统一","items":[
        item("la-k3-2","麦克斯韦方程组",["thm","his"],"$\\nabla\\cdot\\boldsymbol{E}=\\rho/\\varepsilon_0$，$\\nabla\\cdot\\boldsymbol{B}=0$，$\\nabla\\times\\boldsymbol{E}=-\\partial_t\\boldsymbol{B}$，$\\nabla\\times\\boldsymbol{B}=\\mu_0\\boldsymbol{J}+\\mu_0\\varepsilon_0\\partial_t\\boldsymbol{E}$。","<p>麦克斯韦引入位移电流 $\\mu_0\\varepsilon_0\\partial_t\\boldsymbol{E}$，预言电磁波，光速 $c=1/\\sqrt{\\mu_0\\varepsilon_0}$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 14. 电动力学 electrodynamics
# ============================================================
SUBJECTS.append({
  "filename":"electrodynamics.html",
  "title":"电动力学",
  "eyebrow":"ELECTRODYNAMICS",
  "subtitle":"电磁场方程 · 势与规范 · 电磁波 · 辐射 · 相对论电动力学",
  "meta_desc":"电动力学知识体系：电磁场方程、势与规范、电磁波、辐射、相对论电动力学",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"电磁场的普遍规律","en":"ELECTROMAGNETIC FIELD","sub":"边值问题、能量动量","desc":"从麦克斯韦方程组出发，讨论电磁场的能量、动量与边值问题。","sections":[
      {"name":"1.1 能量与动量","color":"#2563eb","desc":"坡印廷矢量","items":[
        item("la-k1-1","坡印廷矢量",["def","thm"],"$\\boldsymbol{S}=\\frac1{\\mu_0}\\boldsymbol{E}\\times\\boldsymbol{B}$，能流密度。","<p>能量守恒：$\\partial_t u+\\nabla\\cdot\\boldsymbol{S}=-\\boldsymbol{J}\\cdot\\boldsymbol{E}$，其中 $u=\\frac12(\\varepsilon_0 E^2+B^2/\\mu_0)$。</p>"),
      ]},
      {"name":"1.2 势与规范","color":"#7c3aed","desc":"矢势与标势","items":[
        item("la-k1-2","规范变换",["def","thm"],"$\\boldsymbol{B}=\\nabla\\times\\boldsymbol{A}$，$\\boldsymbol{E}=-\\nabla\\varphi-\\partial_t\\boldsymbol{A}$。","<p>规范变换 $\\boldsymbol{A}\\to\\boldsymbol{A}+\\nabla\\chi$，$\\varphi\\to\\varphi-\\partial_t\\chi$ 不改变场。常用库仑规范 $\\nabla\\cdot\\boldsymbol{A}=0$ 与洛伦兹规范 $\\nabla\\cdot\\boldsymbol{A}+\\mu_0\\varepsilon_0\\partial_t\\varphi=0$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"电磁波与辐射","en":"EM WAVES & RADIATION","sub":"平面波、偶极辐射","desc":"真空中电磁波为横波，加速电荷辐射电磁波。","sections":[
      {"name":"2.1 平面电磁波","color":"#0f766e","desc":"波动方程","items":[
        item("la-k2-1","平面波",["def","thm"],"$\\boldsymbol{E},\\boldsymbol{B},\\boldsymbol{k}$ 右手正交，$E=cB$。","<p>真空中波动方程 $\\nabla^2\\boldsymbol{E}-\\frac1{c^2}\\partial_t^2\\boldsymbol{E}=0$。电磁波是横波，能量以光速传播。</p>"),
      ]},
      {"name":"2.2 偶极辐射","color":"#c2410c","desc":"加速电荷辐射","items":[
        item("la-k2-2","电偶极辐射",["def","thm","der"],"辐射功率 $P=\\frac{\\mu_0}{12\\pi c}|\\ddot{\\boldsymbol{p}}|^2$。","<p>振荡电偶极子辐射功率正比于频率四次方（拉莫尔公式的推广）。这是天线辐射的基本机制。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"相对论电动力学","en":"RELATIVISTIC ED","sub":"四维形式、协变","desc":"电动力学天然满足狭义相对论，可用四维张量统一表述。","sections":[
      {"name":"3.1 四维形式","color":"#7c3aed","desc":"协变表述","items":[
        item("la-k3-1","电磁场张量",["def","thm"],"$F_{\\mu\\nu}=\\partial_\\mu A_\\nu-\\partial_\\nu A_\\mu$，反对称二阶张量。","<p>麦克斯韦方程组可写为 $\\partial_\\mu F^{\\mu\\nu}=\\mu_0 J^\\nu$ 与 $\\partial_\\lambda F_{\\mu\\nu}+\\partial_\\mu F_{\\nu\\lambda}+\\partial_\\nu F_{\\lambda\\mu}=0$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 15. 电路 circuits
# ============================================================
SUBJECTS.append({
  "filename":"circuits.html",
  "title":"电路",
  "eyebrow":"CIRCUIT ANALYSIS",
  "subtitle":"基尔霍夫定律 · 电阻电路 · 一阶二阶电路 · 正弦稳态 · 三相电路",
  "meta_desc":"电路知识体系：基尔霍夫定律、电阻电路、一阶二阶电路、正弦稳态、三相电路",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"电路基本定律","en":"CIRCUIT LAWS","sub":"欧姆定律、基尔霍夫定律","desc":"电路分析的基础是欧姆定律与基尔霍夫两大定律。","sections":[
      {"name":"1.1 基本定律","color":"#2563eb","desc":"KCL 与 KVL","items":[
        item("la-k1-1","基尔霍夫定律",["def","thm"],"KCL：$\\sum I=0$（节点）；KVL：$\\sum U=0$（回路）。","<p>KCL 是电荷守恒的体现，流入等于流出。KVL 是能量守恒的体现，回路电压和为零。</p>"),
        item("la-k1-2","等效变换",["thm","der"],"串并联、星三角、戴维南/诺顿等效。","<p>戴维南定理：任何线性有源二端网络可等效为电压源 $U_{oc}$ 串联内阻 $R_{eq}$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"动态与正弦电路","en":"DYNAMIC & AC","sub":"一阶、二阶、相量法","desc":"含电容电感的动态电路与正弦稳态分析。","sections":[
      {"name":"2.1 动态电路","color":"#7c3aed","desc":"RC、RL、RLC","items":[
        item("la-k2-1","一阶电路",["def","thm"],"时间常数 $\\tau=RC$ 或 $L/R$，全响应=零输入+零状态。","<p>三要素法：$f(t)=f(\\infty)+[f(0_+)-f(\\infty)]e^{-t/\\tau}$。</p>"),
        item("la-k2-2","相量法",["def","thm"],"正弦量用相量 $\\dot{U}=U\\angle\\varphi$ 表示，微分变 $j\\omega$。","<p>相量法将时域微分方程化为频域代数方程。阻抗 $Z=R+jX$，导纳 $Y=1/Z$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 16. 模拟电子技术 analog-electronics
# ============================================================
SUBJECTS.append({
  "filename":"analog-electronics.html",
  "title":"模拟电子技术",
  "eyebrow":"ANALOG ELECTRONICS",
  "subtitle":"二极管 · BJT · 场效应管 · 放大器 · 运放 · 反馈",
  "meta_desc":"模拟电子技术知识体系：二极管、BJT、场效应管、放大器、运放、反馈",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"半导体器件","en":"SEMICONDUCTOR DEVICES","sub":"二极管、BJT、MOSFET","desc":"模拟电路的基本器件。本章讨论 PN 结二极管、双极型晶体管与场效应管。","sections":[
      {"name":"1.1 二极管与 BJT","color":"#2563eb","desc":"非线性器件","items":[
        item("la-k1-1","PN 结二极管",["def","thm"],"$I=I_s(e^{V/V_T}-1)$，正向导通约 0.7V。","<p>二极管单向导电。用于整流、限幅、稳压。肖特基二极管速度更快。</p>"),
        item("la-k1-2","BJT 三极管",["def","thm"],"工作于放大区时 $I_C=\\beta I_B$。","<p>BJT 有 NPN 与 PNP 两种。放大区条件：发射结正偏、集电结反偏。$\\beta$ 为电流放大系数。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"放大器与运放","en":"AMPLIFIERS & OP-AMPS","sub":"小信号模型、反馈","desc":"晶体管放大器的小信号分析与运算放大器应用。","sections":[
      {"name":"2.1 放大器","color":"#7c3aed","desc":"增益、输入输出阻抗","items":[
        item("la-k2-1","共射放大器",["def","thm","der"],"电压增益 $A_v=-\\beta R_C/r_{be}$。","<p>共射极放大器反相放大，既有电压增益又有电流增益。输入电阻 $r_{be}$，输出电阻 $R_C$。</p>"),
      ]},
      {"name":"2.2 运放与反馈","color":"#0f766e","desc":"理想运放、负反馈","items":[
        item("la-k2-2","理想运放",["def","thm"],"虚短 $v_+=v_-$，虚断 $i_+=i_-=0$。","<p>负反馈组态：电压串联、电压并联、电流串联、电流并联。反相放大器 $A_v=-R_f/R_1$，同相 $A_v=1+R_f/R_1$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 17. 数字电子技术 digital-electronics
# ============================================================
SUBJECTS.append({
  "filename":"digital-electronics.html",
  "title":"数字电子技术",
  "eyebrow":"DIGITAL ELECTRONICS",
  "subtitle":"逻辑代数 · 门电路 · 组合逻辑 · 触发器 · 时序逻辑",
  "meta_desc":"数字电子技术知识体系：逻辑代数、门电路、组合逻辑、触发器、时序逻辑",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"逻辑代数与门电路","en":"LOGIC & GATES","sub":"布尔代数、基本门","desc":"数字电路以二值逻辑为基础。本章介绍布尔代数与基本逻辑门。","sections":[
      {"name":"1.1 逻辑代数","color":"#2563eb","desc":"布尔运算","items":[
        item("la-k1-1","基本逻辑",["def","thm"],"与 AND、或 OR、非 NOT，摩根律 $\\overline{AB}=\\bar A+\\bar B$。","<p>布尔代数中变量取 0 或 1。基本运算：$A\\cdot B$（与）、$A+B$（或）、$\\bar A$（非）。</p>"),
      ]},
      {"name":"1.2 门电路","color":"#7c3aed","desc":"TTL、CMOS","items":[
        item("la-k1-2","CMOS 反相器",["def","app"],"NMOS+PMOS 互补结构，静态功耗极低。","<p>CMOS 是数字集成电路的主流。噪声容限大，速度与电源电压相关。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"组合与时序逻辑","en":"COMBINATIONAL & SEQUENTIAL","sub":"译码器、触发器、状态机","desc":"组合逻辑无记忆，时序逻辑有记忆。本章讨论常见逻辑部件。","sections":[
      {"name":"2.1 组合逻辑","color":"#0f766e","desc":"编码器、译码器","items":[
        item("la-k2-1","组合逻辑电路",["def","thm"],"输出仅取决于当前输入，无反馈。","<p>常用部件：编码器、译码器、数据选择器 MUX、加法器。可用卡诺图化简。</p>"),
      ]},
      {"name":"2.2 时序逻辑","color":"#c2410c","desc":"触发器、状态机","items":[
        item("la-k2-2","D 触发器",["def","thm"],"$Q^{n+1}=D$，边沿触发。","<p>D 触发器是最常用的存储元件。寄存器、计数器、有限状态机均由其构成。建立/保持时间约束决定最高时钟频率。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 18. 集成电路 integrated-circuits
# ============================================================
SUBJECTS.append({
  "filename":"integrated-circuits.html",
  "title":"集成电路",
  "eyebrow":"INTEGRATED CIRCUITS",
  "subtitle":"MOS 工艺 · 数字 IC · 模拟 IC · 版图 · 流片",
  "meta_desc":"集成电路知识体系：MOS工艺、数字IC、模拟IC、版图、流片",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"MOS 管与工艺","en":"MOS & PROCESS","sub":"MOSFET、工艺基础","desc":"集成电路以 MOSFET 为基本器件。本章讨论 MOS 管原理与工艺流程。","sections":[
      {"name":"1.1 MOSFET 原理","color":"#2563eb","desc":"场效应晶体管","items":[
        item("la-k1-1","MOS 管工作原理",["def","thm"],"栅压控制沟道，$I_D$ 工作于线性区或饱和区。","<p>增强型 NMOS：$V_{GS}>V_{th}$ 时反型层形成。饱和区 $I_D=\\frac12\\mu_n C_{ox}\\frac{W}{L}(V_{GS}-V_{th})^2$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"数字与模拟 IC","en":"DIGITAL & ANALOG IC","sub":"逻辑门、放大器","desc":"数字 IC 追求速度与功耗，模拟 IC 追求精度与线性度。","sections":[
      {"name":"2.1 数字 IC","color":"#7c3aed","desc":"逻辑门设计","items":[
        item("la-k2-1","CMOS 逻辑门",["def","app"],"与非门、或非门由 PMOS 上拉网络与 NMOS 下拉网络组成。","<p>CMOS 静态功耗近零。动态功耗 $P=\\alpha C_L V_{DD}^2 f$，是数字芯片功耗主因。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 19. 热学 thermal-physics
# ============================================================
SUBJECTS.append({
  "filename":"thermal-physics.html",
  "title":"热学",
  "eyebrow":"THERMAL PHYSICS",
  "subtitle":"温度 · 热力学定律 · 气体动理论 · 相变",
  "meta_desc":"热学知识体系：温度、热力学定律、气体动理论、相变",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"温度与热力学定律","en":"TEMPERATURE & LAWS","sub":"热平衡、四大定律","desc":"热学研究热现象的宏观规律。本章从温度出发，讨论热力学四大定律。","sections":[
      {"name":"1.1 温度与热平衡","color":"#2563eb","desc":"热力学第零定律","items":[
        item("la-k1-1","热力学第零定律",["def","thm"],"两系统分别与第三系统热平衡，则彼此热平衡。","<p>这为温度的定义提供了依据。温度是决定系统是否热平衡的状态函数。</p>"),
        item("la-k1-2","热力学第一定律",["def","thm"],"$\\Delta U=Q+W$，能量守恒。","<p>系统内能增量等于吸收的热量与外界对系统做功之和。$Q$ 吸热为正，$W$ 外界对系统做功为正。</p>"),
      ]},
      {"name":"1.2 第二与第三定律","color":"#7c3aed","desc":"熵与绝对零度","items":[
        item("la-k1-3","热力学第二定律",["def","thm"],"克劳修斯/开尔文表述，熵增原理 $dS\\ge\\delta Q/T$。","<p>孤立系统熵不减。熵 $S=k_B\\ln\\Omega$（玻尔兹曼关系）连接宏观与微观。</p>"),
        item("la-k1-4","热力学第三定律",["def","thm"],"绝对零度不可达到。","<p>能斯特定理：$T\\to0$ 时熵变 $\\Delta S\\to0$。绝对零度只能无限趋近。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"气体动理论","en":"KINETIC THEORY","sub":"理想气体、麦克斯韦分布","desc":"从微观分子运动解释宏观热性质。","sections":[
      {"name":"2.1 理想气体","color":"#0f766e","desc":"状态方程与微观解释","items":[
        item("la-k2-1","理想气体状态方程",["def","thm"],"$PV=nRT$，分子平均动能 $\\bar\\varepsilon=\\frac32 k_B T$。","<p>压强来源于分子碰撞器壁。$P=\\frac13 nm\\bar{v^2}$。温度是分子平均平动动能的度量。</p>"),
        item("la-k2-2","麦克斯韦速率分布",["def","thm"],"$f(v)=4\\pi\\left(\\frac{m}{2\\pi kT}\\right)^{3/2}v^2 e^{-mv^2/2kT}$。","<p>最概然速率 $v_p=\\sqrt{2kT/m}$，方均根速率 $v_{rms}=\\sqrt{3kT/m}$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 20. 热力学与统计物理 statistical-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"statistical-mechanics.html",
  "title":"热力学与统计物理",
  "eyebrow":"STATISTICAL MECHANICS",
  "subtitle":"系综 · 玻尔兹曼 · 配分函数 · 玻色-费米统计 · 相变",
  "meta_desc":"热力学与统计物理知识体系：系综、玻尔兹曼、配分函数、玻色费米统计、相变",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"系综理论","en":"ENSEMBLE THEORY","sub":"微正则、正则、巨正则","desc":"统计物理用系综描述系统的微观状态分布。本章介绍三大系综。","sections":[
      {"name":"1.1 系综与配分函数","color":"#2563eb","desc":"统计分布","items":[
        item("la-k1-1","微正则系综",["def","thm"],"等概率原理，孤立系统各微观态等概率。","<p>孤立系统（$N,V,E$ 固定）所有可达微观态等概率出现。熵 $S=k_B\\ln\\Omega(E,V,N)$。</p>"),
        item("la-k1-2","正则系综",["def","thm"],"$P_s\\propto e^{-\\beta E_s}$，配分函数 $Z=\\sum e^{-\\beta E_s}$。","<p>与热源接触的系统（$N,V,T$ 固定）。自由能 $F=-k_BT\\ln Z$，内能 $U=-\\partial\\ln Z/\\partial\\beta$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"量子统计","en":"QUANTUM STATISTICS","sub":"玻色、费米","desc":"全同粒子的统计：玻色-爱因斯坦与费米-狄拉克。","sections":[
      {"name":"2.1 量子分布","color":"#7c3aed","desc":"BE 与 FD 分布","items":[
        item("la-k2-1","玻色与费米分布",["def","thm"],"$f_{BE}=\\frac1{e^{\\beta(\\varepsilon-\\mu)}-1}$，$f_{FD}=\\frac1{e^{\\beta(\\varepsilon-\\mu)}+1}$。","<p>玻色子（整数自旋）服从 BE 分布，可发生玻色-爱因斯坦凝聚。费米子（半整数自旋）服从 FD 分布，满足泡利不相容。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 21. 光学 optics
# ============================================================
SUBJECTS.append({
  "filename":"optics.html",
  "title":"光学",
  "eyebrow":"OPTICS",
  "subtitle":"几何光学 · 干涉 · 衍射 · 偏振 · 傅里叶光学",
  "meta_desc":"光学知识体系：几何光学、干涉、衍射、偏振、傅里叶光学",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"几何光学","en":"GEOMETRICAL OPTICS","sub":"折射、反射、成像","desc":"光在波长可忽略时沿直线传播。本章讨论反射折射定律与成像。","sections":[
      {"name":"1.1 基本定律","color":"#2563eb","desc":"费马原理","items":[
        item("la-k1-1","反射与折射定律",["def","thm"],"$n_1\\sin\\theta_1=n_2\\sin\\theta_2$（斯涅尔定律）。","<p>费马原理：光沿光程极值路径传播。反射角等于入射角。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"波动光学","en":"WAVE OPTICS","sub":"干涉、衍射、偏振","desc":"光的波动性在干涉、衍射、偏振中显现。","sections":[
      {"name":"2.1 干涉与衍射","color":"#7c3aed","desc":"相干叠加","items":[
        item("la-k2-1","双缝干涉",["def","thm"],"明纹 $d\\sin\\theta=m\\lambda$，暗纹 $(m+1/2)\\lambda$。","<p>两相干光叠加产生明暗条纹。杨氏双缝证明光的波动性。</p>"),
        item("la-k2-2","单缝衍射",["def","thm"],"暗纹 $a\\sin\\theta=m\\lambda$，中央明纹最亮。","<p>夫琅禾费衍射用惠更斯-菲涅耳原理分析。圆孔衍射产生艾里斑，决定光学仪器分辨率。</p>"),
      ]},
      {"name":"2.2 偏振","color":"#0f766e","desc":"横波特性","items":[
        item("la-k2-3","马吕斯定律",["def","thm"],"$I=I_0\\cos^2\\theta$。","<p>线偏振光通过检偏器后强度按马吕斯定律变化。布儒斯特角下反射光完全偏振。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 22. 光学系统设计 optical-design
# ============================================================
SUBJECTS.append({
  "filename":"optical-design.html",
  "title":"光学系统设计",
  "eyebrow":"OPTICAL DESIGN",
  "subtitle":"像差理论 · 透镜设计 · 镜头组 · Zemax",
  "meta_desc":"光学系统设计知识体系：像差理论、透镜设计、镜头组、Zemax",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"像差理论","en":"ABERRATION THEORY","sub":"七种像差","desc":"实际光学系统偏离理想成像的偏差称为像差。本章讨论五类单色像差与两类色差。","sections":[
      {"name":"1.1 单色像差","color":"#2563eb","desc":"赛德尔五像差","items":[
        item("la-k1-1","球差与彗差",["def","thm"],"球差：轴上点宽光束成像不完善；彗差：轴外点不对称。","<p>球差由透镜边缘与中心焦距不同引起。彗差使轴外物点成彗星状拖尾。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"透镜组设计","en":"LENS DESIGN","sub":"组合消像差","desc":"通过多片透镜组合校正像差。","sections":[
      {"name":"2.1 组合透镜","color":"#7c3aed","desc":"消色差双胶合","items":[
        item("la-k2-1","消色差双胶合镜",["def","thm"],"正负透镜不同色散材料胶合，消去初级色差。","<p>冕牌玻璃正透镜+火石玻璃负透镜，使两种波长焦距重合。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 23. 激光原理 laser-principles
# ============================================================
SUBJECTS.append({
  "filename":"laser-principles.html",
  "title":"激光原理",
  "eyebrow":"LASER PRINCIPLES",
  "subtitle":"受激辐射 · 粒子数反转 · 光放大 · 谐振腔 · 调Q锁模",
  "meta_desc":"激光原理知识体系：受激辐射、粒子数反转、光放大、谐振腔、调Q锁模",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"光与物质相互作用","en":"LIGHT-MATTER","sub":"受激辐射、爱因斯坦系数","desc":"激光基于受激辐射。本章讨论爱因斯坦三过程与粒子数反转。","sections":[
      {"name":"1.1 受激辐射","color":"#2563eb","desc":"爱因斯坦系数","items":[
        item("la-k1-1","爱因斯坦三过程",["def","thm"],"自发辐射 $A_{21}$、受激辐射 $B_{21}\\rho(\\nu)$、受激吸收 $B_{12}\\rho(\\nu)$。","<p>受激辐射产生与入射光同频率、同相位、同方向的光子，是激光相干放大的基础。$B_{12}=B_{21}$。</p>"),
        item("la-k1-2","粒子数反转",["def","thm"],"$N_2>N_1$，光增益条件。","<p>热平衡下 $N_2<N_1$（玻尔兹曼分布）。需通过泵浦实现反转，使光通过介质被放大。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"谐振腔与激光特性","en":"CAVITY & PROPERTIES","sub":"光学谐振腔、模式","desc":"谐振腔提供正反馈与模式选择，使激光具有高方向性、单色性与相干性。","sections":[
      {"name":"2.1 谐振腔","color":"#7c3aed","desc":"法布里-珀罗腔","items":[
        item("la-k2-1","光学谐振腔",["def","thm"],"两反射镜构成，纵模频率间隔 $\\Delta\\nu=c/2L$。","<p>谐振腔选频与正反馈。增益介质+谐振腔+泵浦源构成激光器三要素。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 24. 非线性光学 nonlinear-optics
# ============================================================
SUBJECTS.append({
  "filename":"nonlinear-optics.html",
  "title":"非线性光学",
  "eyebrow":"NONLINEAR OPTICS",
  "subtitle":"极化率 · 倍频 · 和频差频 · 四波混频 · 光孤子",
  "meta_desc":"非线性光学知识体系：极化率、倍频、和频差频、四波混频、光孤子",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"非线性极化","en":"NONLINEAR POLARIZATION","sub":"极化率张量","desc":"强光下介质极化与电场呈非线性关系。本章从极化率展开出发。","sections":[
      {"name":"1.1 非线性极化率","color":"#2563eb","desc":"$P=\\epsilon_0(\\chi^{(1)}E+\\chi^{(2)}E^2+\\chi^{(3)}E^3+\\cdots)$","items":[
        item("la-k1-1","二阶与三阶非线性",["def","thm"],"$\\chi^{(2)}$ 产生倍频、和频；$\\chi^{(3)}$ 产生四波混频、克尔效应。","<p>二阶非线性需非中心对称介质。三阶非线性普遍存在，强激光下显著。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"非线性过程","en":"NONLINEAR PROCESSES","sub":"倍频、相位匹配","desc":"常见非线性光学过程及相位匹配条件。","sections":[
      {"name":"2.1 倍频与相位匹配","color":"#7c3aed","desc":"二次谐波","items":[
        item("la-k2-1","二次谐波产生",["def","thm"],"$\\omega_3=2\\omega_1$，需相位匹配 $n(\\omega_3)=n(\\omega_1)$。","<p>相位匹配保证非线性极化波与辐射波同步。利用双折射晶体的寻常/非常光折射率可调。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 25. 发光物理 luminescence
# ============================================================
SUBJECTS.append({
  "filename":"luminescence.html",
  "title":"发光物理",
  "eyebrow":"LUMINESCENCE",
  "subtitle":"电子跃迁 · 激发态 · 发光机理 · LED · 荧光磷光",
  "meta_desc":"发光物理知识体系：电子跃迁、激发态、发光机理、LED、荧光磷光",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"发光基本原理","en":"LUMINESCENCE BASICS","sub":"激发与辐射跃迁","desc":"发光是物质吸收能量后以光辐射形式释放的过程。本章讨论电子跃迁与发光类型。","sections":[
      {"name":"1.1 电子跃迁","color":"#2563eb","desc":"吸收、自发辐射、受激辐射","items":[
        item("la-k1-1","辐射跃迁",["def","thm"],"电子从激发态回到基态并发射光子 $h\\nu=E_2-E_1$。","<p>荧光（自旋允许跃迁，寿命 ns）与磷光（自旋禁阻，寿命 $\\mu$s-s）。无辐射跃迁以热形式释放能量。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"发光材料与器件","en":"MATERIALS & DEVICES","sub":"LED、激光器","desc":"半导体发光二极管与激光器的工作原理。","sections":[
      {"name":"2.1 LED 与 LD","color":"#7c3aed","desc":"电致发光","items":[
        item("la-k2-1","发光二极管 LED",["def","app"],"PN 结注入载流子复合发光，$h\\nu\\approx E_g$。","<p>LED 电光转换效率高。半导体激光器（LD）在 LED 基础上加谐振腔实现受激辐射放大。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 26. 声学 acoustics
# ============================================================
SUBJECTS.append({
  "filename":"acoustics.html",
  "title":"声学",
  "eyebrow":"ACOUSTICS",
  "subtitle":"声波方程 · 声速 · 反射折射 · 超声 · 噪声",
  "meta_desc":"声学知识体系：声波方程、声速、反射折射、超声、噪声",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"声波基本理论","en":"SOUND WAVES","sub":"波动方程、声速","desc":"声波是弹性介质中传播的机械波。本章从流体方程推导声波方程。","sections":[
      {"name":"1.1 声波方程","color":"#2563eb","desc":"小振幅声波","items":[
        item("la-k1-1","声波方程",["def","thm","der"],"$\\nabla^2 p-\\frac1{c^2}\\partial_t^2 p=0$，$c=\\sqrt{\\partial p/\\partial\\rho}$。","<p>由连续性方程、运动方程、物态方程线性化得到。空气中声速约 340 m/s。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"声学应用","en":"ACOUSTIC APPLICATIONS","sub":"超声、噪声控制","desc":"声学在成像、通信、降噪中的应用。","sections":[
      {"name":"2.1 超声与声纳","color":"#7c3aed","desc":"高频声波","items":[
        item("la-k2-1","超声成像",["def","app"],"利用回波时间与强度重建体内图像。","<p>B 超、彩超广泛用于医学。声纳利用水中声波探测目标。主动降噪利用声波相消干涉。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 27. 原子物理学 atomic-physics
# ============================================================
SUBJECTS.append({
  "filename":"atomic-physics.html",
  "title":"原子物理学",
  "eyebrow":"ATOMIC PHYSICS",
  "subtitle":"原子模型 · 玻尔理论 · 量子数 · 精细结构 · 塞曼效应",
  "meta_desc":"原子物理学知识体系：原子模型、玻尔理论、量子数、精细结构、塞曼效应",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"原子结构","en":"ATOMIC STRUCTURE","sub":"玻尔模型、量子数","desc":"从卢瑟福散射到玻尔模型，建立原子的量子化描述。","sections":[
      {"name":"1.1 玻尔模型","color":"#2563eb","desc":"氢原子能级","items":[
        item("la-k1-1","玻尔假设",["def","thm"],"定态、角动量量子化 $L=n\\hbar$、跃迁辐射 $h\\nu=E_m-E_n$。","<p>氢原子能级 $E_n=-\\frac{me^4}{8\\varepsilon_0^2 h^2 n^2}=-\\frac{13.6}{n^2}$ eV。玻尔半径 $a_0=0.529\\,\\text{\\AA}$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"量子数与精细结构","en":"QUANTUM NUMBERS","sub":"n,l,m,s 与自旋轨道耦合","desc":"原子状态由四个量子数描述。自旋轨道耦合产生精细结构。","sections":[
      {"name":"2.1 量子数","color":"#7c3aed","desc":"n,l,m_l,m_s","items":[
        item("la-k2-1","四个量子数",["def","thm"],"主量子数 $n$、角量子数 $l$、磁量子数 $m_l$、自旋 $m_s=\\pm1/2$。","<p>$l=0,1,\\dots,n-1$（s,p,d,f...），$m_l=-l,\\dots,l$。泡利不相容：每个量子态最多两个电子。</p>"),
        item("la-k2-2","自旋轨道耦合",["def","thm"],"$\\Delta E\\propto\\boldsymbol{L}\\cdot\\boldsymbol{S}$，产生精细结构。","<p>电子自旋磁矩与轨道磁场相互作用，使能级分裂为 $j=l\\pm1/2$ 两条。钠黄线双线即源于此。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"塞曼效应与跃迁","en":"ZEEMAN & TRANSITIONS","sub":"外场分裂、选择定则","desc":"外磁场下原子能级进一步分裂，产生塞曼效应。","sections":[
      {"name":"3.1 塞曼效应","color":"#0f766e","desc":"磁场中的分裂","items":[
        item("la-k3-1","塞曼效应",["def","thm"],"$\\Delta E=m_j g_j\\mu_B B$，谱线分裂。","<p>正常塞曼效应（单态，$g=1$）分裂为三条；反常塞曼效应（$S\\neq0$）分裂更复杂，需朗德 $g$ 因子。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 28. 量子力学 quantum-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"quantum-mechanics.html",
  "title":"量子力学",
  "eyebrow":"QUANTUM MECHANICS",
  "subtitle":"波函数 · 薛定谔方程 · 算符 · 表象 · 自旋 · 微扰",
  "meta_desc":"量子力学知识体系：波函数、薛定谔方程、算符、表象、自旋、微扰",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"波函数与薛定谔方程","en":"WAVE FUNCTION & SCHRÖDINGER","sub":"态叠加、概率诠释","desc":"量子力学用波函数描述系统状态，薛定谔方程支配其演化。","sections":[
      {"name":"1.1 波函数","color":"#2563eb","desc":"概率幅","items":[
        item("la-k1-1","波函数假设",["def","thm"],"$|\\psi(\\boldsymbol{r},t)|^2$ 为概率密度，$\\int|\\psi|^2d^3r=1$。","<p>波函数是概率幅，模平方给出粒子出现概率。态叠加原理：$\\psi=c_1\\psi_1+c_2\\psi_2$。</p>"),
        item("la-k1-2","薛定谔方程",["def","thm"],"$i\\hbar\\partial_t\\psi=\\hat H\\psi$，$\\hat H=-\\frac{\\hbar^2}{2m}\\nabla^2+V$。","<p>量子力学的基本运动方程。定态方程 $\\hat H\\psi=E\\psi$，解为能量本征态。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"算符与表象","en":"OPERATORS & REPRESENTATIONS","sub":"力学量算符、对易关系","desc":"力学量对应厄米算符，其本征值为测量结果。","sections":[
      {"name":"2.1 算符","color":"#7c3aed","desc":"厄米算符、对易子","items":[
        item("la-k2-1","算符假设",["def","thm"],"力学量用厄米算符表示，本征值实数，本征态正交完备。","<p>位置 $\\hat x=x$，动量 $\\hat p=-i\\hbar\\partial_x$。对易关系 $[\\hat x,\\hat p]=i\\hbar$ 是不确定关系的根源。</p>"),
        item("la-k2-2","不确定关系",["thm"],"$\\Delta x\\Delta p\\ge\\hbar/2$。","<p>对易子不为零的力学量不能同时精确测量。一般形式 $\\Delta A\\Delta B\\ge\\frac12|\\langle[A,B]\\rangle|$。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"自旋与微扰","en":"SPIN & PERTURBATION","sub":"角动量、近似方法","desc":"电子自旋是内禀角动量。微扰论处理无法精确求解的系统。","sections":[
      {"name":"3.1 自旋","color":"#0f766e","desc":"泡利矩阵","items":[
        item("la-k3-1","电子自旋",["def","thm"],"自旋 1/2，泡利矩阵 $\\sigma_x,\\sigma_y,\\sigma_z$，$[\\sigma_i,\\sigma_j]=2i\\epsilon_{ijk}\\sigma_k$。","<p>自旋角动量 $\\boldsymbol S=\\frac\\hbar2\\boldsymbol\\sigma$。自旋态是二维希尔伯特空间中的旋量。</p>"),
      ]},
      {"name":"3.2 微扰论","color":"#c2410c","desc":"近似方法","items":[
        item("la-k3-2","定态微扰",["def","thm"],"一级能量修正 $E_n^{(1)}=\\langle n|H'|n\\rangle$。","<p>哈密顿量 $H=H_0+H'$，$H'$ 为小微扰。能级与波函数可按 $H'$ 的阶数展开修正。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 29. 量子计算 quantum-computing
# ============================================================
SUBJECTS.append({
  "filename":"quantum-computing.html",
  "title":"量子计算",
  "eyebrow":"QUANTUM COMPUTING",
  "subtitle":"量子比特 · 量子门 · 量子线路 · Shor · Grover · 纠错",
  "meta_desc":"量子计算知识体系：量子比特、量子门、量子线路、Shor、Grover、纠错",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"量子比特与量子门","en":"QUBITS & GATES","sub":"叠加、纠缠、门操作","desc":"量子计算利用叠加与纠缠实现并行。本章介绍量子比特与基本量子门。","sections":[
      {"name":"1.1 量子比特","color":"#2563eb","desc":"布洛赫球","items":[
        item("la-k1-1","量子比特",["def","thm"],"$|\\psi\\rangle=\\alpha|0\\rangle+\\beta|1\\rangle$，$|\\alpha|^2+|\\beta|^2=1$。","<p>测量以 $|\\alpha|^2$ 概率得 0，$|\\beta|^2$ 得 1。多比特可纠缠，Bell 态 $|\\Phi^+\\rangle=(|00\\rangle+|11\\rangle)/\\sqrt2$。</p>"),
      ]},
      {"name":"1.2 量子门","color":"#7c3aed","desc":"幺正变换","items":[
        item("la-k1-2","基本量子门",["def","thm"],"Hadamard $H$、Pauli $X,Y,Z$、CNOT，均为幺正矩阵。","<p>量子门是幺正操作 $U$，满足 $U^\\dagger U=I$。$H|0\\rangle=(|0\\rangle+|1\\rangle)/\\sqrt2$ 产生叠加态。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"量子算法","en":"QUANTUM ALGORITHMS","sub":"Shor、Grover","desc":"量子算法在特定问题上指数或多项式超越经典。","sections":[
      {"name":"2.1 著名算法","color":"#0f766e","desc":"指数加速","items":[
        item("la-k2-1","Shor 与 Grover 算法",["thm","app"],"Shor 分解大数 $O((\\log N)^3)$；Grover 搜索 $O(\\sqrt N)$。","<p>Shor 算法用量子相位估计求周期，威胁 RSA 加密。Grover 对未排序数据库搜索提供平方加速。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 30. 原子核物理 nuclear-physics
# ============================================================
SUBJECTS.append({
  "filename":"nuclear-physics.html",
  "title":"原子核物理",
  "eyebrow":"NUCLEAR PHYSICS",
  "subtitle":"核结构 · 核力 · 衰变 · 裂变聚变 · 核模型",
  "meta_desc":"原子核物理知识体系：核结构、核力、衰变、裂变聚变、核模型",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"原子核的基本性质","en":"NUCLEAR PROPERTIES","sub":"大小、质量、结合能","desc":"原子核由质子和中子组成。本章讨论核的大小、质量与结合能。","sections":[
      {"name":"1.1 结合能","color":"#2563eb","desc":"质量亏损","items":[
        item("la-k1-1","结合能",["def","thm"],"$B=(Zm_p+Nm_n-M)c^2$，比结合能 $B/A$ 衡量核稳定性。","<p>质量亏损转化为结合能。铁 56 比结合能最大（约 8.8 MeV），是裂变与聚变的能量来源。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"核衰变与核反应","en":"DECAY & REACTIONS","sub":"α/β/γ 衰变、裂变聚变","desc":"不稳定核通过衰变释放能量。裂变与聚变释放巨大核能。","sections":[
      {"name":"2.1 衰变","color":"#7c3aed","desc":"放射性衰变","items":[
        item("la-k2-1","衰变定律",["def","thm"],"$N(t)=N_0e^{-\\lambda t}$，半衰期 $T_{1/2}=\\ln2/\\lambda$。","<p>α 衰变放出氦核，β 衰变中子转质子（或反之）并放出电子/正电子与中微子，γ 退激发射光子。</p>"),
        item("la-k2-2","裂变与聚变",["def","thm","app"],"重核裂变释放约 200 MeV；轻核聚变释放约 17.6 MeV（D-T）。","<p>裂变用于核电站与原子弹；聚变是太阳能量来源，可控聚变是能源前沿。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 31. 基础物理实验 basic-physics-lab
# ============================================================
SUBJECTS.append({
  "filename":"basic-physics-lab.html",
  "title":"基础物理实验",
  "eyebrow":"BASIC PHYSICS LAB",
  "subtitle":"误差分析 · 力学实验 · 电磁学实验 · 光学实验",
  "meta_desc":"基础物理实验知识体系：误差分析、力学实验、电磁学实验、光学实验",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"误差与数据处理","en":"ERROR ANALYSIS","sub":"误差、不确定度","desc":"实验测量不可避免有误差。本章讨论误差分类与不确定度评定。","sections":[
      {"name":"1.1 误差理论","color":"#2563eb","desc":"系统误差与随机误差","items":[
        item("la-k1-1","误差与不确定度",["def","thm"],"绝对误差 $\\Delta x$，相对误差 $E=\\Delta x/x$。","<p>系统误差可修正，随机误差用统计方法处理。标准不确定度 $u_A=\\sigma/\\sqrt n$（A 类），$u_B$ 来自仪器（B 类）。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"典型实验","en":"TYPICAL EXPERIMENTS","sub":"力、电、光","desc":"基础物理实验涵盖力学、电磁学、光学。","sections":[
      {"name":"2.1 力学与电磁学","color":"#7c3aed","desc":"常用实验","items":[
        item("la-k2-1","密立根油滴与霍尔效应",["def","app"],"测量元电荷与载流子类型浓度。","<p>密立根油滴实验测定 $e=1.602\\times10^{-19}$ C。霍尔效应测半导体载流子参数。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 32. 近代物理实验 modern-physics-lab
# ============================================================
SUBJECTS.append({
  "filename":"modern-physics-lab.html",
  "title":"近代物理实验",
  "eyebrow":"MODERN PHYSICS LAB",
  "subtitle":"卢瑟福散射 · 弗兰克-赫兹 · 光电效应 · 塞曼 · 核磁共振",
  "meta_desc":"近代物理实验知识体系：卢瑟福散射、弗兰克-赫兹、光电效应、塞曼、核磁共振",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"量子现象验证","en":"QUANTUM PHENOMENA","sub":"原子能级、量子化","desc":"近代物理实验验证微观世界的量子规律。","sections":[
      {"name":"1.1 原子能级实验","color":"#2563eb","desc":"量子化的直接证据","items":[
        item("la-k1-1","弗兰克-赫兹实验",["def","thm","his"],"汞原子能级量子化，电流随加速电压周期性下降。","<p>电子与汞原子碰撞只损失 4.9 eV，证明原子内部能量是量子化的。</p>"),
        item("la-k1-2","光电效应",["def","thm"],"$E_k=h\\nu-W$，爱因斯坦方程。","<p>光电子动能与光强无关，只与频率有关。证明光具有粒子性（光子）。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"磁共振与散射","en":"RESONANCE & SCATTERING","sub":"NMR、卢瑟福","desc":"磁共振与散射实验探索微观结构。","sections":[
      {"name":"2.1 核磁共振","color":"#7c3aed","desc":"自旋共振","items":[
        item("la-k2-1","NMR",["def","thm","app"],"共振条件 $\\hbar\\omega=\\gamma\\hbar B$，化学位移分析结构。","<p>核磁矩在磁场中能级分裂，射频共振激发。广泛用于医学成像（MRI）与化学结构分析。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 33. 固体物理 solid-state-physics
# ============================================================
SUBJECTS.append({
  "filename":"solid-state-physics.html",
  "title":"固体物理",
  "eyebrow":"SOLID STATE PHYSICS",
  "subtitle":"晶体结构 · 倒易空间 · 声子 · 能带理论 · 费米面",
  "meta_desc":"固体物理知识体系：晶体结构、倒易空间、声子、能带理论、费米面",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"晶体结构与倒易空间","en":"CRYSTAL STRUCTURE","sub":"布拉维格子、倒格子","desc":"晶体由原子周期性排列构成。本章讨论晶体结构与倒易空间。","sections":[
      {"name":"1.1 晶体结构","color":"#2563eb","desc":"周期性","items":[
        item("la-k1-1","布拉维格子",["def","thm"],"14 种布拉维格子，原胞体积 $\\Omega=\\boldsymbol a_1\\cdot(\\boldsymbol a_2\\times\\boldsymbol a_3)$。","<p>晶体结构 = 布拉维格子 + 基元。简单立方、体心立方、面心立方是常见结构。</p>"),
        item("la-k1-2","倒易空间",["def","thm"],"倒格矢 $\\boldsymbol b_i=2\\pi\\boldsymbol a_j\\times\\boldsymbol a_k/\\Omega$。","<p>倒格子与正格子互为傅里叶对偶。布里渊区是倒空间的 Wigner-Seitz 原胞。X 射线衍射条件 $\\Delta\\boldsymbol k=\\boldsymbol G$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"晶格振动与声子","en":"PHONONS","sub":"简谐近似、色散关系","desc":"原子在平衡位置附近振动，量子化为声子。","sections":[
      {"name":"2.1 声子","color":"#7c3aed","desc":"玻色子","items":[
        item("la-k2-1","声子色散",["def","thm"],"$\\omega(\\boldsymbol q)$，声学支与光学支。","<p>单原子链色散 $\\omega=\\sqrt{4K/m}|\\sin(qa/2)|$。声子是玻色子，服从玻色-爱因斯坦分布。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"能带理论","en":"BAND THEORY","sub":"布洛赫定理、自由电子","desc":"周期势中电子形成能带。本章讨论能带的形成与导体绝缘体分类。","sections":[
      {"name":"3.1 布洛赫定理","color":"#0f766e","desc":"周期势中的电子","items":[
        item("la-k3-1","布洛赫定理",["def","thm"],"$\\psi_{\\boldsymbol k}(\\boldsymbol r)=e^{i\\boldsymbol k\\cdot\\boldsymbol r}u_{\\boldsymbol k}(\\boldsymbol r)$，$u$ 周期性。","<p>周期势中电子波函数为调幅平面波。能带 $E_n(\\boldsymbol k)$ 在布里渊区内连续，带间有能隙。</p>"),
        item("la-k3-2","导体与绝缘体",["def","thm"],"能带填充决定导电性。","<p>价带全满 + 带隙大 = 绝缘体；带隙小 = 半导体；价带半满 = 导体。费米能级位置是关键。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 34. 材料物理 materials-physics
# ============================================================
SUBJECTS.append({
  "filename":"materials-physics.html",
  "title":"材料物理",
  "eyebrow":"MATERIALS PHYSICS",
  "subtitle":"晶体缺陷 · 扩散 · 相变 · 力学性能 · 功能材料",
  "meta_desc":"材料物理知识体系：晶体缺陷、扩散、相变、力学性能、功能材料",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"晶体缺陷","en":"CRYSTAL DEFECTS","sub":"点、线、面缺陷","desc":"实际晶体存在各种缺陷，决定材料性能。","sections":[
      {"name":"1.1 点缺陷与位错","color":"#2563eb","desc":"空位、间隙、位错","items":[
        item("la-k1-1","位错",["def","thm"],"刃型位错与螺型位错，柏氏矢量 $\\boldsymbol b$。","<p>位错是线缺陷，是材料塑性变形的载体。位错滑移导致屈服，位错强化（加工硬化）提高强度。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"扩散与相变","en":"DIFFUSION & PHASE","sub":"菲克定律、成核生长","desc":"原子扩散与相变是材料制备的基础。","sections":[
      {"name":"2.1 扩散","color":"#7c3aed","desc":"菲克定律","items":[
        item("la-k2-1","菲克定律",["def","thm"],"$J=-D\\partial c/\\partial x$，$\\partial c/\\partial t=D\\partial^2 c/\\partial x^2$。","<p>扩散系数 $D=D_0e^{-Q/RT}$，温度依赖显著。扩散控制固相反应与相变动力学。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 35. 超导物理 superconductivity
# ============================================================
SUBJECTS.append({
  "filename":"superconductivity.html",
  "title":"超导物理",
  "eyebrow":"SUPERCONDUCTIVITY",
  "subtitle":"零电阻 · 迈斯纳效应 · BCS · 高温超导 · 约瑟夫森",
  "meta_desc":"超导物理知识体系：零电阻、迈斯纳效应、BCS、高温超导、约瑟夫森",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"超导基本现象","en":"SUPERCONDUCTING PHENOMENA","sub":"零电阻、迈斯纳","desc":"超导体在临界温度下电阻消失并排斥磁通。","sections":[
      {"name":"1.1 零电阻与迈斯纳","color":"#2563eb","desc":"超导态特征","items":[
        item("la-k1-1","迈斯纳效应",["def","thm"],"$\\boldsymbol B=0$ 内部，完全抗磁性。","<p>超导体不仅零电阻，还将内部磁场完全排出（迈斯纳效应），这是独立于零电阻的特征。$T<T_c$ 时发生。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"BCS 理论","en":"BCS THEORY","sub":"库珀对、能隙","desc":"BCS 理论解释常规超导：电子配对形成库珀对。","sections":[
      {"name":"2.1 库珀对","color":"#7c3aed","desc":"电子-声子相互作用","items":[
        item("la-k2-1","BCS 理论",["def","thm"],"电子通过声子交换形成库珀对，凝聚为超导基态。","<p>库珀对（自旋相反、动量相反）是玻色子，发生玻色凝聚。能隙 $\\Delta\\approx1.76k_BT_c$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 36. 纳米物理 nanophysics
# ============================================================
SUBJECTS.append({
  "filename":"nanophysics.html",
  "title":"纳米物理",
  "eyebrow":"NANOPHYSICS",
  "subtitle":"量子限域 · 量子点 · 碳纳米管 · 石墨烯 · 纳米器件",
  "meta_desc":"纳米物理知识体系：量子限域、量子点、碳纳米管、石墨烯、纳米器件",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"量子限域效应","en":"QUANTUM CONFINEMENT","sub":"低维材料、态密度","desc":"当材料尺寸缩小到纳米量级，量子效应主导性质。","sections":[
      {"name":"1.1 低维体系","color":"#2563eb","desc":"0D、1D、2D","items":[
        item("la-k1-1","量子限域",["def","thm"],"能隙随尺寸减小而增大，$\\Delta E\\propto1/L^2$。","<p>三维块体→二维量子阱→一维量子线→零维量子点。态密度从连续变为离散。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 37. 拓扑物态 topological-matter
# ============================================================
SUBJECTS.append({
  "filename":"topological-matter.html",
  "title":"拓扑物态",
  "eyebrow":"TOPOLOGICAL MATTER",
  "subtitle":"拓扑绝缘体 · 拓扑半金属 · 陈数 · 边缘态",
  "meta_desc":"拓扑物态知识体系：拓扑绝缘体、拓扑半金属、陈数、边缘态",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"拓扑绝缘体","en":"TOPOLOGICAL INSULATORS","sub":"体绝缘、表面金属","desc":"拓扑绝缘体体内绝缘，表面存在受拓扑保护的金属态。","sections":[
      {"name":"1.1 拓扑不变量","color":"#2563eb","desc":"陈数、Z2 不变量","items":[
        item("la-k1-1","陈数",["def","thm"],"$C=\\frac1{2\\pi}\\int_{BZ}\\boldsymbol F\\cdot d\\boldsymbol S$，整数。","<p>陈数刻画能带的拓扑性质。非零陈数对应量子霍尔态，边缘态数目等于陈数。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 38. 二维材料 2d-materials
# ============================================================
SUBJECTS.append({
  "filename":"2d-materials.html",
  "title":"二维材料",
  "eyebrow":"2D MATERIALS",
  "subtitle":"石墨烯 · MoS2 · 黑磷 · 异质结 · 器件",
  "meta_desc":"二维材料知识体系：石墨烯、MoS2、黑磷、异质结、器件",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"石墨烯","en":"GRAPHENE","sub":"零带隙半导体、相对论性电子","desc":"石墨烯是单层碳原子构成的二维材料，电子呈狄拉克费米子行为。","sections":[
      {"name":"1.1 石墨烯电子结构","color":"#2563eb","desc":"狄拉克锥","items":[
        item("la-k1-1","石墨烯能带",["def","thm"],"线性色散 $E=\\pm\\hbar v_F|\\boldsymbol k|$，$v_F\\approx c/300$。","<p>K 点附近电子行为如无质量狄拉克费米子。载流子迁移率极高，室温弹道输运。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 39. 低温物理 low-temperature-physics
# ============================================================
SUBJECTS.append({
  "filename":"low-temperature-physics.html",
  "title":"低温物理",
  "eyebrow":"LOW TEMPERATURE PHYSICS",
  "subtitle":"液氦 · 超流 · 玻色-爱因斯坦凝聚 · 极低温技术",
  "meta_desc":"低温物理知识体系：液氦、超流、玻色爱因斯坦凝聚、极低温技术",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"液氦与超流","en":"HELIUM & SUPERFLUIDITY","sub":"相变、超流","desc":"液氦在低温下发生超流相变，展现宏观量子现象。","sections":[
      {"name":"1.1 超流","color":"#2563eb","desc":"He II","items":[
        item("la-k1-1","超流 He II",["def","thm"],"$T<2.17$ K 时 He-4 超流，零粘滞、熵为零。","<p>超流是玻色-爱因斯坦凝聚的宏观表现。二流体模型：正常流体 + 超流体组分。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 40. 材料制备技术 materials-preparation
# ============================================================
SUBJECTS.append({
  "filename":"materials-preparation.html",
  "title":"材料制备技术",
  "eyebrow":"MATERIALS PREPARATION",
  "subtitle":"烧结 · 薄膜沉积 · 单晶生长 · CVD · MBE",
  "meta_desc":"材料制备技术知识体系：烧结、薄膜沉积、单晶生长、CVD、MBE",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"薄膜与单晶生长","en":"THIN FILMS & CRYSTALS","sub":"CVD、PVD、MBE","desc":"薄膜制备是半导体与材料科学的核心工艺。","sections":[
      {"name":"1.1 气相沉积","color":"#2563eb","desc":"CVD 与 MBE","items":[
        item("la-k1-1","化学气相沉积 CVD",["def","app"],"气相化学反应在基片上沉积薄膜。","<p>CVD 利用前驱体气体在加热基片上反应沉积。分子束外延 MBE 精度达单原子层，用于高质量半导体异质结。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 41. 材料测试技术 materials-characterization
# ============================================================
SUBJECTS.append({
  "filename":"materials-characterization.html",
  "title":"材料测试技术",
  "eyebrow":"MATERIALS CHARACTERIZATION",
  "subtitle":"XRD · SEM · TEM · AFM · XPS · Raman",
  "meta_desc":"材料测试技术知识体系：XRD、SEM、TEM、AFM、XPS、Raman",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"结构表征","en":"STRUCTURAL","sub":"XRD、TEM","desc":"X 射线衍射与电子显微术分析材料结构。","sections":[
      {"name":"1.1 XRD 与电子显微","color":"#2563eb","desc":"晶体结构与形貌","items":[
        item("la-k1-1","X 射线衍射",["def","thm","app"],"布拉格方程 $2d\\sin\\theta=n\\lambda$。","<p>XRD 测定晶体结构、晶格常数、物相。TEM 可达原子分辨率，分析形貌与晶体结构。SEM 观察表面形貌。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 42. 半导体物理 semiconductor-physics
# ============================================================
SUBJECTS.append({
  "filename":"semiconductor-physics.html",
  "title":"半导体物理",
  "eyebrow":"SEMICONDUCTOR PHYSICS",
  "subtitle":"能带 · 载流子 · 掺杂 · PN 结 · MOS · 输运",
  "meta_desc":"半导体物理知识体系：能带、载流子、掺杂、PN结、MOS、输运",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"半导体能带与载流子","en":"BANDS & CARRIERS","sub":"本征、掺杂、载流子浓度","desc":"半导体的导电性由能带与载流子决定。本章讨论本征与掺杂半导体。","sections":[
      {"name":"1.1 载流子浓度","color":"#2563eb","desc":"本征与非本征","items":[
        item("la-k1-1","载流子浓度",["def","thm"],"$n_i=\\sqrt{N_cN_v}e^{-E_g/2kT}$，$n_0p_0=n_i^2$。","<p>本征载流子浓度 $n_i$ 由带隙 $E_g$ 决定。掺杂引入施主/受主，改变费米能级与多数载流子浓度。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"PN 结与 MOS","en":"PN JUNCTION & MOS","sub":"耗尽层、能带弯曲","desc":"PN 结是半导体器件的核心。MOS 结构是现代晶体管基础。","sections":[
      {"name":"2.1 PN 结","color":"#7c3aed","desc":"整流特性","items":[
        item("la-k2-1","PN 结 I-V",["def","thm"],"$I=I_0(e^{qV/kT}-1)$，肖克莱方程。","<p>正向偏置注入少数载流子，电流指数增长；反向偏置电流几乎为零（击穿除外）。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 43. 半导体材料 semiconductor-materials
# ============================================================
SUBJECTS.append({
  "filename":"semiconductor-materials.html",
  "title":"半导体材料",
  "eyebrow":"SEMICONDUCTOR MATERIALS",
  "subtitle":"硅 · 锗 · 砷化镓 · 氮化镓 · 碳化硅",
  "meta_desc":"半导体材料知识体系：硅、锗、砷化镓、氮化镓、碳化硅",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"半导体材料分类","en":"SEMICONDUCTOR MATERIALS","sub":"元素、化合物、宽禁带","desc":"半导体材料分元素半导体与化合物半导体。","sections":[
      {"name":"1.1 元素与化合物半导体","color":"#2563eb","desc":"Si、GaAs、GaN","items":[
        item("la-k1-1","材料代际",["def","thm","app"],"Si 第一代，GaAs 第二代，GaN/SiC 第三代（宽禁带）。","<p>Si 工艺成熟用于逻辑；GaAs 高频高速；GaN/SiC 宽禁带用于大功率、高频、光电器件。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 44. 半导体器件 semiconductor-devices
# ============================================================
SUBJECTS.append({
  "filename":"semiconductor-devices.html",
  "title":"半导体器件",
  "eyebrow":"SEMICONDUCTOR DEVICES",
  "subtitle":"二极管 · BJT · MOSFET · HEMT · 光电探测器",
  "meta_desc":"半导体器件知识体系：二极管、BJT、MOSFET、HEMT、光电探测器",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"晶体管器件","en":"TRANSISTORS","sub":"BJT、MOSFET","desc":"晶体管是电子电路的核心放大与开关器件。","sections":[
      {"name":"1.1 MOSFET","color":"#2563eb","desc":"场效应晶体管","items":[
        item("la-k1-1","MOSFET 工作原理",["def","thm"],"栅压调制沟道，$I_D$ 分线性区与饱和区。","<p>MOSFET 是数字集成电路的基本单元。亚阈值摆幅 S 决定关断电流，是低功耗设计关键。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 45. 半导体工艺 semiconductor-process
# ============================================================
SUBJECTS.append({
  "filename":"semiconductor-process.html",
  "title":"半导体工艺",
  "eyebrow":"SEMICONDUCTOR PROCESS",
  "subtitle":"光刻 · 刻蚀 · 离子注入 · 薄膜沉积 · CMP · 封装",
  "meta_desc":"半导体工艺知识体系：光刻、刻蚀、离子注入、薄膜沉积、CMP、封装",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"前道工艺","en":"FRONT-END","sub":"光刻、刻蚀、注入","desc":"前道工艺在晶圆上制造晶体管。","sections":[
      {"name":"1.1 光刻与刻蚀","color":"#2563eb","desc":"图形转移","items":[
        item("la-k1-1","光刻",["def","app"],"曝光+显影将掩模图形转移到光刻胶。","<p>EUV 光刻（13.5 nm）是先进节点关键。刻蚀（干法/湿法）将图形转移到薄膜。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 46. 相对论 relativity
# ============================================================
SUBJECTS.append({
  "filename":"relativity.html",
  "title":"相对论",
  "eyebrow":"RELATIVITY",
  "subtitle":"狭义相对论 · 时空图 · 广义相对论 · 引力波",
  "meta_desc":"相对论知识体系：狭义相对论、时空图、广义相对论、引力波",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"狭义相对论","en":"SPECIAL RELATIVITY","sub":"洛伦兹变换、时空","desc":"狭义相对论基于光速不变与相对性原理，统一时空。","sections":[
      {"name":"1.1 洛伦兹变换","color":"#2563eb","desc":"时空坐标变换","items":[
        item("la-k1-1","洛伦兹变换",["def","thm"],"$x'=\\gamma(x-vt)$，$t'=\\gamma(t-vx/c^2)$，$\\gamma=1/\\sqrt{1-v^2/c^2}$。","<p>同时性相对。钟慢效应 $\\Delta t'=\\gamma\\Delta t$，尺缩效应 $L'=L/\\gamma$。质能关系 $E=mc^2$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"广义相对论","en":"GENERAL RELATIVITY","sub":"时空弯曲、爱因斯坦方程","desc":"引力是时空弯曲的几何效应。","sections":[
      {"name":"2.1 爱因斯坦场方程","color":"#7c3aed","desc":"几何即引力","items":[
        item("la-k2-1","场方程",["def","thm"],"$G_{\\mu\\nu}+\\Lambda g_{\\mu\\nu}=\\frac{8\\pi G}{c^4}T_{\\mu\\nu}$。","<p>左边爱因斯坦张量 $G_{\\mu\\nu}=R_{\\mu\\nu}-\\frac12 Rg_{\\mu\\nu}$ 描述时空曲率，右边能量动量张量描述物质。物质告诉时空如何弯曲，时空告诉物质如何运动。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 47. 宇宙学 cosmology
# ============================================================
SUBJECTS.append({
  "filename":"cosmology.html",
  "title":"宇宙学",
  "eyebrow":"COSMOLOGY",
  "subtitle":"大爆炸 · 膨胀 · CMB · 暗物质 · 暗能量",
  "meta_desc":"宇宙学知识体系：大爆炸、膨胀、CMB、暗物质、暗能量",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"膨胀宇宙","en":"EXPANDING UNIVERSE","sub":"哈勃定律、弗里德曼方程","desc":"宇宙在膨胀，起源于大爆炸。本章讨论宇宙学基本方程。","sections":[
      {"name":"1.1 弗里德曼方程","color":"#2563eb","desc":"宇宙动力学","items":[
        item("la-k1-1","弗里德曼方程",["def","thm"],"$\\left(\\frac{\\dot a}{a}\\right)^2=\\frac{8\\pi G}{3}\\rho-\\frac{kc^2}{a^2}+\\frac{\\Lambda c^2}{3}$。","<p>尺度因子 $a(t)$ 描述宇宙膨胀。$\\rho$ 为物质能量密度，$k$ 为空间曲率，$\\Lambda$ 为宇宙学常数（暗能量）。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"热大爆炸","en":"HOT BIG BANG","sub":"CMB、核合成","desc":"早期宇宙炽热致密，经历核合成与复合，留下微波背景辐射。","sections":[
      {"name":"2.1 CMB 与核合成","color":"#7c3aed","desc":"早期宇宙遗迹","items":[
        item("la-k2-1","宇宙微波背景",["def","thm","his"],"$T\\approx2.725$ K 黑体谱，各向异性 $\\sim10^{-5}$。","<p>CMB 是复合期（$z\\sim1100$）光子自由传播至今的遗迹，是大爆炸的直接证据。原初核合成预言轻元素丰度与观测一致。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 48. 黑洞物理 black-hole-physics
# ============================================================
SUBJECTS.append({
  "filename":"black-hole-physics.html",
  "title":"黑洞物理",
  "eyebrow":"BLACK HOLE PHYSICS",
  "subtitle":"事件视界 · 史瓦西解 · 霍金辐射 · 黑洞热力学",
  "meta_desc":"黑洞物理知识体系：事件视界、史瓦西解、霍金辐射、黑洞热力学",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"黑洞解","en":"BLACK HOLE SOLUTIONS","sub":"史瓦西、克尔","desc":"广义相对论预言黑洞。本章讨论经典黑洞解与事件视界。","sections":[
      {"name":"1.1 史瓦西黑洞","color":"#2563eb","desc":"球对称黑洞","items":[
        item("la-k1-1","史瓦西半径",["def","thm"],"$r_s=\\frac{2GM}{c^2}$，事件视界。","<p>史瓦西度规在 $r=r_s$ 处坐标奇异性即视界。黑洞无毛：仅由质量、电荷、角动量描述。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"霍金辐射与热力学","en":"HAWKING & THERMODYNAMICS","sub":"量子黑洞","desc":"黑洞具有温度与熵，通过霍金辐射蒸发。","sections":[
      {"name":"2.1 霍金辐射","color":"#7c3aed","desc":"量子效应","items":[
        item("la-k2-1","霍金温度",["def","thm"],"$T_H=\\frac{\\hbar c^3}{8\\pi GMk_B}$，黑洞熵 $S=\\frac{k_B c^3 A}{4\\hbar G}$。","<p>视界附近虚粒子对中负能粒子落入黑洞，正能粒子逃逸形成热辐射。贝肯斯坦-霍金熵与视界面积成正比。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 49. 粒子物理 particle-physics
# ============================================================
SUBJECTS.append({
  "filename":"particle-physics.html",
  "title":"粒子物理",
  "eyebrow":"PARTICLE PHYSICS",
  "subtitle":"夸克 · 轻子 · 规范玻色子 · 标准模型 · 希格斯",
  "meta_desc":"粒子物理知识体系：夸克、轻子、规范玻色子、标准模型、希格斯",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"基本粒子","en":"FUNDAMENTAL PARTICLES","sub":"三代费米子","desc":"物质由三代夸克与轻子构成，相互作用由规范玻色子传递。","sections":[
      {"name":"1.1 标准模型粒子","color":"#2563eb","desc":"费米子与玻色子","items":[
        item("la-k1-1","标准模型",["def","thm"],"6 夸克 + 6 轻子 + 4 规范玻色子 + 希格斯。","<p>三代夸克（u/d, c/s, t/b）与三代轻子（e/νe, μ/νμ, τ/ντ）。光子、W/Z、胶子传递电磁、弱、强相互作用。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"相互作用","en":"INTERACTIONS","sub":"电弱统一、QCD","desc":"四种基本相互作用中，电磁与弱力已统一为电弱相互作用。","sections":[
      {"name":"2.1 电弱与强相互作用","color":"#7c3aed","desc":"规范理论","items":[
        item("la-k2-1","希格斯机制",["def","thm","his"],"自发对称破缺赋予 W/Z 质量。","<p>希格斯场真空期望值破缺 $SU(2)_L\\times U(1)_Y\\to U(1)_{EM}$，使 W/Z 获得质量，光子保持无质量。2012 年 LHC 发现希格斯玻色子。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 50. 规范场论 gauge-theory
# ============================================================
SUBJECTS.append({
  "filename":"gauge-theory.html",
  "title":"规范场论",
  "eyebrow":"GAUGE THEORY",
  "subtitle":"规范对称性 · Yang-Mills · 自发破缺 · 重整化",
  "meta_desc":"规范场论知识体系：规范对称性、Yang-Mills、自发破缺、重整化",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"规范对称性","en":"GAUGE SYMMETRY","sub":"局域对称、规范场","desc":"规范场论以局域对称性为基础，杨-米尔斯理论是非阿贝尔规范场的核心。","sections":[
      {"name":"1.1 Yang-Mills 理论","color":"#2563eb","desc":"非阿贝尔规范场","items":[
        item("la-k1-1","规范协变导数",["def","thm"],"$D_\\mu=\\partial_\\mu-ig A_\\mu^a T^a$，场强 $F_{\\mu\\nu}^a=\\partial_\\mu A_\\nu^a-\\partial_\\nu A_\\mu^a+gf^{abc}A_\\mu^bA_\\nu^c$。","<p>要求拉氏量在局域规范变换 $\\psi\\to U\\psi$ 下不变，需引入规范场 $A_\\mu$。非阿贝尔项 $f^{abc}A^bA^c$ 使规范场自相互作用。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 51. 量子场论 quantum-field-theory
# ============================================================
SUBJECTS.append({
  "filename":"quantum-field-theory.html",
  "title":"量子场论",
  "eyebrow":"QUANTUM FIELD THEORY",
  "subtitle":"正则量子化 · 路径积分 · 费曼图 · 重整化",
  "meta_desc":"量子场论知识体系：正则量子化、路径积分、费曼图、重整化",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"场的量子化","en":"QUANTIZATION","sub":"正则、路径积分","desc":"将场视为无穷多简谐振子的集合并量子化。","sections":[
      {"name":"1.1 正则量子化","color":"#2563eb","desc":"产生湮灭算符","items":[
        item("la-k1-1","标量场量子化",["def","thm"],"$\\phi(\\boldsymbol x,t)=\\int\\frac{d^3k}{(2\\pi)^3}\\frac1{\\sqrt{2\\omega_k}}(a_ke^{-ikx}+a_k^\\dagger e^{ikx})$。","<p>$a_k$ 湮灭一个动量 $\\boldsymbol k$ 的粒子，$a_k^\\dagger$ 产生。对易关系 $[a_k,a_{k'}^\\dagger]=(2\\pi)^3\\delta^3(\\boldsymbol k-\\boldsymbol k')$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"费曼图与重整化","en":"FEYNMAN & RENORMALIZATION","sub":"微扰论、紫外发散","desc":"用费曼图计算散射振幅，重整化消除紫外发散。","sections":[
      {"name":"2.1 费曼图","color":"#7c3aed","desc":"微扰展开","items":[
        item("la-k2-1","费曼规则",["def","thm","app"],"每个顶点对应耦合常数，内线对应传播子。","<p>S 矩阵 $\\langle f|S|i\\rangle$ 展开为费曼图级数。费曼图是直观的微扰计算工具，QED 计算精度达 $10^{-10}$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 52. 弦理论 string-theory
# ============================================================
SUBJECTS.append({
  "filename":"string-theory.html",
  "title":"弦理论",
  "eyebrow":"STRING THEORY",
  "subtitle":"弦振动 · 10维时空 · 超对称 · D膜 · M理论",
  "meta_desc":"弦理论知识体系：弦振动、10维时空、超对称、D膜、M理论",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"玻色弦与超弦","en":"BOSONIC & SUPERSTRINGS","sub":"弦的量子化","desc":"基本粒子是一维弦的不同振动模式。","sections":[
      {"name":"1.1 弦的振动谱","color":"#2563eb","desc":"质量来自振动","items":[
        item("la-k1-1","弦量子化",["def","thm"],"自洽要求 $D=26$（玻色弦）或 $D=10$（超弦）。","<p>弦的不同振动模式对应不同粒子。量子反常相消要求特定时空维数。超弦引入超对称，消除快子。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 53. 量子引力 quantum-gravity
# ============================================================
SUBJECTS.append({
  "filename":"quantum-gravity.html",
  "title":"量子引力",
  "eyebrow":"QUANTUM GRAVITY",
  "subtitle":"圈量子引力 · 自旋网络 · 渐近安全 · 正则量子化",
  "meta_desc":"量子引力知识体系：圈量子引力、自旋网络、渐近安全、正则量子化",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"量子引力途径","en":"APPROACHES","sub":"圈量子引力","desc":"统一量子力学与广义相对论是物理学终极问题。","sections":[
      {"name":"1.1 圈量子引力","color":"#2563eb","desc":"背景无关量子化","items":[
        item("la-k1-1","自旋网络",["def","thm"],"空间由自旋网络描述，面积与体积离散。","<p>圈量子引力以联络为基本变量，用自旋网络离散几何。预言普朗克尺度的时空量子结构，大爆炸可能为大反弹。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 54. 共形场论 conformal-field-theory
# ============================================================
SUBJECTS.append({
  "filename":"conformal-field-theory.html",
  "title":"共形场论",
  "eyebrow":"CONFORMAL FIELD THEORY",
  "subtitle":"共形对称性 · 算子积展开 · 中心荷 · 临界点",
  "meta_desc":"共形场论知识体系：共形对称性、算子积展开、中心荷、临界点",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"共形对称性","en":"CONFORMAL SYMMETRY","sub":"标度不变、共形群","desc":"共形场论在标度变换下不变，描述临界现象。","sections":[
      {"name":"1.1 二维 CFT","color":"#2563eb","desc":"Virasoro 代数","items":[
        item("la-k1-1","中心荷",["def","thm"],"Virasoro 代数 $[L_m,L_n]=(m-n)L_{m+n}+\\frac c{12}m(m^2-1)\\delta_{m+n}$。","<p>二维共形群无限维，给出严格约束。中心荷 $c$ 是 CFT 的基本参数，自由玻色子 $c=1$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 55. 拓扑量子场论 tqft
# ============================================================
SUBJECTS.append({
  "filename":"tqft.html",
  "title":"拓扑量子场论",
  "eyebrow":"TOPOLOGICAL QFT",
  "subtitle":"拓扑不变量 · TQFT · 拓扑序 · 量子计算",
  "meta_desc":"拓扑量子场论知识体系：拓扑不变量、TQFT、拓扑序、量子计算",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"TQFT 基础","en":"TQFT BASICS","sub":"流形不变量","desc":"拓扑量子场论的相关函数只依赖流形拓扑。","sections":[
      {"name":"1.1 拓扑不变量","color":"#2563eb","desc":"与度量无关","items":[
        item("la-k1-1","TQFT 定义",["def","thm"],"配分函数 $Z(M)$ 是流形 $M$ 的拓扑不变量。","<p>TQFT 的作用量不含度规，关联函数在同胚下不变。Chern-Simons 理论是典型三维 TQFT，与纽结不变量（Jones 多项式）相关。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 56. 天体物理学 astrophysics
# ============================================================
SUBJECTS.append({
  "filename":"astrophysics.html",
  "title":"天体物理学",
  "eyebrow":"ASTROPHYSICS",
  "subtitle":"恒星结构 · 恒星演化 · 星系动力学 · 活动星系核",
  "meta_desc":"天体物理学知识体系：恒星结构、恒星演化、星系动力学、活动星系核",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"恒星结构与演化","en":"STELLAR STRUCTURE","sub":"流体静力学平衡、核反应","desc":"恒星是自引力流体球，核反应提供能量。本章讨论恒星结构方程与演化。","sections":[
      {"name":"1.1 恒星结构方程","color":"#2563eb","desc":"流体静力学平衡","items":[
        item("la-k1-1","流体静力学平衡",["def","thm"],"$\\frac{dP}{dr}=-\\frac{GM(r)\\rho}{r^2}$。","<p>压强梯度抵抗引力。质量连续性 $dM/dr=4\\pi r^2\\rho$。能量传输有辐射与对流两种。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"恒星演化","en":"STELLAR EVOLUTION","sub":"主序、红巨星、超新星","desc":"恒星一生由质量决定，从原恒星到主序，最终白矮星/中子星/黑洞。","sections":[
      {"name":"2.1 演化终点","color":"#7c3aed","desc":"致密星","items":[
        item("la-k2-1","钱德拉塞卡极限",["def","thm"],"白矮星最大质量 $\\sim1.4M_\\odot$，中子星约 $2-3M_\\odot$。","<p>超过钱德拉塞卡极限电子简并压不足以支撑，形成中子星或黑洞。超新星爆发是大质量恒星的壮丽终局。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 57. 等离子体物理 plasma-physics
# ============================================================
SUBJECTS.append({
  "filename":"plasma-physics.html",
  "title":"等离子体物理",
  "eyebrow":"PLASMA PHYSICS",
  "subtitle":"等离子体 · 德拜屏蔽 · 朗缪尔波 · 磁约束 · 不稳定性",
  "meta_desc":"等离子体物理知识体系：等离子体、德拜屏蔽、朗缪尔波、磁约束、不稳定性",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"等离子体基本性质","en":"PLASMA BASICS","sub":"德拜长度、等离子体频率","desc":"等离子体是电离气体，是物质第四态。本章讨论其集体行为。","sections":[
      {"name":"1.1 德拜屏蔽与振荡","color":"#2563eb","desc":"集体效应","items":[
        item("la-k1-1","德拜长度",["def","thm"],"$\\lambda_D=\\sqrt{\\varepsilon_0 kT_e/(ne^2)}$，屏蔽外部电场。","<p>等离子体在大于德拜长度的尺度上呈准中性。等离子体频率 $\\omega_p=\\sqrt{ne^2/(\\varepsilon_0 m_e)}$ 是高频静电振荡频率。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 58. 生物物理 biophysics
# ============================================================
SUBJECTS.append({
  "filename":"biophysics.html",
  "title":"生物物理",
  "eyebrow":"BIOPHYSICS",
  "subtitle":"蛋白质折叠 · DNA力学 · 分子马达 · 膜生物物理",
  "meta_desc":"生物物理知识体系：蛋白质折叠、DNA力学、分子马达、膜生物物理",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"生物大分子物理","en":"BIOMACROMOLECULES","sub":"蛋白质、DNA","desc":"用物理方法研究生物大分子的结构与功能。","sections":[
      {"name":"1.1 蛋白质折叠","color":"#2563eb","desc":"能量地形","items":[
        item("la-k1-1","蛋白质折叠",["def","thm"],"氨基酸序列决定三维结构（Anfinsen 原理）。","<p>蛋白质从随机卷曲折叠到天然态，遵循能量地形漏斗模型。分子伴侣协助折叠，错误折叠导致神经退行性疾病。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 59. 辐射过程 radiation-processes
# ============================================================
SUBJECTS.append({
  "filename":"radiation-processes.html",
  "title":"辐射过程",
  "eyebrow":"RADIATION PROCESSES",
  "subtitle":"同步辐射 · 轫致辐射 · 切伦科夫辐射 · 黑体辐射",
  "meta_desc":"辐射过程知识体系：同步辐射、轫致辐射、切伦科夫辐射、黑体辐射",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"带电粒子辐射","en":"RADIATION BY CHARGES","sub":"加速电荷辐射","desc":"加速的带电粒子必然辐射电磁波。本章讨论各种辐射机制。","sections":[
      {"name":"1.1 辐射机制","color":"#2563eb","desc":"同步、轫致、切伦科夫","items":[
        item("la-k1-1","同步辐射",["def","thm"],"相对论电子在磁场中做圆周运动发出的辐射。","<p>同步辐射高亮度、宽谱、高偏振，是重要光源。轫致辐射是带电粒子在库仑场中减速产生。切伦科夫辐射是粒子超介质光速时的锥形辐射。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 60. 核聚变物理 fusion-physics
# ============================================================
SUBJECTS.append({
  "filename":"fusion-physics.html",
  "title":"核聚变物理",
  "eyebrow":"FUSION PHYSICS",
  "subtitle":"聚变反应 · 劳逊判据 · 托卡马克 · 仿星器 · 惯性约束",
  "meta_desc":"核聚变物理知识体系：聚变反应、劳逊判据、托卡马克、仿星器、惯性约束",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"聚变原理","en":"FUSION PRINCIPLES","sub":"D-T反应、劳逊判据","desc":"轻核聚变释放巨大能量，是太阳的能量来源。本章讨论聚变原理与约束方案。","sections":[
      {"name":"1.1 聚变反应与条件","color":"#2563eb","desc":"高温、高密度、长约束","items":[
        item("la-k1-1","劳逊判据",["def","thm"],"$n\\tau_E\\ge 10^{14}\\,\\text{cm}^{-3}\\cdot\\text{s}$（D-T，$T\\sim10^8$ K）。","<p>D-T 反应 $\\text{D}+\\text{T}\\to\\alpha(3.5\\text{MeV})+n(14.1\\text{MeV})$。劳逊判据给出能量得失相当的密度-约束时间乘积。三重积 $nT\\tau_E$ 是聚变装置的核心指标。</p>"),
      ]},
    ]},
  ]
})

print("Total subjects defined:", len(SUBJECTS))
for s in SUBJECTS:
    write_subject(s)
print(f"\nDone! Generated {len(SUBJECTS)} subject pages.")
