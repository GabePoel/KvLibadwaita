#!/usr/bin/python3
import os
import shutil

here = os.getcwd()
home = os.path.expanduser('~')
src = os.path.join(here, 'KvLibadwaita')
dst = os.path.join(home, '.config', 'Kvantum', 'KvLibadwaitaDraft')

svg_src = os.path.join(src, 'KvLibadwaitaDraft.svg')
kvc_src = os.path.join(src, 'KvLibadwaitaDraft.kvconfig')
svg_dst = os.path.join(dst, 'KvLibadwaitaDraft.svg')
kvc_dst = os.path.join(dst, 'KvLibadwaitaDraft.kvconfig')

os.makedirs(dst, exist_ok=True)
shutil.copy(svg_src, svg_dst)
shutil.copy(kvc_src, kvc_dst)

with open(svg_dst, 'r') as f:
    s = f.read()
s = s.replace('#00037f', 'none', -1)
with open(svg_dst, 'w') as f:
    f.write(s)