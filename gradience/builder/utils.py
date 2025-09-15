import json

from builder.colors import Color
from builder.settings import (
    BASE16_DIR,
    KVC_DARK_SRC,
    KVC_LIGHT_SRC,
    KVC_DARK_MATCHER,
    KVC_LIGHT_MATCHER,
    SVG_DARK_SRC,
    SVG_LIGHT_SRC,
    SVG_DARK_MATCHER,
    SVG_LIGHT_MATCHER,
    KVC_DST,
    SVG_DST,
)


class Gradience(object):
    def __init__(self, color_scheme="catppuccin_mocha", custom=None):
        self.colors = self._get_colors(color_scheme, custom)
        self.kvc_dst = KVC_DST
        self.svg_dst = SVG_DST

        if self.colors.variant == "light":
            self.kvc = self._read_file(KVC_LIGHT_SRC)
            self.svg = self._read_file(SVG_LIGHT_SRC)
            self.kvc_matcher = self._read_file(KVC_LIGHT_MATCHER, is_json=True)
            self.svg_matcher = self._read_file(SVG_LIGHT_MATCHER, is_json=True)
        else:
            self.kvc = self._read_file(KVC_DARK_SRC)
            self.svg = self._read_file(SVG_DARK_SRC)
            self.kvc_matcher = self._read_file(KVC_DARK_MATCHER, is_json=True)
            self.svg_matcher = self._read_file(SVG_DARK_MATCHER, is_json=True)

    def _get_colors(self, color_scheme, custom=None):
        if not custom:
            scheme = self._read_file(BASE16_DIR / f"{color_scheme}.json")
        else:
            try:
                scheme = self._read_file(custom)
            except Exception as error:
                print(error)
                exit(1)
        return Color(**(json.loads(scheme)))

    def _read_file(self, file, is_json=False):
        with open(file, mode="r") as f:
            content = json.loads(f.read()) if is_json else f.read()
            return content

    def _write_file(self, file, content):
        with open(file, mode="w") as f:
            f.write(content)

    def _recolor(self, config, matcher):
        for color in matcher:
            ref = matcher[color]["ref"]
            chanel = matcher[color]["chanel"]
            value = matcher[color]["value"]
            shift_color = self.colors.scheme[ref]
            if chanel == "saturation":
                new_color = self.colors.saturation(
                    color=shift_color,
                    shift=value
                )
            elif chanel == "hue":
                new_color = self.colors.hue(
                    color=shift_color,
                    shift=value
                )
            else:
                new_color = self.colors.lightness(
                    color=shift_color,
                    shift=value
                )
            # replace color:
            config = config.replace(color, new_color, -1)

        return config

    def mktheme(self):
        # recolor:
        kvc = self._recolor(self.kvc, self.kvc_matcher)
        svg = self._recolor(self.svg, self.svg_matcher)
        # make theme dir:
        self.kvc_dst.parent.mkdir(parents=True, exist_ok=True)
        # make theme files:
        self._write_file(self.kvc_dst, kvc)
        self._write_file(self.svg_dst, svg)
