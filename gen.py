#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
物理学知识体系 - 专题页面批量生成器
模仿 linear-algebra.html / engineering-optics.html 的 la- 前缀模式生成全部学科页面。
"""
import os
import json

OUT_DIR = "/workspace"

# ============================================================
# 工具：将 LaTeX 正文转义为 JS 模板字符串
# ============================================================
def js_escape(s):
    """将普通 LaTeX 文本转为可嵌入 JS 反引号字符串的形式。"""
    # 反斜杠双写；反引号转义；${ 转义（避免模板字符串插值）
    s = s.replace("\\", "\\\\")
    s = s.replace("`", "\\`")
    s = s.replace("${", "\\${")
    return s

# ============================================================
# SVG 图库（通用，按需引用）
# ============================================================
def fig_svg(key):
    S='font-family="system-ui,sans-serif" font-size="11" fill="#475569"'
    figs = {
        # ===== 通用 =====
        "line": f'<svg viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="160" x2="320" y2="160" stroke="#94a3b8" stroke-width="1.4"/><line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="1.4"/><line x1="40" y1="180" x2="310" y2="40" stroke="#2563eb" stroke-width="2.4"/><polygon points="310,40 302,48 306,52" fill="#2563eb"/></svg>',
        "curve": f'<svg viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg" {S}><path d="M40,160 Q120,40 200,120 T320,80" fill="none" stroke="#2563eb" stroke-width="2.4"/></svg>',
        "circle": f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="100" cy="100" r="70" fill="none" stroke="#2563eb" stroke-width="2.4"/><circle cx="100" cy="100" r="3" fill="#0f172a"/></svg>',
        "triangle": f'<svg viewBox="0 0 200 180" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="100,20 180,160 20,160" fill="none" stroke="#2563eb" stroke-width="2.4"/></svg>',
        "wave": f'<svg viewBox="0 0 340 120" xmlns="http://www.w3.org/2000/svg" {S}><path d="M20,60 Q60,10 100,60 T180,60 T260,60 T340,60" fill="none" stroke="#2563eb" stroke-width="2.4"/><line x1="20" y1="60" x2="340" y2="60" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/></svg>',
        "atom": f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" {S}><ellipse cx="100" cy="100" rx="80" ry="30" fill="none" stroke="#2563eb" stroke-width="1.8"/><ellipse cx="100" cy="100" rx="80" ry="30" fill="none" stroke="#7c3aed" stroke-width="1.8" transform="rotate(60 100 100)"/><ellipse cx="100" cy="100" rx="80" ry="30" fill="none" stroke="#dc2626" stroke-width="1.8" transform="rotate(120 100 100)"/><circle cx="100" cy="100" r="10" fill="#fbbf24"/></svg>',
        "lens": f'<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="80" x2="220" y2="80" stroke="#94a3b8" stroke-width="1"/><ellipse cx="120" cy="80" rx="14" ry="60" fill="rgba(37,99,235,.15)" stroke="#2563eb" stroke-width="2"/><line x1="20" y1="80" x2="120" y2="80" stroke="#2563eb" stroke-width="1.8"/><line x1="120" y1="80" x2="220" y2="80" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="5,4"/></svg>',
        # ===== 力学 =====
        "inclined-plane": f'<svg viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="20,160 280,160 280,60" fill="rgba(37,99,235,.08)" stroke="#2563eb" stroke-width="1.5"/><rect x="180" y="90" width="36" height="26" rx="3" fill="#7c3aed" stroke="#4c1d95" stroke-width="1.5" transform="rotate(-26.6 198 103)"/><line x1="198" y1="103" x2="198" y2="145" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="4,3"/><polygon points="198,145 193,137 203,137" fill="#dc2626"/><text x="205" y="128" fill="#dc2626">mg</text><text x="250" y="120" fill="#2563eb">θ</text></svg>',
        "pendulum": f'<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" {S}><line x1="100" y1="10" x2="100" y2="30" stroke="#475569" stroke-width="2"/><line x1="100" y1="30" x2="160" y2="180" stroke="#2563eb" stroke-width="1.8"/><line x1="100" y1="30" x2="100" y2="190" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/><circle cx="160" cy="180" r="14" fill="#7c3aed" stroke="#4c1d95" stroke-width="1.5"/><path d="M100,30 A170,170 0 0 1 184,80" fill="none" stroke="#dc2626" stroke-width="1" stroke-dasharray="3,3"/><text x="115" y="70" fill="#dc2626">θ</text><text x="155" y="155" fill="#475569">m</text></svg>',
        "spring": f'<svg viewBox="0 0 320 120" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="60" x2="60" y2="60" stroke="#475569" stroke-width="2"/><path d="M60,60 L72,30 L88,90 L104,30 L120,90 L136,30 L152,90 L168,30 L184,90 L200,60" fill="none" stroke="#2563eb" stroke-width="2"/><line x1="200" y1="60" x2="240" y2="60" stroke="#475569" stroke-width="2"/><rect x="240" y="40" width="50" height="40" rx="4" fill="#7c3aed" stroke="#4c1d95" stroke-width="1.5"/><text x="255" y="65" fill="#fff">m</text><text x="120" y="110" fill="#dc2626">k</text></svg>',
        "projectile": f'<svg viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="170" x2="320" y2="170" stroke="#94a3b8" stroke-width="1.4"/><line x1="30" y1="180" x2="30" y2="20" stroke="#94a3b8" stroke-width="1.4"/><path d="M30,170 Q170,10 310,170" fill="none" stroke="#2563eb" stroke-width="2.4"/><circle cx="30" cy="170" r="5" fill="#dc2626"/><line x1="30" y1="170" x2="80" y2="120" stroke="#dc2626" stroke-width="1.8"/><polygon points="80,120 74,128 78,132" fill="#dc2626"/><text x="84" y="118" fill="#dc2626">v₀</text><text x="165" y="30" fill="#2563eb">抛物线轨迹</text></svg>',
        "fbd": f'<svg viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg" {S}><rect x="80" y="90" width="60" height="50" rx="4" fill="none" stroke="#475569" stroke-width="1.5"/><line x1="110" y1="90" x2="110" y2="30" stroke="#2563eb" stroke-width="2"/><polygon points="110,30 104,40 116,40" fill="#2563eb"/><text x="118" y="55" fill="#2563eb">N</text><line x1="110" y1="140" x2="110" y2="200" stroke="#dc2626" stroke-width="2"/><polygon points="110,200 104,190 116,190" fill="#dc2626"/><text x="118" y="180" fill="#dc2626">mg</text><line x1="80" y1="115" x2="30" y2="115" stroke="#059669" stroke-width="2"/><polygon points="30,115 40,109 40,121" fill="#059669"/><text x="36" y="108" fill="#059669">f</text><line x1="140" y1="115" x2="190" y2="115" stroke="#7c3aed" stroke-width="2"/><polygon points="190,115 180,109 180,121" fill="#7c3aed"/><text x="170" y="108" fill="#7c3aed">F</text></svg>',
        # ===== 热学 =====
        "pv-diagram": f'<svg viewBox="0 0 280 220" xmlns="http://www.w3.org/2000/svg" {S}><line x1="40" y1="190" x2="260" y2="190" stroke="#475569" stroke-width="1.5"/><polygon points="260,190 252,186 252,194" fill="#475569"/><line x1="40" y1="190" x2="40" y2="20" stroke="#475569" stroke-width="1.5"/><polygon points="40,20 36,28 44,28" fill="#475569"/><path d="M70,160 Q130,40 220,80" fill="none" stroke="#2563eb" stroke-width="2.4"/><circle cx="70" cy="160" r="4" fill="#dc2626"/><circle cx="220" cy="80" r="4" fill="#dc2626"/><text x="262" y="186" fill="#475569">V</text><text x="30" y="22" fill="#475569">P</text><text x="58" y="175" fill="#dc2626">1</text><text x="226" y="78" fill="#dc2626">2</text></svg>',
        "heat-engine": f'<svg viewBox="0 0 280 180" xmlns="http://www.w3.org/2000/svg" {S}><rect x="100" y="50" width="80" height="80" rx="8" fill="rgba(124,58,237,.12)" stroke="#7c3aed" stroke-width="2"/><text x="125" y="95" fill="#7c3aed">热机</text><path d="M60,30 L100,60" stroke="#dc2626" stroke-width="2" fill="none"/><polygon points="100,60 92,56 96,66" fill="#dc2626"/><text x="40" y="25" fill="#dc2626">Q₁</text><path d="M180,120 L220,160" stroke="#2563eb" stroke-width="2" fill="none"/><polygon points="220,160 212,152 222,154" fill="#2563eb"/><text x="222" y="172" fill="#2563eb">Q₂</text><path d="M220,70 L260,70" stroke="#059669" stroke-width="2" fill="none"/><polygon points="260,70 252,66 252,74" fill="#059669"/><text x="222" y="60" fill="#059669">W</text></svg>',
        "carnot": f'<svg viewBox="0 0 280 220" xmlns="http://www.w3.org/2000/svg" {S}><line x1="40" y1="190" x2="260" y2="190" stroke="#475569" stroke-width="1.4"/><line x1="40" y1="190" x2="40" y2="20" stroke="#475569" stroke-width="1.4"/><path d="M70,150 Q120,60 160,70" fill="none" stroke="#dc2626" stroke-width="2"/><path d="M160,70 L180,110" fill="none" stroke="#059669" stroke-width="2" stroke-dasharray="5,3"/><path d="M180,110 Q130,170 80,160" fill="none" stroke="#2563eb" stroke-width="2"/><path d="M80,160 L70,150" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="5,3"/><text x="120" y="50" fill="#dc2626">等温膨胀</text><text x="180" y="180" fill="#2563eb">等温压缩</text></svg>',
        # ===== 电磁学 =====
        "e-field": f'<svg viewBox="0 0 260 180" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="130" cy="90" r="12" fill="#dc2626"/><text x="124" y="94" fill="#fff">+</text><line x1="130" y1="30" x2="130" y2="60" stroke="#2563eb" stroke-width="1.8"/><polygon points="130,60 125,52 135,52" fill="#2563eb"/><line x1="130" y1="120" x2="130" y2="160" stroke="#2563eb" stroke-width="1.8"/><polygon points="130,160 125,152 135,152" fill="#2563eb"/><line x1="60" y1="90" x2="100" y2="90" stroke="#2563eb" stroke-width="1.8"/><polygon points="100,90 92,85 92,95" fill="#2563eb"/><line x1="160" y1="90" x2="200" y2="90" stroke="#2563eb" stroke-width="1.8"/><polygon points="200,90 192,85 192,95" fill="#2563eb"/><line x1="75" y1="40" x2="105" y2="65" stroke="#2563eb" stroke-width="1.8"/><polygon points="105,65 97,60 99,70" fill="#2563eb"/><line x1="185" y1="40" x2="155" y2="65" stroke="#2563eb" stroke-width="1.8"/><polygon points="155,65 163,60 161,70" fill="#2563eb"/></svg>',
        "b-field": f'<svg viewBox="0 0 260 160" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="80" x2="240" y2="80" stroke="#dc2626" stroke-width="2.5"/><polygon points="240,80 230,75 230,85" fill="#dc2626"/><circle cx="130" cy="80" r="14" fill="#2563eb" stroke="#1e40af" stroke-width="1.5"/><text x="125" y="85" fill="#fff">I</text><text x="100" y="60" fill="#dc2626">B</text><text x="100" y="105" fill="#dc2626">B</text><path d="M130,80 m-50,0 a50,50 0 0 1 100,0" fill="none" stroke="#2563eb" stroke-width="1" stroke-dasharray="4,3" opacity=".5"/></svg>',
        "capacitor": f'<svg viewBox="0 0 260 160" xmlns="http://www.w3.org/2000/svg" {S}><line x1="100" y1="20" x2="100" y2="50" stroke="#475569" stroke-width="2"/><line x1="100" y1="110" x2="100" y2="140" stroke="#475569" stroke-width="2"/><line x1="60" y1="50" x2="140" y2="50" stroke="#2563eb" stroke-width="3"/><line x1="60" y1="110" x2="140" y2="110" stroke="#dc2626" stroke-width="3"/><text x="150" y="46" fill="#2563eb">+Q</text><text x="150" y="114" fill="#dc2626">-Q</text><text x="40" y="85" fill="#475569">d</text><line x1="60" y1="80" x2="55" y2="80" stroke="#475569"/><line x1="60" y1="60" x2="55" y2="60" stroke="#475569"/><line x1="57" y1="60" x2="57" y2="80" stroke="#475569"/></svg>',
        "inductor": f'<svg viewBox="0 0 280 120" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="60" x2="80" y2="60" stroke="#475569" stroke-width="2"/><path d="M80,60 Q90,30 100,60 Q110,90 120,60 Q130,30 140,60 Q150,90 160,60 Q170,30 180,60 Q190,90 200,60" fill="none" stroke="#7c3aed" stroke-width="2"/><line x1="200" y1="60" x2="260" y2="60" stroke="#475569" stroke-width="2"/><text x="120" y="110" fill="#7c3aed">L</text></svg>',
        "circuit-loop": f'<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" {S}><rect x="40" y="40" width="220" height="120" fill="none" stroke="#475569" stroke-width="2"/><line x1="40" y1="100" x2="20" y2="100" stroke="#dc2626" stroke-width="2.5"/><line x1="20" y1="90" x2="20" y2="110" stroke="#dc2626" stroke-width="2.5"/><text x="5" y="105" fill="#dc2626">ε</text><rect x="130" y="50" width="40" height="20" fill="none" stroke="#2563eb" stroke-width="2"/><text x="140" y="65" fill="#2563eb">R</text><path d="M260,60 L270,55 L270,65 Z" fill="#059669"/><path d="M130,160 L120,155 L120,165 Z" fill="#059669"/><text x="140" y="175" fill="#059669">I</text></svg>',
        # ===== 光学 =====
        "reflection": f'<svg viewBox="0 0 300 160" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="110" x2="280" y2="110" stroke="#475569" stroke-width="2"/><line x1="150" y1="110" x2="150" y2="20" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/><line x1="60" y1="40" x2="150" y2="110" stroke="#2563eb" stroke-width="2.4"/><polygon points="60,40 68,50 62,54" fill="#2563eb"/><line x1="150" y1="110" x2="240" y2="40" stroke="#dc2626" stroke-width="2.4"/><polygon points="240,40 230,44 236,54" fill="#dc2626"/><text x="155" y="70" fill="#94a3b8">法线</text><text x="100" y="80" fill="#2563eb">θ₁</text><text x="170" y="80" fill="#dc2626">θ₂</text></svg>',
        "refraction": f'<svg viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="100" x2="280" y2="100" stroke="#475569" stroke-width="2"/><line x1="150" y1="100" x2="150" y2="20" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/><line x1="150" y1="100" x2="150" y2="170" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/><line x1="60" y1="30" x2="150" y2="100" stroke="#2563eb" stroke-width="2.4"/><polygon points="60,30 68,40 62,44" fill="#2563eb"/><line x1="150" y1="100" x2="210" y2="160" stroke="#dc2626" stroke-width="2.4"/><polygon points="210,160 200,156 204,166" fill="#dc2626"/><text x="110" y="70" fill="#2563eb">θ₁</text><text x="160" y="135" fill="#dc2626">θ₂</text><text x="30" y="90" fill="#475569">n₁</text><text x="30" y="120" fill="#475569">n₂</text></svg>',
        "double-slit": f'<svg viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg" {S}><line x1="40" y1="20" x2="40" y2="160" stroke="#475569" stroke-width="2"/><line x1="40" y1="70" x2="55" y2="70" stroke="#2563eb" stroke-width="2"/><line x1="40" y1="110" x2="55" y2="110" stroke="#2563eb" stroke-width="2"/><line x1="160" y1="20" x2="160" y2="160" stroke="#475569" stroke-width="2"/><line x1="160" y1="80" x2="175" y2="80" stroke="#dc2626" stroke-width="2"/><line x1="160" y1="100" x2="175" y2="100" stroke="#dc2626" stroke-width="2"/><line x1="280" y1="20" x2="280" y2="160" stroke="#475569" stroke-width="2"/><rect x="278" y="40" width="6" height="20" fill="#2563eb"/><rect x="278" y="65" width="6" height="10" fill="#fff" stroke="#94a3b8"/><rect x="278" y="80" width="6" height="20" fill="#2563eb"/><rect x="278" y="105" width="6" height="10" fill="#fff" stroke="#94a3b8"/><rect x="278" y="120" width="6" height="20" fill="#2563eb"/><text x="80" y="95" fill="#475569">双缝</text><text x="190" y="95" fill="#475569">屏</text></svg>',
        # ===== 量子 =====
        "wavefunction": f'<svg viewBox="0 0 340 160" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="80" x2="320" y2="80" stroke="#94a3b8" stroke-width="1"/><path d="M20,80 Q60,20 100,80 T180,80 T260,80 T320,80" fill="none" stroke="#2563eb" stroke-width="2.4"/><path d="M20,80 Q60,20 100,80 T180,80 T260,80 T320,80 L320,80 L20,80 Z" fill="rgba(37,99,235,.1)"/><text x="140" y="140" fill="#475569">|ψ(x)|² 概率密度</text></svg>',
        "energy-level": f'<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" {S}><line x1="60" y1="190" x2="140" y2="190" stroke="#475569" stroke-width="2"/><line x1="60" y1="150" x2="140" y2="150" stroke="#2563eb" stroke-width="2"/><line x1="60" y1="110" x2="140" y2="110" stroke="#7c3aed" stroke-width="2"/><line x1="60" y1="70" x2="140" y2="70" stroke="#dc2626" stroke-width="2"/><line x1="60" y1="35" x2="140" y2="35" stroke="#059669" stroke-width="2" stroke-dasharray="5,3"/><text x="148" y="194" fill="#475569">n=1</text><text x="148" y="154" fill="#2563eb">n=2</text><text x="148" y="114" fill="#7c3aed">n=3</text><text x="148" y="74" fill="#dc2626">n=4</text><text x="148" y="39" fill="#059669">E→∞</text></svg>',
        "uncertainty": f'<svg viewBox="0 0 300 160" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="80" x2="270" y2="80" stroke="#94a3b8" stroke-width="1"/><path d="M30,80 L100,80 Q150,20 200,80 L270,80" fill="none" stroke="#2563eb" stroke-width="2.4"/><text x="130" y="50" fill="#2563eb">Δx</text><line x1="80" y1="120" x2="220" y2="120" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,3"/><text x="130" y="145" fill="#dc2626">Δp</text><text x="100" y="100" fill="#7c3aed">Δx·Δp ≥ ℏ/2</text></svg>',
        # ===== 相对论 =====
        "spacetime": f'<svg viewBox="0 0 260 260" xmlns="http://www.w3.org/2000/svg" {S}><line x1="130" y1="20" x2="130" y2="240" stroke="#475569" stroke-width="1.5"/><polygon points="130,20 126,28 134,28" fill="#475569"/><line x1="20" y1="130" x2="240" y2="130" stroke="#475569" stroke-width="1.5"/><polygon points="240,130 232,126 232,134" fill="#475569"/><line x1="30" y1="230" x2="230" y2="30" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="5,3"/><line x1="30" y1="30" x2="230" y2="230" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="5,3"/><text x="138" y="30" fill="#475569">ct</text><text x="232" y="124" fill="#475569">x</text><text x="170" y="60" fill="#2563eb">光锥</text><circle cx="130" cy="130" r="4" fill="#dc2626"/></svg>',
        # ===== 统计 =====
        "maxwell-boltzmann": f'<svg viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="160" x2="280" y2="160" stroke="#475569" stroke-width="1.4"/><line x1="30" y1="160" x2="30" y2="20" stroke="#475569" stroke-width="1.4"/><path d="M30,155 Q80,30 140,50 Q200,70 270,150" fill="none" stroke="#2563eb" stroke-width="2.4"/><path d="M30,155 Q80,30 140,50 Q200,70 270,150 L270,160 L30,160 Z" fill="rgba(37,99,235,.12)"/><text x="265" y="175" fill="#475569">v</text><text x="10" y="25" fill="#475569">f(v)</text><text x="120" y="45" fill="#2563eb">麦克斯韦分布</text></svg>',
        # ===== 固体 =====
        "band-theory": f'<svg viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg" {S}><line x1="40" y1="160" x2="260" y2="160" stroke="#94a3b8" stroke-width="1"/><rect x="80" y="110" width="140" height="40" fill="rgba(37,99,235,.2)" stroke="#2563eb" stroke-width="1.5"/><text x="130" y="134" fill="#2563eb">价带</text><rect x="80" y="30" width="140" height="40" fill="rgba(220,38,38,.15)" stroke="#dc2626" stroke-width="1.5"/><text x="130" y="54" fill="#dc2626">导带</text><line x1="150" y1="70" x2="150" y2="110" stroke="#7c3aed" stroke-width="2" stroke-dasharray="5,3"/><text x="158" y="95" fill="#7c3aed">Eg</text><text x="30" y="120" fill="#475569">E</text></svg>',
        "bravais": f'<svg viewBox="0 0 260 180" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="40" cy="40" r="6" fill="#2563eb"/><circle cx="120" cy="40" r="6" fill="#2563eb"/><circle cx="200" cy="40" r="6" fill="#2563eb"/><circle cx="40" cy="100" r="6" fill="#2563eb"/><circle cx="120" cy="100" r="6" fill="#7c3aed"/><circle cx="200" cy="100" r="6" fill="#2563eb"/><circle cx="40" cy="160" r="6" fill="#2563eb"/><circle cx="120" cy="160" r="6" fill="#2563eb"/><circle cx="200" cy="160" r="6" fill="#2563eb"/><line x1="40" y1="40" x2="200" y2="40" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/><line x1="40" y1="100" x2="200" y2="100" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/><line x1="40" y1="160" x2="200" y2="160" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/><text x="210" y="104" fill="#7c3aed">基元</text></svg>',
        # ===== 初等数学 =====
        "xy-axes": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#475569" stroke-width="1.6"/><polygon points="280,200 270,196 270,204" fill="#475569"/><line x1="150" y1="220" x2="150" y2="20" stroke="#475569" stroke-width="1.6"/><polygon points="150,20 146,30 154,30" fill="#475569"/><text x="268" y="220" fill="#475569">x</text><text x="156" y="28" fill="#475569">y</text><text x="140" y="216" fill="#475569">O</text></svg>',
        "line-yx": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><line x1="40" y1="210" x2="260" y2="30" stroke="#2563eb" stroke-width="2.4"/><text x="262" y="36" fill="#2563eb">y=x</text><text x="268" y="208" fill="#475569">x</text><text x="156" y="28" fill="#475569">y</text></svg>',
        "parabola-yx2": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M40,180 Q150,40 260,180" fill="none" stroke="#2563eb" stroke-width="2.4"/><text x="240" y="170" fill="#2563eb">y=x²</text><text x="268" y="208" fill="#475569">x</text><text x="156" y="28" fill="#475569">y</text></svg>',
        "cubic-yx3": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M40,190 Q90,180 150,120 Q210,60 260,40" fill="none" stroke="#2563eb" stroke-width="2.4"/><text x="232" y="38" fill="#2563eb">y=x³</text><text x="268" y="208" fill="#475569">x</text><text x="156" y="28" fill="#475569">y</text></svg>',
        "sqrt-x": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M150,200 Q200,140 260,110" fill="none" stroke="#2563eb" stroke-width="2.4"/><text x="220" y="100" fill="#2563eb">y=√x</text><text x="268" y="208" fill="#475569">x</text><text x="156" y="28" fill="#475569">y</text></svg>',
        "hyperbola-1overx": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M50,200 Q90,120 140,60" fill="none" stroke="#2563eb" stroke-width="2.4"/><path d="M160,340 Q210,240 250,200" fill="none" stroke="#2563eb" stroke-width="2.4"/><path d="M160,60 Q210,150 250,200" fill="none" stroke="#2563eb" stroke-width="2.4" transform="translate(0,-20)"/><text x="226" y="100" fill="#2563eb">y=1/x</text></svg>',
        "exp-y": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M40,196 Q100,194 150,120 Q200,40 260,30" fill="none" stroke="#2563eb" stroke-width="2.4"/><text x="220" y="26" fill="#2563eb">y=eˣ</text></svg>',
        "ln-y": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M150,210 Q210,120 260,60" fill="none" stroke="#2563eb" stroke-width="2.4"/><path d="M40,340 Q110,230 150,160" fill="none" stroke="#2563eb" stroke-width="2.4" transform="translate(0,-100)"/><text x="226" y="52" fill="#2563eb">y=ln x</text></svg>',
        "sin-curve": f'<svg viewBox="0 0 340 160" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="80" x2="330" y2="80" stroke="#94a3b8" stroke-width="1"/><path d="M20,80 Q60,20 100,80 T180,80 T260,80 T340,80" fill="none" stroke="#2563eb" stroke-width="2.4"/><text x="300" y="40" fill="#2563eb">sin x</text><line x1="60" y1="80" x2="60" y2="86" stroke="#475569"/><text x="56" y="100" fill="#475569">π</text></svg>',
        "cos-curve": f'<svg viewBox="0 0 340 160" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="80" x2="330" y2="80" stroke="#94a3b8" stroke-width="1"/><path d="M20,20 Q60,80 100,140 T180,80 T260,20 T340,80" fill="none" stroke="#dc2626" stroke-width="2.4"/><text x="300" y="30" fill="#dc2626">cos x</text></svg>',
        "tan-curve": f'<svg viewBox="0 0 340 160" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="80" x2="330" y2="80" stroke="#94a3b8" stroke-width="1"/><line x1="100" y1="20" x2="100" y2="140" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/><line x1="220" y1="20" x2="220" y2="140" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/><path d="M40,130 Q60,80 90,30" fill="none" stroke="#7c3aed" stroke-width="2.4"/><path d="M110,150 Q140,80 170,10" fill="none" stroke="#7c3aed" stroke-width="2.4"/><path d="M230,140 Q260,80 290,20" fill="none" stroke="#7c3aed" stroke-width="2.4"/><text x="300" y="30" fill="#7c3aed">tan x</text></svg>',
        "abs-x": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M40,110 L150,200 L260,110" fill="none" stroke="#2563eb" stroke-width="2.4"/><text x="230" y="100" fill="#2563eb">y=|x|</text></svg>',
        "floor-x": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="200" x2="280" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M40,160 L90,160 M90,140 L140,140 M140,120 L200,120 M200,100 L260,100" fill="none" stroke="#2563eb" stroke-width="2.4"/><circle cx="90" cy="160" r="3" fill="#fff" stroke="#2563eb" stroke-width="1.5"/><circle cx="90" cy="140" r="3" fill="#2563eb"/><circle cx="140" cy="140" r="3" fill="#fff" stroke="#2563eb" stroke-width="1.5"/><circle cx="140" cy="120" r="3" fill="#2563eb"/><circle cx="200" cy="120" r="3" fill="#fff" stroke="#2563eb" stroke-width="1.5"/><circle cx="200" cy="100" r="3" fill="#2563eb"/><text x="226" y="94" fill="#2563eb">y=⌊x⌋</text></svg>',
        "tri-right": f'<svg viewBox="0 0 260 200" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="40,160 220,160 40,40" fill="rgba(37,99,235,.08)" stroke="#2563eb" stroke-width="2.4"/><polygon points="40,140 60,140 60,160" fill="none" stroke="#475569" stroke-width="1.2"/><text x="120" y="178" fill="#475569">a</text><text x="20" y="105" fill="#475569">b</text><text x="130" y="95" fill="#2563eb">c</text><text x="50" y="148" fill="#7c3aed">C=90°</text></svg>',
        "tri-centers": f'<svg viewBox="0 0 260 220" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="130,30 230,180 30,180" fill="none" stroke="#2563eb" stroke-width="2"/><line x1="130" y1="30" x2="130" y2="180" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,3"/><line x1="30" y1="180" x2="180" y2="105" stroke="#059669" stroke-width="1" stroke-dasharray="4,3"/><line x1="230" y1="180" x2="80" y2="105" stroke="#7c3aed" stroke-width="1" stroke-dasharray="4,3"/><circle cx="130" cy="130" r="4" fill="#dc2626"/><text x="138" y="128" fill="#dc2626">G重心</text></svg>',
        "circle-parts": f'<svg viewBox="0 0 260 260" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="130" cy="130" r="90" fill="none" stroke="#2563eb" stroke-width="2.4"/><line x1="130" y1="130" x2="220" y2="130" stroke="#dc2626" stroke-width="1.8"/><line x1="50" y1="130" x2="210" y2="130" stroke="#059669" stroke-width="1.5" stroke-dasharray="4,3"/><line x1="130" y1="130" x2="130" y2="40" stroke="#7c3aed" stroke-width="1.8"/><circle cx="130" cy="130" r="3" fill="#0f172a"/><text x="170" y="122" fill="#dc2626">r半径</text><text x="160" y="75" fill="#7c3aed">r</text><text x="130" y="230" fill="#475569">直径 d=2r</text></svg>',
        "ellipse": f'<svg viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="100" x2="320" y2="100" stroke="#94a3b8" stroke-width="1"/><line x1="170" y1="170" x2="170" y2="30" stroke="#94a3b8" stroke-width="1"/><ellipse cx="170" cy="100" rx="120" ry="60" fill="none" stroke="#2563eb" stroke-width="2.4"/><circle cx="130" cy="100" r="3" fill="#dc2626"/><circle cx="210" cy="100" r="3" fill="#dc2626"/><text x="120" y="120" fill="#dc2626">F₁</text><text x="214" y="120" fill="#dc2626">F₂</text><text x="280" y="96" fill="#2563eb">a</text><text x="166" y="40" fill="#7c3aed">b</text></svg>',
        "parabola-conic": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="180" x2="280" y2="180" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="220" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M40,190 Q150,30 260,190" fill="none" stroke="#2563eb" stroke-width="2.4"/><line x1="150" y1="140" x2="150" y2="180" stroke="#dc2626" stroke-width="1.5"/><circle cx="150" cy="140" r="3" fill="#dc2626"/><text x="156" y="138" fill="#dc2626">F</text><line x1="60" y1="200" x2="240" y2="200" stroke="#7c3aed" stroke-width="1.2" stroke-dasharray="4,3"/><text x="244" y="204" fill="#7c3aed">准线l</text></svg>',
        "hyperbola-conic": f'<svg viewBox="0 0 340 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="120" x2="320" y2="120" stroke="#94a3b8" stroke-width="1"/><line x1="170" y1="20" x2="170" y2="220" stroke="#94a3b8" stroke-width="1"/><path d="M40,40 Q90,120 40,200" fill="none" stroke="#2563eb" stroke-width="2.4"/><path d="M300,40 Q250,120 300,200" fill="none" stroke="#2563eb" stroke-width="2.4"/><line x1="70" y1="30" x2="270" y2="210" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/><line x1="70" y1="210" x2="270" y2="30" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/><circle cx="90" cy="120" r="3" fill="#dc2626"/><circle cx="250" cy="120" r="3" fill="#dc2626"/></svg>',
        "polar-coord": f'<svg viewBox="0 0 280 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="120" x2="260" y2="120" stroke="#94a3b8" stroke-width="1.2"/><polygon points="260,120 252,116 252,124" fill="#94a3b8"/><circle cx="140" cy="120" r="3" fill="#0f172a"/><circle cx="140" cy="120" r="50" fill="none" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3,3"/><circle cx="140" cy="120" r="85" fill="none" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3,3"/><line x1="140" y1="120" x2="210" y2="60" stroke="#2563eb" stroke-width="2"/><circle cx="210" cy="60" r="4" fill="#dc2626"/><path d="M170,120 A30,30 0 0 0 163,105" fill="none" stroke="#7c3aed" stroke-width="1.5"/><text x="214" y="58" fill="#dc2626">P(r,θ)</text><text x="175" y="112" fill="#7c3aed">θ</text><text x="168" y="92" fill="#2563eb">r</text><text x="262" y="128" fill="#94a3b8">极轴</text></svg>',
        "polar-rose": f'<svg viewBox="0 0 280 280" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="140" x2="260" y2="140" stroke="#94a3b8" stroke-width="1"/><line x1="140" y1="20" x2="140" y2="260" stroke="#94a3b8" stroke-width="1"/><circle cx="140" cy="140" r="3" fill="#0f172a"/><path d="M140,140 L140,60 A40,40 0 0 1 175,95 Z" fill="rgba(37,99,235,.15)" stroke="#2563eb" stroke-width="1.8"/><path d="M140,140 L140,60 A40,40 0 0 1 105,95 Z" fill="rgba(37,99,235,.15)" stroke="#2563eb" stroke-width="1.8"/><path d="M140,140 L140,220 A40,40 0 0 1 175,185 Z" fill="rgba(37,99,235,.15)" stroke="#2563eb" stroke-width="1.8"/><path d="M140,140 L140,220 A40,40 0 0 1 105,185 Z" fill="rgba(37,99,235,.15)" stroke="#2563eb" stroke-width="1.8"/><path d="M140,140 L60,140 A40,40 0 0 1 95,105 Z" fill="rgba(37,99,235,.15)" stroke="#2563eb" stroke-width="1.8"/><path d="M140,140 L60,140 A40,40 0 0 1 95,175 Z" fill="rgba(37,99,235,.15)" stroke="#2563eb" stroke-width="1.8"/><path d="M140,140 L220,140 A40,40 0 0 1 185,105 Z" fill="rgba(37,99,235,.15)" stroke="#2563eb" stroke-width="1.8"/><path d="M140,140 L220,140 A40,40 0 0 1 185,175 Z" fill="rgba(37,99,235,.15)" stroke="#2563eb" stroke-width="1.8"/><text x="210" y="40" fill="#2563eb">r=cos4θ</text></svg>',
        "polar-cardioid": f'<svg viewBox="0 0 280 280" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="140" x2="260" y2="140" stroke="#94a3b8" stroke-width="1"/><line x1="140" y1="20" x2="140" y2="260" stroke="#94a3b8" stroke-width="1"/><circle cx="140" cy="140" r="3" fill="#0f172a"/><path d="M140,140 m-70,0 a70,70 0 1 0 140,0 a50,50 0 1 0 -140,0" fill="none" stroke="#2563eb" stroke-width="2.2"/><path d="M140,140 m-40,0 a40,40 0 1 0 80,0 a30,30 0 1 0 -80,0" fill="rgba(37,99,235,.1)" stroke="#2563eb" stroke-width="2"/><text x="200" y="50" fill="#2563eb">心形线</text><text x="200" y="70" fill="#2563eb">r=a(1+cosθ)</text></svg>',
        "polar-spiral": f'<svg viewBox="0 0 280 280" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="140" x2="260" y2="140" stroke="#94a3b8" stroke-width="1"/><line x1="140" y1="20" x2="140" y2="260" stroke="#94a3b8" stroke-width="1"/><circle cx="140" cy="140" r="3" fill="#0f172a"/><path d="M140,140 Q160,140 170,110 Q180,70 140,60 Q90,50 80,100 Q70,160 130,170 Q200,180 210,110" fill="none" stroke="#2563eb" stroke-width="2.2"/><text x="180" y="50" fill="#2563eb">阿基米德螺线</text><text x="200" y="70" fill="#2563eb">r=aθ</text></svg>',
        "param-circle": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="180" x2="270" y2="180" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="210" x2="150" y2="20" stroke="#94a3b8" stroke-width="1"/><circle cx="150" cy="120" r="70" fill="none" stroke="#2563eb" stroke-width="2.4"/><circle cx="150" cy="120" r="3" fill="#0f172a"/><line x1="150" y1="120" x2="220" y2="70" stroke="#dc2626" stroke-width="1.5"/><circle cx="220" cy="70" r="4" fill="#dc2626"/><text x="224" y="66" fill="#dc2626">P(x,y)</text><text x="170" y="100" fill="#7c3aed">t</text><text x="230" y="188" fill="#94a3b8">x=acost</text><text x="230" y="204" fill="#94a3b8">y=asint</text></svg>',
        "param-ellipse": f'<svg viewBox="0 0 340 240" xmlns="http://www.w3.org/2000/svg" {S}><line x1="20" y1="120" x2="320" y2="120" stroke="#94a3b8" stroke-width="1"/><line x1="170" y1="210" x2="170" y2="20" stroke="#94a3b8" stroke-width="1"/><ellipse cx="170" cy="120" rx="120" ry="70" fill="none" stroke="#2563eb" stroke-width="2.4"/><text x="290" y="116" fill="#2563eb">x=acost</text><text x="290" y="136" fill="#7c3aed">y=bsint</text></svg>',
        "3d-axes": f'<svg viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg" {S}><line x1="150" y1="230" x2="150" y2="30" stroke="#475569" stroke-width="1.6"/><polygon points="150,30 146,40 154,40" fill="#475569"/><line x1="150" y1="130" x2="60" y2="200" stroke="#475569" stroke-width="1.6"/><polygon points="60,200 70,196 66,206" fill="#475569"/><line x1="150" y1="130" x2="260" y2="180" stroke="#475569" stroke-width="1.6"/><polygon points="260,180 250,176 254,186" fill="#475569"/><text x="156" y="36" fill="#475569">z</text><text x="50" y="210" fill="#475569">x</text><text x="262" y="178" fill="#475569">y</text><text x="156" y="130" fill="#475569">O</text></svg>',
        "cube-3d": f'<svg viewBox="0 0 260 240" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="60,180 180,180 220,140 100,140" fill="rgba(37,99,235,.12)" stroke="#2563eb" stroke-width="2"/><polygon points="60,180 60,80 100,40 100,140" fill="rgba(124,58,237,.12)" stroke="#7c3aed" stroke-width="2"/><polygon points="100,40 220,40 220,140 100,140" fill="rgba(220,38,38,.1)" stroke="#dc2626" stroke-width="2"/><polygon points="180,180 220,140 220,40 180,80" fill="none" stroke="#2563eb" stroke-width="2"/><line x1="60" y1="80" x2="180" y2="80" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/><line x1="180" y1="80" x2="180" y2="180" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/></svg>',
        "sphere-3d": f'<svg viewBox="0 0 260 260" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="130" cy="130" r="90" fill="rgba(37,99,235,.08)" stroke="#2563eb" stroke-width="2.4"/><ellipse cx="130" cy="130" rx="90" ry="30" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/><ellipse cx="130" cy="130" rx="30" ry="90" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/><line x1="130" y1="130" x2="220" y2="130" stroke="#dc2626" stroke-width="1.8"/><circle cx="130" cy="130" r="3" fill="#0f172a"/><text x="170" y="122" fill="#dc2626">R</text><text x="100" y="30" fill="#2563eb">x²+y²+z²=R²</text></svg>',
        "cylinder-3d": f'<svg viewBox="0 0 240 280" xmlns="http://www.w3.org/2000/svg" {S}><ellipse cx="120" cy="50" rx="70" ry="22" fill="rgba(37,99,235,.08)" stroke="#2563eb" stroke-width="2"/><ellipse cx="120" cy="230" rx="70" ry="22" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="5,4"/><line x1="50" y1="50" x2="50" y2="230" stroke="#2563eb" stroke-width="2"/><line x1="190" y1="50" x2="190" y2="230" stroke="#2563eb" stroke-width="2"/><ellipse cx="120" cy="230" rx="70" ry="22" fill="none" stroke="#94a3b8" stroke-width="1.2"/><line x1="120" y1="230" x2="190" y2="220" stroke="#dc2626" stroke-width="1.5"/><text x="150" y="218" fill="#dc2626">r</text><text x="130" y="148" fill="#2563eb">h</text><line x1="190" y1="72" x2="190" y2="230" stroke="#7c3aed" stroke-width="1" stroke-dasharray="3,3"/></svg>',
        "cone-3d": f'<svg viewBox="0 0 240 280" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="120,30 50,230 190,230" fill="rgba(37,99,235,.08)" stroke="#2563eb" stroke-width="2"/><ellipse cx="120" cy="230" rx="70" ry="22" fill="none" stroke="#2563eb" stroke-width="2"/><line x1="120" y1="30" x2="120" y2="230" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/><line x1="120" y1="230" x2="190" y2="220" stroke="#7c3aed" stroke-width="1.5"/><text x="110" y="140" fill="#dc2626">h</text><text x="150" y="222" fill="#7c3aed">r</text></svg>',
        "ellipsoid-3d": f'<svg viewBox="0 0 300 240" xmlns="http://www.w3.org/2000/svg" {S}><ellipse cx="150" cy="120" rx="120" ry="80" fill="rgba(37,99,235,.08)" stroke="#2563eb" stroke-width="2"/><ellipse cx="150" cy="120" rx="120" ry="28" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/><ellipse cx="150" cy="120" rx="45" ry="80" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/><text x="60" y="40" fill="#2563eb">x²/a²+y²/b²+z²/c²=1</text></svg>',
        "paraboloid-3d": f'<svg viewBox="0 0 280 260" xmlns="http://www.w3.org/2000/svg" {S}><path d="M40,220 Q140,40 240,220" fill="rgba(37,99,235,.1)" stroke="#2563eb" stroke-width="2"/><ellipse cx="140" cy="220" rx="100" ry="25" fill="none" stroke="#2563eb" stroke-width="2"/><ellipse cx="140" cy="180" rx="70" ry="18" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/><ellipse cx="140" cy="140" rx="40" ry="10" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/><line x1="140" y1="230" x2="140" y2="40" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,3"/><text x="60" y="30" fill="#2563eb">z=x²/a²+y²/b²</text></svg>',
        "hyperboloid-3d": f'<svg viewBox="0 0 280 260" xmlns="http://www.w3.org/2000/svg" {S}><path d="M40,200 Q80,100 140,80 Q200,100 240,200" fill="none" stroke="#2563eb" stroke-width="2"/><path d="M50,210 Q90,120 140,100 Q190,120 230,210" fill="none" stroke="#2563eb" stroke-width="2"/><ellipse cx="140" cy="100" rx="60" ry="16" fill="none" stroke="#dc2626" stroke-width="1.5"/><ellipse cx="140" cy="200" rx="100" ry="25" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/><text x="40" y="40" fill="#2563eb">单叶双曲面</text></svg>',
        "cone-surface-3d": f'<svg viewBox="0 0 280 260" xmlns="http://www.w3.org/2000/svg" {S}><line x1="140" y1="40" x2="60" y2="220" stroke="#2563eb" stroke-width="2"/><line x1="140" y1="40" x2="220" y2="220" stroke="#2563eb" stroke-width="2"/><ellipse cx="140" cy="220" rx="80" ry="20" fill="none" stroke="#2563eb" stroke-width="2"/><ellipse cx="140" cy="140" rx="45" ry="12" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/><line x1="140" y1="40" x2="140" y2="230" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,3"/><text x="60" y="30" fill="#2563eb">z²=x²+y² 锥面</text></svg>',
        "space-curve": f'<svg viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg" {S}><line x1="150" y1="230" x2="150" y2="30" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="130" x2="50" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="130" x2="260" y2="180" stroke="#94a3b8" stroke-width="1"/><path d="M100,180 Q130,100 160,120 Q190,140 210,70" fill="none" stroke="#2563eb" stroke-width="2.4"/><circle cx="100" cy="180" r="4" fill="#dc2626"/><circle cx="210" cy="70" r="4" fill="#dc2626"/><text x="200" y="60" fill="#2563eb">空间曲线</text></svg>',
        "helix": f'<svg viewBox="0 0 280 260" xmlns="http://www.w3.org/2000/svg" {S}><line x1="140" y1="240" x2="140" y2="20" stroke="#94a3b8" stroke-width="1"/><path d="M140,30 Q200,60 180,90 Q140,120 100,150 Q60,180 140,210 Q220,240 180,270" fill="none" stroke="#2563eb" stroke-width="2.2"/><ellipse cx="140" cy="60" rx="60" ry="15" fill="none" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3,3"/><ellipse cx="140" cy="150" rx="60" ry="15" fill="none" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3,3"/><ellipse cx="140" cy="240" rx="60" ry="15" fill="none" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3,3"/><text x="40" y="20" fill="#2563eb">螺旋线</text><text x="40" y="40" fill="#94a3b8">x=acost,y=asint,z=bt</text></svg>',
        "cylindrical-coord": f'<svg viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg" {S}><line x1="150" y1="230" x2="150" y2="30" stroke="#475569" stroke-width="1.4"/><line x1="150" y1="130" x2="50" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="130" x2="260" y2="180" stroke="#94a3b8" stroke-width="1"/><circle cx="150" cy="130" r="50" fill="none" stroke="#94a3b8" stroke-width="0.8" stroke-dasharray="3,3"/><circle cx="150" cy="130" r="3" fill="#0f172a"/><line x1="150" y1="130" x2="200" y2="110" stroke="#2563eb" stroke-width="1.8"/><line x1="200" y1="110" x2="200" y2="60" stroke="#7c3aed" stroke-width="1.8"/><circle cx="200" cy="60" r="4" fill="#dc2626"/><text x="206" y="60" fill="#dc2626">P</text><text x="170" y="116" fill="#2563eb">r</text><text x="206" y="90" fill="#7c3aed">z</text><text x="155" y="134" fill="#7c3aed">θ</text><text x="156" y="36" fill="#475569">z</text></svg>',
        "spherical-coord": f'<svg viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg" {S}><line x1="150" y1="230" x2="150" y2="30" stroke="#475569" stroke-width="1.4"/><line x1="150" y1="130" x2="50" y2="200" stroke="#94a3b8" stroke-width="1"/><line x1="150" y1="130" x2="260" y2="180" stroke="#94a3b8" stroke-width="1"/><circle cx="150" cy="130" r="3" fill="#0f172a"/><line x1="150" y1="130" x2="210" y2="70" stroke="#2563eb" stroke-width="1.8"/><circle cx="210" cy="70" r="4" fill="#dc2626"/><line x1="210" y1="70" x2="210" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/><line x1="150" y1="130" x2="210" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/><path d="M170,130 A20,20 0 0 0 166,116" fill="none" stroke="#7c3aed" stroke-width="1.5"/><path d="M150,110 A20,20 0 0 1 164,106" fill="none" stroke="#059669" stroke-width="1.5"/><text x="214" y="66" fill="#dc2626">P(r,φ,θ)</text><text x="176" y="100" fill="#2563eb">r</text><text x="174" y="118" fill="#7c3aed">θ</text><text x="158" y="106" fill="#059669">φ</text><text x="156" y="36" fill="#475569">z</text></svg>',
        "vector-add": f'<svg viewBox="0 0 280 180" xmlns="http://www.w3.org/2000/svg" {S}><line x1="40" y1="140" x2="180" y2="140" stroke="#2563eb" stroke-width="2"/><polygon points="180,140 170,136 170,144" fill="#2563eb"/><line x1="40" y1="140" x2="120" y2="60" stroke="#dc2626" stroke-width="2"/><polygon points="120,60 112,68 118,72" fill="#dc2626"/><line x1="120" y1="60" x2="260" y2="60" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/><line x1="180" y1="140" x2="260" y2="60" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/><line x1="40" y1="140" x2="260" y2="60" stroke="#7c3aed" stroke-width="2.4"/><polygon points="260,60 250,60 255,68" fill="#7c3aed"/><text x="100" y="156" fill="#2563eb">a</text><text x="70" y="100" fill="#dc2626">b</text><text x="160" y="92" fill="#7c3aed">a+b</text></svg>',
        "vector-dot": f'<svg viewBox="0 0 280 180" xmlns="http://www.w3.org/2000/svg" {S}><line x1="40" y1="140" x2="200" y2="140" stroke="#2563eb" stroke-width="2"/><polygon points="200,140 190,136 190,144" fill="#2563eb"/><line x1="40" y1="140" x2="140" y2="50" stroke="#dc2626" stroke-width="2"/><polygon points="140,50 132,58 138,62" fill="#dc2626"/><line x1="140" y1="50" x2="140" y2="140" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="4,3"/><path d="M90,140 A50,50 0 0 0 84,120" fill="none" stroke="#059669" stroke-width="1.5"/><text x="206" y="138" fill="#2563eb">a</text><text x="120" y="52" fill="#dc2626">b</text><text x="146" y="100" fill="#7c3aed">|b|cosθ</text><text x="94" y="128" fill="#059669">θ</text></svg>',
        "circle-inscribed": f'<svg viewBox="0 0 260 260" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="130" cy="130" r="90" fill="none" stroke="#2563eb" stroke-width="2"/><polygon points="130,50 208,180 52,180" fill="rgba(37,99,235,.08)" stroke="#dc2626" stroke-width="2"/><circle cx="130" cy="147" r="33" fill="none" stroke="#7c3aed" stroke-width="1.8"/><circle cx="130" cy="147" r="3" fill="#0f172a"/><text x="136" y="147" fill="#7c3aed">内心</text></svg>',
        "circle-circumscribed": f'<svg viewBox="0 0 260 260" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="130" cy="130" r="90" fill="none" stroke="#2563eb" stroke-width="2"/><polygon points="130,50 208,180 52,180" fill="rgba(37,99,235,.08)" stroke="#dc2626" stroke-width="2"/><circle cx="130" cy="130" r="3" fill="#0f172a"/><text x="138" y="128" fill="#2563eb">外心</text><line x1="130" y1="130" x2="130" y2="40" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="3,3"/></svg>',
        "tangent-chord": f'<svg viewBox="0 0 260 260" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="130" cy="130" r="80" fill="none" stroke="#2563eb" stroke-width="2"/><line x1="50" y1="60" x2="210" y2="200" stroke="#dc2626" stroke-width="2"/><line x1="50" y1="130" x2="210" y2="130" stroke="#7c3aed" stroke-width="1.8" stroke-dasharray="4,3"/><circle cx="130" cy="130" r="3" fill="#0f172a"/><circle cx="170" cy="170" r="4" fill="#dc2626"/><text x="176" y="170" fill="#dc2626">切点</text><text x="60" y="122" fill="#7c3aed">弦</text><text x="60" y="52" fill="#dc2626">切线</text></svg>',
        "intersecting-chords": f'<svg viewBox="0 0 260 260" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="130" cy="130" r="90" fill="none" stroke="#2563eb" stroke-width="2"/><line x1="50" y1="80" x2="210" y2="180" stroke="#dc2626" stroke-width="1.8"/><line x1="210" y1="80" x2="50" y2="180" stroke="#7c3aed" stroke-width="1.8"/><circle cx="130" cy="130" r="4" fill="#0f172a"/><text x="110" y="126" fill="#0f172a">P</text><text x="44" y="78" fill="#dc2626">A</text><text x="212" y="182" fill="#dc2626">B</text><text x="212" y="78" fill="#7c3aed">C</text><text x="40" y="182" fill="#7c3aed">D</text></svg>',
        "secant-tangent": f'<svg viewBox="0 0 280 240" xmlns="http://www.w3.org/2000/svg" {S}><circle cx="130" cy="120" r="70" fill="none" stroke="#2563eb" stroke-width="2"/><line x1="30" y1="200" x2="200" y2="60" stroke="#dc2626" stroke-width="2"/><line x1="200" y1="60" x2="270" y2="30" stroke="#7c3aed" stroke-width="2"/><circle cx="130" cy="120" r="3" fill="#0f172a"/><circle cx="110" y1="170" r="4" fill="#dc2626"/><circle cx="200" y2="60" r="4" fill="#7c3aed"/><text x="22" y="206" fill="#dc2626">P</text><text x="114" y="184" fill="#dc2626">A</text><text x="206" y="58" fill="#7c3aed">T</text><text x="274" y="30" fill="#7c3aed">切线</text></svg>',
        "similar-tri": f'<svg viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="40,150 120,150 80,60" fill="rgba(37,99,235,.12)" stroke="#2563eb" stroke-width="2"/><polygon points="160,150 260,150 210,40" fill="rgba(124,58,237,.12)" stroke="#7c3aed" stroke-width="2"/><text x="70" y="170" fill="#2563eb">△ABC</text><text x="195" y="170" fill="#7c3aed">△A′B′C′</text></svg>',
        "congruent-tri": f'<svg viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="40,150 130,150 80,50" fill="rgba(37,99,235,.12)" stroke="#2563eb" stroke-width="2"/><polygon points="170,150 260,150 210,50" fill="rgba(124,58,237,.12)" stroke="#7c3aed" stroke-width="2"/><text x="80" y="170" fill="#2563eb">△ABC</text><text x="210" y="170" fill="#7c3aed">△DEF</text></svg>',
        "parallel-lines": f'<svg viewBox="0 0 300 140" xmlns="http://www.w3.org/2000/svg" {S}><line x1="30" y1="50" x2="270" y2="50" stroke="#2563eb" stroke-width="2"/><line x1="30" y1="100" x2="270" y2="100" stroke="#2563eb" stroke-width="2"/><line x1="80" y1="20" x2="200" y2="130" stroke="#dc2626" stroke-width="1.5"/><text x="40" y="42" fill="#2563eb">l₁</text><text x="40" y="116" fill="#2563eb">l₂</text><text x="206" y="126" fill="#dc2626">截线</text></svg>',
        "triangle-ineq": f'<svg viewBox="0 0 260 180" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="40,150 220,150 130,40" fill="rgba(37,99,235,.08)" stroke="#2563eb" stroke-width="2.4"/><text x="120" y="170" fill="#475569">a</text><text x="72" y="100" fill="#475569">b</text><text x="170" y="100" fill="#475569">c</text><text x="90" y="30" fill="#dc2626">a+b&gt;c</text></svg>',
        "pythagoras": f'<svg viewBox="0 0 240 220" xmlns="http://www.w3.org/2000/svg" {S}><polygon points="40,180 180,180 40,60" fill="rgba(37,99,235,.1)" stroke="#2563eb" stroke-width="2"/><rect x="40" y="180" width="140" height="30" fill="rgba(220,38,38,.1)" stroke="#dc2626" stroke-width="1.5"/><rect x="10" y="60" width="30" height="120" fill="rgba(124,58,237,.1)" stroke="#7c3aed" stroke-width="1.5"/><polygon points="40,60 180,180 180,60" fill="rgba(5,150,105,.1)" stroke="#059669" stroke-width="1.5"/><text x="90" y="226" fill="#dc2626">a²</text><text x="2" y="128" fill="#7c3aed">b²</text><text x="120" y="100" fill="#059669">c²</text></svg>',
    }
    return figs.get(key, "")

# ============================================================
# HTML 模板
# ============================================================
HTML_HEAD = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{meta_desc}">
<title>{title} · 知识体系</title>
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
  :root{{--la-bg:#f4f7fb;--la-card:#ffffff;--la-ink:#152033;--la-muted:#607089;--la-shadow:0 12px 32px rgba(20,36,60,.09);}}
  *{{box-sizing:border-box}}
  html{{scroll-behavior:smooth}}
  body{{margin:0;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;color:var(--la-ink);background:radial-gradient(circle at 10% 10%,rgba(37,99,235,.08),transparent 28%),radial-gradient(circle at 90% 10%,rgba(124,58,237,.08),transparent 28%),var(--la-bg);line-height:1.7}}
  a{{color:inherit}}
  .la-wrap{{width:min(1400px,94vw);margin:auto}}
  .la-header{{padding:52px 0 20px;text-align:center}}
  .la-eyebrow{{font-size:13px;letter-spacing:.22em;color:var(--la-muted);font-weight:700;text-transform:uppercase}}
  h1{{margin:10px 0 8px;font-size:clamp(30px,5vw,54px);line-height:1.08;letter-spacing:-.03em}}
  .la-subtitle{{margin:0 auto;color:var(--la-muted);font-size:16px;max-width:820px;line-height:1.8}}
  .back-bar{{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:22px 0 6px}}
  .back-btn{{display:inline-flex;align-items:center;gap:8px;padding:10px 22px;border-radius:999px;text-decoration:none;font-size:14px;font-weight:800;background:#fff;color:#1e3a8a;border:1px solid #c7d7ee;box-shadow:0 8px 20px rgba(20,36,60,.08);transition:.25s;cursor:pointer}}
  .back-btn:hover{{transform:translateY(-2px);box-shadow:0 14px 30px rgba(20,36,60,.14);color:#4c1d95;border-color:#ddd6fe}}
  .la-nav-tabs{{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:22px 0 8px}}
  .la-nav-tab{{padding:8px 16px;border-radius:999px;text-decoration:none;font-weight:700;font-size:13px;border:1px solid #d5deea;background:#fff;transition:.25s;color:#334155}}
  .la-nav-tab:hover{{transform:translateY(-2px);box-shadow:0 8px 20px rgba(20,36,60,.1)}}
  .la-nav-tab.c1{{color:#1e40af;border-color:#bfdbfe}}
  .la-nav-tab.c2{{color:#0f766e;border-color:#99f6e4}}
  .la-nav-tab.c3{{color:#047857;border-color:#a7f3d0}}
  .la-nav-tab.c4{{color:#c2410c;border-color:#fed7aa}}
  .la-nav-tab.c5{{color:#6d28d9;border-color:#ddd6fe}}
  .la-nav-tab.c6{{color:#be185d;border-color:#fbcfe8}}
  .la-toolbar{{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:16px 0 8px}}
  button{{border:1px solid #d5deea;background:#fff;color:var(--la-ink);border-radius:999px;padding:9px 14px;font:inherit;cursor:pointer;transition:.2s ease}}
  button:hover{{transform:translateY(-1px);box-shadow:0 8px 20px rgba(20,36,60,.08)}}
  .la-engagement-bar{{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:10px 0 0}}
  .la-stat-item{{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;background:#fff;border:1px solid #d5deea;border-radius:999px;font-size:14px;font-weight:600;color:#475569}}
  .la-stat-value{{color:#2563eb;font-weight:800}}
  .la-legend{{margin:26px auto 0;max-width:1100px;background:rgba(255,255,255,.8);border:1px solid #dde5ef;border-radius:20px;padding:16px 22px;display:flex;gap:14px;flex-wrap:wrap;justify-content:center;box-shadow:var(--la-shadow)}}
  .la-legend-title{{font-size:12px;font-weight:800;letter-spacing:.16em;color:#94a3b8;align-self:center;margin-right:6px}}
  .la-arc-badge{{display:inline-flex;align-items:center;font-size:10px;font-weight:800;padding:3px 8px;border-radius:6px;letter-spacing:.03em;white-space:nowrap}}
  .la-arc-def{{background:#dbeafe;color:#1e40af}}
  .la-arc-thm{{background:#d1fae5;color:#065f46}}
  .la-arc-der{{background:#ede9fe;color:#5b21b6}}
  .la-arc-exa{{background:#cffafe;color:#155e75}}
  .la-arc-app{{background:#ffedd5;color:#9a3412}}
  .la-arc-his{{background:#f1f5f9;color:#475569}}
  .la-roadmap{{margin-top:30px;background:rgba(255,255,255,.74);border:1px solid rgba(189,201,218,.7);box-shadow:var(--la-shadow);border-radius:28px;padding:34px}}
  .la-phase-title{{font-size:24px;font-weight:800;margin:60px 0 4px;display:flex;align-items:center;gap:12px;color:#1e293b;letter-spacing:-.01em}}
  .la-phase-title:first-child{{margin-top:0}}
  .la-phase-title::before{{content:"";display:block;width:6px;height:30px;border-radius:4px;background:#2563eb;flex-shrink:0}}
  .la-phase-title.la-ch1::before{{background:#2563eb}}
  .la-phase-title.la-ch2::before{{background:#0d9488}}
  .la-phase-title.la-ch3::before{{background:#059669}}
  .la-phase-title.la-ch4::before{{background:#c2410c}}
  .la-phase-title.la-ch5::before{{background:#7c3aed}}
  .la-phase-title.la-ch6::before{{background:#be185d}}
  .la-phase-en{{font-size:11px;letter-spacing:.36em;color:#94a3b8;font-weight:700;text-transform:uppercase;margin:0 0 12px 18px;font-style:italic}}
  .la-phase-desc{{color:var(--la-muted);font-size:14px;margin:0 0 24px 18px;line-height:1.8;max-width:960px}}
  .la-domain{{margin-bottom:26px;padding:16px 18px 18px 22px;position:relative;background:rgba(255,255,255,.6);border-radius:18px;border:1px solid #e5ebf2}}
  .la-domain::before{{content:"";position:absolute;left:6px;top:16px;bottom:16px;width:5px;border-radius:5px;background:var(--domain-color,#2563eb);box-shadow:0 0 12px rgba(37,99,235,.25)}}
  .la-domain-header{{display:flex;align-items:center;gap:10px;margin-bottom:14px;padding-left:6px;flex-wrap:wrap}}
  .la-domain-header h3{{margin:0;font-size:18px;color:#1e293b}}
  .la-domain-count{{font-size:11px;padding:3px 10px;border-radius:999px;background:#f1f5f9;color:#64748b;font-weight:600}}
  .la-domain-desc{{font-size:12px;color:#94a3b8;margin-left:auto;font-style:italic}}
  .la-domain-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}}
  .la-course-card{{background:#fff;border:1px solid #dbe3ee;border-radius:14px;padding:14px;cursor:pointer;transition:.25s;position:relative;overflow:hidden}}
  .la-course-card:hover{{transform:translateY(-3px);box-shadow:0 10px 20px rgba(25,44,75,.1);border-color:#aabbd0}}
  .la-course-card h4{{margin:0 0 8px;font-size:14.5px;line-height:1.35;color:#1e293b}}
  .la-course-card p{{margin:0;font-size:11.5px;color:var(--la-muted);line-height:1.6}}
  .la-arc-badges{{display:flex;flex-wrap:wrap;gap:3px;margin-bottom:8px}}
  .la-overlay{{position:fixed;inset:0;background:rgba(15,23,42,.5);display:none;align-items:center;justify-content:center;padding:18px;z-index:60;backdrop-filter:blur(2px)}}
  .la-overlay.show{{display:flex}}
  .la-modal{{width:min(820px,96vw);background:white;border-radius:24px;padding:30px;box-shadow:0 24px 80px rgba(0,0,0,.28);animation:laPopIn .3s;max-height:90vh;overflow-y:auto}}
  @keyframes laPopIn{{from{{transform:scale(.94);opacity:0}}to{{transform:scale(1);opacity:1}}}}
  .la-modal h2{{margin:0 0 10px;font-size:23px;color:#1e293b;line-height:1.35}}
  .la-modal .la-crumbs{{font-size:12px;color:#94a3b8;margin:0 0 14px;font-weight:600;letter-spacing:.02em}}
  .la-modal .la-arc-badges{{margin:0 0 16px}}
  .la-modal-body{{color:#334155;font-size:15px;line-height:1.9}}
  .la-modal-body p{{margin:0 0 12px}}
  .la-modal-body strong{{color:#0f172a}}
  .la-modal-body ul{{margin:0 0 12px;padding-left:22px}}
  .la-modal-body li{{margin-bottom:6px}}
  .la-fml{{margin:16px 0;padding:14px 18px;background:linear-gradient(135deg,#f8fafc,#eef4fb);border-left:4px solid #93b4e8;border-radius:10px;overflow-x:auto;font-size:16px}}
  .la-fml .note{{display:block;font-size:12.5px;color:#8496ad;margin-top:8px;line-height:1.6;font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}}
  .la-fml mjx-container[display="true"]{{margin:0 !important}}
  .la-fig{{margin:18px auto;padding:14px 16px 10px;background:#fafcff;border:1px solid #e2ebf7;border-radius:14px;display:flex;flex-direction:column;align-items:center;max-width:600px}}
  .la-fig svg{{display:block;width:100%;height:auto;max-width:560px}}
  .la-fig .la-fig-cap{{font-size:12px;color:#8496ad;margin-top:8px;text-align:center;letter-spacing:.02em}}
  .la-callout{{margin:14px 0;padding:12px 16px;background:#fffbeb;border-left:3px solid #fbbf24;border-radius:8px;font-size:13.5px;color:#78350f;line-height:1.8}}
  .la-callout.la-app{{background:#fff7ed;border-color:#fb923c;color:#7c2d12}}
  .la-callout.la-his{{background:#f8fafc;border-color:#94a3b8;color:#334155}}
  .la-kp-sec{{margin:0 0 18px;padding:14px 16px;border-radius:12px;background:#f8fafc;border:1px solid #eef2f7}}
  .la-kp-sec h5{{margin:0 0 10px;font-size:14px;color:#1e293b;letter-spacing:.04em;display:flex;align-items:center;gap:8px}}
  .la-kp-sec h5::before{{content:"";width:4px;height:14px;border-radius:2px;background:var(--la-accent,#3b82f6)}}
  .la-kp-def{{border-left:3px solid #3b82f6}}
  .la-kp-thm{{border-left:3px solid #8b5cf6;background:#faf7ff}}
  .la-kp-der{{border-left:3px solid #0ea5e9;background:#f0f9ff}}
  .la-kp-exa{{border-left:3px solid #10b981;background:#f0fdf4}}
  .la-kp-app{{border-left:3px solid #f59e0b;background:#fffbeb}}
  .la-kp-note{{border-left:3px solid #ef4444;background:#fef2f2}}
  .la-kp-his{{border-left:3px solid #64748b;background:#f8fafc}}
  .la-kp-ext{{border-left:3px solid #ec4899;background:#fdf2f8}}
  .la-kp-sec p:last-child{{margin-bottom:0}}
  .la-modal-close{{margin-top:22px;background:#0f172a;color:white;border-color:#0f172a;padding:10px 20px;font-weight:bold}}
  .la-footer{{padding:34px 0 50px;color:var(--la-muted);text-align:center;font-size:13px;line-height:1.9}}
  @media(max-width:900px){{.la-wrap{{width:min(94vw,720px)}}.la-roadmap{{padding:20px}}.la-phase-title{{font-size:19px}}.la-phase-en{{font-size:10px;letter-spacing:.26em}}.la-domain-desc{{display:none}}.la-domain-grid{{grid-template-columns:repeat(auto-fill,minmax(160px,1fr))}}.la-modal{{padding:22px}}}}
</style>
</head>
<body>
<div class="la-wrap">
  <header class="la-header">
    <div class="la-eyebrow">{eyebrow} · KNOWLEDGE MAP</div>
    <h1>{title} · 知识体系</h1>
    <p class="la-subtitle">{subtitle}</p>
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
    <span class="la-legend-title">六类知识记号</span>
    <span class="la-arc-badge la-arc-def">定 义</span>
    <span class="la-arc-badge la-arc-thm">定 理</span>
    <span class="la-arc-badge la-arc-der">推 导</span>
    <span class="la-arc-badge la-arc-exa">例 子</span>
    <span class="la-arc-badge la-arc-app">应 用</span>
    <span class="la-arc-badge la-arc-his">注 记</span>
  </div>
  <main class="la-roadmap" id="laRoadmap"></main>
  <footer class="la-footer">
    <div>{title} · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">物理学知识网络 · 单文件静态站点</div>
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
const LA_FIG = {{ {fig_dict} }};
const LA_TAG_LABEL = {{def:'定 义', thm:'定 理', der:'推 导', exa:'例 子', app:'应 用', note:'注 记', his:'背 景', ext:'拓 展'}};
const LA_DATA = [
{data_json}
];
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
}});
</script>
</body>
</html>
'''

# ============================================================
# 渲染单个学科
# ============================================================
def render_subject(sub):
    """sub: dict with keys filename, title, eyebrow, subtitle, meta_desc, chapters"""
    # nav tabs
    nav_tabs = ""
    for i, ch in enumerate(sub["chapters"], 1):
        nav_tabs += f'<a class="la-nav-tab c{i}" href="#{ch["id"]}">{ch["num"]} · {ch["title"]}</a>'

    # build LA_DATA as JS
    data_parts = []
    for ch in sub["chapters"]:
        secs_parts = []
        for sec in ch["sections"]:
            items_parts = []
            for it in sec["items"]:
                body_js = js_escape(it["body"])
                item_fields = [
                    f"id:'{it['id']}'",
                    f"name:'{it['name']}'",
                    f"tags:{json.dumps(it['tags'], ensure_ascii=False)}",
                    f"brief:'{js_escape(it['brief'])}'",
                ]
                if it.get("fig"):
                    item_fields.append(f"fig:'{it['fig']}'")
                if it.get("figCap"):
                    item_fields.append(f"figCap:'{js_escape(it['figCap'])}'")
                item_fields.append(f"body:`{body_js}`")
                items_parts.append("{" + ",".join(item_fields) + "}")
            secs_parts.append(
                "{" + f"name:'{sec['name']}',color:'{sec['color']}',desc:'{js_escape(sec['desc'])}',items:[{','.join(items_parts)}]" + "}"
            )
        data_parts.append(
            "{" + f"id:'{ch['id']}',num:'{ch['num']}',title:'{ch['title']}',en:'{ch['en']}',sub:'{js_escape(ch.get('sub',''))}',desc:'{js_escape(ch['desc'])}',sections:[{','.join(secs_parts)}]" + "}"
        )
    data_json = ",\n".join(data_parts)

    # fig dict
    fig_keys = set()
    for ch in sub["chapters"]:
        for sec in ch["sections"]:
            for it in sec["items"]:
                if it.get("fig"):
                    fig_keys.add(it["fig"])
    fig_entries = []
    for k in sorted(fig_keys):
        svg = fig_svg(k)
        if svg:
            fig_entries.append(f"'{k}':`{svg}`")
    fig_dict = ",".join(fig_entries)

    html = HTML_HEAD.format(
        meta_desc=sub["meta_desc"],
        title=sub["title"],
        eyebrow=sub["eyebrow"],
        subtitle=sub["subtitle"],
        nav_tabs=nav_tabs,
        fig_dict=fig_dict,
        data_json=data_json,
    )
    return html

def write_subject(sub):
    html = render_subject(sub)
    path = os.path.join(OUT_DIR, sub["filename"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [OK] {sub['filename']}  ({len(sub['chapters'])} 章)")

# ============================================================
# 主入口（数据在 subjects.py 中定义，此处仅测试模板）
# ============================================================
if __name__ == "__main__":
    print("Generator template loaded. Import subjects from gen_subjects.py to run.")
