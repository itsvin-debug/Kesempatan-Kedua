import urllib.request
import urllib.parse
import json
import time

def translate_to_english(text):
    if not text.strip() or "....." in text:
        return text
        
    encoded_text = urllib.parse.quote(text)
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=id&tl=en&dt=t&q={encoded_text}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return "".join([x[0] for x in data[0]])
    except Exception as e:
        print(f"Error translating: {text} - {e}")
        return text

file_path = 'd:/RenpyProjects/DREAM_S1/game/tl/english/script.rpy'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i in range(len(lines)):
    line = lines[i]
    if line.strip().startswith('#') or line.strip() == '' or line.startswith('translate english') or 'label' in line or 'return' in line:
        new_lines.append(line)
        continue
        
    # Find the line that needs translation
    # Example format: n "halo"
    # or "ini narasi"
    # we need to preserve the prefix and quotes
    parts = line.split('\"')
    if len(parts) >= 3:
        prefix = parts[0]
        text_to_translate = parts[1]
        suffix = '\"'.join(parts[2:])
        
        # Don't translate tags like {color=#...}
        if '{' in text_to_translate:
             new_lines.append(line)
             continue
             
        translated = translate_to_english(text_to_translate)
        # Avoid rate limits
        time.sleep(0.3)
        new_lines.append(f'{prefix}"{translated}"{suffix}')
        print(f"[{i}/{len(lines)}] {text_to_translate} -> {translated}")
    else:
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
    
print("Translation complete.")
