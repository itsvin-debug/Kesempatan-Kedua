import os
import re

screens_rpy = r'd:\RenpyProjects\DREAM_S1\game\tl\english\screens.rpy'
custom_rpy = r'd:\RenpyProjects\DREAM_S1\game\tl\english\custom_menu_translations.rpy'

# Read screens.rpy definitions
with open(screens_rpy, 'r', encoding='utf-8') as f:
    screens_content = f.read()

# Extract all old definitions in screens.rpy
screens_olds = set(re.findall(r'old\s+"(.*?)"', screens_content, re.DOTALL))

# Read custom_menu_translations.rpy
with open(custom_rpy, 'r', encoding='utf-8') as f:
    custom_lines = f.readlines()

new_custom_lines = []
skip_next = False
for i, line in enumerate(custom_lines):
    if skip_next:
        skip_next = False
        continue
    
    match = re.search(r'old\s+"(.*?)"', line)
    if match:
        old_val = match.group(1)
        if old_val in screens_olds:
            print(f'Removing duplicate from custom: {old_val}')
            skip_next = True
            continue
    new_custom_lines.append(line)

with open(custom_rpy, 'w', encoding='utf-8') as f:
    f.writelines(new_custom_lines)
