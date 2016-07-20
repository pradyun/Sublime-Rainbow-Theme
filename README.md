# Theme - Rainbow

Light and Dark Sublime Text UI themes that adapts to your active colour scheme. Based off [Soda].

> TODO: Add an awesome Screencast!

## WOW! How do I get this?

Install the themes using Sublime Package Control, it's listed as `Theme - Rainbow`.

Activate one of the Themes by modifying your user preferences file, which you
can find using the menu item Preferences -> Settings - User in Sublime Text.

The Themes provided are:

 - `Rainbow Soda Light.sublime-theme`
 - `Rainbow Soda Dark.sublime-theme`

## How does it work?
The themes are re-generated on the fly when you change the colour scheme. These changes are picked up by Sublime Text and changes become visible.

This package uses the same algorithms to determine the base-colours for the UI elements as `one-light-ui` and `one-dark-ui` from Atom, ported to pure-Python. These colours are then used when generating the themes.

  [Soda]: https://github.com/buymeasoda/soda-theme
