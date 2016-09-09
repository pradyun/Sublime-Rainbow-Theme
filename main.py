"""Adaptive theme for Sublime Text
"""

import sublime
import sublime_plugin

# Just import the one command
from .rainbow_lib import RainbowThemeAdapter

rta = None


class RainbowAdaptThemeCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        global rta

        try:
            val = rta.run('sublime command')
        except Exception:
            msg = "Could not generate Rainbow Theme. Check console."
            sublime.status_message(msg)
            raise
        else:
            if val:
                msg = "Successfully Regenerated Rainbow Theme! Yay!"
                sublime.status_message(msg)
            else:
                sublime.status_message("Skipped Rainbow Theme generation...")


class RainbowClearCacheCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        global rta

        try:
            rta.clear_cache()
        except Exception:
            sublime.status_message("Could not clear cache. Check console.")
            raise
        else:
            sublime.status_message("Cleared Cache.")


class RainbowViewThemeAdapter(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        rta.run('tab change')


def plugin_loaded():
    global rta

    rta = RainbowThemeAdapter()

    settings = sublime.load_settings("Preferences.sublime-settings")

    settings.add_on_change('theme', rta.run)
    settings.add_on_change('color_scheme', rta.run)


def plugin_unloaded():
    settings = sublime.load_settings("Preferences.sublime-settings")

    settings.clear_on_change('theme')
    settings.clear_on_change('color_scheme')
