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
    ("完全平方公式", "(a\\pm b)^2 = a^2 \\pm 2ab + b^2", "二项式平方展开"),
    ("平方差公式", "a^2 - b^2 = (a+b)(a-b)", "因式分解基本公式"),
    ("立方和公式", "a^3+b^3 = (a+b)(a^2-ab+b^2)", "立方和分解"),
    ("立方差公式", "a^3-b^3 = (a-b)(a^2+ab+b^2)", "立方差分解"),
    ("二项式定理", "(a+b)^n = \\sum_{k=0}^n \\binom{n}{k} a^{n-k}b^k", "二项式展开"),
    ("一元二次求根", "x = \\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}", "ax²+bx+c=0 的求根公式"),
    ("判别式", "\\Delta = b^2-4ac", "判别二次方程实根个数"),
    ("韦达定理·和", "x_1+x_2=-\\dfrac{b}{a}", "两根之和"),
    ("韦达定理·积", "x_1x_2=\\dfrac{c}{a}", "两根之积"),
    ("有理根定理", "x=\\dfrac{p}{q}\\ (p|a_0,\\ q|a_n)", "整系数多项式有理根的可能值"),
    ("不等式传递性", "a>b,\\ b>c \\Rightarrow a>c", "不等关系的传递"),
    ("均值不等式·二元", "\\dfrac{a+b}{2}\\ge\\sqrt{ab}\\ (a,b>0)", "算术平均不小于几何平均"),
    ("均值不等式链", "\\dfrac{2}{\\frac{1}{a}+\\frac{1}{b}}\\le\\sqrt{ab}\\le\\dfrac{a+b}{2}\\le\\sqrt{\\dfrac{a^2+b^2}{2}}", "调和≤几何≤算术≤平方平均"),
    ("绝对值不等式", "|a|-|b|\\le|a\\pm b|\\le|a|+|b|", "三角不等式"),
    ("同角关系·平方", "\\sin^2\\alpha+\\cos^2\\alpha=1", "正弦余弦平方和为 1"),
    ("同角关系·商", "\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}", "正切等于正弦比余弦"),
    ("同角关系·倒数", "\\cot\\alpha=\\dfrac{\\cos\\alpha}{\\sin\\alpha}=\\dfrac{1}{\\tan\\alpha}", "余切的定义"),
    ("诱导公式·π-α", "\\sin(\\pi-\\alpha)=\\sin\\alpha,\\ \\cos(\\pi-\\alpha)=-\\cos\\alpha", "奇变偶不变，符号看象限"),
    ("和角正弦", "\\sin(\\alpha+\\beta)=\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta", "正弦和角公式"),
    ("和角余弦", "\\cos(\\alpha+\\beta)=\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta", "余弦和角公式"),
    ("差角正切", "\\tan(\\alpha-\\beta)=\\dfrac{\\tan\\alpha-\\tan\\beta}{1+\\tan\\alpha\\tan\\beta}", "正切差角公式"),
    ("倍角正弦", "\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha", "二倍角正弦"),
    ("倍角余弦", "\\cos 2\\alpha=\\cos^2\\alpha-\\sin^2\\alpha=2\\cos^2\\alpha-1=1-2\\sin^2\\alpha", "二倍角余弦"),
    ("半角公式", "\\sin\\dfrac{\\alpha}{2}=\\pm\\sqrt{\\dfrac{1-\\cos\\alpha}{2}}", "半角正弦"),
    ("对数换底", "\\log_a b = \\dfrac{\\log_c b}{\\log_c a}", "对数换底公式"),
    ("对数运算·积", "\\log_a(MN)=\\log_aM+\\log_aN", "积的对数等于对数之和"),
    ("对数运算·商", "\\log_a\\dfrac{M}{N}=\\log_aM-\\log_aN", "商的对数等于对数之差"),
    ("对数运算·幂", "\\log_a M^n = n\\log_a M", "幂的对数"),
    ("指数运算", "a^m\\cdot a^n=a^{m+n},\\ (a^m)^n=a^{mn}", "指数运算法则"),
    ("等差数列通项", "a_n = a_1 + (n-1)d", "公差为 d 的等差数列第 n 项"),
    ("等差数列求和", "S_n = \\dfrac{n(a_1+a_n)}{2} = na_1+\\dfrac{n(n-1)}{2}d", "前 n 项和"),
    ("等差中项", "2A=a+b \\Rightarrow A=\\dfrac{a+b}{2}", "a,b 的等差中项"),
    ("等比数列通项", "a_n = a_1 q^{n-1}", "公比为 q 的等比数列第 n 项"),
    ("等比数列求和", "S_n = \\dfrac{a_1(1-q^n)}{1-q}\\ (q\\neq 1)", "前 n 项和"),
    ("无穷等比级数", "S = \\dfrac{a_1}{1-q}\\ (|q|<1)", "公比绝对值小于 1 时的和"),
    ("等比中项", "G^2=ab \\Rightarrow G=\\pm\\sqrt{ab}", "a,b 的等比中项"),
    ("裂项·相邻", "\\dfrac{1}{n(n+1)}=\\dfrac{1}{n}-\\dfrac{1}{n+1}", "相邻整数乘积的裂项"),
    ("裂项·差为d", "\\dfrac{1}{n(n+d)}=\\dfrac{1}{d}\\left(\\dfrac{1}{n}-\\dfrac{1}{n+d}\\right)", "差为 d 的裂项"),
    ("勾股定理", "a^2+b^2 = c^2", "直角三角形两直角边平方和等于斜边平方"),
    ("正弦定理", "\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R", "三角形边与对角正弦之比"),
    ("余弦定理", "c^2 = a^2+b^2-2ab\\cos C", "已知两边夹角求第三边"),
    ("三角形面积·底高", "S = \\dfrac{1}{2}ah", "底乘高除以二"),
    ("三角形面积·夹角", "S = \\dfrac{1}{2}ab\\sin C", "两边及其夹角求面积"),
    ("海伦公式", "S = \\sqrt{p(p-a)(p-b)(p-c)},\\ p=\\dfrac{a+b+c}{2}", "已知三边求面积"),
    ("三角形面积·内切圆", "S = pr = \\dfrac{1}{2}(a+b+c)r", "内切圆半径法"),
    ("平行四边形面积", "S = ah = ab\\sin\\theta", "底乘高或两边夹角"),
    ("梯形面积", "S = \\dfrac{(a+b)h}{2}", "上底加下底乘高除以二"),
    ("圆周长", "C = 2\\pi r", "圆的周长公式"),
    ("圆面积", "S = \\pi r^2", "圆的面积公式"),
    ("扇形弧长", "l = \\alpha r = \\dfrac{n\\pi r}{180}", "弧长与圆心角关系"),
    ("扇形面积", "S = \\dfrac{1}{2}lr = \\dfrac{1}{2}\\alpha r^2", "扇形面积公式"),
    ("球表面积", "S = 4\\pi R^2", "球面面积"),
    ("球体积", "V = \\dfrac{4}{3}\\pi R^3", "球的体积"),
    ("圆柱体积", "V = \\pi r^2 h", "底面积乘高"),
    ("圆柱侧面积", "S_{\\text{侧}} = 2\\pi rh", "圆柱侧面积"),
    ("圆锥体积", "V = \\dfrac{1}{3}\\pi r^2 h", "同底等高圆柱体积的 1/3"),
    ("圆锥侧面积", "S_{\\text{侧}} = \\pi rl", "母线长为 l 的圆锥侧面积"),
    ("圆台体积", "V = \\dfrac{1}{3}\\pi h(R^2+Rr+r^2)", "上下底半径 R,r 的圆台体积"),
    ("棱锥体积", "V = \\dfrac{1}{3}Sh", "底面积为 S 高为 h 的棱锥"),
    ("两点距离", "d = \\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}", "平面内两点间距离"),
    ("点到直线距离", "d = \\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}", "点到直线 Ax+By+C=0 的距离"),
    ("直线斜率", "k = \\dfrac{y_2-y_1}{x_2-x_1} = \\tan\\alpha", "斜率与倾斜角关系"),
    ("圆方程", "(x-a)^2+(y-b)^2 = r^2", "圆心 (a,b) 半径 r 的圆"),
    ("椭圆标准方程", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2} = 1\\ (a>b>0)", "焦点在 x 轴的椭圆"),
    ("椭圆离心率", "e=\\dfrac{c}{a}\\in(0,1),\\ c^2=a^2-b^2", "椭圆扁平程度"),
    ("双曲线标准方程", "\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2} = 1", "焦点在 x 轴的双曲线"),
    ("抛物线标准方程", "y^2 = 2px\\ (p>0)", "开口向右的抛物线"),
    ("极坐标互化", "x=\\rho\\cos\\theta,\\ y=\\rho\\sin\\theta,\\ \\rho^2=x^2+y^2", "极坐标与直角坐标互化"),
    ("柱坐标关系", "x=\\rho\\cos\\theta,\\ y=\\rho\\sin\\theta,\\ z=z", "柱坐标与直角坐标关系"),
    ("球坐标关系", "x=r\\sin\\varphi\\cos\\theta,\\ y=r\\sin\\varphi\\sin\\theta,\\ z=r\\cos\\varphi", "球坐标与直角坐标关系"),
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
    ("样本均值", "\\bar{x} = \\dfrac{1}{n}\\sum_{i=1}^n x_i", "样本算术平均值"),
    ("样本方差", "s^2 = \\dfrac{1}{n}\\sum_{i=1}^n (x_i-\\bar{x})^2", "样本方差"),
    ("线性回归斜率", "b = \\dfrac{\\sum(x_i-\\bar{x})(y_i-\\bar{y})}{\\sum(x_i-\\bar{x})^2}", "回归直线斜率"),
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
{"id":"e1s1-1","name":"集合的概念与表示","tags":["def","exa"],"brief":"集合是确定对象的全体，常用列举法、描述法表示。",
"body":wrap(
 defn("集合与元素",p("具有某种特定性质的事物的总体称为<strong>集合</strong>，组成集合的事物称为<strong>元素</strong>。若 a 是集合 A 的元素，记 $a\\in A$；否则 $a\\notin A$。"))+
 note(p("集合中元素具有<strong>确定性、互异性、无序性</strong>三大特性。确定性要求能判断任一对象是否属于该集合；互异性要求元素不重复；无序性要求元素排列顺序不影响集合相等。"))+
 der(p("<strong>互异性的推论：</strong>若 $\\{1,2,a\\}=\\{1,2,3\\}$，则 $a$ 只能等于 3，因为集合中已有 1 和 2，由互异性 $a$ 不能取 1 或 2。"))+
 exa(p("<strong>常见数集：</strong>$\\mathbb{N}$ 自然数集、$\\mathbb{Z}$ 整数集、$\\mathbb{Q}$ 有理数集、$\\mathbb{R}$ 实数集、$\\mathbb{C}$ 复数集。<br>集合的表示方法：① <strong>列举法</strong> $A=\\{1,2,3\\}$；② <strong>描述法</strong> $A=\\{x\\mid x>0, x\\in\\mathbb{R}\\}$；③ <strong>图示法</strong>（韦恩图）。"))
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
 der(p("<strong>第一式推导（双向包含）：</strong>任取 $x\\in\\complement_U(A\\cap B)$，则 $x\\notin A\\cap B$，即 $x\\notin A$ 或 $x\\notin B$，故 $x\\in\\complement_U A$ 或 $x\\in\\complement_U B$，即 $x\\in\\complement_U A\\cup\\complement_U B$，故左⊆右。")+
 p("反向：任取 $x\\in\\complement_U A\\cup\\complement_U B$，则 $x\\notin A$ 或 $x\\notin B$，即 $x\\notin A\\cap B$，故 $x\\in\\complement_U(A\\cap B)$，右⊆左。两边相等得证。"))
)}
]},
{"name":"1.2 子集与容斥原理","color":"#0ea5e9","desc":"子集、真子集与容斥原理",
"items":[
{"id":"e1s2-1","name":"子集与真子集","tags":["def","thm","der"],"brief":"子集、真子集、集合相等的判定与子集个数。",
"body":wrap(
 defn("子集",p("若集合 A 的每一个元素都属于 B，则称 A 是 B 的<strong>子集</strong>，记作 $A\\subseteq B$。若 $A\\subseteq B$ 且 $B\\subseteq A$，则 $A=B$。"))+
 defn("真子集",p("若 $A\\subseteq B$ 且存在 $b\\in B$ 使 $b\\notin A$，则称 A 是 B 的<strong>真子集</strong>，记作 $A\\subsetneq B$。"))+
 thm("子集个数",p("含有 $n$ 个元素的集合共有 $2^n$ 个子集，$2^n-1$ 个真子集，$2^n-2$ 个非空真子集。"))+
 der(p("<strong>推导：</strong>对集合 A 的每个元素，在构造子集时都有「选」或「不选」两种可能。$n$ 个元素共有 $2\\times2\\times\\cdots\\times2=2^n$ 种组合，故子集总数为 $2^n$。去掉集合本身得真子集 $2^n-1$ 个，再去掉空集得非空真子集 $2^n-2$ 个。"))+
 note(p("空集 $\\varnothing$ 是任何集合的子集，是任何非空集合的真子集。判断集合相等常用「双向包含」法。"))
)},
{"id":"e1s2-2","name":"容斥原理","tags":["thm","der","exa"],"brief":"有限集合并集的元素个数公式。",
"body":wrap(
 thm("二元容斥原理",p("设 A、B 为有限集，则：")+
 fml("|A\\cup B| = |A|+|B|-|A\\cap B|"))+
 der(p("<strong>推导：</strong>$|A|+|B|$ 把 $A\\cap B$ 的元素算了两次（一次在 A 中，一次在 B 中），因此需要减去重复计算的 $|A\\cap B|$，才得到 $A\\cup B$ 的真实元素个数。"))+
 thm("三元容斥原理",p("")+
 fml("|A\\cup B\\cup C| = |A|+|B|+|C|-|A\\cap B|-|B\\cap C|-|C\\cap A|+|A\\cap B\\cap C|"))+
 der(p("<strong>推导：</strong>先 $|A|+|B|+|C|$，其中两两交集被多加了一次，故减去 $|A\\cap B|+|B\\cap C|+|C\\cap A|$。但这样 $A\\cap B\\cap C$ 被加了 3 次又减了 3 次，恰好抵消为 0，所以要再加回一次 $|A\\cap B\\cap C|$。"))+
 exa(p("<strong>例：</strong>某班 50 人，喜欢数学 30 人，喜欢物理 25 人，两科都喜欢 15 人。两科至少喜欢一科的人数 $=30+25-15=40$ 人。"))
)}
]},
{"name":"1.3 常用逻辑用语","color":"#0284c7","desc":"命题、四种命题、充要条件与量词",
"items":[
{"id":"e1s3-1","name":"命题与四种命题","tags":["def","thm","der"],"brief":"原命题、逆命题、否命题、逆否命题的关系。",
"body":wrap(
 defn("命题",p("可以判断真假的陈述句称为<strong>命题</strong>。判断为真的叫真命题，判断为假的叫假命题。"))+
 p("设原命题为「若 p，则 q」，则：① <strong>逆命题</strong>：若 q，则 p；② <strong>否命题</strong>：若 ¬p，则 ¬q；③ <strong>逆否命题</strong>：若 ¬q，则 ¬p。")+
 thm("等价性",p("原命题与其逆否命题同真同假（等价）；逆命题与否命题同真同假。但原命题与逆命题、否命题的真假无必然联系。"))+
 der(p("<strong>逆否命题等价性推导：</strong>「若 p 则 q」等价于「$p\\Rightarrow q$」，其逆否为「$\\neg q\\Rightarrow\\neg p$」。用真值表验证：当 p 真 q 真时两者都真；p 真 q 假时两者都假；p 假时两者都真。故原命题与逆否命题真值完全相同。"))
)},
{"id":"e1s3-2","name":"充要条件与量词","tags":["def","exa","der"],"brief":"充要条件的判定与全称、存在量词。",
"body":wrap(
 defn("充分条件与必要条件",p("若 $p\\Rightarrow q$（p 推出 q），则称 p 是 q 的<strong>充分条件</strong>，q 是 p 的<strong>必要条件</strong>。"))+
 defn("充要条件",p("若 $p\\Leftrightarrow q$（p 与 q 可互推），则称 p 是 q 的<strong>充要条件</strong>。"))+
 der(p("<strong>从集合角度看：</strong>设 $P=\\{x\\mid p(x)\\text{ 成立}\\}$，$Q=\\{x\\mid q(x)\\text{ 成立}\\}$。若 $p\\Rightarrow q$，则 $P\\subseteq Q$（满足 p 的必满足 q）。故 p 是 q 的充分条件 $\\Leftrightarrow$ $P\\subseteq Q$；p 是 q 的充要条件 $\\Leftrightarrow$ $P=Q$。"))+
 exa(p("<strong>例：</strong>「$x=1$」是「$x^2=1$」的充分不必要条件（$x=1\\Rightarrow x^2=1$，但 $x^2=1$ 时 $x$ 也可为 $-1$，故 $\\{1\\}\\subsetneq\\{-1,1\\}$）。"))+
 defn("全称量词与存在量词",p("<strong>全称量词</strong> $\\forall$ 表示「对任意」，<strong>存在量词</strong> $\\exists$ 表示「存在」。全称命题 $\\forall x\\in M, p(x)$ 的否定为 $\\exists x\\in M, \\neg p(x)$；存在命题的否定为全称命题。"))
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
 der(p("<strong>平方差推导：</strong>$(a+b)(a-b)=a^2-ab+ab-b^2=a^2-b^2$，交叉项 $-ab$ 与 $+ab$ 抵消。")+
 p("<strong>完全平方推导：</strong>$(a+b)^2=(a+b)(a+b)=a^2+ab+ba+b^2=a^2+2ab+b^2$。")+
 p("<strong>立方和推导：</strong>$(a+b)(a^2-ab+b^2)=a^3-a^2b+ab^2+a^2b-ab^2+b^3=a^3+b^3$。"))
)},
{"id":"e2s1-2","name":"因式分解的方法","tags":["def","exa","der"],"brief":"提公因式、公式法、十字相乘法、分组分解。",
"body":wrap(
 defn("因式分解",p("把一个多项式化为几个整式乘积的形式，称为<strong>因式分解</strong>。分解必须进行到每一个因式都不能再分解为止（在指定数域内）。"))+
 p("常用方法：① <strong>提公因式法</strong>：$ma+mb+mc=m(a+b+c)$；② <strong>公式法</strong>：套用乘法公式；③ <strong>十字相乘法</strong>：$x^2+(p+q)x+pq=(x+p)(x+q)$；④ <strong>分组分解法</strong>：适当分组后提取公因式。")+
 der(p("<strong>十字相乘法原理：</strong>$(x+p)(x+q)=x^2+qx+px+pq=x^2+(p+q)x+pq$。因此对二次三项式 $x^2+bx+c$，找到 $p,q$ 使 $p+q=b$，$pq=c$，即可分解为 $(x+p)(x+q)$。"))+
 exa(p("<strong>例：</strong>分解 $x^3-3x^2+2x$。先提公因式 $x$ 得 $x(x^2-3x+2)$，再对二次式十字相乘：找 $p+q=-3$，$pq=2$，得 $p=-1,q=-2$，故 $x^2-3x+2=(x-1)(x-2)$。原式 $=x(x-1)(x-2)$。"))
)}
]},
{"name":"2.2 方程","color":"#a855f7","desc":"一次方程、一元二次方程与高次方程",
"items":[
{"id":"e2s2-1","name":"一次方程与方程组","tags":["def","thm","der"],"brief":"一元一次方程与二元一次方程组的消元法。",
"body":wrap(
 defn("一元一次方程",p("形如 $ax+b=0$（$a\\neq 0$）的方程，解为 $x=-\\dfrac{b}{a}$。"))+
 defn("二元一次方程组",p("由两个二元一次方程组成的方程组，解法有<strong>代入消元法</strong>和<strong>加减消元法</strong>。"))+
 der(p("<strong>加减消元法推导：</strong>设方程组 $\\begin{cases}a_1x+b_1y=c_1\\\\a_2x+b_2y=c_2\\end{cases}$。将第一个方程乘 $a_2$，第二个乘 $a_1$，得 $a_1a_2x+a_2b_1y=a_2c_1$ 和 $a_1a_2x+a_1b_2y=a_1c_2$。两式相减消去 $x$：$(a_2b_1-a_1b_2)y=a_2c_1-a_1c_2$，解出 $y$ 再代回求 $x$。"))+
 app(p("<strong>代入消元法：</strong>从一个方程解出一个变量（如 $x=\\dfrac{c_1-b_1y}{a_1}$），代入另一个方程化为一元方程求解。"))+
 exa(p("<strong>例：</strong>$\\begin{cases}2x+y=5\\\\x-y=1\\end{cases}$。两式相加：$3x=6$，$x=2$，代入得 $y=1$。"))
)},
{"id":"e2s2-2","name":"一元二次方程","tags":["thm","der"],"brief":"求根公式推导、判别式、韦达定理推导。",
"fig":"quadratic","figCap":"二次函数 y=ax²+bx+c 图像，开口向上，顶点在 x 轴上方",
"body":wrap(
 thm("求根公式",p("一元二次方程 $ax^2+bx+c=0\\ (a\\neq 0)$ 的解为：")+
 fml("x = \\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}"))+
 der(p("<strong>配方法推导：</strong>两边除以 $a$：$x^2+\\dfrac{b}{a}x+\\dfrac{c}{a}=0$。移项并配方：$x^2+\\dfrac{b}{a}x+\\dfrac{b^2}{4a^2}=\\dfrac{b^2}{4a^2}-\\dfrac{c}{a}$。")+
 fml("\\left(x+\\dfrac{b}{2a}\\right)^2 = \\dfrac{b^2-4ac}{4a^2}")+
 p("当 $\\Delta=b^2-4ac\\ge 0$ 时两边开方：$x+\\dfrac{b}{2a}=\\pm\\dfrac{\\sqrt{\\Delta}}{2a}$，移项得求根公式。"))+
 thm("判别式与根的关系",p("$\\Delta=b^2-4ac$：$\\Delta>0$ 两个不相等实根；$\\Delta=0$ 两个相等实根；$\\Delta<0$ 无实根（有共轭虚根）。"))+
 thm("韦达定理",p("若方程两根为 $x_1,x_2$，则：")+
 fml("x_1+x_2=-\\dfrac{b}{a},\\quad x_1x_2=\\dfrac{c}{a}"))+
 der(p("<strong>韦达定理推导：</strong>由求根公式 $x_1=\\dfrac{-b+\\sqrt{\\Delta}}{2a}$，$x_2=\\dfrac{-b-\\sqrt{\\Delta}}{2a}$。相加：$x_1+x_2=\\dfrac{-2b}{2a}=-\\dfrac{b}{a}$。相乘：$x_1x_2=\\dfrac{(-b)^2-(\\sqrt{\\Delta})^2}{4a^2}=\\dfrac{b^2-(b^2-4ac)}{4a^2}=\\dfrac{4ac}{4a^2}=\\dfrac{c}{a}$。"))
)},
{"id":"e2s2-3","name":"高次方程与有理根定理","tags":["thm","der","exa"],"brief":"因式分解降次与有理根定理。",
"body":wrap(
 defn("高次方程",p("次数 $n\\ge 3$ 的整式方程称为高次方程，基本解法是<strong>降次</strong>：通过因式分解化为低次方程求解。"))+
 thm("因式定理",p("多项式 $f(x)$ 有因式 $(x-a)$ 当且仅当 $f(a)=0$，即 $a$ 是方程 $f(x)=0$ 的根。"))+
 der(p("<strong>因式定理推导：</strong>用带余除法，$f(x)=(x-a)q(x)+r$，其中 $r$ 为常数。代入 $x=a$：$f(a)=0\\cdot q(a)+r=r$。故 $f(a)=0$ 当且仅当 $r=0$，即 $(x-a)$ 是 $f(x)$ 的因式。"))+
 thm("有理根定理",p("若整系数多项式 $f(x)=a_nx^n+\\cdots+a_1x+a_0$ 有有理根 $\\dfrac{p}{q}$（$p,q$ 互质），则 $p$ 整除常数项 $a_0$，$q$ 整除首项系数 $a_n$。"))+
 exa(p("<strong>例：</strong>解方程 $x^3-2x^2-x+2=0$。常数项 2 的因数有 $\\pm1,\\pm2$，首项系数 1 的因数为 $\\pm1$，故可能有理根为 $\\pm1,\\pm2$。试根：$f(1)=0$，故 $(x-1)$ 是因式。多项式除法得 $f(x)=(x-1)(x^2-x-2)=(x-1)(x-2)(x+1)$，根为 $x=1,2,-1$。"))
)}
]},
{"name":"2.3 不等式与三角补充","color":"#c026d3","desc":"不等式、均值不等式链与三角函数补充",
"items":[
{"id":"e2s3-1","name":"不等式的性质与一元二次不等式","tags":["thm","der","exa"],"brief":"不等式基本性质与一元二次不等式的图像法。",
"body":wrap(
 thm("不等式基本性质",p("① 对称性：$a>b\\Leftrightarrow b<a$；② 传递性：$a>b,\\ b>c\\Rightarrow a>c$；③ 可加性：$a>b\\Rightarrow a+c>b+c$；④ 乘正数不变向：$a>b,\\ c>0\\Rightarrow ac>bc$；⑤ 乘负数变向：$a>b,\\ c<0\\Rightarrow ac<bc$。"))+
 der(p("<strong>乘负数变向推导：</strong>若 $a>b$，则 $a-b>0$。两边乘 $c<0$，正数乘负数得负数：$c(a-b)<0$，即 $ac-bc<0$，故 $ac<bc$。"))+
 thm("一元二次不等式",p("对 $ax^2+bx+c>0$（$a>0$），设 $\\Delta=b^2-4ac$：")+
 p("$\\Delta>0$ 时，不等式解集为 $x<x_1$ 或 $x>x_2$（两根之外）；$\\Delta=0$ 时，解集为 $x\\neq -\\dfrac{b}{2a}$；$\\Delta<0$ 时，解集为全体实数 $\\mathbb{R}$。"))+
 der(p("<strong>图像法原理：</strong>$a>0$ 时抛物线开口向上。不等式 $>0$ 对应图像在 x 轴上方的部分。当 $\\Delta>0$ 时抛物线与 x 轴交于 $x_1,x_2$，上方部分在两根之外。"))+
 exa(p("<strong>例：</strong>解 $x^2-3x+2<0$。因式分解 $(x-1)(x-2)<0$，解集为 $1<x<2$（两根之间）。"))
)},
{"id":"e2s3-2","name":"分式不等式与绝对值不等式","tags":["thm","der","exa"],"brief":"分式不等式转化与绝对值不等式求解。",
"body":wrap(
 thm("分式不等式",p("$\\dfrac{f(x)}{g(x)}>0 \\Leftrightarrow f(x)g(x)>0$；$\\dfrac{f(x)}{g(x)}\\le 0 \\Leftrightarrow f(x)g(x)\\le 0$ 且 $g(x)\\neq 0$。"))+
 der(p("<strong>推导：</strong>分式 $\\dfrac{f(x)}{g(x)}$ 的符号由分子分母共同决定。$\\dfrac{A}{B}>0$ 等价于 $A,B$ 同号，即 $AB>0$；注意分母不能为零。"))+
 thm("绝对值不等式",p("$|x|<a\\ (a>0)\\Leftrightarrow -a<x<a$；$|x|>a\\ (a>0)\\Leftrightarrow x<-a$ 或 $x>a$。")+
 fml("|a|-|b|\\le|a\\pm b|\\le|a|+|b|\\quad(\\text{三角不等式})"))+
 der(p("<strong>三角不等式推导：</strong>由 $-|a|\\le a\\le |a|$，$-|b|\\le b\\le |b|$，两式相加得 $-(|a|+|b|)\\le a+b\\le |a|+|b|$，即 $|a+b|\\le |a|+|b|$。将 $b$ 换为 $-b$ 得 $|a-b|\\le |a|+|b|$。"))+
 exa(p("<strong>例：</strong>解 $|2x-1|<3$。由 $-3<2x-1<3$，得 $-2<2x<4$，即 $-1<x<2$。"))
)},
{"id":"e2s3-3","name":"基本不等式与均值不等式链","tags":["thm","der","app"],"brief":"二元均值不等式与均值不等式链的完整推导。",
"body":wrap(
 thm("基本不等式",p("对任意正实数 $a,b$，有：")+
 fml("\\dfrac{a+b}{2} \\ge \\sqrt{ab}"))+
 der(p("<strong>推导：</strong>由 $(\\sqrt{a}-\\sqrt{b})^2\\ge 0$ 展开得 $a-2\\sqrt{ab}+b\\ge 0$，即 $a+b\\ge 2\\sqrt{ab}$，两边除以 2 得证。等号当且仅当 $\\sqrt{a}=\\sqrt{b}$ 即 $a=b$ 时成立。"))+
 thm("均值不等式链",p("对正实数 $a,b$，有：")+
 fml("\\dfrac{2}{\\frac{1}{a}+\\frac{1}{b}}\\le\\sqrt{ab}\\le\\dfrac{a+b}{2}\\le\\sqrt{\\dfrac{a^2+b^2}{2}}"))+
 der(p("<strong>均值不等式链推导：</strong>① 调和≤几何：$\\dfrac{2}{\\frac{1}{a}+\\frac{1}{b}}\\le\\sqrt{ab}$ 等价于 $\\dfrac{2ab}{a+b}\\le\\sqrt{ab}$，即 $2\\sqrt{ab}\\le a+b$，就是基本不等式。")+
 p("② 几何≤算术：即基本不等式 $\\sqrt{ab}\\le\\dfrac{a+b}{2}$。")+
 p("③ 算术≤平方：$\\dfrac{a+b}{2}\\le\\sqrt{\\dfrac{a^2+b^2}{2}}$ 两边平方得 $\\dfrac{(a+b)^2}{4}\\le\\dfrac{a^2+b^2}{2}$，即 $(a+b)^2\\le 2(a^2+b^2)$，展开 $a^2+2ab+b^2\\le 2a^2+2b^2$，即 $0\\le(a-b)^2$，显然成立。等号当且仅当 $a=b$。"))+
 app(p("<strong>应用——求最值口诀：</strong>「一正二定三相等」。若 $ab$ 为定值，则 $a+b\\ge 2\\sqrt{ab}$，当 $a=b$ 时取最小值；若 $a+b$ 为定值，则 $ab\\le\\dfrac{(a+b)^2}{4}$，当 $a=b$ 时取最大值。"))
)},
{"id":"e2s3-4","name":"余切、正割、余割与同角八式","tags":["def","thm","der"],"brief":"cot/sec/csc 的定义、同角三角函数关系与诱导公式。",
"fig":"trig_circle","figCap":"单位圆上点 P(cosθ,sinθ)，展示三角函数定义",
"body":wrap(
 defn("cot/sec/csc 的定义",p("设角 $\\alpha$ 终边上一点 $P(x,y)$，$r=\\sqrt{x^2+y^2}$，则：")+
 fml("\\sin\\alpha=\\dfrac{y}{r},\\ \\cos\\alpha=\\dfrac{x}{r},\\ \\tan\\alpha=\\dfrac{y}{x},\\ \\cot\\alpha=\\dfrac{x}{y},\\ \\sec\\alpha=\\dfrac{r}{x},\\ \\csc\\alpha=\\dfrac{r}{y}"))+
 thm("同角三角函数关系（八式）",p("")+
 fml("\\sin^2\\alpha+\\cos^2\\alpha=1,\\quad 1+\\tan^2\\alpha=\\sec^2\\alpha,\\quad 1+\\cot^2\\alpha=\\csc^2\\alpha")+
 fml("\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha},\\quad \\cot\\alpha=\\dfrac{\\cos\\alpha}{\\sin\\alpha},\\quad \\tan\\alpha\\cdot\\cot\\alpha=1")+
 fml("\\sin\\alpha\\cdot\\csc\\alpha=1,\\quad \\cos\\alpha\\cdot\\sec\\alpha=1"))+
 der(p("<strong>推导 $1+\\tan^2\\alpha=\\sec^2\\alpha$：</strong>$1+\\tan^2\\alpha=1+\\dfrac{\\sin^2\\alpha}{\\cos^2\\alpha}=\\dfrac{\\cos^2\\alpha+\\sin^2\\alpha}{\\cos^2\\alpha}=\\dfrac{1}{\\cos^2\\alpha}=\\sec^2\\alpha$。")+
 p("<strong>推导 $1+\\cot^2\\alpha=\\csc^2\\alpha$：</strong>同理，$1+\\cot^2\\alpha=1+\\dfrac{\\cos^2\\alpha}{\\sin^2\\alpha}=\\dfrac{\\sin^2\\alpha+\\cos^2\\alpha}{\\sin^2\\alpha}=\\dfrac{1}{\\sin^2\\alpha}=\\csc^2\\alpha$。"))+
 thm("诱导公式",p("口诀「<strong>奇变偶不变，符号看象限</strong>」。例如：")+
 fml("\\sin(\\pi-\\alpha)=\\sin\\alpha,\\ \\cos(\\pi+\\alpha)=-\\cos\\alpha,\\ \\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha,\\ \\tan(\\pi+\\alpha)=\\tan\\alpha"))
)}
]}
]

