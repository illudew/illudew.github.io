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
<line x1="58" y1="50" x2="182" y2="60" stroke="#f59e0b" stroke-width="1.3" marker-end="url(#arr2)"/>
<line x1="58" y1="80" x2="182" y2="60" stroke="#f59e0b" stroke-width="1.3"/>
<line x1="58" y1="110" x2="182" y2="100" stroke="#f59e0b" stroke-width="1.3"/>
<defs><marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#f59e0b"/></marker></defs>
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
</svg>''',
"trig_circle": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="56" fill="none" stroke="#2563eb" stroke-width="1.6"/>
<line x1="40" y1="80" x2="200" y2="80" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="16" x2="120" y2="144" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="80" x2="160" y2="40" stroke="#ef4444" stroke-width="1.8"/>
<circle cx="160" cy="40" r="2.5" fill="#ef4444"/>
<line x1="160" y1="40" x2="160" y2="80" stroke="#10b981" stroke-width="1.3" stroke-dasharray="3 2"/>
<line x1="120" y1="80" x2="160" y2="80" stroke="#0ea5e9" stroke-width="1.3"/>
<text x="164" y="38" font-size="10" fill="#ef4444">P(cosθ,sinθ)</text>
<text x="132" y="76" font-size="9" fill="#0ea5e9">cosθ</text>
<text x="164" y="62" font-size="9" fill="#10b981">sinθ</text>
<text x="122" y="22" font-size="10" fill="#2563eb">单位圆</text>
</svg>''',
"sequence": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="130" x2="210" y2="130" stroke="#94a3b8" stroke-width="1"/>
<circle cx="50" cy="110" r="4" fill="#c2410c"/><circle cx="80" cy="90" r="4" fill="#c2410c"/>
<circle cx="110" cy="70" r="4" fill="#c2410c"/><circle cx="140" cy="50" r="4" fill="#c2410c"/>
<circle cx="170" cy="30" r="4" fill="#c2410c"/>
<line x1="50" y1="110" x2="170" y2="30" stroke="#c2410c" stroke-width="1.4" stroke-dasharray="3 3"/>
<text x="42" y="140" font-size="9" fill="#475569">a₁</text><text x="72" y="140" font-size="9" fill="#475569">a₂</text>
<text x="102" y="140" font-size="9" fill="#475569">a₃</text><text x="132" y="140" font-size="9" fill="#475569">a₄</text>
<text x="162" y="140" font-size="9" fill="#475569">a₅</text>
<text x="70" y="36" font-size="11" fill="#c2410c" font-weight="bold">公差 d</text>
</svg>''',
"polar_coord": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="130" x2="210" y2="130" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="140" x2="120" y2="10" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="130" x2="180" y2="70" stroke="#0891b2" stroke-width="1.8"/>
<circle cx="180" cy="70" r="3" fill="#ef4444"/>
<path d="M 150 130 A 30 30 0 0 0 138 112" fill="none" stroke="#f59e0b" stroke-width="1.4"/>
<text x="144" y="118" font-size="10" fill="#f59e0b">θ</text>
<text x="148" y="106" font-size="10" fill="#0891b2">ρ</text>
<text x="184" y="66" font-size="10" fill="#ef4444">P(ρ,θ)</text>
<text x="122" y="126" font-size="10" fill="#475569">O</text>
<text x="206" y="126" font-size="10" fill="#475569">极轴</text>
</svg>''',
"cube": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="70,40 170,40 200,70 100,70" fill="#eef4fb" stroke="#2563eb" stroke-width="1.6"/>
<polygon points="70,40 100,70 100,140 70,110" fill="#dbeafe" stroke="#2563eb" stroke-width="1.6"/>
<polygon points="100,70 200,70 200,140 100,140" fill="#bfdbfe" stroke="#2563eb" stroke-width="1.6"/>
<line x1="170" y1="40" x2="200" y2="70" stroke="#2563eb" stroke-width="1.6"/>
<text x="130" y="110" font-size="11" fill="#1e40af" font-weight="bold">a</text>
<text x="150" y="66" font-size="10" fill="#475569">正方体</text>
</svg>''',
"parabola": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="80" x2="220" y2="80" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="16" x2="120" y2="144" stroke="#94a3b8" stroke-width="1"/>
<path d="M 120 20 Q 200 80 120 140" fill="none" stroke="#0891b2" stroke-width="2"/>
<line x1="60" y1="16" x2="60" y2="144" stroke="#ef4444" stroke-width="1" stroke-dasharray="4 3"/>
<circle cx="150" cy="80" r="2.5" fill="#ef4444"/>
<text x="154" y="76" font-size="10" fill="#ef4444">F(p/2,0)</text>
<text x="40" y="20" font-size="9" fill="#ef4444">x=-p/2</text>
<text x="170" y="146" font-size="10" fill="#0891b2">y²=2px</text>
</svg>''',
"parallelogram": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="40,120 100,60 200,60 140,120" fill="#fde7f3" stroke="#be185d" stroke-width="1.8"/>
<line x1="40" y1="120" x2="40" y2="60" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="4 3"/>
<text x="22" y="92" font-size="10" fill="#ef4444">h</text>
<text x="62" y="124" font-size="10" fill="#be185d">a</text>
<text x="160" y="58" font-size="10" fill="#be185d">b</text>
<text x="80" y="146" font-size="10" fill="#475569">S = a·h = b·a·sinθ</text>
</svg>''',
"sphere": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="56" fill="#ede9fe" fill-opacity="0.45" stroke="#7c3aed" stroke-width="1.8"/>
<ellipse cx="120" cy="80" rx="56" ry="14" fill="none" stroke="#7c3aed" stroke-width="1" stroke-dasharray="3 3"/>
<ellipse cx="120" cy="80" rx="14" ry="56" fill="none" stroke="#7c3aed" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="120" y1="80" x2="176" y2="80" stroke="#ef4444" stroke-width="1.8"/>
<text x="140" y="76" font-size="10" fill="#ef4444">R</text>
<text x="80" y="148" font-size="10" fill="#7c3aed">S=4πR², V=(4/3)πR³</text>
</svg>''',
"helix": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="60" y1="20" x2="60" y2="150" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="180" y1="20" x2="180" y2="150" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<path d="M 60 30 Q 90 40 120 50 Q 150 60 180 50 Q 150 70 120 80 Q 90 90 60 80 Q 90 100 120 110 Q 150 120 180 110 Q 150 130 120 140" fill="none" stroke="#0891b2" stroke-width="2"/>
<text x="120" y="18" font-size="10" fill="#0891b2" font-weight="bold">圆柱螺旋线</text>
<text x="70" y="36" font-size="9" fill="#475569">x=a cos t</text>
<text x="70" y="48" font-size="9" fill="#475569">y=a sin t</text>
<text x="70" y="60" font-size="9" fill="#475569">z=bt</text>
</svg>''',
"quadric": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="20" x2="120" y2="148" stroke="#94a3b8" stroke-width="1"/>
<line x1="40" y1="80" x2="200" y2="80" stroke="#94a3b8" stroke-width="1"/>
<ellipse cx="120" cy="80" rx="75" ry="32" fill="#e0f2fe" fill-opacity="0.5" stroke="#0891b2" stroke-width="1.6"/>
<ellipse cx="120" cy="58" rx="32" ry="10" fill="none" stroke="#0891b2" stroke-width="1.2"/>
<ellipse cx="120" cy="102" rx="50" ry="16" fill="none" stroke="#0891b2" stroke-width="1.2"/>
<text x="80" y="18" font-size="10" fill="#0891b2" font-weight="bold">单叶双曲面</text>
</svg>''',
"normal_dist": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="120" y1="20" x2="120" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<path d="M 40 128 Q 80 128 120 40 Q 160 128 200 128" fill="none" stroke="#10b981" stroke-width="2"/>
<text x="124" y="36" font-size="10" fill="#10b981" font-weight="bold">μ</text>
<text x="60" y="146" font-size="9" fill="#475569">μ-σ</text>
<text x="100" y="146" font-size="9" fill="#475569">μ</text>
<text x="140" y="146" font-size="9" fill="#475569">μ+σ</text>
<text x="180" y="146" font-size="9" fill="#475569">μ+2σ</text>
<text x="40" y="20" font-size="10" fill="#10b981">N(μ,σ²) 钟形曲线</text>
</svg>''',
"number_line": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="80" x2="220" y2="80" stroke="#475569" stroke-width="1.5"/>
<polygon points="220,80 212,76 212,84" fill="#475569"/>
<circle cx="80" cy="80" r="3" fill="#ef4444"/>
<circle cx="120" cy="80" r="3" fill="#ef4444"/>
<line x1="80" y1="60" x2="120" y2="60" stroke="#2563eb" stroke-width="2"/>
<text x="74" y="100" font-size="10" fill="#475569">a</text>
<text x="114" y="100" font-size="10" fill="#475569">b</text>
<text x="92" y="54" font-size="10" fill="#2563eb">|a-b|</text>
<text x="20" y="40" font-size="10" fill="#475569">|x-a| &lt; b</text>
</svg>''',
"abs_value": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="20" x2="120" y2="140" stroke="#94a3b8" stroke-width="1"/>
<path d="M 40 40 L 120 130 L 200 40" fill="none" stroke="#7c3aed" stroke-width="2"/>
<text x="40" y="34" font-size="10" fill="#7c3aed" font-weight="bold">y=|x|</text>
<text x="208" y="124" font-size="10" fill="#475569">x</text>
<text x="124" y="22" font-size="10" fill="#475569">y</text>
<text x="80" y="148" font-size="9" fill="#475569">|ab|=|a||b|</text>
</svg>'''
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","note":"备 注"}

CORE_FORMULAS = [
    ("集合交换律", "A\\cap B = B\\cap A,\\quad A\\cup B = B\\cup A", "交集与并集满足交换律"),
    ("集合结合律", "(A\\cap B)\\cap C = A\\cap(B\\cap C)", "交集与并集满足结合律"),
    ("德摩根律·交", "\\complement_U(A\\cap B) = \\complement_U A \\cup \\complement_U B", "补集对交集的对偶"),
    ("德摩根律·并", "\\complement_U(A\\cup B) = \\complement_U A \\cap \\complement_U B", "补集对并集的对偶"),
    ("容斥原理·二元", "|A\\cup B| = |A|+|B|-|A\\cap B|", "两集合并集的元素个数"),
    ("容斥原理·三元", "|A\\cup B\\cup C| = |A|+|B|+|C|-|A\\cap B|-|B\\cap C|-|C\\cap A|+|A\\cap B\\cap C|", "三集合并集的元素个数"),
    ("子集个数", "|\\mathcal{P}(A)|=2^{|A|}", "n 元集合的子集总数"),
    ("有理数稠密性", "\\forall\\epsilon>0,\\exists r\\in\\mathbb{Q}: |x-r|<\\epsilon", "实数可用有理数逼近"),
    ("绝对值定义", "|a|=\\begin{cases}a,&a\\ge0\\\\-a,&a<0\\end{cases}", "绝对值的分段定义"),
    ("绝对值乘性", "|ab|=|a|\\cdot|b|", "乘积的绝对值等于绝对值之积"),
    ("三角不等式", "|a|-|b|\\le|a\\pm b|\\le|a|+|b|", "绝对值三角不等式"),
    ("完全平方公式", "(a\\pm b)^2 = a^2 \\pm 2ab + b^2", "二项式平方展开"),
    ("平方差公式", "a^2 - b^2 = (a+b)(a-b)", "因式分解基本公式"),
    ("立方和公式", "a^3+b^3 = (a+b)(a^2-ab+b^2)", "立方和分解"),
    ("立方差公式", "a^3-b^3 = (a-b)(a^2+ab+b^2)", "立方差分解"),
    ("三数完全平方", "(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca", "三数和的平方展开"),
    ("二项式定理", "(a+b)^n = \\sum_{k=0}^n \\binom{n}{k} a^{n-k}b^k", "二项式展开"),
    ("一元二次求根", "x = \\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}", "ax²+bx+c=0 的求根公式"),
    ("判别式", "\\Delta = b^2-4ac", "判别二次方程实根个数"),
    ("韦达定理·和", "x_1+x_2=-\\dfrac{b}{a}", "两根之和"),
    ("韦达定理·积", "x_1x_2=\\dfrac{c}{a}", "两根之积"),
    ("有理根定理", "x=\\dfrac{p}{q}\\ (p|a_0,\\ q|a_n)", "整系数多项式有理根的可能值"),
    ("不等式传递性", "a>b,\\ b>c \\Rightarrow a>c", "不等关系的传递"),
    ("基本不等式", "a^2+b^2\\ge 2ab", "平方和非负的推论"),
    ("均值不等式·二元", "\\dfrac{a+b}{2}\\ge\\sqrt{ab}\\ (a,b>0)", "算术平均不小于几何平均"),
    ("均值不等式链", "\\dfrac{2}{\\frac{1}{a}+\\frac{1}{b}}\\le\\sqrt{ab}\\le\\dfrac{a+b}{2}\\le\\sqrt{\\dfrac{a^2+b^2}{2}}", "调和≤几何≤算术≤平方平均"),
    ("绝对值不等式", "|a|-|b|\\le|a\\pm b|\\le|a|+|b|", "三角不等式"),
    ("常见放缩·倒数", "\\dfrac{1}{n}>\\dfrac{1}{n+1}\\ (n>0)", "分子相同分母大者值小"),
    ("常见放缩·平方", "\\dfrac{1}{n^2}<\\dfrac{1}{n(n-1)}\\ (n\\ge2)", "平方裂项放缩"),
    ("常见放缩·阶乘", "n!<n^n\\ (n\\ge2)", "阶乘不超过 n 的 n 次幂"),
    ("常见放缩·指数", "2^n>n^2\\ (n\\ge5)", "指数增长快于多项式"),
    ("常见放缩·对数", "\\ln(1+x)<x\\ (x>0)", "对数上界"),
    ("常见放缩·指数函数", "e^x\\ge 1+x", "指数函数下界"),
    ("常见放缩·正弦", "\\sin x<x\\ (x>0)", "正弦不超过自变量"),
    ("常见放缩·根差", "\\sqrt{n+1}-\\sqrt{n}<\\dfrac{1}{2\\sqrt{n}}", "根式差的有理化放缩"),
    ("同角关系·平方", "\\sin^2\\alpha+\\cos^2\\alpha=1", "正弦余弦平方和为 1"),
    ("同角关系·商", "\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}", "正切等于正弦比余弦"),
    ("同角关系·倒数", "\\cot\\alpha=\\dfrac{1}{\\tan\\alpha},\\ \\sec\\alpha=\\dfrac{1}{\\cos\\alpha},\\ \\csc\\alpha=\\dfrac{1}{\\sin\\alpha}", "余切正割余割定义"),
    ("同角关系·切平方", "1+\\tan^2\\alpha=\\sec^2\\alpha", "正切正割平方关系"),
    ("同角关系·余切平方", "1+\\cot^2\\alpha=\\csc^2\\alpha", "余切余割平方关系"),
    ("诱导公式·π-α", "\\sin(\\pi-\\alpha)=\\sin\\alpha,\\ \\cos(\\pi-\\alpha)=-\\cos\\alpha", "奇变偶不变，符号看象限"),
    ("诱导公式·π/2-α", "\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha,\\ \\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\sin\\alpha", "互余关系"),
    ("和角正弦", "\\sin(\\alpha+\\beta)=\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta", "正弦和角公式"),
    ("和角余弦", "\\cos(\\alpha+\\beta)=\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta", "余弦和角公式"),
    ("差角正切", "\\tan(\\alpha-\\beta)=\\dfrac{\\tan\\alpha-\\tan\\beta}{1+\\tan\\alpha\\tan\\beta}", "正切差角公式"),
    ("倍角正弦", "\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha", "二倍角正弦"),
    ("倍角余弦", "\\cos 2\\alpha=\\cos^2\\alpha-\\sin^2\\alpha=2\\cos^2\\alpha-1=1-2\\sin^2\\alpha", "二倍角余弦三种形式"),
    ("倍角正切", "\\tan 2\\alpha=\\dfrac{2\\tan\\alpha}{1-\\tan^2\\alpha}", "二倍角正切"),
    ("半角正弦", "\\sin\\dfrac{\\alpha}{2}=\\pm\\sqrt{\\dfrac{1-\\cos\\alpha}{2}}", "半角正弦"),
    ("半角余弦", "\\cos\\dfrac{\\alpha}{2}=\\pm\\sqrt{\\dfrac{1+\\cos\\alpha}{2}}", "半角余弦"),
    ("半角正切", "\\tan\\dfrac{\\alpha}{2}=\\dfrac{1-\\cos\\alpha}{\\sin\\alpha}=\\dfrac{\\sin\\alpha}{1+\\cos\\alpha}", "半角正切有理式"),
    ("对数换底", "\\log_a b = \\dfrac{\\log_c b}{\\log_c a}", "对数换底公式"),
    ("对数运算·积", "\\log_a(MN)=\\log_aM+\\log_aN", "积的对数等于对数之和"),
    ("对数运算·商", "\\log_a\\dfrac{M}{N}=\\log_aM-\\log_aN", "商的对数等于对数之差"),
    ("对数运算·幂", "\\log_a M^n = n\\log_a M", "幂的对数"),
    ("指数运算", "a^m\\cdot a^n=a^{m+n},\\ (a^m)^n=a^{mn}", "指数运算法则"),
    ("等差数列通项", "a_n = a_1 + (n-1)d", "公差为 d 的等差数列第 n 项"),
    ("等差数列求和", "S_n = \\dfrac{n(a_1+a_n)}{2} = na_1+\\dfrac{n(n-1)}{2}d", "前 n 项和"),
    ("等差中项", "2A=a+b \\Rightarrow A=\\dfrac{a+b}{2}", "a,b 的等差中项"),
    ("等差片段和", "S_n,\\ S_{2n}-S_n,\\ S_{3n}-S_{2n}\\text{ 成等差，公差 }n^2d", "片段和的等差性质"),
    ("等差求和二次型", "S_n=An^2+Bn\\ (A=\\dfrac{d}{2},B=a_1-\\dfrac{d}{2})", "前 n 项和是 n 的二次函数"),
    ("等比数列通项", "a_n = a_1 q^{n-1}", "公比为 q 的等比数列第 n 项"),
    ("等比数列求和", "S_n = \\dfrac{a_1(1-q^n)}{1-q}\\ (q\\neq 1)", "前 n 项和"),
    ("无穷等比级数", "S = \\dfrac{a_1}{1-q}\\ (|q|<1)", "公比绝对值小于 1 时的和"),
    ("等比中项", "G^2=ab \\Rightarrow G=\\pm\\sqrt{ab}", "a,b 的等比中项"),
    ("等比片段和", "S_n,\\ S_{2n}-S_n,\\ S_{3n}-S_{2n}\\text{ 成等比，公比 }q^n", "片段和的等比性质"),
    ("裂项·相邻", "\\dfrac{1}{n(n+1)}=\\dfrac{1}{n}-\\dfrac{1}{n+1}", "相邻整数乘积的裂项"),
    ("裂项·差为d", "\\dfrac{1}{n(n+d)}=\\dfrac{1}{d}\\left(\\dfrac{1}{n}-\\dfrac{1}{n+d}\\right)", "差为 d 的裂项"),
    ("平方和公式", "\\sum_{k=1}^n k^2=\\dfrac{n(n+1)(2n+1)}{6}", "前 n 个自然数平方和"),
    ("立方和公式", "\\sum_{k=1}^n k^3=\\left[\\dfrac{n(n+1)}{2}\\right]^2", "前 n 个自然数立方和"),
    ("勾股定理", "a^2+b^2 = c^2", "直角三角形两直角边平方和等于斜边平方"),
    ("正弦定理", "\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R", "三角形边与对角正弦之比"),
    ("余弦定理", "c^2 = a^2+b^2-2ab\\cos C", "已知两边夹角求第三边"),
    ("三角形面积·底高", "S = \\dfrac{1}{2}ah", "底乘高除以二"),
    ("三角形面积·夹角", "S = \\dfrac{1}{2}ab\\sin C", "两边及其夹角求面积"),
    ("海伦公式", "S = \\sqrt{p(p-a)(p-b)(p-c)},\\ p=\\dfrac{a+b+c}{2}", "已知三边求面积"),
    ("三角形面积·内切圆", "S = pr = \\dfrac{1}{2}(a+b+c)r", "内切圆半径法"),
    ("平行四边形面积", "S = ah = ab\\sin\\theta", "底乘高或两边夹角"),
    ("矩形面积", "S = ab", "长乘宽"),
    ("菱形面积", "S = \\dfrac{1}{2}d_1d_2", "对角线乘积一半"),
    ("正方形面积", "S = a^2", "边长平方"),
    ("梯形面积", "S = \\dfrac{(a+b)h}{2}", "上底加下底乘高除以二"),
    ("梯形中位线", "m=\\dfrac{a+b}{2}", "梯形中位线长"),
    ("圆周长", "C = 2\\pi r", "圆的周长公式"),
    ("圆面积", "S = \\pi r^2", "圆的面积公式"),
    ("垂径定理", "CD\\perp AB \\Rightarrow AE=EB", "垂直于弦的直径平分弦"),
    ("圆心角定理", "\\angle AOB = 2\\angle ACB", "圆心角等于两倍圆周角"),
    ("圆周角定理", "\\angle ACB = \\dfrac{1}{2}\\angle AOB", "同弧所对圆周角是圆心角之半"),
    ("切线性质", "PT\\perp OT", "切线垂直于过切点的半径"),
    ("切线长定理", "PA=PB", "从圆外一点引两切线长相等"),
    ("切割线定理", "PT^2 = PA\\cdot PB", "切线长是割线两段的比例中项"),
    ("相交弦定理", "PA\\cdot PB = PC\\cdot PD", "圆内两弦交点分四段比例"),
    ("扇形弧长", "l = \\alpha r = \\dfrac{n\\pi r}{180}", "弧长与圆心角关系"),
    ("扇形面积", "S = \\dfrac{1}{2}lr = \\dfrac{1}{2}\\alpha r^2", "扇形面积公式"),
    ("弓形面积", "S = \\dfrac{1}{2}r^2(\\alpha-\\sin\\alpha)", "扇形减三角形"),
    ("球表面积", "S = 4\\pi R^2", "球面面积"),
    ("球体积", "V = \\dfrac{4}{3}\\pi R^3", "球的体积"),
    ("圆柱体积", "V = \\pi r^2 h", "底面积乘高"),
    ("圆柱侧面积", "S_{\\text{侧}} = 2\\pi rh", "圆柱侧面积"),
    ("圆锥体积", "V = \\dfrac{1}{3}\\pi r^2 h", "同底等高圆柱体积的 1/3"),
    ("圆锥侧面积", "S_{\\text{侧}} = \\pi rl", "母线长为 l 的圆锥侧面积"),
    ("圆台体积", "V = \\dfrac{1}{3}\\pi h(R^2+Rr+r^2)", "上下底半径 R,r 的圆台体积"),
    ("棱柱体积", "V_{\\text{柱}} = Sh", "底面积乘高"),
    ("棱锥体积", "V_{\\text{锥}} = \\dfrac{1}{3}Sh", "锥体积是同底等高柱的 1/3"),
    ("台体体积", "V_{\\text{台}} = \\dfrac{1}{3}h(S_{\\text{上}}+\\sqrt{S_{\\text{上}}S_{\\text{下}}}+S_{\\text{下}})", "台体体积一般公式"),
    ("线面角", "\\sin\\theta=\\dfrac{|\\vec{s}\\cdot\\vec{n}|}{|\\vec{s}||\\vec{n}|}", "线面角的正弦"),
    ("二面角", "\\cos\\varphi=\\pm\\dfrac{\\vec{n_1}\\cdot\\vec{n_2}}{|\\vec{n_1}||\\vec{n_2}|}", "二面角的余弦"),
    ("点面距离", "d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}", "点到平面距离"),
    ("两点距离", "d = \\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}", "平面内两点间距离"),
    ("点到直线距离", "d = \\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}", "点到直线 Ax+By+C=0 的距离"),
    ("直线斜率", "k = \\dfrac{y_2-y_1}{x_2-x_1} = \\tan\\alpha", "斜率与倾斜角关系"),
    ("圆方程", "(x-a)^2+(y-b)^2 = r^2", "圆心 (a,b) 半径 r 的圆"),
    ("椭圆标准方程", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2} = 1\\ (a>b>0)", "焦点在 x 轴的椭圆"),
    ("椭圆离心率", "e=\\dfrac{c}{a}\\in(0,1),\\ c^2=a^2-b^2", "椭圆扁平程度"),
    ("双曲线标准方程", "\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2} = 1", "焦点在 x 轴的双曲线"),
    ("双曲线渐近线", "y=\\pm\\dfrac{b}{a}x", "双曲线渐近线方程"),
    ("双曲线离心率", "e=\\dfrac{c}{a}>1,\\ c^2=a^2+b^2", "双曲线离心率大于 1"),
    ("抛物线标准方程", "y^2 = 2px\\ (p>0)", "开口向右的抛物线"),
    ("极坐标互化", "x=\\rho\\cos\\theta,\\ y=\\rho\\sin\\theta,\\ \\rho^2=x^2+y^2", "极坐标与直角坐标互化"),
    ("柱坐标关系", "x=\\rho\\cos\\theta,\\ y=\\rho\\sin\\theta,\\ z=z", "柱坐标与直角坐标关系"),
    ("球坐标关系", "x=r\\sin\\varphi\\cos\\theta,\\ y=r\\sin\\varphi\\sin\\theta,\\ z=r\\cos\\varphi", "球坐标与直角坐标关系"),
    ("空间直线对称式", "\\dfrac{x-x_0}{m}=\\dfrac{y-y_0}{n}=\\dfrac{z-z_0}{p}", "过点方向向量的直线"),
    ("空间两点距离", "|P_1P_2| = \\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}", "空间两点距离"),
    ("平面点法式", "A(x-x_0)+B(y-y_0)+C(z-z_0)=0", "过点法向量的平面"),
    ("椭球面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}+\\dfrac{z^2}{c^2}=1", "椭球面标准方程"),
    ("单叶双曲面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=1", "单叶双曲面"),
    ("双叶双曲面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=-1", "双叶双曲面"),
    ("椭圆抛物面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=z", "椭圆抛物面"),
    ("双曲抛物面", "\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=z", "马鞍面"),
    ("二次锥面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=0", "二次锥面"),
    ("圆柱螺旋线", "x=a\\cos t,\\ y=a\\sin t,\\ z=bt", "圆柱螺旋线参数方程"),
    ("螺旋线弧长", "s=\\sqrt{a^2+b^2}\\cdot t", "螺旋线一段弧长"),
    ("排列数", "A_n^m = n(n-1)\\cdots(n-m+1)=\\dfrac{n!}{(n-m)!}", "从 n 个中取 m 个的排列数"),
    ("组合数", "C_n^m = \\dfrac{A_n^m}{m!}=\\dfrac{n!}{m!(n-m)!}", "从 n 个中取 m 个的组合数"),
    ("组合恒等式·对称", "C_n^m = C_n^{n-m}", "组合数对称性"),
    ("组合恒等式·帕斯卡", "C_n^m = C_{n-1}^m+C_{n-1}^{m-1}", "帕斯卡恒等式"),
    ("二项式通项", "T_{k+1}=\\binom{n}{k}a^{n-k}b^k", "二项展开第 k+1 项"),
    ("古典概型", "P(A) = \\dfrac{m}{n}", "事件 A 包含 m 个基本事件，共 n 个等可能基本事件"),
    ("互斥事件加法", "P(A\\cup B) = P(A)+P(B)", "A、B 互斥时的概率加法"),
    ("独立事件乘法", "P(A\\cap B) = P(A)\\cdot P(B)", "A、B 独立时的概率乘法"),
    ("条件概率", "P(A|B) = \\dfrac{P(A\\cap B)}{P(B)}", "B 发生条件下 A 发生的概率"),
    ("全概率公式", "P(A) = \\sum_i P(B_i)P(A|B_i)", "由分割 B_i 求 A 的概率"),
    ("贝叶斯公式", "P(B_i|A) = \\dfrac{P(B_i)P(A|B_i)}{\\sum_j P(B_j)P(A|B_j)}", "后验概率公式"),
    ("期望", "E(X) = \\sum_i x_i p_i", "离散型随机变量的数学期望"),
    ("方差", "D(X) = E[(X-E(X))^2] = E(X^2)-[E(X)]^2", "随机变量的方差"),
    ("二项分布概率", "P(X=k)=\\binom{n}{k}p^k(1-p)^{n-k}", "X~B(n,p) 的分布列"),
    ("二项分布期望方差", "E(X)=np,\\ D(X)=np(1-p)", "二项分布的期望与方差"),
    ("正态分布密度", "f(x) = \\dfrac{1}{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}", "N(μ,σ²) 的概率密度"),
    ("3σ 原则", "P(\\mu-3\\sigma<X<\\mu+3\\sigma)\\approx 99.7\\%", "正态分布的 3σ 范围"),
    ("样本均值", "\\bar{x} = \\dfrac{1}{n}\\sum_{i=1}^n x_i", "样本算术平均值"),
    ("样本方差", "s^2 = \\dfrac{1}{n}\\sum_{i=1}^n (x_i-\\bar{x})^2", "样本方差"),
    ("线性回归斜率", "b = \\dfrac{\\sum(x_i-\\bar{x})(y_i-\\bar{y})}{\\sum(x_i-\\bar{x})^2}", "回归直线斜率"),
    ("反三角关系", "\\arcsin x+\\arccos x=\\dfrac{\\pi}{2}", "反正弦与反余弦互补"),
    ("反三角恒等", "\\tan(\\arctan x)=x,\\ \\sin(\\arcsin x)=x", "反三角函数的还原性"),
]

def js_escape(s): return s.replace("\\","\\\\").replace("`","\\`").replace("${","\\${")
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
{"name":"1.1 集合及其运算","color":"#2563eb","desc":"集合概念、交并补运算与德摩根律",
"items":[
{"id":"e1s1-1","name":"集合的概念与表示","tags":["def","exa","der"],"brief":"集合是确定对象的全体，常用列举法、描述法表示。",
"body":wrap(
 defn("集合与元素",p("具有某种特定性质的事物的总体称为<strong>集合</strong>，组成集合的事物称为<strong>元素</strong>。若 $a$ 是集合 $A$ 的元素，记 $a\\in A$；否则 $a\\notin A$。"))+
 note(p("集合中元素具有<strong>确定性、互异性、无序性</strong>三大特性。确定性要求能判断任一对象是否属于该集合；互异性要求元素不重复；无序性要求元素排列顺序不影响集合相等。"))+
 der(p("<strong>互异性的推论：</strong>若 $\\{1,2,a\\}=\\{1,2,3\\}$，则 $a$ 只能等于 3，因为集合中已有 1 和 2，由互异性 $a$ 不能取 1 或 2，否则会出现重复元素，与互异性矛盾。")+
 p("<strong>子集个数推导：</strong>对 $n$ 元集合 $A$，构造子集时每个元素有「属于」或「不属于」两种选择，由乘法原理子集总数为 $2\\times2\\times\\cdots\\times2=2^n$。"))+
 exa(p("<strong>常见数集：</strong>$\\mathbb{N}$ 自然数集、$\\mathbb{Z}$ 整数集、$\\mathbb{Q}$ 有理数集、$\\mathbb{R}$ 实数集。<br>集合的表示方法：① <strong>列举法</strong> $A=\\{1,2,3\\}$；② <strong>描述法</strong> $A=\\{x\\mid x>0, x\\in\\mathbb{R}\\}$；③ <strong>图示法</strong>（韦恩图）。"))
)},
{"id":"e1s1-2","name":"集合的交、并、补与德摩根律","tags":["def","thm","der"],"brief":"交集、并集、补集的定义与德摩根律推导。",
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
 der(p("<strong>第一式推导（双向包含）：</strong>任取 $x\\in\\complement_U(A\\cap B)$，则 $x\\notin A\\cap B$，即 $x\\notin A$ 或 $x\\notin B$，故 $x\\in\\complement_U A$ 或 $x\\in\\complement_U B$，即 $x\\in\\complement_U A\\cup\\complement_U B$，故左 $\\subseteq$ 右。")+
 p("反向：任取 $x\\in\\complement_U A\\cup\\complement_U B$，则 $x\\notin A$ 或 $x\\notin B$，即 $x\\notin A\\cap B$，故 $x\\in\\complement_U(A\\cap B)$，右 $\\subseteq$ 左。两边相等得证。")+
 p("第二式可由第一式取补集的对偶得到：将第一式中的 $A\\cap B$ 换为 $\\complement_U(A\\cup B)$，再两边取补，得 $\\complement_U(A\\cup B)=\\complement_U A\\cap\\complement_U B$。")))
]}
],
"items2":[
{"id":"e1s2-1","name":"子集与容斥原理","tags":["def","thm","der","exa"],"brief":"子集、真子集、集合相等与容斥原理。",
"body":wrap(
 defn("子集",p("若集合 A 的每一个元素都属于 B，则称 A 是 B 的<strong>子集</strong>，记作 $A\\subseteq B$。若 $A\\subseteq B$ 且 $B\\subseteq A$，则 $A=B$。"))+
 defn("真子集",p("若 $A\\subseteq B$ 且存在 $b\\in B$ 使 $b\\notin A$，则称 A 是 B 的<strong>真子集</strong>，记作 $A\\subsetneq B$。"))+
 thm("子集个数",p("含有 $n$ 个元素的集合共有 $2^n$ 个子集，$2^n-1$ 个真子集，$2^n-2$ 个非空真子集。"))+
 der(p("<strong>推导：</strong>对集合 A 的每个元素，在构造子集时都有「选」或「不选」两种可能。$n$ 个元素共有 $2\\times2\\times\\cdots\\times2=2^n$ 种组合，故子集总数为 $2^n$。去掉集合本身得真子集 $2^n-1$ 个，再去掉空集得非空真子集 $2^n-2$ 个。"))+
 thm("二元容斥原理",p("设 A、B 为有限集，则：")+
 fml("|A\\cup B| = |A|+|B|-|A\\cap B|"))+
 der(p("<strong>推导：</strong>$|A|+|B|$ 把 $A\\cap B$ 的元素算了两次（一次在 A 中，一次在 B 中），因此需要减去重复计算的 $|A\\cap B|$，才得到 $A\\cup B$ 的真实元素个数。")+
 p("<strong>三元情形：</strong>$|A\\cup B\\cup C| = |A|+|B|+|C|-|A\\cap B|-|B\\cap C|-|C\\cap A|+|A\\cap B\\cap C|$。先加 $|A|+|B|+|C|$，其中两两交集被多加一次故减去，但 $A\\cap B\\cap C$ 被加了 3 次又减了 3 次恰好抵消为 0，需再加回一次。"))+
 exa(p("<strong>例：</strong>某班 50 人，喜欢数学 30 人，喜欢物理 25 人，两科都喜欢 15 人。两科至少喜欢一科的人数 $=30+25-15=40$ 人。")))
]}
],
"items3":[
{"id":"e1s3-1","name":"命题与四种命题","tags":["def","thm","der"],"brief":"原命题、逆命题、否命题、逆否命题的关系。",
"body":wrap(
 defn("命题",p("可以判断真假的陈述句称为<strong>命题</strong>。判断为真的叫真命题，判断为假的叫假命题。"))+
 p("设原命题为「若 p，则 q」，则：① <strong>逆命题</strong>：若 q，则 p；② <strong>否命题</strong>：若 $\\neg p$，则 $\\neg q$；③ <strong>逆否命题</strong>：若 $\\neg q$，则 $\\neg p$。")+
 thm("等价性",p("原命题与其逆否命题同真同假（等价）；逆命题与否命题同真同假。但原命题与逆命题、否命题的真假无必然联系。"))+
 der(p("<strong>逆否命题等价性推导：</strong>「若 p 则 q」等价于「$p\\Rightarrow q$」，其逆否为「$\\neg q\\Rightarrow\\neg p$」。用真值表验证：当 p 真 q 真时，$\\neg q$ 假，$\\neg q\\Rightarrow\\neg p$ 为真，两者都真；p 真 q 假时原命题假，$\\neg q$ 真 $\\neg p$ 假，逆否为假；p 假时两者都真。故原命题与逆否命题真值完全相同。")))
},
{"id":"e1s3-2","name":"充要条件与量词","tags":["def","exa","der"],"brief":"充要条件的判定与全称、存在量词。",
"body":wrap(
 defn("充分条件与必要条件",p("若 $p\\Rightarrow q$（p 推出 q），则称 p 是 q 的<strong>充分条件</strong>，q 是 p 的<strong>必要条件</strong>。"))+
 defn("充要条件",p("若 $p\\Leftrightarrow q$（p 与 q 可互推），则称 p 是 q 的<strong>充要条件</strong>。"))+
 der(p("<strong>从集合角度看：</strong>设 $P=\\{x\\mid p(x)\\text{ 成立}\\}$，$Q=\\{x\\mid q(x)\\text{ 成立}\\}$。若 $p\\Rightarrow q$，则 $P\\subseteq Q$（满足 p 的必满足 q）。故 p 是 q 的充分条件 $\\Leftrightarrow$ $P\\subseteq Q$；p 是 q 的充要条件 $\\Leftrightarrow$ $P=Q$。"))+
 exa(p("<strong>例：</strong>「$x=1$」是「$x^2=1$」的充分不必要条件（$x=1\\Rightarrow x^2=1$，但 $x^2=1$ 时 $x$ 也可为 $-1$，故 $\\{1\\}\\subsetneq\\{-1,1\\}$）。"))+
 defn("全称量词与存在量词",p("<strong>全称量词</strong> $\\forall$ 表示「对任意」，<strong>存在量词</strong> $\\exists$ 表示「存在」。全称命题 $\\forall x\\in M, p(x)$ 的否定为 $\\exists x\\in M, \\neg p(x)$；存在命题的否定为全称命题。"))+
 der(p("<strong>量词否定推导：</strong>$\\forall x, p(x)$ 表示「对所有 $x$ 都有 $p(x)$ 成立」，其否定是「并非所有 $x$ 都使 $p(x)$ 成立」，即「存在 $x$ 使 $p(x)$ 不成立」，记作 $\\exists x, \\neg p(x)$。这正是「$\\forall$ 与 $\\exists$ 互换、并否定后件」的规则。")))
}
]
}

# ============ 第二章 代数 ============
ch2_sections = [
{"name":"2.1 数系基础","color":"#7c3aed","desc":"实数、有理数、运算律与绝对值",
"items":[
{"id":"e2s1-1","name":"实数、有理数与运算律","tags":["def","thm","der"],"brief":"数系分类与加减乘除运算律。",
"body":wrap(
 defn("数系",p("<strong>自然数集</strong> $\\mathbb{N}$：$\\{0,1,2,\\dots\\}$；<strong>整数集</strong> $\\mathbb{Z}$：含正负整数与零；<strong>有理数集</strong> $\\mathbb{Q}$：可表为 $\\dfrac{p}{q}$（$p\\in\\mathbb{Z},q\\in\\mathbb{N}^*$，互质）的数；<strong>实数集</strong> $\\mathbb{R}$：有理数与无理数（如 $\\sqrt{2},\\pi$）的全体。关系 $\\mathbb{N}\\subset\\mathbb{Z}\\subset\\mathbb{Q}\\subset\\mathbb{R}$。"))+
 thm("运算律",p("对 $a,b,c\\in\\mathbb{R}$：")+
 fml("\\text{交换律：}\\ a+b=b+a,\\ ab=ba")+
 fml("\\text{结合律：}\\ (a+b)+c=a+(b+c),\\ (ab)c=a(bc)")+
 fml("\\text{分配律：}\\ a(b+c)=ab+ac"))+
 der(p("<strong>有理数稠密性推导：</strong>对任意实数 $x$ 和任意 $\\epsilon>0$，取 $n>\\dfrac{1}{\\epsilon}$（由阿基米德性质存在），则 $\\dfrac{1}{n}<\\epsilon$。设 $m=\\lfloor nx\\rfloor$（不超过 $nx$ 的最大整数），则 $m\\le nx<m+1$，即 $\\dfrac{m}{n}\\le x<\\dfrac{m+1}{n}$。取 $r=\\dfrac{m}{n}\\in\\mathbb{Q}$，则 $|x-r|<\\dfrac{1}{n}<\\epsilon$。故有理数在实数中稠密，即任意实数都可用有理数任意逼近。"))
)},
{"id":"e2s1-2","name":"绝对值定义与性质","tags":["def","thm","der","app"],"brief":"|a| 几何意义、|ab|=|a||b|、三角不等式。",
"fig":"abs_value","figCap":"y=|x| 图像，V 形折线，顶点在原点",
"body":wrap(
 defn("绝对值",p("实数 $a$ 的<strong>绝对值</strong>定义为：")+
 fml("|a|=\\begin{cases}a,&a\\ge 0\\\\-a,&a<0\\end{cases}"))+
 p("几何意义：$|a|$ 表示数 $a$ 在数轴上到原点的距离；$|a-b|$ 表示 $a$ 与 $b$ 在数轴上的距离。")+
 thm("绝对值性质",p("")+
 fml("|ab|=|a|\\cdot|b|,\\quad \\left|\\dfrac{a}{b}\\right|=\\dfrac{|a|}{|b|}\\ (b\\neq 0)")+
 fml("|a|^2=a^2,\\quad |a|=\\sqrt{a^2}")+
 fml("|a|-|b|\\le|a+b|\\le|a|+|b|\\ (\\text{三角不等式})"))+
 der(p("<strong>$|ab|=|a||b|$ 推导：</strong>分情况讨论。若 $a\\ge 0, b\\ge 0$，则 $ab\\ge 0$，$|ab|=ab=|a||b|$；若 $a\\ge 0, b<0$，则 $ab\\le 0$，$|ab|=-ab=|a|\\cdot(-b)=|a||b|$；其他两种情形类似。综合四种情况恒有 $|ab|=|a||b|$。")+
 p("<strong>三角不等式推导：</strong>由 $-|a|\\le a\\le |a|$ 与 $-|b|\\le b\\le |b|$ 相加得 $-(|a|+|b|)\\le a+b\\le |a|+|b|$，即 $|a+b|\\le |a|+|b|$。等号成立当且仅当 $ab\\ge 0$（同号或之一为零）。将 $b$ 换为 $-b$ 得 $|a-b|\\le |a|+|b|$。又 $|a|=|(a+b)+(-b)|\\le |a+b|+|b|$，故 $|a|-|b|\\le |a+b|$，即下界成立。"))+
 app(p("<strong>解 $|x-a|+|x-b|=c$ 型不等式：</strong>利用绝对值几何意义（数轴距离），将问题转化为数轴上动点到两定点距离之和的取值。"))
)}
]},
{"name":"2.2 整式运算与乘法公式","color":"#8b5cf6","desc":"多项式运算、乘法公式与因式分解",
"items":[
{"id":"e2s2-1","name":"多项式与乘法公式","tags":["thm","der","exa"],"brief":"平方差、完全平方、立方和差、三数完全平方。",
"body":wrap(
 thm("幂的运算法则",p("同底数幂相乘、幂的乘方、积的乘方：")+
 fml("a^m\\cdot a^n = a^{m+n},\\quad (a^m)^n = a^{mn},\\quad (ab)^n = a^n b^n"))+
 thm("平方差公式",p("")+
 fml("(a+b)(a-b)=a^2-b^2"))+
 der(p("<strong>平方差推导：</strong>$(a+b)(a-b)=a^2-ab+ab-b^2=a^2-b^2$，交叉项 $-ab$ 与 $+ab$ 抵消。"))+
 thm("完全平方公式",p("")+
 fml("(a\\pm b)^2=a^2 \\pm 2ab + b^2"))+
 der(p("<strong>完全平方推导：</strong>$(a+b)^2=(a+b)(a+b)=a^2+ab+ba+b^2=a^2+2ab+b^2$。差号情形把 $b$ 换为 $-b$ 即得 $(a-b)^2=a^2-2ab+b^2$。"))+
 thm("立方和与立方差公式",p("")+
 fml("a^3+b^3=(a+b)(a^2-ab+b^2),\\quad a^3-b^3=(a-b)(a^2+ab+b^2)"))+
 der(p("<strong>立方和推导：</strong>$(a+b)(a^2-ab+b^2)=a^3-a^2b+ab^2+a^2b-ab^2+b^3=a^3+b^3$，交叉项 $-a^2b$ 与 $+a^2b$、$+ab^2$ 与 $-ab^2$ 抵消。")+
 p("<strong>立方差推导：</strong>把立方和中的 $b$ 换为 $-b$，得 $a^3+(-b)^3=(a-b)(a^2+a b+b^2)$，即 $a^3-b^3=(a-b)(a^2+ab+b^2)$。"))+
 thm("三数完全平方",p("")+
 fml("(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca"))+
 der(p("<strong>三数完全平方推导：</strong>$(a+b+c)^2=(a+b+c)(a+b+c)=a^2+ab+ac+ab+b^2+bc+ac+bc+c^2$。合并同类项：$a^2+b^2+c^2+2ab+2bc+2ca$。推广：$n$ 个数和的平方等于各数平方和加上两两乘积的二倍。"))+
 exa(p("<strong>例：</strong>化简 $(x+3)(x-3)+(x+3)^2$。原式 $=(x^2-9)+(x^2+6x+9)=2x^2+6x$。")))
]},
{"id":"e2s2-2","name":"因式分解方法","tags":["def","exa","der"],"brief":"提公因式、公式法、十字相乘、分组分解。",
"body":wrap(
 defn("因式分解",p("把一个多项式化为几个整式乘积的形式，称为<strong>因式分解</strong>。分解必须进行到每一个因式都不能再分解为止（在指定数域内）。"))+
 p("常用方法：① <strong>提公因式法</strong>：$ma+mb+mc=m(a+b+c)$；② <strong>公式法</strong>：套用乘法公式；③ <strong>十字相乘法</strong>：$x^2+(p+q)x+pq=(x+p)(x+q)$；④ <strong>分组分解法</strong>：适当分组后提取公因式。")+
 der(p("<strong>十字相乘法原理：</strong>$(x+p)(x+q)=x^2+qx+px+pq=x^2+(p+q)x+pq$。因此对二次三项式 $x^2+bx+c$，找到 $p,q$ 使 $p+q=b$，$pq=c$，即可分解为 $(x+p)(x+q)$。对一般二次式 $ax^2+bx+c$，将 $ax^2$ 拆为 $a_1x\\cdot a_2x$，$c$ 拆为 $c_1\\cdot c_2$，使交叉相乘之和 $a_1c_2+a_2c_1=b$。"))+
 exa(p("<strong>例 1：</strong>分解 $x^3-3x^2+2x$。先提公因式 $x$ 得 $x(x^2-3x+2)$，再对二次式十字相乘：找 $p+q=-3$，$pq=2$，得 $p=-1,q=-2$，故 $x^2-3x+2=(x-1)(x-2)$。原式 $=x(x-1)(x-2)$。")+
 p("<strong>例 2：</strong>分组分解 $ax+ay+bx+by$。分两组 $(ax+ay)+(bx+by)=a(x+y)+b(x+y)=(a+b)(x+y)$。")))
]}
]},
{"name":"2.3 方程","color":"#a855f7","desc":"一次方程、一元二次方程与高次方程",
"items":[
{"id":"e2s3-1","name":"一次方程与二元一次方程组","tags":["def","thm","der"],"brief":"一元一次方程与二元一次方程组的消元法。",
"body":wrap(
 defn("一元一次方程",p("形如 $ax+b=0$（$a\\neq 0$）的方程，解为 $x=-\\dfrac{b}{a}$。"))+
 defn("二元一次方程组",p("由两个二元一次方程组成的方程组，解法有<strong>代入消元法</strong>和<strong>加减消元法</strong>。"))+
 der(p("<strong>加减消元法推导：</strong>设方程组 $\\begin{cases}a_1x+b_1y=c_1\\\\a_2x+b_2y=c_2\\end{cases}$。将第一个方程乘 $a_2$，第二个乘 $a_1$，得 $a_1a_2x+a_2b_1y=a_2c_1$ 和 $a_1a_2x+a_1b_2y=a_1c_2$。两式相减消去 $x$：$(a_2b_1-a_1b_2)y=a_2c_1-a_1c_2$，解出 $y=\\dfrac{a_2c_1-a_1c_2}{a_2b_1-a_1b_2}$ 再代回求 $x$。")+
 p("<strong>代入消元法：</strong>从一个方程解出一个变量（如 $x=\\dfrac{c_1-b_1y}{a_1}$），代入另一个方程化为一元方程求解。"))+
 exa(p("<strong>例：</strong>$\\begin{cases}2x+y=5\\\\x-y=1\\end{cases}$。两式相加：$3x=6$，$x=2$，代入得 $y=1$。")))
},
{"id":"e2s3-2","name":"一元二次方程","tags":["thm","der"],"brief":"求根公式推导、判别式、韦达定理推导。",
"fig":"quadratic","figCap":"二次函数 y=ax²+bx+c 图像，开口向上，顶点在 x 轴上方",
"body":wrap(
 thm("求根公式",p("一元二次方程 $ax^2+bx+c=0\\ (a\\neq 0)$ 的解为：")+
 fml("x = \\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}"))+
 der(p("<strong>配方法推导：</strong>两边除以 $a$：$x^2+\\dfrac{b}{a}x+\\dfrac{c}{a}=0$。移项并配方：$x^2+\\dfrac{b}{a}x+\\dfrac{b^2}{4a^2}=\\dfrac{b^2}{4a^2}-\\dfrac{c}{a}$。")+
 fml("\\left(x+\\dfrac{b}{2a}\\right)^2 = \\dfrac{b^2-4ac}{4a^2}")+
 p("当 $\\Delta=b^2-4ac\\ge 0$ 时两边开方：$x+\\dfrac{b}{2a}=\\pm\\dfrac{\\sqrt{\\Delta}}{2a}$，移项得求根公式。"))+
 thm("判别式与根的关系",p("$\\Delta=b^2-4ac$：$\\Delta>0$ 两个不相等实根；$\\Delta=0$ 两个相等实根；$\\Delta<0$ 无实根。"))+
 thm("韦达定理",p("若方程两根为 $x_1,x_2$，则：")+
 fml("x_1+x_2=-\\dfrac{b}{a},\\quad x_1x_2=\\dfrac{c}{a}"))+
 der(p("<strong>韦达定理推导：</strong>由求根公式 $x_1=\\dfrac{-b+\\sqrt{\\Delta}}{2a}$，$x_2=\\dfrac{-b-\\sqrt{\\Delta}}{2a}$。相加：$x_1+x_2=\\dfrac{-2b}{2a}=-\\dfrac{b}{a}$。相乘：$x_1x_2=\\dfrac{(-b)^2-(\\sqrt{\\Delta})^2}{4a^2}=\\dfrac{b^2-(b^2-4ac)}{4a^2}=\\dfrac{4ac}{4a^2}=\\dfrac{c}{a}$。")))
},
{"id":"e2s3-3","name":"高次方程与有理根定理","tags":["thm","der","exa"],"brief":"因式分解降次与有理根定理。",
"body":wrap(
 defn("高次方程",p("次数 $n\\ge 3$ 的整式方程称为高次方程，基本解法是<strong>降次</strong>：通过因式分解化为低次方程求解。"))+
 thm("因式定理",p("多项式 $f(x)$ 有因式 $(x-a)$ 当且仅当 $f(a)=0$，即 $a$ 是方程 $f(x)=0$ 的根。"))+
 der(p("<strong>因式定理推导：</strong>用带余除法，$f(x)=(x-a)q(x)+r$，其中 $r$ 为常数（因为除式 $x-a$ 是一次）。代入 $x=a$：$f(a)=0\\cdot q(a)+r=r$。故 $f(a)=0$ 当且仅当 $r=0$，即 $(x-a)$ 是 $f(x)$ 的因式。"))+
 thm("有理根定理",p("若整系数多项式 $f(x)=a_nx^n+\\cdots+a_1x+a_0$ 有有理根 $\\dfrac{p}{q}$（$p,q$ 互质），则 $p$ 整除常数项 $a_0$，$q$ 整除首项系数 $a_n$。"))+
 der(p("<strong>有理根定理推导：</strong>设 $f\\left(\\dfrac{p}{q}\\right)=0$，即 $a_n\\dfrac{p^n}{q^n}+\\cdots+a_1\\dfrac{p}{q}+a_0=0$。两边乘 $q^n$：$a_np^n+a_{n-1}p^{n-1}q+\\cdots+a_1pq^{n-1}+a_0q^n=0$。除最后一项外各项含因子 $p$，故 $a_0q^n$ 必被 $p$ 整除；又 $\\gcd(p,q)=1$ 故 $\\gcd(p,q^n)=1$，因此 $p|a_0$。同理可证 $q|a_n$。"))+
 exa(p("<strong>例：</strong>解方程 $x^3-2x^2-x+2=0$。常数项 2 的因数有 $\\pm1,\\pm2$，首项系数 1 的因数为 $\\pm1$，故可能有理根为 $\\pm1,\\pm2$。试根：$f(1)=0$，故 $(x-1)$ 是因式。多项式除法得 $f(x)=(x-1)(x^2-x-2)=(x-1)(x-2)(x+1)$，根为 $x=1,2,-1$。")))
]},
{"name":"2.4 不等式","color":"#c026d3","desc":"不等式性质、一元二次不等式、均值不等式与放缩",
"items":[
{"id":"e2s4-1","name":"不等式性质与一元二次不等式","tags":["thm","der","exa"],"brief":"不等式基本性质与一元二次不等式的图像法。",
"body":wrap(
 thm("不等式基本性质",p("① 对称性：$a>b\\Leftrightarrow b<a$；② 传递性：$a>b,\\ b>c\\Rightarrow a>c$；③ 可加性：$a>b\\Rightarrow a+c>b+c$；④ 乘正数不变向：$a>b,\\ c>0\\Rightarrow ac>bc$；⑤ 乘负数变向：$a>b,\\ c<0\\Rightarrow ac<bc$。"))+
 der(p("<strong>乘负数变向推导：</strong>若 $a>b$，则 $a-b>0$。两边乘 $c<0$，正数乘负数得负数：$c(a-b)<0$，即 $ac-bc<0$，故 $ac<bc$。"))+
 thm("一元二次不等式",p("对 $ax^2+bx+c>0$（$a>0$），设 $\\Delta=b^2-4ac$：")+
 p("$\\Delta>0$ 时，不等式解集为 $x<x_1$ 或 $x>x_2$（两根之外）；$\\Delta=0$ 时，解集为 $x\\neq -\\dfrac{b}{2a}$；$\\Delta<0$ 时，解集为全体实数 $\\mathbb{R}$。"))+
 der(p("<strong>图像法原理：</strong>$a>0$ 时抛物线开口向上。不等式 $>0$ 对应图像在 x 轴上方的部分。当 $\\Delta>0$ 时抛物线与 x 轴交于 $x_1,x_2$，上方部分在两根之外；$\\Delta=0$ 时抛物线仅顶点触 x 轴，除顶点外均在 x 轴上方；$\\Delta<0$ 时整条抛物线悬于 x 轴上方。"))+
 exa(p("<strong>例：</strong>解 $x^2-3x+2<0$。因式分解 $(x-1)(x-2)<0$，解集为 $1<x<2$（两根之间）。")))
},
{"id":"e2s4-2","name":"分式、绝对值不等式与均值不等式链","tags":["thm","der","app"],"brief":"分式不等式、绝对值不等式与均值不等式链完整推导。",
"body":wrap(
 thm("分式不等式",p("$\\dfrac{f(x)}{g(x)}>0 \\Leftrightarrow f(x)g(x)>0$；$\\dfrac{f(x)}{g(x)}\\le 0 \\Leftrightarrow f(x)g(x)\\le 0$ 且 $g(x)\\neq 0$。"))+
 der(p("<strong>推导：</strong>分式 $\\dfrac{f(x)}{g(x)}$ 的符号由分子分母共同决定。$\\dfrac{A}{B}>0$ 等价于 $A,B$ 同号，即 $AB>0$；注意分母不能为零。"))+
 thm("绝对值不等式",p("$|x|<a\\ (a>0)\\Leftrightarrow -a<x<a$；$|x|>a\\ (a>0)\\Leftrightarrow x<-a$ 或 $x>a$。")+
 fml("|a|+|b|\\ge|a+b|\\quad(\\text{当且仅当 }ab\\ge 0\\text{ 取等})"))+
 der(p("<strong>三角不等式推导：</strong>由 $-|a|\\le a\\le |a|$，$-|b|\\le b\\le |b|$，两式相加得 $-(|a|+|b|)\\le a+b\\le |a|+|b|$，即 $|a+b|\\le |a|+|b|$。等号当 $a,b$ 同号时成立（$a+b$ 不互相抵消）。"))+
 thm("基本不等式",p("对任意正实数 $a,b$，有：")+
 fml("\\dfrac{a+b}{2} \\ge \\sqrt{ab}"))+
 der(p("<strong>推导：</strong>由 $(\\sqrt{a}-\\sqrt{b})^2\\ge 0$ 展开，$a-2\\sqrt{ab}+b\\ge 0$，即 $a+b\\ge 2\\sqrt{ab}$，两边除以 2 得证。等号当且仅当 $\\sqrt{a}=\\sqrt{b}$ 即 $a=b$ 时成立。"))+
 thm("均值不等式链",p("对正实数 $a,b$，有：")+
 fml("\\dfrac{2}{\\frac{1}{a}+\\frac{1}{b}}\\le\\sqrt{ab}\\le\\dfrac{a+b}{2}\\le\\sqrt{\\dfrac{a^2+b^2}{2}}"))+
 der(p("<strong>均值不等式链推导：</strong>① 调和 $\\le$ 几何：$\\dfrac{2}{\\frac{1}{a}+\\frac{1}{b}}\\le\\sqrt{ab}$ 等价于 $\\dfrac{2ab}{a+b}\\le\\sqrt{ab}$，即 $2\\sqrt{ab}\\le a+b$，就是基本不等式。")+
 p("② 几何 $\\le$ 算术：即基本不等式 $\\sqrt{ab}\\le\\dfrac{a+b}{2}$。")+
 p("③ 算术 $\\le$ 平方：$\\dfrac{a+b}{2}\\le\\sqrt{\\dfrac{a^2+b^2}{2}}$ 两边平方得 $\\dfrac{(a+b)^2}{4}\\le\\dfrac{a^2+b^2}{2}$，即 $(a+b)^2\\le 2(a^2+b^2)$，展开 $a^2+2ab+b^2\\le 2a^2+2b^2$，即 $0\\le(a-b)^2$，显然成立。等号当且仅当 $a=b$。"))+
 app(p("<strong>应用——求最值口诀：</strong>「一正二定三相等」。若 $ab$ 为定值，则 $a+b\\ge 2\\sqrt{ab}$，当 $a=b$ 时取最小值；若 $a+b$ 为定值，则 $ab\\le\\dfrac{(a+b)^2}{4}$，当 $a=b$ 时取最大值。")))
},
{"id":"e2s4-3","name":"常见放缩方法","tags":["thm","der","app"],"brief":"倒数、平方、阶乘、指数、对数、正弦、根差等常见放缩。",
"body":wrap(
 thm("倒数放缩",p("")+
 fml("\\dfrac{1}{n}>\\dfrac{1}{n+1}\\ (n>0)"))+
 der(p("<strong>推导：</strong>$n+1>n>0$，两边取倒数（正数取倒数不等号变向）得 $\\dfrac{1}{n+1}<\\dfrac{1}{n}$。"))+
 thm("平方裂项放缩",p("")+
 fml("\\dfrac{1}{n^2}<\\dfrac{1}{n(n-1)}=\\dfrac{1}{n-1}-\\dfrac{1}{n}\\ (n\\ge2)"))+
 der(p("<strong>推导：</strong>$n^2>n(n-1)>0$（因为 $n>n-1>0$），取倒数得 $\\dfrac{1}{n^2}<\\dfrac{1}{n(n-1)}$。又 $\\dfrac{1}{n(n-1)}=\\dfrac{1}{n-1}-\\dfrac{1}{n}$（裂项），故 $\\sum_{k=2}^n\\dfrac{1}{k^2}<\\sum_{k=2}^n\\left(\\dfrac{1}{k-1}-\\dfrac{1}{k}\\right)=1-\\dfrac{1}{n}$。"))+
 thm("阶乘与指数放缩",p("")+
 fml("n!<n^n\\ (n\\ge2),\\quad 2^n>n^2\\ (n\\ge5)"))+
 der(p("<strong>$n!<n^n$ 推导：</strong>$n!=1\\cdot2\\cdots n$，每一项 $k\\le n$，且至少 $1<n$，故 $n!<n\\cdot n\\cdots n=n^n$。")+
 p("<strong>$2^n>n^2$ 推导（n≥5）：</strong>归纳法。$n=5$ 时 $2^5=32>25=5^2$。设 $2^k>k^2$，则 $2^{k+1}=2\\cdot 2^k>2k^2$。需证 $2k^2\\ge(k+1)^2$，即 $k^2-2k-1\\ge0$，对 $k\\ge3$ 成立（更对 $k\\ge5$ 显然成立）。故由归纳 $2^n>n^2$ 对 $n\\ge5$ 成立。"))+
 thm("对数与指数函数放缩",p("")+
 fml("\\ln(1+x)<x\\ (x>0),\\quad e^x\\ge 1+x"))+
 der(p("<strong>$\\ln(1+x)<x$ 推导：</strong>令 $f(x)=x-\\ln(1+x)$，$f'(x)=1-\\dfrac{1}{1+x}=\\dfrac{x}{1+x}>0$（$x>0$），故 $f$ 在 $x>0$ 单调递增，$f(x)>f(0)=0$，即 $\\ln(1+x)<x$。")+
 p("<strong>$e^x\\ge 1+x$ 推导：</strong>令 $g(x)=e^x-1-x$，$g'(x)=e^x-1$。$x<0$ 时 $g'<0$ 递减，$x>0$ 时 $g'>0$ 递增，故 $g$ 在 $x=0$ 取最小值 $g(0)=0$，即 $e^x\\ge1+x$，等号当 $x=0$ 时成立。"))+
 thm("正弦与根差放缩",p("")+
 fml("\\sin x<x\\ (x>0),\\quad \\sqrt{n+1}-\\sqrt{n}<\\dfrac{1}{2\\sqrt{n}}"))+
 der(p("<strong>$\\sin x<x$ 推导：</strong>单位圆中，角 $x$（弧度）对应的弧长为 $x$，而正弦值为对应纵坐标。由「直线段不超过弧长」（弦长不超过弧长）得 $\\sin x<x$（$x>0$）。形式化：$f(x)=x-\\sin x$，$f'(x)=1-\\cos x\\ge0$，故 $f$ 递增，$f(x)>f(0)=0$。")+
 p("<strong>根差放缩推导：</strong>$\\sqrt{n+1}-\\sqrt{n}=\\dfrac{1}{\\sqrt{n+1}+\\sqrt{n}}$（分子有理化）。由 $\\sqrt{n+1}+\\sqrt{n}>\\sqrt{n}+\\sqrt{n}=2\\sqrt{n}$，故 $\\dfrac{1}{\\sqrt{n+1}+\\sqrt{n}}<\\dfrac{1}{2\\sqrt{n}}$。"))+
 app(p("<strong>应用：</strong>证明 $\\sum_{k=1}^n\\dfrac{1}{k^2}<2$。由 $\\dfrac{1}{k^2}<\\dfrac{1}{k(k-1)}=\\dfrac{1}{k-1}-\\dfrac{1}{k}$（$k\\ge2$），求和得 $\\sum_{k=2}^n\\dfrac{1}{k^2}<1-\\dfrac{1}{n}<1$，故 $\\sum_{k=1}^n\\dfrac{1}{k^2}=1+\\sum_{k=2}^n\\dfrac{1}{k^2}<2$。")))
]}
],

# ============ 第三章 函数 ============
ch3_sections = [
{"name":"3.1 函数概念与三要素","color":"#0d9488","desc":"函数定义、三要素与抽象函数图像变换",
"items":[
{"id":"e3s1-1","name":"函数的概念与三要素","tags":["def","exa","der"],"brief":"函数是定义域到值域的映射，三要素缺一不可。",
"fig":"func_mapping","figCap":"函数 f: A→B 将定义域中每个 x 唯一对应到值域中的 y",
"body":wrap(
 defn("函数",p("设 A、B 是非空数集，若按某种确定的对应关系 $f$，使 A 中任意一个数 $x$，在 B 中都有唯一确定的数 $y$ 与之对应，则称 $f:A\\to B$ 为从 A 到 B 的一个<strong>函数</strong>，记作 $y=f(x)$。A 称为<strong>定义域</strong>，函数值集合 $\\{f(x)\\mid x\\in A\\}$ 称为<strong>值域</strong>。"))+
 p("函数的<strong>三要素</strong>：定义域、对应关系、值域。定义域与对应关系相同的两个函数是同一函数。")+
 der(p("<strong>值域由定义域和对应关系决定：</strong>给定定义域 D 和对应关系 f，值域 $f(D)=\\{f(x)\\mid x\\in D\\}$ 随之确定。因此判断两函数是否相同，只需比较定义域与对应关系是否一致，值域不必单独验证。"))+
 exa(p("<strong>例：</strong>$f(x)=\\dfrac{1}{x}$ 的定义域为 $\\{x\\mid x\\neq 0\\}$，值域为 $\\{y\\mid y\\neq 0\\}$。$f(x)=x^2$ 与 $g(x)=\\sqrt{x^2}$ 不是同一函数（对应关系不同：$g(x)=|x|$）。")))
},
{"id":"e3s1-2","name":"抽象函数的图像变换","tags":["def","thm","der"],"brief":"平移、伸缩、对称、翻折的图像变换规律。",
"body":wrap(
 thm("平移变换",p("① $y=f(x+a)$：$y=f(x)$ 向左（$a>0$）或向右（$a<0$）平移 $|a|$ 个单位；<br>② $y=f(x)+b$：向上（$b>0$）或向下（$b<0$）平移 $|b|$ 个单位。"))+
 thm("伸缩变换",p("① $y=f(kx)$（$k>0$）：横向伸缩为原来的 $\\dfrac{1}{k}$ 倍（$k>1$ 压缩，$0<k<1$ 拉伸）；<br>② $y=kf(x)$（$k>0$）：纵向伸缩为原来的 $k$ 倍。"))+
 thm("对称与翻折变换",p("① $y=f(-x)$：关于 y 轴对称；② $y=-f(x)$：关于 x 轴对称；③ $y=|f(x)|$：x 轴下方翻折到上方；④ $y=f(|x|)$：保留 y 轴右侧，左侧与右侧关于 y 轴对称。"))+
 der(p("<strong>平移推导：</strong>设 $y=f(x)$ 上一点 $(x_0,y_0)$ 满足 $y_0=f(x_0)$。在 $y=f(x+a)$ 中，令 $x=x_0-a$，则 $y=f((x_0-a)+a)=f(x_0)=y_0$，故点 $(x_0-a,y_0)$ 在新图像上，即原图像向左平移 $a$ 个单位（$a>0$ 时）。")+
 p("<strong>翻折推导 $y=|f(x)|$：</strong>当 $f(x)\\ge 0$ 时 $|f(x)|=f(x)$，图像不变；当 $f(x)<0$ 时 $|f(x)|=-f(x)$，即 x 轴下方的点 $(x,f(x))$ 变为 $(x,-f(x))$，关于 x 轴对称到上方。")+
 p("<strong>截断推导 $y=f(|x|)$：</strong>当 $x\\ge0$ 时 $f(|x|)=f(x)$，图像保留 y 轴右侧；当 $x<0$ 时 $f(|x|)=f(-x)=f(|x|)$，由 $f(|-x|)=f(|x|)$ 知图像关于 y 轴对称，故左侧与右侧关于 y 轴对称。")))
]}
]},
{"name":"3.2 函数的性质","color":"#14b8a6","desc":"单调性、奇偶性、有界性与周期性",
"items":[
{"id":"e3s2-1","name":"单调性与复合函数单调性","tags":["def","thm","der"],"brief":"单调递增/递减的定义与复合函数「同增异减」。",
"body":wrap(
 defn("单调性",p("若对定义域内任意 $x_1<x_2$，都有 $f(x_1)<f(x_2)$，则 $f(x)$ 在该区间<strong>单调递增</strong>；若 $f(x_1)>f(x_2)$，则<strong>单调递减</strong>。"))+
 thm("复合函数单调性",p("设 $y=f(g(x))$，内层 $u=g(x)$，外层 $y=f(u)$。若内外层单调性相同，则复合函数递增；若相反，则递减。口诀「<strong>同增异减</strong>」。"))+
 der(p("<strong>推导：</strong>设 $x_1<x_2$，$g$ 递增则 $g(x_1)<g(x_2)$，即 $u_1<u_2$。若 $f$ 也递增，则 $f(u_1)<f(u_2)$，即 $f(g(x_1))<f(g(x_2))$，复合递增；若 $f$ 递减，则 $f(u_1)>f(u_2)$，复合递减。$g$ 递减时同理可得相同结论。"))+
 app(p("<strong>判定方法：</strong>① 定义法：作差 $f(x_1)-f(x_2)$ 判符号；② 导数法（若可导）：$f'(x)>0$ 递增，$f'(x)<0$ 递减。")))
},
{"id":"e3s2-2","name":"奇偶性与运算性质","tags":["def","thm","der"],"brief":"奇函数/偶函数的判定与运算性质。",
"body":wrap(
 defn("奇偶性",p("若定义域关于原点对称，且对任意 $x$ 有 $f(-x)=-f(x)$，则 $f(x)$ 为<strong>奇函数</strong>（图像关于原点对称）；若 $f(-x)=f(x)$，则为<strong>偶函数</strong>（图像关于 y 轴对称）。"))+
 thm("运算性质",p("① 奇±奇=奇，偶±偶=偶；② 奇×奇=偶，偶×偶=偶，奇×偶=奇；③ 两个奇函数的复合为奇函数，其他组合按「内层×外层」符号规则。"))+
 der(p("<strong>奇×偶=奇 的推导：</strong>设 $f$ 奇、$g$ 偶，则 $(fg)(-x)=f(-x)g(-x)=(-f(x))\\cdot g(x)=-f(x)g(x)=-(fg)(x)$，故 $fg$ 为奇函数。")+
 p("<strong>奇+奇=奇 的推导：</strong>$(f+g)(-x)=f(-x)+g(-x)=-f(x)-g(x)=-(f(x)+g(x))=-(f+g)(x)$。"))+
 note(p("判断奇偶性前必须先确认<strong>定义域关于原点对称</strong>。奇函数在 $x=0$ 处有定义时必有 $f(0)=0$；偶函数满足 $f(|x|)=f(x)$。")))
},
{"id":"e3s2-3","name":"有界性与周期性","tags":["def","thm","der"],"brief":"有界函数与周期函数的定义与性质。",
"body":wrap(
 defn("有界性",p("若存在常数 $M$，使对定义域内所有 $x$ 有 $|f(x)|\\le M$，则 $f(x)$ 为<strong>有界函数</strong>。$f(x)\\le M$ 称上有界，$f(x)\\ge m$ 称下有界。"))+
 defn("周期性",p("若存在非零常数 $T$，使对定义域内任意 $x$ 有 $f(x+T)=f(x)$，则 $f(x)$ 为<strong>周期函数</strong>，$T$ 为一个周期。所有正周期中最小的称为<strong>最小正周期</strong>。"))+
 der(p("<strong>周期倍数推导：</strong>若 $T$ 是 $f(x)$ 的周期，则 $f(x+2T)=f((x+T)+T)=f(x+T)=f(x)$，故 $2T$ 也是周期。同理 $nT$（$n\\in\\mathbb{Z},\\ n\\neq 0$）都是周期。")+
 p("<strong>$f(kx)$ 的周期推导：</strong>若 $f(x)$ 周期为 $T$，则 $f(k(x+\\dfrac{T}{|k|}))=f(kx+T)=f(kx)$，故 $f(kx)$ 的周期为 $\\dfrac{T}{|k|}$。例如 $\\sin 2x$ 的周期为 $\\dfrac{2\\pi}{2}=\\pi$。"))+
 note(p("常见周期：$\\sin x,\\cos x$ 周期 $2\\pi$；$\\tan x,\\cot x$ 周期 $\\pi$。常函数是周期函数但无最小正周期。")))
}
]},
{"name":"3.3 基本初等函数","color":"#0d9488","desc":"指数函数、对数函数、幂函数",
"items":[
{"id":"e3s3-1","name":"指数函数","tags":["def","thm","der"],"brief":"$y=a^x$ 的定义、性质与图像。",
"body":wrap(
 defn("指数函数",p("形如 $y=a^x$（$a>0$ 且 $a\\neq 1$）的函数称为<strong>指数函数</strong>，定义域 $\\mathbb{R}$，值域 $(0,+\\infty)$。"))+
 thm("指数运算法则",p("")+
 fml("a^m\\cdot a^n = a^{m+n},\\quad (a^m)^n = a^{mn},\\quad (ab)^n = a^n b^n"))+
 thm("指数函数性质",p("当 $a>1$ 时单调递增，$0<a<1$ 时单调递减；恒过点 $(0,1)$；$x\\to+\\infty$ 时若 $a>1$ 则 $y\\to+\\infty$，若 $0<a<1$ 则 $y\\to0$。"))+
 der(p("<strong>$a^0=1$ 推导：</strong>由 $a^m\\cdot a^n=a^{m+n}$，令 $m=0$ 得 $a^0\\cdot a^n=a^n$，因 $a^n\\neq0$ 故 $a^0=1$。")+
 p("<strong>$a^{-n}=\\dfrac{1}{a^n}$ 推导：</strong>令 $m=-n$，$a^{-n}\\cdot a^n=a^0=1$，故 $a^{-n}=\\dfrac{1}{a^n}$。")+
 p("<strong>单调性推导（$a>1$）：</strong>对 $x_1<x_2$，$\\dfrac{a^{x_2}}{a^{x_1}}=a^{x_2-x_1}>1$（因为 $a>1$ 且 $x_2-x_1>0$），故 $a^{x_2}>a^{x_1}$，递增。"))
)},
{"id":"e3s3-2","name":"对数函数","tags":["def","thm","der"],"brief":"$\\log_a x$ 的定义、性质、换底公式推导。",
"body":wrap(
 defn("对数函数",p("$y=\\log_a x$（$a>0$ 且 $a\\neq 1$）是 $y=a^x$ 的反函数，定义域 $(0,+\\infty)$，值域 $\\mathbb{R}$。当 $a>1$ 时单调递增，恒过点 $(1,0)$。"))+
 thm("对数运算法则",p("（$a>0,a\\neq1$，$M,N>0$）")+
 fml("\\log_a(MN)=\\log_aM+\\log_aN,\\quad \\log_a\\dfrac{M}{N}=\\log_aM-\\log_aN")+
 fml("\\log_a M^n = n\\log_a M,\\quad \\log_a b = \\dfrac{\\log_c b}{\\log_c a}\\ (\\text{换底公式})"))+
 der(p("<strong>换底公式推导：</strong>设 $\\log_a b=x$，则 $a^x=b$。两边取以 $c$ 为底的对数：$\\log_c(a^x)=\\log_c b$，由对数幂法则 $x\\log_c a=\\log_c b$，故 $x=\\dfrac{\\log_c b}{\\log_c a}$。")+
 p("<strong>乘积法则推导：</strong>设 $\\log_a M=p$，$\\log_a N=q$，则 $M=a^p$，$N=a^q$。$MN=a^p\\cdot a^q=a^{p+q}$，故 $\\log_a(MN)=p+q=\\log_a M+\\log_a N$。")+
 p("<strong>幂法则推导：</strong>$M=a^p$，则 $M^n=(a^p)^n=a^{pn}$，故 $\\log_a M^n=pn=n\\log_a M$。")))
},
{"id":"e3s3-3","name":"幂函数","tags":["def","exa","der"],"brief":"$y=x^\\alpha$ 的图像与性质。",
"body":wrap(
 defn("幂函数",p("形如 $y=x^\\alpha$（$\\alpha$ 为常数）的函数称为<strong>幂函数</strong>。图像恒过点 $(1,1)$。"))+
 p("常见幂函数：① $\\alpha=1$：$y=x$，直线；② $\\alpha=2$：$y=x^2$，抛物线，偶函数；③ $\\alpha=3$：$y=x^3$，奇函数，单调递增；④ $\\alpha=-1$：$y=1/x$，双曲线，奇函数；⑤ $\\alpha=1/2$：$y=\\sqrt{x}$，定义域 $[0,+\\infty)$。")+
 der(p("<strong>过定点推导：</strong>对任意 $\\alpha$，$1^\\alpha=1$，故幂函数图像恒过 $(1,1)$。当 $\\alpha>0$ 时，$0^\\alpha=0$，故也过原点；当 $\\alpha<0$ 时，$x=0$ 处无定义，不过原点。")+
 p("<strong>第一象限单调性推导：</strong>对 $y=x^\\alpha$ 求导（$x>0$），$y'=\\alpha x^{\\alpha-1}$。当 $\\alpha>0$ 时 $y'>0$，递增；当 $\\alpha<0$ 时 $y'<0$，递减。"))+
 note(p("幂函数在第一象限：$\\alpha>1$ 时下凸（递增加快），$0<\\alpha<1$ 时上凸（递增减慢）；$\\alpha<0$ 时递减。")))
}
]},
{"name":"3.4 三角函数","color":"#0d9488","desc":"六函数定义、同角关系、诱导、和差角、倍角、半角",
"items":[
{"id":"e3s4-1","name":"三角函数定义与同角关系","tags":["def","thm","der"],"brief":"sin/cos/tan/cot/sec/csc 定义与同角八式。",
"fig":"trig_circle","figCap":"单位圆上点 P(cosθ,sinθ)，展示三角函数定义",
"body":wrap(
 defn("六种三角函数定义",p("设角 $\\alpha$ 终边上一点 $P(x,y)$，$r=\\sqrt{x^2+y^2}$，则：")+
 fml("\\sin\\alpha=\\dfrac{y}{r},\\ \\cos\\alpha=\\dfrac{x}{r},\\ \\tan\\alpha=\\dfrac{y}{x},\\ \\cot\\alpha=\\dfrac{x}{y},\\ \\sec\\alpha=\\dfrac{r}{x},\\ \\csc\\alpha=\\dfrac{r}{y}"))+
 p("<strong>单位圆定义：</strong>在单位圆上 $r=1$，点 $P(\\cos\\alpha,\\sin\\alpha)$，故 $\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}$，$\\cot\\alpha,\\sec\\alpha,\\csc\\alpha$ 为相应倒数。")+
 thm("同角三角函数关系（八式）",p("")+
 fml("\\sin^2\\alpha+\\cos^2\\alpha=1,\\quad 1+\\tan^2\\alpha=\\sec^2\\alpha,\\quad 1+\\cot^2\\alpha=\\csc^2\\alpha")+
 fml("\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha},\\quad \\cot\\alpha=\\dfrac{\\cos\\alpha}{\\sin\\alpha},\\quad \\tan\\alpha\\cdot\\cot\\alpha=1")+
 fml("\\sin\\alpha\\cdot\\csc\\alpha=1,\\quad \\cos\\alpha\\cdot\\sec\\alpha=1"))+
 der(p("<strong>推导 $\\sin^2\\alpha+\\cos^2\\alpha=1$：</strong>在单位圆定义中，$x=\\cos\\alpha$，$y=\\sin\\alpha$，$r=1$，由 $x^2+y^2=r^2$ 直接得 $\\sin^2\\alpha+\\cos^2\\alpha=1$。")+
 p("<strong>推导 $1+\\tan^2\\alpha=\\sec^2\\alpha$：</strong>$1+\\tan^2\\alpha=1+\\dfrac{\\sin^2\\alpha}{\\cos^2\\alpha}=\\dfrac{\\cos^2\\alpha+\\sin^2\\alpha}{\\cos^2\\alpha}=\\dfrac{1}{\\cos^2\\alpha}=\\sec^2\\alpha$。")+
 p("<strong>推导 $1+\\cot^2\\alpha=\\csc^2\\alpha$：</strong>同理，$1+\\cot^2\\alpha=1+\\dfrac{\\cos^2\\alpha}{\\sin^2\\alpha}=\\dfrac{\\sin^2\\alpha+\\cos^2\\alpha}{\\sin^2\\alpha}=\\dfrac{1}{\\sin^2\\alpha}=\\csc^2\\alpha$。")+
 p("<strong>推导链：</strong>平方关系 $\\sin^2+\\cos^2=1$ 两边除以 $\\cos^2$ 得 $\\tan^2+1=\\sec^2$；除以 $\\sin^2$ 得 $\\cot^2+1=\\csc^2$。商关系 $\\tan=\\sin/\\cos$ 由定义直接得到。倒数关系 $\\tan\\cdot\\cot=1$，$\\sin\\cdot\\csc=1$，$\\cos\\cdot\\sec=1$ 由各函数定义的倒数关系得到。")))
},
{"id":"e3s4-2","name":"诱导公式与和差角公式","tags":["thm","der","exa"],"brief":"诱导公式与和差角公式推导。",
"body":wrap(
 thm("诱导公式",p("口诀「<strong>奇变偶不变，符号看象限</strong>」。即 $\\dfrac{k\\pi}{2}\\pm\\alpha$ 形式中，$k$ 为奇数变名（$\\sin\\leftrightarrow\\cos$，$\\tan\\leftrightarrow\\cot$），$k$ 为偶数不变名；符号视原角所在象限的函数符号而定。例如：")+
 fml("\\sin(\\pi-\\alpha)=\\sin\\alpha,\\ \\cos(\\pi+\\alpha)=-\\cos\\alpha,\\ \\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha,\\ \\tan(\\pi+\\alpha)=\\tan\\alpha"))+
 der(p("<strong>$\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha$ 推导：</strong>在单位圆上，$\\alpha$ 与 $\\dfrac{\\pi}{2}-\\alpha$ 互余。设 $P(\\cos\\alpha,\\sin\\alpha)$ 是 $\\alpha$ 终边与单位圆的交点。将坐标系顺时针旋转 $\\alpha$ 后，新横轴沿 $\\alpha$ 终边方向。点 $P$ 在新坐标系中横坐标 $=\\sin\\alpha=\\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)$，纵坐标 $=\\cos\\alpha=\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)$。故 $\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha$。")+
 p("<strong>$\\sin(\\pi-\\alpha)=\\sin\\alpha$ 推导：</strong>$\\pi-\\alpha$ 的终边与 $\\alpha$ 的终边关于 y 轴对称。设 $P(\\cos\\alpha,\\sin\\alpha)$，关于 y 轴对称点 $P'(-\\cos\\alpha,\\sin\\alpha)$，正是角 $\\pi-\\alpha$ 终边上的点，故 $\\sin(\\pi-\\alpha)=\\sin\\alpha$，$\\cos(\\pi-\\alpha)=-\\cos\\alpha$。"))+
 thm("和差角公式",p("")+
 fml("\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta")+
 fml("\\cos(\\alpha\\pm\\beta)=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta")+
 fml("\\tan(\\alpha\\pm\\beta)=\\dfrac{\\tan\\alpha\\pm\\tan\\beta}{1\\mp\\tan\\alpha\\tan\\beta}"))+
 der(p("<strong>余弦差角公式推导（单位圆法）：</strong>在单位圆上取点 $A(\\cos\\alpha,\\sin\\alpha)$ 和 $B(\\cos\\beta,\\sin\\beta)$，则 $|AB|^2=(\\cos\\alpha-\\cos\\beta)^2+(\\sin\\alpha-\\sin\\beta)^2=2-2(\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta)$。")+
 p("另一方面，$\\angle AOB=\\alpha-\\beta$，由余弦定理 $|AB|^2=1+1-2\\cos(\\alpha-\\beta)$。比较两式得 $\\cos(\\alpha-\\beta)=\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta$。")+
 p("把 $\\beta$ 换为 $-\\beta$ 得 $\\cos(\\alpha+\\beta)=\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta$。再用互补关系 $\\sin=\\cos(\\pi/2-\\cdot)$ 推出正弦和差角公式。")+
 p("正切和差角：$\\tan(\\alpha+\\beta)=\\dfrac{\\sin(\\alpha+\\beta)}{\\cos(\\alpha+\\beta)}=\\dfrac{\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta}{\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta}$，分子分母同除 $\\cos\\alpha\\cos\\beta$ 得 $\\dfrac{\\tan\\alpha+\\tan\\beta}{1-\\tan\\alpha\\tan\\beta}$。")))
},
{"id":"e3s4-3","name":"倍角与半角公式","tags":["thm","der"],"brief":"二倍角、半角公式及推导。",
"body":wrap(
 thm("二倍角公式",p("")+
 fml("\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha")+
 fml("\\cos 2\\alpha=\\cos^2\\alpha-\\sin^2\\alpha=2\\cos^2\\alpha-1=1-2\\sin^2\\alpha")+
 fml("\\tan 2\\alpha=\\dfrac{2\\tan\\alpha}{1-\\tan^2\\alpha}"))+
 der(p("<strong>倍角公式推导：</strong>在和角公式中令 $\\beta=\\alpha$，即得 $\\sin 2\\alpha=\\sin(\\alpha+\\alpha)=\\sin\\alpha\\cos\\alpha+\\cos\\alpha\\sin\\alpha=2\\sin\\alpha\\cos\\alpha$。")+
 p("余弦：$\\cos 2\\alpha=\\cos(\\alpha+\\alpha)=\\cos^2\\alpha-\\sin^2\\alpha$。再利用 $\\sin^2\\alpha+\\cos^2\\alpha=1$，得 $\\cos 2\\alpha=2\\cos^2\\alpha-1=1-2\\sin^2\\alpha$（分别消去 $\\sin^2$ 或 $\\cos^2$）。")+
 p("正切：$\\tan 2\\alpha=\\dfrac{2\\tan\\alpha}{1-\\tan^2\\alpha}$，由正切和角公式令 $\\beta=\\alpha$ 直接得到。"))+
 thm("半角公式",p("")+
 fml("\\sin\\dfrac{\\alpha}{2}=\\pm\\sqrt{\\dfrac{1-\\cos\\alpha}{2}},\\quad \\cos\\dfrac{\\alpha}{2}=\\pm\\sqrt{\\dfrac{1+\\cos\\alpha}{2}}")+
 fml("\\tan\\dfrac{\\alpha}{2}=\\dfrac{1-\\cos\\alpha}{\\sin\\alpha}=\\dfrac{\\sin\\alpha}{1+\\cos\\alpha}"))+
 der(p("<strong>半角公式推导：</strong>由倍角公式 $\\cos\\alpha=1-2\\sin^2\\dfrac{\\alpha}{2}=2\\cos^2\\dfrac{\\alpha}{2}-1$，移项得 $\\sin^2\\dfrac{\\alpha}{2}=\\dfrac{1-\\cos\\alpha}{2}$，$\\cos^2\\dfrac{\\alpha}{2}=\\dfrac{1+\\cos\\alpha}{2}$，开方并加符号（视 $\\dfrac{\\alpha}{2}$ 所在象限）得半角公式。")+
 p("<strong>正切半角有理式推导：</strong>$\\tan\\dfrac{\\alpha}{2}=\\dfrac{\\sin\\dfrac{\\alpha}{2}}{\\cos\\dfrac{\\alpha}{2}}$。分子分母同乘 $2\\sin\\dfrac{\\alpha}{2}$：$\\tan\\dfrac{\\alpha}{2}=\\dfrac{2\\sin^2\\dfrac{\\alpha}{2}}{2\\sin\\dfrac{\\alpha}{2}\\cos\\dfrac{\\alpha}{2}}=\\dfrac{1-\\cos\\alpha}{\\sin\\alpha}$；同乘 $2\\cos\\dfrac{\\alpha}{2}$：$=\\dfrac{\\sin\\alpha}{1+\\cos\\alpha}$。"))
)}
]},
{"name":"3.5 反三角函数","color":"#14b8a6","desc":"arcsin/arccos/arctan 定义、性质与关系",
"items":[
{"id":"e3s5-1","name":"反三角函数","tags":["def","thm","der"],"brief":"arcsin/arccos/arctan 的定义域、值域与基本关系。",
"body":wrap(
 defn("反正弦函数",p("$y=\\arcsin x$ 是 $y=\\sin x$（$x\\in[-\\pi/2,\\pi/2]$）的反函数。定义域 $[-1,1]$，值域 $\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$，单调递增，奇函数。"))+
 defn("反余弦函数",p("$y=\\arccos x$ 是 $y=\\cos x$（$x\\in[0,\\pi]$）的反函数。定义域 $[-1,1]$，值域 $[0,\\pi]$，单调递减，非奇非偶。"))+
 defn("反正切函数",p("$y=\\arctan x$ 是 $y=\\tan x$（$x\\in(-\\pi/2,\\pi/2)$）的反函数。定义域 $\\mathbb{R}$，值域 $\\left(-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right)$，单调递增，奇函数。"))+
 thm("基本关系",p("")+
 fml("\\arcsin x+\\arccos x=\\dfrac{\\pi}{2}\\quad(x\\in[-1,1])")+
 fml("\\sin(\\arcsin x)=x,\\quad \\tan(\\arctan x)=x")+
 fml("\\arctan x+\\arctan\\dfrac{1}{x}=\\dfrac{\\pi}{2}\\ (x>0)"))+
 der(p("<strong>推导 $\\arcsin x+\\arccos x=\\pi/2$：</strong>设 $\\alpha=\\arcsin x$，则 $\\alpha\\in\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$，$\\sin\\alpha=x$。而 $\\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\sin\\alpha=x$，且 $\\dfrac{\\pi}{2}-\\alpha\\in[0,\\pi]$，正是 $\\arccos x$ 的主值区间，故 $\\arccos x=\\dfrac{\\pi}{2}-\\alpha$，即 $\\arcsin x+\\arccos x=\\dfrac{\\pi}{2}$。")+
 p("<strong>推导 $\\arctan x+\\arctan\\dfrac{1}{x}=\\dfrac{\\pi}{2}$（$x>0$）：</strong>设 $\\alpha=\\arctan x$，则 $\\tan\\alpha=x$。设 $\\beta=\\arctan\\dfrac{1}{x}$，则 $\\tan\\beta=\\dfrac{1}{x}$。由 $\\tan\\alpha\\cdot\\tan\\beta=1$，知 $\\alpha+\\beta=\\dfrac{\\pi}{2}$（在 $x>0$ 时 $\\alpha,\\beta\\in\\left(0,\\dfrac{\\pi}{2}\\right)$，故 $\\alpha+\\beta\\in(0,\\pi)$ 内使正切无定义的角度只能是 $\\dfrac{\\pi}{2}$）。")+
 p("<strong>定义域推导（$\\arcsin x$）：</strong>$y=\\sin x$ 在 $\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$ 上的值域是 $[-1,1]$，故其反函数 $\\arcsin x$ 的定义域为 $[-1,1]$。在该区间内 $\\sin x$ 单调递增，保证反函数存在且唯一。"))+
 note(p("$\\arcsin x$ 与 $\\arccos x$ 的主值区间选择是为了使原函数在该区间单调，从而保证反函数存在且唯一。$\\arctan x$ 取 $\\left(-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right)$ 是因为 $\\tan x$ 在该区间单调递增。")))
}
]}
]

# ============ 第四章 数列 ============
ch4_sections = [
{"name":"4.1 等差数列","color":"#c2410c","desc":"通项、求和与嵌入的二级结论",
"items":[
{"id":"e4s1-1","name":"等差数列及性质","tags":["def","thm","der","app"],"brief":"通项、求和、中项、片段和、$S_n$ 二次型等。",
"fig":"sequence","figCap":"等差数列各项均匀分布，公差为 d",
"body":wrap(
 defn("等差数列",p("从第二项起，每一项与前一项的差等于同一个常数的数列，称为<strong>等差数列</strong>。该常数称为<strong>公差</strong>，记作 $d$。"))+
 thm("通项公式",p("首项为 $a_1$，公差为 $d$ 的等差数列，第 $n$ 项为：")+
 fml("a_n = a_1 + (n-1)d"))+
 der(p("<strong>归纳推导：</strong>$a_2=a_1+d$，$a_3=a_2+d=a_1+2d$，$a_4=a_1+3d$，……，归纳得 $a_n=a_1+(n-1)d$。")+
 p("<strong>通项推广：</strong>由 $a_n-a_m=(n-m)d$ 得 $a_n=a_m+(n-m)d$，可用于已知任意一项求其他项。")+
 p("<strong>推导 $a_n=a_m+(n-m)d$：</strong>$a_n=a_1+(n-1)d$，$a_m=a_1+(m-1)d$，两式相减 $a_n-a_m=(n-m)d$，移项即得。"))+
 thm("前 n 项和",p("")+
 fml("S_n = \\dfrac{n(a_1+a_n)}{2} = na_1 + \\dfrac{n(n-1)}{2}d"))+
 der(p("<strong>倒序相加法推导：</strong>设 $S_n=a_1+a_2+\\cdots+a_n$，倒序写 $S_n=a_n+a_{n-1}+\\cdots+a_1$。两式相加，对应项 $a_i+a_{n+1-i}=a_1+a_n$（共 $n$ 对，因为 $a_i+a_{n+1-i}=a_1+(i-1)d+a_1+(n-i)d=a_1+a_1+(n-1)d=a_1+a_n$），得 $2S_n=n(a_1+a_n)$，故 $S_n=\\dfrac{n(a_1+a_n)}{2}$。代入 $a_n=a_1+(n-1)d$ 得 $S_n=na_1+\\dfrac{n(n-1)}{2}d$。"))+
 thm("二级结论·等差中项",p("若 $a,A,b$ 成等差数列，则 $2A=a+b$，即 $A=\\dfrac{a+b}{2}$。"))+
 der(p("<strong>等差中项推导：</strong>由等差数列定义 $A-a=b-A$（公差相同），移项 $2A=a+b$。推广：若 $m+n=p+q$，则 $a_m+a_n=a_p+a_q$（因 $a_m+a_n=2a_1+(m+n-2)d$，只与 $m+n$ 有关）。"))+
 thm("二级结论·片段和",p("$S_n, S_{2n}-S_n, S_{3n}-S_{2n}$ 仍成等差数列，公差为 $n^2d$。"))+
 der(p("<strong>等差片段和推导：</strong>$(S_{2n}-S_n)-S_n=(a_{n+1}+\\cdots+a_{2n})-(a_1+\\cdots+a_n)$。每一项 $a_{n+k}-a_k=nd$（$k=1,\\dots,n$，由 $a_{n+k}=a_k+nd$），共 $n$ 项，故差为 $n\\cdot nd=n^2d$。同理 $(S_{3n}-S_{2n})-(S_{2n}-S_n)=n^2d$，三者成等差。"))+
 thm("二级结论·$S_n$ 二次型",p("$S_n=An^2+Bn$ 是 $n$ 的二次函数，其中 $A=\\dfrac{d}{2}$，$B=a_1-\\dfrac{d}{2}$。"))+
 der(p("<strong>$S_n$ 二次型推导：</strong>由 $S_n=na_1+\\dfrac{n(n-1)}{2}d=\\dfrac{d}{2}n^2+\\left