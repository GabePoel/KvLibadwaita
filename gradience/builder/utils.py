import json

from builder.colors import Color
from builder.settings import (
    BASE16_DIR,
    KVC_SRC,
    KVC_DST,
    SVG_SRC,
    SVG_DST,
    KVCONFIG_MATCHER,
    SVG_MATCHER
)


class Gradience(object):
    def __init__(self, color_scheme="catppuccin_mocha", custom=None):
        self.kvc_src = KVC_SRC
        self.kvc_dst = KVC_DST
        self.svg_src = SVG_SRC
        self.svg_dst = SVG_DST
        self.base16_dir = BASE16_DIR
        self.kvconfig_matcher = KVCONFIG_MATCHER
        self.svg_matcher = SVG_MATCHER
        self.color_scheme = color_scheme
        self.custom = custom

    def _read_file(self, file):
        with open(file, mode="r") as f:
            content = f.read()
            return content

    def _write_file(self, file, content):
        with open(file, mode="w") as f:
            f.write(content)

    def _recolor(self, config, matcher):
        scheme = self._read_file(self.base16_dir / f"{self.color_scheme}.json")
        if self.custom:
            try:
                scheme = self._read_file(self.custom)
            except Exception as error:
                print(error)
                exit(1)

        color_scheme = json.loads(scheme)
        colors = Color(**color_scheme)

        for color in matcher:
            ref = matcher[color]["ref"]
            chanel = matcher[color]["chanel"]
            value = matcher[color]["value"]
            shift_color = colors.scheme[ref]
            if chanel == "saturation":
                new_color = colors.saturation(color=shift_color, shift=value)
            elif chanel == "hue":
                new_color = colors.hue(color=shift_color, shift=value)
            else:
                new_color = colors.lightness(color=shift_color, shift=value)
            # replace color:
            config = config.replace(color, new_color, -1)

        return config

    def mktheme(self):
        # read config files:
        kvconfig = self._read_file(self.kvc_src)
        svg = self._read_file(self.svg_src)
        # read matchers:
        kvconfig_matcher = json.loads(self._read_file(self.kvconfig_matcher))
        svg_matcher = json.loads(self._read_file(self.svg_matcher))
        # recolor:
        kvconfig = self._recolor(kvconfig, kvconfig_matcher)
        svg = self._recolor(svg, svg_matcher)
        # make theme dir:
        self.kvc_dst.parent.mkdir(parents=True, exist_ok=True)
        # make theme files:
        self._write_file(self.kvc_dst, kvconfig)
        self._write_file(self.svg_dst, svg)
