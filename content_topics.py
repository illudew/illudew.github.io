# -*- coding: utf-8 -*-
"""各学科的主题定义。每个主题含 name/formula/explain/deriv/ex/app/note。"""
from content_bank import T

# ===================== 初等数学 elementary-math =====================
ELEMENTARY_MATH = [
  # 第一章 三角函数
  {"ch":"第一章","title":"三角函数","en":"TRIGONOMETRY","sub":"角的度量与恒等式","sections":[
    {"name":"1.1 角的度量","color":"#2563eb","topics":[
      {"name":"弧度制","formula":"180^\\circ=\\pi\\text{ rad}","explain":"半径为r的圆中弧长等于半径的圆心角为1弧度。","deriv":"由定义直接得弧长公式 l=rθ。","ex":"将60°化为弧度：60°=π/3 rad。","app":"在微积分与物理中统一使用弧度制。","note":"角度制与弧度制不可混用。"},
      {"name":"扇形面积","formula":"S=\\frac12 r^2\\theta","explain":"扇形面积等于弧长与半径乘积的一半。","deriv":"S=½rl=½r(rθ)=½r²θ。","ex":"半径2，圆心角π/3的扇形面积=½×4×π/3=2π/3。","app":"计算圆的部分面积。","note":"θ须用弧度。"},
      {"name":"三角函数定义","formula":"\\sin\\theta=y/r,\\cos\\theta=x/r","explain":"在单位圆上，角θ终边与圆交于(x,y)，sinθ=y，cosθ=x。","deriv":"由直角三角形对边比邻边定义推广到任意角。","ex":"θ=π/2时，sin=1,cos=0。","app":"用于描述周期现象。","note":"sin²θ+cos²θ=1恒成立。"},
      {"name":"诱导公式","formula":"\\sin(\\pi-\\theta)=\\sin\\theta","explain":"奇变偶不变，符号看象限。","deriv":"由单位圆对称性得到。","ex":"sin(5π/6)=sin(π-π/6)=sin(π/6)=1/2。","app":"将大角化为小角求值。","note":"π/2奇数倍时函数名变化。"},
      {"name":"同角恒等式","formula":"\\sin^2\\theta+\\cos^2\\theta=1","explain":"由单位圆x²+y²=1直接得到。","deriv":"x=cosθ,y=sinθ代入x²+y²=1。","ex":"已知sinθ=3/5，θ在第二象限，求cosθ=-4/5。","app":"化简三角表达式。","note":"开方时注意象限符号。"},
      {"name":"商数与倒数","formula":"\\tan\\theta=\\sin\\theta/\\cos\\theta","explain":"正切=正弦/余弦，余割=1/正弦。","deriv":"由定义直接相除。","ex":"已知sin=3/5,cos=-4/5，则tan=-3/4。","app":"用一个函数表示其他函数。","note":"tanθ在cosθ=0时无定义。"},
    ]},
    {"name":"1.2 和差角与倍角","color":"#7c3aed","topics":[
      {"name":"和差角正弦","formula":"\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta","explain":"两角和差的正弦展开。","deriv":"由余弦差角公式结合诱导公式推出。","ex":"sin75°=sin(45°+30°)=(√6+√2)/4。","app":"化简与求值。","note":"注意±号对应。"},
      {"name":"和差角余弦","formula":"\\cos(\\alpha\\pm\\beta)=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta","explain":"余弦和角中间为减号。","deriv":"利用单位圆上两点距离公式证明。","ex":"cos15°=cos(45°-30°)=(√6+√2)/4。","app":"与正弦和差角配合使用。","note":"符号与正弦相反。"},
      {"name":"和差角正切","formula":"\\tan(\\alpha\\pm\\beta)=\\frac{\\tan\\alpha\\pm\\tan\\beta}{1\\mp\\tan\\alpha\\tan\\beta}","explain":"由正余弦和差角相除得到。","deriv":"tan(α+β)=sin(α+β)/cos(α+β)，分子分母同除以cosαcosβ。","ex":"tan75°=tan(45°+30°)=2+√3。","app":"求两直线夹角。","note":"分母为0时角为90°。"},
      {"name":"二倍角公式","formula":"\\sin2\\theta=2\\sin\\theta\\cos\\theta","explain":"令α=β=θ代入和角公式。","deriv":"cos2θ=cos²θ-sin²θ=2cos²θ-1=1-2sin²θ。","ex":"sin60°=2sin30°cos30°=2×½×(√3/2)=√3/2。","app":"降次与化简。","note":"是和角公式特例。"},
      {"name":"半角公式","formula":"\\sin\\frac{\\theta}{2}=\\pm\\sqrt{\\frac{1-\\cos\\theta}{2}}","explain":"由二倍角余弦变形得到。","deriv":"cosθ=1-2sin²(θ/2)，解出sin(θ/2)。","ex":"sin(π/8)=√[(1-cosπ/4)/2]=√(2-√2)/2。","app":"半角的三角函数值。","note":"符号由θ/2所在象限决定。"},
      {"name":"万能公式","formula":"\\sin\\theta=\\frac{2t}{1+t^2},t=\\tan\\frac{\\theta}{2}","explain":"将三角函数统一化为t的有理函数。","deriv":"用半角公式代入化简。","ex":"求∫dθ/(1+sinθ)，令t=tan(θ/2)化为有理积分。","app":"三角积分万能代换。","note":"又称魏尔斯特拉斯代换。"},
      {"name":"和差化积","formula":"\\sin\\alpha+\\sin\\beta=2\\sin\\frac{\\alpha+\\beta}{2}\\cos\\frac{\\alpha-\\beta}{2}","explain":"将和化为积的形式。","deriv":"令α=A+B,β=A-B代入和差角公式相加。","ex":"sin50°+sin10°=2sin30°cos20°=cos20°。","app":"便于分析和提取公因子。","note":"与积化和差互为逆运算。"},
      {"name":"积化和差","formula":"\\sin\\alpha\\cos\\beta=\\frac12[\\sin(\\alpha+\\beta)+\\sin(\\alpha-\\beta)]","explain":"将积化为和的形式。","deriv":"由和差角正弦公式相加得到。","ex":"sin40°cos20°=½(sin60°+sin20°)。","app":"积的积分与化简。","note":"系数为1/2。"},
    ]},
    {"name":"1.3 反三角函数","color":"#0f766e","topics":[
      {"name":"反正弦","formula":"y=\\arcsin x, x\\in[-1,1], y\\in[-\\pi/2,\\pi/2]","explain":"正弦在主值区间的反函数。","deriv":"限制sinx在[-π/2,π/2]单调。","ex":"arcsin(√3/2)=π/3。","app":"解三角方程。","note":"值域是主值区间。"},
      {"name":"反余弦","formula":"y=\\arccos x, y\\in[0,\\pi]","explain":"余弦在[0,π]上的反函数，单调递减。","deriv":"限制cosx在[0,π]单调。","ex":"arccos(-1/2)=2π/3。","app":"与反正弦互补。","note":"arcsinx+arccosx=π/2。"},
      {"name":"反正切","formula":"y=\\arctan x, y\\in(-\\pi/2,\\pi/2)","explain":"正切的反函数，定义域R。","deriv":"限制tanx在(-π/2,π/2)单调。","ex":"arctan1=π/4。","app":"表示直线倾斜角。","note":"有水平渐近线y=±π/2。"},
      {"name":"反三角恒等式","formula":"\\arcsin x+\\arccos x=\\frac{\\pi}{2}","explain":"反三角函数之间的恒等关系。","deriv":"令α=arcsinx,β=arccosx，则sinα=cosβ=x，故α+β=π/2。","ex":"arcsin0.5+arccos0.5=π/6+π/3=π/2。","app":"化简反三角表达式。","note":"仅对|x|≤1成立。"},
      {"name":"三角方程","formula":"\\sin x=a \\Rightarrow x=k\\pi+(-1)^k\\arcsin a","explain":"简单三角方程的通解。","deriv":"由正弦周期性和诱导公式得到。","ex":"sinx=1/2的解：x=kπ+(-1)^k·π/6。","app":"解含有三角函数的方程。","note":"需验证|a|≤1。"},
    ]},
  ]},
  # 第二章 向量与极坐标
  {"ch":"第二章","title":"向量与极坐标","en":"VECTORS & POLAR","sub":"向量运算与坐标变换","sections":[
    {"name":"2.1 向量代数","color":"#2563eb","topics":[
      {"name":"向量线性运算","formula":"\\lambda\\boldsymbol{a}=(\\lambda a_1,\\lambda a_2,\\lambda a_3)","explain":"数乘缩放向量长度，方向由λ符号决定。","deriv":"按分量定义。","ex":"2(1,2,3)=(2,4,6)。","app":"向量的缩放与共线。","note":"|λa|=|λ||a|。"},
      {"name":"点积","formula":"\\boldsymbol{a}\\cdot\\boldsymbol{b}=a_1b_1+a_2b_2+a_3b_3=|a||b|\\cos\\theta","explain":"点积结果为标量，反映投影。","deriv":"由余弦定理推出几何意义。","ex":"(1,2)·(3,4)=3+8=11。","app":"判断垂直（点积为0）、求夹角。","note":"点积满足交换律与分配律。"},
      {"name":"叉乘","formula":"\\boldsymbol{a}\\times\\boldsymbol{b}=(a_2b_3-a_3b_2,a_3b_1-a_1b_3,a_1b_2-a_2b_1)","explain":"叉乘结果为向量，垂直于a,b，方向右手定则。","deriv":"由行列式定义。","ex":"|a×b|=|a||b|sinθ。","app":"求法向量、面积、判断平行。","note":"a×b=-(b×a)。"},
      {"name":"混合积","formula":"(\\boldsymbol{a}\\times\\boldsymbol{b})\\cdot\\boldsymbol{c}","explain":"混合积的绝对值等于平行六面体体积。","deriv":"由叉乘和点积定义。","ex":"用于判断三向量共面（混合积为0）。","app":"求体积、判断共面。","note":"轮换对称。"},
      {"name":"向量夹角","formula":"\\cos\\theta=\\frac{\\boldsymbol{a}\\cdot\\boldsymbol{b}}{|a||b|}","explain":"由点积定义反解夹角余弦。","deriv":"点积公式变形。","ex":"a=(1,0),b=(0,1)，夹角90°。","app":"计算两向量夹角。","note":"θ∈[0,π]。"},
      {"name":"向量投影","formula":"\\text{proj}_{\\boldsymbol{b}}\\boldsymbol{a}=\\frac{\\boldsymbol{a}\\cdot\\boldsymbol{b}}{|b|^2}\\boldsymbol{b}","explain":"a在b方向上的投影向量。","deriv":"由点积几何意义得到。","ex":"a=(3,4)在x轴上投影为(3,0)。","app":"力的分解、坐标变换。","note":"投影是向量。"},
    ]},
    {"name":"2.2 极坐标","color":"#7c3aed","topics":[
      {"name":"极坐标定义","formula":"x=r\\cos\\theta,\\ y=r\\sin\\theta","explain":"用(r,θ)表示平面点。","deriv":"由直角三角形边角关系。","ex":"(r,θ)=(2,π/3)对应直角坐标(1,√3)。","app":"描述圆形、螺旋形图形。","note":"r≥0，θ为极角。"},
      {"name":"极直互化","formula":"r=\\sqrt{x^2+y^2},\\ \\theta=\\arctan\\frac{y}{x}","explain":"由直角坐标求极坐标。","deriv":"勾股定理与反正切。","ex":"直角(1,1)的极坐标为(√2,π/4)。","app":"坐标系转换。","note":"注意θ的象限。"},
      {"name":"极坐标方程","formula":"r=a(1-\\cos\\theta)","explain":"心形线的极坐标方程。","deriv":"由几何定义推出。","ex":"r=2(1-cosθ)是心形线。","app":"描述对称图形。","note":"极坐标方程常比直角坐标简洁。"},
      {"name":"极坐标面积","formula":"S=\\frac12\\int_\\alpha^\\beta r^2(\\theta)d\\theta","explain":"极坐标下曲边扇形面积。","deriv":"将扇形微元积分。","ex":"圆r=a的面积=½∫₀²πa²dθ=πa²。","app":"求极坐标图形面积。","note":"注意积分区间。"},
    ]},
  ]},
  # 第三章 数列
  {"ch":"第三章","title":"数列","en":"SEQUENCES","sub":"等差等比与求和","sections":[
    {"name":"3.1 等差数列","color":"#0f766e","topics":[
      {"name":"等差数列通项","formula":"a_n=a_1+(n-1)d","explain":"公差为d的等差数列通项。","deriv":"每一项比前一项多d。","ex":"1,4,7,10,...的aₙ=1+3(n-1)=3n-2。","app":"求数列任意项。","note":"d为公差。"},
      {"name":"等差数列求和","formula":"S_n=\\frac{n(a_1+a_n)}{2}=na_1+\\frac{n(n-1)}{2}d","explain":"倒序相加法求和。","deriv":"S=a₁+a₂+...+aₙ与倒序相加。","ex":"1+2+...+100=5050。","app":"连续整数求和。","note":"高斯小时候的发现。"},
      {"name":"等差中项","formula":"A=\\frac{a+b}{2}","explain":"a,b的等差中项即算术平均。","deriv":"由a,A,b成等差得2A=a+b。","ex":"3和7的等差中项为5。","app":"插入等差项。","note":"唯一。"},
    ]},
    {"name":"3.2 等比数列","color":"#c2410c","topics":[
      {"name":"等比数列通项","formula":"a_n=a_1q^{n-1}","explain":"公比为q的等比数列。","deriv":"每一项是前一项的q倍。","ex":"2,6,18,...的aₙ=2×3ⁿ⁻¹。","app":"求数列任意项。","note":"q≠0。"},
      {"name":"等比数列求和","formula":"S_n=a_1\\frac{1-q^n}{1-q}","explain":"错位相减法求和。","deriv":"qS-S=a₁qⁿ-a₁。","ex":"1+2+4+...+2⁹=2¹⁰-1=1023。","app":"等比数列求和。","note":"q≠1；q=1时S=na₁。"},
      {"name":"无穷等比级数","formula":"S=\\frac{a_1}{1-q},\\ |q|<1","explain":"公比绝对值小于1时收敛。","deriv":"n→∞时qⁿ→0。","ex":"1+½+¼+...=2。","app":"几何级数求和。","note":"|q|≥1时发散。"},
      {"name":"等比中项","formula":"G=\\pm\\sqrt{ab}","explain":"a,b的等比中项。","deriv":"由a,G,b成等比得G²=ab。","ex":"4和9的等比中项为±6。","app":"插入等比项。","note":"ab>0时存在。"},
    ]},
  ]},
  # 第四章 不等式
  {"ch":"第四章","title":"不等式","en":"INEQUALITIES","sub":"均值不等式与证明","sections":[
    {"name":"4.1 均值不等式","color":"#2563eb","topics":[
      {"name":"均值不等式","formula":"\\frac{a+b}{2}\\ge\\sqrt{ab}","explain":"算术平均≥几何平均。","deriv":"(√a-√b)²≥0展开即得。","ex":"x>0时x+1/x≥2。","app":"求最值。","note":"等号当且仅当a=b。"},
      {"name":"均值链","formula":"H\\le G\\le A\\le Q","explain":"调和≤几何≤算术≤平方平均。","deriv":"由均值不等式推广。","ex":"对a=2,b=8：H=3.2,G=4,A=5,Q=√34≈5.83。","app":"不同平均的关系。","note":"均为正数时成立。"},
      {"name":"柯西不等式","formula":"(\\sum a_i^2)(\\sum b_i^2)\\ge(\\sum a_ib_i)^2","explain":"向量形式|a|²|b|²≥(a·b)²。","deriv":"由二次型非负得到。","ex":"(a²+b²)(c²+d²)≥(ac+bd)²。","app":"证明不等式、求最值。","note":"等号当a_i/b_i为常数。"},
    ]},
    {"name":"4.2 不等式证明","color":"#7c3aed","topics":[
      {"name":"比较法","formula":"a-b>0\\Leftrightarrow a>b","explain":"作差比较大小。","deriv":"由实数序关系。","ex":"证明a²+b²≥2ab，作差(a-b)²≥0。","app":"直接证明。","note":"最基本方法。"},
      {"name":"分析法","formula":"由结论倒推条件","explain":"从要证的结论出发，寻找充分条件。","deriv":"逻辑倒推。","ex":"要证√3+√7<2√5，平方后比较。","app":"复杂不等式证明。","note":"每步须可逆。"},
      {"name":"放缩法","formula":"A>C>B \\Rightarrow A>B","explain":"通过中间量传递不等式。","deriv":"不等式传递性。","ex":"证明1/n²<1/[n(n-1)]用于级数收敛。","app":"级数收敛证明。","note":"放缩方向要正确。"},
    ]},
  ]},
  # 第五章 解析几何
  {"ch":"第五章","title":"解析几何","en":"ANALYTIC GEOMETRY","sub":"直线与圆锥曲线","sections":[
    {"name":"5.1 直线","color":"#0f766e","topics":[
      {"name":"直线方程","formula":"y-y_0=k(x-x_0)","explain":"点斜式直线方程。","deriv":"斜率定义k=(y-y₀)/(x-x₀)。","ex":"过(1,2)斜率3的直线：y-2=3(x-1)。","app":"直线表示。","note":"k不存在时为竖直线x=x₀。"},
      {"name":"两直线夹角","formula":"\\tan\\theta=\\left|\\frac{k_2-k_1}{1+k_1k_2}\\right|","explain":"由正切差角公式。","deriv":"tan(θ₂-θ₁)。","ex":"k₁=1,k₂=√3，夹角30°。","app":"求直线夹角。","note":"取锐角。"},
      {"name":"点到直线距离","formula":"d=\\frac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}","explain":"点(x₀,y₀)到直线Ax+By+C=0的距离。","deriv":"由投影公式。","ex":"(0,0)到3x+4y-12=0的距离=12/5。","app":"距离计算。","note":"分子绝对值。"},
    ]},
    {"name":"5.2 圆","color":"#c2410c","topics":[
      {"name":"圆的标准方程","formula":"(x-a)^2+(y-b)^2=r^2","explain":"圆心(a,b)半径r的圆。","deriv":"由距离公式。","ex":"圆心(0,0)半径2：x²+y²=4。","app":"圆的表示。","note":"展开为一般式。"},
      {"name":"圆的一般方程","formula":"x^2+y^2+Dx+Ey+F=0","explain":"圆心(-D/2,-E/2)。","deriv":"配方得到标准式。","ex":"x²+y²-4x+6y-3=0圆心(2,-3)半径4。","app":"识别圆与圆心半径。","note":"需D²+E²-4F>0。"},
      {"name":"直线与圆位置","formula":"d<r相交,\\ d=r相切,\\ d>r相离","explain":"圆心到直线距离d与半径r比较。","deriv":"几何直观。","ex":"判断直线与圆交点个数。","app":"切线方程。","note":"切线与半径垂直。"},
    ]},
    {"name":"5.3 圆锥曲线","color":"#2563eb","topics":[
      {"name":"椭圆","formula":"\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1","explain":"到两焦点距离和为2a的点轨迹。","deriv":"由定义|PF₁|+|PF₂|=2a。","ex":"a=3,b=2的椭圆，c=√5。","app":"行星轨道。","note":"c²=a²-b²,e=c/a<1。"},
      {"name":"双曲线","formula":"\\frac{x^2}{a^2}-\\frac{y^2}{b^2}=1","explain":"到两焦点距离差的绝对值为2a。","deriv":"由定义||PF₁|-|PF₂||=2a。","ex":"渐近线y=±(b/a)x。","app":"双曲线轨道。","note":"c²=a²+b²,e>1。"},
      {"name":"抛物线","formula":"y^2=2px","explain":"到焦点与准线距离相等的点轨迹。","deriv":"由定义|PF|=d。","ex":"y²=4x焦点(1,0)准线x=-1。","app":"抛物面天线。","note":"e=1。"},
      {"name":"离心率","formula":"e=\\frac{c}{a}","explain":"描述圆锥曲线形状。","deriv":"由焦点与准线定义。","ex":"e<1椭圆，e=1抛物线，e>1双曲线。","app":"统一圆锥曲线。","note":"圆的e=0。"},
    ]},
  ]},
]

print("elementary-math topics:", sum(len(s["topics"]) for c in ELEMENTARY_MATH for s in c["sections"]))