# ============ 第三章 函数 ============
ch3_sections = [
{"name":"3.1 函数的概念与变换","color":"#0d9488","desc":"函数定义、三要素与抽象函数图像变换",
"items":[
{"id":"e3s1-1","name":"函数的概念与三要素","tags":["def","exa","der"],"brief":"函数是定义域到值域的映射，三要素缺一不可。",
"fig":"func_mapping","figCap":"函数 f: A→B 将定义域中每个 x 唯一对应到值域中的 y",
"body":wrap(
 defn("函数",p("设 A、B 是非空数集，若按某种确定的对应关系 $f$，使 A 中任意一个数 $x$，在 B 中都有唯一确定的数 $y$ 与之对应，则称 $f:A\\to B$ 为从 A 到 B 的一个<strong>函数</strong>，记作 $y=f(x)$。A 称为<strong>定义域</strong>，函数值集合 $\\{f(x)\\mid x\\in A\\}$ 称为<strong>值域</strong>。"))+
 p("函数的<strong>三要素</strong>：定义域、对应关系、值域。定义域与对应关系相同的两个函数是同一函数。")+
 der(p("<strong>值域由定义域和对应关系决定：</strong>给定定义域 D 和对应关系 f，值域 $f(D)=\\{f(x)\\mid x\\in D\\}$ 随之确定。因此判断两函数是否相同，只需比较定义域与对应关系是否一致，值域不必单独验证。"))+
 exa(p("<strong>例：</strong>$f(x)=\\dfrac{1}{x}$ 的定义域为 $\\{x\\mid x\\neq 0\\}$，值域为 $\\{y\\mid y\\neq 0\\}$。$f(x)=x^2$ 与 $g(x)=\\sqrt{x^2}$ 不是同一函数（对应关系不同：$g(x)=|x|$）。"))
)},
{"id":"e3s1-2","name":"抽象函数的图像变换","tags":["def","thm","der"],"brief":"平移、伸缩、对称、翻折的图像变换规律。",
"body":wrap(
 thm("平移变换",p("① $y=f(x+a)$：$y=f(x)$ 向左（$a>0$）或向右（$a<0$）平移 $|a|$ 个单位；<br>② $y=f(x)+b$：向上（$b>0$）或向下（$b<0$）平移 $|b|$ 个单位。"))+
 thm("伸缩变换",p("① $y=f(kx)$（$k>0$）：横向伸缩为原来的 $\\dfrac{1}{k}$ 倍（$k>1$ 压缩，$0<k<1$ 拉伸）；<br>② $y=kf(x)$（$k>0$）：纵向伸缩为原来的 $k$ 倍。"))+
 thm("对称与翻折变换",p("① $y=f(-x)$：关于 y 轴对称；② $y=-f(x)$：关于 x 轴对称；③ $y=|f(x)|$：x 轴下方翻折到上方；④ $y=f(|x|)$：保留 y 轴右侧，左侧与右侧关于 y 轴对称。"))+
 der(p("<strong>平移推导：</strong>设 $y=f(x)$ 上一点 $(x_0,y_0)$ 满足 $y_0=f(x_0)$。在 $y=f(x+a)$ 中，令 $x=x_0-a$，则 $y=f((x_0-a)+a)=f(x_0)=y_0$，故点 $(x_0-a,y_0)$ 在新图像上，即原图像向左平移 $a$ 个单位（$a>0$ 时）。")+
 p("<strong>翻折推导 $y=|f(x)|$：</strong>当 $f(x)\\ge 0$ 时 $|f(x)|=f(x)$，图像不变；当 $f(x)<0$ 时 $|f(x)|=-f(x)$，即 x 轴下方的点 $(x,f(x))$ 变为 $(x,-f(x))$，关于 x 轴对称到上方。"))
)}
]},
{"name":"3.2 函数的性质","color":"#14b8a6","desc":"单调性、奇偶性、有界性与周期性",
"items":[
{"id":"e3s2-1","name":"单调性与复合函数单调性","tags":["def","thm","der"],"brief":"单调递增/递减的定义与复合函数「同增异减」。",
"body":wrap(
 defn("单调性",p("若对定义域内任意 $x_1<x_2$，都有 $f(x_1)<f(x_2)$，则 $f(x)$ 在该区间<strong>单调递增</strong>；若 $f(x_1)>f(x_2)$，则<strong>单调递减</strong>。"))+
 thm("复合函数单调性",p("设 $y=f(g(x))$，内层 $u=g(x)$，外层 $y=f(u)$。若内外层单调性相同，则复合函数递增；若相反，则递减。口诀「<strong>同增异减</strong>」。"))+
 der(p("<strong>推导：</strong>设 $x_1<x_2$，$g$ 递增则 $g(x_1)<g(x_2)$，即 $u_1<u_2$。若 $f$ 也递增，则 $f(u_1)<f(u_2)$，即 $f(g(x_1))<f(g(x_2))$，复合递增；若 $f$ 递减，则 $f(u_1)>f(u_2)$，复合递减。$g$ 递减时同理可得相同结论。"))+
 app(p("<strong>判定方法：</strong>① 定义法：作差 $f(x_1)-f(x_2)$ 判符号；② 导数法（若可导）：$f'(x)>0$ 递增，$f'(x)<0$ 递减。"))
)},
{"id":"e3s2-2","name":"奇偶性与运算性质","tags":["def","thm","der"],"brief":"奇函数/偶函数的判定与运算性质。",
"body":wrap(
 defn("奇偶性",p("若定义域关于原点对称，且对任意 $x$ 有 $f(-x)=-f(x)$，则 $f(x)$ 为<strong>奇函数</strong>（图像关于原点对称）；若 $f(-x)=f(x)$，则为<strong>偶函数</strong>（图像关于 y 轴对称）。"))+
 thm("运算性质",p("① 奇±奇=奇，偶±偶=偶；② 奇×奇=偶，偶×偶=偶，奇×偶=奇；③ 两个奇函数的复合为奇函数，其他组合按「内层×外层」符号规则。"))+
 der(p("<strong>奇×偶=奇 的推导：</strong>设 $f$ 奇、$g$ 偶，则 $(fg)(-x)=f(-x)g(-x)=(-f(x))\\cdot g(x)=-f(x)g(x)=-(fg)(x)$，故 $fg$ 为奇函数。")+
 p("<strong>奇+奇=奇 的推导：</strong>$(f+g)(-x)=f(-x)+g(-x)=-f(x)-g(x)=-(f(x)+g(x))=-(f+g)(x)$。"))+
 note(p("判断奇偶性前必须先确认<strong>定义域关于原点对称</strong>。奇函数在 $x=0$ 处有定义时必有 $f(0)=0$；偶函数满足 $f(|x|)=f(x)$。"))
)},
{"id":"e3s2-3","name":"有界性与周期性","tags":["def","thm","der"],"brief":"有界函数与周期函数的定义与性质。",
"body":wrap(
 defn("有界性",p("若存在常数 $M$，使对定义域内所有 $x$ 有 $|f(x)|\\le M$，则 $f(x)$ 为<strong>有界函数</strong>。$f(x)\\le M$ 称上有界，$f(x)\\ge m$ 称下有界。"))+
 defn("周期性",p("若存在非零常数 $T$，使对定义域内任意 $x$ 有 $f(x+T)=f(x)$，则 $f(x)$ 为<strong>周期函数</strong>，$T$ 为一个周期。所有正周期中最小的称为<strong>最小正周期</strong>。"))+
 der(p("<strong>周期倍数推导：</strong>若 $T$ 是 $f(x)$ 的周期，则 $f(x+2T)=f((x+T)+T)=f(x+T)=f(x)$，故 $2T$ 也是周期。同理 $nT$（$n\\in\\mathbb{Z},\\ n\\neq 0$）都是周期。")+
 p("<strong>$f(kx)$ 的周期推导：</strong>若 $f(x)$ 周期为 $T$，则 $f(k(x+\\dfrac{T}{|k|}))=f(kx+T)=f(kx)$，故 $f(kx)$ 的周期为 $\\dfrac{T}{|k|}$。例如 $\\sin 2x$ 的周期为 $\\dfrac{2\\pi}{2}=\\pi$。"))+
 note(p("常见周期：$\\sin x,\\cos x$ 周期 $2\\pi$；$\\tan x,\\cot x$ 周期 $\\pi$。常函数是周期函数但无最小正周期。"))
)}
]},
{"name":"3.3 基本初等函数与三角","color":"#0d9488","desc":"指数、对数、幂函数与三角函数公式",
"items":[
{"id":"e3s3-1","name":"指数函数与对数函数","tags":["def","thm","der"],"brief":"指数与对数的定义、性质及换底公式推导。",
"body":wrap(
 defn("指数函数",p("$y=a^x$（$a>0$ 且 $a\\neq 1$），定义域 $\\mathbb{R}$，值域 $(0,+\\infty)$。当 $a>1$ 时单调递增，$0<a<1$ 时单调递减，恒过点 $(0,1)$。"))+
 defn("对数函数",p("$y=\\log_a x$（$a>0$ 且 $a\\neq 1$）是 $y=a^x$ 的反函数，定义域 $(0,+\\infty)$，值域 $\\mathbb{R}$。当 $a>1$ 时单调递增，恒过点 $(1,0)$。"))+
 thm("对数运算法则",p("（$a>0,a\\neq1$，$M,N>0$）")+
 fml("\\log_a(MN)=\\log_aM+\\log_aN,\\quad \\log_a\\dfrac{M}{N}=\\log_aM-\\log_aN")+
 fml("\\log_a M^n = n\\log_a M,\\quad \\log_a b = \\dfrac{\\log_c b}{\\log_c a}\\ (\\text{换底公式})"))+
 der(p("<strong>换底公式推导：</strong>设 $\\log_a b=x$，则 $a^x=b$。两边取以 $c$ 为底的对数：$\\log_c(a^x)=\\log_c b$，由对数幂法则 $x\\log_c a=\\log_c b$，故 $x=\\dfrac{\\log_c b}{\\log_c a}$。")+
 p("<strong>乘积法则推导：</strong>设 $\\log_a M=p$，$\\log_a N=q$，则 $M=a^p$，$N=a^q$。$MN=a^p\\cdot a^q=a^{p+q}$，故 $\\log_a(MN)=p+q=\\log_a M+\\log_a N$。"))
)},
{"id":"e3s3-2","name":"幂函数","tags":["def","exa","der"],"brief":"y=x^α 的图像与性质。",
"body":wrap(
 defn("幂函数",p("形如 $y=x^\\alpha$（$\\alpha$ 为常数）的函数称为<strong>幂函数</strong>。图像恒过点 $(1,1)$。"))+
 p("常见幂函数：① $\\alpha=1$：$y=x$，直线；② $\\alpha=2$：$y=x^2$，抛物线，偶函数；③ $\\alpha=3$：$y=x^3$，奇函数，单调递增；④ $\\alpha=-1$：$y=1/x$，双曲线，奇函数；⑤ $\\alpha=1/2$：$y=\\sqrt{x}$，定义域 $[0,+\\infty)$。")+
 der(p("<strong>过定点推导：</strong>对任意 $\\alpha$，$1^\\alpha=1$，故幂函数图像恒过 $(1,1)$。当 $\\alpha>0$ 时，$0^\\alpha=0$，故也过原点；当 $\\alpha<0$ 时，$x=0$ 处无定义，不过原点。")+
 p("<strong>第一象限单调性推导：</strong>对 $y=x^\\alpha$ 求导（$x>0$），$y'=\\alpha x^{\\alpha-1}$。当 $\\alpha>0$ 时 $y'>0$，递增；当 $\\alpha<0$ 时 $y'<0$，递减。"))+
 note(p("幂函数在第一象限：$\\alpha>1$ 时下凸（递增加快），$0<\\alpha<1$ 时上凸（递增减慢）；$\\alpha<0$ 时递减。"))
)},
{"id":"e3s3-3","name":"三角函数的和差角与倍角公式","tags":["thm","der","exa"],"brief":"和差角公式、二倍角公式及推导。",
"body":wrap(
 thm("和差角公式",p("")+
 fml("\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta")+
 fml("\\cos(\\alpha\\pm\\beta)=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta")+
 fml("\\tan(\\alpha\\pm\\beta)=\\dfrac{\\tan\\alpha\\pm\\tan\\beta}{1\\mp\\tan\\alpha\\tan\\beta}"))+
 der(p("<strong>余弦差角公式推导（单位圆法）：</strong>在单位圆上取点 $A(\\cos\\alpha,\\sin\\alpha)$ 和 $B(\\cos\\beta,\\sin\\beta)$，则 $|AB|^2=(\\cos\\alpha-\\cos\\beta)^2+(\\sin\\alpha-\\sin\\beta)^2=2-2(\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta)$。")+
 p("另一方面，$\\angle AOB=\\alpha-\\beta$，由余弦定理 $|AB|^2=1+1-2\\cos(\\alpha-\\beta)$。比较两式得 $\\cos(\\alpha-\\beta)=\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta$。其他和差角公式可由此及诱导公式推出。"))+
 thm("二倍角公式",p("")+
 fml("\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha")+
 fml("\\cos 2\\alpha=\\cos^2\\alpha-\\sin^2\\alpha=2\\cos^2\\alpha-1=1-2\\sin^2\\alpha")+
 fml("\\tan 2\\alpha=\\dfrac{2\\tan\\alpha}{1-\\tan^2\\alpha}"))+
 der(p("<strong>倍角公式推导：</strong>在和角公式中令 $\\beta=\\alpha$，即得 $\\sin 2\\alpha=\\sin(\\alpha+\\alpha)=\\sin\\alpha\\cos\\alpha+\\cos\\alpha\\sin\\alpha=2\\sin\\alpha\\cos\\alpha$。余弦同理。$\\tan 2\\alpha=\\dfrac{2\\tan\\alpha}{1-\\tan^2\\alpha}$。"))
)},
{"id":"e3s3-4","name":"反三角函数","tags":["def","thm","der"],"brief":"arcsin/arccos/arctan 的定义域、值域与基本关系。",
"body":wrap(
 defn("反正弦函数",p("$y=\\arcsin x$ 是 $y=\\sin x$（$x\\in[-\\pi/2,\\pi/2]$）的反函数。定义域 $[-1,1]$，值域 $[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}]$，单调递增。"))+
 defn("反余弦函数",p("$y=\\arccos x$ 是 $y=\\cos x$（$x\\in[0,\\pi]$）的反函数。定义域 $[-1,1]$，值域 $[0,\\pi]$，单调递减。"))+
 defn("反正切函数",p("$y=\\arctan x$ 是 $y=\\tan x$（$x\\in(-\\pi/2,\\pi/2)$）的反函数。定义域 $\\mathbb{R}$，值域 $(-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2})$，单调递增。"))+
 thm("基本关系",p("")+
 fml("\\arcsin x+\\arccos x=\\dfrac{\\pi}{2}\\quad(x\\in[-1,1])")+
 fml("\\sin(\\arcsin x)=x,\\quad \\arcsin(\\sin x)=x\\ (x\\in[-\\pi/2,\\pi/2])"))+
 der(p("<strong>推导 $\\arcsin x+\\arccos x=\\pi/2$：</strong>设 $\\alpha=\\arcsin x$，则 $\\alpha\\in[-\\pi/2,\\pi/2]$，$\\sin\\alpha=x$。而 $\\cos(\\pi/2-\\alpha)=\\sin\\alpha=x$，且 $\\pi/2-\\alpha\\in[0,\\pi]$，正是 $\\arccos x$ 的主值区间，故 $\\arccos x=\\pi/2-\\alpha$，即 $\\arcsin x+\\arccos x=\\pi/2$。"))
)}
]}
]

