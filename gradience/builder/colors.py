# -*- coding: utf-8 -*-


# █▀▄ █▀█ █▀▀ █▀ ▀
# █▄▀ █▄█ █▄▄ ▄█ ▄
# ----------------
"""The module contains the class Color
which can store color scheme like base16,
change colors according to the HSL color model using public methods,
and also convert different color schemes
(as it does, the built-in colorsys module):
    hex => rgb
    rgb => hex
    hex => hsl
    hsl => hex
    hsl => rgb
    rgb => hsl

The software is provided "as is", without warranty of any kind, express or
implied, including but not limited to the warranties of merchantability,
fitness for a particular purpose and noninfringement. in no event shall the
authors or copyright holders be liable for any claim, damages or other
liability, whether in an action of contract, tort or otherwise, arising from,
out of or in connection with the software or the use or other dealings in the
software.
"""
import colorsys


# █▀▄▀█ █▀▀ ▀█▀ ▄▀█ ▀
# █░▀░█ ██▄ ░█░ █▀█ ▄
# -------------------
__author__ = "MOIS3Y"
__credits__ = ["Stepan Zhukovsky"]
__license__ = "GPL v3.0"
__version__ = "0.2.0"
__maintainer__ = "Stepan Zhukovsky"
__email__ = "stepan@zhukovsky.me"
__status__ = "Production"


