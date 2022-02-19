import glob
import os
import shutil
import re

from dataclasses import dataclass

@dataclass
class IconType:
	name: str
	color: str

SOURCE_FOLDER = './icon_src'
DESTINATION_FOLDER = './icons'

FILL_REGEX = 'fill="(.+?)"'

KEEP_COLOR = [
	"json",
	"sound",
	"sound_file"
]

ICON_TYPES = [
	IconType('rp', '#8da5f3'),
	IconType('bp', '#fc7f7f'),
	IconType('', '#e0e0e0')
]


def main():
	for icon in glob.glob('./icon_src/**.svg'):
		base = os.path.basename(icon)
		
		for icon_type in ICON_TYPES:
			source_path = os.path.join(SOURCE_FOLDER, base)
			destination_path = os.path.join(DESTINATION_FOLDER, icon_type.name, base)
			shutil.copy(source_path, destination_path)

			with open(destination_path, 'r') as f:
				raw_svg = f.read()
			
			with open(destination_path, 'w') as f:
				raw_svg = re.sub(FILL_REGEX, f'fill="{icon_type.color}"', raw_svg)
				f.write(raw_svg)

	for icon in KEEP_COLOR:
		source_path = os.path.join(SOURCE_FOLDER, icon + '.svg')
		destination_path = os.path.join(DESTINATION_FOLDER, icon + '.svg')
		shutil.copy(source_path, destination_path)

if __name__ == "__main__":
	main()