# ===================== 高等数学 advanced-math =====================
ADVANCED_MATH = [
  {"ch":"第一章","title":"极限与连续","en":"LIMITS & CONTINUITY","sub":"极限定义与计算","sections":[
    {"name":"1.1 数列极限","color":"#2563eb","topics":[
      {"name":"ε-N定义","formula":"\\forall\\varepsilon>0,\\exists N, n>N\\Rightarrow|a_n-A|<\\varepsilon","explain":"数列{aₙ}收敛于A的严格定义。","deriv":"柯西给出严格定义。","ex":"lim(n→∞)1/n=0。","app":"分析数列收敛性。","note":"N依赖ε。"},
      {"name":"函数极限","formula":"\\lim_{x\\to a}f(x)=A","explain":"x趋近a时f(x)趋近A。","deriv":"ε-δ定义。","ex":"lim(x→0)sinx/x=1。","app":"微积分基础。","note":"与f(a)无关。"},
      {"name":"极限运算法则","formula":"\\lim(f+g)=\\lim f+\\lim g","explain":"和差积商的极限等于极限的和差积商。","deriv":"由ε-δ证明。","ex":"lim(x²+3x)=lim x²+3lim x。","app":"计算极限。","note":"商时分母极限非零。"},
      {"name":"两个重要极限","formula":"\\lim_{x\\to0}\\frac{\\sin x}{x}=1","explain":"第一个重要极限。","deriv":"用夹逼准则证明。","ex":"lim(x→0)sin3x/x=3。","app":"三角函数极限。","note":"第二个lim(1+1/x)^x=e。"},
      {"name":"夹逼准则","formula":"g(x)\\le f(x)\\le h(x), g,h\\to A\\Rightarrow f\\to A","explain":"若f被g,h夹住且g,h同极限，则f也趋于该极限。","deriv":"由不等式传递。","ex":"证明lim sinx/x=1。","app":"证明极限。","note":"也叫三明治定理。"},
      {"name":"单调有界定理","formula":"单调有界数列必收敛","explain":"单调递增有上界或单调递减有下界的数列收敛。","deriv":"实数完备性公理。","ex":"aₙ=(1+1/n)ⁿ单调递增有上界，收敛于e。","app":"证明数列收敛。","note":"是实数完备性等价命题。"},
    ]},
    {"name":"1.2 连续与间断","color":"#7c3aed","topics":[
      {"name":"连续定义","formula":"\\lim_{x\\to a}f(x)=f(a)","explain":"f在a处连续当且仅当极限等于函数值。","deriv":"需极限存在且等于f(a)。","ex":"f(x)=x²在任意点连续。","app":"判断连续性。","note":"三个条件缺一不可。"},
      {"name":"间断点分类","formula":"第一类：左右极限存在；第二类：至少一侧不存在","explain":"可去、跳跃、无穷、振荡间断。","deriv":"由左右极限情况分类。","ex":"f(x)=sin(1/x)在x=0振荡间断。","app":"分析函数性质。","note":"可去间断可补充定义连续。"},
      {"name":"介值定理","formula":"f连续, f(a)f(b)<0 \\Rightarrow \\exists c\\in(a,b), f(c)=0","explain":"连续函数取到两端点之间所有值。","deriv":"实数完备性。","ex":"证明方程x³-x-1=0在(1,2)有根。","app":"根的存在性。","note":"零点定理是特例。"},
      {"name":"最值定理","formula":"闭区间连续函数必有最大值和最小值","explain":"f∈C[a,b]，则∃最大值M和最小值m。","deriv":"由紧致性。","ex":"f(x)=sinx在[0,π]最大值1。","app":"求闭区间最值。","note":"开区间不一定成立。"},
    ]},
  ]},
  {"ch":"第二章","title":"导数与微分","en":"DERIVATIVES","sub":"导数定义与求导法则","sections":[
    {"name":"2.1 导数","color":"#2563eb","topics":[
      {"name":"导数定义","formula":"f'(x)=\\lim_{\\Delta x\\to0}\\frac{f(x+\\Delta x)-f(x)}{\\Delta x}","explain":"函数在x处的瞬时变化率。","deriv":"割线斜率的极限。","ex":"(x²)'=2x。","app":"切线斜率、速度。","note":"左导=右导才可导。"},
      {"name":"基本求导公式","formula":"(x^n)'=nx^{n-1}","explain":"幂函数求导。","deriv":"二项式展开取极限。","ex":"(x³)'=3x²。","app":"多项式求导。","note":"n为任意实数。"},
      {"name":"求导四则运算","formula":"(uv)'=u'v+uv'","explain":"乘积求导法则。","deriv":"由定义展开。","ex":"(xsinx)'=sinx+xcosx。","app":"复杂函数求导。","note":"(u/v)'=(u'v-uv')/v²。"},
      {"name":"链式法则","formula":"[f(g(x))]'=f'(g(x))g'(x)","explain":"复合函数求导。","deriv":"用微分定义证明。","ex":"(sin(x²))'=cos(x²)·2x。","app":"复合函数求导。","note":"多层嵌套逐层求导。"},
      {"name":"隐函数求导","formula":"F(x,y)=0 \\Rightarrow \\frac{dy}{dx}=-F_x/F_y","explain":"隐函数导数公式。","deriv":"对x求导解y'。","ex":"x²+y²=1，y'=-x/y。","app":"隐函数曲线切线。","note":"F_y≠0。"},
      {"name":"高阶导数","formula":"f^{(n)}(x)","explain":"导数的n阶导数。","deriv":"逐阶求导。","ex":"(sinx)⁽⁴⁾=sinx。","app":"泰勒展开、微分方程。","note":"莱布尼茨公式(uv)⁽ⁿ⁾。"},
    ]},
    {"name":"2.2 微分中值定理","color":"#7c3aed","topics":[
      {"name":"罗尔定理","formula":"f∈C[a,b],D(a,b),f(a)=f(b) \\Rightarrow \\exists\\xi,f'(\\xi)=0","explain":"两端点值相等的可导函数内部有水平切线。","deriv":"由最值定理与费马引理。","ex":"验证f(x)=x²-1在[-1,1]。","app":"证明存在性。","note":"三个条件缺一不可。"},
      {"name":"拉格朗日中值定理","formula":"f'(\\xi)=\\frac{f(b)-f(a)}{b-a}","explain":"存在切线平行于割线。","deriv":"构造辅助函数用罗尔定理。","ex":"证明f'=0则f为常数。","app":"证明不等式、恒等式。","note":"罗尔定理是特例。"},
      {"name":"柯西中值定理","formula":"\\frac{f'(\\xi)}{g'(\\xi)}=\\frac{f(b)-f(a)}{g(b)-g(a)}","explain":"参数形式的中值定理。","deriv":"构造辅助函数。","ex":"用于洛必达法则证明。","app":"证明不定式极限。","note":"g'≠0。"},
      {"name":"洛必达法则","formula":"\\lim\\frac{f}{g}=\\lim\\frac{f'}{g'}","explain":"0/0或∞/∞型不定式可对分子分母分别求导。","deriv":"由柯西中值定理。","ex":"lim(x→0)sinx/x=lim cosx/1=1。","app":"求不定式极限。","note":"可重复使用直到非不定式。"},
      {"name":"泰勒公式","formula":"f(x)=\\sum_{k=0}^n\\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n","explain":"用多项式逼近函数。","deriv":"由中值定理递推。","ex":"eˣ=1+x+x²/2!+...。","app":"近似计算、极限。","note":"Rₙ为余项。"},
    ]},
  ]},
  {"ch":"第三章","title":"积分学","en":"INTEGRATION","sub":"不定积分与定积分","sections":[
    {"name":"3.1 不定积分","color":"#0f766e","topics":[
      {"name":"原函数与不定积分","formula":"\\int f(x)dx=F(x)+C, F'=f","explain":"f的全体原函数。","deriv":"导数逆运算。","ex":"∫2xdx=x²+C。","app":"求原函数。","note":"常数C不可忘。"},
      {"name":"基本积分公式","formula":"\\int x^n dx=\\frac{x^{n+1}}{n+1}+C","explain":"幂函数积分。","deriv":"幂函数求导逆运算。","ex":"∫x³dx=x⁴/4+C。","app":"基础积分。","note":"n≠-1。"},
      {"name":"换元积分法","formula":"\\int f(g(x))g'(x)dx=\\int f(u)du","explain":"第一类换元（凑微分）。","deriv":"链式法则逆用。","ex":"∫2xcos(x²)dx=sin(x²)+C。","app":"复杂积分。","note":"第二类换元需回代。"},
      {"name":"分部积分法","formula":"\\int u dv=uv-\\int v du","explain":"乘积求导的逆运算。","deriv":"d(uv)=udv+vdu积分。","ex":"∫xeˣdx=xeˣ-eˣ+C。","app":"乘积型积分。","note":"选u按LIATE法则。"},
    ]},
    {"name":"3.2 定积分","color":"#c2410c","topics":[
      {"name":"定积分定义","formula":"\\int_a^b f(x)dx=\\lim\\sum f(\\xi_i)\\Delta x_i","explain":"黎曼和的极限。","deriv":"分割、取点、求和、取极限。","ex":"∫₀¹x²dx=1/3。","app":"面积、体积、物理量。","note":"可积条件。"},
      {"name":"牛顿-莱布尼茨公式","formula":"\\int_a^b f(x)dx=F(b)-F(a)","explain":"微积分基本定理。","deriv":"由变上限积分求导证明。","ex":"∫₀¹x²dx=[x³/3]₀¹=1/3。","app":"计算定积分。","note":"联系微分与积分。"},
      {"name":"变上限积分","formula":"\\frac{d}{dx}\\int_a^x f(t)dt=f(x)","explain":"变上限积分对上限求导等于被积函数。","deriv":"由积分中值定理。","ex":"d/dx∫₀ˣsin t dt=sinx。","app":"含积分的函数求导。","note":"上限是x的函数时用链式法则。"},
      {"name":"定积分应用","formula":"S=\\int_a^b|f(x)-g(x)|dx","explain":"两条曲线间面积。","deriv":"微元法。","ex":"y=x²与y=x围成面积=1/6。","app":"面积、体积、弧长、物理应用。","note":"注意积分区间与上下函数。"},
    ]},
  ]},
  {"ch":"第四章","title":"多元微积分","en":"MULTIVARIABLE CALCULUS","sub":"偏导数与重积分","sections":[
    {"name":"4.1 偏导数与全微分","color":"#2563eb","topics":[
      {"name":"偏导数","formula":"f_x=\\lim_{\\Delta x\\to0}\\frac{f(x+\\Delta x,y)-f(x,y)}{\\Delta x}","explain":"固定y对x求导。","deriv":"一元导数推广。","ex":"f=x²y，fₓ=2xy。","app":"多元变化率。","note":"偏导存在不一定连续。"},
      {"name":"全微分","formula":"dz=f_x dx+f_y dy","explain":"函数增量的线性主部。","deriv":"由可微定义。","ex":"z=x²y，dz=2xydx+x²dy。","app":"近似计算。","note":"可微必偏导存在。"},
      {"name":"链式法则","formula":"\\frac{dz}{dt}=f_x\\frac{dx}{dt}+f_y\\frac{dy}{dt}","explain":"多元复合函数求导。","deriv":"全微分形式不变性。","ex":"z=x²+y²,x=t,y=t²。","app":"复合函数导数。","note":"树状图辅助。"},
      {"name":"方向导数与梯度","formula":"\\nabla f=(f_x,f_y,f_z)","explain":"梯度是方向导数最大的方向。","deriv":"由方向导数公式。","ex":"f=x²+y²，∇f=(2x,2y)。","app":"最速下降、场论。","note":"方向导数=∇f·方向向量。"},
    ]},
    {"name":"4.2 重积分","color":"#7c3aed","topics":[
      {"name":"二重积分","formula":"\\iint_D f(x,y)d\\sigma","explain":"曲顶柱体体积。","deriv":"黎曼和推广。","ex":"∬_D x dσ，D为单位圆。","app":"面积、质量、体积。","note":"化为累次积分。"},
      {"name":"极坐标二重积分","formula":"\\iint f(r\\cos\\theta,r\\sin\\theta)r dr d\\theta","explain":"极坐标变换，面积元r dr dθ。","deriv":"雅可比行列式r。","ex":"∬_D (x²+y²)dσ，D:单位圆，=π/2。","app":"圆形区域积分。","note":"别忘了r因子。"},
      {"name":"三重积分","formula":"\\iiint_\\Omega f(x,y,z)dV","explain":"空间区域上的积分。","deriv":"黎曼和。","ex":"∭dV=区域体积。","app":"体积、质量、重心。","note":"柱坐标、球坐标变换。"},
    ]},
  ]},
  {"ch":"第五章","title":"级数","en":"SERIES","sub":"数项级数与幂级数","sections":[
    {"name":"5.1 数项级数","color":"#0f766e","topics":[
      {"name":"级数收敛定义","formula":"\\sum_{n=1}^\\infty a_n=\\lim_{n\\to\\infty}S_n","explain":"部分和数列收敛。","deriv":"由数列极限定义。","ex":"∑(1/2)ⁿ=2。","app":"级数求和。","note":"收敛必要条件aₙ→0。"},
      {"name":"正项级数判敛","formula":"\\lim\\frac{a_{n+1}}{a_n}=\\rho","explain":"比值判别法，ρ<1收敛。","deriv":"与等比级数比较。","ex":"∑n!/nⁿ收敛。","app":"判断收敛。","note":"ρ=1时失效。"},
      {"name":"比较判别法","formula":"0\\le a_n\\le b_n, \\sum b_n收敛 \\Rightarrow \\sum a_n收敛","explain":"大的收敛则小的收敛。","deriv":"部分和单调有界。","ex":"∑1/n²收敛（<∑1/[n(n-1)]）。","app":"已知级数判未知。","note":"需找到合适比较级数。"},
      {"name":"交错级数","formula":"莱布尼茨判敛法","explain":"aₙ单调递减趋于0则交错级数收敛。","deriv":"部分和的奇偶子列收敛于同一值。","ex":"∑(-1)ⁿ/n收敛。","app":"交错级数判敛。","note":"是条件收敛。"},
      {"name":"绝对收敛","formula":"\\sum|a_n|收敛 \\Rightarrow \\sum a_n收敛","explain":"绝对值级数收敛则原级数收敛。","deriv":"由柯西准则。","ex":"∑(-1)ⁿ/n²绝对收敛。","app":"更强的收敛性。","note":"绝对收敛可重排。"},
    ]},
    {"name":"5.2 幂级数","color":"#c2410c","topics":[
      {"name":"幂级数收敛半径","formula":"R=\\frac{1}{\\lim\\sqrt[n]{|a_n|}}","explain":"柯西-阿达马公式。","deriv":"根值判别法。","ex":"∑xⁿ/n的R=1。","app":"求收敛域。","note":"端点需单独判断。"},
      {"name":"泰勒级数","formula":"f(x)=\\sum_{n=0}^\\infty\\frac{f^{(n)}(0)}{n!}x^n","explain":"函数的幂级数展开。","deriv":"泰勒公式n→∞余项→0。","ex":"eˣ=∑xⁿ/n!。","app":"函数逼近。","note":"需在收敛域内。"},
      {"name":"常用展开","formula":"\\frac{1}{1-x}=\\sum_{n=0}^\\infty x^n","explain":"几何级数展开。","deriv":"等比级数求和。","ex":"1/(1+x²)=∑(-1)ⁿx²ⁿ。","app":"求其他展开。","note":"|x|<1。"},
    ]},
  ]},
  {"ch":"第六章","title":"微分方程","en":"DIFFERENTIAL EQUATIONS","sub":"一阶与高阶微分方程","sections":[
    {"name":"6.1 一阶微分方程","color":"#2563eb","topics":[
      {"name":"可分离变量","formula":"\\frac{dy}{dx}=f(x)g(y)","explain":"变量分离后积分。","deriv":"两边除以g(y)乘dx积分。","ex":"dy/dx=xy，y=Ce^(x²/2)。","app":"简单微分方程。","note":"需g(y)≠0。"},
      {"name":"一阶线性方程","formula":"y'+P(x)y=Q(x)","explain":"通解y=e^{-∫Pdx}(∫Qe^{∫Pdx}dx+C)。","deriv":"积分因子法。","ex":"y'+y=x，y=x-1+Ce⁻ˣ。","app":"线性方程求解。","note":"先化为标准形式。"},
      {"name":"齐次方程","formula":"\\frac{dy}{dx}=\\varphi(\\frac{y}{x})","explain":"令u=y/x化为可分离。","deriv":"y=ux，y'=u+xu'。","ex":"dy/dx=(x+y)/(x-y)。","app":"齐次方程。","note":"判断齐次性。"},
    ]},
    {"name":"6.2 高阶线性方程","color":"#7c3aed","topics":[
      {"name":"二阶常系数齐次","formula":"y''+py'+qy=0","explain":"特征方程r²+pr+q=0。","deriv":"设y=e^{rx}代入。","ex":"y''-3y'+2y=0，y=C₁eˣ+C₂e²ˣ。","app":"齐次方程通解。","note":"按判别式分三种情况。"},
      {"name":"非齐次特解","formula":"y=y_h+y_p","explain":"通解=齐次通解+非齐次特解。","deriv":"线性方程解结构。","ex":"y''+y=x，yₚ=x。","app":"非齐次方程。","note":"待定系数法或常数变易法。"},
    ]},
  ]},
]

# ===================== 概率论与数理统计 probability-statistics =====================
PROBABILITY_STATISTICS = [
  {"ch":"第一章","title":"随机事件与概率","en":"RANDOM EVENTS & PROBABILITY","sub":"古典概型与概率公式","sections":[
    {"name":"1.1 概率基础","color":"#2563eb","topics":[
      {"name":"概率公理化","formula":"0\\le P(A)\\le1, P(\\Omega)=1","explain":"概率满足非负、规范、可列可加。","deriv":"柯尔莫哥洛夫公理。","ex":"抛硬币P(正面)=1/2。","app":"概率计算基础。","note":"可列可加性是核心。"},
      {"name":"古典概型","formula":"P(A)=\\frac{|A|}{|\\Omega|}","explain":"等可能事件的概率。","deriv":"样本空间有限且等可能。","ex":"掷骰子得偶数的概率=3/6=1/2。","app":"简单概率问题。","note":"需等可能。"},
      {"name":"加法公式","formula":"P(A\\cup B)=P(A)+P(B)-P(A\\cap B)","explain":"并事件概率。","deriv":"容斥原理。","ex":"P(A∪B)避免重复计算交集。","app":"求并事件概率。","note":"互斥时交集为0。"},
      {"name":"条件概率","formula":"P(A|B)=\\frac{P(AB)}{P(B)}","explain":"在B发生条件下A的概率。","deriv":"定义。","ex":"P(第二次正面|第一次正面)=1/2。","app":"更新概率。","note":"P(B)>0。"},
      {"name":"乘法公式","formula":"P(AB)=P(A)P(B|A)","explain":"交事件概率。","deriv":"条件概率变形。","ex":"无放回取两球都红的概率。","app":"联合概率。","note":"可推广到n个事件。"},
      {"name":"全概率公式","formula":"P(A)=\\sum P(B_i)P(A|B_i)","explain":"由划分{B_i}求A的概率。","deriv":"A=∪(AB_i)互斥。","ex":"用全概率求次品率。","app":"复杂事件概率。","note":"{B_i}是完备事件组。"},
      {"name":"贝叶斯公式","formula":"P(B_i|A)=\\frac{P(B_i)P(A|B_i)}{\\sum P(B_j)P(A|B_j)}","explain":"后验概率公式。","deriv":"条件概率与全概率结合。","ex":"已知阳性求患病概率。","app":"贝叶斯推断。","note":"先验→后验。"},
      {"name":"事件独立性","formula":"P(AB)=P(A)P(B)","explain":"A,B独立当且仅当交概率等于概率乘积。","deriv":"由条件概率P(A|B)=P(A)。","ex":"抛两次硬币独立。","app":"独立事件计算。","note":"独立≠互斥。"},
    ]},
  ]},
  {"ch":"第二章","title":"随机变量及其分布","en":"RANDOM VARIABLES","sub":"分布函数与常见分布","sections":[
    {"name":"2.1 离散型随机变量","color":"#7c3aed","topics":[
      {"name":"分布律","formula":"P(X=x_k)=p_k","explain":"离散随机变量取各值的概率。","deriv":"由概率定义。","ex":"泊松分布P(X=k)=λᵏe⁻λ/k!。","app":"描述离散随机变量。","note":"∑pₖ=1。"},
      {"name":"二项分布","formula":"X\\sim B(n,p), P(X=k)=C_n^k p^k(1-p)^{n-k}","explain":"n次独立伯努利试验中成功次数。","deriv":"乘法原理与组合。","ex":"抛10次硬币正面次数~B(10,½)。","app":"独立重复试验。","note":"期望np，方差np(1-p)。"},
      {"name":"泊松分布","formula":"P(X=k)=\\frac{\\lambda^k e^{-\\lambda}}{k!}","explain":"稀有事件次数。","deriv":"二项分布n→∞,np→λ的极限。","ex":"电话呼叫次数、放射性衰变。","app":"稀有事件建模。","note":"期望=方差=λ。"},
      {"name":"分布函数","formula":"F(x)=P(X\\le x)","explain":"随机变量不超过x的概率。","deriv":"由概率定义。","ex":"F(x)单调不减、右连续、F(-∞)=0,F(∞)=1。","app":"统一描述离散与连续。","note":"P(a<X≤b)=F(b)-F(a)。"},
    ]},
    {"name":"2.2 连续型随机变量","color":"#0f766e","topics":[
      {"name":"概率密度","formula":"f(x)=F'(x), P(a<X<b)=\\int_a^b f(x)dx","explain":"密度函数的积分是概率。","deriv":"由分布函数导数定义。","ex":"均匀分布f(x)=1/(b-a)。","app":"连续随机变量。","note":"f(x)≥0，∫f=1。"},
      {"name":"正态分布","formula":"f(x)=\\frac{1}{\\sigma\\sqrt{2\\pi}}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}","explain":"最重要的连续分布。","deriv":"中心极限定理的产物。","ex":"身高、测量误差近似正态。","app":"大量自然现象。","note":"N(μ,σ²)，标准化Z=(X-μ)/σ。"},
      {"name":"均匀分布","formula":"f(x)=\\frac{1}{b-a}, x\\in[a,b]","explain":"区间上等概率分布。","deriv":"密度为常数。","ex":"随机数生成。","app":"等可能连续取值。","note":"期望(a+b)/2，方差(b-a)²/12。"},
      {"name":"指数分布","formula":"f(x)=\\lambda e^{-\\lambda x}, x>0","explain":"无记忆性分布。","deriv":"泊松过程的等待时间。","ex":"电子元件寿命。","app":"寿命、排队。","note":"P(X>s+t|X>s)=P(X>t)。"},
    ]},
  ]},
  {"ch":"第三章","title":"数字特征","en":"EXPECTATION & VARIANCE","sub":"期望方差协方差","sections":[
    {"name":"3.1 期望与方差","color":"#2563eb","topics":[
      {"name":"数学期望","formula":"E(X)=\\sum x_k p_k","explain":"随机变量的加权平均。","deriv":"加权平均。","ex":"E(B(n,p))=np。","app":"平均值。","note":"线性E(aX+b)=aE(X)+b。"},
      {"name":"方差","formula":"D(X)=E[(X-E(X))^2]=E(X^2)-[E(X)]^2","explain":"偏离期望的程度。","deriv":"展开得到计算公式。","ex":"D(B(n,p))=np(1-p)。","app":"离散程度。","note":"D(aX+b)=a²D(X)。"},
      {"name":"协方差","formula":"Cov(X,Y)=E(XY)-E(X)E(Y)","explain":"X,Y协同变化程度。","deriv":"由定义展开。","ex":"Cov(X,X)=D(X)。","app":"相关性。","note":"独立则协方差为0。"},
      {"name":"相关系数","formula":"\\rho=\\frac{Cov(X,Y)}{\\sqrt{D(X)D(Y)}}","explain":"标准化的协方差，|ρ|≤1。","deriv":"由柯西不等式。","ex":"ρ=1完全正相关。","app":"线性相关程度。","note":"|ρ|=1时线性相关。"},
    ]},
  ]},
  {"ch":"第四章","title":"大数定律与中心极限定理","en":"LAWS OF LARGE NUMBERS & CLT","sub":"极限定理","sections":[
    {"name":"4.1 极限定理","color":"#7c3aed","topics":[
      {"name":"切比雪夫不等式","formula":"P(|X-E(X)|\\ge\\varepsilon)\\le\\frac{D(X)}{\\varepsilon^2}","explain":"偏离期望的概率上界。","deriv":"由期望定义放缩。","ex":"估计离群概率。","app":"概率估计。","note":"对任意分布成立。"},
      {"name":"大数定律","formula":"\\bar{X}\\xrightarrow{P}\\mu","explain":"样本均值依概率收敛于期望。","deriv":"切比雪夫不等式证明。","ex":"抛硬币频率趋于1/2。","app":"频率稳定性。","note":"独立同分布条件。"},
      {"name":"中心极限定理","formula":"\\frac{\\sum X_i-n\\mu}{\\sigma\\sqrt{n}}\\to N(0,1)","explain":"独立同分布和的标准化趋于正态。","deriv":"特征函数证明。","ex":"大量独立因素之和近似正态。","app":"正态分布的普适性。","note":"n充分大时可用正态近似。"},
    ]},
  ]},
  {"ch":"第五章","title":"数理统计","en":"MATHEMATICAL STATISTICS","sub":"参数估计与假设检验","sections":[
    {"name":"5.1 参数估计","color":"#0f766e","topics":[
      {"name":"矩估计","formula":"用样本矩估计总体矩","explain":"令样本矩等于总体矩解参数。","deriv":"大数定律保证样本矩收敛。","ex":"正态分布矩估计μ=样本均值。","app":"参数估计。","note":"简单但不一定最优。"},
      {"name":"最大似然估计","formula":"L(\\theta)=\\prod f(x_i;\\theta)","explain":"使样本出现概率最大的参数。","deriv":"对L取对数求导令为0。","ex":"伯努利p的MLE=样本均值。","app":"参数估计。","note":"对数似然求导更方便。"},
      {"name":"置信区间","formula":"P(\\hat{\\theta}_L<\\theta<\\hat{\\theta}_U)=1-\\alpha","explain":"参数以1-α概率落在区间内。","deriv":"由枢轴量分布。","ex":"μ的95%置信区间。","app":"区间估计。","note":"置信水平1-α。"},
    ]},
    {"name":"5.2 假设检验","color":"#c2410c","topics":[
      {"name":"假设检验思想","formula":"H_0 vs H_1","explain":"根据样本判断是否拒绝原假设。","deriv":"小概率事件原理。","ex":"检验均值是否等于给定值。","app":"统计推断。","note":"两类错误α,β。"},
      {"name":"u检验","formula":"u=\\frac{\\bar{X}-\\mu_0}{\\sigma/\\sqrt{n}}","explain":"方差已知时检验均值。","deriv":"标准化统计量。","ex":"H₀:μ=μ₀。","app":"大样本或方差已知。","note":"|u|>u_{α/2}拒绝。"},
      {"name":"t检验","formula":"t=\\frac{\\bar{X}-\\mu_0}{S/\\sqrt{n}}","explain":"方差未知时用样本标准差。","deriv":"t分布。","ex":"小样本检验均值。","app":"方差未知。","note":"自由度n-1。"},
      {"name":"χ²检验","formula":"\\chi^2=\\frac{(n-1)S^2}{\\sigma_0^2}","explain":"检验方差。","deriv":"χ²分布。","ex":"检验方差是否等于σ₀²。","app":"方差检验。","note":"自由度n-1。"},
    ]},
  ]},
]

