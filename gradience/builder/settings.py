import pathlib

# Project dir:
ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

# Top level:
SRC_DIR = ROOT_DIR / "src" / "KvLibadwaita"
SELF_DIR = ROOT_DIR / "gradience"
BASE16_DIR = SELF_DIR / "base16"
MATCHERS_DIR = SELF_DIR / "matchers"
RESULT_DIR = SELF_DIR / "result"

# Config files:
KVC_SRC = SRC_DIR / "KvLibadwaitaDark.kvconfig"
KVC_DST = RESULT_DIR / "KvLibadwaita" / "KvLibadwaita.kvconfig"
SVG_SRC = SRC_DIR / "KvLibadwaitaDark.svg"
SVG_DST = RESULT_DIR / "KvLibadwaita" / "KvLibadwaita.svg"

# Matchers:
KVCONFIG_MATCHER = MATCHERS_DIR / "colors-kvconfig.json"
SVG_MATCHER = MATCHERS_DIR / "colors-svg.json"
