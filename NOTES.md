# NOTES
These are some mind-dumps I do occasionally when I need to clear my head.

## Directory Structure
All the temporary stuff should be put Packages/User. That is the theme-cache.

Base directory: Packages/Theme - Rainbow/

Directory             | Type of Files
----------------------|---------------------------------------------------------------------
`/`                   | Basic stuff
`/metadata`           | Generated Sidebar Icon metadata for the themes
`/themes`             | Generated themes
`/themes/icons`       | Sidebar icons for the themes
`/themes/images`      | Assets for the themes
`/themes/settings`    | Widget Settings Files

## Flow of Package and Regeneration
> Task (`Where is it handled?`)

#### Initialization (`plugin_loaded()`)

1. Load and Compile Templates (`Compiler.load_templates`)
1. Cache Templates (`TemplateCache.cache_templates`)

#### Compile on Change (`rainbow_adapt_theme`)

This command merely calls the run command on the Adapter. All the donkey work is done there.

#### Compilation Process

It's written in a self-documenting manner in rainbow_lib/commands.py
