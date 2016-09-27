<h1 align="center">
    Rainbow Theme
</h1>

<p align="center">
    <img src="https://img.shields.io/packagecontrol/dt/Theme%20-%20Rainbow.svg?style=flat-square" alt="Downloads">
    <img src="https://img.shields.io/github/release/pradyunsg/Sublime-Rainbow-Theme.svg?style=flat-square" alt="Release">
</p>

<p align="center">
    Sublime Text UI themes that adapt to your active colour scheme.
</p>

![Screencast](./screencast.gif)

> PR with better screencast more than welcome!

-----

<p align="center">
    <a href="#installation">Installation</a> ▪ <a href="#activation">Activation</a> ▪ <a href="#settings">Settings</a> ▪ <a href="#contributing">Contributing</a> ▪ <a href="#license">License</a>
</p>

-----

## Installation

##### Package Control (recommended)

This is the easiest method of installation.

1. Open Command Palette using menu item `Tools → Command Palette...`
1. Choose `Package Control: Install Package`
1. Find and select `Theme - Rainbow`
1. Restart Sublime Text
1. Repeat Step 1
1. Choose `Package Control: Satisfy Dependencies`
1. Restart Sublime Text

##### Manually

1. Download the [.zip from Github].
1. Unzip the contents and rename the folder to `Theme - Rainbow`.
1. Copy the folder into Packages directory, which you can find using the menu item `Preferences → Browse Packages...`
1. Restart Sublime Text
1. Manually install all dependencies listed in the `dependencies.json` in the `Theme - Rainbow` folder.
1. Restart Sublime Text

##### Git (bleeding edge)

1. Clone the Repository into `Theme - Rainbow` of Packages directory.
   ```
   git clone https://github.com/pradyunsg/Sublime-Rainbow-Theme "Theme - Rainbow"
   ```
1. Restart Sublime Text
1. Manually install all dependencies listed in the `dependencies.json` in the `Theme - Rainbow` folder.
1. Restart Sublime Text

## Activation
This theme is activated as simply as any other theme. Open your User Preferences file, which can be located in the menu: `Preferences → Settings - User` or `Preferences → Settings` and add/modify the `theme` key to one of the following variants of the theme:

 - `Rainbow Soda Light.sublime-theme`
 - `Rainbow Soda Dark.sublime-theme`

> I plan on adding flat variants soon. Stay tuned!

Example:

```json
{
    "theme": "Rainbow Soda Light.sublime-theme"
}
```

## Settings

There is really just one settings useful to the end-user, you, today. I hope that over time this changes.

```js
"load_colors_from_active_view": true
```

If true, the theme will be adapted from the currently active view's colour scheme instead of the globally set scheme. There may be a short lag in the change of theme when switching between tabs with different colour schemes.

## Contributing
If you like the theme, help spread the word! I spent a fair amount of my free time fiddling with and tweaking this. It'll be nice to see other people using this.

If you spot some problem or face any sort of difficulty regarding this package, check out the [issues] if someone else is facing a similar issue. Otherwise, feel free to create a new issue!

## License
Theme - Rainbow is based on [Soda Theme] by Ian Hill. Like Soda Theme, it is licensed under the [Creative Commons Attribution-ShareAlike 3.0 License].

  [Creative Commons Attribution-ShareAlike 3.0 License]: https://creativecommons.org/licenses/by-sa/3.0/
  [Soda Theme]: http://buymeasoda.com/

  [.zip from Github]: https://github.com/pradyunsg/Sublime-Rainbow-Theme/releases
  [issues]: https://github.com/pradyunsg/Sublime-Rainbow-Theme/issues
