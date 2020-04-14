import re
file = open('', encoding='UTF-8')

pattern = "[0-9][0-9]\.[0-9][0-9]"
pattern_alder = "[0-9]*-.rig"
pattern_fire = '["ild", "brand"]'

while True:
    line = file.readline()
    match = re.search(pattern, line)
    alder_match = re.search(pattern_alder, line)
    if match:
        print(match[0])
    if alder_match:
        print(alder_match[0])
    if not line:
        break
file.close()
