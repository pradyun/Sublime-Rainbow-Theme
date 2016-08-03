# Theme - Rainbow

Light and Dark Sublime Text UI themes that adapts to your active colour scheme. Based off [Soda].

> PR with better screencast more than welcome!

![Screencast](./screencast.gif)

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

## Issues faced while trying make this?

1. ST does not acknowledge changes to Widget Schemes on the fly.

   - If support for modification and re-loading of Widget Schemes on the fly is added, it'll be awesome! 
   - That'll make this package a tiny bit simpler but more importantly, it'll make ST's behaviour more consistent.

  [Soda]: https://github.com/buymeasoda/soda-theme
