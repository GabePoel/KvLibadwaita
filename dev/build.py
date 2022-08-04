#!/usr/bin/python3
import os
import shutil
import json

here = os.getcwd()
home = os.path.expanduser('~')
src = os.path.join(here, 'KvLibadwaita')
dst = os.path.join(home, '.config', 'Kvantum', 'KvLibadwaitaDraft')

svg_src = os.path.join(src, 'KvLibadwaitaDraft.svg')
kvc_src = os.path.join(src, 'KvLibadwaitaDraft.kvconfig')
svg_dst = os.path.join(dst, 'KvLibadwaitaDraft.svg')
kvc_dst = os.path.join(dst, 'KvLibadwaitaDraft.kvconfig')
svg_l_dst = os.path.join(dst, 'KvLibadwaita.svg')
svg_d_dst = os.path.join(dst, 'KvLibadwaitaDark.svg')
kvc_l_dst = os.path.join(dst, 'KvLibadwaita.kvconfig')
kvc_d_dst = os.path.join(dst, 'KvLibadwaitaDark.kvconfig')

os.makedirs(dst, exist_ok=True)
shutil.copy(svg_src, svg_dst)
# shutil.copy(kvc_src, kvc_l_dst)
# shutil.copy(kvc_src, kvc_d_dst)

with open(svg_dst, 'r') as f:
    s = f.read()
s = s.replace('#00037f', 'none', -1)
with open(svg_dst, 'w') as f:
    f.write(s)
    
# with open(os.path.join(here, 'color-assignment.json'), 'r') as f:
#     colors = json.load(f)
# new_colors = dict()
# for h in colors:
#     c = colors[h]
#     new_colors[c] = dict()
#     new_colors[c]["ref"] = h
#     new_colors[c]["light"] = h
#     new_colors[c]["dark"] = h
# with open(os.path.join(here, 'colors.json'), 'w') as f:
#     json.dump(new_colors, f)

with open(os.path.join(here, 'colors.json'), 'r') as f:
    colors = json.load(f)
with open(svg_src, 'r') as f:
    svg_l_str = f.read()
with open(svg_src, 'r') as f:
    svg_d_str = f.read()
with open(kvc_src, 'r') as f:
    kvc_l_str = f.read()
with open(kvc_src, 'r') as f:
    kvc_d_str = f.read()
for color in colors:
    ref = colors[color]["ref"]
    light = colors[color]["light"]
    dark = colors[color]["dark"]
    svg_l_str = svg_l_str.replace(ref, light, -1)
    svg_d_str = svg_d_str.replace(ref, dark, -1)
    kvc_l_str = kvc_l_str.replace(ref, light, -1)
    kvc_d_str = kvc_d_str.replace(ref, dark, -1)
svg_l_str = svg_l_str.replace('#00037f', 'none', -1)
svg_d_str = svg_d_str.replace('#00037f', 'none', -1)
with open(svg_l_dst, 'w') as f:
    f.write(svg_l_str)
with open(svg_d_dst, 'w') as f:
    f.write(svg_d_str)
with open(kvc_l_dst, 'w') as f:
    f.write(kvc_l_str)
with open(kvc_d_dst, 'w') as f:
    f.write(kvc_d_str)