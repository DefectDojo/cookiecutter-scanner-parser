import json
import os
import shutil

tool_directory = "{{cookiecutter.tool_directory_name}}"
source = "../temp-{{cookiecutter.tool_directory_name}}/"
destination = 'dojo/'
filename = 'dojo/fixtures/test_type.json'

# Add the scanner to the test types
maxNum = 0
new_scanner_json = None
with open(filename) as test_fixtures:
    test_types = json.load(test_fixtures)
    for test in test_types:
        if maxNum < test["pk"]:
            maxNum = test["pk"]

    new_scanner = f'{% raw %}{{ "fields": {{ "name": "{% endraw %}{{cookiecutter.tool_name}}" {% raw %}}}, "model":"dojo.test_type", "pk":{maxNum+1}}}{% endraw %}'
    new_scanner_json = json.loads(new_scanner)
    test_types.append(new_scanner_json)

    with open(filename, 'w') as f:
        json.dump(test_types, f, indent=4)

print("######################################")
print("File templates created for {{cookiecutter.tool_name}}")
print("######################################")
for subdir, dirs, files in os.walk(source):
    for filename in files:
        if filename.endswith(".DS_Store") is False:
            print(subdir + os.sep + filename)

print("######################################")
print("Files moved to:")
print("######################################")
print(destination + "tools")
shutil.move(source + "tools/" + tool_directory, destination + "/tools")

print(destination + "unittests/scans")
shutil.move(source + "unittests/scans/" + tool_directory, destination + "unittests/scans")

print(destination + "unittests/tools/test_{{ cookiecutter.tool_directory_name }}_parser.py")
shutil.move(source + "unittests/tools/test_{{ cookiecutter.tool_directory_name }}_parser.py", destination + "unittests/tools")

print("Modified: dojo/fixtures/test_type.json")
print("Added:")
print(json.dumps(new_scanner_json, indent=4))
print("Removing temp directory")
shutil.rmtree(source)
print("######################################")
print("Complete, go forth and make it so!")
print("######################################")