# ===================== 群论 group-theory =====================
GROUP_THEORY = [
  {"ch":"第一章","title":"群的基本概念","en":"GROUP BASICS","sub":"群定义与性质","sections":[
    {"name":"1.1 群定义","color":"#2563eb","topics":[
      {"name":"群的定义","formula":"(G,\\cdot)满足封闭、结合、单位元、逆元","explain":"群是带有二元运算的集合，满足四条公理。","deriv":"伽罗瓦提出。","ex":"整数加法群(Z,+)。","app":"对称性描述。","note":"运算不一定交换。"},
      {"name":"阿贝尔群","formula":"ab=ba","explain":"运算交换的群。","deriv":"附加交换律。","ex":"加法群都是阿贝尔群。","app":"可交换结构。","note":"非阿贝尔群如置换群。"},
      {"name":"子群","formula":"H\\le G","explain":"G的非空子集H在G的运算下也成群。","deriv":"需验证封闭、逆元。","ex":"偶数是整数加法群的子群。","app":"群的子结构。","note":"单位元必在子群中。"},
      {"name":"群的阶","formula":"|G|","explain":"群中元素个数。","deriv":"基数。","ex":"S₃阶为6。","app":"分类群。","note":"有限群与无限群。"},
      {"name":"元素的阶","formula":"ord(a)=\\min\\{n:a^n=e\\}","explain":"使aⁿ=e的最小正整数n。","deriv":"由幂运算定义。","ex":"模2非零元阶为2。","app":"元素性质。","note":"有限群中元素阶整除群阶。"},
      {"name":"循环群","formula":"G=\\langle a\\rangle","explain":"由一个元素生成的群。","deriv":"所有元素为a的幂。","ex":"Zₙ是n阶循环群。","app":"最简单的群。","note":"循环群必阿贝尔。"},
    ]},
    {"name":"1.2 群同态与商群","color":"#7c3aed","topics":[
      {"name":"群同态","formula":"\\varphi(ab)=\\varphi(a)\\varphi(b)","explain":"保持群运算的映射。","deriv":"定义。","ex":"行列式是GL(n)到乘法群的同态。","app":"群结构比较。","note":"同态核是正规子群。"},
      {"name":"同构","formula":"G\\cong H","explain":"双射同态。","deriv":"同态+双射。","ex":"所有n阶循环群互相同构。","app":"群的等价分类。","note":"同构群结构相同。"},
      {"name":"正规子群","formula":"N\\triangleleft G, gNg^{-1}=N","explain":"对所有g共轭不变的子群。","deriv":"定义。","ex":"交错群Aₙ是Sₙ的正规子群。","app":"构造商群。","note":"阿贝尔群所有子群正规。"},
      {"name":"商群","formula":"G/N","explain":"N的陪集构成的群。","deriv":"正规子群保证陪集运算良定。","ex":"Z/2Z是二元群。","app":"群的分解。","note":"|G/N|=|G|/|N|。"},
      {"name":"同态基本定理","formula":"G/\\ker\\varphi\\cong\\text{Im}\\varphi","explain":"同态像与商群同构。","deriv":"构造自然同构。","ex":"Z/nZ≅Zₙ。","app":"群同态结构。","note":"群论核心定理。"},
    ]},
  ]},
  {"ch":"第二章","title":"群作用与置换群","en":"GROUP ACTIONS & PERMUTATION GROUPS","sub":"群作用与轨道","sections":[
    {"name":"2.1 群作用","color":"#0f766e","topics":[
      {"name":"群作用定义","formula":"g\\cdot x","explain":"群G在集合X上的作用。","deriv":"e·x=x，(gh)·x=g·(h·x)。","ex":"对称群作用在集合上。","app":"对称性研究。","note":"左作用与右作用。"},
      {"name":"轨道","formula":"\\mathcal{O}_x=\\{g\\cdot x:g\\in G\\}","explain":"x在群作用下的像集合。","deriv":"等价类。","ex":"正多边形顶点在旋转群下的轨道。","app":"分类轨道。","note":"轨道划分X。"},
      {"name":"稳定子群","formula":"G_x=\\{g:g\\cdot x=x\\}","explain":"保持x不动的元素构成的子群。","deriv":"验证子群条件。","ex":"旋转群中保持某顶点的元素。","app":"轨道-稳定子定理。","note":"|O_x|=[G:G_x]。"},
      {"name":"轨道-稳定子定理","formula":"|\\mathcal{O}_x|=[G:G_x]","explain":"轨道大小等于稳定子群的指数。","deriv":"建立双射。","ex":"正n边形顶点数=n。","app":"计数。","note":"拉格朗日定理应用。"},
      {"name":"伯恩赛德引理","formula":"|X/G|=\\frac1{|G|}\\sum_{g\\in G}|X^g|","explain":"轨道数等于平均不动点数。","deriv":"双重计数。","ex":"项链染色计数。","app":"计数轨道。","note":"群作用计数核心。"},
    ]},
    {"name":"2.2 置换群","color":"#c2410c","topics":[
      {"name":"对称群Sₙ","formula":"|S_n|=n!","explain":"n个元素的全体置换构成的群。","deriv":"全排列数。","ex":"S₃是正三角形对称群。","app":"置换与对称。","note":"n≥3时非阿贝尔。"},
      {"name":"对换","formula":"(ij)","explain":"只交换两个元素的置换。","deriv":"2阶循环。","ex":"(12)交换1和2。","app":"置换分解。","note":"每个置换可表为对换乘积。"},
      {"name":"奇偶置换","formula":"\\text{sgn}(\\sigma)=\\pm1","explain":"对换个数的奇偶性。","deriv":"置换的逆序数奇偶。","ex":"(123)是偶置换。","app":"交错群定义。","note":"偶置换构成Aₙ。"},
      {"name":"交错群Aₙ","formula":"|A_n|=n!/2","explain":"Sₙ中偶置换构成的正规子群。","deriv":"sgn同态的核。","ex":"A₃是3阶循环群。","app":"简单群例子。","note":"Aₙ(n≥5)是单群。"},
      {"name":"循环置换","formula":"(i_1 i_2 \\cdots i_k)","explain":"轮换分解。","deriv":"置换的循环表示。","ex":"(123)将1→2→3→1。","app":"置换表示。","note":"不相交轮换可交换。"},
    ]},
  ]},
  {"ch":"第三章","title":"西罗定理与可解群","en":"SYLOW THEOREMS & SOLVABLE GROUPS","sub":"有限群结构","sections":[
    {"name":"3.1 西罗定理","color":"#2563eb","topics":[
      {"name":"拉格朗日定理","formula":"H\\le G \\Rightarrow |H|||G|","explain":"子群阶整除群阶。","deriv":"陪集划分。","ex":"6阶群的子群阶只能是1,2,3,6。","app":"子群阶限制。","note":"逆命题不成立。"},
      {"name":"西罗p子群","formula":"P\\le G, |P|=p^k","explain":"群阶中p的最高次幂阶子群。","deriv":"西罗第一定理保证存在。","ex":"S₃的西罗3子群阶3。","app":"有限群分类。","note":"西罗子群共轭。"},
      {"name":"西罗定理","formula":"n_p\\equiv1\\pmod p, n_p||G|/p^k","explain":"西罗p子群个数的约束。","deriv":"群作用证明。","ex":"6阶群n₃=1，故唯一正规。","app":"判断正规子群。","note":"nₚ=1则西罗子群正规。"},
    ]},
    {"name":"3.2 可解群与单群","color":"#7c3aed","topics":[
      {"name":"换位子群","formula":"[G,G]=\\langle aba^{-1}b^{-1}\\rangle","explain":"由换位子生成的子群。","deriv":"最小的使G/N阿贝尔的正规子群N。","ex":"[S₃,S₃]=A₃。","app":"可解群定义。","note":"G/[G,G]是最大阿贝尔商。"},
      {"name":"可解群","formula":"存在正规列G=G₀▷G₁▷...▷Gₙ={e}，商因子阿贝尔","explain":"有阿贝尔正规列的群。","deriv":"定义。","ex":"S₃可解（S₃▷A₃▷{e}）。","app":"方程可解性。","note":"阿贝尔群必可解。"},
      {"name":"单群","formula":"G只有{e}和G为正规子群","explain":"无非平凡正规子群。","deriv":"定义。","ex":"Aₙ(n≥5)是单群。","app":"有限群的积木。","note":"有限单群分类定理。"},
    ]},
  ]},
  {"ch":"第四章","title":"表示论基础","en":"REPRESENTATION THEORY","sub":"群表示","sections":[
    {"name":"4.1 表示","color":"#0f766e","topics":[
      {"name":"群表示","formula":"\\rho:G\\to GL(V)","explain":"群到一般线性群的同态。","deriv":"定义。","ex":"正三角形旋转的矩阵表示。","app":"群的线性化。","note":"忠实表示是单射。"},
      {"name":"不可约表示","formula":"没有非平凡不变子空间","explain":"不可分解为子表示的直和。","deriv":"不变子空间定义。","ex":"S₃的二维不可约表示。","app":"表示的基本构件。","note":"马施克定理保证半单。"},
      {"name":"特征标","formula":"\\chi(g)=\\text{tr}\\rho(g)","explain":"表示矩阵的迹。","deriv":"迹的相似不变性。","ex":"平凡表示特征标恒为1。","app":"表示分类。","note":"共轭类上常值。"},
    ]},
  ]},
]

print("math subjects loaded")

# ===================== 数学物理方法 mathematical-methods =====================
MATHEMATICAL_METHODS = [
  {"ch":"第一章","title":"复变函数","en":"COMPLEX ANALYSIS","sub":"解析函数与留数","sections":[
    {"name":"1.1 解析函数","color":"#2563eb","topics":[
      {"name":"解析函数定义","formula":"f(z)=u+iv, u_x=v_y, u_y=-v_x","explain":"满足柯西-黎曼方程的复函数。","deriv":"由可微定义推出C-R方程。","ex":"eᶻ解析，|z|不解析。","app":"复分析基础。","note":"C-R方程是必要条件。"},
      {"name":"柯西积分定理","formula":"\\oint_C f(z)dz=0","explain":"解析函数沿闭曲线积分为零。","deriv":"由格林公式与C-R方程。","ex":"∮_C eᶻdz=0。","app":"复积分计算。","note":"C为简单闭曲线。"},
      {"name":"柯西积分公式","formula":"f(z_0)=\\frac1{2\\pi i}\\oint_C\\frac{f(z)}{z-z_0}dz","explain":"解析函数由边界值确定。","deriv":"由柯西定理变形。","ex":"求∮_C z/(z-1)dz。","app":"计算围道积分。","note":"z₀在C内部。"},
      {"name":"留数定理","formula":"\\oint_C f(z)dz=2\\pi i\\sum \\text{Res}(f,z_k)","explain":"围道积分等于留数之和。","deriv":"由洛朗展开系数。","ex":"计算实积分∫₋∞^∞dx/(1+x²)=π。","app":"实积分计算。","note":"极点处留数Res=a₋₁。"},
      {"name":"洛朗级数","formula":"f(z)=\\sum_{n=-\\infty}^\\infty a_n(z-z_0)^n","explain":"圆环域内的级数展开。","deriv":"泰勒级数推广。","ex":"1/[z(z-1)]在0<|z|<1的展开。","app":"奇点分类。","note":"主部决定奇点类型。"},
      {"name":"奇点分类","formula":"可去、极点、本性奇点","explain":"由洛朗主部项数分类。","deriv":"主部分类。","ex":"sinz/z在0可去，1/z为极点。","app":"分析函数奇点。","note":"本性奇点附近取任意值。"},
      {"name":"留数计算","formula":"Res(f,z_0)=\\lim_{z\\to z_0}(z-z_0)f(z)","explain":"一阶极点留数。","deriv":"洛朗展开a₋₁。","ex":"Res(1/sinz,0)=1。","app":"留数定理应用。","note":"高阶极点用导数公式。"},
    ]},
    {"name":"1.2 保角变换","color":"#7c3aed","topics":[
      {"name":"保角变换","formula":"f'(z)\\neq0","explain":"解析函数保持角度与局部形状。","deriv":"导数非零处保角。","ex":"w=z²将第一象限映为上半平面。","app":"边值问题化简。","note":"又称共形映射。"},
      {"name":"分式线性变换","formula":"w=\\frac{az+b}{cz+d}","explain":"莫比乌斯变换。","deriv":"保圆性。","ex":"w=(z-i)/(z+i)将上半平面映为单位圆。","app":"区域映射。","note":"ad-bc≠0。"},
    ]},
  ]},
  {"ch":"第二章","title":"傅里叶分析","en":"FOURIER ANALYSIS","sub":"傅里叶级数与变换","sections":[
    {"name":"2.1 傅里叶级数","color":"#0f766e","topics":[
      {"name":"傅里叶级数","formula":"f(x)=\\frac{a_0}{2}+\\sum(a_n\\cos nx+b_n\\sin nx)","explain":"周期函数展开为三角级数。","deriv":"正交性。","ex":"方波的傅里叶级数。","app":"信号分析。","note":"aₙ,bₙ为傅里叶系数。"},
      {"name":"傅里叶系数","formula":"a_n=\\frac1\\pi\\int_{-\\pi}^\\pi f(x)\\cos nx dx","explain":"利用正交性计算。","deriv":"两边乘cosmx积分。","ex":"f(x)=x的傅里叶系数。","app":"级数展开。","note":"区间[-π,π]。"},
      {"name":"收敛定理","formula":"狄利克雷条件","explain":"满足条件的函数傅里叶级数收敛。","deriv":"狄利克雷积分。","ex":"连续点收敛于f(x)。","app":"级数收敛性。","note":"间断点收敛于平均值。"},
    ]},
    {"name":"2.2 傅里叶变换","color":"#c2410c","topics":[
      {"name":"傅里叶变换","formula":"\\hat{f}(k)=\\int_{-\\infty}^\\infty f(x)e^{-ikx}dx","explain":"非周期函数的频率分解。","deriv":"周期趋于无穷。","ex":"e^{-ax²}的傅里叶变换为√(π/a)e^{-k²/4a}。","app":"信号处理、PDE。","note":"逆变换含1/(2π)。"},
      {"name":"卷积定理","formula":"\\mathcal{F}\\{f*g\\}=\\hat{f}\\hat{g}","explain":"卷积的变换等于变换的乘积。","deriv":"交换积分顺序。","ex":"用卷积定理解微分方程。","app":"信号处理。","note":"时域卷积↔频域乘积。"},
      {"name":"帕塞瓦尔定理","formula":"\\int|f|^2dx=\\frac1{2\\pi}\\int|\\hat{f}|^2dk","explain":"能量守恒。","deriv":"由卷积定理。","ex":"信号能量在时域频域相等。","app":"能量计算。","note":"普朗歇尔定理。"},
    ]},
  ]},
  {"ch":"第三章","title":"偏微分方程","en":"PARTIAL DIFFERENTIAL EQUATIONS","sub":"分离变量与格林函数","sections":[
    {"name":"3.1 分离变量法","color":"#2563eb","topics":[
      {"name":"分离变量","formula":"u(x,t)=X(x)T(t)","explain":"将PDE化为ODE。","deriv":"代入PDE分离变量。","ex":"热方程分离为X''+λX=0,T'+λa²T=0。","app":"求解PDE。","note":"需方程与边界齐次。"},
      {"name":"波动方程","formula":"u_{tt}=a^2u_{xx}","explain":"一维波动方程。","deriv":"达朗贝尔解。","ex":"弦振动u(x,t)=f(x-at)+g(x+at)。","app":"波传播。","note":"通解为左右行波。"},
      {"name":"热方程","formula":"u_t=a^2u_{xx}","explain":"扩散方程。","deriv":"分离变量。","ex":"有界杆热传导。","app":"热传导、扩散。","note":"解趋于平均。"},
      {"name":"拉普拉斯方程","formula":"\\nabla^2u=0","explain":"调和方程。","deriv":"无外源稳态。","ex":"圆内狄利克雷问题泊松积分。","app":"静电势、稳态温度。","note":"解满足平均值性质。"},
      {"name":"本征值问题","formula":"X''+\\lambda X=0","explain":"施图姆-刘维尔问题。","deriv":"边界条件定本征值。","ex":"X(0)=X(L)=0得λ=(nπ/L)²。","app":"分离变量基础。","note":"本征函数正交。"},
      {"name":"格林函数","formula":"LG(x,\\xi)=\\delta(x-\\xi)","explain":"点源响应。","deriv":"广义函数。","ex":"-ΔG=δ的基本解。","app":"PDE求解。","note":"叠加格林函数得解。"},
    ]},
  ]},
  {"ch":"第四章","title":"特殊函数与积分变换","en":"SPECIAL FUNCTIONS & TRANSFORMS","sub":"球谐、拉普拉斯变换","sections":[
    {"name":"4.1 特殊函数","color":"#7c3aed","topics":[
      {"name":"贝塞尔函数","formula":"x^2y''+xy'+(x^2-\\nu^2)y=0","explain":"贝塞尔方程的解。","deriv":"分离变量柱坐标。","ex":"J₀(x)零阶贝塞尔函数。","app":"柱面波、振动。","note":"Jₙ,Nₙ,Hₙ。"},
      {"name":"勒让德多项式","formula":"(1-x^2)y''-2xy'+l(l+1)y=0","explain":"勒让德方程多项式解。","deriv":"球坐标分离变量。","ex":"P₀=1,P₁=x,P₂=(3x²-1)/2。","app":"球对称问题。","note":"正交性∫PₗPₘ=2δₗₘ/(2l+1)。"},
      {"name":"球谐函数","formula":"Y_l^m(\\theta,\\phi)","explain":"球面上的正交基。","deriv":"角向方程解。","ex":"Y₀⁰=1/√(4π)。","app":"量子力学、电磁。","note":"l≥|m|。"},
    ]},
    {"name":"4.2 拉普拉斯变换","color":"#0f766e","topics":[
      {"name":"拉普拉斯变换","formula":"F(s)=\\int_0^\\infty f(t)e^{-st}dt","explain":"单边积分变换。","deriv":"定义。","ex":"L{1}=1/s,L{t}=1/s²。","app":"ODE求解。","note":"Re(s)>收敛横坐标。"},
      {"name":"拉普拉斯变换性质","formula":"\\mathcal{L}\\{f'\\}=sF(s)-f(0)","explain":"微分变为乘s。","deriv":"分部积分。","ex":"L{f''}=s²F-sf(0)-f'(0)。","app":"化ODE为代数方程。","note":"需初值。"},
      {"name":"卷积与逆变换","formula":"\\mathcal{L}\\{f*g\\}=F(s)G(s)","explain":"时域卷积↔频域乘积。","deriv":"交换积分。","ex":"用卷积定理求逆变换。","app":"解非齐次ODE。","note":"留数法求逆。"},
    ]},
  ]},
  {"ch":"第五章","title":"变分法","en":"CALCULUS OF VARIATIONS","sub":"泛函极值","sections":[
    {"name":"5.1 变分原理","color":"#c2410c","topics":[
      {"name":"泛函与变分","formula":"\\delta J=0","explain":"泛函取极值的条件。","deriv":"类比函数极值。","ex":"最速降线问题。","app":"最小作用量原理。","note":"变分δJ为零。"},
      {"name":"欧拉-拉格朗日方程","formula":"\\frac{\\partial F}{\\partial y}-\\frac{d}{dt}\\frac{\\partial F}{\\partial y'}=0","explain":"泛函J=∫Fdt极值的必要条件。","deriv":"分部积分变分。","ex":"由拉氏量得运动方程。","app":"力学、场论。","note":"变分法核心方程。"},
      {"name":"最小作用量原理","formula":"\\delta S=0, S=\\int L dt","explain":"真实运动使作用量取极值。","deriv":"变分原理。","ex":"自由粒子L=T。","app":"理论力学。","note":"哈密顿原理。"},
    ]},
  ]},
]

# ===================== 特殊函数 special-functions =====================
SPECIAL_FUNCTIONS = [
  {"ch":"第一章","title":"伽马函数与贝塔函数","en":"GAMMA & BETA FUNCTIONS","sub":"阶乘推广","sections":[
    {"name":"1.1 伽马函数","color":"#2563eb","topics":[
      {"name":"伽马函数定义","formula":"\\Gamma(z)=\\int_0^\\infty t^{z-1}e^{-t}dt","explain":"阶乘的解析延拓。","deriv":"欧拉积分。","ex":"Γ(n+1)=n!。","app":"阶乘推广。","note":"Re(z)>0。"},
      {"name":"伽马函数性质","formula":"\\Gamma(z+1)=z\\Gamma(z)","explain":"递推关系。","deriv":"分部积分。","ex":"Γ(1/2)=√π。","app":"特殊函数基础。","note":"Γ(n+1)=n!。"},
      {"name":"欧拉反射公式","formula":"\\Gamma(z)\\Gamma(1-z)=\\frac{\\pi}{\\sin\\pi z}","explain":"互补参数关系。","deriv":"围道积分。","ex":"Γ(1/2)²=π。","app":"计算特殊值。","note":"z非整数。"},
      {"name":"斯特林公式","formula":"\\Gamma(z)\\sim\\sqrt{2\\pi}z^{z-1/2}e^{-z}","explain":"大z渐近展开。","deriv":"拉普拉斯方法。","ex":"n!≈√(2πn)(n/e)ⁿ。","app":"阶乘近似。","note":"z→∞。"},
    ]},
    {"name":"1.2 贝塔函数","color":"#7c3aed","topics":[
      {"name":"贝塔函数定义","formula":"B(p,q)=\\int_0^1 t^{p-1}(1-t)^{q-1}dt","explain":"第一类欧拉积分。","deriv":"定义。","ex":"B(1,1)=1。","app":"积分计算。","note":"Re(p),Re(q)>0。"},
      {"name":"贝塔与伽马关系","formula":"B(p,q)=\\frac{\\Gamma(p)\\Gamma(q)}{\\Gamma(p+q)}","explain":"贝塔函数用伽马表示。","deriv":"二重积分变换。","ex":"B(1/2,1/2)=π。","app":"贝塔函数求值。","note":"重要恒等式。"},
    ]},
  ]},
  {"ch":"第二章","title":"贝塞尔函数","en":"BESSEL FUNCTIONS","sub":"柱函数","sections":[
    {"name":"2.1 贝塞尔方程","color":"#0f766e","topics":[
      {"name":"贝塞尔方程","formula":"x^2y''+xy'+(x^2-\\nu^2)y=0","explain":"二阶变系数ODE。","deriv":"柱坐标分离变量。","ex":"圆形膜振动。","app":"柱对称问题。","note":"ν为阶。"},
      {"name":"第一类贝塞尔函数","formula":"J_\\nu(x)=\\sum_{m=0}^\\infty\\frac{(-1)^m}{m!\\Gamma(m+\\nu+1)}(\\frac{x}{2})^{2m+\\nu}","explain":"贝塞尔方程的正则解。","deriv":"幂级数解。","ex":"J₀(0)=1。","app":"柱面波。","note":"收敛于全平面。"},
      {"name":"贝塞尔函数递推","formula":"J_{\\nu-1}+J_{\\nu+1}=\\frac{2\\nu}{x}J_\\nu","explain":"相邻阶关系。","deriv":"级数比较。","ex":"J₁'=J₀-J₁/x。","app":"积分计算。","note":"多组递推关系。"},
      {"name":"贝塞尔函数零点","formula":"J_\\nu(x)=0的根","explain":"用于边界条件。","deriv":"数值或查表。","ex":"J₀的零点2.405,5.520,...。","app":"本征值问题。","note":"无穷多个正零点。"},
    ]},
  ]},
  {"ch":"第三章","title":"勒让德函数与球谐函数","en":"LEGENDRE & SPHERICAL HARMONICS","sub":"球函数","sections":[
    {"name":"3.1 勒让德多项式","color":"#c2410c","topics":[
      {"name":"勒让德方程","formula":"(1-x^2)y''-2xy'+l(l+1)y=0","explain":"l为非负整数时有多项式解。","deriv":"球坐标分离变量。","ex":"l=0时y=常数。","app":"球对称。","note":"l(l+1)为本征值。"},
      {"name":"罗德里格斯公式","formula":"P_l(x)=\\frac{1}{2^l l!}\\frac{d^l}{dx^l}(x^2-1)^l","explain":"勒让德多项式表达式。","deriv":"幂级数整理。","ex":"P₂=(3x²-1)/2。","app":"计算Pₗ。","note":"l次多项式。"},
      {"name":"勒让德正交性","formula":"\\int_{-1}^1 P_l P_m dx=\\frac{2}{2l+1}\\delta_{lm}","explain":"在[-1,1]上正交。","deriv":"施图姆-刘维尔。","ex":"展开f(x)为Pₗ级数。","app":"勒让德级数。","note":"权函数为1。"},
    ]},
    {"name":"3.2 球谐函数","color":"#2563eb","topics":[
      {"name":"球谐函数定义","formula":"Y_l^m(\\theta,\\phi)=N_{lm}P_l^m(\\cos\\theta)e^{im\\phi}","explain":"球面上的正交完备基。","deriv":"角向方程解。","ex":"Y₀⁰=1/√(4π)。","app":"角动量、辐射。","note":"-l≤m≤l。"},
      {"name":"球谐正交性","formula":"\\int Y_l^m Y_{l'}^{m'*}d\\Omega=\\delta_{ll'}\\delta_{mm'}","explain":"单位球面上正交归一。","deriv":"Pₗᵐ正交与e^{imφ}正交。","ex":"展开球面上函数。","app":"多极展开。","note":"dΩ=sinθdθdφ。"},
      {"name":"加法定理","formula":"P_l(\\cos\\gamma)=\\frac{4\\pi}{2l+1}\\sum_m Y_l^m(\\theta_1,\\phi_1)Y_l^{m*}(\\theta_2,\\phi_2)","explain":"两方向夹角的勒让德多项式。","deriv":"旋转不变性。","ex":"1/|r₁-r₂|展开。","app":"多极展开、格林函数。","note":"γ为两方向夹角。"},
    ]},
  ]},
  {"ch":"第四章","title":"超几何函数与合流超几何","en":"HYPERGEOMETRIC FUNCTIONS","sub":"广义超几何","sections":[
    {"name":"4.1 超几何函数","color":"#7c3aed","topics":[
      {"name":"超几何方程","formula":"x(1-x)y''+[c-(a+b+1)x]y'-aby=0","explain":"含三个参数的二阶ODE。","deriv":"一般化。","ex":"许多特殊函数为其特例。","app":"统一特殊函数。","note":"有三个正则奇点。"},
      {"name":"超几何级数","formula":"F(a,b;c;x)=\\sum\\frac{(a)_n(b)_n}{(c)_n n!}x^n","explain":"超几何方程的解。","deriv":"幂级数解。","ex":"F(1,1;2;x)=-ln(1-x)/x。","app":"特殊函数统一。","note":"(a)ₙ为上升阶乘。"},
    ]},
  ]},
  {"ch":"第五章","title":"椭圆函数与其他","en":"ELLIPTIC FUNCTIONS","sub":"双周期函数","sections":[
    {"name":"5.1 椭圆函数","color":"#0f766e","topics":[
      {"name":"椭圆积分","formula":"\\int R(x,\\sqrt{P(x)})dx","explain":"含四次多项式平方根的积分。","deriv":"定义。","ex":"第一类椭圆积分。","app":"摆周期、椭圆弧长。","note":"不能用初等函数表示。"},
      {"name":"椭圆函数","formula":"双周期亚纯函数","explain":"椭圆积分的反函数。","deriv":"定义。","ex":"雅可比椭圆函数sn,cn,dn。","app":"非线性振动。","note":"有两个基本周期。"},
    ]},
  ]},
]