# ============ 第四章 数列 ============
ch4_sections = [
{"name":"4.1 等差数列与等比数列","color":"#c2410c","desc":"等差、等比数列的通项与求和",
"items":[
{"id":"e4s1-1","name":"等差数列","tags":["def","thm","der","app"],"brief":"a_n = a_1 + (n-1)d，S_n = n(a_1+a_n)/2。",
"fig":"sequence","figCap":"等差数列各项均匀分布，公差为 d",
"body":wrap(
 defn("等差数列",p("从第二项起，每一项与前一项的差等于同一个常数的数列，称为<strong>等差数列</strong>。该常数称为<strong>公差</strong>，记作 $d$。"))+
 thm("通项公式",p("首项为 $a_1$，公差为 $d$ 的等差数列，第 $n$ 项为：")+
 fml("a_n = a_1 + (n-1)d"))+
 der(p("<strong>归纳推导：</strong>$a_2=a_1+d$，$a_3=a_2+d=a_1+2d$，$a_4=a_1+3d$，……，归纳得 $a_n=a_1+(n-1)d$。")+
 p("通项推广：$a_n=a_m+(n-m)d$。"))+
 thm("前 n 项和",p("")+
 fml("S_n = \\dfrac{n(a_1+a_n)}{2} = na_1 + \\dfrac{n(n-1)}{2}d"))+
 der(p("<strong>倒序相加法推导：</strong>设 $S_n=a_1+a_2+\\cdots+a_n$，倒序写 $S_n=a_n+a_{n-1}+\\cdots+a_1$。两式相加，对应项 $a_i+a_{n+1-i}=a_1+a_n$（共 $n$ 对），得 $2S_n=n(a_1+a_n)$，故 $S_n=\\dfrac{n(a_1+a_n)}{2}$。代入 $a_n=a_1+(n-1)d$ 得第二式。"))+
 app(p("<strong>性质：</strong>若 $m+n=p+q$，则 $a_m+a_n=a_p+a_q$。$S_n, S_{2n}-S_n, S_{3n}-S_{2n}$ 仍成等差数列，公差为 $n^2d$。"))
)},
{"id":"e4s2-1","name":"等比数列","tags":["def","thm","der","app"],"brief":"a_n = a_1·q^(n-1)，S_n = a_1(1-q^n)/(1-q)。",
"body":wrap(
 defn("等比数列",p("从第二项起，每一项与前一项的比等于同一个非零常数的数列，称为<strong>等比数列</strong>。该常数称为<strong>公比</strong>，记作 $q$（$q\\neq 0$）。"))+
 thm("通项公式",p("首项为 $a_1$，公比为 $q$ 的等比数列，第 $n$ 项为：")+
 fml("a_n = a_1 q^{n-1}"))+
 der(p("<strong>归纳推导：</strong>$a_2=a_1q$，$a_3=a_2q=a_1q^2$，……，$a_n=a_1q^{n-1}$。通项推广：$a_n=a_mq^{n-m}$。"))+
 thm("前 n 项和",p("当 $q\\neq 1$ 时：")+
 fml("S_n = \\dfrac{a_1(1-q^n)}{1-q} = \\dfrac{a_1-a_nq}{1-q}"))+
 der(p("<strong>错位相减法推导：</strong>$S_n=a_1+a_1q+\\cdots+a_1q^{n-1}$，两边乘 $q$：$qS_n=a_1q+\\cdots+a_1q^{n-1}+a_1q^n$。两式相减：$S_n-qS_n=a_1-a_1q^n$，即 $(1-q)S_n=a_1(1-q^n)$，故 $S_n=\\dfrac{a_1(1-q^n)}{1-q}$。"))+
 thm("无穷等比级数",p("当 $|q|<1$ 时，无穷项之和为：")+
 fml("S = \\lim_{n\\to\\infty} S_n = \\dfrac{a_1}{1-q}"))+
 der(p("$|q|<1$ 时 $q^n\\to 0$（$n\\to\\infty$），故 $S=\\dfrac{a_1(1-0)}{1-q}=\\dfrac{a_1}{1-q}$。"))+
 app(p("<strong>性质：</strong>若 $m+n=p+q$，则 $a_m\\cdot a_n=a_p\\cdot a_q$。$S_n, S_{2n}-S_n, S_{3n}-S_{2n}$ 成等比数列（公比 $q^n$）。"))
)}
]},
{"name":"4.2 数列二级结论","color":"#ea580c","desc":"中项、片段和性质与 a_n 与 S_n 关系",
"items":[
{"id":"e4s2-2","name":"等差（比）中项与片段和性质","tags":["thm","der"],"brief":"中项公式与片段和的等差/等比性质。",
"body":wrap(
 thm("等差中项",p("若 $a,A,b$ 成等差数列，则 $2A=a+b$，即 $A=\\dfrac{a+b}{2}$。"))+
 thm("等比中项",p("若 $a,G,b$ 成等比数列，则 $G^2=ab$，即 $G=\\pm\\sqrt{ab}$。"))+
 der(p("<strong>等差中项推导：</strong>由等差数列定义 $A-a=b-A$，移项得 $2A=a+b$。")+
 p("<strong>等比中项推导：</strong>由等比数列定义 $\\dfrac{G}{a}=\\dfrac{b}{G}$，交叉相乘得 $G^2=ab$。"))+
 thm("片段和性质",p("等差数列 $\\{a_n\\}$：$S_n, S_{2n}-S_n, S_{3n}-S_{2n}$ 成等差数列，公差为 $n^2d$。<br>等比数列 $\\{a_n\\}$：$S_n, S_{2n}-S_n, S_{3n}-S_{2n}$ 成等比数列，公比为 $q^n$（$S_n\\neq 0$）。"))+
 der(p("<strong>等差片段和推导：</strong>$(S_{2n}-S_n)-S_n=(a_{n+1}+\\cdots+a_{2n})-(a_1+\\cdots+a_n)$。每一项 $a_{n+k}-a_k=nd$（$k=1,\\dots,n$），共 $n$ 项，故差为 $n\\cdot nd=n^2d$。同理 $(S_{3n}-S_{2n})-(S_{2n}-S_n)=n^2d$，三者成等差。"))
)},
{"id":"e4s2-3","name":"a_n 与 S_n 的关系","tags":["thm","der","exa"],"brief":"由前 n 项和 S_n 求通项 a_n 的公式。",
"body":wrap(
 thm("a_n 与 S_n 关系",p("设 $S_n=a_1+a_2+\\cdots+a_n$，则：")+
 fml("a_n = \\begin{cases} S_1, & n=1 \\\\ S_n-S_{n-1}, & n\\ge 2 \\end{cases}"))+
 der(p("<strong>推导：</strong>当 $n\\ge 2$ 时，$S_n=a_1+\\cdots+a_n$，$S_{n-1}=a_1+\\cdots+a_{n-1}$，两式相减得 $S_n-S_{n-1}=a_n$。当 $n=1$ 时，$S_1=a_1$，必须单独验证，因为 $S_0$ 通常无定义。")+
 p("<strong>注意：</strong>由 $S_n$ 求 $a_n$ 时，必须验证 $n=1$ 是否满足 $n\\ge 2$ 时的表达式。若满足，可写成统一公式；若不满足，必须分段写。"))+
 exa(p("<strong>例：</strong>已知 $S_n=n^2+1$，求 $a_n$。$n=1$ 时 $a_1=S_1=2$；$n\\ge 2$ 时 $a_n=S_n-S_{n-1}=n^2+1-[(n-1)^2+1]=2n-1$。验证 $n=1$：$2\\times1-1=1\\neq 2$，故 $a_n=\\begin{cases}2,&n=1\\\\2n-1,&n\\ge2\\end{cases}$。"))
)}
]},
{"name":"4.3 数列求和与求通项方法","color":"#f59e0b","desc":"错位相减、裂项相消、分组求和、累加累乘等",
"items":[
{"id":"e4s3-1","name":"公式法与倒序相加法","tags":["def","exa","der"],"brief":"直接套公式与倒序相加求和。",
"body":wrap(
 defn("公式法",p("直接利用等差、等比数列求和公式，或常用幂和公式：")+
 fml("\\sum_{k=1}^n k=\\dfrac{n(n+1)}{2},\\quad \\sum_{k=1}^n k^2=\\dfrac{n(n+1)(2n+1)}{6},\\quad \\sum_{k=1}^n k^3=\\left[\\dfrac{n(n+1)}{2}\\right]^2"))+
 defn("倒序相加法",p("将数列倒序排列后与原式相加，利用对应项之和为定值的方法。"))+
 der(p("<strong>平方和公式推导：</strong>由 $(k+1)^3-k^3=3k^2+3k+1$，对 $k=1,2,\\dots,n$ 求和，左边 $\\sum_{k=1}^n[(k+1)^3-k^3]=(n+1)^3-1$（望远镜求和）。右边 $=3\\sum k^2+3\\sum k+n$。代入 $\\sum k=\\dfrac{n(n+1)}{2}$，解得 $\\sum k^2=\\dfrac{n(n+1)(2n+1)}{6}$。"))+
 exa(p("<strong>倒序相加例：</strong>求 $S=\\sin^2 1°+\\sin^2 2°+\\cdots+\\sin^2 89°$。注意 $\\sin^2 k°+\\sin^2(90°-k°)=\\sin^2 k°+\\cos^2 k°=1$。倒序相加：$2S=(\\sin^21°+\\sin^289°)+\\cdots+(\\sin^289°+\\sin^21°)=89$，故 $S=89/2$。"))
)},
{"id":"e4s3-2","name":"错位相减法","tags":["thm","der","exa"],"brief":"适用于等差×等比型数列求和。",
"body":wrap(
 defn("错位相减法",p("设 $c_n=a_n\\cdot b_n$，其中 $\\{a_n\\}$ 等差、$\\{b_n\\}$ 等比（公比 $q$）。写出 $S_n$ 与 $qS_n$，错位相减后化为等比求和。"))+
 der(p("<strong>推导：</strong>$S_n=a_1b_1+a_2b_2+\\cdots+a_nb_n$，$qS_n=a_1b_2+a_2b_3+\\cdots+a_nb_{n+1}$。两式相减：$(1-q)S_n=a_1b_1+(a_2-a_1)b_2+\\cdots+(a_n-a_{n-1})b_n-a_nb_{n+1}$。由于 $a_i-a_{i-1}=d$（公差），中间项为 $d(b_2+\\cdots+b_n)$，是等比数列求和，可解出 $S_n$。"))+
 exa(p("<strong>例：</strong>求 $S_n=1+2x+3x^2+\\cdots+nx^{n-1}$（$x\\neq 1$）。<br>$xS_n=x+2x^2+\\cdots+(n-1)x^{n-1}+nx^n$，两式相减：$(1-x)S_n=1+x+x^2+\\cdots+x^{n-1}-nx^n=\\dfrac{1-x^n}{1-x}-nx^n$，故 $S_n=\\dfrac{1-x^n}{(1-x)^2}-\\dfrac{nx^n}{1-x}$。"))
)},
{"id":"e4s3-3","name":"裂项相消法","tags":["def","exa","der"],"brief":"将通项拆成两项之差，相消求和。",
"body":wrap(
 defn("裂项相消",p("将数列的每一项拆成两项之差，使得求和时中间项相互抵消。常见裂项：")+
 fml("\\dfrac{1}{n(n+1)} = \\dfrac{1}{n}-\\dfrac{1}{n+1}")+
 fml("\\dfrac{1}{n(n+d)} = \\dfrac{1}{d}\\left(\\dfrac{1}{n}-\\dfrac{1}{n+d}\\right)")+
 fml("\\dfrac{1}{\\sqrt{n+1}+\\sqrt{n}} = \\sqrt{n+1}-\\sqrt{n}"))+
 der(p("<strong>裂项公式推导：</strong>设 $\\dfrac{1}{n(n+d)}=\\dfrac{A}{n}+\\dfrac{B}{n+d}$，通分右边 $=\\dfrac{A(n+d)+Bn}{n(n+d)}=\\dfrac{(A+B)n+Ad}{n(n+d)}$。与左边比较系数：$A+B=0$，$Ad=1$，解得 $A=1/d$，$B=-1/d$，故 $\\dfrac{1}{n(n+d)}=\\dfrac{1}{d}\\left(\\dfrac{1}{n}-\\dfrac{1}{n+d}\\right)$。"))+
 exa(p("<strong>例：</strong>求 $S_n=\\dfrac{1}{1\\cdot 2}+\\dfrac{1}{2\\cdot 3}+\\cdots+\\dfrac{1}{n(n+1)}$。<br>由裂项 $\\dfrac{1}{k(k+1)}=\\dfrac{1}{k}-\\dfrac{1}{k+1}$，$S_n=\\left(1-\\dfrac{1}{2}\\right)+\\left(\\dfrac{1}{2}-\\dfrac{1}{3}\\right)+\\cdots+\\left(\\dfrac{1}{n}-\\dfrac{1}{n+1}\\right)=1-\\dfrac{1}{n+1}=\\dfrac{n}{n+1}$。"))
)},
{"id":"e4s3-4","name":"分组求和与并项求和","tags":["def","exa","der"],"brief":"分组后分别求和与相邻两项合并求和。",
"body":wrap(
 defn("分组求和法",p("将数列的项分成若干组，每组利用公式分别求和再合并。适用于通项由若干可求和部分组成的数列。"))+
 defn("并项求和法",p("将相邻两项（或若干项）合并为一项，构造新的可求和数列。常用于含 $(-1)^n$ 的摆动数列。"))+
 der(p("<strong>分组求和推导：</strong>若 $a_n=b_n+c_n$，则 $S_n=\\sum_{k=1}^n a_k=\\sum_{k=1}^n b_k+\\sum_{k=1}^n c_k$，分别对 $\\{b_n\\},\\{c_n\\}$ 求和。")+
 p("<strong>并项求和推导：</strong>对摆动数列 $a_n=(-1)^n f(n)$，常将两项合并：$a_{2k-1}+a_{2k}=-f(2k-1)+f(2k)$，构造新数列 $b_k=a_{2k-1}+a_{2k}$ 后求和。"))+
 exa(p("<strong>分组求和例：</strong>求 $S_n=(1+2)+(2+4)+\\cdots+(n+2^n)$。分组：$S_n=(1+2+\\cdots+n)+(2+4+\\cdots+2^n)=\\dfrac{n(n+1)}{2}+\\dfrac{2(1-2^n)}{1-2}=\\dfrac{n(n+1)}{2}+2^{n+1}-2$。")+
 p("<strong>并项求和例：</strong>求 $S_n=-1+2-3+4-\\cdots+(-1)^n n$。当 $n$ 为偶数，$S_n=(-1+2)+(-3+4)+\\cdots=\\dfrac{n}{2}$；当 $n$ 为奇数，$S_n=\\dfrac{n-1}{2}-n=-\\dfrac{n+1}{2}$。"))
)},
{"id":"e4s3-5","name":"累加法与累乘法求通项","tags":["thm","der","exa"],"brief":"由递推关系 a_{n+1}-a_n=f(n) 或 a_{n+1}/a_n=f(n) 求通项。",
"body":wrap(
 thm("累加法",p("若 $a_{n+1}-a_n=f(n)$，则：")+
 fml("a_n = a_1 + \\sum_{k=1}^{n-1} f(k)\\quad(n\\ge 2)"))+
 thm("累乘法",p("若 $\\dfrac{a_{n+1}}{a_n}=f(n)$，则：")+
 fml("a_n = a_1 \\cdot \\prod_{k=1}^{n-1} f(k)\\quad(n\\ge 2)"))+
 der(p("<strong>累加法推导：</strong>由 $a_{n+1}-a_n=f(n)$，令 $n=1,2,\\dots,n-1$ 得：$a_2-a_1=f(1)$，$a_3-a_2=f(2)$，……，$a_n-a_{n-1}=f(n-1)$。将这 $n-1$ 个式子相加，左边抵消后得 $a_n-a_1=\\sum_{k=1}^{n-1}f(k)$，即 $a_n=a_1+\\sum_{k=1}^{n-1}f(k)$。")+
 p("<strong>累乘法推导：</strong>由 $\\dfrac{a_{n+1}}{a_n}=f(n)$，令 $n=1,2,\\dots,n-1$ 得：$\\dfrac{a_2}{a_1}=f(1)$，……，$\\dfrac{a_n}{a_{n-1}}=f(n-1)$。各式相乘，左边抵消得 $\\dfrac{a_n}{a_1}=\\prod_{k=1}^{n-1}f(k)$。"))+
 exa(p("<strong>累加例：</strong>$a_1=1$，$a_{n+1}-a_n=n$，求 $a_n$。$a_n=a_1+\\sum_{k=1}^{n-1}k=1+\\dfrac{(n-1)n}{2}$。")+
 p("<strong>累乘例：</strong>$a_1=1$，$\\dfrac{a_{n+1}}{a_n}=\\dfrac{n}{n+1}$，求 $a_n$。$a_n=a_1\\cdot\\prod_{k=1}^{n-1}\\dfrac{k}{k+1}=1\\cdot\\dfrac{1}{2}\\cdot\\dfrac{2}{3}\\cdots\\dfrac{n-1}{n}=\\dfrac{1}{n}$。"))
)}
]}
]

