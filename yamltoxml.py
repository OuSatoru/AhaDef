import yaml
import plistlib

data = yaml.load(open('ahadef.yaml'))

print(data)

with open('ahadef.tmLanguage', 'wb') as f:
    plistlib.dump(data, f)