# ===================== 矢量分析 vector-analysis =====================
VECTOR_ANALYSIS = [
  {"ch":"第一章","title":"矢量代数与微分","en":"VECTOR ALGEBRA & CALCULUS","sub":"梯度散度旋度","sections":[
    {"name":"1.1 矢量代数","color":"#2563eb","topics":[
      {"name":"矢量内积","formula":"\\boldsymbol{a}\\cdot\\boldsymbol{b}=|a||b|\\cos\\theta","explain":"点积为标量。","deriv":"投影定义。","ex":"a·b=0则垂直。","app":"夹角、投影。","note":"交换律。"},
      {"name":"矢量叉积","formula":"\\boldsymbol{a}\\times\\boldsymbol{b}","explain":"叉积为矢量，垂直于a,b。","deriv":"行列式。","ex":"|a×b|=|a||b|sinθ。","app":"面积、法向量。","note":"反交换。"},
      {"name":"标量三重积","formula":"(\\boldsymbol{a}\\times\\boldsymbol{b})\\cdot\\boldsymbol{c}","explain":"平行六面体体积。","deriv":"行列式。","ex":"混合积为零则共面。","app":"体积。","note":"轮换不变。"},
      {"name":"矢量三重积","formula":"\\boldsymbol{a}\\times(\\boldsymbol{b}\\times\\boldsymbol{c})=\\boldsymbol{b}(a\\cdot c)-\\boldsymbol{c}(a\\cdot b)","explain":"bac-cab公式。","deriv":"分量展开。","ex":"化简矢量表达式。","app":"矢量恒等式。","note":"注意顺序。"},
    ]},
    {"name":"1.2 矢量微分","color":"#7c3aed","topics":[
      {"name":"梯度","formula":"\\nabla\\phi=(\\partial_x\\phi,\\partial_y\\phi,\\partial_z\\phi)","explain":"标量场的方向导数最大值方向。","deriv":"方向导数公式。","ex":"∇r=r̂。","app":"力场、等值面法向。","note":"梯度垂直于等值面。"},
      {"name":"散度","formula":"\\nabla\\cdot\\boldsymbol{F}=\\partial_xF_x+\\partial_yF_y+\\partial_zF_z","explain":"矢量场的源强度。","deriv":"通量体密度。","ex":"∇·r=3。","app":"流体源汇、电荷。","note":"散度为0无源。"},
      {"name":"旋度","formula":"\\nabla\\times\\boldsymbol{F}","explain":"矢量场的涡旋强度。","deriv":"环量面密度。","ex":"∇×(ω×r)=2ω。","app":"涡旋、电流。","note":"旋度为0有势。"},
      {"name":"拉普拉斯算子","formula":"\\nabla^2=\\partial_x^2+\\partial_y^2+\\partial_z^2","explain":"梯度的散度。","deriv":"∇·∇。","ex":"∇²r²=6。","app":"拉普拉斯方程。","note":"标量场的二阶微分。"},
    ]},
  ]},
  {"ch":"第二章","title":"积分定理","en":"INTEGRAL THEOREMS","sub":"高斯、斯托克斯","sections":[
    {"name":"2.1 高斯定理","color":"#0f766e","topics":[
      {"name":"高斯散度定理","formula":"\\oint_S\\boldsymbol{F}\\cdot d\\boldsymbol{S}=\\int_V\\nabla\\cdot\\boldsymbol{F}dV","explain":"面积分等于体积分。","deriv":"散度定义积分。","ex":"电场高斯定律。","app":"通量计算。","note":"S为V的边界。"},
      {"name":"格林第一公式","formula":"\\int_V(\\phi\\nabla^2\\psi+\\nabla\\phi\\cdot\\nabla\\psi)dV=\\oint_S\\phi\\nabla\\psi\\cdot dS","explain":"散度定理应用。","deriv":"令F=φ∇ψ。","ex":"证明调和函数性质。","app":"PDE边值问题。","note":"格林恒等式。"},
    ]},
    {"name":"2.2 斯托克斯定理","color":"#c2410c","topics":[
      {"name":"斯托克斯定理","formula":"\\oint_C\\boldsymbol{F}\\cdot d\\boldsymbol{l}=\\int_S(\\nabla\\times\\boldsymbol{F})\\cdot d\\boldsymbol{S}","explain":"线积分等于面积分。","deriv":"旋度定义积分。","ex":"安培环路定律。","app":"环量计算。","note":"C为S的边界。"},
      {"name":"格林公式","formula":"\\oint_C(Pdx+Qdy)=\\iint_D(\\partial_xQ-\\partial_yP)dxdy","explain":"平面斯托克斯。","deriv":"二维特例。","ex":"计算平面线积分。","app":"面积公式。","note":"C正向。"},
    ]},
  ]},
  {"ch":"第三章","title":"曲线坐标","en":"CURVILINEAR COORDINATES","sub":"正交曲线坐标","sections":[
    {"name":"3.1 正交曲线坐标","color":"#2563eb","topics":[
      {"name":"坐标变换","formula":"ds^2=h_1^2du_1^2+h_2^2du_2^2+h_3^2du_3^2","explain":"拉梅系数hᵢ。","deriv":"度量张量。","ex":"柱坐标ds²=dρ²+ρ²dφ²+dz²。","app":"曲线坐标。","note":"hᵢ为拉梅系数。"},
      {"name":"柱坐标","formula":"x=\\rho\\cos\\phi, y=\\rho\\sin\\phi, z=z","explain":"柱面坐标。","deriv":"变换。","ex":"轴对称问题。","app":"柱对称。","note":"h₁=1,h₂=ρ,h₃=1。"},
      {"name":"球坐标","formula":"x=r\\sin\\theta\\cos\\phi, y=r\\sin\\theta\\sin\\phi, z=r\\cos\\theta","explain":"球面坐标。","deriv":"变换。","ex":"中心力场。","app":"球对称。","note":"h₁=1,h₂=r,h₃=r sinθ。"},
      {"name":"曲线坐标梯度","formula":"\\nabla\\phi=\\sum\\frac{1}{h_i}\\frac{\\partial\\phi}{\\partial u_i}\\boldsymbol{e}_i","explain":"曲线坐标中的梯度。","deriv":"基矢量归一化。","ex":"球坐标梯度。","app":"曲线坐标微分。","note":"含拉梅系数倒数。"},
    ]},
  ]},
]

print("math methods loaded")

# ===================== 理论力学 theoretical-mechanics =====================
THEORETICAL_MECHANICS = [
  {"ch":"第一章","title":"质点力学","en":"PARTICLE MECHANICS","sub":"牛顿定律与运动","sections":[
    {"name":"1.1 牛顿运动定律","color":"#2563eb","topics":[
      {"name":"牛顿第一定律","formula":"\\sum F=0\\Rightarrow v=\\text{常数}","explain":"惯性定律，物体保持静止或匀速直线运动。","deriv":"伽利略惯性实验。","ex":"冰面上物体近似匀速。","app":"惯性系定义。","note":"又称惯性定律。"},
      {"name":"牛顿第二定律","formula":"F=ma","explain":"力等于质量乘加速度。","deriv":"动量对时间的导数。","ex":"1kg物体受10N力加速10m/s²。","app":"动力学核心。","note":"F=dp/dt更普遍。"},
      {"name":"牛顿第三定律","formula":"F_{12}=-F_{21}","explain":"作用力与反作用力大小相等方向相反。","deriv":"实验事实。","ex":"火箭喷气反推。","app":"受力分析。","note":"作用于不同物体。"},
      {"name":"惯性系","formula":"牛顿定律成立的参考系","explain":"相对惯性系匀速运动的也是惯性系。","deriv":"伽利略变换。","ex":"地面近似惯性系。","app":"参考系选择。","note":"非惯性系需引入惯性力。"},
      {"name":"惯性力","formula":"F_{惯}=-ma","explain":"非惯性系中虚拟力。","deriv":"参考系变换。","ex":"转弯时乘客感受到离心力。","app":"非惯性系分析。","note":"无施力物体。"},
    ]},
    {"name":"1.2 运动学","color":"#7c3aed","topics":[
      {"name":"位移与速度","formula":"v=dr/dt","explain":"速度是位移对时间的导数。","deriv":"定义。","ex":"匀速直线运动v=s/t。","app":"运动描述。","note":"矢量。"},
      {"name":"加速度","formula":"a=dv/dt=d²r/dt²","explain":"加速度是速度对时间的导数。","deriv":"定义。","ex":"匀加速v=v₀+at。","app":"变速运动。","note":"矢量。"},
      {"name":"匀加速直线运动","formula":"x=x_0+v_0t+\\frac12 at^2","explain":"匀加速位移公式。","deriv":"积分a=常数。","ex":"自由落体h=½gt²。","app":"抛体、落体。","note":"v²-v₀²=2a(x-x₀)。"},
      {"name":"抛体运动","formula":"x=v_0\\cos\\theta\\cdot t, y=v_0\\sin\\theta\\cdot t-\\frac12 gt^2","explain":"水平匀速+竖直匀加速。","deriv":"运动分解。","ex":"射程R=v₀²sin2θ/g。","app":"弹道。","note":"忽略空气阻力。"},
      {"name":"圆周运动","formula":"a_n=v^2/r, a_t=dv/dt","explain":"向心加速度与切向加速度。","deriv":"极坐标求导。","ex":"匀速圆周a=v²/r。","app":"旋转运动。","note":"向心加速度指向圆心。"},
    ]},
  ]},
  {"ch":"第二章","title":"功与能","en":"WORK & ENERGY","sub":"功、动能、势能","sections":[
    {"name":"2.1 功与功率","color":"#0f766e","topics":[
      {"name":"功的定义","formula":"W=\\int\\boldsymbol{F}\\cdot d\\boldsymbol{r}","explain":"力沿路径的线积分。","deriv":"定义。","ex":"恒力W=Fscosθ。","app":"能量转换度量。","note":"标量，可正可负。"},
      {"name":"功率","formula":"P=dW/dt=F\\cdot v","explain":"单位时间做功。","deriv":"W对t求导。","ex":"汽车P=Fv。","app":"机械性能。","note":"单位瓦特。"},
      {"name":"动能定理","formula":"W_{合}=\\Delta E_k=\\frac12 mv_2^2-\\frac12 mv_1^2","explain":"合外力做功等于动能变化。","deriv":"由F=ma积分。","ex":"合外力做功增加动能。","app":"功能分析。","note":"标量定理。"},
    ]},
    {"name":"2.2 势能与守恒","color":"#c2410c","topics":[
      {"name":"保守力","formula":"\\oint\\boldsymbol{F}\\cdot d\\boldsymbol{r}=0","explain":"做功与路径无关的力。","deriv":"环路积分为零。","ex":"重力、弹力、库仑力。","app":"势能定义。","note":"保守力才有势能。"},
      {"name":"势能","formula":"E_p=-\\int\\boldsymbol{F}_{保}\\cdot d\\boldsymbol{r}","explain":"保守力对应的势能。","deriv":"由保守力定义。","ex":"重力势能mgh。","app":"能量守恒。","note":"势能零点可任选。"},
      {"name":"机械能守恒","formula":"E_k+E_p=\\text{常数}","explain":"只有保守力做功时机械能守恒。","deriv":"由动能定理。","ex":"自由落体动能增加势能减少。","app":"能量分析。","note":"非保守力做功改变机械能。"},
      {"name":"功能原理","formula":"W_{非保}=\\Delta E","explain":"非保守力做功等于机械能变化。","deriv":"动能定理+保守力势能。","ex":"摩擦力做功减少机械能。","app":"综合能量分析。","note":"W非保可正可负。"},
    ]},
  ]},
  {"ch":"第三章","title":"动量与角动量","en":"MOMENTUM & ANGULAR MOMENTUM","sub":"碰撞与转动","sections":[
    {"name":"3.1 动量","color":"#2563eb","topics":[
      {"name":"动量","formula":"p=mv","explain":"质量乘速度。","deriv":"定义。","ex":"运动物体的运动量。","app":"碰撞分析。","note":"矢量。"},
      {"name":"动量定理","formula":"I=\\Delta p","explain":"冲量等于动量变化。","deriv":"F=dp/dt积分。","ex":"撞击力F=Δp/Δt。","app":"冲击问题。","note":"I=∫Fdt。"},
      {"name":"动量守恒","formula":"\\sum p_i=\\text{常数}","explain":"系统不受外力时总动量守恒。","deriv":"牛顿第三定律。","ex":"碰撞前后总动量不变。","app":"碰撞、爆炸。","note":"矢量守恒。"},
      {"name":"碰撞分类","formula":"弹性/非弹性/完全非弹性","explain":"按动能是否守恒分类。","deriv":"动量守恒+能量分析。","ex":"完全非弹性碰后共速。","app":"碰撞问题。","note":"弹性碰撞动能守恒。"},
    ]},
    {"name":"3.2 角动量","color":"#7c3aed","topics":[
      {"name":"角动量","formula":"L=r\\times p","explain":"位矢叉乘动量。","deriv":"定义。","ex":"圆周运动L=mvr。","app":"转动运动。","note":"矢量，垂直于r和p。"},
      {"name":"角动量定理","formula":"M=dL/dt","explain":"合外力矩等于角动量变化率。","deriv":"由牛顿定律推导。","ex":"力矩使角动量变化。","app":"转动动力学。","note":"M=r×F。"},
      {"name":"角动量守恒","formula":"L=\\text{常数}","explain":"合外力矩为零时角动量守恒。","deriv":"M=0则dL/dt=0。","ex":"花样滑冰收臂加速。","app":"天体、陀螺。","note":"矢量守恒。"},
      {"name":"开普勒定律","formula":"T^2\\propto a^3","explain":"行星运动三定律。","deriv":"由万有引力。","ex":"地球公转周期1年。","app":"天体力学。","note":"第二定律即角动量守恒。"},
    ]},
  ]},
  {"ch":"第四章","title":"刚体力学","en":"RIGID BODY MECHANICS","sub":"转动与平衡","sections":[
    {"name":"4.1 刚体转动","color":"#0f766e","topics":[
      {"name":"刚体转动动能","formula":"E_k=\\frac12 I\\omega^2","explain":"转动惯量乘角速度平方。","deriv":"求和各质元动能。","ex":"圆盘I=½mR²。","app":"转动能量。","note":"I为转动惯量。"},
      {"name":"转动惯量","formula":"I=\\int r^2 dm","explain":"质量分布对转动的惯性。","deriv":"定义。","ex":"细杆I=mL²/12。","app":"转动难易。","note":"与转轴有关。"},
      {"name":"转动定律","formula":"M=I\\alpha","explain":"力矩等于转动惯量乘角加速度。","deriv":"由角动量定理。","ex":"M=Iα类比F=ma。","app":"转动动力学。","note":"α=dω/dt。"},
      {"name":"平行轴定理","formula":"I=I_c+md^2","explain":"绕平行于质心轴的转动惯量。","deriv":"坐标平移。","ex":"杆绕端点I=mL²/3。","app":"转动惯量计算。","note":"Ic为质心轴转动惯量。"},
    ]},
    {"name":"4.2 刚体平衡","color":"#c2410c","topics":[
      {"name":"刚体平衡条件","formula":"\\sum F=0, \\sum M=0","explain":"合外力为零且合外力矩为零。","deriv":"静止条件。","ex":"天平平衡。","app":"静力学。","note":"两个条件缺一不可。"},
      {"name":"质心","formula":"r_c=\\frac{\\sum m_i r_i}{\\sum m_i}","explain":"质量加权平均位置。","deriv":"定义。","ex":"均匀杆质心在中点。","app":"平动描述。","note":"质心运动定理。"},
    ]},
  ]},
  {"ch":"第五章","title":"分析力学","en":"ANALYTICAL MECHANICS","sub":"拉格朗日与哈密顿","sections":[
    {"name":"5.1 拉格朗日力学","color":"#2563eb","topics":[
      {"name":"广义坐标","formula":"q_i","explain":"描述系统位形的独立坐标。","deriv":"约束减少自由度。","ex":"单摆用θ描述。","app":"约束系统。","note":"数目等于自由度。"},
      {"name":"拉格朗日量","formula":"L=T-V","explain":"动能减势能。","deriv":"定义。","ex":"弹簧振子L=½mẋ²-½kx²。","app":"拉氏方程。","note":"L(q,\\dot q,t)。"},
      {"name":"拉格朗日方程","formula":"\\frac{d}{dt}\\frac{\\partial L}{\\partial \\dot q_i}-\\frac{\\partial L}{\\partial q_i}=0","explain":"欧拉-拉格朗日方程。","deriv":"哈密顿原理变分。","ex":"由L得运动方程。","app":"力学系统求解。","note":"分析力学核心。"},
      {"name":"循环坐标","formula":"\\partial L/\\partial q_i=0","explain":"L不显含的坐标。","deriv":"拉氏方程。","ex":"中心力场角坐标循环。","app":"守恒量识别。","note":"对应动量守恒。"},
    ]},
    {"name":"5.2 哈密顿力学","color":"#7c3aed","topics":[
      {"name":"正则动量","formula":"p_i=\\partial L/\\partial \\dot q_i","explain":"广义动量。","deriv":"勒让德变换。","ex":"p=L的广义速度偏导。","app":"哈密顿力学。","note":"不一定是机械动量。"},
      {"name":"哈密顿量","formula":"H=\\sum p_i\\dot q_i-L","explain":"勒让德变换到(p,q)。","deriv":"定义。","ex":"H=T+V（保守系）。","app":"哈密顿方程。","note":"H=E当L不显含t。"},
      {"name":"哈密顿方程","formula":"\\dot q_i=\\partial H/\\partial p_i, \\dot p_i=-\\partial H/\\partial q_i","explain":"正则方程。","deriv":"由勒让德变换。","ex":"弹簧振子哈密顿方程。","app":"力学与统计。","note":"2n个一阶方程。"},
      {"name":"泊松括号","formula":"\\{f,g\\}=\\sum(\\partial f/\\partial q_i\\partial g/\\partial p_i-\\partial f/\\partial p_i\\partial g/\\partial q_i)","explain":"正则变换的工具。","deriv":"定义。","ex":"{q,p}=1。","app":"量子化对应。","note":"运动方程df/dt={f,H}。"},
    ]},
  ]},
]

# ===================== 流体力学 fluid-mechanics =====================
FLUID_MECHANICS = [
  {"ch":"第一章","title":"流体静力学","en":"FLUID STATICS","sub":"压强与浮力","sections":[
    {"name":"1.1 流体压强","color":"#2563eb","topics":[
      {"name":"压强定义","formula":"p=F/A","explain":"单位面积受力。","deriv":"定义。","ex":"帕斯卡Pa=N/m²。","app":"流体力学基础。","note":"标量。"},
      {"name":"静止流体压强","formula":"p=p_0+\\rho gh","explain":"深度h处压强。","deriv":"受力平衡。","ex":"水下10m压强约2atm。","app":"潜水、液压。","note":"同一水平面压强相等。"},
      {"name":"帕斯卡原理","formula":"密闭流体压强等值传递","explain":"施加压强传递到各点。","deriv":"流体不可压缩。","ex":"液压千斤顶。","app":"液压机械。","note":"力的放大。"},
      {"name":"浮力","formula":"F_浮=\\rho gV","explain":"排开流体的重量。","deriv":"阿基米德原理。","ex":"木块漂浮。","app":"造船、浮体。","note":"方向竖直向上。"},
    ]},
  ]},
  {"ch":"第二章","title":"流体运动学","en":"FLUID KINEMATICS","sub":"流线与连续性","sections":[
    {"name":"2.1 流动描述","color":"#7c3aed","topics":[
      {"name":"流线与流管","formula":"流线切线平行于速度","explain":"某时刻速度场的切线。","deriv":"定义。","ex":"定常流动流线不变。","app":"流动可视化。","note":"流线不相交。"},
      {"name":"连续性方程","formula":"\\frac{\\partial\\rho}{\\partial t}+\\nabla\\cdot(\\rho\\boldsymbol{v})=0","explain":"质量守恒。","deriv":"质量守恒积分。","ex":"不可压缩∇·v=0。","app":"流量计算。","note":"质量守恒体现。"},
      {"name":"定常流动","formula":"\\partial/\\partial t=0","explain":"流场不随时间变化。","deriv":"定义。","ex":"恒定流量的管道流。","app":"简化分析。","note":"流线与迹线重合。"},
    ]},
  ]},
  {"ch":"第三章","title":"流体动力学","en":"FLUID DYNAMICS","sub":"伯努利方程与NS方程","sections":[
    {"name":"3.1 伯努利方程","color":"#0f766e","topics":[
      {"name":"伯努利方程","formula":"p+\\frac12\\rho v^2+\\rho gh=\\text{常数}","explain":"理想流体定常流动沿流线能量守恒。","deriv":"沿流线积分欧拉方程。","ex":"机翼升力、文丘里管。","app":"流速压强关系。","note":"理想、定常、不可压缩、无粘。"},
      {"name":"伯努利应用","formula":"v大则p小","explain":"流速大处压强小。","deriv":"伯努利方程。","ex":"喷雾器、飞机升力。","app":"工程应用。","note":"沿同一流线。"},
      {"name":"欧拉方程","formula":"\\rho(\\frac{\\partial\\boldsymbol v}{\\partial t}+(\\boldsymbol v\\cdot\\nabla)\\boldsymbol v)=-\\nabla p+\\rho\\boldsymbol g","explain":"无粘流体运动方程。","deriv":"牛顿第二定律。","ex":"理想流体。","app":"无粘流动。","note":"忽略粘性。"},
    ]},
    {"name":"3.2 粘性流动","color":"#c2410c","topics":[
      {"name":"牛顿粘性定律","formula":"\\tau=\\mu\\frac{du}{dy}","explain":"切应力与速度梯度成正比。","deriv":"实验。","ex":"层流切应力。","app":"粘性流动。","note":"μ为动力粘度。"},
      {"name":"雷诺数","formula":"Re=\\rho vL/\\mu","explain":"惯性力与粘性力之比。","deriv":"无量纲化。","ex":"Re<2300层流，>4000湍流。","app":"流动状态判断。","note":"临界雷诺数。"},
      {"name":"NS方程","formula":"\\rho(\\frac{\\partial\\boldsymbol v}{\\partial t}+(\\boldsymbol v\\cdot\\nabla)\\boldsymbol v)=-\\nabla p+\\mu\\nabla^2\\boldsymbol v+\\rho\\boldsymbol g","explain":"纳维-斯托克斯方程。","deriv":"含粘性项的欧拉方程。","ex":"粘性不可压缩流体。","app":"真实流体。","note":"千禧年难题之一。"},
      {"name":"边界层","formula":"\\delta\\sim\\sqrt{\\nu L/U}","explain":"壁面附近粘性主导薄层。","deriv":"普朗特理论。","ex":"平板边界层。","app":"阻力计算。","note":"δ随√L增长。"},
    ]},
  ]},
]

print("mechanics topics loaded")

