# NOTES
These are some mind-dumps I do occasionally when I need to clear my head.

## Directory Structure
All the temporary stuff should be put Packages/User. That is the theme-cache.

Base directory: Packages/Theme - Rainbow/

Directory             | Type of Files
----------------------|------------------------------------------------------------------
`/`                   | Basic stuff
`/assets`             | Assets for the themes
`/settings`           | Widget Settings Files
`/widget-scheme`      | Widget Scheme Files
`/themes`             | Generated themes
`/rainbow_lib`        | The magical entity that creates magic.
`/themes/icons`       | Sidebar icons for the themes
`/metadata`           | Generated Sidebar Icon metadata for the themes


> Beyond this, it's out of date.

## Flow of Package and Regeneration
> Task (`Where is it handled?`)

#### Initialization (`plugin_loaded()`)

1. Load and Compile Templates (`Compiler.load_templates`)
1. Cache Templates (`TemplateCache.cache_templates`)

#### Compile on Change (`rainbow_adapt_theme`)

This command merely calls the run command on the Adapter. All the donkey work is done there.

#### Compilation Process

It's written in a self-documenting manner in rainbow_lib/commands.py
