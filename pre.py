"""
This file is part of pre.

pre is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

pre is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Foobar. If not, see <https://www.gnu.org/licenses/>.
"""

# Tiny pre implementation (V0.0.1)
# This impl included: #include and #define

import re
import sys

def preprocess_file(file_path, defines, processed_files):
    if file_path in processed_files:
        return []

    processed_files.add(file_path)
    processed_lines = []

    with open(file_path, 'r') as infile:
        lines = infile.readlines()

    for line in lines:
        include_match = re.match(r'#include\s+"(.*)"', line)
        define_match = re.match(r'#define\s+(\S+)\s+(.*)', line)

        if include_match:
            include_file = include_match.group(1)
            processed_lines.extend(preprocess_file(include_file, defines, processed_files))
        elif define_match:
            macro, value = define_match.groups()
            defines[macro.replace('"', "")] = value.replace('"', "")
        else:
            for macro, value in defines.items():
                line = re.sub(r'\b' + re.escape(macro) + r'\b', value, line)
            processed_lines.append(line)

    return processed_lines

def preprocess(input_file, output_file):
    defines = {}
    processed_files = set()
    processed_lines = preprocess_file(input_file, defines, processed_files)

    with open(output_file, 'w') as outfile:
        outfile.writelines(processed_lines)

if len(sys.argv) == 2:
    preprocess(sys.argv[1], "a.out")
elif len(sys.argv) == 3:
    preprocess(sys.argv[1], sys.argv[2])
else:
    print("Tiny IMPL of pre")
    print("Usage: [INPUT] [OUTPUT]")