# ===================== 固体力学 solid-mechanics =====================
SOLID_MECHANICS = [
  {"ch":"第一章","title":"应力与应变","en":"STRESS & STRAIN","sub":"应力张量与应变张量","sections":[
    {"name":"1.1 应力","color":"#2563eb","topics":[T("应力张量","σ_ij","应力是单位面积的内力，二阶张量。"),
      T("正应力与切应力","σ, τ","正应力垂直于面，切应力平行于面。"),
      T("主应力","σ_1,σ_2,σ_3","应力张量的特征值，切应力为零的方向。"),
      T("最大切应力","τ_max=(σ_1-σ_3)/2","最大与最小主应力之差的一半。"),
      T("应力莫尔圆","莫尔圆","图解应力状态的方法。"),
      T("平衡微分方程","∂σ_ij/∂x_j+f_i=0","微元体平衡条件。"),
      T("边界条件","σ_ij n_j=T_i","面力边界条件。"),
    ]},
    {"name":"1.2 应变","color":"#7c3aed","topics":[T("应变张量","ε_ij","描述变形的二阶张量。"),
      T("正应变与切应变","ε, γ","正应变是线元相对伸长，切应变是角度变化。"),
      T("主应变","ε_1,ε_2,ε_3","应变张量的特征值。"),
      T("几何方程","ε_ij=(u_i,j+u_j,i)/2","位移与应变的关系。"),
      T("体积应变","θ=ε_kk","单位体积变化。"),
      T("应变协调方程","ε_ij,kl+...","应变分量需满足的可积条件。"),
    ]},
  ]},
  {"ch":"第二章","title":"本构关系","en":"CONSTITUTIVE RELATIONS","sub":"胡克定律","sections":[
    {"name":"2.1 弹性本构","color":"#0f766e","topics":[T("胡克定律","σ=Eε","线弹性材料应力应变成正比。"),
      T("杨氏模量","E","正应力与正应变之比。"),
      T("泊松比","ν=-ε_lat/ε_long","横向应变与纵向应变之比的负值。"),
      T("剪切模量","G=E/[2(1+ν)]","切应力与切应变之比。"),
      T("体积模量","K=E/[3(1-2ν)]","平均应力与体积应变之比。"),
      T("拉梅常数","λ, μ","各向同性弹性的两个常数。"),
      T("广义胡克定律","σ_ij=λδ_ijε_kk+2με_ij","各向同性三维弹性本构。"),
    ]},
  ]},
  {"ch":"第三章","title":"梁的弯曲","en":"BEAM BENDING","sub":"梁的内力与变形","sections":[
    {"name":"3.1 梁的内力","color":"#c2410c","topics":[T("剪力与弯矩","V, M","梁横截面上的内力。"),
      T("微分关系","dM/dx=V, dV/dx=-q","内力与荷载的关系。"),
      T("弯曲正应力","σ=My/I_z","梁弯曲时横截面上的正应力。"),
      T("弯曲切应力","τ=VQ/(I_z b)","梁弯曲时的切应力。"),
      T("截面惯性矩","I_z","截面抗弯几何性质。"),
      T("梁的挠度","w(x)","梁轴线的弯曲变形。"),
      T("挠曲线微分方程","EIw''=M(x)","小变形下梁的弯曲方程。"),
    ]},
  ]},
  {"ch":"第四章","title":"强度理论与屈服","en":"STRENGTH THEORIES","sub":"屈服准则","sections":[
    {"name":"4.1 强度理论","color":"#2563eb","topics":[T("第一强度理论","最大拉应力理论","最大拉应力达到极限时断裂。"),
      T("第二强度理论","最大拉应变理论","最大拉应变达到极限时断裂。"),
      T("第三强度理论","τ_max=(σ_1-σ_3)/2≤σ_s/2","最大切应力屈服准则。"),
      T("第四强度理论","von Mises","形状改变比能屈服准则。"),
      T("von Mises等效应力","σ_e=√[(σ1-σ2)²+(σ2-σ3)²+(σ3-σ1)²]/√2","用于屈服判断。"),
      T("Tresca屈服准则","max切应力≤屈服切应力","六边形屈服面。"),
      T("安全系数","n=σ_s/σ","极限应力与工作应力之比。"),
    ]},
  ]},
  {"ch":"第五章","title":"压杆稳定与疲劳","en":"BUCKLING & FATIGUE","sub":"稳定性与疲劳","sections":[
    {"name":"5.1 稳定与疲劳","color":"#7c3aed","topics":[T("欧拉临界力","P_cr=π²EI/L²","压杆失稳的临界荷载。"),
      T("长度系数","μ","支座条件对临界力的影响。"),
      T("长细比","λ=μL/i","压杆柔度。"),
      T("疲劳破坏","交变应力下的低应力断裂","在交变应力下低于强度极限的破坏。"),
      T("S-N曲线","应力幅-循环次数曲线","疲劳寿命曲线。"),
      T("疲劳极限","σ_-1","无限寿命的最大应力幅。"),
      T("应力集中","K_t","截面突变处应力增大。"),
    ]},
  ]},
]

# ===================== 计算流体力学 cfd =====================
CFD = [
  {"ch":"第一章","title":"CFD基础","en":"CFD FUNDAMENTALS","sub":"控制方程离散化","sections":[
    {"name":"1.1 控制方程","color":"#2563eb","topics":[T("连续性方程","∂ρ/∂t+∇·(ρv)=0","质量守恒。"),
      T("动量方程","NS方程","动量守恒，含粘性项。"),
      T("能量方程","能量守恒","含热传导与粘性耗散。"),
      T("N-S方程无量纲化","Re, Ma, Pr","无量纲数表征流动。"),
    ]},
    {"name":"1.2 离散方法","color":"#7c3aed","topics":[T("有限差分法","FDM","用差商近似导数。"),
      T("有限体积法","FVM","对控制体积分离散。"),
      T("有限元法","FEM","变分形式离散。"),
      T("显式与隐式","时间推进方式","显式条件稳定，隐式无条件稳定。"),
      T("CFL条件","Courant数","显式格式稳定性条件。"),
    ]},
  ]},
  {"ch":"第二章","title":"湍流模型","en":"TURBULENCE MODELING","sub":"RANS与LES","sections":[
    {"name":"2.1 湍流模拟","color":"#0f766e","topics":[T("雷诺平均","RANS","对NS方程取时间平均。"),
      T("Boussinesq假设","μ_t","涡粘性假设。"),
      T("k-ε模型","k, ε两方程","最常用的工程湍流模型。"),
      T("k-ω模型","k, ω两方程","近壁处理更好。"),
      T("大涡模拟","LES","直接计算大尺度涡，模化小尺度。"),
      T("直接数值模拟","DNS","直接求解所有尺度，计算量极大。"),
      T("壁函数","壁面律","避免解析近壁网格。"),
    ]},
  ]},
  {"ch":"第三章","title":"网格与边界条件","en":"MESH & BC","sub":"网格生成","sections":[
    {"name":"3.1 网格","color":"#c2410c","topics":[T("结构化网格","规则网格","六面体为主，质量高。"),
      T("非结构化网格","任意多面体","适应复杂几何。"),
      T("网格质量","正交性、长宽比","影响计算精度与稳定性。"),
      T("边界层网格","近壁加密","解析边界层需y+~1。"),
      T("网格无关性","网格收敛性","结果不随网格加密变化。"),
    ]},
  ]},
]

print("solid & cfd loaded")

# ===================== 电磁学 electromagnetism =====================
ELECTROMAGNETISM = [
  {"ch":"第一章","title":"静电场","en":"ELECTROSTATICS","sub":"库仑定律与高斯定理","sections":[
    {"name":"1.1 电荷与电场","color":"#2563eb","topics":[T("库仑定律","F=kq1q2/r²","两点电荷间作用力。"),
      T("电场强度","E=F/q","单位正电荷受力。"),
      T("点电荷电场","E=kq/r²","点电荷的电场分布。"),
      T("电场叠加原理","E=ΣE_i","多电荷电场矢量叠加。"),
      T("电偶极子","p=ql","一对等量异号电荷。"),
      T("电场线","电场的几何描述","从正电荷出发到负电荷。"),
      T("均匀带电球壳","壳内E=0","球壳内部电场为零。"),
      T("无限大带电平面","E=σ/(2ε₀)","均匀电场。"),
    ]},
    {"name":"1.2 高斯定理","color":"#7c3aed","topics":[T("电通量","Φ_E=∮E·dS","电场穿过曲面的通量。"),
      T("高斯定理","∮E·dS=q_enclosed/ε₀","电通量正比于闭合面内电荷。"),
      T("高斯定理应用","对称电场计算","用对称性求电场。"),
      T("导体静电平衡","E内=0","导体内部电场为零。"),
      T("导体表面电场","E=σ/ε₀","垂直于导体表面。"),
      T("静电屏蔽","空腔屏蔽外电场","导体壳屏蔽外部电场。"),
    ]},
  ]},
  {"ch":"第二章","title":"电势与电容","en":"POTENTIAL & CAPACITANCE","sub":"电势、电势能、电容","sections":[
    {"name":"2.1 电势","color":"#0f766e","topics":[T("电势能","W=qU","电荷在电场中的势能。"),
      T("电势","U=W/q","单位正电荷电势能。"),
      T("电势差","U_AB=∫_A^B E·dl","电场力做功与电势差。"),
      T("点电荷电势","U=kq/r","取无穷远为零点。"),
      T("等势面","电势相等的面","与电场线垂直。"),
      T("电势与电场关系","E=-∇U","电场是电势的负梯度。"),
    ]},
    {"name":"2.2 电容","color":"#c2410c","topics":[T("电容定义","C=Q/U","储存电荷的能力。"),
      T("平行板电容","C=ε₀S/d","面积S间距d。"),
      T("电容器串联","1/C=Σ1/C_i","等效电容倒数相加。"),
      T("电容器并联","C=ΣC_i","电容相加。"),
      T("电场能量","W=½CU²","电容器储存的能量。"),
      T("能量密度","w=½εE²","单位体积电场能量。"),
      T("电介质","ε_r=ε/ε₀","相对介电常数。"),
    ]},
  ]},
  {"ch":"第三章","title":"稳恒电流","en":"STEADY CURRENT","sub":"欧姆定律与电路","sections":[
    {"name":"3.1 电流","color":"#2563eb","topics":[T("电流强度","I=dq/dt","单位时间通过的电量。"),
      T("电流密度","j=I/S","单位面积电流。"),
      T("欧姆定律","U=IR","电压电流电阻关系。"),
      T("电阻定律","R=ρL/S","电阻率长度面积。"),
      T("焦耳定律","P=I²R","电流热效应功率。"),
      T("电动势","ε","非静电力做功能力。"),
      T("基尔霍夫定律","KCL,KVL","节点电流与回路电压。"),
    ]},
  ]},
  {"ch":"第四章","title":"静磁场","en":"MAGNETOSTATICS","sub":"毕奥-萨伐尔定律","sections":[
    {"name":"4.1 磁场","color":"#7c3aed","topics":[T("磁感应强度","B","描述磁场强弱方向。"),
      T("毕奥-萨伐尔定律","dB=μ₀Idl×r̂/(4πr²)","电流元产生磁场。"),
      T("安培力","dF=Idl×B","电流在磁场中受力。"),
      T("洛伦兹力","F=qv×B","运动电荷在磁场中受力。"),
      T("载流导线磁场","B=μ₀I/(2πr)","长直导线磁场。"),
      T("螺线管磁场","B=μ₀nI","内部均匀磁场。"),
      T("磁矩","m=IS","载流线圈的磁矩。"),
    ]},
    {"name":"4.2 磁介质","color":"#0f766e","topics":[T("磁化强度","M","单位体积磁矩。"),
      T("磁场强度","H=B/μ₀-M","辅助矢量。"),
      T("磁导率","μ=B/H","介质磁性质。"),
      T("顺磁抗磁铁磁","三类磁介质","不同磁化特性。"),
      T("磁滞回线","B-H曲线","铁磁质磁化历史。"),
    ]},
  ]},
  {"ch":"第五章","title":"电磁感应","en":"ELECTROMAGNETIC INDUCTION","sub":"法拉第定律","sections":[
    {"name":"5.1 感应","color":"#c2410c","topics":[T("法拉第定律","ε=-dΦ/dt","感应电动势。"),
      T("楞次定律","阻碍磁通量变化","感应电流方向。"),
      T("动生电动势","ε=Blv","导体切割磁感线。"),
      T("感生电动势","变化磁场产生涡旋电场","感生电场。"),
      T("自感","L=Φ/I","线圈自身磁通量与电流比。"),
      T("互感","M=Φ₂₁/I₁","两线圈相互感应。"),
      T("磁场能量","W=½LI²","线圈储存磁能。"),
    ]},
  ]},
]

# ===================== 电动力学 electrodynamics =====================
ELECTRODYNAMICS = [
  {"ch":"第一章","title":"麦克斯韦方程组","en":"MAXWELL EQUATIONS","sub":"电磁场统一","sections":[
    {"name":"1.1 麦氏方程","color":"#2563eb","topics":[T("高斯电定律","∇·D=ρ","电场散度等于电荷密度。"),
      T("高斯磁定律","∇·B=0","无磁单极。"),
      T("法拉第定律","∇×E=-∂B/∂t","变化磁场产生电场。"),
      T("安培-麦克斯韦定律","∇×H=J+∂D/∂t","电流和变化电场产生磁场。"),
      T("位移电流","∂D/∂t","麦克斯韦引入。"),
      T("介质中的场","D=εE, B=μH","本构关系。"),
      T("真空光速","c=1/√(ε₀μ₀)","电磁波速度。"),
    ]},
  ]},
  {"ch":"第二章","title":"电磁波","en":"ELECTROMAGNETIC WAVES","sub":"波动方程","sections":[
    {"name":"2.1 平面波","color":"#7c3aed","topics":[T("波动方程","∇²E-με∂²E/∂t²=0","电磁波方程。"),
      T("平面波解","E=E₀e^{i(k·r-ωt)}","单色平面波。"),
      T("波阻抗","Z=E/H=√(μ/ε)","电场磁场振幅比。"),
      T("能流密度","S=E×H","坡印廷矢量。"),
      T("能流平均值","S=½E₀H₀","平均能流。"),
      T("横波性","k·E=0","电磁波是横波。"),
      T("偏振","E的振动方向","线偏、圆偏、椭圆偏。"),
    ]},
  ]},
  {"ch":"第三章","title":"电磁波传播","en":"WAVE PROPAGATION","sub":"反射折射","sections":[
    {"name":"3.1 界面现象","color":"#0f766e","topics":[T("边界条件","E_t连续, B_n连续","电磁场边界条件。"),
      T("反射定律","θ_i=θ_r","入射角等于反射角。"),
      T("折射定律","n₁sinθ₁=n₂sinθ₂","斯涅尔定律。"),
      T("菲涅尔公式","r,t系数","反射折射振幅比。"),
      T("布儒斯特角","tanθ_B=n₂/n₁","反射光全偏振。"),
      T("全反射","sinθ_c=n₂/n₁","光密到光疏。"),
      T("相速度","v_p=c/n","波传播速度。"),
    ]},
  ]},
  {"ch":"第四章","title":"辐射","en":"RADIATION","sub":"加速电荷辐射","sections":[
    {"name":"4.1 电磁辐射","color":"#c2410c","topics":[T("电偶极辐射","p̈","加速电偶极子辐射。"),
      T("辐射功率","P∝p̈²","拉莫尔公式推广。"),
      T("辐射方向图","sin²θ","偶极辐射角分布。"),
      T("天线","辐射或接收电磁波","半波天线等。"),
      T("近场与远场","感应场与辐射场","近场1/r³，远场1/r。"),
    ]},
  ]},
]

print("EM loaded")

# ===================== 电路 circuits =====================
CIRCUITS = [
  {"ch":"第一章","title":"电路基本定律","en":"CIRCUIT LAWS","sub":"欧姆定律、基尔霍夫","sections":[
    {"name":"1.1 基本概念","color":"#2563eb","topics":[T("电压","U","电位差。"),
      T("电流","I","电荷流动。"),
      T("电阻","R","阻碍电流。"),
      T("欧姆定律","U=IR","电压电流电阻关系。"),
      T("电功率","P=UI","电路功率。"),
      T("焦耳定律","Q=I²Rt","电热。"),
      T("串联电路","I相同, U=ΣU_i","串联分压。"),
      T("并联电路","U相同, I=ΣI_i","并联分流。"),
    ]},
    {"name":"1.2 基尔霍夫定律","color":"#7c3aed","topics":[T("KCL","ΣI_in=ΣI_out","节点电流守恒。"),
      T("KVL","ΣU=0","回路电压和为零。"),
      T("支路电流法","设支路电流列方程","基本解法。"),
      T("节点电压法","设节点电压列方程","节点法。"),
      T("网孔电流法","设网孔电流列方程","网孔法。"),
      T("叠加定理","各源单独作用叠加","线性电路。"),
      T("戴维南定理","等效电压源","二端网络等效。"),
      T("诺顿定理","等效电流源","戴维南对偶。"),
    ]},
  ]},
  {"ch":"第二章","title":"一阶二阶电路","en":"FIRST & SECOND ORDER","sub":"RC,RL,RLC","sections":[
    {"name":"2.1 一阶电路","color":"#0f766e","topics":[T("RC电路","τ=RC","电容充放电。"),
      T("RL电路","τ=L/R","电感电流变化。"),
      T("零输入响应","初始储能衰减","无激励响应。"),
      T("零状态响应","阶跃激励响应","初始为零。"),
      T("三要素法","f(t)=f(∞)+[f(0+)-f(∞)]e^{-t/τ}","一阶响应公式。"),
      T("全响应","零输入+零状态","完全响应。"),
    ]},
    {"name":"2.2 二阶电路","color":"#c2410c","topics":[T("RLC串联","LC振荡","二阶微分方程。"),
      T("过阻尼","α>ω₀","非振荡衰减。"),
      T("欠阻尼","α<ω₀","衰减振荡。"),
      T("临界阻尼","α=ω₀","临界状态。"),
      T("谐振","ω=ω₀","能量交换。"),
      T("品质因数Q","Q=ω₀L/R","储能与耗能比。"),
    ]},
  ]},
  {"ch":"第三章","title":"交流电路","en":"AC CIRCUITS","sub":"相量法","sections":[
    {"name":"3.1 正弦稳态","color":"#2563eb","topics":[T("正弦量","u=U_m sin(ωt+φ)","交流电。"),
      T("相量","U∠φ","复数表示。"),
      T("阻抗","Z=R+jX","复数阻抗。"),
      T("RL串联","Z=R+jωL","感性负载。"),
      T("RC串联","Z=R-j/(ωC)","容性负载。"),
      T("有功功率","P=UIcosφ","平均功率。"),
      T("无功功率","Q=UIsinφ","能量交换。"),
      T("功率因数","cosφ","有功与视在比。"),
    ]},
  ]},
]

# ===================== 模拟电子技术 analog-electronics =====================
ANALOG_ELECTRONICS = [
  {"ch":"第一章","title":"半导体器件","en":"SEMICONDUCTOR DEVICES","sub":"二极管、三极管","sections":[
    {"name":"1.1 二极管","color":"#2563eb","topics":[T("PN结","耗尽层","二极管核心。"),
      T("伏安特性","I=I₀(e^{U/U_T}-1)","二极管方程。"),
      T("导通压降","0.7V(Si)","硅管导通电压。"),
      T("整流","单向导电","交流变直流。"),
      T("稳压二极管","反向击穿区","稳压。"),
      T("限幅","利用导通特性","信号限幅。"),
      T("二极管电路","理想模型","简化分析。"),
    ]},
    {"name":"1.2 三极管","color":"#7c3aed","topics":[T("BJT结构","NPN/PNP","三层半导体。"),
      T("放大原理","Ic=βIb","电流放大。"),
      T("输入输出特性","曲线族","工作区域。"),
      T("工作区域","截止/放大/饱和","三种状态。"),
      T("共射放大","Au=-βRc/rbe","电压放大。"),
      T("静态工作点","Q点","直流偏置。"),
      T("微变等效","rbe模型","小信号分析。"),
    ]},
  ]},
  {"ch":"第二章","title":"放大电路","en":"AMPLIFIERS","sub":"各种组态","sections":[
    {"name":"2.1 单管放大","color":"#0f766e","topics":[T("共射极","反相放大","最常用。"),
      T("共集电极","电压跟随器","高输入低输出。"),
      T("共基极","电流跟随器","高频好。"),
      T("静态分析","直流通路","求Q点。"),
      T("动态分析","交流通路","求增益阻抗。"),
      T("工作点稳定","分压偏置","温度补偿。"),
    ]},
    {"name":"2.2 运算放大器","color":"#c2410c","topics":[T("理想运放","A→∞, Ri→∞","理想化。"),
      T("虚短虚断","u+=u-, i=0","理想条件。"),
      T("反相比例","Au=-Rf/R1","反相放大。"),
      T("同相比例","Au=1+Rf/R1","同相放大。"),
      T("电压跟随器","Au=1","缓冲。"),
      T("加法器","多输入相加","求和电路。"),
      T("积分器","输出积分","∫输入。"),
      T("微分器","输出微分","d输入/dt。"),
    ]},
  ]},
  {"ch":"第三章","title":"反馈与振荡","en":"FEEDBACK & OSCILLATION","sub":"负反馈","sections":[
    {"name":"3.1 反馈","color":"#2563eb","topics":[T("负反馈","稳定性能","改善性能。"),
      T("电压串联","电压反馈","稳定电压。"),
      T("反馈深度","1+AF","反馈强弱。"),
      T("增益稳定性","提高稳定性","负反馈作用。"),
      T("非线性失真","减小失真","改善线性。"),
      T("扩展带宽","展宽通频带","负反馈。"),
    ]},
  ]},
]

# ===================== 数字电子技术 digital-electronics =====================
DIGITAL_ELECTRONICS = [
  {"ch":"第一章","title":"逻辑代数","en":"LOGIC ALGEBRA","sub":"布尔代数","sections":[
    {"name":"1.1 数制与编码","color":"#2563eb","topics":[T("二进制","0,1","数字电路基础。"),
      T("十六进制","0-F","简写。"),
      T("BCD码","8421","十进制编码。"),
      T("格雷码","相邻一位变","减少错误。"),
      T("ASCII","字符编码","7位码。"),
    ]},
    {"name":"1.2 逻辑运算","color":"#7c3aed","topics":[T("与运算","Y=AB","全1出1。"),
      T("或运算","Y=A+B","有1出1。"),
      T("非运算","Y=Ā","取反。"),
      T("与非","Y=(AB)'","与后非。"),
      T("或非","Y=(A+B)'","或后非。"),
      T("异或","Y=A⊕B","不同出1。"),
      T("同或","Y=A⊙B","相同出1。"),
      T("德摩根定律","(AB)'=A'+B'","逻辑变换。"),
    ]},
  ]},
  {"ch":"第二章","title":"组合逻辑","en":"COMBINATIONAL LOGIC","sub":"门电路","sections":[
    {"name":"2.1 门电路","color":"#0f766e","topics":[T("与门","实现与逻辑","基本门。"),
      T("或门","实现或逻辑","基本门。"),
      T("非门","实现非逻辑","反相器。"),
      T("与非门","通用门","可实现所有逻辑。"),
      T("或非门","通用门","可实现所有逻辑。"),
      T("三态门","高阻态","总线应用。"),
      T("传输门","双向开关","CMOS。"),
    ]},
    {"name":"2.2 组合电路","color":"#c2410c","topics":[T("编码器","多入少出","编码。"),
      T("译码器","少入多出","译码。"),
      T("数据选择器","MUX","选通。"),
      T("加法器","半加全加","算术。"),
      T("比较器","大小比较","比较。"),
    ]},
  ]},
  {"ch":"第三章","title":"时序逻辑","en":"SEQUENTIAL LOGIC","sub":"触发器","sections":[
    {"name":"3.1 触发器","color":"#2563eb","topics":[T("RS触发器","置位复位","基本。"),
      T("D触发器","数据锁存","边沿触发。"),
      T("JK触发器","功能最全","全能。"),
      T("T触发器","翻转","计数。"),
      T("寄存器","寄存数据","并行。"),
      T("移位寄存器","移位","串行。"),
    ]},
    {"name":"3.2 计数器","color":"#7c3aed","topics":[T("异步计数器"," ripple","串行时钟。"),
      T("同步计数器","同时钟","并行。"),
      T("二进制计数器","2^n进制","基本。"),
      T("十进制计数器","BCD","常用。"),
      T("任意进制","反馈清零","N进制。"),
    ]},
  ]},
]

# ===================== 集成电路 integrated-circuits =====================
INTEGRATED_CIRCUITS = [
  {"ch":"第一章","title":"集成电路基础","en":"IC FUNDAMENTALS","sub":"MOS管","sections":[
    {"name":"1.1 MOS器件","color":"#2563eb","topics":[T("MOS结构","金属-氧化物-半导体","场效应。"),
      T("NMOS/PMOS","N沟道/P沟道","两种类型。"),
      T("阈值电压","Vth","开启电压。"),
      T("线性区","Vds<Vgs-Vth","电阻区。"),
      T("饱和区","Vds>Vgs-Vth","恒流区。"),
      T("跨导","gm=∂Id/∂Vgs","放大能力。"),
    ]},
    {"name":"1.2 CMOS","color":"#7c3aed","topics":[T("CMOS反相器","NMOS+PMOS","互补。"),
      T("CMOS优点","低功耗","静态功耗近零。"),
      T("传输特性","VTC","输入输出关系。"),
      T("噪声容限","V_NH,V_NL","抗干扰。"),
      T("延迟","tpd","开关速度。"),
      T("功耗","动态+静态","能量。"),
    ]},
  ]},
  {"ch":"第二章","title":"组合与时序IC","en":"COMB & SEQ IC","sub":"标准单元","sections":[
    {"name":"2.1 组合单元","color":"#0f766e","topics":[T("标准单元","库","设计复用。"),
      T("逻辑综合","RTL→门级","自动综合。"),
      T("布线","布局布线","物理实现。"),
    ]},
  ]},
]

print("electronics loaded")

