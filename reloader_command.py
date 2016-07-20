import sublime_plugin


class RainbowReloadPackageCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        sublime_plugin.reload_plugin("Theme - Rainbow.1_reloader")
        sublime_plugin.reload_plugin("Theme - Rainbow.main")