# ============ 第五章 平面几何 ============
ch5_sections = [
{"name":"5.1 三角形","color":"#be185d","desc":"全等相似、勾股定理、正余弦定理与面积公式",
"items":[
{"id":"e5s1-1","name":"全等三角形与相似三角形","tags":["def","thm","der"],"brief":"全等判定与相似判定、性质。",
"body":wrap(
 defn("全等三角形",p("能够完全重合的两个三角形称为<strong>全等三角形</strong>。全等三角形的对应边相等、对应角相等。"))+
 thm("全等判定",p("① <strong>SSS</strong>（边边边）：三边对应相等；<br>② <strong>SAS</strong>（边角边）：两边及其夹角对应相等；<br>③ <strong>ASA</strong>（角边角）：两角及其夹边对应相等；<br>④ <strong>AAS</strong>（角角边）：两角及其中一角的对边对应相等。"))+
 defn("相似三角形",p("对应角相等、对应边成比例的两个三角形称为<strong>相似三角形</strong>。相似比 $k$ 等于对应边之比。"))+
 thm("相似判定与性质",p("判定：AA（两角对应相等）、SAS（两边成比例且夹角相等）、SSS（三边成比例）。<br>性质：对应角相等，对应边、周长、对应线段之比等于相似比 $k$，面积比等于 $k^2$。"))+
 der(p("<strong>面积比推导：</strong>设相似比为 $k$，对应底边和高分别为 $a,ka$ 和 $h,kh$。面积比 $=\\dfrac{\\frac{1}{2}(ka)(kh)}{\\frac{1}{2}ah}=k^2$。"))
)},
{"id":"e5s1-2","name":"勾股定理","tags":["thm","der"],"brief":"直角三角形两直角边平方和等于斜边平方。",
"fig":"triangle","figCap":"三角形 ABC，底边 a，高 h，三边 a,b,c",
"body":wrap(
 thm("勾股定理",p("直角三角形中，两直角边 $a,b$ 的平方和等于斜边 $c$ 的平方：")+
 fml("a^2+b^2=c^2"))+
 der(p("<strong>证明（面积法）：</strong>构造边长为 $a+b$ 的正方形，内部以四个全等的直角三角形（直角边 $a,b$，斜边 $c$）拼成一个边长为 $c$ 的小正方形（中间）。大正方形面积 $=(a+b)^2$，也等于 $4\\times\\dfrac{1}{2}ab+c^2$。")+
 fml("(a+b)^2 = 2ab + c^2")+
 p("展开左边：$a^2+2ab+b^2=2ab+c^2$，两边消去 $2ab$，得 $a^2+b^2=c^2$。"))+
 note(p("勾股定理逆定理：若三角形三边满足 $a^2+b^2=c^2$，则该三角形为直角三角形（$c$ 所对的角为直角）。常见勾股数：3-4-5，5-12-13，8-15-17。"))
)},
{"id":"e5s1-3","name":"正弦定理与余弦定理","tags":["thm","der","app"],"brief":"解三角形的基本工具。",
"body":wrap(
 thm("正弦定理",p("在 $\\triangle ABC$ 中，$R$ 为外接圆半径：")+
 fml("\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R"))+
 der(p("<strong>证明（外接圆法）：</strong>作 $\\triangle ABC$ 的外接圆，直径为 $2R$。过 $B$ 作直径 $BD$，则 $\\angle BCD=90°$（直径所对圆周角），且 $\\angle BDC=\\angle BAC=\\angle A$（同弧 $BC$）。在 $Rt\\triangle BCD$ 中，$\\sin\\angle BDC=\\dfrac{BC}{BD}=\\dfrac{a}{2R}$，即 $\\sin A=\\dfrac{a}{2R}$，故 $\\dfrac{a}{\\sin A}=2R$。同理得其他。"))+
 thm("余弦定理",p("")+
 fml("c^2 = a^2+b^2-2ab\\cos C"))+
 der(p("<strong>证明（向量法）：</strong>设 $\\vec{AB}=\\vec{c}$，$\\vec{CB}=\\vec{a}$，$\\vec{CA}=\\vec{b}$，则 $\\vec{c}=\\vec{a}-\\vec{b}$。两边取模的平方：$|\\vec{c}|^2=|\\vec{a}-\\vec{b}|^2=|\\vec{a}|^2+|\\vec{b}|^2-2\\vec{a}\\cdot\\vec{b}=a^2+b^2-2ab\\cos C$。"))+
 app(p("<strong>适用场景：</strong>正弦定理适用于已知两角一边或两边一对角；余弦定理适用于已知两边夹角或三边。"))
)},
{"id":"e5s1-4","name":"三角形面积公式","tags":["thm","der","app"],"brief":"底乘高、两边夹角、海伦公式、内切圆半径。",
"body":wrap(
 thm("面积公式汇总",p("")+
 fml("S = \\dfrac{1}{2}ah = \\dfrac{1}{2}ab\\sin C = \\sqrt{p(p-a)(p-b)(p-c)} = pr = \\dfrac{abc}{4R}"))+
 p("其中 $p=\\dfrac{a+b+c}{2}$ 为半周长，$r$ 为内切圆半径，$R$ 为外接圆半径。")+
 der(p("<strong>两边夹角公式推导：</strong>以 $a$ 为底，高 $h=b\\sin C$（$b$ 边上的高在 $C$ 角处的投影），故 $S=\\dfrac{1}{2}ah=\\dfrac{1}{2}ab\\sin C$。")+
 p("<strong>海伦公式推导：</strong>由 $S=\\dfrac{1}{2}ab\\sin C$ 和余弦定理 $\\cos C=\\dfrac{a^2+b^2-c^2}{2ab}$，$\\sin C=\\sqrt{1-\\cos^2 C}$。代入化简，利用 $p=\\dfrac{a+b+c}{2}$ 可得 $S=\\sqrt{p(p-a)(p-b)(p-c)}$。")+
 p("<strong>内切圆半径法推导：</strong>三角形可分为以内切圆圆心为顶点的三个小三角形，底分别为 $a,b,c$，高均为 $r$，故 $S=\\dfrac{1}{2}ar+\\dfrac{1}{2}br+\\dfrac{1}{2}cr=\\dfrac{a+b+c}{2}r=pr$。"))+
 app(p("<strong>选择口诀：</strong>已知底和高用 $\\dfrac{1}{2}ah$；已知两边夹角用 $\\dfrac{1}{2}ab\\sin C$；已知三边用海伦公式；已知内切圆半径用 $pr$。"))
)}
]},
{"name":"5.2 四边形与圆","color":"#db2777","desc":"四边形性质判定与圆的定理",
"items":[
{"id":"e5s2-1","name":"四边形的性质与判定","tags":["def","thm","der"],"brief":"平行四边形、矩形、菱形、正方形、梯形。",
"body":wrap(
 thm("平行四边形",p("<strong>性质：</strong>对边平行且相等，对角相等，对角线互相平分。<br><strong>判定：</strong>两组对边分别平行（或相等）；一组对边平行且相等；对角线互相平分。")+
 fml("S_{\\text{平行四边形}} = ah = ab\\sin\\theta"))+
 thm("矩形与菱形",p("<strong>矩形：</strong>有一个角是直角的平行四边形。对角线相等且互相平分。$S=ab$。<br><strong>菱形：</strong>有一组邻边相等的平行四边形。对角线互相垂直平分。$S=\\dfrac{1}{2}d_1d_2$（$d_1,d_2$ 为对角线）。"))+
 thm("正方形与梯形",p("<strong>正方形：</strong>既是矩形又是菱形，四边相等四角直角。$S=a^2$。<br><strong>梯形：</strong>一组对边平行。$S=\\dfrac{(a+b)h}{2}$（$a,b$ 为上下底，$h$ 为高）。<strong>等腰梯形</strong>对角线相等。"))+
 der(p("<strong>菱形面积推导：</strong>菱形对角线互相垂直，将菱形分成四个全等直角三角形。每个三角形面积 $=\\dfrac{1}{2}\\cdot\\dfrac{d_1}{2}\\cdot\\dfrac{d_2}{2}=\\dfrac{d_1d_2}{8}$，四个共 $4\\times\\dfrac{d_1d_2}{8}=\\dfrac{d_1d_2}{2}$。"))+
 note(p("正方形是特殊的矩形和菱形，具备所有性质。梯形中位线 $=\\dfrac{a+b}{2}$，面积 $=$ 中位线 $\\times$ 高。"))
)},
{"id":"e5s2-2","name":"圆的基本性质","tags":["thm","der"],"brief":"垂径定理、圆周角定理及其推论。",
"fig":"circle","figCap":"圆 O，半径 r，周长 C=2πr，面积 S=πr²",
"body":wrap(
 thm("垂径定理",p("垂直于弦的直径平分这条弦，并且平分弦所对的两条弧。"))+
 der(p("<strong>证明：</strong>设直径 $CD\\perp$ 弦 $AB$ 于 $E$，圆心为 $O$。$OA=OB$（半径），$OE$ 公共，$\\angle OEA=\\angle OEB=90°$，故 $\\triangle OEA\\cong\\triangle OEB$（HL），得 $AE=EB$。弧的平分由对应圆心角相等推出。"))+
 thm("圆周角定理",p("同弧所对的圆周角等于圆心角的一半。")+
 fml("\\angle ACB = \\dfrac{1}{2}\\angle AOB"))+
 der(p("<strong>证明（圆心在圆周角一边上）：</strong>设 $O$ 在 $CA$ 上，$OB=OC$（半径），故 $\\triangle OBC$ 等腰，$\\angle OCB=\\angle OBC$。$\\angle AOB$ 是 $\\triangle OBC$ 的外角，$\\angle AOB=\\angle OCB+\\angle OBC=2\\angle ACB$，故 $\\angle ACB=\\dfrac{1}{2}\\angle AOB$。圆心在角内或角外时同理可证。"))+
 thm("推论",p("① 同弧或等弧所对的圆周角相等；<br>② 半圆（或直径）所对的圆周角是直角（$90°$）；<br>③ $90°$ 的圆周角所对的弦是直径。"))
)},
{"id":"e5s2-3","name":"切线与圆幂定理","tags":["thm","der"],"brief":"切线判定、切割线定理与相交弦定理。",
"body":wrap(
 thm("切线判定与性质",p("<strong>判定：</strong>经过半径外端且垂直于这条半径的直线是圆的切线。<br><strong>性质：</strong>圆的切线垂直于经过切点的半径。切线长相等：从圆外一点引圆的两条切线，切线长相等。"))+
 thm("切割线定理",p("从圆外一点 $P$ 引切线 $PT$（$T$ 为切点）和割线 $PAB$（$A,B$ 为交点），则：")+
 fml("PT^2 = PA\\cdot PB"))+
 der(p("<strong>证明：</strong>连接 $TA, TB$。由弦切角定理，$\\angle PTA=\\angle PBT$（弦切角等于所夹弧的圆周角）。又 $\\angle P$ 公共，故 $\\triangle PTA\\sim\\triangle PBT$，得 $\\dfrac{PT}{PB}=\\dfrac{PA}{PT}$，即 $PT^2=PA\\cdot PB$。"))+
 thm("相交弦定理",p("圆内两弦 $AB,CD$ 交于 $P$，则 $PA\\cdot PB=PC\\cdot PD$。"))+
 der(p("<strong>证明：</strong>连接 $AC,BD$。$\\angle A=\\angle D$（同弧 $BC$），$\\angle C=\\angle B$（同弧 $AD$），故 $\\triangle PAC\\sim\\triangle PDB$，得 $\\dfrac{PA}{PD}=\\dfrac{PC}{PB}$，即 $PA\\cdot PB=PC\\cdot PD$。"))
)}
]},
{"name":"5.3 平面图形面积与周长图表","color":"#f472b6","desc":"常见平面图形面积周长公式汇总",
"items":[
{"id":"e5s3-1","name":"常见平面图形面积周长公式表","tags":["thm","der"],"brief":"三角形、四边形、圆、扇形、弓形的面积周长公式汇总。",
"body":wrap(
 thm("公式汇总表",p("")+
 fml("\\begin{array}{c|c|c} \\text{图形} & \\text{周长} & \\text{面积} \\\\ \\hline \\text{三角形} & a+b+c & \\dfrac{1}{2}ah=\\dfrac{1}{2}ab\\sin C \\\\ \\text{矩形} & 2(a+b) & ab \\\\ \\text{平行四边形} & 2(a+b) & ah=ab\\sin\\theta \\\\ \\text{菱形} & 4a & \\dfrac{1}{2}d_1d_2 \\\\ \\text{正方形} & 4a & a^2 \\\\ \\text{梯形} & a+b+c+d & \\dfrac{(a+b)h}{2} \\\\ \\text{圆} & 2\\pi r & \\pi r^2 \\\\ \\text{扇形} & l+2r & \\dfrac{1}{2}lr=\\dfrac{1}{2}\\alpha r^2 \\\\ \\end{array}"))+
 der(p("<strong>扇形面积推导：</strong>扇形面积与圆心角成正比。整圆面积 $\\pi r^2$ 对应圆心角 $2\\pi$，故圆心角 $\\alpha$（弧度）的扇形面积 $S=\\dfrac{\\alpha}{2\\pi}\\cdot\\pi r^2=\\dfrac{1}{2}\\alpha r^2$。又弧长 $l=\\alpha r$，代入得 $S=\\dfrac{1}{2}lr$。")+
 p("<strong>弓形面积：</strong>弓形 $=$ 扇形 $-$ 三角形。$S_{\\text{弓形}}=\\dfrac{1}{2}r^2(\\alpha-\\sin\\alpha)$（$\\alpha$ 为圆心角弧度）。"))+
 note(p("记忆要点：圆的所有公式都与半径 $r$ 相关；扇形面积类比三角形 $\\dfrac{1}{2}\\times$ 底 $\\times$ 高（底为弧长 $l$，高为半径 $r$）。"))
)}
]}
]