# ===================== 热力学 thermodynamics =====================
THERMODYNAMICS = [
  {"ch":"第一章","title":"热力学基本概念","en":"BASIC CONCEPTS","sub":"温度、热平衡","sections":[
    {"name":"1.1 温度与热平衡","color":"#2563eb","topics":[T("热力学第零定律","热平衡","定义温度。"),
      T("温标","摄氏、开尔文","温度量度。"),
      T("理想气体温标","T=PV/(nR)","基准温标。"),
      T("物态方程","PV=nRT","理想气体。"),
      T("热力学系统","孤立/封闭/开放","系统分类。"),
      T("状态参量","P,V,T","描述平衡态。"),
      T("准静态过程","无限缓慢","可逆过程。"),
    ]},
    {"name":"1.2 内能与功","color":"#7c3aed","topics":[T("内能","U","系统内部能量。"),
      T("准静态功","W=∫PdV","体积功。"),
      T("热量","Q","能量传递。"),
      T("热容","C=dQ/dT","吸热能力。"),
      T("定容热容","Cv=(∂U/∂T)_V","等容。"),
      T("定压热容","Cp=(∂H/∂T)_P","等压。"),
    ]},
  ]},
  {"ch":"第二章","title":"热力学第一定律","en":"FIRST LAW","sub":"能量守恒","sections":[
    {"name":"2.1 第一定律","color":"#0f766e","topics":[T("第一定律","dU=dQ+dW","能量守恒。"),
      T("等容过程","W=0, Q=ΔU","体积不变。"),
      T("等压过程","Q=ΔH","压强不变。"),
      T("等温过程","ΔU=0","温度不变。"),
      T("绝热过程","Q=0","无热交换。"),
      T("多方过程","PV^n=C","一般过程。"),
      T("焓","H=U+PV","等压热函数。"),
    ]},
  ]},
  {"ch":"第三章","title":"热力学第二定律","en":"SECOND LAW","sub":"熵增原理","sections":[
    {"name":"3.1 第二定律","color":"#c2410c","topics":[T("开尔文表述","不可能单一热源做功","热二律。"),
      T("克劳修斯表述","热不能自发低温到高温","热二律。"),
      T("卡诺循环","两热源可逆循环","最高效率。"),
      T("卡诺效率","η=1-T₂/T₁","理想效率。"),
      T("熵","dS=dQ_rev/T","状态函数。"),
      T("熵增原理","ΔS≥0","孤立系统熵不减。"),
      T("可逆绝热","等熵过程","S不变。"),
      T("热力学温标","T∝Q","卡诺热机定义。"),
    ]},
    {"name":"3.2 热力学势","color":"#2563eb","topics":[T("自由能","F=U-TS","等温等容。"),
      T("吉布斯自由能","G=H-TS","等温等压。"),
      T("麦克斯韦关系","偏导关系","热力学势导出。"),
      T("化学势","μ=(∂G/∂n)","粒子变化趋势。"),
    ]},
  ]},
  {"ch":"第四章","title":"相变","en":"PHASE TRANSITIONS","sub":"气液固","sections":[
    {"name":"4.1 相变","color":"#7c3aed","topics":[T("一级相变","潜热、体积突变","气液相变。"),
      T("二级相变","无潜热","临界点。"),
      T("克拉珀龙方程","dP/dT=L/(TΔV)","相平衡曲线斜率。"),
      T("临界点","气液不分","临界温度。"),
      T("三相点","三相共存","唯一。"),
      T("相图","P-T图","相平衡。"),
    ]},
  ]},
]

# ===================== 统计物理 statistical-physics =====================
STATISTICAL_PHYSICS = [
  {"ch":"第一章","title":"统计物理基础","en":"STATISTICAL FOUNDATIONS","sub":"系综理论","sections":[
    {"name":"1.1 基本概念","color":"#2563eb","topics":[T("微观态","微观状态数","粒子状态。"),
      T("宏观态","宏观量","统计平均。"),
      T("等概率原理","等权假设","基本假设。"),
      T("玻尔兹曼熵","S=k lnΩ","熵与微观态数。"),
      T("配分函数","Z=Σe^{-βE}","统计核心。"),
      T("系综","系统集合","统计描述。"),
    ]},
    {"name":"1.2 系综","color":"#7c3aed","topics":[T("微正则系综","N,V,E固定","孤立系统。"),
      T("正则系综","N,V,T固定","与热源接触。"),
      T("巨正则系综","μ,V,T固定","粒子可交换。"),
      T("正则分布","ρ∝e^{-βE}","概率分布。"),
      T("巨正则分布","ρ∝e^{-β(E-μN)}","概率分布。"),
      T("热力学量","由配分函数求","统计平均。"),
    ]},
  ]},
  {"ch":"第二章","title":"玻尔兹曼统计","en":"BOLTZMANN STATISTICS","sub":"近独立粒子","sections":[
    {"name":"2.1 玻尔兹曼分布","color":"#0f766e","topics":[T("玻尔兹曼分布","n_i∝e^{-βε_i}","可分辨粒子。"),
      T("麦克斯韦速度分布","f(v)","速度分布。"),
      T("能量均分定理","½kT per自由度","经典。"),
      T("理想气体内能","U=½fNkT","由均分定理。"),
      T("理想气体压强","P=NkT/V","状态方程。"),
      T("热容量","Cv=½fNk","经典结果。"),
    ]},
  ]},
  {"ch":"第三章","title":"量子统计","en":"QUANTUM STATISTICS","sub":"玻色与费米","sections":[
    {"name":"3.1 量子分布","color":"#c2410c","topics":[T("玻色分布","n=1/(e^{β(ε-μ)}-1)","玻色子。"),
      T("费米分布","n=1/(e^{β(ε-μ)}+1)","费米子。"),
      T("玻色-爱因斯坦凝聚","BEC","低温玻色子聚集。"),
      T("费米能","ε_F","T=0费米面能量。"),
      T("普朗克公式","黑体辐射","玻色统计。"),
      T("德拜模型","晶格比热","声子。"),
      T("自由电子气","金属电子","费米统计。"),
    ]},
  ]},
]

# ===================== 光学 optics =====================
OPTICS = [
  {"ch":"第一章","title":"几何光学","en":"GEOMETRICAL OPTICS","sub":"光线","sections":[
    {"name":"1.1 基本定律","color":"#2563eb","topics":[T("光的直线传播","均匀介质","光线。"),
      T("反射定律","θ_i=θ_r","反射。"),
      T("折射定律","n₁sinθ₁=n₂sinθ₂","斯涅尔。"),
      T("全反射","sinθ_c=n₂/n₁","光密到光疏。"),
      T("费马原理","光程极值","最短时间。"),
      T("棱镜偏向角","δ","色散。"),
    ]},
    {"name":"1.2 透镜成像","color":"#7c3aed","topics":[T("薄透镜公式","1/u+1/v=1/f","成像。"),
      T("放大率","m=-v/u","横向放大。"),
      T("焦距","f","透镜参数。"),
      T("物像距","u,v","共轭。"),
      T("实像虚像","光线会聚/发散","成像性质。"),
    ]},
  ]},
  {"ch":"第二章","title":"波动光学","en":"WAVE OPTICS","sub":"干涉衍射","sections":[
    {"name":"2.1 干涉","color":"#0f766e","topics":[T("相干条件","频率相同位相差恒定","相干。"),
      T("杨氏双缝","Δx=λD/d","双缝干涉。"),
      T("薄膜干涉","等倾等厚","薄膜。"),
      T("牛顿环","同心圆环","薄膜等厚。"),
      T("迈克尔逊干涉仪","分振幅","精密测量。"),
      T("光程差","Δ=nΔr","相位差。"),
    ]},
    {"name":"2.2 衍射","color":"#c2410c","topics":[T("惠更斯-菲涅尔原理","子波叠加","衍射。"),
      T("单缝衍射","a sinθ=kλ","暗纹。"),
      T("圆孔衍射","艾里斑","分辨极限。"),
      T("光栅衍射","d sinθ=kλ","主极大。"),
      T("分辨本领","R=λ/Δλ","分辨率。"),
      T("夫琅禾费衍射","远场","平行光。"),
    ]},
  ]},
  {"ch":"第三章","title":"偏振","en":"POLARIZATION","sub":"光的偏振","sections":[
    {"name":"3.1 偏振","color":"#2563eb","topics":[T("线偏振","E振动固定","线偏。"),
      T("圆偏振","E旋转","圆偏。"),
      T("椭圆偏振","椭圆轨迹","椭圆偏。"),
      T("起偏器","自然光变线偏","偏振片。"),
      T("马吕斯定律","I=I₀cos²θ","偏振光强度。"),
      T("双折射","o光e光","各向异性。"),
      T("波片","λ/4,λ/2","相位延迟。"),
    ]},
  ]},
]

# ===================== 声学 acoustics =====================
ACOUSTICS = [
  {"ch":"第一章","title":"声学基础","en":"ACOUSTIC FUNDAMENTALS","sub":"声波","sections":[
    {"name":"1.1 声波","color":"#2563eb","topics":[T("声波","介质中弹性波","机械波。"),
      T("声速","c=√(γP/ρ)","空气中声速。"),
      T("频率","f","每秒振动次数。"),
      T("波长","λ=c/f","空间周期。"),
      T("声压","p","压强变化。"),
      T("声强","I","能流密度。"),
      T("声压级","L_p=20log(p/p_ref)","分贝。"),
      T("声强级","L_I=10log(I/I_ref)","分贝。"),
    ]},
    {"name":"1.2 波动方程","color":"#7c3aed","topics":[T("声学波动方程","∇²p-1/c²∂²p/∂t²=0","声波方程。"),
      T("平面波","p=Ae^{i(kx-ωt)}","解。"),
      T("球面波","p∝1/r","发散。"),
      T("波阻抗","Z=ρc","介质特性。"),
    ]},
  ]},
  {"ch":"第二章","title":"声传播","en":"SOUND PROPAGATION","sub":"反射折射","sections":[
    {"name":"2.1 传播","color":"#0f766e","topics":[T("声反射","界面反射","反射系数。"),
      T("声折射","折射率","折射定律。"),
      T("声吸收","α","衰减。"),
      T("声散射","障碍物","散射。"),
      T("衍射","绕过障碍物","衍射。"),
      T("多普勒效应","f'=f(c±v_o)/(c∓v_s)","频率变化。"),
    ]},
  ]},
]

print("thermal & optics loaded")

# ===================== 量子力学 quantum-mechanics =====================
QUANTUM_MECHANICS = [
  {"ch":"第一章","title":"量子力学基础","en":"QM FUNDAMENTALS","sub":"波函数与薛定谔方程","sections":[
    {"name":"1.1 波函数","color":"#2563eb","topics":[T("波函数","ψ(r,t)","描述微观粒子状态。"),
      T("概率密度","|ψ|²","粒子出现概率。"),
      T("归一化","∫|ψ|²dV=1","总概率为1。"),
      T("波函数性质","单值连续有限","标准条件。"),
      T("叠加原理","ψ=c₁ψ₁+c₂ψ₂","状态叠加。"),
    ]},
    {"name":"1.2 薛定谔方程","color":"#7c3aed","topics":[T("薛定谔方程","iℏ∂ψ/∂t=Ĥψ","基本方程。"),
      T("哈密顿算符","Ĥ=-ℏ²/(2m)∇²+V","能量算符。"),
      T("定态薛定谔方程","Ĥψ=Eψ","不含时。"),
      T("概率守恒","∂ρ/∂t+∇·j=0","连续性方程。"),
      T("势垒穿透","隧道效应","量子隧穿。"),
    ]},
  ]},
  {"ch":"第二章","title":"一维问题","en":"1D PROBLEMS","sub":"无限深势阱","sections":[
    {"name":"2.1 势阱","color":"#0f766e","topics":[T("无限深势阱","E_n=n²π²ℏ²/(2mL²)","离散能级。"),
      T("有限深势阱","束缚态","有限个能级。"),
      T("谐振子","E_n=(n+½)ℏω","等间距能级。"),
      T("势垒","透射反射","隧穿。"),
      T("δ势阱","束缚态","一维。"),
    ]},
  ]},
  {"ch":"第三章","title":"算符与表象","en":"OPERATORS & REPRESENTATIONS","sub":"量子力学形式","sections":[
    {"name":"3.1 算符","color":"#c2410c","topics":[T("力学量算符","可观测量","厄米算符。"),
      T("本征值方程","Âψ=aψ","本征态。"),
      T("对易子","[Â,B̂]=ÂB̂-B̂Â","可对易可观测量。"),
      T("不确定关系","ΔAΔB≥½|<[Â,B̂]>|","海森堡。"),
      T("坐标表象","ψ(x)","位置表象。"),
      T("动量表象","φ(p)","动量表象。"),
      T("希尔伯特空间","态空间","复矢量空间。"),
    ]},
  ]},
  {"ch":"第四章","title":"角动量","en":"ANGULAR MOMENTUM","sub":"轨道与自旋","sections":[
    {"name":"4.1 角动量","color":"#2563eb","topics":[T("轨道角动量","L̂=r̂×p̂","轨道。"),
      T("角动量本征值","L²=l(l+1)ℏ²","量子化。"),
      T("z分量","L_z=mℏ","磁量子数。"),
      T("自旋","S","内禀角动量。"),
      T("自旋1/2","电子自旋","泡利矩阵。"),
      T("泡利矩阵","σ_x,σ_y,σ_z","自旋算符。"),
      T("总角动量","J=L+S","耦合。"),
    ]},
  ]},
  {"ch":"第五章","title":"氢原子与微扰","en":"HYDROGEN & PERTURBATION","sub":"近似方法","sections":[
    {"name":"5.1 氢原子","color":"#7c3aed","topics":[T("氢原子能级","E_n=-13.6/n² eV","玻尔模型。"),
      T("主量子数","n","能级。"),
      T("角量子数","l","轨道形状。"),
      T("磁量子数","m","空间取向。"),
      T("波函数","ψ_nlm","球谐函数×径向。"),
    ]},
    {"name":"5.2 微扰论","color":"#0f766e","topics":[T("非简并微扰","一级修正","近似方法。"),
      T("简并微扰","简并子空间","需对角化。"),
      T("含时微扰","跃迁概率","费米黄金规则。"),
      T("变分法","试探波函数","基态能量上限。"),
    ]},
  ]},
]

# ===================== 原子物理 atomic-physics =====================
ATOMIC_PHYSICS = [
  {"ch":"第一章","title":"原子结构","en":"ATOMIC STRUCTURE","sub":"玻尔模型","sections":[
    {"name":"1.1 玻尔模型","color":"#2563eb","topics":[T("玻尔假设","定态、跃迁、角动量量子化","早期量子。"),
      T("氢原子光谱","巴尔末系","频率公式。"),
      T("里德伯公式","1/λ=R(1/n₁²-1/n₂²)","光谱线。"),
      T("玻尔半径","a₀=0.529Å","原子尺度。"),
      T("能级","E_n=-13.6/n² eV","离散。"),
    ]},
    {"name":"1.2 量子力学描述","color":"#7c3aed","topics":[T("量子数","n,l,m,m_s","描述电子态。"),
      T("电子组态","1s²2s²...","排布。"),
      T("泡利不相容","一个态最多两个电子","自旋相反。"),
      T("洪特规则","最大自旋多重度","基态。"),
      T("能量最低原理","从低到高填充","排布规则。"),
    ]},
  ]},
  {"ch":"第二章","title":"原子光谱","en":"ATOMIC SPECTRA","sub":"精细结构","sections":[
    {"name":"2.1 光谱","color":"#0f766e","topics":[T("碱金属光谱","主线系、锐线系、漫线系、基线系","四系。"),
      T("精细结构","自旋轨道耦合","能级分裂。"),
      T("塞曼效应","磁场中谱线分裂","正常/反常。"),
      T("斯塔克效应","电场中谱线分裂","电场。"),
      T("选择定则","Δl=±1, Δj=0,±1","跃迁规则。"),
    ]},
  ]},
]

# ===================== 核物理 nuclear-physics =====================
NUCLEAR_PHYSICS = [
  {"ch":"第一章","title":"原子核基本性质","en":"NUCLEAR PROPERTIES","sub":"核结构","sections":[
    {"name":"1.1 核性质","color":"#2563eb","topics":[T("原子核组成","质子+中子","核子。"),
      T("核电荷数","Z","质子数。"),
      T("质量数","A=Z+N","核子数。"),
      T("同位素","同Z不同A","同位素。"),
      T("核半径","R=R₀A^{1/3}","R₀≈1.2fm。"),
      T("核自旋","I","核总角动量。"),
      T("核磁矩","μ","磁性。"),
      T("结合能","B=Zm_pc²+Nm_nc²-Mc²","核稳定度。"),
      T("比结合能","B/A","平均每核子。"),
    ]},
    {"name":"1.2 核力","color":"#7c3aed","topics":[T("核力","强相互作用","短程吸引。"),
      T("核力性质","电荷无关、饱和","强作用。"),
      T("介子理论","π介子","汤川秀树。"),
      T("核模型","液滴、壳层","描述核。"),
    ]},
  ]},
  {"ch":"第二章","title":"核衰变","en":"NUCLEAR DECAY","sub":"放射性","sections":[
    {"name":"2.1 衰变","color":"#0f766e","topics":[T("α衰变","放出α粒子","氦核。"),
      T("β衰变","放出电子/正电子","弱作用。"),
      T("γ衰变","放出γ光子","电磁跃迁。"),
      T("衰变定律","N=N₀e^{-λt}","指数衰减。"),
      T("半衰期","T₁/₂=ln2/λ","半数衰变时间。"),
      T("平均寿命","τ=1/λ","平均生存时间。"),
    ]},
  ]},
  {"ch":"第三章","title":"核反应","en":"NUCLEAR REACTIONS","sub":"裂变聚变","sections":[
    {"name":"3.1 反应","color":"#c2410c","topics":[T("核反应","X+a→Y+b","轰击。"),
      T("反应能","Q","质量亏损。"),
      T("裂变","重核分裂","释放能量。"),
      T("聚变","轻核聚合","释放能量。"),
      T("链式反应","中子增殖","反应堆。"),
      T("临界质量","维持链式反应","最小质量。"),
    ]},
  ]},
]

# ===================== 实验物理 experimental-physics =====================
EXPERIMENTAL_PHYSICS = [
  {"ch":"第一章","title":"实验方法","en":"EXPERIMENTAL METHODS","sub":"测量与误差","sections":[
    {"name":"1.1 误差","color":"#2563eb","topics":[T("系统误差","恒定规律误差","可修正。"),
      T("偶然误差","随机波动","统计。"),
      T("绝对误差","Δx","测量值与真值差。"),
      T("相对误差","Δx/x","比值。"),
      T("标准偏差","σ","离散程度。"),
      T("不确定度","合成不确定度","测量可信度。"),
      T("有效数字","反映精度","位数。"),
    ]},
    {"name":"1.2 数据处理","color":"#7c3aed","topics":[T("最小二乘法","拟合直线","最佳拟合。"),
      T("线性回归","y=kx+b","参数估计。"),
      T("相关系数","r","线性程度。"),
      T("逐差法","等间隔数据","处理。"),
    ]},
  ]},
  {"ch":"第二章","title":"常用实验","en":"COMMON EXPERIMENTS","sub":"经典实验","sections":[
    {"name":"2.1 实验","color":"#0f766e","topics":[T("长度测量","游标卡尺、螺旋测微器","基本工具。"),
      T("密度测量","ρ=m/V","间接测量。"),
      T("重力加速度","单摆、自由落体","g测量。"),
      T("杨氏模量","拉伸法","弹性模量。"),
      T("比热容","混合法","热学量。"),
      T("电阻测量","伏安法、惠斯通电桥","电学。"),
    ]},
  ]},
]

print("quantum & nuclear loaded")

# ===================== 凝聚态物理 condensed-matter-physics =====================
CONDENSED_MATTER_PHYSICS = [
  {"ch":"第一章","title":"晶体结构","en":"CRYSTAL STRUCTURE","sub":"晶格","sections":[
    {"name":"1.1 晶格","color":"#2563eb","topics":[T("晶格","周期性排列","晶体结构。"),
      T("布拉菲格子","14种","基本格子。"),
      T("原胞","最小重复单元","初基原胞。"),
      T("晶胞","惯用原胞","对称性。"),
      T("晶面指数","密勒指数(hkl)","晶面表示。"),
      T("晶向指数","[uvw]","方向。"),
      T("倒格子","正格子傅里叶变换","k空间。"),
      T("布里渊区","倒格子Wigner-Seitz原胞","k空间区域。"),
    ]},
    {"name":"1.2 结合","color":"#7c3aed","topics":[T("离子键","正负离子吸引","NaCl。"),
      T("共价键","共用电子对","金刚石。"),
      T("金属键","自由电子","金属。"),
      T("范德瓦尔斯键","分子间力","惰性气体。"),
      T("氢键","氢原子桥","冰。"),
    ]},
  ]},
  {"ch":"第二章","title":"能带理论","en":"BAND THEORY","sub":"电子态","sections":[
    {"name":"2.1 能带","color":"#0f766e","topics":[T("布洛赫定理","ψ=e^{ik·r}u_k(r)","周期势。"),
      T("能带","允许能量区域","禁带分隔。"),
      T("禁带","不允许能量","带隙。"),
      T("近自由电子模型","弱周期势","微扰。"),
      T("紧束缚模型","原子轨道线性组合","LCAO。"),
      T("费米面","E=E_F等能面","k空间。"),
      T("态密度","单位能量态数","DOS。"),
    ]},
  ]},
  {"ch":"第三章","title":"晶格振动","en":"LATTICE VIBRATIONS","sub":"声子","sections":[
    {"name":"3.1 声子","color":"#c2410c","topics":[T("简谐近似","势能二次项","振动。"),
      T("声学支","ω∝k长波","声频支。"),
      T("光学支","高频支","光频支。"),
      T("声子","格波量子","玻色子。"),
      T("声子态密度","D(ω)","分布。"),
      T("德拜模型","连续介质","比热。"),
      T("爱因斯坦模型","单一频率","比热。"),
    ]},
  ]},
]

# ===================== 半导体物理 semiconductor-physics =====================
SEMICONDUCTOR_PHYSICS = [
  {"ch":"第一章","title":"半导体基础","en":"SEMICONDUCTOR BASICS","sub":"能带与载流子","sections":[
    {"name":"1.1 能带","color":"#2563eb","topics":[T("本征半导体","纯半导体","Si,Ge。"),
      T("导带价带","电子空穴","导电。"),
      T("禁带宽度","E_g","带隙。"),
      T("本征载流子浓度","n_i","热激发。"),
      T("费米能级","E_F","电子填充水平。"),
      T("施主杂质","N型","提供电子。"),
      T("受主杂质","P型","提供空穴。"),
      T("杂质电离","施主/受主电离","载流子。"),
    ]},
    {"name":"1.2 载流子","color":"#7c3aed","topics":[T("电子浓度","n","导带电子。"),
      T("空穴浓度","p","价带空穴。"),
      T("电中性条件","n+N_a=p+N_d","电荷平衡。"),
      T("迁移率","μ","载流子迁移能力。"),
      T("电导率","σ=nqμ_n+pqμ_p","导电能力。"),
      T("载流子寿命","τ","复合时间。"),
      T("扩散系数","D","扩散能力。"),
      T("爱因斯坦关系","D/μ=kT/q","联系。"),
    ]},
  ]},
  {"ch":"第二章","title":"PN结","en":"PN JUNCTION","sub":"二极管","sections":[
    {"name":"2.1 PN结","color":"#0f766e","topics":[T("PN结形成","扩散+漂移","空间电荷区。"),
      T("内建电场","耗尽区电场","阻止扩散。"),
      T("势垒高度","qV_D","接触电势。"),
      T("正向偏置","P正N负","导通。"),
      T("反向偏置","P负N正","截止。"),
      T("整流特性","单向导电","I-V曲线。"),
      T("肖克莱方程","I=I₀(e^{V/V_T}-1)","二极管方程。"),
    ]},
  ]},
]

# ===================== 半导体器件 semiconductor-devices =====================
SEMICONDUCTOR_DEVICES = [
  {"ch":"第一章","title":"双极型器件","en":"BIPOLAR DEVICES","sub":"BJT","sections":[
    {"name":"1.1 BJT","color":"#2563eb","topics":[T("BJT结构","NPN/PNP","三层两结。"),
      T("发射结正偏","放大条件","导通。"),
      T("集电结反偏","放大条件","收集。"),
      T("电流放大系数","β=Ic/Ib","电流增益。"),
      T("共射电流增益","h_FE","β。"),
      T("截止频率","f_T","高频特性。"),
      T("工作区域","截止/放大/饱和","三区域。"),
    ]},
  ]},
  {"ch":"第二章","title":"MOS器件","en":"MOS DEVICES","sub":"MOSFET","sections":[
    {"name":"2.1 MOSFET","color":"#7c3aed","topics":[T("MOSFET结构","源漏栅","场效应。"),
      T("增强型/耗尽型","Vth正负","两种。"),
      T("阈值电压","V_th","开启电压。"),
      T("线性区电流","I_D=μCox(W/L)[(Vgs-Vth)Vds-½Vds²]","非饱和。"),
      T("饱和区电流","I_D=½μCox(W/L)(Vgs-Vth)²","饱和。"),
      T("亚阈值摆幅","S","弱反型斜率。"),
      T("迁移率退化","高场效应","短沟道。"),
    ]},
  ]},
]

# ===================== 超导电性 superconductivity =====================
SUPERCONDUCTIVITY = [
  {"ch":"第一章","title":"超导电性基础","en":"SUPERCONDUCTIVITY","sub":"零电阻与迈斯纳","sections":[
    {"name":"1.1 基本性质","color":"#2563eb","topics":[T("零电阻","R=0","超导态。"),
      T("临界温度","T_c","转变温度。"),
      T("迈斯纳效应","B=0","完全抗磁。"),
      T("临界磁场","H_c","破坏超导。"),
      T("临界电流","I_c","破坏超导。"),
      T("第一类超导体","一个H_c","完全迈斯纳。"),
      T("第二类超导体","H_c1,H_c2","混合态。"),
      T("磁通量子","Φ₀=h/(2e)","量子化。"),
    ]},
    {"name":"1.2 理论","color":"#7c3aed","topics":[T("BCS理论","库珀对","超导微观。"),
      T("能隙","Δ","超导能隙。"),
      T("约瑟夫森效应","隧穿","SIS结。"),
      T("SQUID","超导量子干涉仪","磁强计。"),
      T("伦敦方程","超导电磁","唯象。"),
      T("金兹堡-朗道理论","GL方程","唯象。"),
    ]},
  ]},
]

