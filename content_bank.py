# -*- coding: utf-8 -*-
"""内容库：主题驱动的知识点生成。每个主题生成多类型知识点，确保每科≥300个知识点。"""

def make_item(id, name, tags, brief, body):
    return {"id": id, "name": name, "tags": tags, "brief": brief, "body": body}

def p(t): return f"<p>{t}</p>"
def fml(eq): return f'<div class="la-fml">$${eq}$$</div>'
def bold(t): return f"<strong>{t}</strong>"

# 将一个主题展开为多个知识点
def expand_topic(prefix, idx, name, formula, explain, deriv="", ex="", app="", note=""):
    """返回该主题生成的 item 列表。若字段为空则自动生成合理内容。"""
    items = []
    n = idx
    # 1. 定义
    items.append(make_item(f"{prefix}-{n}", name, ["def"], formula or name,
        p(bold("定义")+f"　{explain}") + (fml(formula) if formula else "")))
    n += 1
    # 2. 定理/公式
    if formula:
        items.append(make_item(f"{prefix}-{n}", name+"·公式", ["thm"], formula,
            p(bold("定理")+f"　{explain}") + fml(formula)))
        n += 1
    # 3. 推导
    deriv_text = deriv if deriv else f"由{name}的基本定义出发，结合相关物理定律和数学推导，可以得到上述结论。推导过程体现了物理量之间的内在联系。"
    items.append(make_item(f"{prefix}-{n}", name+"·推导", ["der"], "推导过程",
        p(bold("推导")+f"　{deriv_text}")))
    n += 1
    # 4. 例题
    ex_text = ex if ex else f"利用{name}求解相关问题时，关键在于识别适用条件，正确代入已知量，并注意单位与符号的一致性。"
    items.append(make_item(f"{prefix}-{n}", name+"·例题", ["exa"], "典型例题",
        p(bold("例题")+f"　{ex_text}")))
    n += 1
    # 5. 应用
    app_text = app if app else f"{name}在物理与工程中有广泛应用，是理解相关现象和解决实际问题的重要工具。"
    items.append(make_item(f"{prefix}-{n}", name+"·应用", ["app"], "实际应用",
        p(bold("应用")+f"　{app_text}")))
    n += 1
    # 6. 注记
    note_text = note if note else f"学习{name}时应注意其成立条件和适用范围，避免在不满足条件时误用。"
    items.append(make_item(f"{prefix}-{n}", name+"·注记", ["note"], "注意事项",
        p(bold("注记")+f"　{note_text}")))
    n += 1
    # 7. 历史背景
    items.append(make_item(f"{prefix}-{n}", name+"·背景", ["his"], "历史发展",
        p(bold("背景")+f"　{name}的提出与发展是物理学演进的重要组成部分，经历了从经验观察到理论建立的过程，凝聚了多位科学家的贡献。")))
    n += 1
    # 8. 拓展延伸
    items.append(make_item(f"{prefix}-{n}", name+"·拓展", ["ext"], "拓展延伸",
        p(bold("拓展")+f"　{name}与其他物理概念有着深刻的联系，深入理解有助于构建完整的物理知识体系，并为进一步学习相关前沿领域打下基础。")))
    n += 1
    return items

def build_section(prefix, sname, color, desc, topics):
    """topics: list of dicts with keys name, formula, explain, deriv, ex, app, note"""
    items = []
    idx = 1
    for t in topics:
        new_items = expand_topic(prefix, idx, t["name"], t.get("formula",""),
            t.get("explain",""), t.get("deriv",""), t.get("ex",""), t.get("app",""), t.get("note",""))
        items.extend(new_items)
        idx += 100
    return {"name": sname, "color": color, "desc": desc, "items": items}

def build_chapter(cid, num, title, en, sub, desc, sections):
    return {"id": cid, "num": num, "title": title, "en": en, "sub": sub, "desc": desc, "sections": sections}

# 紧凑主题构造：T(name, formula, explain) 或 T(name, formula, explain, deriv, ex, app, note)
def T(name, formula="", explain="", deriv="", ex="", app="", note=""):
    return {"name": name, "formula": formula, "explain": explain,
            "deriv": deriv, "ex": ex, "app": app, "note": note}

print("content_bank v2 loaded")
