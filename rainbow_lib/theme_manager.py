"""Manages everything related to themes
"""

import os

from . import core
from .compiler import Compiler


class ThemeManager(object):
    """Runs the rendering pipeline with appropriate functions
    """

    def __init__(self, cache=None):
        super().__init__()
        self.cache = None

        self.compiler = Compiler()
        self._fsi = core.FileSystemInterfacer()

    def set_cache(self, cache):
        self.cache = cache

    def _get_helper_functions(self, variant):
        def lighten(colour, amount):
            return colour.lighten(amount)

        def darken(colour, amount):
            return colour.darken(amount)

        retval = {}
        if "dark" in variant:
            retval["contrast_decrease"] = darken
            retval["contrast_increase"] = lighten
        elif "light" in variant:
            retval["contrast_decrease"] = lighten
            retval["contrast_increase"] = darken

        return retval

    def get_rendered_theme_parts(self, context, scheme_colours, variant):
        """Returns a rendered theme with given context and colours
        """

        if self.cache is None:
            raise RuntimeError(
                "There has been an emergency. There is no cache prepared. "
                "Go die."
            )
        retval = {
            "theme": None,
            "widget-scheme": None,
            "widget-settings": None
        }

        helpers = self._get_helper_functions(variant)

        for thing in retval.keys():
            cache_key = (
                thing + "-" +
                scheme_colours["background"].hex[1:] + "-" +
                "-".join(variant)
            )

            # Use a cached version if it exists
            try:
                val = self.cache.get(cache_key)
            except KeyError:
                # Because the environment should stay consistent
                context = context.copy()

                # Save the generated theme in the Cache
                val = self.compiler.render_part(thing, context, helpers)
                try:
                    self.cache.set(cache_key, val)
                except KeyError:
                    pass

            retval[thing] = val

        return retval

    def write_theme_parts(self, context, rendered):
        for thing in rendered:
            path = core.utils.get_path_for(thing)
            fname = core.utils.get_name_for(thing, context)

            self._fsi.folder_create(path)
            self._fsi.file_write(rendered[thing], os.path.join(path, fname))