# ===================== 等离子体物理 plasma-physics =====================
PLASMA_PHYSICS = [
  {"ch":"第一章","title":"等离子体基础","en":"PLASMA FUNDAMENTALS","sub":"第四态","sections":[
    {"name":"1.1 基本概念","color":"#2563eb","topics":[T("等离子体","电离气体","第四态。"),
      T("准中性","n_e≈n_i","宏观中性。"),
      T("德拜长度","λ_D","屏蔽尺度。"),
      T("等离子体频率","ω_p","集体振荡。"),
      T("碰撞频率","ν","粒子碰撞。"),
      T("温度","T_e,T_i","电子离子温度。"),
    ]},
    {"name":"1.2 运动","color":"#7c3aed","topics":[T("单粒子运动","E×B漂移","导引中心。"),
      T("回旋运动","ω_c=qB/m","拉莫尔回旋。"),
      T("磁镜","磁场反射","约束。"),
      T("绝热不变量","守恒量","缓变场。"),
    ]},
  ]},
]

print("condensed matter loaded")

# ===================== 狭义相对论 special-relativity =====================
SPECIAL_RELATIVITY = [
  {"ch":"第一章","title":"狭义相对论基础","en":"SPECIAL RELATIVITY","sub":"洛伦兹变换","sections":[
    {"name":"1.1 基本假设","color":"#2563eb","topics":[T("相对性原理","物理定律惯性系等价","公设1。"),
      T("光速不变","c恒定","公设2。"),
      T("惯性系","匀速运动参考系","牛顿第一定律。"),
      T("伽利略变换","经典变换","低速近似。"),
      T("洛伦兹变换","相对论变换","时空坐标。"),
      T("洛伦兹因子","γ=1/√(1-v²/c²)","膨胀因子。"),
    ]},
    {"name":"1.2 时空效应","color":"#7c3aed","topics":[T("时间膨胀","Δt=γΔτ","运动时钟变慢。"),
      T("长度收缩","L=L₀/γ","运动方向收缩。"),
      T("同时的相对性","同时依赖参考系","相对论核心。"),
      T("钟慢效应","双生子佯谬","时间膨胀。"),
      T("相对论速度合成","u=(u'+v)/(1+u'v/c²)","速度叠加。"),
    ]},
  ]},
  {"ch":"第二章","title":"相对论动力学","en":"RELATIVISTIC DYNAMICS","sub":"质能关系","sections":[
    {"name":"2.1 动量能量","color":"#0f766e","topics":[T("相对论动量","p=γmv","动量。"),
      T("相对论能量","E=γmc²","总能量。"),
      T("静能","E₀=mc²","质量即能量。"),
      T("动能","E_k=(γ-1)mc²","相对论动能。"),
      T("质能关系","E=mc²","著名公式。"),
      T("能量动量关系","E²=(pc)²+(mc²)²","不变量。"),
    ]},
  ]},
]

# ===================== 广义相对论 general-relativity =====================
GENERAL_RELATIVITY = [
  {"ch":"第一章","title":"广义相对论基础","en":"GENERAL RELATIVITY","sub":"等效原理","sections":[
    {"name":"1.1 等效原理","color":"#2563eb","topics":[T("等效原理","引力=加速度","基本原理。"),
      T("引力质量=惯性质量","相等","实验验证。"),
      T("弯曲时空","引力=几何","爱因斯坦。"),
      T("测地线","自由粒子路径","短程线。"),
      T("黎曼几何","弯曲空间数学","基础。"),
      T("度规张量","g_μν","时空度量。"),
    ]},
    {"name":"1.2 场方程","color":"#7c3aed","topics":[T("爱因斯坦场方程","G_μν=8πGT_μν/c⁴","引力场方程。"),
      T("时空曲率","R_μν","曲率张量。"),
      T("能量动量张量","T_μν","源。"),
      T("史瓦西解","球对称真空解","黑洞。"),
      T("史瓦西半径","r_s=2GM/c²","事件视界。"),
      T("光线偏折","引力透镜","实验验证。"),
    ]},
  ]},
]

# ===================== 宇宙学 cosmology =====================
COSMOLOGY = [
  {"ch":"第一章","title":"宇宙学基础","en":"COSMOLOGY","sub":"大爆炸","sections":[
    {"name":"1.1 宇宙模型","color":"#2563eb","topics":[T("宇宙学原理","均匀各向同性","基本假设。"),
      T("弗里德曼方程","宇宙演化","标准模型。"),
      T("哈勃定律","v=H₀d","宇宙膨胀。"),
      T("大爆炸","宇宙起源","标准模型。"),
      T("宇宙微波背景","CMB","2.7K辐射。"),
      T("宇宙年龄","~138亿年","时间。"),
      T("暗物质","不可见物质","引力证据。"),
      T("暗能量","加速膨胀","宇宙学常数。"),
    ]},
    {"name":"1.2 演化","color":"#7c3aed","topics":[T("暴胀","指数膨胀","解决视界平直问题。"),
      T("核合成","轻元素形成","大爆炸后。"),
      T("复合","中性原子","CMB产生。"),
      T("结构形成","引力不稳定性","星系形成。"),
      T("红移","z=λ/λ₀-1","宇宙学红移。"),
    ]},
  ]},
]

# ===================== 天体物理 astrophysics =====================
ASTROPHYSICS = [
  {"ch":"第一章","title":"恒星","en":"STARS","sub":"恒星结构演化","sections":[
    {"name":"1.1 恒星","color":"#2563eb","topics":[T("恒星结构","流体静力学平衡","内部。"),
      T("主序星","氢燃烧","稳定阶段。"),
      T("红巨星","氢耗尽膨胀","演化。"),
      T("白矮星","简并压支撑","恒星残骸。"),
      T("中子星","中子简并压","致密。"),
      T("黑洞","引力坍缩","奇点。"),
      T("赫罗图","H-R图","光度温度。"),
      T("质量下限","~0.08M☉","氢点火。"),
      T("钱德拉塞卡极限","1.4M☉","白矮星上限。"),
    ]},
    {"name":"1.2 天体","color":"#7c3aed","topics":[T("超新星","大质量恒星爆发","高能。"),
      T("脉冲星","旋转中子星","射电脉冲。"),
      T("类星体","活动星系核","高红移。"),
      T("星系","恒星集合","银河系。"),
      T("星团","引力束缚恒星","疏散/球状。"),
    ]},
  ]},
]

# ===================== 粒子物理 particle-physics =====================
PARTICLE_PHYSICS = [
  {"ch":"第一章","title":"基本粒子","en":"ELEMENTARY PARTICLES","sub":"标准模型","sections":[
    {"name":"1.1 粒子分类","color":"#2563eb","topics":[T("费米子","半整数自旋","物质粒子。"),
      T("玻色子","整数自旋","传递相互作用。"),
      T("夸克","u,d,c,s,t,b","六种。"),
      T("轻子","e,μ,τ,ν_e,ν_μ,ν_τ","六种。"),
      T("光子","γ","电磁作用。"),
      T("胶子","g","强作用。"),
      T("W,Z玻色子","弱作用","弱力。"),
      T("希格斯玻色子","H","质量起源。"),
    ]},
    {"name":"1.2 相互作用","color":"#7c3aed","topics":[T("电磁相互作用","光子传递","长程。"),
      T("弱相互作用","W/Z传递","短程。"),
      T("强相互作用","胶子传递","色荷。"),
      T("引力","引力子(假设)","最弱。"),
      T("色荷","夸克携带","三种色。"),
      T("味","夸克种类","六种味。"),
      T("代","三代粒子","费米子代。"),
    ]},
  ]},
  {"ch":"第二章","title":"标准模型","en":"STANDARD MODEL","sub":"规范理论","sections":[
    {"name":"2.1 模型","color":"#0f766e","topics":[T("标准模型","SU(3)×SU(2)×U(1)","规范群。"),
      T("规范对称","局域不变性","理论基础。"),
      T("希格斯机制","对称性自发破缺","质量。"),
      T("真空期望值","v≈246GeV","希格斯场。"),
      T("味混合","CKM矩阵","夸克混合。"),
      T("中微子振荡","PMNS矩阵","轻子混合。"),
    ]},
  ]},
]

# ===================== 量子电动力学 QED =====================
QUANTUM_ELECTRODYNAMICS = [
  {"ch":"第一章","title":"QED","en":"QED","sub":"量子场论","sections":[
    {"name":"1.1 量子化","color":"#2563eb","topics":[T("电磁场量子化","光子","量子化。"),
      T("电子场量子化","电子正电子","狄拉克场。"),
      T("相互作用","eψ̄γ^μψA_μ","顶点。"),
      T("费曼图","散射振幅图示","计算。"),
      T("微扰论","耦合常数展开","α≈1/137。"),
      T("重整化","消除发散","可重整。"),
    ]},
    {"name":"1.2 过程","color":"#7c3aed","topics":[T("康普顿散射","γe→γe","QED过程。"),
      T("正负电子湮灭","e+e-→γγ","湮灭。"),
      T("穆勒散射","e-e-→e-e-","电子散射。"),
      T("电子反常磁矩","g-2","高精度。"),
      T("兰姆移位","能级修正","量子效应。"),
    ]},
  ]},
]

print("relativity & particle loaded")

# ===================== 量子色动力学 QCD =====================
QUANTUM_CHROMODYNAMICS = [
  {"ch":"第一章","title":"QCD","en":"QCD","sub":"强相互作用","sections":[
    {"name":"1.1 色动力学","color":"#2563eb","topics":[T("色荷","红、绿、蓝","夸克携带。"),
      T("胶子","8种","传递强作用。"),
      T("渐近自由","高能弱耦合","QCD特性。"),
      T("色禁闭","夸克不可单独存在","低能强耦合。"),
      T("强子","夸克束缚态","介子重子。"),
      T("SU(3)规范","色规范群","理论。"),
      T("跑动耦合","α_s(Q)","随能量变化。"),
    ]},
    {"name":"1.2 现象","color":"#7c3aed","topics":[T("部分子","夸克胶子","核子内部。"),
      T("深度非弹性散射","DIS","探测内部结构。"),
      T("喷注","高能夸克碎裂","实验观测。"),
      T("格点QCD","数值计算","非微扰。"),
    ]},
  ]},
]

# ===================== 电弱统一 electroweak =====================
ELECTROWEAK = [
  {"ch":"第一章","title":"电弱统一","en":"ELECTROWEAK UNIFICATION","sub":"格拉肖-萨拉姆-温伯格","sections":[
    {"name":"1.1 统一","color":"#2563eb","topics":[T("电弱统一","电磁弱作用统一","GSW模型。"),
      T("SU(2)×U(1)","规范群","电弱。"),
      T("弱同位旋","T","SU(2)荷。"),
      T("弱超荷","Y","U(1)荷。"),
      T("混合角","θ_W","温伯格角。"),
      T("希格斯机制","质量起源","自发破缺。"),
      T("W,Z质量","由希格斯场","m_W,m_Z。"),
    ]},
    {"name":"1.2 弱作用","color":"#7c3aed","topics":[T("β衰变","中子衰变","弱作用。"),
      T("宇称不守恒","弱作用破坏P","李杨。"),
      T("CP破坏","K介子","CKM。"),
      T("中性流","Z玻色子传递","发现验证。"),
    ]},
  ]},
]

# ===================== 量子场论 quantum-field-theory =====================
QUANTUM_FIELD_THEORY = [
  {"ch":"第一章","title":"量子场论基础","en":"QFT FUNDAMENTALS","sub":"场的量子化","sections":[
    {"name":"1.1 量子化","color":"#2563eb","topics":[T("经典场","拉格朗日量","场论。"),
      T("正则量子化","对易关系","量子化。"),
      T("路径积分","∫Dφ e^{iS}","另一种形式。"),
      T("克莱因-戈登场","标量场","自旋0。"),
      T("狄拉克场","旋量场","自旋1/2。"),
      T("矢量场","规范场","自旋1。"),
    ]},
    {"name":"1.2 散射","color":"#7c3aed","topics":[T("S矩阵","散射振幅","S=⟨out|in⟩。"),
      T("费曼规则","图计算振幅","微扰。"),
      T("圈图","量子修正","高阶。"),
      T("发散","紫外红外","重整化。"),
      T("重整化群","跑动耦合","RG。"),
    ]},
  ]},
]

# ===================== 弦理论 string-theory =====================
STRING_THEORY = [
  {"ch":"第一章","title":"弦理论基础","en":"STRING THEORY","sub":"一维弦","sections":[
    {"name":"1.1 弦","color":"#2563eb","topics":[T("弦","一维延展体","基本对象。"),
      T("开弦/闭弦","有端无端","两种。"),
      T("玻色弦","26维","只有玻色子。"),
      T("超弦","10维","含费米子。"),
      T("弦振动模式","粒子谱","不同模式=粒子。"),
      T("弦张力","T_s","基本参数。"),
      T("闭弦谱","引力子","含引力。"),
    ]},
    {"name":"1.2 M理论","color":"#7c3aed","topics":[T("M理论","11维","统一五种超弦。"),
      T("D膜","开弦端点附着","膜。"),
      T("对偶性","S,T,U","理论等价。"),
      T("紧致化","额外维卷曲","得到4维。"),
    ]},
  ]},
]

# ===================== 量子引力 quantum-gravity =====================
QUANTUM_GRAVITY = [
  {"ch":"第一章","title":"量子引力","en":"QUANTUM GRAVITY","sub":"统一量子与引力","sections":[
    {"name":"1.1 量子引力","color":"#2563eb","topics":[T("量子引力","引力量子化","终极理论。"),
      T("普朗克长度","ℓ_P=√(ℏG/c³)","量子引力尺度。"),
      T("普朗克能量","E_P","~10^19 GeV。"),
      T("圈量子引力","自旋网络","非微扰。"),
      T("弦理论","引力量子","统一。"),
      T("时空量子化","离散时空","引力子。"),
    ]},
    {"name":"1.2 前沿","color":"#7c3aed","topics":[T("全息原理","AdS/CFT","对偶。"),
      T("黑洞信息佯谬","信息守恒","悖论。"),
      T("量子宇宙学","宇宙波函数","惠勒-德威特。"),
    ]},
  ]},
]

# ===================== 生物物理 biophysics =====================
BIOPHYSICS = [
  {"ch":"第一章","title":"生物物理","en":"BIOPHYSICS","sub":"物理与生命","sections":[
    {"name":"1.1 生物分子","color":"#2563eb","topics":[T("蛋白质结构","一级到四级","分子结构。"),
      T("DNA双螺旋","遗传物质","结构。"),
      T("分子马达","马达蛋白","能量转换。"),
      T("膜电位","神经信号","离子通道。"),
      T("X射线衍射","晶体结构","生物大分子。"),
      T("分子动力学模拟","原子运动","计算。"),
    ]},
    {"name":"1.2 生物系统","color":"#7c3aed","topics":[T("生物力学","细胞力学","力学。"),
      T("电泳","电场分离","技术。"),
      T("荧光","荧光蛋白","成像。"),
      T("光镊","光力操控","单分子。"),
    ]},
  ]},
]

# ===================== 医学物理 medical-physics =====================
MEDICAL_PHYSICS = [
  {"ch":"第一章","title":"医学物理","en":"MEDICAL PHYSICS","sub":"物理在医学","sections":[
    {"name":"1.1 影像与治疗","color":"#2563eb","topics":[T("X射线成像","伦琴","透视。"),
      T("CT","计算机断层","三维成像。"),
      T("MRI","核磁共振成像","软组织。"),
      T("超声成像","声波反射","无创。"),
      T("放射治疗","高能射线","治癌。"),
      T("核医学","放射性核素","PET。"),
    ]},
    {"name":"1.2 剂量与防护","color":"#7c3aed","topics":[T("辐射剂量","Gy,Sv","量度。"),
      T("辐射防护","ALARA","防护原则。"),
      T("治疗计划","TPS","剂量分布。"),
    ]},
  ]},
]

# ===================== 经济物理 econophysics =====================
ECONOPHYSICS = [
  {"ch":"第一章","title":"经济物理","en":"ECONOPHYSICS","sub":"统计物理与经济","sections":[
    {"name":"1.1 方法","color":"#2563eb","topics":[T("统计物理方法","应用于经济","跨学科。"),
      T("幂律分布","长尾","金融数据。"),
      T("金融市场","价格波动","随机过程。"),
      T("复杂网络","经济网络","拓扑。"),
      T("Agent模型","多主体模拟","经济仿真。"),
    ]},
    {"name":"1.2 应用","color":"#7c3aed","topics":[T("股票市场","收益分布","波动。"),
      T("经济危机","级联失效","风险。"),
      T("财富分布","帕累托律","不平等。"),
    ]},
  ]},
]

# ===================== 地球物理 geophysics =====================
GEOPHYSICS = [
  {"ch":"第一章","title":"地球物理","en":"GEOPHYSICS","sub":"地球物理","sections":[
    {"name":"1.1 地球","color":"#2563eb","topics":[T("地球结构","地壳地幔地核","分层。"),
      T("地震波","P波S波","探测内部。"),
      T("地磁场","地球磁场","发电机。"),
      T("重力场","地球引力","测量。"),
      T("地热","地球内部热","来源。"),
      T("板块构造","大陆漂移","运动。"),
    ]},
    {"name":"1.2 勘探","color":"#7c3aed","topics":[T("地震勘探","人工地震","油气。"),
      T("磁法勘探","磁异常","矿产。"),
      T("电法勘探","电阻率","资源。"),
    ]},
  ]},
]

# ===================== 计算物理 computational-physics =====================
COMPUTATIONAL_PHYSICS = [
  {"ch":"第一章","title":"计算物理方法","en":"COMPUTATIONAL PHYSICS","sub":"数值方法","sections":[
    {"name":"1.1 数值方法","color":"#2563eb","topics":[T("数值微分","差分近似","导数。"),
      T("数值积分","梯形辛普森","积分。"),
      T("常微分方程","RK方法","ODE。"),
      T("偏微分方程","有限差分","PDE。"),
      T("蒙特卡洛方法","随机采样","MC。"),
      T("分子动力学","MD","粒子模拟。"),
      T("有限元","FEM","边值问题。"),
    ]},
  ]},
]

print("advanced loaded")

# ===================== 激光物理 laser-physics =====================
LASER_PHYSICS = [
  {"ch":"第一章","title":"激光原理","en":"LASER PRINCIPLES","sub":"受激辐射","sections":[
    {"name":"1.1 基本原理","color":"#2563eb","topics":[T("受激辐射","E₂→E₁+hν","激光基础。"),
      T("自发辐射","随机相位","普通光。"),
      T("受激吸收","E₁+hν→E₂","吸收。"),
      T("粒子数反转","N₂>N₁","激光条件。"),
      T("阈值条件","增益≥损耗","起振。"),
      T("光放大","G(ν)","增益介质。"),
      T("谐振腔","两面反射镜","反馈选模。"),
    ]},
    {"name":"1.2 激光器","color":"#7c3aed","topics":[T("红宝石激光器","三能级","第一台。"),
      T("He-Ne激光器","四能级","气体。"),
      T("半导体激光器","LD","电注入。"),
      T("光纤激光器","光纤增益","高功率。"),
      T("锁模","超短脉冲","飞秒。"),
      T("调Q","巨脉冲","高峰值。"),
    ]},
  ]},
]

# ===================== 非线性光学 nonlinear-optics =====================
NONLINEAR_OPTICS = [
  {"ch":"第一章","title":"非线性光学","en":"NONLINEAR OPTICS","sub":"强光与介质","sections":[
    {"name":"1.1 非线性效应","color":"#2563eb","topics":[T("非线性极化","P=χ⁽¹⁾E+χ⁽²⁾E²+...","强光。"),
      T("二次谐波","SHG, ω→2ω","倍频。"),
      T("三次谐波","THG, ω→3ω","三倍频。"),
      T("和频","ω₁+ω₂","频率相加。"),
      T("差频","ω₁-ω₂","频率相减。"),
      T("相位匹配","Δk=0","效率最大。"),
      T("光参量放大","OPA","参量过程。"),
    ]},
  ]},
]

# ===================== 光纤光学 fiber-optics =====================
FIBER_OPTICS = [
  {"ch":"第一章","title":"光纤","en":"FIBER OPTICS","sub":"光导纤维","sections":[
    {"name":"1.1 光纤","color":"#2563eb","topics":[T("光纤结构","纤芯包层涂覆","光波导。"),
      T("全反射","n₁>n₂","导光原理。"),
      T("数值孔径","NA=sinθ_max","收光能力。"),
      T("单模光纤","SMF","单模传输。"),
      T("多模光纤","MMF","多模传输。"),
      T("损耗","α dB/km","衰减。"),
      T("色散","模式/材料/波导","展宽。"),
    ]},
  ]},
]

# ===================== 光子学 photonics =====================
PHOTONICS = [
  {"ch":"第一章","title":"光子学","en":"PHOTONICS","sub":"光子技术","sections":[
    {"name":"1.1 光子器件","color":"#2563eb","topics":[T("光子晶体","周期介电结构","光子带隙。"),
      T("光波导","导光","集成光路。"),
      T("光调制器","电光调制","信号。"),
      T("光探测器","光电转换","PD。"),
      T("光开关","光路切换","交换。"),
      T("光放大器","EDFA","放大。"),
    ]},
    {"name":"1.2 光子技术","color":"#7c3aed","topics":[T("光子集成","PIC","光路集成。"),
      T("光通信","光纤通信","信息。"),
      T("光传感","光纤传感","测量。"),
      T("光计算","光子计算","并行。"),
    ]},
  ]},
]

# ===================== 固体物理 solid-state-physics =====================
SOLID_STATE_PHYSICS = [
  {"ch":"第一章","title":"固体物理","en":"SOLID STATE PHYSICS","sub":"凝聚态","sections":[
    {"name":"1.1 电子","color":"#2563eb","topics":[T("自由电子气","德鲁德模型","经典。"),
      T("索末菲模型","量子自由电子","费米统计。"),
      T("布洛赫电子","周期势","能带。"),
      T("费米面","E_F","k空间。"),
      T("霍尔效应","横向电压","载流子。"),
      T("德哈斯-范阿尔芬","振荡","费米面测量。"),
    ]},
    {"name":"1.2 输运","color":"#7c3aed","topics":[T("电导率","σ","欧姆定律。"),
      T("热导率","κ","傅里叶定律。"),
      T("维德曼-弗兰兹定律","κ/σ=LT","关系。"),
      T("磁阻","磁场电阻","输运。"),
    ]},
  ]},
]

# ===================== 材料科学 materials-science =====================
MATERIALS_SCIENCE = [
  {"ch":"第一章","title":"材料科学","en":"MATERIALS SCIENCE","sub":"结构性能","sections":[
    {"name":"1.1 材料分类","color":"#2563eb","topics":[T("金属材料","金属键","塑性。"),
      T("陶瓷材料","离子共价键","硬脆。"),
      T("高分子","共价键","长链。"),
      T("复合材料","多相","综合性能。"),
      T("半导体","硅锗","电子。"),
      T("纳米材料","纳米尺度","量子效应。"),
    ]},
    {"name":"1.2 性能","color":"#7c3aed","topics":[T("力学性能","强度硬度","机械。"),
      T("热学性能","热膨胀导热","热。"),
      T("电学性能","电阻率","电。"),
      T("磁学性能","磁化率","磁。"),
      T("光学性能","折射率","光。"),
      T("相图","平衡相","成分温度。"),
    ]},
  ]},
]

# ===================== 晶体学 crystallography =====================
CRYSTALLOGRAPHY = [
  {"ch":"第一章","title":"晶体学","en":"CRYSTALLOGRAPHY","sub":"晶体对称","sections":[
    {"name":"1.1 对称","color":"#2563eb","topics":[T("点对称","旋转反演","点群。"),
      T("平移对称","晶格平移","空间群。"),
      T("点群","32种","晶体学点群。"),
      T("空间群","230种","晶体空间群。"),
      T("晶系","7种","三斜到立方。"),
      T("布拉菲格子","14种","原胞。"),
    ]},
    {"name":"1.2 衍射","color":"#7c3aed","topics":[T("X射线衍射","布拉格定律","结构。"),
      T("布拉格公式","2d sinθ=nλ","衍射。"),
      T("电子衍射","TEM","晶体。"),
      T("中子衍射","磁结构","中子。"),
      T("粉末衍射","多晶","物相。"),
    ]},
  ]},
]

# ===================== 微电子学 microelectronics =====================
MICROELECTRONICS = [
  {"ch":"第一章","title":"微电子学","en":"MICROELECTRONICS","sub":"集成电路","sections":[
    {"name":"1.1 工艺","color":"#2563eb","topics":[T("光刻","图形转移","工艺。"),
      T("刻蚀","去除材料","干法湿法。"),
      T("薄膜沉积","CVD,PVD","镀膜。"),
      T("离子注入","掺杂","控制。"),
      T("氧化","SiO₂生长","栅氧。"),
      T("扩散","高温掺杂","杂质。"),
      T("CMP","化学机械抛光","平坦化。"),
    ]},
  ]},
]

# ===================== 光电子学 optoelectronics =====================
OPTOELECTRONICS = [
  {"ch":"第一章","title":"光电子学","en":"OPTOELECTRONICS","sub":"光电转换","sections":[
    {"name":"1.1 器件","color":"#2563eb","topics":[T("LED","发光二极管","电致发光。"),
      T("激光二极管","LD","受激发射。"),
      T("光电二极管","PD","光生电流。"),
      T("太阳能电池","光伏效应","发电。"),
      T("光电倍增管","PMT","弱光探测。"),
      T("CCD","电荷耦合","成像。"),
    ]},
    {"name":"1.2 物理基础","color":"#7c3aed","topics":[T("光电效应","光子→电子","爱因斯坦。"),
      T("辐射复合","电子空穴复合发光","LED。"),
      T("受激辐射","光放大","激光。"),
      T("光吸收","带间跃迁","探测器。"),
    ]},
  ]},
]

