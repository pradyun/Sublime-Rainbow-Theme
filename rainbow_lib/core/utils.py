"""Generic Utilities used by everyone
"""

import os
import sublime


# -----------------------------------------------------------------------------

PACKAGE_NAME = "Theme - Rainbow"

# Path
_PATHS = {
    "templates": [PACKAGE_NAME, "templates"],

    "theme": [PACKAGE_NAME, "theme"],
    "widget-scheme": [PACKAGE_NAME, "widget-scheme"],
    "widget-settings": [PACKAGE_NAME, "settings"],

    "cache": ["..", "Cache", PACKAGE_NAME, "fs-cache"],
}

_NAMES = {
    "theme": "{name}.sublime-theme",

    # Keeping the hex value to work-around Sublime Text
    # not reloading widget scheme.
    "widget-scheme": "Widget - {name} - {theme[background].hex}.stTheme",
    "widget-settings": "Widget - {name}.sublime-settings",
    # If somehow two colour schemes use the same colours, we're screwed!

    "template-theme": "theme.jinja2",
    "template-widget-scheme": "widget-scheme.jinja2",
    "template-widget-settings": "widget-settings.jinja2",
}

THEME_VARIANTS = {
    "Rainbow Soda Light": ("soda", "light"),
    "Rainbow Soda Dark": ("soda", "dark"),
    # Planned.
    # "Rainbow Flat Light": ("flat", "light"),
    # "Rainbow Flat Dark": ("flat", "dark"),
}


# -----------------------------------------------------------------------------
# Paths and Names for things
# -----------------------------------------------------------------------------
def _no_idea(thing):
    msg = "Whoops! Don't know what to do with {!r}..."
    raise RuntimeError(msg.format(thing))


def get_path_for(thing):
    if thing in _PATHS:
        return os.path.join(sublime.packages_path(), *_PATHS[thing])
    _no_idea(thing)


def get_name_for(thing, context):
    if thing in _NAMES:
        return _NAMES[thing].format(**context)
    _no_idea(thing)
