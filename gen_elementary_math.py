# -*- coding: utf-8 -*-
"""Generate elementary-math.html with 8 chapters: 集合与逻辑/代数/函数/数列/平面几何/立体几何/解析几何/概率统计."""
import json

FIG = {
"set_venn": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="220" height="140" fill="#f8fafc" stroke="#cbd5e1" rx="10"/>
<text x="18" y="28" font-size="11" fill="#64748b">U（全集）</text>
<circle cx="92" cy="86" r="48" fill="#dbeafe" fill-opacity="0.6" stroke="#2563eb" stroke-width="1.5"/>
<circle cx="148" cy="86" r="48" fill="#ede9fe" fill-opacity="0.6" stroke="#7c3aed" stroke-width="1.5"/>
<text x="62" y="86" font-size="12" fill="#1e40af" font-weight="bold">A</text>
<text x="168" y="86" font-size="12" fill="#6d28d9" font-weight="bold">B</text>
<text x="108" y="90" font-size="10" fill="#475569">A∩B</text>
</svg>''',
"quadratic": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="120" y1="20" x2="120" y2="140" stroke="#475569" stroke-width="1.2"/>
<path d="M 40 110 Q 120 20 200 110" fill="none" stroke="#2563eb" stroke-width="2"/>
<circle cx="120" cy="50" r="3" fill="#ef4444"/>
<line x1="120" y1="50" x2="120" y2="130" stroke="#ef4444" stroke-width="1" stroke-dasharray="3 3"/>
<text x="124" y="48" font-size="10" fill="#ef4444">顶点</text>
<text x="208" y="124" font-size="10" fill="#475569">x</text>
<text x="110" y="18" font-size="10" fill="#475569">y</text>
</svg>''',
"func_mapping": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="55" cy="80" rx="38" ry="50" fill="#dbeafe" fill-opacity="0.5" stroke="#2563eb"/>
<ellipse cx="185" cy="80" rx="38" ry="50" fill="#dcfce7" fill-opacity="0.5" stroke="#16a34a"/>
<text x="40" y="18" font-size="11" fill="#1e40af" font-weight="bold">定义域 A</text>
<text x="168" y="18" font-size="11" fill="#15803d" font-weight="bold">值域 B</text>
<circle cx="55" cy="50" r="3" fill="#2563eb"/><text x="62" y="54" font-size="10" fill="#2563eb">x1</text>
<circle cx="55" cy="80" r="3" fill="#2563eb"/><text x="62" y="84" font-size="10" fill="#2563eb">x2</text>
<circle cx="55" cy="110" r="3" fill="#2563eb"/><text x="62" y="114" font-size="10" fill="#2563eb">x3</text>
<circle cx="185" cy="60" r="3" fill="#16a34a"/><text x="194" y="64" font-size="10" fill="#16a34a">y1</text>
<circle cx="185" cy="100" r="3" fill="#16a34a"/><text x="194" y="104" font-size="10" fill="#16a34a">y2</text>
<line x1="58" y1="50" x2="182" y2="60" stroke="#f59e0b" stroke-width="1.3" marker-end="url(#arr)"/>
<line x1="58" y1="80" x2="182" y2="60" stroke="#f59e0b" stroke-width="1.3"/>
<line x1="58" y1="110" x2="182" y2="100" stroke="#f59e0b" stroke-width="1.3"/>
<defs><marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#f59e0b"/></marker></defs>
<text x="100" y="148" font-size="10" fill="#475569">f: A → B</text>
</svg>''',
"triangle": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="40,130 200,130 120,40" fill="#eef4fb" stroke="#2563eb" stroke-width="1.8"/>
<line x1="120" y1="40" x2="120" y2="130" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="4 3"/>
<text x="110" y="148" font-size="10" fill="#475569">a（底边）</text>
<text x="124" y="88" font-size="10" fill="#ef4444">h（高）</text>
<text x="70" y="96" font-size="10" fill="#2563eb">b</text>
<text x="158" y="96" font-size="10" fill="#2563eb">c</text>
<text x="108" y="34" font-size="10" fill="#475569">A</text>
<text x="34" y="126" font-size="10" fill="#475569">B</text>
<text x="202" y="126" font-size="10" fill="#475569">C</text>
</svg>''',
"circle": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="56" fill="none" stroke="#2563eb" stroke-width="2"/>
<line x1="120" y1="80" x2="176" y2="80" stroke="#ef4444" stroke-width="1.8"/>
<circle cx="120" cy="80" r="2.5" fill="#475569"/>
<line x1="64" y1="80" x2="176" y2="80" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="140" y="76" font-size="10" fill="#ef4444">r</text>
<text x="110" y="76" font-size="10" fill="#475569">O</text>
<text x="100" y="150" font-size="10" fill="#475569">C = 2πr,  S = πr²</text>
</svg>''',
"cone": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 120 28 L 60 132 L 180 132 Z" fill="#eef4fb" stroke="#2563eb" stroke-width="1.8"/>
<ellipse cx="120" cy="132" rx="60" ry="12" fill="none" stroke="#2563eb" stroke-width="1.5"/>
<line x1="120" y1="28" x2="120" y2="132" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="4 3"/>
<text x="124" y="82" font-size="10" fill="#ef4444">h</text>
<text x="80" y="148" font-size="10" fill="#475569">r</text>
<text x="78" y="14" font-size="10" fill="#2563eb">V = (1/3)πr²h</text>
</svg>''',
"conic": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1"/>
<line x1="120" y1="16" x2="120" y2="148" stroke="#475569" stroke-width="1"/>
<ellipse cx="120" cy="74" rx="70" ry="40" fill="none" stroke="#2563eb" stroke-width="2"/>
<circle cx="96" cy="74" r="2.5" fill="#ef4444"/><text x="84" y="70" font-size="9" fill="#ef4444">F1</text>
<circle cx="144" cy="74" r="2.5" fill="#ef4444"/><text x="148" y="70" font-size="9" fill="#ef4444">F2</text>
<text x="40" y="146" font-size="10" fill="#2563eb">椭圆 x²/a²+y²/b²=1</text>
</svg>''',
"probability": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="40" width="160" height="80" fill="#f8fafc" stroke="#cbd5e1" rx="8"/>
<circle cx="72" cy="70" r="12" fill="#2563eb"/>
<circle cx="110" cy="70" r="12" fill="#f59e0b"/>
<circle cx="148" cy="70" r="12" fill="#16a34a"/>
<circle cx="186" cy="70" r="12" fill="#ef4444"/>
<text x="66" y="74" font-size="10" fill="white" font-weight="bold">1</text>
<text x="104" y="74" font-size="10" fill="white" font-weight="bold">2</text>
<text x="142" y="74" font-size="10" fill="white" font-weight="bold">3</text>
<text x="180" y="74" font-size="10" fill="white" font-weight="bold">4</text>
<text x="70" y="110" font-size="11" fill="#475569">P(事件A) = m/n</text>
</svg>'''
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","note":"备 注"}

CORE_FORMULAS = [
    ("集合交换律", "A\\cap B = B\\cap A,\\quad A\\cup B = B\\cup A", "交集与并集满足交换律"),
    ("集合结合律", "(A\\cap B)\\cap C = A\\cap(B\\cap C)", "交集与并集满足结合律"),
    ("德摩根律", "\\complement_U(A\\cap B) = \\complement_U A \\cup \\complement_U B", "补集对交并的对偶关系"),
    ("二次方程求根", "x = \\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}", "ax²+bx+c=0 的求根公式"),
    ("判别式", "\\Delta = b^2-4ac", "判别二次方程实根个数"),
    ("韦达定理", "x_1+x_2=-\\dfrac{b}{a},\\quad x_1x_2=\\dfrac{c}{a}", "根与系数的关系"),
    ("完全平方公式", "(a\\pm b)^2 = a^2 \\pm 2ab + b^2", "二项式平方展开"),
    ("平方差公式", "a^2 - b^2 = (a+b)(a-b)", "因式分解基本公式"),
    ("立方和差", "a^3\\pm b^3 = (a\\pm b)(a^2\\mp ab+b^2)", "立方和/差分解"),
    ("二项式定理", "(a+b)^n = \\sum_{k=0}^n \\binom{n}{k} a^{n-k}b^k", "二项式展开"),
    ("对数换底", "\\log_a b = \\dfrac{\\log_c b}{\\log_c a}", "对数换底公式"),
    ("对数运算", "\\log_a(MN)=\\log_aM+\\log_aN", "积的对数等于对数之和"),
    ("等差数列通项", "a_n = a_1 + (n-1)d", "公差为 d 的等差数列第 n 项"),
    ("等差数列求和", "S_n = \\dfrac{n(a_1+a_n)}{2} = na_1+\\dfrac{n(n-1)}{2}d", "前 n 项和"),
    ("等比数列通项", "a_n = a_1 q^{n-1}", "公比为 q 的等比数列第 n 项"),
    ("等比数列求和", "S_n = \\dfrac{a_1(1-q^n)}{1-q}\\ (q\\neq 1)", "前 n 项和"),
    ("无穷等比级数", "S = \\dfrac{a_1}{1-q}\\ (|q|<1)", "公比绝对值小于 1 时的和"),
    ("勾股定理", "a^2+b^2 = c^2", "直角三角形两直角边平方和等于斜边平方"),
    ("正弦定理", "\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R", "三角形边与对角正弦之比"),
    ("余弦定理", "c^2 = a^2+b^2-2ab\\cos C", "已知两边夹角求第三边"),
    ("三角形面积", "S = \\dfrac{1}{2}ab\\sin C", "两边及其夹角求面积"),
    ("海伦公式", "S = \\sqrt{p(p-a)(p-b)(p-c)},\\ p=\\dfrac{a+b+c}{2}", "已知三边求面积"),
    ("圆周长", "C = 2\\pi r", "圆的周长公式"),
    ("圆面积", "S = \\pi r^2", "圆的面积公式"),
    ("扇形弧长", "l = \\alpha r = \\dfrac{n\\pi r}{180}", "弧长与圆心角关系"),
    ("扇形面积", "S = \\dfrac{1}{2}lr = \\dfrac{1}{2}\\alpha r^2", "扇形面积公式"),
    ("球表面积", "S = 4\\pi R^2", "球面面积"),
    ("球体积", "V = \\dfrac{4}{3}\\pi R^3", "球的体积"),
    ("圆柱体积", "V = \\pi r^2 h", "底面积乘高"),
    ("圆锥体积", "V = \\dfrac{1}{3}\\pi r^2 h", "同底等高圆柱体积的 1/3"),
    ("两点距离", "d = \\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}", "平面内两点间距离"),
    ("点到直线距离", "d = \\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}", "点到直线 Ax+By+C=0 的距离"),
    ("直线斜率", "k = \\dfrac{y_2-y_1}{x_2-x_1} = \\tan\\alpha", "斜率与倾斜角关系"),
    ("圆方程", "(x-a)^2+(y-b)^2 = r^2", "圆心 (a,b) 半径 r 的圆"),
    ("椭圆标准方程", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2} = 1\\ (a>b>0)", "焦点在 x 轴的椭圆"),
    ("双曲线标准方程", "\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2} = 1", "焦点在 x 轴的双曲线"),
    ("抛物线标准方程", "y^2 = 2px\\ (p>0)", "开口向右的抛物线"),
    ("古典概型", "P(A) = \\dfrac{m}{n}", "事件 A 包含 m 个基本事件，共 n 个等可能基本事件"),
    ("互斥事件加法", "P(A\\cup B) = P(A)+P(B)", "A、B 互斥时的概率加法"),
    ("独立事件乘法", "P(A\\cap B) = P(A)\\cdot P(B)", "A、B 独立时的概率乘法"),
    ("条件概率", "P(A|B) = \\dfrac{P(A\\cap B)}{P(B)}", "B 发生条件下 A 发生的概率"),
    ("全概率公式", "P(A) = \\sum_i P(B_i)P(A|B_i)", "由分割 B_i 求 A 的概率"),
    ("贝叶斯公式", "P(B_i|A) = \\dfrac{P(B_i)P(A|B_i)}{\\sum_j P(B_j)P(A|B_j)}", "后验概率公式"),
    ("期望", "E(X) = \\sum_i x_i p_i", "离散型随机变量的数学期望"),
    ("方差", "D(X) = E[(X-E(X))^2] = E(X^2)-[E(X)]^2", "随机变量的方差"),
    ("二项分布期望", "E(X)=np,\\ D(X)=np(1-p)", "X~B(n,p) 的期望与方差"),
    ("正态分布密度", "f(x) = \\dfrac{1}{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}", "N(μ,σ²) 的概率密度"),
]

def js_escape(s):
    return s.replace("\\","\\\\").replace("`","\\`").replace("${","\\${")
def fix_lt_math(s):
    import re
    return re.sub(r"\$\$[\s\S]*?\$\$|\$[^$\n]*?\$", lambda m: m.group(0).replace("<", "&lt;"), s)
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

# ============ 第一章 集合与逻辑 ============
ch1_sections = [
{"name":"1.1 集合及其运算","color":"#2563eb","desc":"集合概念、交并补运算与韦恩图",
"items":[
{"id":"e1s1-1","name":"集合的概念与表示","tags":["def","exa"],"brief":"集合是确定对象的全体，常用列举法、描述法表示。",
"body":wrap(
 defn("集合与元素",p("具有某种特定性质的事物的总体称为<strong>集合</strong>，组成集合的事物称为<strong>元素</strong>。若 a 是集合 A 的元素，记 $a\\in A$；否则 $a\\notin A$。"))+
 note(p("集合中元素具有<strong>确定性、互异性、无序性</strong>三大特性。确定性要求能判断任一对象是否属于该集合；互异性要求元素不重复；无序性要求元素排列顺序不影响集合相等。"))+
 exa(p("<strong>常见数集：</strong>$\\mathbb{N}$ 自然数集、$\\mathbb{Z}$ 整数集、$\\mathbb{Q}$ 有理数集、$\\mathbb{R}$ 实数集、$\\mathbb{C}$ 复数集。"))+
 p("集合的表示方法：<br>① <strong>列举法</strong>：$A=\\{1,2,3\\}$；<br>② <strong>描述法</strong>：$A=\\{x\\mid x>0, x\\in\\mathbb{R}\\}$；<br>③ <strong>图示法</strong>（韦恩图）。"))
},
{"id":"e1s1-2","name":"集合的交、并、补运算","tags":["def","thm","der"],"brief":"交集、并集、补集的定义与运算律。",
"fig":"set_venn","figCap":"集合 A 与 B 的韦恩图，重叠区为 A∩B",
"body":wrap(
 defn("交集",p("由所有既属于 A 又属于 B 的元素组成的集合，称为 A 与 B 的<strong>交集</strong>：")+
 fml("A\\cap B = \\{x\\mid x\\in A \\text{ 且 } x\\in B\\}"))+
 defn("并集",p("由所有属于 A 或属于 B 的元素组成的集合，称为 A 与 B 的<strong>并集</strong>：")+
 fml("A\\cup B = \\{x\\mid x\\in A \\text{ 或 } x\\in B\\}"))+
 defn("补集",p("设 U 为全集，A 是 U 的子集，则 U 中所有不属于 A 的元素组成的集合称为 A 相对于 U 的<strong>补集</strong>：")+
 fml("\\complement_U A = \\{x\\mid x\\in U \\text{ 且 } x\\notin A\\}"))+
 thm("德摩根律",p("补集对交并运算满足对偶关系：")+
 fml("\\complement_U(A\\cap B)=\\complement_U A\\cup\\complement_U B,\\quad \\complement_U(A\\cup B)=\\complement_U A\\cap\\complement_U B"))+
 der(p("证明第一式：任取 $x\\in\\complement_U(A\\cap B)$，则 $x\\notin A\\cap B$，即 $x\\notin A$ 或 $x\\notin B$，故 $x\\in\\complement_U A$ 或 $x\\in\\complement_U B$，即 $x\\in\\complement_U A\\cup\\complement_U B$。反向包含同理可证。"))
)},
{"id":"e1s1-3","name":"子集与真子集","tags":["def","thm"],"brief":"子集、真子集、集合相等的判定。",
"body":wrap(
 defn("子集",p("若集合 A 的每一个元素都属于 B，则称 A 是 B 的<strong>子集</strong>，记作 $A\\subseteq B$。若 $A\\subseteq B$ 且 $B\\subseteq A$，则 $A=B$。"))+
 defn("真子集",p("若 $A\\subseteq B$ 且存在 $b\\in B$ 使 $b\\notin A$，则称 A 是 B 的<strong>真子集</strong>，记作 $A\\subsetneq B$。"))+
 note(p("空集 $\\varnothing$ 是任何集合的子集，是任何非空集合的真子集。含有 $n$ 个元素的集合共有 $2^n$ 个子集，$2^n-1$ 个真子集，$2^n-2$ 个非空真子集。"))
)}
]},
{"name":"1.2 常用逻辑用语","color":"#0ea5e9","desc":"命题、充要条件与量词",
"items":[
{"id":"e1s2-1","name":"命题与四种命题","tags":["def","thm"],"brief":"原命题、逆命题、否命题、逆否命题的关系。",
"body":wrap(
 defn("命题",p("可以判断真假的陈述句称为<strong>命题</strong>。判断为真的叫真命题，判断为假的叫假命题。"))+
 p("设原命题为「若 p，则 q」，则：<br>① <strong>逆命题</strong>：若 q，则 p；<br>② <strong>否命题</strong>：若 ¬p，则 ¬q；<br>③ <strong>逆否命题</strong>：若 ¬q，则 ¬p。")+
 thm("等价性",p("原命题与其逆否命题同真同假（等价）；逆命题与否命题同真同假。但原命题与逆命题、否命题的真假无必然联系。"))
)},
{"id":"e1s2-2","name":"充分条件与必要条件","tags":["def","exa"],"brief":"充要条件的判定与逻辑推理。",
"body":wrap(
 defn("充分条件与必要条件",p("若 $p\\Rightarrow q$（p 推出 q），则称 p 是 q 的<strong>充分条件</strong>，q 是 p 的<strong>必要条件</strong>。"))+
 defn("充要条件",p("若 $p\\Leftrightarrow q$（p 与 q 可互推），则称 p 是 q 的<strong>充要条件</strong>（充分必要条件）。"))+
 exa(p("<strong>例：</strong>「$x=1$」是「$x^2=1$」的充分不必要条件（$x=1\\Rightarrow x^2=1$，但 $x^2=1$ 时 $x$ 也可为 $-1$）。"))+
 note(p("判断口诀：<strong>充分看前推后，必要看后推前</strong>。小范围推大范围是充分，大范围推小范围是必要。"))
)}
]}
]

# ============ 第二章 代数 ============
ch2_sections = [
{"name":"2.1 多项式与因式分解","color":"#7c3aed","desc":"整式运算、乘法公式与因式分解",
"items":[
{"id":"e2s1-1","name":"整式运算与乘法公式","tags":["thm","der"],"brief":"幂的运算、乘法公式及其推导。",
"body":wrap(
 thm("幂的运算法则",p("同底数幂相乘、幂的乘方、积的乘方：")+
 fml("a^m\\cdot a^n = a^{m+n},\\quad (a^m)^n = a^{mn},\\quad (ab)^n = a^n b^n"))+
 thm("乘法公式",p("常用乘法公式：")+
 fml("(a+b)(a-b)=a^2-b^2,\\quad (a\\pm b)^2=a^2\\pm 2ab+b^2"))+
 fml("(a\\pm b)^3=a^3\\pm 3a^2b+3ab^2\\pm b^3,\\quad a^3\\pm b^3=(a\\pm b)(a^2\\mp ab+b^2)")+
 der(p("<strong>推导平方差：</strong>$(a+b)(a-b)=a^2-ab+ab-b^2=a^2-b^2$，交叉项抵消。")+
 p("<strong>推导完全平方：</strong>$(a+b)^2=(a+b)(a+b)=a^2+ab+ba+b^2=a^2+2ab+b^2$。"))
)},
{"id":"e2s1-2","name":"因式分解的方法","tags":["def","exa"],"brief":"提公因式、公式法、十字相乘法、分组分解。",
"body":wrap(
 defn("因式分解",p("把一个多项式化为几个整式乘积的形式，称为<strong>因式分解</strong>。分解必须进行到每一个因式都不能再分解为止（在指定数域内）。"))+
 p("常用方法：<br>① <strong>提公因式法</strong>：$ma+mb+mc=m(a+b+c)$；<br>② <strong>公式法</strong>：套用乘法公式；<br>③ <strong>十字相乘法</strong>：$x^2+(p+q)x+pq=(x+p)(x+q)$；<br>④ <strong>分组分解法</strong>：适当分组后提取公因式。")+
 exa(p("<strong>例：</strong>分解 $x^3-3x^2+2x$。先提公因式 $x$ 得 $x(x^2-3x+2)$，再对二次式十字相乘：$x^2-3x+2=(x-1)(x-2)$。故原式 $=x(x-1)(x-2)$。"))
)}
]},
{"name":"2.2 方程与不等式","color":"#a855f7","desc":"一元二次方程、分式方程与不等式",
"items":[
{"id":"e2s2-1","name":"一元二次方程","tags":["thm","der"],"brief":"求根公式、判别式、韦达定理。",
"fig":"quadratic","figCap":"二次函数 y=ax²+bx+c 图像，开口向上，顶点在 x 轴上方",
"body":wrap(
 thm("求根公式",p("一元二次方程 $ax^2+bx+c=0\\ (a\\neq 0)$ 的解为：")+
 fml("x = \\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}"))+
 der(p("<strong>配方法推导：</strong>两边除以 $a$：$x^2+\\dfrac{b}{a}x+\\dfrac{c}{a}=0$。配方：")+
 fml("\\left(x+\\dfrac{b}{2a}\\right)^2 = \\dfrac{b^2-4ac}{4a^2}")+
 p("当 $b^2-4ac\\ge 0$ 时开方即得求根公式。"))+
 thm("判别式与根的关系",p("$\\Delta=b^2-4ac$：")+
 p("$\\Delta>0$：两个不相等实根；$\\Delta=0$：两个相等实根；$\\Delta<0$：无实根（有共轭虚根）。"))+
 thm("韦达定理",p("若方程两根为 $x_1,x_2$，则：")+
 fml("x_1+x_2=-\\dfrac{b}{a},\\quad x_1x_2=\\dfrac{c}{a}"))+
 der(p("由求根公式 $x_1=\\dfrac{-b+\\sqrt{\\Delta}}{2a}$，$x_2=\\dfrac{-b-\\sqrt{\\Delta}}{2a}$，相加得 $x_1+x_2=\\dfrac{-2b}{2a}=-\\dfrac{b}{a}$；相乘利用平方差得 $x_1x_2=\\dfrac{b^2-\\Delta}{4a^2}=\\dfrac{4ac}{4a^2}=\\dfrac{c}{a}$。"))
)},
{"id":"e2s2-2","name":"基本不等式","tags":["thm","der","app"],"brief":"均值不等式及其应用。",
"body":wrap(
 thm("基本不等式",p("对任意正实数 $a,b$，有：")+
 fml("\\dfrac{a+b}{2} \\ge \\sqrt{ab}"))+
 der(p("<strong>推导：</strong>由 $(\\sqrt{a}-\\sqrt{b})^2\\ge 0$ 展开得 $a-2\\sqrt{ab}+b\\ge 0$，即 $a+b\\ge 2\\sqrt{ab}$，两边除以 2 得证。等号当且仅当 $\\sqrt{a}=\\sqrt{b}$ 即 $a=b$ 时成立。"))+
 app(p("<strong>应用——求最值：</strong>若 $a,b>0$ 且 $ab$ 为定值，则 $a+b\\ge 2\\sqrt{ab}$，当 $a=b$ 时取最小值；若 $a+b$ 为定值，则 $ab\\le \\dfrac{(a+b)^2}{4}$，当 $a=b$ 时取最大值。口诀「<strong>一正二定三相等</strong>」。"))
)}
]},
{"name":"2.3 复数","color":"#c026d3","desc":"复数概念、运算与几何意义",
"items":[
{"id":"e2s3-1","name":"复数的概念与运算","tags":["def","thm"],"brief":"复数代数形式、加减乘除运算。",
"body":wrap(
 defn("复数",p("形如 $a+bi$（$a,b\\in\\mathbb{R}$）的数称为<strong>复数</strong>，其中 $i^2=-1$。$a$ 称为实部（Re z），$b$ 称为虚部（Im z）。当 $b=0$ 时为实数，$b\\neq 0$ 时为虚数，$a=0,b\\neq 0$ 时为纯虚数。"))+
 thm("运算法则",p("设 $z_1=a+bi$，$z_2=c+di$：")+
 fml("z_1+z_2=(a+c)+(b+d)i,\\quad z_1-z_2=(a-c)+(b-d)i")+
 fml("z_1\\cdot z_2=(ac-bd)+(ad+bc)i")+
 fml("\\dfrac{z_1}{z_2}=\\dfrac{(ac+bd)+(bc-ad)i}{c^2+d^2}\\quad(z_2\\neq 0)"))+
 note(p("复数除法通过<strong>分母实数化</strong>完成：分子分母同乘分母的共轭复数 $c-di$。"))
)},
{"id":"e2s3-2","name":"复数的几何意义与三角形式","tags":["def","thm"],"brief":"复平面、模、辐角与三角表示。",
"body":wrap(
 defn("复平面与模",p("复数 $z=a+bi$ 对应复平面上的点 $(a,b)$ 或向量 $(a,b)$。其<strong>模</strong>为：")+
 fml("|z| = \\sqrt{a^2+b^2}"))+
 defn("三角形式",p("设 $|z|=r$，辐角为 $\\theta$，则 $z=r(\\cos\\theta+i\\sin\\theta)$。")+
 fml("a = r\\cos\\theta,\\quad b = r\\sin\\theta"))+
 thm("棣莫弗公式",p("对正整数 $n$，有：")+
 fml("[r(\\cos\\theta+i\\sin\\theta)]^n = r^n(\\cos n\\theta+i\\sin n\\theta)"))
)}
]}
]

# ============ 第三章 函数 ============
ch3_sections = [
{"name":"3.1 函数的概念与性质","color":"#0d9488","desc":"函数定义、三要素与基本性质",
"items":[
{"id":"e3s1-1","name":"函数的概念","tags":["def","exa"],"brief":"函数是定义域到值域的映射。",
"fig":"func_mapping","figCap":"函数 f: A→B 将定义域中每个 x 唯一对应到值域中的 y",
"body":wrap(
 defn("函数",p("设 A、B 是非空数集，若按某种确定的对应关系 $f$，使 A 中任意一个数 $x$，在 B 中都有唯一确定的数 $y$ 与之对应，则称 $f:A\\to B$ 为从 A 到 B 的一个<strong>函数</strong>，记作 $y=f(x)$。A 称为<strong>定义域</strong>，函数值集合 $\\{f(x)\\mid x\\in A\\}$ 称为<strong>值域</strong>。"))+
 p("函数的<strong>三要素</strong>：定义域、对应关系、值域。定义域与对应关系相同的两个函数是同一函数。")+
 exa(p("<strong>例：</strong>$f(x)=\\dfrac{1}{x}$ 的定义域为 $\\{x\\mid x\\neq 0\\}$，值域为 $\\{y\\mid y\\neq 0\\}$。"))
)},
{"id":"e3s1-2","name":"函数的单调性与奇偶性","tags":["def","thm"],"brief":"单调递增/递减、奇函数/偶函数的判定。",
"body":wrap(
 defn("单调性",p("若对定义域内任意 $x_1<x_2$，都有 $f(x_1)<f(x_2)$，则 $f(x)$ 在该区间<strong>单调递增</strong>；若 $f(x_1)>f(x_2)$，则<strong>单调递减</strong>。"))+
 defn("奇偶性",p("若定义域关于原点对称，且对任意 $x$ 有 $f(-x)=-f(x)$，则 $f(x)$ 为<strong>奇函数</strong>（图像关于原点对称）；若 $f(-x)=f(x)$，则为<strong>偶函数</strong>（图像关于 y 轴对称）。"))+
 note(p("奇函数在 $x=0$ 处有定义时必有 $f(0)=0$；偶函数满足 $f(|x|)=f(x)$。判断奇偶性前必须先确认定义域关于原点对称。"))
)},
{"id":"e3s1-3","name":"反函数","tags":["def","thm"],"brief":"反函数存在条件与图像对称性。",
"body":wrap(
 defn("反函数",p("若函数 $y=f(x)$ 的定义域到值域的对应是一一对应，则存在<strong>反函数</strong> $x=f^{-1}(y)$，习惯记为 $y=f^{-1}(x)$。"))+
 thm("反函数性质",p("① $y=f(x)$ 与 $y=f^{-1}(x)$ 的图像关于直线 $y=x$ 对称；<br>② 反函数的定义域是原函数的值域，值域是原函数的定义域；<br>③ $f(f^{-1}(x))=x$，$f^{-1}(f(x))=x$。")+
 note(p("只有<strong>一一对应</strong>的函数才有反函数。严格单调函数一定有反函数。"))
))}
]},
{"name":"3.2 基本初等函数","color":"#14b8a6","desc":"指数、对数、幂函数与三角函数",
"items":[
{"id":"e3s2-1","name":"指数函数与对数函数","tags":["def","thm"],"brief":"指数与对数的定义、性质及互逆关系。",
"body":wrap(
 defn("指数函数",p("$y=a^x$（$a>0$ 且 $a\\neq 1$），定义域 $\\mathbb{R}$，值域 $(0,+\\infty)$。当 $a>1$ 时单调递增，$0<a<1$ 时单调递减，恒过点 $(0,1)$。"))+
 defn("对数函数",p("$y=\\log_a x$（$a>0$ 且 $a\\neq 1$）是 $y=a^x$ 的反函数，定义域 $(0,+\\infty)$，值域 $\\mathbb{R}$。当 $a>1$ 时单调递增，恒过点 $(1,0)$。"))+
 thm("对数运算法则",p("（$a>0,a\\neq1$，$M,N>0$）")+
 fml("\\log_a(MN)=\\log_aM+\\log_aN,\\quad \\log_a\\dfrac{M}{N}=\\log_aM-\\log_aN")+
 fml("\\log_a M^n = n\\log_a M,\\quad \\log_a b = \\dfrac{\\log_c b}{\\log_c a}\\ (\\text{换底公式})"))+
 der(p("<strong>换底公式推导：</strong>设 $\\log_a b=x$，则 $a^x=b$。两边取以 $c$ 为底的对数：$x\\log_c a=\\log_c b$，故 $x=\\dfrac{\\log_c b}{\\log_c a}$。"))
)},
{"id":"e3s2-2","name":"幂函数","tags":["def","exa"],"brief":"y=x^α 的图像与性质。",
"body":wrap(
 defn("幂函数",p("形如 $y=x^\\alpha$（$\\alpha$ 为常数）的函数称为<strong>幂函数</strong>。图像恒过点 $(1,1)$。"))+
 p("常见幂函数性质：<br>① $\\alpha=1$：$y=x$，直线；<br>② $\\alpha=2$：$y=x^2$，抛物线，偶函数；<br>③ $\\alpha=3$：$y=x^3$，奇函数，单调递增；<br>④ $\\alpha=-1$：$y=1/x$，双曲线，奇函数；<br>⑤ $\\alpha=1/2$：$y=\\sqrt{x}$，定义域 $[0,+\\infty)$。")+
 note(p("幂函数在第一象限的图像：$\\alpha>0$ 时递增且过原点（$\\alpha>1$ 时下凸，$0<\\alpha<1$ 时上凸）；$\\alpha<0$ 时递减，不过原点。"))
)},
{"id":"e3s2-3","name":"三角函数","tags":["def","thm"],"brief":"正弦、余弦、正切的定义、性质与基本关系。",
"body":wrap(
 defn("三角函数",p("在单位圆中，设角 $\\alpha$ 终边与单位圆交于 $(x,y)$，则：")+
 fml("\\sin\\alpha = y,\\quad \\cos\\alpha = x,\\quad \\tan\\alpha = \\dfrac{y}{x}\\ (x\\neq 0)"))+
 thm("同角三角函数基本关系",p("")+
 fml("\\sin^2\\alpha + \\cos^2\\alpha = 1,\\quad \\tan\\alpha = \\dfrac{\\sin\\alpha}{\\cos\\alpha}"))+
 thm("诱导公式",p("奇变偶不变，符号看象限。例如：")+
 fml("\\sin(\\pi-\\alpha)=\\sin\\alpha,\\quad \\cos(\\pi+\\alpha)=-\\cos\\alpha,\\quad \\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha"))
)}
]}
]

# ============ 第四章 数列 ============
ch4_sections = [
{"name":"4.1 等差数列","color":"#c2410c","desc":"等差数列通项、求和与性质",
"items":[
{"id":"e4s1-1","name":"等差数列的通项公式","tags":["def","thm","der"],"brief":"a_n = a_1 + (n-1)d。",
"body":wrap(
 defn("等差数列",p("从第二项起，每一项与前一项的差等于同一个常数的数列，称为<strong>等差数列</strong>。该常数称为<strong>公差</strong>，记作 $d$。"))+
 thm("通项公式",p("首项为 $a_1$，公差为 $d$ 的等差数列，第 $n$ 项为：")+
 fml("a_n = a_1 + (n-1)d"))+
 der(p("<strong>归纳推导：</strong>$a_2=a_1+d$，$a_3=a_2+d=a_1+2d$，$a_4=a_1+3d$，……，归纳得 $a_n=a_1+(n-1)d$。"))+
 note(p("通项公式推广：$a_n=a_m+(n-m)d$。"))
)},
{"id":"e4s1-2","name":"等差数列求和公式","tags":["thm","der","app"],"brief":"S_n = n(a_1+a_n)/2。",
"body":wrap(
 thm("前 n 项和",p("")+
 fml("S_n = \\dfrac{n(a_1+a_n)}{2} = na_1 + \\dfrac{n(n-1)}{2}d"))+
 der(p("<strong>倒序相加法：</strong>设 $S_n=a_1+a_2+\\cdots+a_n$，倒序写 $S_n=a_n+a_{n-1}+\\cdots+a_1$。两式相加，利用 $a_i+a_{n+1-i}=a_1+a_n$（共 $n$ 对），得 $2S_n=n(a_1+a_n)$，故 $S_n=\\dfrac{n(a_1+a_n)}{2}$。"))+
 app(p("<strong>性质：</strong>若 $m+n=p+q$，则 $a_m+a_n=a_p+a_q$。$S_n, S_{2n}-S_n, S_{3n}-S_{2n}$ 仍成等差数列，公差为 $n^2d$。"))
)}
]},
{"name":"4.2 等比数列","color":"#ea580c","desc":"等比数列通项、求和与性质",
"items":[
{"id":"e4s2-1","name":"等比数列的通项公式","tags":["def","thm","der"],"brief":"a_n = a_1·q^(n-1)。",
"body":wrap(
 defn("等比数列",p("从第二项起，每一项与前一项的比等于同一个非零常数的数列，称为<strong>等比数列</strong>。该常数称为<strong>公比</strong>，记作 $q$（$q\\neq 0$）。"))+
 thm("通项公式",p("首项为 $a_1$，公比为 $q$ 的等比数列，第 $n$ 项为：")+
 fml("a_n = a_1 q^{n-1}"))+
 der(p("<strong>归纳推导：</strong>$a_2=a_1q$，$a_3=a_2q=a_1q^2$，……，$a_n=a_1q^{n-1}$。"))
)},
{"id":"e4s2-2","name":"等比数列求和与无穷级数","tags":["thm","der"],"brief":"S_n = a_1(1-q^n)/(1-q)。",
"body":wrap(
 thm("前 n 项和",p("当 $q\\neq 1$ 时：")+
 fml("S_n = \\dfrac{a_1(1-q^n)}{1-q} = \\dfrac{a_1-a_nq}{1-q}"))+
 der(p("<strong>错位相减法：</strong>$S_n=a_1+a_1q+\\cdots+a_1q^{n-1}$，两边乘 $q$：$qS_n=a_1q+\\cdots+a_1q^{n-1}+a_1q^n$。两式相减：$(1-q)S_n=a_1(1-q^n)$，故 $S_n=\\dfrac{a_1(1-q^n)}{1-q}$。"))+
 thm("无穷等比级数",p("当 $|q|<1$ 时，无穷项之和为：")+
 fml("S = \\lim_{n\\to\\infty} S_n = \\dfrac{a_1}{1-q}"))+
 der(p("$|q|<1$ 时 $q^n\\to 0$，故 $S=\\dfrac{a_1(1-0)}{1-q}=\\dfrac{a_1}{1-q}$。"))
)}
]},
{"name":"4.3 数列求和方法","color":"#f59e0b","desc":"裂项相消、错位相减、分组求和",
"items":[
{"id":"e4s3-1","name":"裂项相消法","tags":["def","exa"],"brief":"将通项拆成两项之差，相消求和。",
"body":wrap(
 defn("裂项相消",p("将数列的每一项拆成两项之差，使得求和时中间项相互抵消。常见裂项：")+
 fml("\\dfrac{1}{n(n+1)} = \\dfrac{1}{n}-\\dfrac{1}{n+1}")+
 fml("\\dfrac{1}{(2n-1)(2n+1)} = \\dfrac{1}{2}\\left(\\dfrac{1}{2n-1}-\\dfrac{1}{2n+1}\\right)"))+
 exa(p("<strong>例：</strong>求 $S_n=\\dfrac{1}{1\\cdot 2}+\\dfrac{1}{2\\cdot 3}+\\cdots+\\dfrac{1}{n(n+1)}$。<br>由裂项 $\\dfrac{1}{k(k+1)}=\\dfrac{1}{k}-\\dfrac{1}{k+1}$，得 $S_n=\\left(1-\\dfrac{1}{2}\\right)+\\left(\\dfrac{1}{2}-\\dfrac{1}{3}\\right)+\\cdots+\\left(\\dfrac{1}{n}-\\dfrac{1}{n+1}\\right)=1-\\dfrac{1}{n+1}=\\dfrac{n}{n+1}$。"))
)},
{"id":"e4s3-2","name":"错位相减法","tags":["exa"],"brief":"适用于等差×等比型数列求和。",
"body":wrap(
 p("<strong>方法：</strong>设 $c_n=a_n\\cdot b_n$，其中 $\\{a_n\\}$ 等差、$\\{b_n\\}$ 等比（公比 $q$）。写出 $S_n$ 与 $qS_n$，错位相减后化为等比求和。")+
 exa(p("<strong>例：</strong>求 $S_n=1+2x+3x^2+\\cdots+nx^{n-1}$（$x\\neq 1$）。<br>$xS_n=x+2x^2+\\cdots+(n-1)x^{n-1}+nx^n$，两式相减：$(1-x)S_n=1+x+x^2+\\cdots+x^{n-1}-nx^n=\\dfrac{1-x^n}{1-x}-nx^n$，故 $S_n=\\dfrac{1-x^n}{(1-x)^2}-\\dfrac{nx^n}{1-x}$。"))
)}
]}
]

# ============ 第五章 平面几何 ============
ch5_sections = [
{"name":"5.1 三角形","color":"#be185d","desc":"三角形边角关系、全等与相似",
"items":[
{"id":"e5s1-1","name":"三角形基本性质","tags":["thm","der"],"brief":"内角和、外角、三边关系。",
"body":wrap(
 thm("内角和定理",p("三角形三个内角之和等于 $180°$（$\\pi$ 弧度）。")+
 fml("\\angle A + \\angle B + \\angle C = 180°"))+
 der(p("<strong>证明：</strong>过顶点 A 作 BC 的平行线 $l$。由平行线内错角相等，$\\angle B$ 等于 $l$ 与 AB 的夹角，$\\angle C$ 等于 $l$ 与 AC 的夹角。$l$ 为直线，故三个角拼成平角 $180°$。"))+
 thm("三边关系",p("三角形任意两边之和大于第三边，任意两边之差小于第三边：")+
 fml("a+b>c,\\quad a+c>b,\\quad b+c>a"))+
 thm("外角定理",p("三角形的一个外角等于与它不相邻的两个内角之和。"))
)},
{"id":"e5s1-2","name":"全等三角形与相似三角形","tags":["def","thm"],"brief":"全等判定（SSS/SAS/ASA/AAS）与相似判定。",
"body":wrap(
 defn("全等三角形",p("能够完全重合的两个三角形称为<strong>全等三角形</strong>。全等三角形的对应边相等、对应角相等。"))+
 thm("全等判定",p("① <strong>SSS</strong>（边边边）：三边对应相等；<br>② <strong>SAS</strong>（边角边）：两边及其夹角对应相等；<br>③ <strong>ASA</strong>（角边角）：两角及其夹边对应相等；<br>④ <strong>AAS</strong>（角角边）：两角及其中一角的对边对应相等。"))+
 defn("相似三角形",p("对应角相等、对应边成比例的两个三角形称为<strong>相似三角形</strong>。相似比 $k$ 等于对应边之比。"))+
 thm("相似判定与性质",p("判定：AA（两角对应相等）、SAS（两边成比例且夹角相等）、SSS（三边成比例）。<br>性质：对应角相等，对应边、周长、对应线段之比等于相似比 $k$，面积比等于 $k^2$。"))
)},
{"id":"e5s1-3","name":"正弦定理与余弦定理","tags":["thm","der","app"],"brief":"解三角形的基本工具。",
"fig":"triangle","figCap":"三角形 ABC，底边 a，高 h，三边 a,b,c",
"body":wrap(
 thm("正弦定理",p("在 $\\triangle ABC$ 中，$R$ 为外接圆半径：")+
 fml("\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R"))+
 der(p("<strong>证明：</strong>作 $\\triangle ABC$ 的外接圆，直径为 $2R$。由同弧所对圆周角相等，$\\angle A$ 等于边 $a$ 所对的圆周角。在直角三角形中 $\\sin A = \\dfrac{a}{2R}$，即 $\\dfrac{a}{\\sin A}=2R$。同理得其他。"))+
 thm("余弦定理",p("")+
 fml("c^2 = a^2+b^2-2ab\\cos C"))+
 der(p("<strong>证明（向量法）：</strong>$\\vec{c}=\\vec{a}-\\vec{b}$，则 $|\\vec{c}|^2=|\\vec{a}-\\vec{b}|^2=|\\vec{a}|^2+|\\vec{b}|^2-2\\vec{a}\\cdot\\vec{b}=a^2+b^2-2ab\\cos C$。"))+
 app(p("<strong>适用场景：</strong>正弦定理适用于已知两角一边或两边一对角；余弦定理适用于已知两边夹角或三边。"))
)}
]},
{"name":"5.2 圆","color":"#db2777","desc":"圆的性质、切线与圆幂定理",
"items":[
{"id":"e5s2-1","name":"圆的基本性质","tags":["thm","der"],"brief":"垂径定理、圆周角定理。",
"fig":"circle","figCap":"圆 O，半径 r，周长 C=2πr，面积 S=πr²",
"body":wrap(
 thm("垂径定理",p("垂直于弦的直径平分这条弦，并且平分弦所对的两条弧。"))+
 der(p("<strong>证明：</strong>设直径 $CD\\perp$ 弦 $AB$ 于 $E$，圆心为 $O$。$OA=OB$（半径），$OE$ 公共，$\\angle OEA=\\angle OEB=90°$，故 $\\triangle OEA\\cong\\triangle OEB$，得 $AE=EB$。"))+
 thm("圆周角定理",p("同弧所对的圆周角等于圆心角的一半。")+
 fml("\\angle ACB = \\dfrac{1}{2}\\angle AOB"))+
 thm("推论",p("① 同弧或等弧所对的圆周角相等；<br>② 半圆（或直径）所对的圆周角是直角（$90°$）；<br>③ $90°$ 的圆周角所对的弦是直径。"))
)},
{"id":"e5s2-2","name":"切线与圆幂定理","tags":["thm","der"],"brief":"切线判定、切割线定理。",
"body":wrap(
 thm("切线判定与性质",p("判定：经过半径外端且垂直于这条半径的直线是圆的切线。<br>性质：圆的切线垂直于经过切点的半径。"))+
 thm("切割线定理",p("从圆外一点 $P$ 引切线 $PT$（$T$ 为切点）和割线 $PAB$（$A,B$ 为交点），则：")+
 fml("PT^2 = PA\\cdot PB"))+
 der(p("<strong>证明：</strong>连接 $TA, TB$。由弦切角定理，$\\angle PTA=\\angle PBT$（弦切角等于所夹弧的圆周角）。又 $\\angle P$ 公共，故 $\\triangle PTA\\sim\\triangle PBT$，得 $\\dfrac{PT}{PB}=\\dfrac{PA}{PT}$，即 $PT^2=PA\\cdot PB$。"))
)}
]}
]

# ============ 第六章 立体几何 ============
ch6_sections = [
{"name":"6.1 空间几何体","color":"#7c3aed","desc":"柱、锥、台、球的表面积与体积",
"items":[
{"id":"e6s1-1","name":"棱柱与棱锥","tags":["def","thm"],"brief":"棱柱棱锥的概念、表面积与体积。",
"body":wrap(
 defn("棱柱",p("有两个面互相平行，其余各面都是四边形，且每相邻两个四边形的公共边互相平行的多面体。")+
 fml("S_{\\text{直棱柱侧}} = ch\\ (c\\text{ 为底面周长},h\\text{ 为高}),\\quad V = Sh"))+
 defn("棱锥",p("有一个面是多边形，其余各面都是有一个公共顶点的三角形的多面体。")+
 fml("V_{\\text{棱锥}} = \\dfrac{1}{3}Sh"))+
 note(p("正棱锥的侧面积 $S_{\\text{侧}}=\\dfrac{1}{2}ch'$（$c$ 为底面周长，$h'$ 为斜高）。棱锥体积是同底等高棱柱的 $\\dfrac{1}{3}$。"))
)},
{"id":"e6s1-2","name":"圆柱、圆锥与球","tags":["def","thm","der"],"brief":"旋转体的表面积与体积公式。",
"fig":"cone","figCap":"圆锥，底面半径 r，高 h，体积 V=πr²h/3",
"body":wrap(
 defn("圆柱",p("以矩形的一边所在直线为旋转轴，其余三边旋转而成的旋转体。")+
 fml("S_{\\text{侧}} = 2\\pi rh,\\quad V = \\pi r^2 h"))+
 defn("圆锥",p("以直角三角形的一条直角边为旋转轴旋转而成的旋转体。")+
 fml("S_{\\text{侧}} = \\pi rl\\ (l\\text{ 为母线长}),\\quad V = \\dfrac{1}{3}\\pi r^2 h"))+
 thm("球的表面积与体积",p("半径为 $R$ 的球：")+
 fml("S_{\\text{球}} = 4\\pi R^2,\\quad V_{\\text{球}} = \\dfrac{4}{3}\\pi R^3"))+
 der(p("<strong>球体积推导（祖暅原理）：</strong>取半径为 $R$ 的半球，与底面半径和高均为 $R$ 的圆柱挖去一个等底等高的圆锥比较。在任一高度 $h$ 处，半球截面面积 $\\pi(R^2-h^2)$，圆柱挖圆锥后截面面积也是 $\\pi R^2-\\pi h^2=\\pi(R^2-h^2)$。由祖暅原理两者体积相等，故半球体积 $=\\pi R^3-\\dfrac{1}{3}\\pi R^3=\\dfrac{2}{3}\\pi R^3$，球体积 $=\\dfrac{4}{3}\\pi R^3$。"))
)}
]},
{"name":"6.2 空间中的线面关系","color":"#8b5cf6","desc":"线面平行、垂直的判定与性质",
"items":[
{"id":"e6s2-1","name":"空间直线与平面的位置关系","tags":["def","thm"],"brief":"线面平行、垂直的判定定理。",
"body":wrap(
 defn("线面平行判定",p("若平面外一条直线与此平面内的一条直线平行，则该直线与此平面平行。（线线平行 $\\Rightarrow$ 线面平行）"))+
 defn("线面垂直判定",p("若一条直线与一个平面内的两条相交直线都垂直，则该直线与此平面垂直。"))+
 thm("面面平行判定",p("若一个平面内有两条相交直线都平行于另一个平面，则这两个平面平行。"))+
 thm("面面垂直判定",p("若一个平面经过另一个平面的一条垂线，则这两个平面互相垂直。"))+
 note(p("关键思想：<strong>线线关系 → 线面关系 → 面面关系</strong>，逐层转化。"))
)},
{"id":"e6s2-2","name":"空间角与距离","tags":["def","thm"],"brief":"异面直线所成角、线面角、二面角。",
"body":wrap(
 defn("异面直线所成角",p("将两条异面直线平移至相交，所成的锐角或直角称为异面直线所成角，范围 $(0°,90°]$。"))+
 defn("线面角",p("直线与平面所成角是直线与其在平面内的射影所成的锐角，范围 $[0°,90°]$。当直线垂直于平面时为 $90°$，平行或在平面内时为 $0°$。"))+
 defn("二面角",p("从一条直线出发的两个半平面所组成的图形。其平面角是在棱上任取一点，分别在两个半平面内作垂直于棱的射线所成的角，范围 $[0°,180°]$。"))+
 note(p("求空间角的通法：<strong>找（作）角 → 证明 → 计算</strong>，常通过向量法转化为向量夹角计算。"))
)}
]}
]

# ============ 第七章 解析几何 ============
ch7_sections = [
{"name":"7.1 直线与圆","color":"#0891b2","desc":"直线方程、圆的方程及位置关系",
"items":[
{"id":"e7s1-1","name":"直线方程","tags":["def","thm"],"brief":"点斜式、斜截式、两点式、一般式。",
"body":wrap(
 defn("直线方程形式",p("① <strong>点斜式</strong>：$y-y_0=k(x-x_0)$；<br>② <strong>斜截式</strong>：$y=kx+b$；<br>③ <strong>两点式</strong>：$\\dfrac{y-y_1}{y_2-y_1}=\\dfrac{x-x_1}{x_2-x_1}$；<br>④ <strong>截距式</strong>：$\\dfrac{x}{a}+\\dfrac{y}{b}=1$；<br>⑤ <strong>一般式</strong>：$Ax+By+C=0$（$A,B$ 不同时为 0）。"))+
 thm("两直线位置关系",p("设 $l_1:y=k_1x+b_1$，$l_2:y=k_2x+b_2$：<br>平行：$k_1=k_2$ 且 $b_1\\neq b_2$；<br>垂直：$k_1k_2=-1$；<br>相交：$k_1\\neq k_2$。"))+
 thm("距离公式",p("点 $P(x_0,y_0)$ 到直线 $Ax+By+C=0$ 的距离：")+
 fml("d = \\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}"))
)},
{"id":"e7s1-2","name":"圆的方程","tags":["def","thm","der"],"brief":"标准方程、一般方程与直线圆位置关系。",
"body":wrap(
 defn("圆的标准方程",p("圆心为 $(a,b)$，半径为 $r$ 的圆：")+
 fml("(x-a)^2+(y-b)^2 = r^2"))+
 defn("圆的一般方程",p("")+
 fml("x^2+y^2+Dx+Ey+F=0\\quad(D^2+E^2-4F>0)")+
 p("圆心 $\\left(-\\dfrac{D}{2},-\\dfrac{E}{2}\\right)$，半径 $r=\\dfrac{1}{2}\\sqrt{D^2+E^2-4F}$。"))+
 thm("直线与圆的位置关系",p("设圆心到直线距离为 $d$，半径为 $r$：<br>$d>r$ 相离；$d=r$ 相切；$d<r$ 相交（弦长 $=2\\sqrt{r^2-d^2}$）。"))
)},
{"id":"e7s1-3","name":"空间解析几何简介","tags":["def","thm"],"brief":"空间直角坐标系、空间直线与平面。",
"body":wrap(
 defn("空间直角坐标系",p("过空间定点 $O$ 作三条互相垂直的数轴 $x,y,z$ 轴，构成空间直角坐标系。点 $P$ 的坐标 $(x,y,z)$。"))+
 thm("空间两点距离",p("$P_1(x_1,y_1,z_1)$，$P_2(x_2,y_2,z_2)$：")+
 fml("|P_1P_2| = \\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}"))+
 defn("空间平面方程",p("平面的一般方程：$Ax+By+Cz+D=0$，其中 $\\vec{n}=(A,B,C)$ 为法向量。"))+
 defn("空间直线方程",p("过点 $P_0(x_0,y_0,z_0)$，方向向量 $\\vec{s}=(m,n,p)$ 的直线参数方程：")+
 fml("\\dfrac{x-x_0}{m} = \\dfrac{y-y_0}{n} = \\dfrac{z-z_0}{p}"))+
 note(p("空间中直线与平面的夹角 $\\theta$ 满足 $\\sin\\theta=|\\cos\\langle\\vec{s},\\vec{n}\\rangle|$，两平面夹角等于其法向量夹角或其补角。"))
)}
]},
{"name":"7.2 圆锥曲线","color":"#0e7490","desc":"椭圆、双曲线、抛物线的定义与性质",
"items":[
{"id":"e7s2-1","name":"椭圆","tags":["def","thm","der"],"brief":"椭圆定义、标准方程与几何性质。",
"fig":"conic","figCap":"椭圆 x²/a²+y²/b²=1，两焦点 F1, F2",
"body":wrap(
 defn("椭圆定义",p("平面内与两个定点 $F_1,F_2$ 的距离之和等于常数 $2a$（$2a>|F_1F_2|$）的点的轨迹。两定点称为<strong>焦点</strong>，$|F_1F_2|=2c$。"))+
 thm("标准方程",p("焦点在 $x$ 轴上：")+
 fml("\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1\\quad(a>b>0,\\ c^2=a^2-b^2)"))+
 der(p("<strong>推导：</strong>设 $P(x,y)$，$|PF_1|+|PF_2|=2a$，即 $\\sqrt{(x+c)^2+y^2}+\\sqrt{(x-c)^2+y^2}=2a$。移项平方、整理、再平方，化简得 $(a^2-c^2)x^2+a^2y^2=a^2(a^2-c^2)$。令 $b^2=a^2-c^2$，两边除以 $a^2b^2$ 即得标准方程。"))+
 thm("离心率",p("$e=\\dfrac{c}{a}\\in(0,1)$，$e$ 越接近 0 椭圆越圆，越接近 1 越扁。"))
)},
{"id":"e7s2-2","name":"双曲线","tags":["def","thm"],"brief":"双曲线定义、标准方程与渐近线。",
"body":wrap(
 defn("双曲线定义",p("平面内与两个定点 $F_1,F_2$ 的距离之差的绝对值等于常数 $2a$（$0<2a<|F_1F_2|$）的点的轨迹。"))+
 thm("标准方程",p("焦点在 $x$ 轴上：")+
 fml("\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1\\quad(c^2=a^2+b^2)"))+
 thm("渐近线与离心率",p("渐近线：$y=\\pm\\dfrac{b}{a}x$；离心率 $e=\\dfrac{c}{a}>1$。"))+
 note(p("等轴双曲线 $a=b$，渐近线为 $y=\\pm x$，离心率 $e=\\sqrt{2}$。"))
)},
{"id":"e7s2-3","name":"抛物线","tags":["def","thm"],"brief":"抛物线定义、标准方程与焦点准线。",
"body":wrap(
 defn("抛物线定义",p("平面内与一个定点 $F$ 和一条定直线 $l$（$F\\notin l$）距离相等的点的轨迹。定点 $F$ 为<strong>焦点</strong>，定直线 $l$ 为<strong>准线</strong>。"))+
 thm("标准方程",p("开口向右（$p>0$）：")+
 fml("y^2 = 2px,\\quad \\text{焦点 } F\\left(\\dfrac{p}{2},0\\right),\\quad \\text{准线 } x=-\\dfrac{p}{2}"))+
 note(p("离心率 $e=1$。抛物线四种开口方向：$y^2=2px$（右）、$y^2=-2px$（左）、$x^2=2py$（上）、$x^2=-2py$（下）。"))
)}
]}
]

# ============ 第八章 概率统计 ============
ch8_sections = [
{"name":"8.1 随机事件与概率","color":"#059669","desc":"古典概型、几何概型与概率公式",
"items":[
{"id":"e8s1-1","name":"古典概型","tags":["def","thm","exa"],"brief":"等可能事件概率的计算。",
"fig":"probability","figCap":"古典概型：P(A)=m/n，m 为有利事件数，n 为基本事件总数",
"body":wrap(
 defn("古典概型",p("具有以下两个特征的随机试验模型：① 试验的所有可能结果只有有限个；② 每个结果出现的可能性相等。则事件 $A$ 的概率：")+
 fml("P(A) = \\dfrac{m}{n}")+
 p("其中 $n$ 为基本事件总数，$m$ 为事件 $A$ 包含的基本事件数。"))+
 exa(p("<strong>例：</strong>掷一枚均匀骰子，求点数为偶数的概率。<br>基本事件共 6 个（1~6 点），偶数点有 2,4,6 共 3 个，故 $P=\\dfrac{3}{6}=\\dfrac{1}{2}$。"))
)},
{"id":"e8s1-2","name":"概率的基本公式","tags":["thm","der"],"brief":"互斥事件加法、独立事件乘法、条件概率。",
"body":wrap(
 thm("互斥事件加法",p("若 $A,B$ 互斥（$A\\cap B=\\varnothing$），则：")+
 fml("P(A\\cup B) = P(A)+P(B)")+
 p("一般情况（容斥）：$P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$。"))+
 thm("独立事件乘法",p("若 $A,B$ 相互独立（$P(A|B)=P(A)$），则：")+
 fml("P(A\\cap B) = P(A)\\cdot P(B)"))+
 defn("条件概率",p("在事件 $B$ 已发生的条件下，事件 $A$ 发生的概率：")+
 fml("P(A|B) = \\dfrac{P(A\\cap B)}{P(B)}\\quad(P(B)>0)"))+
 thm("全概率公式与贝叶斯公式",p("设 $B_1,B_2,\\dots,B_n$ 为样本空间的一个分割，则：")+
 fml("P(A) = \\sum_{i=1}^n P(B_i)P(A|B_i)")+
 fml("P(B_i|A) = \\dfrac{P(B_i)P(A|B_i)}{\\sum_{j=1}^n P(B_j)P(A|B_j)}"))
)}
]},
{"name":"8.2 随机变量与分布","color":"#10b981","desc":"离散型随机变量、二项分布与正态分布",
"items":[
{"id":"e8s2-1","name":"离散型随机变量","tags":["def","thm"],"brief":"分布列、期望与方差。",
"body":wrap(
 defn("分布列",p("设离散型随机变量 $X$ 的可能取值为 $x_1,x_2,\\dots,x_n$，$P(X=x_i)=p_i$，则 $\\begin{pmatrix}x_1&x_2&\\cdots&x_n\\\\ p_1&p_2&\\cdots&p_n\\end{pmatrix}$ 为 $X$ 的分布列，满足 $p_i\\ge 0$，$\\sum p_i=1$。"))+
 defn("数学期望",p("")+
 fml("E(X) = \\sum_{i=1}^n x_i p_i"))+
 defn("方差",p("")+
 fml("D(X) = \\sum_{i=1}^n [x_i-E(X)]^2 p_i = E(X^2)-[E(X)]^2"))+
 note(p("标准差 $\\sigma(X)=\\sqrt{D(X)}$。期望反映平均水平，方差反映波动程度。"))
)},
{"id":"e8s2-2","name":"二项分布与正态分布","tags":["def","thm"],"brief":"n 次独立重复试验与连续型分布。",
"body":wrap(
 defn("二项分布",p("在 $n$ 次独立重复试验中，事件 $A$ 每次发生概率为 $p$，则 $A$ 发生次数 $X\\sim B(n,p)$：")+
 fml("P(X=k) = \\binom{n}{k} p^k (1-p)^{n-k},\\quad k=0,1,\\dots,n"))+
 thm("二项分布的期望与方差",p("")+
 fml("E(X) = np,\\quad D(X) = np(1-p)"))+
 defn("正态分布",p("若随机变量 $X$ 的概率密度为：")+
 fml("f(x) = \\dfrac{1}{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}")+
 p("则 $X\\sim N(\\mu,\\sigma^2)$，其中 $\\mu$ 为期望，$\\sigma^2$ 为方差。图像关于 $x=\\mu$ 对称，呈钟形曲线。"))+
 thm("3σ 原则",p("正态分布中：$P(\\mu-\\sigma<X<\\mu+\\sigma)\\approx 68.3\\%$，$P(\\mu-2\\sigma<X<\\mu+2\\sigma)\\approx 95.4\\%$，$P(\\mu-3\\sigma<X<\\mu+3\\sigma)\\approx 99.7\\%$。"))
)}
]},
{"name":"8.3 统计","color":"#34d399","desc":"抽样、频率分布与统计量",
"items":[
{"id":"e8s3-1","name":"抽样方法与频率分布","tags":["def","exa"],"brief":"简单随机抽样、分层抽样、频率分布直方图。",
"body":wrap(
 defn("抽样方法",p("① <strong>简单随机抽样</strong>：从总体中逐个抽取，每个个体被抽到概率相等；<br>② <strong>分层抽样</strong>：将总体分成若干层，按比例从各层抽取；<br>③ <strong>系统抽样</strong>：将总体均分后按规则抽取。"))+
 defn("频率分布直方图",p("用矩形面积表示各区间频率。矩形面积 = 频率 = 频率/组距 × 组距。所有矩形面积之和为 1。"))+
 note(p("频率分布直方图中，<strong>众数</strong>为最高矩形底边中点；<strong>中位数</strong>为使左右面积各为 0.5 的点。"))
)},
{"id":"e8s3-2","name":"样本数字特征","tags":["def","thm"],"brief":"平均数、方差、标准差与线性回归。",
"body":wrap(
 defn("样本均值与方差",p("样本 $x_1,x_2,\\dots,x_n$：")+
 fml("\\bar{x} = \\dfrac{1}{n}\\sum_{i=1}^n x_i,\\quad s^2 = \\dfrac{1}{n}\\sum_{i=1}^n (x_i-\\bar{x})^2"))+
 defn("线性回归方程",p("两个变量 $x,y$ 的线性回归直线 $\\hat{y}=bx+a$，其中：")+
 fml("b = \\dfrac{\\sum_{i=1}^n (x_i-\\bar{x})(y_i-\\bar{y})}{\\sum_{i=1}^n (x_i-\\bar{x})^2},\\quad a = \\bar{y}-b\\bar{x}"))+
 note(p("回归直线过样本中心点 $(\\bar{x},\\bar{y})$。$|r|$（相关系数）越接近 1，线性相关性越强。"))
)}
]}
]

CHAPTERS = [
{"id":"ch1","num":"第一章","title":"集合与逻辑","en":"SETS & LOGIC","desc":"集合的概念与运算、命题、充要条件，是数学严谨推理的语言基础。","sections":ch1_sections},
{"id":"ch2","num":"第二章","title":"代数","en":"ALGEBRA","desc":"多项式与因式分解、方程与不等式、复数，是运算变形的基本工具。","sections":ch2_sections},
{"id":"ch3","num":"第三章","title":"函数","en":"FUNCTIONS","desc":"函数的概念与性质、基本初等函数（指数、对数、幂、三角）。","sections":ch3_sections},
{"id":"ch4","num":"第四章","title":"数列","en":"SEQUENCES","desc":"等差数列、等比数列的通项与求和，以及数列求和的通用方法。","sections":ch4_sections},
{"id":"ch5","num":"第五章","title":"平面几何","en":"PLANE GEOMETRY","desc":"三角形、圆的性质与定理，正弦定理、余弦定理与圆幂定理。","sections":ch5_sections},
{"id":"ch6","num":"第六章","title":"立体几何","en":"SOLID GEOMETRY","desc":"空间几何体的表面积与体积，线面、面面的平行与垂直关系。","sections":ch6_sections},
{"id":"ch7","num":"第七章","title":"解析几何","en":"ANALYTIC GEOMETRY","desc":"直线与圆、圆锥曲线（椭圆、双曲线、抛物线）及空间解析几何。","sections":ch7_sections},
{"id":"ch8","num":"第八章","title":"概率统计","en":"PROBABILITY & STATISTICS","desc":"古典概型、概率公式、随机变量分布与统计推断。","sections":ch8_sections},
]

def gen_html():
    data_lines = []
    for ch in CHAPTERS:
        sec_strs = []
        for sec in ch["sections"]:
            item_strs = []
            for it in sec["items"]:
                tags_js = json.dumps(it["tags"], ensure_ascii=False)
                body_esc = js_escape(fix_lt_math(it["body"]))
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
  .la-nav-tab.c1{color:#2563eb;border-color:#bfdbfe}
  .la-nav-tab.c2{color:#7c3aed;border-color:#ddd6fe}
  .la-nav-tab.c3{color:#0d9488;border-color:#99f6e4}
  .la-nav-tab.c4{color:#c2410c;border-color:#fed7aa}
  .la-nav-tab.c5{color:#be185d;border-color:#fbcfe8}
  .la-nav-tab.c6{color:#7c3aed;border-color:#ddd6fe}
  .la-nav-tab.c7{color:#0891b2;border-color:#a5f3fc}
  .la-nav-tab.c8{color:#059669;border-color:#a7f3d0}
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
  .la-phase-title.ch1::before{background:#2563eb}
  .la-phase-title.ch2::before{background:#7c3aed}
  .la-phase-title.ch3::before{background:#0d9488}
  .la-phase-title.ch4::before{background:#c2410c}
  .la-phase-title.ch5::before{background:#be185d}
  .la-phase-title.ch6::before{background:#7c3aed}
  .la-phase-title.ch7::before{background:#0891b2}
  .la-phase-title.ch8::before{background:#059669}
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
<meta name="description" content="初等数学知识体系：集合与逻辑、代数、函数、数列、平面几何、立体几何、解析几何、概率统计">
<title>初等数学 · 知识体系</title>
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
    <div class="la-eyebrow">ELEMENTARY MATHEMATICS · KNOWLEDGE MAP</div>
    <h1>初等数学 · 知识体系</h1>
    <p class="la-subtitle">集合与逻辑 · 代数 · 函数 · 数列 · 平面几何 · 立体几何 · 解析几何 · 概率统计</p>
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
    <div>初等数学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于初等数学核心知识体系整理</div>
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
    with open("/workspace/elementary-math.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated elementary-math.html ({len(html)} chars)")
