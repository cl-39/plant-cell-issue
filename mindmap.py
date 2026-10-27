# -*- coding: utf-8 -*-
"""普通生物学（陈阅增 第五版）——植物的细胞、组织、组织系统 思维导图 (PNG)"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = 2                      # supersample
W, H = 4800, 3100          # design px
CW, CH = W * S, H * S

F_REG = r"C:\Windows\Fonts\msyh.ttc"
F_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
F_LIGHT = r"C:\Windows\Fonts\msyhl.ttc"

_fc = {}
def font(size, weight="r"):
    key = (size, weight)
    if key not in _fc:
        path = {"r": F_REG, "b": F_BOLD, "l": F_LIGHT}[weight]
        _fc[key] = ImageFont.truetype(path, int(round(size * S)), index=0)
    return _fc[key]

def R(v):
    return int(round(v * S))

# ---------------- 配色 ----------------
TEAL = (16, 121, 106)
BLUE = (40, 94, 158)
PURP = (114, 70, 142)
AMBR = (176, 104, 36)
INK = (34, 38, 36)
INK2 = (78, 84, 81)
HUB = (26, 54, 48)

# ---------------- 排印参数 ----------------
F_HUB = 72
F_L1 = 50
F_L2 = 44
F_LEAF = 48
LH = 80          # 叶片行距
G_GAP = 40       # 组间距
B_GAP = 130      # 分支间距

CX = W // 2
HDR_Y = 108
BAND_TOP = 150

# ---------------- 内容 ----------------
LEFT = [
    dict(name="植物细胞", color=TEAL, groups=[
        dict(name="基本结构", leaves=[
            ("质膜", " 选择透过性，控制物质进出"),
            ("细胞质基质", " 多种代谢反应场所"),
            ("细胞核", " 核膜、核仁、染色质"),
        ]),
        dict(name="细胞壁", leaves=[
            ("成分", " 纤维素、半纤维素、果胶"),
            ("分层", " 胞间层、初生壁、次生壁"),
            ("胞间连丝", " 细胞间的运输通道"),
        ]),
        dict(name="细胞器", leaves=[
            ("质体", " 叶绿体、有色体、白色体"),
            ("线粒体", " 有氧呼吸，供应能量"),
            ("内质网", " 合成蛋白质、脂类并运输"),
            ("高尔基体", " 分泌，并参与细胞壁形成"),
            ("液泡", " 细胞液，渗透调节与贮藏"),
            ("核糖体", " 蛋白质合成的场所"),
        ]),
        dict(name="后含物与分化", leaves=[
            ("后含物", " 淀粉粒、糊粉粒、油滴、结晶"),
            ("细胞分化", " 形成不同形态与功能的细胞"),
        ]),
    ]),
    dict(name="组织系统", color=PURP, groups=[
        dict(name="皮组织", leaves=[
            ("组成", " 表皮与周皮"),
            ("功能", " 覆盖保护、减少失水"),
        ]),
        dict(name="维管组织", leaves=[
            ("组成", " 木质部 + 韧皮部"),
            ("功能", " 长距离输导与机械支持"),
        ]),
        dict(name="基本组织", leaves=[
            ("组成", " 薄壁为主，兼机械、分泌"),
            ("功能", " 填充、同化、贮藏"),
        ]),
        dict(name="相互关系", leaves=[
            ("分工协作", " 连续贯穿各器官"),
            ("共同构成", " 植物体的组织骨架"),
        ]),
    ]),
]

RIGHT = [
    dict(name="植物组织", color=BLUE, groups=[
        dict(name="分生组织", leaves=[
            ("共同特征", " 细胞小、壁薄、无大液泡"),
            ("顶端分生", " 根尖、茎尖，使伸长"),
            ("侧生分生", " 维管、木栓形成层，使加粗"),
            ("居间分生", " 禾本科节间基部，助拔节"),
            ("按来源分", " 原分生→初生→次生"),
        ]),
        dict(name="保护组织", leaves=[
            ("表皮", " 角质层、气孔、表皮毛"),
            ("周皮", " 木栓层+栓内层+形成层"),
            ("气孔", " 保卫细胞控制开闭，行气体交换"),
        ]),
        dict(name="薄壁组织", leaves=[
            ("特征", " 壁薄、间隙大、液泡大"),
            ("同化组织", " 叶肉含叶绿体，行光合"),
            ("贮藏组织", " 根、茎、种子积累养分"),
            ("通气组织", " 水生植物，形成气腔"),
            ("吸收·贮水", " 根毛吸收；肉质植物贮水"),
        ]),
        dict(name="机械组织", leaves=[
            ("厚角组织", " 角隅加厚、活细胞、可伸长"),
            ("厚壁组织", " 均匀加厚、死细胞"),
        ]),
        dict(name="输导组织", leaves=[
            ("木质部", " 导管、管胞，运水和无机盐"),
            ("韧皮部", " 筛管+伴胞，运有机养料"),
        ]),
        dict(name="分泌组织", leaves=[
            ("外分泌", " 腺毛、蜜腺、排水器"),
            ("内分泌", " 分泌腔、乳汁管、树脂道"),
        ]),
    ]),
    dict(name="分布位置", color=AMBR, groups=[
        dict(name="根", leaves=[
            ("根尖生长点", " 顶端分生组织"),
            ("根毛区表皮", " 吸收组织，发生根毛"),
            ("皮层与中柱", " 薄壁、导管、筛管"),
        ]),
        dict(name="茎", leaves=[
            ("茎尖与腋芽", " 顶端分生组织"),
            ("维管形成层", " 加粗，并产生木栓形成层"),
            ("皮层·髓·维管束", " 薄壁与输导组织"),
        ]),
        dict(name="叶", leaves=[
            ("上下表皮", " 保护组织，气孔分布其上"),
            ("叶肉", " 栅栏、海绵组织"),
            ("叶脉", " 维管束 + 厚壁纤维"),
        ]),
        dict(name="花果种子", leaves=[
            ("花瓣与蜜腺", " 有色体、分泌组织"),
            ("果皮与种皮", " 石细胞、纤维"),
            ("子叶与胚乳", " 贮藏薄壁组织"),
        ]),
    ]),
]

# 左右分工：左侧「细胞 + 分布位置」，右侧「组织类型 + 组织系统」
LEFT[1], RIGHT[1] = RIGHT[1], LEFT[1]


def h_of_group(n):
    return n * LH

def h_of_branch(b):
    return sum(h_of_group(len(g["leaves"])) for g in b["groups"]) + G_GAP * (len(b["groups"]) - 1)


def place(branches, ytop):
    for b in branches:
        h = h_of_branch(b)
        b["y0"] = ytop
        b["h"] = h
        b["y"] = ytop + h / 2.0
        cy = ytop
        for g in b["groups"]:
            gh = h_of_group(len(g["leaves"]))
            g["y"] = cy + gh / 2.0
            for i, lf in enumerate(g["leaves"]):
                g.setdefault("ys", []).append(cy + i * LH + LH / 2.0)
            cy += gh + G_GAP
        ytop = ytop + h + B_GAP


hL = sum(h_of_branch(b) for b in LEFT) + B_GAP * (len(LEFT) - 1)
hR = sum(h_of_branch(b) for b in RIGHT) + B_GAP * (len(RIGHT) - 1)
BAND_BOT = H - 150
band = BAND_BOT - BAND_TOP
place(LEFT, BAND_TOP + (band - hL) / 2.0)
place(RIGHT, BAND_TOP + (band - hR) / 2.0)

CY = sum(b["y"] for b in LEFT + RIGHT) / 4.0

# 中心节点尺寸
_meas = ImageDraw.Draw(Image.new("RGB", (10, 10)))
HUB_TXT = "植物的细胞与组织"
HUB_SUB = "细胞 · 组织 · 组织系统"
hub_tw = max(_meas.textlength(HUB_TXT, font=font(F_HUB, "b")) / S,
             _meas.textlength(HUB_SUB, font=font(25, "r")) / S)
HUB_W = hub_tw + 108
HUB_H = 168

NX_R = CX + HUB_W / 2          # hub right edge
NX_L = CX - HUB_W / 2

X_L1 = NX_R + 170 + 130        # L1 pill center (right side)
X_L1L = W - X_L1
X_L2 = X_L1 + 130 + 40 + 170   # L2 box left edge (right side)
X_LEAF = X_L2 + 220 + 160      # leaf dot x (right side)
X_L2L = W - X_L2
X_LEAFL = W - X_LEAF

# ---------------- 画布 ----------------
top_c = np.array([253, 254, 251], dtype=np.float32)
bot_c = np.array([238, 243, 237], dtype=np.float32)
ramp = np.linspace(0, 1, 256, dtype=np.float32).reshape(256, 1, 1)
grad_small = np.clip(top_c * (1 - ramp) + bot_c * ramp, 0, 255).astype(np.uint8)
grad_small = np.repeat(grad_small, 4, axis=1)
bg = Image.fromarray(grad_small).resize((CW, CH), Image.BICUBIC)
img = bg.convert("RGBA")

# 柔和光晕
glow = Image.new("L", (CW, CH), 0)
gd = ImageDraw.Draw(glow)
gd.ellipse([R(CX - 700), R(CY - 700), R(CX + 700), R(CY + 700)], fill=78)
glow = glow.filter(ImageFilter.GaussianBlur(R(140)))
gcol = Image.new("RGBA", (CW, CH), TEAL + (0,))
gcol.putalpha(glow)
img = Image.alpha_composite(img, gcol)

lay = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
d = ImageDraw.Draw(lay)


def bez(p0, p1, k=0.52, n=56):
    x0, y0 = p0
    x1, y1 = p1
    dx = (x1 - x0) * k
    c1x, c1y = x0 + dx, y0
    c2x, c2y = x1 - dx, y1
    out = []
    for i in range(n + 1):
        t = i / n
        m = 1 - t
        out.append((m**3 * x0 + 3 * m * m * t * c1x + 3 * m * t * t * c2x + t**3 * x1,
                    m**3 * y0 + 3 * m * m * t * c1y + 3 * m * t * t * c2y + t**3 * y1))
    return out


def curve(p0, p1, color, width, k=0.52):
    pts = [(R(x), R(y)) for x, y in bez(p0, p1, k)]
    w = max(1, int(round(width * S)))
    d.line(pts, fill=color, width=w, joint="curve")
    r = w / 2.0
    for p in (pts[0], pts[-1]):
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=color)


# ============ 连接线 ============
for side, branches in (("L", LEFT), ("R", RIGHT)):
    for b in branches:
        c = b["color"]
        sx = NX_R if side == "R" else NX_L
        l1x = X_L1 if side == "R" else X_L1L
        half1 = (len(b["name"]) * F_L1 + 62) / 2.0
        ex = l1x - half1 if side == "R" else l1x + half1
        curve((sx, CY), (ex, b["y"]), c + (215,), 7.0)
        l2e = X_L2 if side == "R" else X_L2L
        l1edge = l1x + half1 if side == "R" else l1x - half1
        for g in b["groups"]:
            curve((l1edge, b["y"]), (l2e, g["y"]), c + (170,), 4.2)
            gw = len(g["name"]) * F_L2 + 46
            gx = l2e + gw if side == "R" else l2e - gw
            lx = X_LEAF if side == "R" else X_LEAFL
            for y in g["ys"]:
                curve((gx, g["y"]), (lx, y), c + (125,), 2.0, k=0.62)

img = Image.alpha_composite(img, lay)

# ============ 阴影 ============
sh = Image.new("L", (CW, CH), 0)
sd = ImageDraw.Draw(sh)
boxes = [(CX, CY, HUB_W, HUB_H, 40)]
for side, branches in (("L", LEFT), ("R", RIGHT)):
    for b in branches:
        l1x = X_L1 if side == "R" else X_L1L
        w = len(b["name"]) * F_L1 + 62
        boxes.append((l1x, b["y"], w, F_L1 * 1.30 + 34, (F_L1 * 1.30 + 34) / 2))
        l2e = X_L2 if side == "R" else X_L2L
        for g in b["groups"]:
            gw = len(g["name"]) * F_L2 + 46
            gx = l2e + gw / 2 if side == "R" else l2e - gw / 2
            boxes.append((gx, g["y"], gw, F_L2 * 1.30 + 26, 14))
for (bx, by, bw, bh, br) in boxes:
    sd.rounded_rectangle([R(bx - bw / 2 + 4), R(by - bh / 2 + 9), R(bx + bw / 2 + 4), R(by + bh / 2 + 9)],
                         radius=R(br), fill=64)
sh = sh.filter(ImageFilter.GaussianBlur(R(9)))
scol = Image.new("RGBA", (CW, CH), (18, 34, 30, 0))
scol.putalpha(sh)
img = Image.alpha_composite(img, scol)

lay = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
d = ImageDraw.Draw(lay)


# ============ 方框 ============
def pill(cx, cy, w, h, fill, radius=None, outline=None, ow=0):
    rr = radius if radius is not None else h / 2
    d.rounded_rectangle([R(cx - w / 2), R(cy - h / 2), R(cx + w / 2), R(cy + h / 2)],
                        radius=R(rr), fill=fill, outline=outline, width=int(ow * S))


# 中心
pill(CX, CY, HUB_W, HUB_H, HUB + (255,), 44)
d.rounded_rectangle([R(CX - HUB_W / 2 + 8), R(CY - HUB_H / 2 + 8), R(CX + HUB_W / 2 - 8), R(CY + HUB_H / 2 - 8)],
                    radius=R(38), outline=(255, 255, 255, 55), width=R(2))
d.text((R(CX), R(CY - 29)), HUB_TXT, font=font(F_HUB, "b"), fill=(255, 255, 255, 255), anchor="mm")
d.text((R(CX), R(CY + 45)), HUB_SUB, font=font(25, "r"), fill=(178, 206, 196, 255), anchor="mm")

for side, branches in (("L", LEFT), ("R", RIGHT)):
    for b in branches:
        c = b["color"]
        l1x = X_L1 if side == "R" else X_L1L
        w = len(b["name"]) * F_L1 + 62
        h = F_L1 * 1.30 + 34
        pill(l1x, b["y"], w, h, c + (255,))
        d.text((R(l1x), R(b["y"] - 2)), b["name"], font=font(F_L1, "b"), fill=(255, 255, 255, 255), anchor="mm")
        l2e = X_L2 if side == "R" else X_L2L
        for g in b["groups"]:
            gw = len(g["name"]) * F_L2 + 46
            gx = l2e + gw / 2 if side == "R" else l2e - gw / 2
            gh = F_L2 * 1.30 + 26
            pill(gx, g["y"], gw, gh, (255, 255, 255, 255), 14, c + (255,), 2.6)
            d.text((R(gx), R(g["y"] - 2)), g["name"], font=font(F_L2, "b"), fill=c + (255,), anchor="mm")

# ============ 叶片文字 ============
fh = font(F_LEAF, "b")
ft = font(F_LEAF, "r")
for side, branches in (("L", LEFT), ("R", RIGHT)):
    for b in branches:
        c = b["color"]
        lx = X_LEAF if side == "R" else X_LEAFL
        for g in b["groups"]:
            for (head, tail), y in zip(g["leaves"], g["ys"]):
                dot_r = 7.0
                d.ellipse([R(lx - dot_r), R(y - dot_r), R(lx + dot_r), R(y + dot_r)], fill=c + (255,))
                hw = d.textlength(head, font=fh) / S
                tw2 = d.textlength(tail, font=ft) / S
                if side == "R":
                    tx = lx + 26
                    d.text((R(tx), R(y - 2)), head, font=fh, fill=INK + (255,), anchor="lm")
                    d.text((R(tx + hw), R(y - 2)), tail, font=ft, fill=INK2 + (255,), anchor="lm")
                else:
                    tx = lx - 26
                    d.text((R(tx), R(y - 2)), tail, font=ft, fill=INK2 + (255,), anchor="rm")
                    d.text((R(tx - tw2), R(y - 2)), head, font=fh, fill=INK + (255,), anchor="rm")

img = Image.alpha_composite(img, lay)

# ============ 页眉 / 页脚 ============
lay = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
d = ImageDraw.Draw(lay)
d.text((R(120), R(HDR_Y - 6)), "普通生物学", font=font(42, "b"), fill=INK + (255,), anchor="lm")
w1 = d.textlength("普通生物学", font=font(42, "b")) / S
d.text((R(120 + w1 + 16), R(HDR_Y - 4)), "陈阅增 · 第五版", font=font(30, "r"), fill=(150, 154, 150, 255), anchor="lm")
d.text((R(W - 120), R(HDR_Y - 4)), "图文笔记 · 复习提纲", font=font(28, "r"), fill=(158, 162, 158, 255), anchor="rm")

d.line([(R(120), R(HDR_Y + 42)), (R(W - 120), R(HDR_Y + 42))], fill=(214, 220, 214, 200), width=R(1.6))
d.line([(R(120), R(HDR_Y + 42)), (R(120 + 96), R(HDR_Y + 42))], fill=TEAL + (255,), width=R(5))

# 页脚
FOOT = "记忆主线：细胞分化 → 组织 → 组织系统 → 器官"
fw = d.textlength(FOOT, font=font(36, "r")) / S
fy = H - 72
d.rounded_rectangle([R(CX - fw / 2 - 50), R(fy - 42), R(CX + fw / 2 + 50), R(fy + 42)], radius=R(42),
                    fill=(232, 239, 232, 225))
d.text((R(CX), R(fy - 1)), FOOT, font=font(36, "r"), fill=(52, 82, 70, 255), anchor="mm")

img = Image.alpha_composite(img, lay)
out = img.convert("RGB").resize((W, H), Image.LANCZOS)
out.save("植物细胞与组织_思维导图.png", "PNG")
print("saved", out.size)
