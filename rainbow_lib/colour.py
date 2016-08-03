"""A nice colour object for the templates
"""

import colorsys
import unittest
from collections import namedtuple


# ========================================================================================
# Web Colours Mapping
# ========================================================================================
# This list was extracted from w3schools's web-page on Thursday 24th March 2016.
# If it needs updating, lemme know.
_name_to_hex = {
    "black": "#000000",
    "navy": "#000080",
    "darkblue": "#00008b",
    "mediumblue": "#0000cd",
    "blue": "#0000ff",
    "darkgreen": "#006400",
    "green": "#008000",
    "teal": "#008080",
    "darkcyan": "#008b8b",
    "deepskyblue": "#00bfff",
    "darkturquoise": "#00ced1",
    "mediumspringgreen": "#00fa9a",
    "lime": "#00ff00",
    "springgreen": "#00ff7f",
    "aqua": "#00ffff",
    "cyan": "#00ffff",
    "midnightblue": "#191970",
    "dodgerblue": "#1e90ff",
    "lightseagreen": "#20b2aa",
    "forestgreen": "#228b22",
    "seagreen": "#2e8b57",
    "darkslategray": "#2f4f4f",
    "darkslategrey": "#2f4f4f",
    "limegreen": "#32cd32",
    "mediumseagreen": "#3cb371",
    "turquoise": "#40e0d0",
    "royalblue": "#4169e1",
    "steelblue": "#4682b4",
    "darkslateblue": "#483d8b",
    "mediumturquoise": "#48d1cc",
    "indigo": "#4b0082",
    "darkolivegreen": "#556b2f",
    "cadetblue": "#5f9ea0",
    "cornflowerblue": "#6495ed",
    "rebeccapurple": "#663399",
    "mediumaquamarine": "#66cdaa",
    "dimgray": "#696969",
    "dimgrey": "#696969",
    "slateblue": "#6a5acd",
    "olivedrab": "#6b8e23",
    "slategray": "#708090",
    "slategrey": "#708090",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "mediumslateblue": "#7b68ee",
    "lawngreen": "#7cfc00",
    "chartreuse": "#7fff00",
    "aquamarine": "#7fffd4",
    "maroon": "#800000",
    "purple": "#800080",
    "olive": "#808000",
    "gray": "#808080",
    "grey": "#808080",
    "skyblue": "#87ceeb",
    "lightskyblue": "#87cefa",
    "blueviolet": "#8a2be2",
    "darkred": "#8b0000",
    "darkmagenta": "#8b008b",
    "saddlebrown": "#8b4513",
    "darkseagreen": "#8fbc8f",
    "lightgreen": "#90ee90",
    "mediumpurple": "#9370db",
    "darkviolet": "#9400d3",
    "palegreen": "#98fb98",
    "darkorchid": "#9932cc",
    "yellowgreen": "#9acd32",
    "sienna": "#a0522d",
    "brown": "#a52a2a",
    "darkgray": "#a9a9a9",
    "darkgrey": "#a9a9a9",
    "lightblue": "#add8e6",
    "greenyellow": "#adff2f",
    "paleturquoise": "#afeeee",
    "lightsteelblue": "#b0c4de",
    "powderblue": "#b0e0e6",
    "firebrick": "#b22222",
    "darkgoldenrod": "#b8860b",
    "mediumorchid": "#ba55d3",
    "rosybrown": "#bc8f8f",
    "darkkhaki": "#bdb76b",
    "silver": "#c0c0c0",
    "mediumvioletred": "#c71585",
    "indianred": "#cd5c5c",
    "peru": "#cd853f",
    "chocolate": "#d2691e",
    "tan": "#d2b48c",
    "lightgray": "#d3d3d3",
    "lightgrey": "#d3d3d3",
    "thistle": "#d8bfd8",
    "orchid": "#da70d6",
    "goldenrod": "#daa520",
    "palevioletred": "#db7093",
    "crimson": "#dc143c",
    "gainsboro": "#dcdcdc",
    "plum": "#dda0dd",
    "burlywood": "#deb887",
    "lightcyan": "#e0ffff",
    "lavender": "#e6e6fa",
    "darksalmon": "#e9967a",
    "violet": "#ee82ee",
    "palegoldenrod": "#eee8aa",
    "lightcoral": "#f08080",
    "khaki": "#f0e68c",
    "aliceblue": "#f0f8ff",
    "honeydew": "#f0fff0",
    "azure": "#f0ffff",
    "sandybrown": "#f4a460",
    "wheat": "#f5deb3",
    "beige": "#f5f5dc",
    "whitesmoke": "#f5f5f5",
    "mintcream": "#f5fffa",
    "ghostwhite": "#f8f8ff",
    "salmon": "#fa8072",
    "antiquewhite": "#faebd7",
    "linen": "#faf0e6",
    "lightgoldenrodyellow": "#fafad2",
    "oldlace": "#fdf5e6",
    "red": "#ff0000",
    "fuchsia": "#ff00ff",
    "magenta": "#ff00ff",
    "deeppink": "#ff1493",
    "orangered": "#ff4500",
    "tomato": "#ff6347",
    "hotpink": "#ff69b4",
    "coral": "#ff7f50",
    "darkorange": "#ff8c00",
    "lightsalmon": "#ffa07a",
    "orange": "#ffa500",
    "lightpink": "#ffb6c1",
    "pink": "#ffc0cb",
    "gold": "#ffd700",
    "peachpuff": "#ffdab9",
    "navajowhite": "#ffdead",
    "moccasin": "#ffe4b5",
    "bisque": "#ffe4c4",
    "mistyrose": "#ffe4e1",
    "blanchedalmond": "#ffebcd",
    "papayawhip": "#ffefd5",
    "lavenderblush": "#fff0f5",
    "seashell": "#fff5ee",
    "cornsilk": "#fff8dc",
    "lemonchiffon": "#fffacd",
    "floralwhite": "#fffaf0",
    "snow": "#fffafa",
    "yellow": "#ffff00",
    "lightyellow": "#ffffe0",
    "ivory": "#fffff0",
    "white": "#ffffff",
}