# ============ 第六章 立体几何 ============
ch6_sections = [
{"name":"6.1 空间几何体","color":"#7c3aed","desc":"柱锥台球的概念与体积表面积公式",
"items":[
{"id":"e6s1-1","name":"空间几何体的概念","tags":["def","thm"],"brief":"棱柱、棱锥、棱台、圆柱、圆锥、圆台、球。",
"body":wrap(
 defn("棱柱",p("有两个面互相平行，其余各面都是四边形，且每相邻两个四边形的公共边互相平行的多面体。侧棱垂直于底面的棱柱叫<strong>直棱柱</strong>，底面是正多边形的直棱柱叫<strong>正棱柱</strong>。"))+
 defn("棱锥与棱台",p("<strong>棱锥</strong>：有一个面是多边形，其余各面都是有一个公共顶点的三角形的多面体。<strong>棱台</strong>：用平行于棱锥底面的平面截棱锥，截面与底面之间的部分。"))+
 defn("旋转体",p("<strong>圆柱</strong>：矩形绕一边旋转而成；<strong>圆锥</strong>：直角三角形绕直角边旋转而成；<strong>圆台</strong>：直角梯形绕垂直于底的腰旋转而成；<strong>球</strong>：半圆绕直径旋转而成。"))+
 thm("面积体积基本公式",p("")+
 fml("V_{\\text{柱}}=Sh,\\quad V_{\\text{锥}}=\\dfrac{1}{3}Sh,\\quad V_{\\text{台}}=\\dfrac{1}{3}h(S_{\\text{上}}+\\sqrt{S_{\\text{上}}S_{\\text{下}}}+S_{\\text{下}})")+
 fml("V_{\\text{球}}=\\dfrac{4}{3}\\pi R^3,\\quad S_{\\text{球}}=4\\pi R^2"))+
 der(p("<strong>台体体积公式推导：</strong>台体可看作大棱锥截去小棱锥。设大棱锥高 $H$，小棱锥高 $H-h$，相似比 $\\sqrt{S_{\\text{上}}/S_{\\text{下}}}=k$。$V=\\dfrac{1}{3}S_{\\text{下}}H-\\dfrac{1}{3}S_{\\text{上}}(H-h)$。由 $\\dfrac{H-h}{H}=k$ 得 $H=\\dfrac{h}{1-k}$，代入化简得 $V=\\dfrac{1}{3}h(S_{\\text{上}}+\\sqrt{S_{\\text{上}}S_{\\text{下}}}+S_{\\text{下}})$。"))
)},
{"id":"e6s1-2","name":"旋转体与球的公式","tags":["thm","der"],"brief":"圆柱、圆锥、圆台、球的侧面积与体积。",
"fig":"cone","figCap":"圆锥，底面半径 r，高 h，体积 V=πr²h/3",
"body":wrap(
 thm("圆柱",p("")+
 fml("S_{\\text{侧}}=2\\pi rh,\\quad S_{\\text{表}}=2\\pi r(r+h),\\quad V=\\pi r^2h"))+
 thm("圆锥",p("")+
 fml("S_{\\text{侧}}=\\pi rl,\\quad S_{\\text{表}}=\\pi r(r+l),\\quad V=\\dfrac{1}{3}\\pi r^2h"))+
 p("其中 $l=\\sqrt{r^2+h^2}$ 为母线长。")+
 thm("圆台",p("")+
 fml("S_{\\text{侧}}=\\pi(R+r)l,\\quad V=\\dfrac{1}{3}\\pi h(R^2+Rr+r^2)"))+
 thm("球",p("")+
 fml("S_{\\text{球}}=4\\pi R^2,\\quad V_{\\text{球}}=\\dfrac{4}{3}\\pi R^3"))+
 der(p("<strong>球体积推导（祖暅原理）：</strong>取半径为 $R$ 的半球，与「底面半径和高均为 $R$ 的圆柱挖去一个等底等高的圆锥」比较。在任一高度 $h$ 处，半球截面面积 $=\\pi(R^2-h^2)$，圆柱挖圆锥后截面面积 $=\\pi R^2-\\pi h^2=\\pi(R^2-h^2)$。由祖暅原理（幂势既同则积不容异）两者体积相等，故半球体积 $=\\pi R^3-\\dfrac{1}{3}\\pi R^3=\\dfrac{2}{3}\\pi R^3$，球体积 $=\\dfrac{4}{3}\\pi R^3$。")+
 p("<strong>圆锥体积推导：</strong>等底等高的圆柱与圆锥，圆锥体积是圆柱的 $\\dfrac{1}{3}$。可由三个全等等底等高圆锥拼成一个圆柱（实验/积分验证）得到。"))
)}
]},
{"name":"6.2 空间中的线面关系","color":"#8b5cf6","desc":"线线、线面、面面的平行与垂直判定与性质",
"items":[
{"id":"e6s2-1","name":"线面平行与垂直的判定","tags":["def","thm","der"],"brief":"线面平行、面面平行、线面垂直、面面垂直。",
"body":wrap(
 thm("线面平行判定",p("若平面外一条直线与此平面内的一条直线平行，则该直线与此平面平行。（线线平行 $\\Rightarrow$ 线面平行）"))+
 thm("面面平行判定",p("若一个平面内有两条相交直线都平行于另一个平面，则这两个平面平行。"))+
 thm("线面垂直判定",p("若一条直线与一个平面内的两条相交直线都垂直，则该直线与此平面垂直。"))+
 thm("面面垂直判定",p("若一个平面经过另一个平面的一条垂线，则这两个平面互相垂直。"))+
 der(p("<strong>线面平行判定推导：</strong>设直线 $a\\not\\subset\\alpha$，$b\\subset\\alpha$，$a\\parallel b$。反证：若 $a$ 不平行 $\\alpha$，则 $a$ 与 $\\alpha$ 相交于某点 $P$。因 $a\\parallel b$，$a,b$ 确定平面 $\\beta$，$P\\in\\alpha\\cap\\beta=b$，故 $P\\in b$，但 $a\\cap b=P$ 与 $a\\parallel b$ 矛盾。故 $a\\parallel\\alpha$。")+
 p("<strong>面面垂直推导：</strong>设 $l\\perp\\beta$，$l\\subset\\alpha$。过 $l$ 与 $\\beta$ 的交点作 $\\beta$ 内垂直于交线的直线 $m$，则 $l\\perp m$，故二面角的平面角为 $90°$，$\\alpha\\perp\\beta$。"))+
 note(p("关键思想：<strong>线线关系 → 线面关系 → 面面关系</strong>，逐层转化。性质定理反向使用：面面平行→线面平行→线线平行。"))
)},
{"id":"e6s2-2","name":"空间角与空间距离","tags":["def","thm","der"],"brief":"异面直线角、线面角、二面角与点面距离。",
"body":wrap(
 defn("异面直线所成角",p("将两条异面直线平移至相交，所成的锐角或直角称为异面直线所成角，范围 $(0°,90°]$。"))+
 defn("线面角",p("直线与平面所成角是直线与其在平面内的射影所成的锐角，范围 $[0°,90°]$。当直线垂直于平面时为 $90°$，平行或在平面内时为 $0°$。"))+
 defn("二面角",p("从一条直线出发的两个半平面所组成的图形。其平面角是在棱上任取一点，分别在两个半平面内作垂直于棱的射线所成的角，范围 $[0°,180°]$。"))+
 defn("空间距离",p("<strong>点到面：</strong>点到平面的垂线段长度；<strong>线到面：</strong>直线上一点到平面的距离（线面平行时）；<strong>面到面：</strong>一个平面内一点到另一平面的距离（面面平行时）。"))+
 der(p("<strong>点到面距离推导（体积法）：</strong>设点 $P$ 到平面 $\\alpha$ 距离为 $h$，平面 $\\alpha$ 内三角形 $ABC$ 面积为 $S$。三棱锥 $P-ABC$ 体积 $V=\\dfrac{1}{3}Sh$，故 $h=\\dfrac{3V}{S}$。通过换底求 $V$ 即可得到 $h$。")+
 p("<strong>线面角计算：</strong>设直线方向向量 $\\vec{a}$，平面法向量 $\\vec{n}$，线面角 $\\theta$，则 $\\sin\\theta=|\\cos\\langle\\vec{a},\\vec{n}\\rangle|$，即 $\\theta=\\arcsin\\dfrac{|\\vec{a}\\cdot\\vec{n}|}{|\\vec{a}||\\vec{n}|}$。")+
 p("<strong>二面角计算：</strong>设两个半平面的法向量为 $\\vec{n_1},\\vec{n_2}$，则二面角 $\\varphi$ 满足 $\\cos\\varphi=\\pm\\dfrac{\\vec{n_1}\\cdot\\vec{n_2}}{|\\vec{n_1}||\\vec{n_2}|}$，符号由二面角实际为锐角或钝角决定。"))+
 note(p("求空间角的通法：<strong>找（作）角 → 证明 → 计算</strong>，常通过向量法转化为向量夹角计算。"))
)}
]},
{"name":"6.3 立体几何体积与表面积图表","color":"#a78bfa","desc":"常见立体几何体侧面积、表面积、体积公式汇总",
"items":[
{"id":"e6s3-1","name":"柱锥台球公式汇总表","tags":["thm","der"],"brief":"棱柱、棱锥、圆柱、圆锥、球的侧面积、表面积、体积公式。",
"fig":"cube","figCap":"正方体示意图，棱长为 a",
"body":wrap(
 thm("公式汇总表",p("")+
 fml("\\begin{array}{c|c|c|c} \\text{几何体} & \\text{侧面积} & \\text{表面积} & \\text{体积} \\\\ \\hline \\text{直棱柱} & ch & ch+2S & Sh \\\\ \\text{正棱锥} & \\dfrac{1}{2}ch' & \\dfrac{1}{2}ch'+S & \\dfrac{1}{3}Sh \\\\ \\text{圆柱} & 2\\pi rh & 2\\pi r(r+h) & \\pi r^2h \\\\ \\text{圆锥} & \\pi rl & \\pi r(r+l) & \\dfrac{1}{3}\\pi r^2h \\\\ \\text{圆台} & \\pi(R+r)l & \\pi(R^2+r^2+(R+r)l) & \\dfrac{1}{3}\\pi h(R^2+Rr+r^2) \\\\ \\text{球} & - & 4\\pi R^2 & \\dfrac{4}{3}\\pi R^3 \\\\ \\end{array}"))+
 der(p("<strong>圆柱侧面积推导：</strong>将圆柱侧面沿一条母线展开，得到一个长方形，长为底面圆周长 $2\\pi r$，宽为圆柱的高 $h$，故 $S_{\\text{侧}}=2\\pi rh$。")+
 p("<strong>圆锥侧面积推导：</strong>将圆锥侧面展开为扇形，扇形半径为母线长 $l$，弧长为底面周长 $2\\pi r$。扇形面积 $=\\dfrac{1}{2}\\times$ 弧长 $\\times$ 半径 $=\\dfrac{1}{2}\\times 2\\pi r\\times l=\\pi rl$。")+
 p("<strong>球表面积推导：</strong>球面面积可由积分或祖暅原理得到 $S=4\\pi R^2$，是同底等高圆柱侧面积 $2\\pi R\\cdot 2R=4\\pi R^2$。"))+
 note(p("表中 $c$ 为底面周长，$h'$ 为斜高，$l$ 为母线长，$S$ 为底面积。"))
)}
]}
]

