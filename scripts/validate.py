"""pip install pyyaml jsonschema"""
import glob, json, yaml, jsonschema
s = json.load(open("schema/provider.schema.json"))
for f in sorted(glob.glob("providers/*.yaml")):
    jsonschema.validate(yaml.safe_load(open(f)), s); print("ok", f)