# ========================================================================================
# Colour Conversion Functions
# ========================================================================================
def _ensure_within_range(val, lower, upper):
    if val < lower:
        return lower
    elif val > upper:
        return upper
    else:
        return val


def _rgb_convert_to_1(rgb):
    return tuple(i/255 for i in rgb)


def _rgb_convert_from_1(rgb):
    return tuple(i*255 for i in rgb)


def _hsv_convert_to_1(hsv):
    h, s, v = hsv
    return (h/360, s/100, v/100)


def _hsv_convert_from_1(hsv):
    h, s, v = hsv
    return (h*360, s*100, v*100)


def _rgba2hex(rgb, opacity):
    """Given a RGB-255, return the Hex-str
    """
    def to_hex(x):
        return hex(int(round(x)))[2:].rjust(2, '0')

    parts = ["#"]
    for value in rgb:
        parts.append(to_hex(value))
    if opacity is not 255:
        parts.append(to_hex(opacity))
    return "".join(parts)


def _hex2rgba(s):
    """Given a Hex-str, return the corresponding RGB-255
    """
    if not isinstance(s, str):
        raise TypeError('Expected hex string. Got non-string value')
    elif not s.startswith("#"):
        raise ValueError('Got ill-formed hex string')
    val = s[1:]

    di = {
        8: lambda c: (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16), int(c[6:8], 16)),
        4: lambda c: (int(c[0]*2, 16), int(c[1]*2, 16), int(c[2]*2, 16), int(c[3]*2, 16)),
        6: lambda c: (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16), None),
        3: lambda c: (int(c[0]*2, 16), int(c[1]*2, 16), int(c[2]*2, 16), None),
    }

    return di[len(val)](val)


def _rgb2hsv(rgb):
    """Given a RGB, return the corresponding HSV
    """
    hsv = _hsv_convert_from_1(colorsys.rgb_to_hsv(*_rgb_convert_to_1(rgb)))
    return hsv


def _hsv2rgb(hsv):
    """Given a HSV, return the corresponding RGB
    """
    rgb = _rgb_convert_from_1(colorsys.hsv_to_rgb(*_hsv_convert_to_1(hsv)))
    return rgb

HSV = namedtuple("HSV", ["hue", "saturation", "value"])
RGB = namedtuple("RGB", ["red", "green", "blue"])