# ============ 第七章 解析几何 ============
ch7_sections = [
{"name":"7.1 坐标系与参数方程","color":"#0891b2","desc":"极坐标、柱坐标、球坐标与参数方程",
"items":[
{"id":"e7s1-1","name":"极坐标与坐标互化","tags":["def","thm","der"],"brief":"极坐标定义、与直角坐标互化、常见曲线极坐标方程。",
"fig":"polar_coord","figCap":"极坐标系：点 P(ρ,θ)，ρ 为极径，θ 为极角",
"body":wrap(
 defn("极坐标",p("在平面内取定点 $O$（极点），引射线 $Ox$（极轴），选定长度单位和角度正方向（逆时针）。对平面内任一点 $P$，记 $\\rho=|OP|$ 为<strong>极径</strong>，$\\theta=\\angle xOP$ 为<strong>极角</strong>，有序数对 $(\\rho,\\theta)$ 为 $P$ 的<strong>极坐标</strong>。"))+
 thm("极坐标与直角坐标互化",p("极点与原点重合、极轴与 x 轴正半轴重合时：")+
 fml("x=\\rho\\cos\\theta,\\quad y=\\rho\\sin\\theta,\\quad \\rho^2=x^2+y^2,\\quad \\tan\\theta=\\dfrac{y}{x}"))+
 der(p("<strong>互化推导：</strong>由三角函数定义，点 $P$ 在直角坐标系中的坐标 $(x,y)$ 满足 $x=\\rho\\cos\\theta$，$y=\\rho\\sin\\theta$。两边平方相加得 $x^2+y^2=\\rho^2(\\cos^2\\theta+\\sin^2\\theta)=\\rho^2$。两式相除得 $\\dfrac{y}{x}=\\tan\\theta$（$x\\neq 0$）。"))+
 thm("常见曲线极坐标方程",p("① 圆心在极点半径 $r$ 的圆：$\\rho=r$；<br>② 过极点倾角为 $\\alpha$ 的直线：$\\theta=\\alpha$；<br>③ 圆心在 $(a,0)$ 半径 $a$ 的圆：$\\rho=2a\\cos\\theta$。"))+
 der(p("<strong>圆 $\\rho=2a\\cos\\theta$ 推导：</strong>圆心在 $(a,0)$、半径 $a$ 的圆直角坐标方程为 $(x-a)^2+y^2=a^2$，即 $x^2-2ax+y^2=0$。代入 $x=\\rho\\cos\\theta$，$\\rho^2=x^2+y^2$，得 $\\rho^2-2a\\rho\\cos\\theta=0$，即 $\\rho=2a\\cos\\theta$（$\\rho\\neq 0$ 时）。"))
)},
{"id":"e7s1-2","name":"柱坐标与球坐标","tags":["def","thm","der"],"brief":"柱坐标、球坐标与直角坐标的关系。",
"body":wrap(
 defn("柱坐标",p("空间点 $P$ 的柱坐标 $(\\rho,\\theta,z)$，其中 $(\\rho,\\theta)$ 是 $P$ 在 $xy$ 平面上投影的极坐标，$z$ 是 $P$ 的竖坐标。"))+
 thm("柱坐标与直角坐标关系",p("")+
 fml("x=\\rho\\cos\\theta,\\quad y=\\rho\\sin\\theta,\\quad z=z"))+
 defn("球坐标",p("空间点 $P$ 的球坐标 $(r,\\varphi,\\theta)$，其中 $r=|OP|$，$\\varphi$ 是 $OP$ 与 $z$ 轴正方向的夹角（极角），$\\theta$ 是 $OP$ 在 $xy$ 平面投影与 $x$ 轴正方向的夹角（方位角）。"))+
 thm("球坐标与直角坐标关系",p("")+
 fml("x=r\\sin\\varphi\\cos\\theta,\\quad y=r\\sin\\varphi\\sin\\theta,\\quad z=r\\cos\\varphi"))+
 der(p("<strong>球坐标关系推导：</strong>$P$ 在 $xy$ 平面的投影为 $P'$，$|OP'|=r\\sin\\varphi$（$\\varphi$ 为 $OP$ 与 $z$ 轴夹角）。$P'$ 的极坐标为 $(r\\sin\\varphi,\\theta)$，故 $x=|OP'|\\cos\\theta=r\\sin\\varphi\\cos\\theta$，$y=|OP'|\\sin\\theta=r\\sin\\varphi\\sin\\theta$。而 $z=r\\cos\\varphi$（$z$ 方向分量）。"))
)},
{"id":"e7s1-3","name":"参数方程","tags":["def","thm","der"],"brief":"直线、圆、椭圆的参数方程。",
"body":wrap(
 defn("参数方程",p("在平面直角坐标系中，若曲线上任一点坐标 $(x,y)$ 都可表示为某个变量 $t$ 的函数 $\\begin{cases}x=f(t)\\\\y=g(t)\\end{cases}$，则称其为曲线的<strong>参数方程</strong>，$t$ 为参数。"))+
 thm("常见曲线的参数方程",p("① 过 $(x_0,y_0)$、倾角为 $\\alpha$ 的直线：$\\begin{cases}x=x_0+t\\cos\\alpha\\\\y=y_0+t\\sin\\alpha\\end{cases}$（$t$ 为参数，$|t|$ 为到定点距离）；<br>② 圆心 $(a,b)$ 半径 $r$ 的圆：$\\begin{cases}x=a+r\\cos\\theta\\\\y=b+r\\sin\\theta\\end{cases}$；<br>③ 椭圆 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1$：$\\begin{cases}x=a\\cos\\theta\\\\y=b\\sin\\theta\\end{cases}$。"))+
 der(p("<strong>圆参数方程推导：</strong>圆心 $(a,b)$ 半径 $r$ 的圆标准方程 $(x-a)^2+(y-b)^2=r^2$。令 $\\dfrac{x-a}{r}=\\cos\\theta$，$\\dfrac{y-b}{r}=\\sin\\theta$（利用 $\\cos^2\\theta+\\sin^2\\theta=1$），即得 $x=a+r\\cos\\theta$，$y=b+r\\sin\\theta$。")+
 p("<strong>椭圆参数方程推导：</strong>椭圆 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1$，令 $\\dfrac{x}{a}=\\cos\\theta$，$\\dfrac{y}{b}=\\sin\\theta$，满足 $\\cos^2\\theta+\\sin^2\\theta=1$，故 $x=a\\cos\\theta$，$y=b\\sin\\theta$。"))
)}
]},
{"name":"7.2 直线与圆","color":"#0e7490","desc":"直线方程、点到线距离、圆的方程与位置关系",
"items":[
{"id":"e7s2-1","name":"直线方程与两直线关系","tags":["def","thm","der"],"brief":"直线方程5种形式、两直线位置关系、点到线距离。",
"body":wrap(
 defn("直线方程形式",p("① <strong>点斜式</strong>：$y-y_0=k(x-x_0)$；<br>② <strong>斜截式</strong>：$y=kx+b$；<br>③ <strong>两点式</strong>：$\\dfrac{y-y_1}{y_2-y_1}=\\dfrac{x-x_1}{x_2-x_1}$；<br>④ <strong>截距式</strong>：$\\dfrac{x}{a}+\\dfrac{y}{b}=1$；<br>⑤ <strong>一般式</strong>：$Ax+By+C=0$（$A,B$ 不同时为 0）。"))+
 thm("两直线位置关系",p("设 $l_1:y=k_1x+b_1$，$l_2:y=k_2x+b_2$：<br>平行：$k_1=k_2$ 且 $b_1\\neq b_2$；<br>垂直：$k_1k_2=-1$；<br>相交：$k_1\\neq k_2$。"))+
 thm("距离公式",p("点 $P(x_0,y_0)$ 到直线 $Ax+By+C=0$ 的距离：")+
 fml("d = \\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}"))+
 der(p("<strong>点到直线距离推导：</strong>过 $P$ 作直线 $Ax+By+C=0$ 的垂线，垂足为 $Q$。直线法向量为 $\\vec{n}=(A,B)$。取直线上一点 $M(x_1,y_1)$（满足 $Ax_1+By_1+C=0$），则 $d=|\\overrightarrow{PM}\\cdot\\vec{n_0}|=\\dfrac{|A(x_0-x_1)+B(y_0-y_1)|}{\\sqrt{A^2+B^2}}=\\dfrac{|Ax_0+By_0-(Ax_1+By_1)|}{\\sqrt{A^2+B^2}}=\\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}$。"))+
 der(p("<strong>两直线垂直推导：</strong>设 $l_1$ 倾角 $\\alpha_1$，$l_2$ 倾角 $\\alpha_2=\\alpha_1+90°$。$k_2=\\tan(\\alpha_1+90°)=-\\cot\\alpha_1=-\\dfrac{1}{\\tan\\alpha_1}=-\\dfrac{1}{k_1}$，故 $k_1k_2=-1$。"))
)},
{"id":"e7s2-2","name":"圆的方程与直线圆位置关系","tags":["def","thm","der"],"brief":"标准方程、一般方程与直线圆位置关系。",
"body":wrap(
 defn("圆的标准方程",p("圆心为 $(a,b)$，半径为 $r$ 的圆：")+
 fml("(x-a)^2+(y-b)^2 = r^2"))+
 defn("圆的一般方程",p("")+
 fml("x^2+y^2+Dx+Ey+F=0\\quad(D^2+E^2-4F>0)")+
 p("圆心 $\\left(-\\dfrac{D}{2},-\\dfrac{E}{2}\\right)$，半径 $r=\\dfrac{1}{2}\\sqrt{D^2+E^2-4F}$。"))+
 der(p("<strong>一般方程推导：</strong>将标准方程 $(x-a)^2+(y-b)^2=r^2$ 展开：$x^2-2ax+a^2+y^2-2by+b^2-r^2=0$。令 $D=-2a$，$E=-2b$，$F=a^2+b^2-r^2$，得 $x^2+y^2+Dx+Ey+F=0$。$r>0$ 要求 $D^2+E^2-4F>0$。"))+
 thm("直线与圆的位置关系",p("设圆心到直线距离为 $d$，半径为 $r$：<br>$d>r$ 相离；$d=r$ 相切；$d<r$ 相交（弦长 $=2\\sqrt{r^2-d^2}$）。"))+
 der(p("<strong>弦长公式推导：</strong>设弦为 $AB$，圆心 $O$ 到弦距离 $d=|OM|$（$M$ 为弦中点）。由垂径定理 $OM\\perp AB$，在 $Rt\\triangle OMA$ 中，$AM=\\sqrt{OA^2-OM^2}=\\sqrt{r^2-d^2}$，故弦长 $AB=2AM=2\\sqrt{r^2-d^2}$。"))
)},
{"id":"e7s2-3","name":"空间解析几何","tags":["def","thm","der"],"brief":"空间直线方程、平面方程与线面关系。",
"body":wrap(
 defn("空间平面方程",p("平面的一般方程：$Ax+By+Cz+D=0$，其中 $\\vec{n}=(A,B,C)$ 为法向量。过点 $(x_0,y_0,z_0)$ 且法向量为 $(A,B,C)$ 的平面：$A(x-x_0)+B(y-y_0)+C(z-z_0)=0$。"))+
 defn("空间直线方程",p("过点 $P_0(x_0,y_0,z_0)$，方向向量 $\\vec{s}=(m,n,p)$ 的直线：<br><strong>对称式</strong>（点向式）：$\\dfrac{x-x_0}{m}=\\dfrac{y-y_0}{n}=\\dfrac{z-z_0}{p}$；<br><strong>参数式</strong>：$\\begin{cases}x=x_0+mt\\\\y=y_0+nt\\\\z=z_0+pt\\end{cases}$。"))+
 thm("空间两点距离",p("$P_1(x_1,y_1,z_1)$，$P_2(x_2,y_2,z_2)$：")+
 fml("|P_1P_2| = \\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}"))+
 der(p("<strong>空间两点距离推导：</strong>过 $P_1,P_2$ 分别作平行于坐标轴的平面，构成长方体，$P_1P_2$ 为对角线。由长方体对角线公式 $|P_1P_2|^2=(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2$。")+
 p("<strong>线面角推导：</strong>直线方向向量 $\\vec{s}$ 与平面法向量 $\\vec{n}$ 的夹角为 $\\beta$，线面角 $\\theta$ 与 $\\beta$ 互余（$\\theta+\\beta=90°$），故 $\\sin\\theta=|\\cos\\beta|=\\dfrac{|\\vec{s}\\cdot\\vec{n}|}{|\\vec{s}||\\vec{n}|}$。"))+
 note(p("两平面夹角等于其法向量夹角或其补角（取锐角）；两直线夹角等于其方向向量夹角或其补角（取锐角）。"))
)}
]},
{"name":"7.3 圆锥曲线","color":"#155e75","desc":"椭圆、双曲线、抛物线的定义与性质",
"items":[
{"id":"e7s3-1","name":"椭圆","tags":["def","thm","der"],"brief":"椭圆定义、标准方程推导、离心率。",
"fig":"conic","figCap":"椭圆 x²/a²+y²/b²=1，两焦点 F1, F2",
"body":wrap(
 defn("椭圆定义",p("平面内与两个定点 $F_1,F_2$ 的距离之和等于常数 $2a$（$2a>|F_1F_2|$）的点的轨迹。两定点称为<strong>焦点</strong>，$|F_1F_2|=2c$。"))+
 thm("标准方程",p("焦点在 $x$ 轴上：")+
 fml("\\dfrac{x^2}{a^2} + \\dfrac{y^2}{b^2} = 1\\quad(a>b>0,\\ c^2=a^2-b^2)"))+
 der(p("<strong>标准方程推导：</strong>设 $P(x,y)$，$F_1(-c,0)$，$F_2(c,0)$，$|PF_1|+|PF_2|=2a$，即 $\\sqrt{(x+c)^2+y^2}+\\sqrt{(x-c)^2+y^2}=2a$。移项得 $\\sqrt{(x+c)^2+y^2}=2a-\\sqrt{(x-c)^2+y^2}$，两边平方：$(x+c)^2+y^2=4a^2-4a\\sqrt{(x-c)^2+y^2}+(x-c)^2+y^2$。")+
 p("化简：$4cx=4a^2-4a\\sqrt{(x-c)^2+y^2}$，即 $a\\sqrt{(x-c)^2+y^2}=a^2-cx$。再平方：$a^2[(x-c)^2+y^2]=(a^2-cx)^2$，展开整理得 $(a^2-c^2)x^2+a^2y^2=a^2(a^2-c^2)$。令 $b^2=a^2-c^2$，两边除以 $a^2b^2$ 得 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1$。"))+
 thm("离心率",p("$e=\\dfrac{c}{a}\\in(0,1)$，$e$ 越接近 0 椭圆越圆，越接近 1 越扁。"))
)},
{"id":"e7s3-2","name":"双曲线","tags":["def","thm","der"],"brief":"双曲线定义、标准方程、渐近线与离心率。",
"body":wrap(
 defn("双曲线定义",p("平面内与两个定点 $F_1,F_2$ 的距离之差的绝对值等于常数 $2a$（$0<2a<|F_1F_2|$）的点的轨迹。"))+
 thm("标准方程",p("焦点在 $x$ 轴上：")+
 fml("\\dfrac{x^2}{a^2} - \\dfrac{y^2}{b^2} = 1\\quad(c^2=a^2+b^2)"))+
 der(p("<strong>标准方程推导：</strong>$||PF_1|-|PF_2||=2a$，即 $|PF_1|-|PF_2|=\\pm 2a$。与椭圆推导类似，移项平方、再平方，最终得 $(c^2-a^2)x^2-a^2y^2=a^2(c^2-a^2)$。令 $b^2=c^2-a^2$，两边除以 $a^2b^2$ 得 $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1$。"))+
 thm("渐近线与离心率",p("渐近线：$y=\\pm\\dfrac{b}{a}x$；离心率 $e=\\dfrac{c}{a}>1$。"))+
 der(p("<strong>渐近线推导：</strong>由 $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1$ 得 $y=\\pm\\dfrac{b}{a}x\\sqrt{1-\\dfrac{a^2}{x^2}}$。当 $x\\to\\infty$ 时 $\\sqrt{1-\\dfrac{a^2}{x^2}}\\to 1$，故 $y\\to\\pm\\dfrac{b}{a}x$，即渐近线为 $y=\\pm\\dfrac{b}{a}x$。"))+
 note(p("等轴双曲线 $a=b$，渐近线为 $y=\\pm x$，离心率 $e=\\sqrt{2}$。"))
)},
{"id":"e7s3-3","name":"抛物线","tags":["def","thm","der"],"brief":"抛物线定义、标准方程与焦点准线。",
"fig":"parabola","figCap":"抛物线 y²=2px，焦点 F(p/2,0)，准线 x=-p/2",
"body":wrap(
 defn("抛物线定义",p("平面内与一个定点 $F$ 和一条定直线 $l$（$F\\notin l$）距离相等的点的轨迹。定点 $F$ 为<strong>焦点</strong>，定直线 $l$ 为<strong>准线</strong>。"))+
 thm("标准方程",p("开口向右（$p>0$）：")+
 fml("y^2 = 2px,\\quad \\text{焦点 } F\\left(\\dfrac{p}{2},0\\right),\\quad \\text{准线 } x=-\\dfrac{p}{2}"))+
 der(p("<strong>标准方程推导：</strong>设 $F\\left(\\dfrac{p}{2},0\\right)$，准线 $x=-\\dfrac{p}{2}$，$P(x,y)$。由定义 $|PF|=d$（$P$ 到准线距离）：$\\sqrt{\\left(x-\\dfrac{p}{2}\\right)^2+y^2}=\\left|x+\\dfrac{p}{2}\\right|$。两边平方：$\\left(x-\\dfrac{p}{2}\\right)^2+y^2=\\left(x+\\dfrac{p}{2}\\right)^2$，展开得 $x^2-px+\\dfrac{p^2}{4}+y^2=x^2+px+\\dfrac{p^2}{4}$，化简得 $y^2=2px$。"))+
 note(p("离心率 $e=1$。抛物线四种开口方向：$y^2=2px$（右）、$y^2=-2px$（左）、$x^2=2py$（上）、$x^2=-2py$（下）。焦点到准线距离均为 $p$。"))
)}
]}
]

