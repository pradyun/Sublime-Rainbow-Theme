"""Compiles the Jinja2 templates.
"""

import jinja2

from . import core


class Compiler(object):
    """Compiles a Jinja2 template in a given context
    """

    def __init__(self):
        super().__init__()
        self._jinja_env = jinja2.Environment(
            loader=self._get_loader(), trim_blocks=True, lstrip_blocks=True
        )

    def _get_loader(self):
        return jinja2.FileSystemLoader(core.utils.get_path_for("templates"))

    def render_part(self, thing, context, helpers):
        template_name = core.utils.get_name_for("template-" + thing, context)
        template = self._jinja_env.get_template(template_name)

        template.globals.update(helpers)

        return template.render(context)
