# Bedrock Addon Icons

Bedrock Addon Icons is an extension that provides Godot icons inside of VSCode, for the purpose of creating Bedrock addons. The icons will display based on file extensions. 

For example `obsidian_knife.recipe.json` will display a recipe icon.

 - [👋 Join us on Discord](https://discord.gg/XjV87YN)
 - [🔗 View on GitHub](https://github.com/SirLich/bedrock-addon-icons)
 - [🔗 View on VSCode Store](https://marketplace.visualstudio.com/items?itemName=SirLich.bedrock-addon-icons)


## Using this Extension

Due to limitations in VSCode, this extension replaces *all icons, across the entire editor*. For this reason, you should disable the extension globally, and only enable in the workspaces where you are developing addons:

```json
"extensions": {
	"recommendations": [
		"sirlich.bedrock-addon-icons"
	]
}
```

## Theme and Style

It was difficult to find good icons for all possible asset types. If some icons disagree with you, please [get in touch](https://discord.gg/XjV87YN). In general, *red* icons are for the behavior pack, and *blue* icons are for the resource pack.

For icons that can exist in both, like entities, the icon can be red or blue depending on which pack you specify. It will show white if it can't figure it out.

Example:
 - `troll.entity.json` : White (unknown pack)
 - `troll.entity.rp.json` : Blue (resource pack)
 - `troll.entity.bp.json` : Red (behavior pack)

## Extension Bindings

To allow different styles of naming, there are many allowed bindings for every asset type. This allows you the most flexibility in your file naming. You may manually examine `theme.json` if you would like to view all mappings, otherwise you can use the following sensible heuristic:


General naming Rule:

 - The full name will always be there: e.g., `troll.entity.json` and `troll.animation_controller.json`
 - Various short versions exist as well: e.g., `troll.e.json` and `troll.ac.json`

You can specify color by including 'rp' or 'bp':
 - At the end: e.g., `troll.entity.bp.json` and `troll.e.bp.json`
 - At the start: e.g., `troll.rp.entity.json` and `troll.rp.e.json`
 - A second short version is usually provided, which puts pack first, with no dot: `troll.bpe.json`

Lots of files are also supported, such as:
 - tick.json
 - manifest.json
 - example.mcfunction

![](./preview.png)

## Attribution

This repository contains icons from Godot. [Please consider donating to them](https://godotengine.org/donate). Two icons (JS, TS and Json) are copied from [seti](https://github.com/jesseweed/seti-ui). Both projects are MIT licensed.
