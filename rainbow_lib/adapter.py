"""The Main Command that runs the show.
"""

from . import core
from .cache import NullCache, FileSystemCache
from .theme_manager import ThemeManager
from .context_manager import ContextManager
from .preferences_manager import PreferencesManager


class RainbowThemeAdapter(object):
    """Run the entire re-generation procedure for the theme
    """

    def __init__(self):
        super().__init__()
        self.ctx_man = ContextManager()
        self.th_man = ThemeManager()
        self.prefs = PreferencesManager()

    def run(self, trigger_by="settings change"):
        core.logger.debug("[adapter] Triggered by: %s", trigger_by)

        # Reload the preferences
        self.prefs.load_settings()

        # Prepare everything according to settings.
        core.setup_logger(self.prefs)

        if self.prefs.develop_mode:
            self.th_man.set_cache(NullCache())
        else:
            self.th_man.set_cache(FileSystemCache())

        # To decide if generation can be skipped.
        skip_reason = None

        # Extract colours from the colour schemes
        scheme_colours = self.prefs.get_current_scheme_colours()

        # Detect what the type of theme is active
        variant, theme_name = self.prefs.get_theme_variant_and_name()
        if variant is None:
            skip_reason = "Inactive theme"
        else:
            # Get the currently active colour for the theme
            theme_bg = self.prefs.get_active_theme_bg_base()
            if (
                scheme_colours["background"].hex == theme_bg and
                not self.prefs.develop_mode
            ):
                skip_reason = "Correct theme is active"

        if skip_reason is not None:
            core.logger.debug("[adapter] Skipping generation - " + skip_reason)
            return False

        # Generate other colours for the theme from what we know
        context = self.ctx_man.generate_theme_context(
            scheme_colours, variant, theme_name
        )

        # Generate the theme and supporting files
        rendered = self.th_man.get_rendered_theme_parts(
            context, scheme_colours, variant
        )

        # Write the generated theme in the Package
        self.th_man.write_theme_parts(context, rendered)

        # Set the currently active colour for the theme
        self.prefs.set_active_theme_bg_base(scheme_colours["background"].hex)

        return True

    def clear_cache(self):
        self.th_man.cache.clear()