# ===================== 磁学 magnetism =====================
MAGNETISM = [
  {"ch":"第一章","title":"磁学","en":"MAGNETISM","sub":"磁现象","sections":[
    {"name":"1.1 磁性","color":"#2563eb","topics":[T("抗磁性","χ<0","所有材料。"),
      T("顺磁性","χ>0","未成对电子。"),
      T("铁磁性","自发磁化","交换作用。"),
      T("反铁磁性","反平行排列","奈尔温度。"),
      T("亚铁磁性","不等反平行","铁氧体。"),
      T("磁畴","磁化区域","畴壁。"),
      T("居里温度","T_c","铁磁顺磁转变。"),
      T("磁滞回线","B-H","磁化历史。"),
    ]},
  ]},
]

# ===================== 电介质物理 dielectrics =====================
DIELECTRICS = [
  {"ch":"第一章","title":"电介质","en":"DIELECTRICS","sub":"绝缘与极化","sections":[
    {"name":"1.1 极化","color":"#2563eb","topics":[T("电极化","P","偶极矩密度。"),
      T("位移极化","电子离子位移","瞬时。"),
      T("取向极化","偶极取向","热运动。"),
      T("介电常数","ε_r=1+χ_e","极化能力。"),
      T("电损耗","tanδ","能量损耗。"),
      T("击穿","电场过强","绝缘破坏。"),
      T("铁电体","自发极化","P-E回线。"),
    ]},
  ]},
]

# ===================== 近代物理实验 modern-physics-experiments =====================
MODERN_PHYSICS_EXPERIMENTS = [
  {"ch":"第一章","title":"近代物理实验","en":"MODERN PHYSICS EXPERIMENTS","sub":"经典实验","sections":[
    {"name":"1.1 实验","color":"#2563eb","topics":[T("密立根油滴","电子电荷","e测量。"),
      T("迈克尔逊-莫雷","以太不存在","相对论前奏。"),
      T("黑体辐射","普朗克公式","量子起源。"),
      T("光电效应","爱因斯坦","光子。"),
      T("康普顿散射","光子动量","X射线。"),
      T("卢瑟福散射","核式结构","α粒子。"),
      T("弗兰克-赫兹","能级量子化","汞原子。"),
    ]},
  ]},
]

print("remaining loaded")

# ===================== 光学设计 optical-design =====================
OPTICAL_DESIGN = [
  {"ch":"第一章","title":"光学设计","en":"OPTICAL DESIGN","sub":"像差与镜头","sections":[
    {"name":"1.1 像差","color":"#2563eb","topics":[T("球差","球面透镜像差","轴上点。"),
      T("彗差","轴外点","彗星状。"),
      T("像散","轴外细光束","两个焦点。"),
      T("场曲","像面弯曲","Petzval。"),
      T("畸变","形状畸变","桶形枕形。"),
      T("色差","波长不同","位置放大率。"),
      T("二级光谱","残留色差","复消色差。"),
    ]},
    {"name":"1.2 光学系统","color":"#7c3aed","topics":[T("望远镜","物镜目镜","望远。"),
      T("显微镜","高倍放大","显微。"),
      T("照相机镜头","多片组","成像。"),
      T("目镜","放大虚像","观察。"),
      T("棱镜","反射色散","转向分光。"),
      T("光阑","限制光束","孔径视场。"),
      T("相对孔径","D/f","光通量。"),
      T("F数","f/D","光圈。"),
    ]},
  ]},
  {"ch":"第二章","title":"像质评价","en":"IMAGE QUALITY","sub":"评价方法","sections":[
    {"name":"2.1 评价","color":"#0f766e","topics":[T("几何像差","光线追迹","像差。"),
      T("点列图","光线像点分布","弥散。"),
      T("传递函数","MTF","频率响应。"),
      T("斯特列尔比","中心点亮度","像质。"),
      T("波像差","波前偏差","瑞利判据。"),
    ]},
  ]},
]

# ===================== 发光学 luminescence =====================
LUMINESCENCE = [
  {"ch":"第一章","title":"发光学","en":"LUMINESCENCE","sub":"非热辐射","sections":[
    {"name":"1.1 发光","color":"#2563eb","topics":[T("发光定义","非热辐射","区别热辐射。"),
      T("光致发光","光激发","PL。"),
      T("电致发光","电激发","EL。"),
      T("阴极射线发光","电子束","CRT。"),
      T("化学发光","化学反应","CL。"),
      T("生物发光","生物过程","BL。"),
      T("激发谱","激发波长依赖","激发。"),
      T("发射谱","发光波长分布","发射。"),
      T("发光寿命","衰减时间","τ。"),
      T("量子效率","光子数比","η。"),
    ]},
  ]},
]

# ===================== 量子计算 quantum-computing =====================
QUANTUM_COMPUTING = [
  {"ch":"第一章","title":"量子计算","en":"QUANTUM COMPUTING","sub":"量子比特","sections":[
    {"name":"1.1 量子比特","color":"#2563eb","topics":[T("量子比特","|0⟩,|1⟩叠加","qubit。"),
      T("叠加态","α|0⟩+β|1⟩","量子特性。"),
      T("纠缠态","不可分离","Bell态。"),
      T("测量","投影测量","坍缩。"),
      T("量子门","U操作","幺正变换。"),
      T("Hadamard门","H","叠加。"),
      T("CNOT门","控制非","两比特。"),
      T("量子电路","门序列","算法。"),
    ]},
    {"name":"1.2 算法","color":"#7c3aed","topics":[T("Shor算法","大数分解","指数加速。"),
      T("Grover算法","搜索","√N加速。"),
      T("量子傅里叶变换","QFT","核心。"),
      T("量子纠错","纠错码","容错。"),
      T("退相干","环境耦合","噪声。"),
    ]},
  ]},
]

# ===================== 纳米物理 nanophysics =====================
NANOPHYSICS = [
  {"ch":"第一章","title":"纳米物理","en":"NANOPHYSICS","sub":"纳米尺度","sections":[
    {"name":"1.1 纳米效应","color":"#2563eb","topics":[T("量子尺寸效应","能级离散","小尺寸。"),
      T("表面效应","大比表面积","表面原子。"),
      T("量子隧道效应","势垒穿透","纳米。"),
      T("小尺寸效应","物性变化","尺度。"),
      T("量子点","零维","人造原子。"),
      T("量子线","一维","电子限制。"),
      T("量子阱","二维","层状。"),
    ]},
  ]},
]

# ===================== 拓扑物质 topological-matter =====================
TOPOLOGICAL_MATTER = [
  {"ch":"第一章","title":"拓扑物质","en":"TOPOLOGICAL MATTER","sub":"拓扑相变","sections":[
    {"name":"1.1 拓扑","color":"#2563eb","topics":[T("拓扑序","非局域序","拓扑。"),
      T("拓扑不变量","陈数、Z2","表征。"),
      T("拓扑绝缘体","体绝缘面导电","表面态。"),
      T("量子霍尔效应","整数量子化","拓扑。"),
      T("量子自旋霍尔","自旋分辨","QSHE。"),
      T("边缘态","受拓扑保护","无散射。"),
      T("任意子","2D统计","非阿贝尔。"),
    ]},
  ]},
]

# ===================== 二维材料 2d-materials =====================
TWO_D_MATERIALS = [
  {"ch":"第一章","title":"二维材料","en":"2D MATERIALS","sub":"石墨烯等","sections":[
    {"name":"1.1 石墨烯","color":"#2563eb","topics":[T("石墨烯","单层碳原子","sp2。"),
      T("狄拉克锥","线性色散","零带隙。"),
      T("高迁移率","~200000 cm²/Vs","电子。"),
      T("力学强度","最强材料","杨氏模量。"),
      T("热导率","极高","~5000 W/mK。"),
      T("透明","97.7%透光","光电器件。"),
    ]},
    {"name":"1.2 其他2D","color":"#7c3aed","topics":[T("MoS₂","过渡金属硫化物","带隙。"),
      T("h-BN","六方氮化硼","绝缘体。"),
      T("黑磷","直接带隙","可调。"),
      T("范德瓦尔斯异质结","堆垛","人工结构。"),
    ]},
  ]},
]

# ===================== 低温物理 low-temperature-physics =====================
LOW_TEMPERATURE_PHYSICS = [
  {"ch":"第一章","title":"低温物理","en":"LOW TEMPERATURE PHYSICS","sub":"极低温","sections":[
    {"name":"1.1 低温","color":"#2563eb","topics":[T("低温制冷","液氦","4K。"),
      T("稀释制冷机","3He/4He","mK。"),
      T("绝热退磁","顺磁盐","μK。"),
      T("超流氦","He II","无粘。"),
      T("超导电性","低温超导","零电阻。"),
      T("玻色-爱因斯坦凝聚","BEC","nK。"),
    ]},
    {"name":"1.2 低温现象","color":"#7c3aed","topics":[T("量子流体","液氦","量子效应。"),
      T("量子化涡旋","超流涡旋","量子化。"),
      T("第二声","温度波","超流。"),
      T("低温热容","T³律","德拜。"),
    ]},
  ]},
]

# ===================== 材料制备 materials-preparation =====================
MATERIALS_PREPARATION = [
  {"ch":"第一章","title":"材料制备","en":"MATERIALS PREPARATION","sub":"合成方法","sections":[
    {"name":"1.1 方法","color":"#2563eb","topics":[T("晶体生长","提拉法","单晶。"),
      T("区熔","杂质分离","提纯。"),
      T("CVD","化学气相沉积","薄膜。"),
      T("PVD","物理气相沉积","溅射蒸发。"),
      T("MBE","分子束外延","超晶格。"),
      T("溶胶-凝胶","wet化学","陶瓷。"),
      T("烧结","高温致密化","陶瓷。"),
    ]},
  ]},
]

# ===================== 材料表征 materials-characterization =====================
MATERIALS_CHARACTERIZATION = [
  {"ch":"第一章","title":"材料表征","en":"MATERIALS CHARACTERIZATION","sub":"分析方法","sections":[
    {"name":"1.1 表征","color":"#2563eb","topics":[T("XRD","X射线衍射","晶体结构。"),
      T("SEM","扫描电镜","形貌。"),
      T("TEM","透射电镜","高分辨。"),
      T("AFM","原子力显微镜","表面。"),
      T("XPS","光电子能谱","成分。"),
      T("Raman","拉曼光谱","振动。"),
      T("UV-Vis","紫外可见","光学。"),
      T("PPMS","物性测量系统","电磁热。"),
    ]},
  ]},
]

# ===================== 半导体材料 semiconductor-materials =====================
SEMICONDUCTOR_MATERIALS = [
  {"ch":"第一章","title":"半导体材料","en":"SEMICONDUCTOR MATERIALS","sub":"材料体系","sections":[
    {"name":"1.1 元素半导体","color":"#2563eb","topics":[T("硅Si","最常用","间接带隙。"),
      T("锗Ge","早期","间接。"),
      T("金刚石","宽禁带","高温。"),
    ]},
    {"name":"1.2 化合物","color":"#7c3aed","topics":[T("GaAs","直接带隙","光电子。"),
      T("InP","光纤通信","1.55μm。"),
      T("GaN","蓝绿光","宽禁带。"),
      T("SiC","高温高频","宽禁带。"),
      T("ZnO","紫外","透明导电。"),
      T("三元合金","AlGaAs,InGaAs","带隙可调。"),
    ]},
  ]},
]

# ===================== 黑洞物理 black-hole-physics =====================
BLACK_HOLE_PHYSICS = [
  {"ch":"第一章","title":"黑洞物理","en":"BLACK HOLE PHYSICS","sub":"引力坍缩","sections":[
    {"name":"1.1 黑洞","color":"#2563eb","topics":[T("史瓦西黑洞","球对称","静态。"),
      T("事件视界","r_s=2GM/c²","不归点。"),
      T("奇点","曲率无穷","中心。"),
      T("克尔黑洞","旋转","轴对称。"),
      T("吸积盘","物质旋入","辐射。"),
      T("霍金辐射","量子蒸发","黑洞温度。"),
      T("黑洞熵","S=A/(4ℓ_P²)","面积律。"),
      T("无毛定理","质量电荷角动量","三参数。"),
    ]},
  ]},
]

# ===================== 规范场论 gauge-theory =====================
GAUGE_THEORY = [
  {"ch":"第一章","title":"规范场论","en":"GAUGE THEORY","sub":"局域对称","sections":[
    {"name":"1.1 规范","color":"#2563eb","topics":[T("规范对称","局域相位不变","核心。"),
      T("U(1)规范","电磁","QED。"),
      T("SU(2)规范","弱作用","非阿贝尔。"),
      T("SU(3)规范","强作用","QCD。"),
      T("协变导数","D_μ=∂_μ-igA_μ","规范场。"),
      T("场强张量","F_μν","曲率。"),
      T("杨-米尔斯","非阿贝尔规范","YM。"),
    ]},
  ]},
]

# ===================== 共形场论 conformal-field-theory =====================
CONFORMAL_FIELD_THEORY = [
  {"ch":"第一章","title":"共形场论","en":"CONFORMAL FIELD THEORY","sub":"共形对称","sections":[
    {"name":"1.1 CFT","color":"#2563eb","topics":[T("共形变换","保角变换","对称。"),
      T("共形代数","Virasoro","无穷维。"),
      T("中心荷","c","反常。"),
      T("初级场","共形权","基本。"),
      T("关联函数","多点函数","结构。"),
      T("算子积展开","OPE","短程展开。"),
      T("2D CFT","完全可解","二维。"),
    ]},
  ]},
]

# ===================== 拓扑量子场论 tqft =====================
TQFT = [
  {"ch":"第一章","title":"拓扑量子场论","en":"TQFT","sub":"拓扑不变量","sections":[
    {"name":"1.1 TQFT","color":"#2563eb","topics":[T("TQFT","度规无关","拓扑。"),
      T("陈-西蒙斯","3D TQFT","CS。"),
      T("扭结不变量","Jones多项式","结。"),
      T("拓扑量子计算","非阿贝尔任意子","容错。"),
      T("配分函数","流形不变量","Z(M)。"),
    ]},
    {"name":"1.2 数学结构","color":"#7c3aed","topics":[T("张量范畴","代数结构","TQFT基础。"),
      T("模函子","曲面到向量空间","TQFT。"),
      T("Frobenius代数","交换Frobenius","2D TQFT。"),
    ]},
  ]},
]

# ===================== 辐射过程 radiation-processes =====================
RADIATION_PROCESSES = [
  {"ch":"第一章","title":"辐射过程","en":"RADIATION PROCESSES","sub":"天体辐射","sections":[
    {"name":"1.1 辐射","color":"#2563eb","topics":[T("轫致辐射","加速带电粒子","连续谱。"),
      T("同步辐射","相对论电子磁场","偏振。"),
      T("逆康普顿","光子被电子加速","高能。"),
      T("回旋辐射","非相对论电子","谱线。"),
      T("黑体辐射","热平衡","普朗克。"),
      T("辐射转移","辐射在介质中","RT。"),
      T("不透明度","κ","吸收。"),
    ]},
  ]},
]

# ===================== 聚变物理 fusion-physics =====================
FUSION_PHYSICS = [
  {"ch":"第一章","title":"聚变物理","en":"FUSION PHYSICS","sub":"受控热核聚变","sections":[
    {"name":"1.1 聚变","color":"#2563eb","topics":[T("聚变反应","D+T→He+n","产能。"),
      T("劳逊判据","nτ>10^14","点火。"),
      T("三重积","nTτ","聚变条件。"),
      T("等离子体约束","磁约束/惯性","方案。"),
      T("托卡马克","环形磁约束","主流。"),
      T("仿星器","三维磁约束","稳态。"),
      T("惯性约束","激光压缩","ICF。"),
      T("Q值","输出/输入能量","增益。"),
    ]},
  ]},
]

# ===================== 相对论(合并 special+general) =====================
RELATIVITY = SPECIAL_RELATIVITY + GENERAL_RELATIVITY

print("all topics loaded")

# ===================== 线性代数 linear-algebra =====================
LINEAR_ALGEBRA = [
  {"ch":"第一章","title":"行列式与矩阵","en":"DETERMINANTS & MATRICES","sub":"线性代数基础","sections":[
    {"name":"1.1 行列式","color":"#2563eb","topics":[T("二阶行列式","ad-bc","基础。"),
      T("n阶行列式","Σ(-1)^τ a₁p₁...","定义。"),
      T("行列式性质","转置不变等","7条性质。"),
      T("行列式展开","按行/列展开","余子式。"),
      T("克莱姆法则","x_i=D_i/D","解方程组。"),
      T("范德蒙行列式","∏(x_j-x_i)","特殊。"),
    ]},
    {"name":"1.2 矩阵","color":"#7c3aed","topics":[T("矩阵定义","m×n数组","基本。"),
      T("矩阵加法","对应元素相加","运算。"),
      T("矩阵乘法","C=AB","行乘列。"),
      T("转置矩阵","A^T","行列互换。"),
      T("逆矩阵","AA⁻¹=I","可逆。"),
      T("伴随矩阵","A*=C^T","求逆。"),
      T("初等变换","行/列变换","化简。"),
      T("矩阵的秩","r(A)","最高阶非零。"),
    ]},
  ]},
  {"ch":"第二章","title":"向量与线性方程组","en":"VECTORS & LINEAR SYSTEMS","sub":"线性空间","sections":[
    {"name":"2.1 向量","color":"#0f766e","topics":[T("n维向量","(a₁,...,aₙ)","向量。"),
      T("线性组合","k₁α₁+...+kₙαₙ","组合。"),
      T("线性相关","存在不全为零k_i","相关。"),
      T("线性无关","只有全零k_i","无关。"),
      T("向量组的秩","最大无关组个数","秩。"),
      T("基与维数","极大无关组","空间。"),
    ]},
    {"name":"2.2 方程组","color":"#c2410c","topics":[T("齐次方程组","Ax=0","解空间。"),
      T("非齐次方程组","Ax=b","解的结构。"),
      T("基础解系","解空间基","n-r个。"),
      T("通解","特解+齐次通解","结构。"),
    ]},
  ]},
  {"ch":"第三章","title":"特征值与二次型","en":"EIGENVALUES & QUADRATIC FORMS","sub":"谱理论","sections":[
    {"name":"3.1 特征值","color":"#2563eb","topics":[T("特征值与特征向量","Ax=λx","定义。"),
      T("特征多项式","|λI-A|=0","求特征值。"),
      T("相似矩阵","B=P⁻¹AP","相似。"),
      T("对角化","P⁻¹AP=Λ","可对角化。"),
      T("实对称矩阵","正交对角化","对称。"),
    ]},
    {"name":"3.2 二次型","color":"#7c3aed","topics":[T("二次型","x^TAx","定义。"),
      T("标准形","只含平方项","化简。"),
      T("正定二次型","x^TAx>0","正定。"),
      T("惯性定理","正负惯性指数","不变量。"),
    ]},
  ]},
]

# ===================== 牛顿力学 newtonian-mechanics =====================
NEWTONIAN_MECHANICS = [
  {"ch":"第一章","title":"运动学","en":"KINEMATICS","sub":"运动描述","sections":[
    {"name":"1.1 质点运动","color":"#2563eb","topics":[T("位移","Δr","位置变化。"),
      T("速度","v=dr/dt","位置变化率。"),
      T("加速度","a=dv/dt","速度变化率。"),
      T("匀速直线运动","v恒定","x=vt。"),
      T("匀加速运动","v=v₀+at","x=v₀t+½at²。"),
      T("自由落体","a=g","竖直下落。"),
      T("抛体运动","水平+竖直","抛物线。"),
      T("圆周运动","向心加速度","a=v²/r。"),
    ]},
  ]},
  {"ch":"第二章","title":"牛顿定律","en":"NEWTON'S LAWS","sub":"动力学","sections":[
    {"name":"2.1 三定律","color":"#7c3aed","topics":[T("第一定律","惯性定律","F=0时v不变。"),
      T("第二定律","F=ma","核心定律。"),
      T("第三定律","作用反作用","F₁₂=-F₂₁。"),
      T("重力","W=mg","地球引力。"),
      T("弹力","F=-kx","胡克定律。"),
      T("摩擦力","f=μN","阻碍相对运动。"),
      T("张力","绳中拉力","约束。"),
      T("法向力","N","支撑力。"),
    ]},
  ]},
  {"ch":"第三章","title":"动量与能量","en":"MOMENTUM & ENERGY","sub":"守恒律","sections":[
    {"name":"3.1 动量","color":"#0f766e","topics":[T("动量","p=mv","运动量。"),
      T("冲量","I=Ft","力的累积。"),
      T("动量定理","I=Δp","冲量等于动量变化。"),
      T("动量守恒","Σp恒定","无外力。"),
      T("碰撞","弹性/非弹性","动量交换。"),
      T("质心","加权平均位置","质心运动。"),
    ]},
    {"name":"3.2 能量","color":"#c2410c","topics":[T("功","W=F·s","力做功。"),
      T("动能","E_k=½mv²","运动能量。"),
      T("动能定理","W=ΔE_k","合功等于动能变化。"),
      T("势能","E_p=mgh","位置能量。"),
      T("机械能守恒","E_k+E_p恒定","只有保守力。"),
      T("功率","P=W/t","做功速率。"),
    ]},
  ]},
  {"ch":"第四章","title":"刚体与振动","en":"RIGID BODY & OSCILLATION","sub":"转动与振动","sections":[
    {"name":"4.1 刚体","color":"#2563eb","topics":[T("角位移","θ","转动角度。"),
      T("角速度","ω=dθ/dt","转动快慢。"),
      T("角加速度","α=dω/dt","角速度变化。"),
      T("转动惯量","I=∫r²dm","转动惯性。"),
      T("力矩","τ=r×F","转动原因。"),
      T("转动定律","τ=Iα","牛顿第二定律转动形式。"),
      T("角动量","L=Iω","转动动量。"),
      T("角动量守恒","L恒定","无外力矩。"),
    ]},
    {"name":"4.2 振动","color":"#7c3aed","topics":[T("简谐振动","x=Acos(ωt+φ)","基本振动。"),
      T("周期","T=2π/ω","振动时间。"),
      T("振幅","A","最大位移。"),
      T("相位","ωt+φ","振动状态。"),
      T("阻尼振动","振幅衰减","能量损耗。"),
      T("受迫振动","外力驱动","共振。"),
    ]},
  ]},
]

# ===================== 工程光学 engineering-optics =====================
ENGINEERING_OPTICS = [
  {"ch":"第一章","title":"几何光学","en":"GEOMETRICAL OPTICS","sub":"光线追迹","sections":[
    {"name":"1.1 基本定律","color":"#2563eb","topics":[T("光的直线传播","均匀介质","光线。"),
      T("反射定律","θ_i=θ_r","反射。"),
      T("折射定律","n₁sinθ₁=n₂sinθ₂","斯涅尔。"),
      T("全反射","sinθ_c=n₂/n₁","光密到光疏。"),
      T("费马原理","光程极值","最短时间。"),
      T("棱镜偏向角","δ","色散。"),
    ]},
    {"name":"1.2 光学系统","color":"#7c3aed","topics":[T("薄透镜","1/u+1/v=1/f","成像。"),
      T("透镜组合","多个透镜","系统。"),
      T("光阑","孔径/视场","限制光束。"),
      T("光瞳","入瞳出瞳","光束。"),
      T("景深","清晰范围","成像。"),
    ]},
  ]},
  {"ch":"第二章","title":"像差与像质","en":"ABERRATIONS","sub":"像差校正","sections":[
    {"name":"2.1 像差","color":"#0f766e","topics":[T("球差","轴上像差","球面。"),
      T("彗差","轴外像差","彗星。"),
      T("像散","轴外细光束","两焦点。"),
      T("场曲","像面弯曲","Petzval。"),
      T("畸变","形状畸变","桶枕形。"),
      T("色差","波长差异","位置放大率。"),
    ]},
  ]},
]

# ===================== 量子信息 quantum-information =====================
QUANTUM_INFORMATION = [
  {"ch":"第一章","title":"量子信息基础","en":"QUANTUM INFORMATION","sub":"量子比特与纠缠","sections":[
    {"name":"1.1 量子信息","color":"#2563eb","topics":[T("量子比特","|ψ⟩=α|0⟩+β|1⟩","信息单元。"),
      T("量子叠加","同时处于多态","叠加。"),
      T("量子纠缠","不可分离态","关联。"),
      T("量子测量","投影测量","坍缩。"),
      T("不可克隆定理","未知态不可复制","定理。"),
      T("量子门","U操作","幺正变换。"),
    ]},
    {"name":"1.2 量子通信","color":"#7c3aed","topics":[T("量子密钥分发","QKD","安全。"),
      T("BB84协议","偏振编码","密钥。"),
      T("量子隐形传态","传输量子态","纠缠。"),
      T("量子密集编码","1量子比特传2比特","编码。"),
    ]},
  ]},
]

print("extra subjects loaded")
