---
title: "A DefectDojo scanner parser template generator"
date: 2021-03-26T20:46:28+01:00
draft: false
---

{{% notice info %}}
All commands assume that you're located at the root of the django-DefectDojo cloned repo.
{{% /notice %}}

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for generating
a new [DefectDojo](https://www.defectdojo.org/) scanner parser.

## Features

- Generates the appropriate file structure and parser for a minimal scanner parser.
- Contains everything needed to get started with writing unit tests for your scanner parser.

## Installation

To get started you will need to install [cookiecutter](https://github.com/cookiecutter/cookiecutter).

```bash
$ pip install cookiecutter
```

Then generate your scanner parser from the root of django-DefectDojo:

```bash
$ cookiecutter https://github.com/DefectDojo/cookiecutter-scanner-parser
```

## Context Options

You will be asked to provide the following values to configure your scanner parser:

| Field               | Default                               | Description                                                                                                                                                                                  |
| ------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                                            |
| tool name           | My Scanner                            | The human readable name of your scanner.                                                                                                                                                     |
| tool_directory_name | Lowercase name of my scanner          | The directory name of the scanner (in most cases choose the default).                                                                                                                        |
| tool_class_name     | Capitalized name of scanner           | Class name of scanner in the parser.py file. (in most cases choose the default).                                                                                                             |
| tool_description    | My scanner is for ....                | Brief Description of scanner                                                                                                                                                                 |
| tool_type           | None                                  | Select the kind of scanner, static or dynamic.                                                                                                                                               |
| tool_file_type      | None                                  | Scanner import file type: CSV, JSON or XML.                                                                                                                                                  |

## On completion

The directory, parser and scanner will be copied to the appropriate folder locations.

Sample Output:

```bash
######################################
File templates created for Fossa
######################################
../temp-fossa/tools/fossa/__init__.py
../temp-fossa/tools/fossa/parser.py
../temp-fossa/unittests/tools/test_fossa_parser.py
../temp-fossa/unittests/scans/fossa/empty_with_error.json
../temp-fossa/unittests/scans/fossa/fossa_many_vul.json
../temp-fossa/unittests/scans/fossa/fossa_zero_vul.json
../temp-fossa/unittests/scans/fossa/fossa_one_vul.json
######################################
Files moved to:
######################################
/django-DefectDojo/dojo/tools
/django-DefectDojo/dojo/unittests/scans
/django-DefectDojo/dojo/unittests/tools/test_fossa_parser.py
Modified: dojo/fixtures/test_type.json
Added:
{
    "fields": {
        "name": "Fossa"
    },
    "model": "dojo.test_type",
    "pk": 232
}
Removing temp directory
######################################
Complete, go forth and make it so!
######################################
```