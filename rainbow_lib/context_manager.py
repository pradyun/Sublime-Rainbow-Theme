"""Generates a context for the theme to be rendered in.

The context is what contains the modified colours and basically, everything
else in the theme.
"""

from .colour import Colour


class ContextManager(object):

    def generate_theme_context(self, scheme_colours, variant, theme_name):
        context = {
            "name": theme_name,
            "variant": variant,
            "scheme": scheme_colours,
        }

        # Colours
        context["theme"] = self.generate_colour_settings(scheme_colours, variant)

        return context

    def generate_colour_settings(self, scheme_colours, variant):
        if "dark" in variant:
            return self._dark_variant_colours(scheme_colours)
        elif "light" in variant:
            return self._light_variant_colours(scheme_colours)

    def _dark_variant_colours(self, scheme_colours):
        # Adapted from One UI Dark (an Atom text editor theme)
        fallback_color = Colour(rgb=[38, 46, 63])
        fallback_hue = 220  # Blueish
        too_dark_threshold = 10

        scheme_bg_colour = scheme_colours.get("background", fallback_color)

        hue, saturation, value = scheme_bg_colour.hsv

        # Hue Guards
        if saturation == 0:
            hue = fallback_hue

        # Saturation Guards
        if hue <= 80:
            # Minimize saturation for brown
            saturation = min(5, saturation)
        elif hue < 160:
            # Reduce saturation for green
            saturation = min(12, saturation)
        if value < too_dark_threshold:
            # Limit max saturation for very dark backgrounds
            saturation = min(48, saturation)

        # Value Guards
        if value < too_dark_threshold:
            # Increase brightness when too dark
            value += 8
        else:
            # Limit max lightness (for light syntax themes)
            value = min(18, value)

        theme_fg = Colour(hsv=(hue, min(saturation, 18), max(value*3, 66)))
        theme_bg = Colour(hsv=(hue, saturation, value))

        return {
            "foreground": theme_fg,
            "background": theme_bg,
        }

    def _light_variant_colours(self, scheme_colours):
        # Adapted from One UI Dark (an Atom text editor theme)
        fallback_color = Colour(rgb=[38, 46, 63])
        fallback_hue = 220  # Blueish

        scheme_bg_colour = scheme_colours.get("background", fallback_color)

        hue, saturation, value = scheme_bg_colour.hsv

        # Hue Guards
        if hue == 0:
            hue = fallback_hue

        # Saturation Guards
        saturation = min(saturation, 24)

        # Value Guards
        value = max(value, 92)

        theme_fg = Colour(hsv=(hue, saturation, value - 72))
        theme_bg = Colour(hsv=(hue, saturation, value))

        return {
            "foreground": theme_fg,
            "background": theme_bg,
        }