# ============ 第八章 概率统计 ============
ch8_sections = [
{"name":"8.1 排列组合与二项式定理","color":"#059669","desc":"两个原理、排列组合与二项式定理",
"items":[
{"id":"e8s1-1","name":"加法原理与乘法原理","tags":["def","thm","der","exa"],"brief":"分类加法与分步乘法计数原理。",
"body":wrap(
 defn("加法原理（分类计数）",p("完成一件事有 $n$ 类办法，第 $i$ 类有 $m_i$ 种方法，则总方法数 $N=m_1+m_2+\\cdots+m_n$。各类办法相互独立。"))+
 defn("乘法原理（分步计数）",p("完成一件事分 $n$ 个步骤，第 $i$ 步有 $m_i$ 种方法，则总方法数 $N=m_1\\times m_2\\times\\cdots\\times m_n$。各步骤相互依存。"))+
 der(p("<strong>原理本质：</strong>加法原理对应「<strong>或</strong>」关系（选第一类或第二类……），用加法；乘法原理对应「<strong>且</strong>」关系（第一步且第二步……），用乘法。关键区分：分类之间互斥，分步之间连续。"))+
 exa(p("<strong>例：</strong>从 3 种主食和 2 种饮料中选一份主食和一份饮料，共 $3\\times2=6$ 种搭配（乘法原理）。若只需选一种（主食或饮料），则 $3+2=5$ 种（加法原理）。"))
)},
{"id":"e8s1-2","name":"排列数与组合数","tags":["def","thm","der"],"brief":"A(n,m) 与 C(n,m) 的定义、公式与性质。",
"body":wrap(
 defn("排列",p("从 $n$ 个不同元素中取出 $m$（$m\\le n$）个元素，按照一定顺序排成一列，称为从 $n$ 个中取 $m$ 个的一个排列。排列数记为 $A_n^m$。"))+
 thm("排列数公式",p("")+
 fml("A_n^m = n(n-1)(n-2)\\cdots(n-m+1) = \\dfrac{n!}{(n-m)!}"))+
 der(p("<strong>排列数推导：</strong>第 1 个位置有 $n$ 种选法，第 2 个位置有 $n-1$ 种，……，第 $m$ 个位置有 $n-m+1$ 种。由乘法原理，$A_n^m=n(n-1)\\cdots(n-m+1)$。利用阶乘 $n!=n(n-1)\\cdots1$，可写为 $\\dfrac{n!}{(n-m)!}$。"))+
 defn("组合",p("从 $n$ 个不同元素中取出 $m$ 个元素并成一组，不考虑顺序，称为一个组合。组合数记为 $C_n^m$。"))+
 thm("组合数公式",p("")+
 fml("C_n^m = \\dfrac{A_n^m}{m!} = \\dfrac{n!}{m!(n-m)!}"))+
 der(p("<strong>组合数推导：</strong>排列 $A_n^m$ 可看作先选 $m$ 个元素（组合 $C_n^m$），再对这 $m$ 个元素全排列（$m!$ 种）。由乘法原理 $A_n^m=C_n^m\\cdot m!$，故 $C_n^m=\\dfrac{A_n^m}{m!}$。"))+
 thm("组合恒等式",p("① 对称性：$C_n^m=C_n^{n-m}$；② 帕斯卡恒等式：$C_n^m=C_{n-1}^m+C_{n-1}^{m-1}$。"))
)},
{"id":"e8s1-3","name":"二项式定理","tags":["thm","der","app"],"brief":"(a+b)^n 的展开公式与通项。",
"body":wrap(
 thm("二项式定理",p("对正整数 $n$：")+
 fml("(a+b)^n = \\sum_{k=0}^n \\binom{n}{k} a^{n-k}b^k = C_n^0a^n+C_n^1a^{n-1}b+\\cdots+C_n^nb^n"))+
 thm("通项公式",p("展开式第 $k+1$ 项为：")+
 fml("T_{k+1} = \\binom{n}{k} a^{n-k}b^k"))+
 der(p("<strong>推导（组合意义法）：</strong>$(a+b)^n$ 是 $n$ 个 $(a+b)$ 相乘。展开式中 $a^{n-k}b^k$ 项的系数，等于从 $n$ 个括号中选 $k$ 个取 $b$（其余取 $a$）的选法数，即 $C_n^k$。故 $(a+b)^n=\\sum_{k=0}^n C_n^k a^{n-k}b^k$。")+
 p("<strong>系数和：</strong>令 $a=b=1$，得 $2^n=\\sum_{k=0}^n C_n^k$；令 $a=1,b=-1$，得 $0=\\sum_{k=0}^n (-1)^k C_n^k$，即奇数项系数和等于偶数项系数和 $=2^{n-1}$。"))+
 app(p("<strong>应用：</strong>求展开式特定项、系数、系数最大值，以及证明组合恒等式。例如 $(1+x)^n$ 展开式中 $x^k$ 的系数为 $C_n^k$。"))
)}
]},
{"name":"8.2 随机事件与概率","color":"#10b981","desc":"古典概型、几何概型与概率公式",
"items":[
{"id":"e8s2-1","name":"古典概型与几何概型","tags":["def","thm","der","exa"],"brief":"等可能事件概率与几何概率。",
"fig":"probability","figCap":"古典概型：P(A)=m/n，m 为有利事件数，n 为基本事件总数",
"body":wrap(
 defn("古典概型",p("具有以下两个特征的随机试验：① 所有可能结果只有有限个；② 每个结果出现的可能性相等。事件 $A$ 的概率：")+
 fml("P(A) = \\dfrac{m}{n}")+
 p("$n$ 为基本事件总数，$m$ 为 $A$ 包含的基本事件数。"))+
 defn("几何概型",p("试验结果无限多但每个结果等可能，概率与区域长度（面积、体积）成正比：")+
 fml("P(A) = \\dfrac{\\text{构成事件 A 的区域测度}}{\\text{试验全部结果区域测度}}"))+
 der(p("<strong>古典概型等可能性推导：</strong>由于 $n$ 个基本事件等可能，每个基本事件概率为 $\\dfrac{1}{n}$。事件 $A$ 包含 $m$ 个基本事件，且这些事件互斥，由加法公式 $P(A)=m\\times\\dfrac{1}{n}=\\dfrac{m}{n}$。"))+
 exa(p("<strong>古典例：</strong>掷一枚均匀骰子，求点数为偶数的概率。基本事件共 6 个（1~6 点），偶数点有 2,4,6 共 3 个，故 $P=\\dfrac{3}{6}=\\dfrac{1}{2}$。")+
 p("<strong>几何例：</strong>在区间 $[0,1]$ 上任取一数 $x$，求 $x<0.3$ 的概率。$P=\\dfrac{0.3}{1}=0.3$。"))
)},
{"id":"e8s2-2","name":"概率的基本公式","tags":["thm","der"],"brief":"互斥加法、独立乘法、条件概率、全概率、贝叶斯。",
"body":wrap(
 thm("互斥事件加法",p("若 $A,B$ 互斥（$A\\cap B=\\varnothing$），则：")+
 fml("P(A\\cup B) = P(A)+P(B)")+
 p("一般情况（容斥）：$P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$。"))+
 thm("独立事件乘法",p("若 $A,B$ 相互独立（$P(A|B)=P(A)$），则：")+
 fml("P(A\\cap B) = P(A)\\cdot P(B)"))+
 defn("条件概率",p("在事件 $B$ 已发生的条件下，事件 $A$ 发生的概率：")+
 fml("P(A|B) = \\dfrac{P(A\\cap B)}{P(B)}\\quad(P(B)>0)"))+
 der(p("<strong>条件概率推导：</strong>在 $B$ 已发生的条件下，样本空间缩减为 $B$。$A$ 在缩减空间中发生的概率等于 $A\\cap B$ 占 $B$ 的比例，即 $\\dfrac{P(A\\cap B)}{P(B)}$。")+
 p("<strong>独立与乘法推导：</strong>$A,B$ 独立意味着 $B$ 的发生不影响 $A$ 的概率，即 $P(A|B)=P(A)$。代入条件概率公式：$\\dfrac{P(A\\cap B)}{P(B)}=P(A)$，故 $P(A\\cap B)=P(A)P(B)$。"))+
 thm("全概率公式与贝叶斯公式",p("设 $B_1,B_2,\\dots,B_n$ 为样本空间的一个分割（互斥且并为全集），则：")+
 fml("P(A) = \\sum_{i=1}^n P(B_i)P(A|B_i)")+
 fml("P(B_i|A) = \\dfrac{P(B_i)P(A|B_i)}{\\sum_{j=1}^n P(B_j)P(A|B_j)}"))
)}
]},
{"name":"8.3 随机变量与统计","color":"#34d399","desc":"分布列、期望方差、二项分布、正态分布与统计",
"items":[
{"id":"e8s3-1","name":"离散型随机变量及其分布","tags":["def","thm","der"],"brief":"分布列、期望、方差与二项分布。",
"body":wrap(
 defn("分布列",p("设离散型随机变量 $X$ 的可能取值为 $x_1,x_2,\\dots,x_n$，$P(X=x_i)=p_i$，则 $\\begin{pmatrix}x_1&x_2&\\cdots&x_n\\\\ p_1&p_2&\\cdots&p_n\\end{pmatrix}$ 为 $X$ 的分布列，满足 $p_i\\ge 0$，$\\sum p_i=1$。"))+
 defn("数学期望",p("")+
 fml("E(X) = \\sum_{i=1}^n x_i p_i"))+
 defn("方差",p("")+
 fml("D(X) = \\sum_{i=1}^n [x_i-E(X)]^2 p_i = E(X^2)-[E(X)]^2"))+
 der(p("<strong>方差公式推导：</strong>$D(X)=E[(X-E(X))^2]=E[X^2-2XE(X)+(E(X))^2]=E(X^2)-2E(X)\\cdot E(X)+[E(X)]^2=E(X^2)-[E(X)]^2$。这里利用期望的线性性质 $E(aX+b)=aE(X)+b$。"))+
 defn("二项分布",p("在 $n$ 次独立重复试验中，事件 $A$ 每次发生概率为 $p$，则 $A$ 发生次数 $X\\sim B(n,p)$：")+
 fml("P(X=k) = \\binom{n}{k} p^k (1-p)^{n-k},\\quad k=0,1,\\dots,n"))+
 thm("二项分布的期望与方差",p("")+
 fml("E(X) = np,\\quad D(X) = np(1-p)"))+
 der(p("<strong>二项分布期望推导：</strong>$X$ 可分解为 $n$ 个独立的 0-1 变量 $X_i$（第 $i$ 次试验 $A$ 发生则 $X_i=1$，否则 0），$X=X_1+\\cdots+X_n$。每个 $E(X_i)=p$，由期望可加性 $E(X)=np$。方差 $D(X_i)=p(1-p)$，独立可加得 $D(X)=np(1-p)$。"))
)},
{"id":"e8s3-2","name":"正态分布","tags":["def","thm","der"],"brief":"正态分布密度、性质与 3σ 原则。",
"body":wrap(
 defn("正态分布",p("若随机变量 $X$ 的概率密度为：")+
 fml("f(x) = \\dfrac{1}{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}")+
 p("则 $X\\sim N(\\mu,\\sigma^2)$，其中 $\\mu$ 为期望，$\\sigma^2$ 为方差。图像关于 $x=\\mu$ 对称，呈钟形曲线。"))+
 der(p("<strong>密度函数归一性：</strong>$\\int_{-\\infty}^{+\\infty}f(x)dx=1$。令 $u=\\dfrac{x-\\mu}{\\sigma}$，则 $\\int_{-\\infty}^{+\\infty}\\dfrac{1}{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}dx=\\dfrac{1}{\\sqrt{2\\pi}}\\int_{-\\infty}^{+\\infty}e^{-\\frac{u^2}{2}}du=1$（高斯积分 $\\int_{-\\infty}^{+\\infty}e^{-u^2/2}du=\\sqrt{2\\pi}$）。")+
 p("<strong>对称性推导：</strong>$f(\\mu+t)=\\dfrac{1}{\\sqrt{2\\pi}\\sigma}e^{-\\frac{t^2}{2\\sigma^2}}=f(\\mu-t)$，故图像关于 $x=\\mu$ 对称，$P(X<\\mu)=P(X>\\mu)=0.5$。"))+
 thm("3σ 原则",p("正态分布中：$P(\\mu-\\sigma<X<\\mu+\\sigma)\\approx 68.3\\%$，$P(\\mu-2\\sigma<X<\\mu+2\\sigma)\\approx 95.4\\%$，$P(\\mu-3\\sigma<X<\\mu+3\\sigma)\\approx 99.7\\%$。"))+
 note(p("标准正态分布 $N(0,1)$：若 $X\\sim N(\\mu,\\sigma^2)$，则 $Z=\\dfrac{X-\\mu}{\\sigma}\\sim N(0,1)$。"))
)},
{"id":"e8s3-3","name":"统计：抽样、频率分布与数字特征","tags":["def","thm","der"],"brief":"抽样方法、频率分布、样本均值方差与线性回归。",
"body":wrap(
 defn("抽样方法",p("① <strong>简单随机抽样</strong>：从总体中逐个抽取，每个个体被抽到概率相等；<br>② <strong>分层抽样</strong>：将总体分成若干层，按比例从各层抽取；<br>③ <strong>系统抽样</strong>：将总体均分后按规则抽取。"))+
 defn("频率分布直方图",p("用矩形面积表示各区间频率。矩形面积 = 频率 = 频率/组距 × 组距。所有矩形面积之和为 1。"))+
 note(p("频率分布直方图中，<strong>众数</strong>为最高矩形底边中点；<strong>中位数</strong>为使左右面积各为 0.5 的点；<strong>平均数</strong>为各矩形面积乘以对应区间中点之和。"))+
 defn("样本均值与方差",p("样本 $x_1,x_2,\\dots,x_n$：")+
 fml("\\bar{x} = \\dfrac{1}{n}\\sum_{i=1}^n x_i,\\quad s^2 = \\dfrac{1}{n}\\sum_{i=1}^n (x_i-\\bar{x})^2"))+
 defn("线性回归方程",p("两个变量 $x,y$ 的线性回归直线 $\\hat{y}=bx+a$，其中：")+
 fml("b = \\dfrac{\\sum_{i=1}^n (x_i-\\bar{x})(y_i-\\bar{y})}{\\sum_{i=1}^n (x_i-\\bar{x})^2},\\quad a = \\bar{y}-b\\bar{x}"))+
 der(p("<strong>回归系数推导（最小二乘法）：</strong>目标最小化 $Q=\\sum_{i=1}^n(y_i-bx_i-a)^2$。对 $a$ 求偏导令其为 0：$\\dfrac{\\partial Q}{\\partial a}=-2\\sum(y_i-bx_i-a)=0$，得 $a=\\bar{y}-b\\bar{x}$。对 $b$ 求偏导为 0，代入 $a$ 化简得 $b=\\dfrac{\\sum(x_i-\\bar{x})(y_i-\\bar{y})}{\\sum(x_i-\\bar{x})^2}$。"))+
 note(p("回归直线过样本中心点 $(\\bar{x},\\bar{y})$。相关系数 $r$ 的绝对值越接近 1，线性相关性越强。"))
)}
]}
]