# ========================================================================================
# Main Class
# ========================================================================================
class Colour(object):
    """A convenience immutable-like class representing an RGB Colour.

    Can be instantiated with
        - Named HTML Colours
        - RGB-255 tuples
        - Hex values (3, 4, 6, 8 lengths, with #)
        - HSV values (with ranges of (0-360, 0-100, 0-100))

    It takes a value of opacity separately, which is a 0-255 ranged value.
    """

    def __init__(self, *, web=None, rgb=None, hex=None, hsv=None, opacity=None):
        if sum(1 if i is not None else 0 for i in (rgb, hex, hsv, web)) != 1:
            raise TypeError(
                "Need exactly one of 'rgb', 'hex', 'web' and 'hsv' "
                "to create a colour object."
            )
        super().__init__()

        self._instantiated_with = {
            "web": web,
            "rgb": rgb,
            "hex": hex,
            "hsv": hsv,
            "opacity": opacity,
        }

        # Convert from other formats to RGB
        if web is not None:
            try:
                hex = _name_to_hex[web]
            except KeyError:
                raise Exception("Got unexpected web colour name {!r}".format(web))

        if hex is not None:
            *rgb, val_opacity = _hex2rgba(hex)
            # Do not override the passed opacity value
            if val_opacity is not None:
                if opacity is None:
                    opacity = val_opacity
                else:
                    raise Exception(
                        "Got opacity value from both hex code and argument. "
                        "I'm confused."
                    )

        if rgb is not None:
            hsv = _rgb2hsv(rgb)

        if opacity is None:
            opacity = 255
        else:
            opacity = _ensure_within_range(opacity, 0, 255)

        # Assign the relevant values
        self._hsv = tuple(map(float, hsv))
        self._opacity = opacity

        if opacity and opacity < 1:
            print(
                "Are you sure that you want a colour with opacity less than 1? "
                "It's a 0-255 range value, which gets floored when converting "
                "to a hex-value."
            )

    @property
    def hsv(self):
        return HSV(*self._hsv)

    @property
    def rgb(self):
        return RGB(*_hsv2rgb(self._hsv))

    @property
    def hex(self):
        return _rgba2hex(self.rgb, self._opacity)

    @property
    def opacity(self):
        return self._opacity

    def __str__(self):
        return str(list(round(i, 2) for i in self.rgb))

    def __repr__(self):
        return "Colour({})".format(", ".join(
            "{}={!r}".format(key, value)
            for key, value in self._instantiated_with.items()
        ))

    def __eq__(self, other):
        return (
            isinstance(other, Colour) and
            self.rgb == other.rgb and
            self.opacity == other.opacity
        )

    def with_opacity(self, new_opacity):
        return Colour(rgb=self.rgb, opacity=new_opacity)

    def lighten(self, amount=10.0):
        amount = _ensure_within_range(amount, 0, 100)
        new_hsv = list(self.hsv)
        new_hsv[2] = min(100, new_hsv[2] + amount)
        return Colour(hsv=new_hsv)

    def darken(self, amount=10.0):
        amount = _ensure_within_range(amount, 0, 100)
        new_hsv = list(self.hsv)
        new_hsv[2] = max(0, new_hsv[2] - amount)
        return Colour(hsv=new_hsv)

    def saturate(self, amount=20.0):
        amount = _ensure_within_range(amount, 0, 100)
        new_hsv = list(self.hsv)
        new_hsv[1] = min(100, new_hsv[1] + amount)
        return Colour(hsv=new_hsv)

    def desaturate(self, amount=20.0):
        amount = _ensure_within_range(amount, 0, 100)
        new_hsv = list(self.hsv)
        new_hsv[1] = max(0, new_hsv[1] - amount)
        return Colour(hsv=new_hsv)

    def adjust_hue(self, degrees=20.0):
        # Do not clamp in a range.
        new_hsv = list(self.hsv)
        new_hsv[0] = (new_hsv[0] + degrees) % 360
        return Colour(hsv=new_hsv)

    def mix_with(self, other, weight=0):
        p = _ensure_within_range(weight, -1, 1)

        w1 = (1 + p) / 2
        w2 = 1 - w1

        return Colour(rgb=[
            self.rgb[i] * w1 + other.rgb[i] * w2 for i in range(3)
        ], opacity=(w1 * self.opacity + w2 * other.opacity))

    # Converts from percent to -1 to 1 range
    #     x/50 - 1
    # Converts from 0 to 1 to -1 to 1 range
    #     x*2 - 1

    def tint(self, amount=10.0):
        return self.mix_with(Colour(web="black"), 1 - amount/50)

    def shade(self, amount=10.0):
        return self.mix_with(Colour(web="white"), 1 - amount/50)

    def complement(self):
        return self.adjust_hue(180)

    def invert(self):
        return Colour(rgb=[255 - i for i in self.rgb], opacity=self.opacity)


