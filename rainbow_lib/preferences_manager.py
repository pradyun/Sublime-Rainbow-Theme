"""A class to load and pre-process data from Sublime's User Preferences
"""

import sublime
import plistlib

from .colour import Colour
from . import core


class PreferencesManager(object):
    """Loads Preference and Colour Scheme details.
    """

    colour_defaults = {
        "background": "#FAFAFA",
        "foreground": "#1F1F1F",
        "caret": "#1F1F1F",
    }

    theme_extension = ".sublime-theme"

    def __init__(self):
        super().__init__()

        self.load_settings()

    def load_settings(self):
        # Load the settings files
        self._s_prefs = sublime.load_settings(
            "Preferences.sublime-settings"
        )

    def get_theme_variant_and_name(self):
        theme = self._s_prefs.get("theme", "")

        if not theme.endswith(self.theme_extension):
            return None, None

        search_name = theme[:-len(self.theme_extension)]
        if search_name not in core.utils.THEME_VARIANTS:
            return None, None

        return core.utils.THEME_VARIANTS[search_name], search_name

    def get_current_scheme_colours(self):
        # Load from Preferences
        colour_scheme = self._get_colour_scheme()
        if not colour_scheme:
            core.logger.fatal("Could not get colour-scheme from view")
            return

        # Read the File and locate general settings
        try:
            byte_stream = sublime.load_binary_resource(colour_scheme)
            plist_obj = plistlib.readPlistFromBytes(byte_stream)
            general_settings = self._find_general_settings(plist_obj)
        except Exception as e:
            raise Exception("Could not load from colour-scheme") from e

        final = self.colour_defaults.copy()
        final.update({
            k: v for (k, v) in general_settings.items() if k in final
        })

        for key, value in final.items():
            if value.startswith("#"):
                final[key] = Colour(hex=value)

        return final

    def _get_colour_scheme(self):
        load_from_view = False
        if load_from_view:
            settings = sublime.active_window().active_view().settings()
        else:
            settings = sublime.load_settings("Preferences.sublime-settings")
        return settings.get("color_scheme", None)

    # TODO: Make sure this works exactly like Sublime Text applies the general
    #       scope.
    def _find_general_settings(self, plist_obj):
        retval = {}
        for item in plist_obj.get("settings", []):
            if 'scope' not in item and "settings" in item:
                retval.update(item["settings"])
        return retval