CHAPTERS = [
{"id":"ch1","num":"第一章","title":"集合与逻辑","en":"SETS & LOGIC","desc":"集合的概念与运算、命题、充要条件，是数学严谨推理的语言基础。","sections":ch1_sections},
{"id":"ch2","num":"第二章","title":"代数","en":"ALGEBRA","desc":"多项式与因式分解、方程与不等式、三角函数补充，是运算变形的基本工具。","sections":ch2_sections},
{"id":"ch3","num":"第三章","title":"函数","en":"FUNCTIONS","desc":"函数的概念与性质、基本初等函数（指数、对数、幂、三角）、反三角函数。","sections":ch3_sections},
{"id":"ch4","num":"第四章","title":"数列","en":"SEQUENCES","desc":"等差数列、等比数列的通项与求和，以及数列求和的通用方法。","sections":ch4_sections},
{"id":"ch5","num":"第五章","title":"平面几何","en":"PLANE GEOMETRY","desc":"三角形、圆的性质与定理，正弦定理、余弦定理与圆幂定理。","sections":ch5_sections},
{"id":"ch6","num":"第六章","title":"立体几何","en":"SOLID GEOMETRY","desc":"空间几何体的表面积与体积，线面、面面的平行与垂直关系。","sections":ch6_sections},
{"id":"ch7","num":"第七章","title":"解析几何","en":"ANALYTIC GEOMETRY","desc":"坐标系、直线与圆、圆锥曲线（椭圆、双曲线、抛物线）及空间解析几何。","sections":ch7_sections},
{"id":"ch8","num":"第八章","title":"概率统计","en":"PROBABILITY & STATISTICS","desc":"排列组合、古典概型、概率公式、随机变量分布与统计推断。","sections":ch8_sections},
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