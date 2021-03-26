import shutil
import os
filename = "{{cookiecutter.tool_file_type}}".lower() + "_parser.py"
print(os.getcwd())
# Copy the appropriate template to the scanner folder
shutil.copyfile("../parser_templates/" + filename, "../temp-{% raw %}{{ cookiecutter.tool_directory_name }}{% endraw %}/tools/{% raw %}{{ cookiecutter.tool_directory_name }}{% endraw %}/parser.py")