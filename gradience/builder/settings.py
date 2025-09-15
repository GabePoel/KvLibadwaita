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
KVC_DARK_SRC = SRC_DIR / "KvLibadwaitaDark.kvconfig"
SVG_DARK_SRC = SRC_DIR / "KvLibadwaitaDark.svg"

KVC_LIGHT_SRC = SRC_DIR / "KvLibadwaita.kvconfig"
SVG_LIGHT_SRC = SRC_DIR / "KvLibadwaita.svg"

KVC_DST = RESULT_DIR / "KvLibadwaita" / "KvLibadwaita.kvconfig"
SVG_DST = RESULT_DIR / "KvLibadwaita" / "KvLibadwaita.svg"

# Matchers:
KVC_DARK_MATCHER = MATCHERS_DIR / "colors-dark-kvconfig.json"
SVG_DARK_MATCHER = MATCHERS_DIR / "colors-dark-svg.json"

KVC_LIGHT_MATCHER = MATCHERS_DIR / "colors-light-kvconfig.json"
SVG_LIGHT_MATCHER = MATCHERS_DIR / "colors-light-svg.json"