class TestColour(unittest.TestCase):
    """Some rudimentary tests to check that stuff works.

    Not extensive.
    """

    def assert_almost_equal(self, c1, c2, diff=0.7):
        if isinstance(c1, tuple) and isinstance(c2, tuple):
            for a, b in zip(c1, c2):
                self.assertAlmostEqual(a, b)
        else:
            self.assertAlmostEqual(c1, c2)

    # =========================================================================
    # Colour Formats
    # =========================================================================
    def test_init(self):
        rgb_blue = Colour(rgb=[0, 0, 255])
        web_blue = Colour(web="blue")

        hex_blue1 = Colour(hex="#0000FF")
        hex_blue2 = Colour(hex="#0000ff")

        hsv_blue = Colour(hsv=[240, 100, 100])

        self.assertEqual(rgb_blue, hex_blue1)
        self.assertEqual(web_blue, hex_blue1)
        self.assertEqual(hsv_blue, hex_blue1)
        self.assertEqual(hex_blue2, hex_blue1)

    def test_from_rgb_to_rgb(self):
        cases = [
            [[0, 0, 255], (0, 0, 255)],
            [[0, 255, 0], (0, 255, 0)],
            [[0, 0, 0], (0, 0, 0)],
            [[255, 255, 255], (255, 255, 255)],
        ]

        for color, rgb in cases:
            obj = Colour(rgb=color)
            self.assertEqual(obj.rgb, tuple(rgb), "{!r} != {!r}".format(obj, rgb))

    def test_from_hex_to_rgb(self):
        cases = [
            ["#00F", (0, 0, 255)],
            ["#0000FF", (0, 0, 255)],
            ["#FF0000", (255, 0, 0)],
            ["#0000FF", (0, 0, 255)],
        ]

        for color, rgb in cases:
            obj = Colour(hex=color)
            self.assertEqual(obj.rgb, tuple(rgb), "{!r} != {!r}".format(obj, rgb))

    def test_web_to_hex(self):
        # Check all hex colours!
        for name in _name_to_hex:
            obj = Colour(web=name)
            self.assertEqual(obj.hex, _name_to_hex[name], name)

    def test_rgb_to_hsv(self):
        cases = [
            [[255, 0, 0], (0, 100, 100)],
            [[0, 255, 0], (120, 100, 100)],
            [[0, 0, 255], (240, 100, 100)],
        ]

        for color, hsv in cases:
            obj = Colour(rgb=color)
            self.assertEqual(obj.hsv, tuple(hsv), "{!r} != {!r}".format(obj, hsv))

    def test_hsv_to_rgb(self):
        cases = [
            [(0, 100, 100), [255, 0, 0]],
            [(120, 100, 100), [0, 255, 0]],
            [(240, 100, 100), [0, 0, 255]],
        ]

        for color, rgb in cases:
            obj = Colour(hsv=color)
            self.assertEqual(obj.rgb, tuple(rgb), "{!r} != {!r}".format(obj, rgb))

    # =========================================================================
    # Colour Functions
    # =========================================================================
    def test_with_opacity(self):
        blue = Colour(web="blue")
        self.assertEqual(blue.with_opacity(100).opacity, 100)
        self.assertEqual(blue.with_opacity(-100).opacity, 0)
        self.assertEqual(blue.with_opacity(400).opacity, 255)

    def test_lighten(self):
        maroon = Colour(web="maroon")
        self.assertAlmostEqual(maroon.hsv.value + 10, maroon.lighten().hsv.value)
        self.assertAlmostEqual(maroon.hsv.value + 20, maroon.lighten(20).hsv.value)

    def test_darken(self):
        maroon = Colour(web="maroon")
        self.assertAlmostEqual(maroon.hsv.value - 10, maroon.darken().hsv.value)
        self.assertAlmostEqual(maroon.hsv.value - 20, maroon.darken(20).hsv.value)

    def test_saturate(self):
        skyblue = Colour(web="skyblue")
        self.assertAlmostEqual(
            skyblue.hsv.saturation + 20, skyblue.saturate().hsv.saturation
        )
        self.assertAlmostEqual(
            skyblue.hsv.saturation + 10, skyblue.saturate(10).hsv.saturation
        )

    def test_desaturate(self):
        skyblue = Colour(web="skyblue")
        self.assertAlmostEqual(
            skyblue.hsv.saturation - 20, skyblue.desaturate().hsv.saturation
        )
        self.assertAlmostEqual(
            skyblue.hsv.saturation - 10, skyblue.desaturate(10).hsv.saturation
        )

    def test_adjust_hue(self):
        red = Colour(web="red")

        self.assertEqual(red.adjust_hue(120).hsv.hue, 120)
        self.assertEqual(red.adjust_hue(-120).hsv.hue, 240)

    def test_mix_with__basic(self):
        red = Colour(web="red")
        blue = Colour(web="blue")

        self.assertEqual(blue.mix_with(red).rgb, (127.5, 0, 127.5))

    def test_mix_with__handling_opacity(self):
        blue_50 = Colour(web="blue", opacity=50)
        red_100 = Colour(web="red", opacity=100)

        self.assertEqual(blue_50.mix_with(red_100).rgb, (127.5, 0, 127.5))
        self.assertAlmostEqual(blue_50.mix_with(red_100).opacity, 75)

    def test_tint(self):
        red = Colour(web="red")
        self.assertEqual(red.tint(10).rgb, (229.5, 0, 0))

    def test_shade(self):
        red = Colour(web="red")
        self.assert_almost_equal(red.shade(10).rgb, (255, 25.5, 25.5))

    def test_complement(self):
        olive = Colour(web="olive")
        self.assert_almost_equal(olive.complement().rgb, (0, 0, 128))

    def test_invert(self):
        olive = Colour(web="olive")
        self.assert_almost_equal(olive.invert().rgb, (127, 127, 255))


if __name__ == '__main__':
    unittest.main()