# █▀▀ █▀█ █░░ █▀█ █▀█ ▀
# █▄▄ █▄█ █▄▄ █▄█ █▀▄ ▄
# -------------------
class Color(object):
    """This class is intended to be stored in an attribute
    Color.scheme color scheme in base16 format
    https://github.com/chriskempson/base16
    And its subsequent use to set the color for various elements.
    Since there are only 16 colors in base16, sometimes this is not enough to
    place color accents anywhere.
    Therefore, the class has several methods for adjusting the color.
    The HSL color model is used here.
        HLS: Hue, Luminance, Saturation
            H: position in the spectrum
            S: color saturation
            L: color lightness
    You are probably familiar with it, if not, it's best to just see how
    you can change the color by changing one of the parameters,
    for example here:
    https://hslpicker.com/
    Each channel has its own method which accepts a color and a ratio
    offsets:
        color.hue(color, shift)
        color saturation(color, shift)
        Color.lightness(color, shift)

    For saturation, lightness, the shift argument takes the offset percentage
    relative to the current color (-100, 100), if you pass a percentage
    that will go beyond frame, then the parameter being changed will take
    the maximum or minimum possible value.
    For hue, the absolute value of the degree that H can
    be changed this channel (-360, 360).

        Examples:
        ---------

        color_scheme = some_base16_theme

        color = Color(**color_scheme)

        shift_color = color.scheme['base08']                =>  #b4befe

        hue_color = Color.hue(shift_color, -60)             =>  #b4fef4

        saturation = Color.saturation(shift_color, 20)      =>  #b3bdff

        lightness_color = Color.lightness(shift_color, 20)  =>  #e6eaff
    """
    def __init__(self, **color_scheme) -> dict:
        """Stores the color scheme as an attribute of the scheme class
        preferably in base16 simple example:
        themes = {
            #....
            "catppuccin_mocha": {
                "scheme": "Catppuccin Mocha",
                "author": "https://github.com/catppuccin/catppuccin",
                "base00": "#11111b", # crust
                "base01": "#181825", # mantle
                "base02": "#313244", # surface0
                "base03": "#45475a", # surface1
                "base04": "#585b70", # surface2
                "base05": "#cdd6f4", # text
                "base06": "#f5e0dc", # rosewater
                "base07": "#b4befe", # lavender
                "base08": "#f38ba8", # red
                "base09": "#fab387", # peach
                "base0A": "#f9e2af", # yellow
                "base0B": "#a6e3a1", # green
                "base0C": "#94e2d5", # teal
                "base0D": "#89b4fa", # blue
                "base0E": "#cba6f7", # mauve
                "base0F": "#f2cdcd", # flamingo
            },
            #....
        }
        color_scheme = Color(themes['catppuccin_mocha'])
        """
        self.scheme = color_scheme

    def hex_to_rgb(self, color: str) -> tuple:
        """
        Args:
            color (_str_): '#b4befe'
        Returns:       R    G    B
            _tuple_: (180, 190, 254)
        """
        hex_value = color.strip('#')
        rgb = tuple(int(hex_value[item:item + 2], 16) for item in (0, 2, 4))
        return rgb  # (RGB)

    def rgb_to_hex(self, *rgb) -> str:
        """
        Args:                 R    G    B
            *rgb (_tuple_): (180, 190, 254)
        Returns:
            _str_: '#b4befe'
        """
        r, g, b = [int(channel) for channel in rgb]
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)  # #HEX

    def hex_to_hsl(self, color: str) -> tuple:
        """
        Args:
            color (_str_): '#b4befe'
        Returns:       H    S    L
            _tuple_: (0.64 0.97 0.85)
            16 decimal places, rounding is not performed to preserve precision.
        """
        rgb = self.hex_to_rgb(color)
        return (self.rgb_to_hsl(*rgb))

    def hsl_to_hex(self, *hsl) -> str:
        """
        Args:                  H    S    L
            *hsl (_tuple_): (0.64 0.97 0.85)
        Returns:
            _str_: '#b4befe'
        """
        rgb = self.hsl_to_rgb(*hsl)
        return (self.rgb_to_hex(*rgb))  # #HEX

    def rgb_to_hsl(self, *rgb) -> tuple:
        """
        Args:                 R    G    B
            *rgb (_tuple_): (180, 190, 254)
        Returns:
            _tuple_: (0.64 0.97 0.85)
            16 decimal places, rounding is not performed to preserve precision.
        """
        # Normalize R, G, B values:
        r, g, b = [item / 255.0 for item in rgb]
        h, l, s = [item for item in colorsys.rgb_to_hls(r, g, b)]  # noqa: E741
        return (h, s, l)

    def hsl_to_rgb(self, *hsl) -> tuple:
        """
        Args:                  H    S    L
            *hsl (_tuple_): (0.64 0.97 0.85)
        Returns:       R    G    B
            _tuple_: (180, 190, 254)
        """
        h, s, l = [channel for channel in hsl]   # noqa: E741
        r, g, b = [round(item * 255) for item in colorsys.hls_to_rgb(h, l, s)]
        return (r, g, b)

    @staticmethod
    def _check_range(channel: float) -> int | float:
        return 0 if channel < 0 else (1 if channel > 1 else channel)

    def hue(self, color: str, shift: int) -> str:
        """position in the spectrum 0 -> 360 degrees
        takes an int number and shift the current position by that number:
        to increase, the number must be positive (10)
        to decrease, the number must be negative (-10)

        Args:
            color (_str_): '#b4befe'
            shift (_int_): 10 or -10 or 42 or -42 etc
        Returns:
            _str_: #feb4b4
        """
        h, s, l = [channel for channel in self.hex_to_hsl(color)]  # noqa: E741
        if shift < 0:
            h = self._check_range(((h * 3.6 - abs(shift) / 100) / 3.6))
        else:
            h = self._check_range(((h * 3.6 + shift / 100) / 3.6))
        return self.hsl_to_hex(h, s, l)

    def saturation(self, color: str, shift: int) -> str:
        """color saturation 0 -> 100%
        takes an int (percentage) and shifts the current position
        by that percentage:
        to increase, the number must be positive (20)
        to decrease, the number must be negative (-20)

        Args:
            color (_str_): '#b4befe'
            shift (_int_): 10 or -10 or 42 or -42 etc
        Returns:
            _str_: '#b3bdff'
        """
        h, s, l = [channel for channel in self.hex_to_hsl(color)]  # noqa: E741
        if shift < 0:
            s = self._check_range((s - (abs(shift) / 100)))
        else:
            s = self._check_range((s + (shift / 100)))
        return self.hsl_to_hex(h, s, l)

    def lightness(self, color: str, shift: int) -> str:
        """color lightness 0 -> 100%
        takes an int (percentage) and shifts the current position
        by that percentage:
        to increase, the number must be positive (20)
        to decrease, the number must be negative (-20)

        Args:
            color (_str_): '#b4befe'
            shift (_int_): 10 or -10 or 42 or -42 etc
        Returns:
            _str_: '#b3bdff'
        """
        h, s, l = [channel for channel in self.hex_to_hsl(color)]  # noqa: E741
        if shift < 0:
            l = self._check_range((l - (abs(shift) / 100)))  # noqa: E741
        else:
            l = self._check_range((l + (shift / 100)))  # noqa: E741
        return self.hsl_to_hex(h, s, l)

    @property
    def variant(self):
        base00 = self.hex_to_hsl(self.scheme["base00"])
        if base00[2] > 0.5:
            variant = "light"
        else:
            variant = "dark"
        return variant
