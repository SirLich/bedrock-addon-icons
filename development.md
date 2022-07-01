# Bedrock Addon Icons

This page contains technical information for working within this repository. For information about the extension itself, you should check out `readme.md`.

## Structure

The project is structured fairly simply. The `icons` folder contains SVG images, which are then mapped to filepaths in `theme.json`. There are essentially three things to pay attention to:
 - `iconDefinitions` maps a `shortname` field to the actual SVG path. The shortname will be used within the rest of the file to identify this icon.
 - `fileExtensions` maps between `extension` and `shortname`. The extension part must come as an *extension*, not the whole filename. For example `t.json` would match `test.t.json`, but not `t.json` itself.
  - `fileNames` maps between `filename` and `shortname`. The filename must match exactly, so it's used for stuff like `tick.json`.

## Adding a new Icon
In general, to add a new icon, follow these steps:
 - Add SV image into `icons`
 - Manually edit the SVG data to use the correct colors (blue for RP, red for BP). There is a VSCode extension for previewing.
 - Edit `theme.json` with an `iconDefinition`
 - Edit `theme.json` with either `fileExtension` or `fileName` data, as desired
 - Run locally to test

## Running Locally

To run locally, you first need to install the correct VSCode Extension tooling (I will let the internet handle this), then press F5 to test the extension.

## Releasing new Version
 - Update version in `package.json`
 - Update the `CHANGELOG.md`
 - `vsce login SirLich` (may not be required)
 - `vsce publish`