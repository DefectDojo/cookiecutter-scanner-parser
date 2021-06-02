from django.test import TestCase
from dojo.tools.{{ cookiecutter.tool_directory_name }}.parser import {{ cookiecutter.tool_class_name }}Parser
from dojo.models import Test


class Test{{ cookiecutter.tool_class_name }}Parser(TestCase):

    def test_{{ cookiecutter.tool_directory_name }}_parser_with_no_vuln_has_no_findings(self):
        testfile = open("dojo/unittests/scans/{{ cookiecutter.tool_directory_name }}/{{ cookiecutter.tool_directory_name }}_zero_vul.{{ cookiecutter.tool_file_type|lower }}")
        parser = {{ cookiecutter.tool_class_name }}Parser()
        findings = parser.get_findings(testfile, Test())
        testfile.close()
        self.assertEqual(0, len(findings))

    def test_{{ cookiecutter.tool_directory_name }}_parser_with_one_criticle_vuln_has_one_findings(self):
        testfile = open("dojo/unittests/scans/{{ cookiecutter.tool_directory_name }}/{{ cookiecutter.tool_directory_name }}_one_vul.{{ cookiecutter.tool_file_type|lower }}")
        parser = {{ cookiecutter.tool_class_name }}Parser()
        findings = parser.get_findings(testfile, Test())
        testfile.close()
        for finding in findings:
            for endpoint in finding.unsaved_endpoints:
                endpoint.clean()
        self.assertEqual(1, len(findings))
        self.assertEqual("handlebars", findings[0].component_name)
        self.assertEqual("4.5.2", findings[0].component_version)

    def test_{{ cookiecutter.tool_directory_name }}_parser_with_many_vuln_has_many_findings(self):
        testfile = open("dojo/unittests/scans/{{ cookiecutter.tool_directory_name }}/{{ cookiecutter.tool_directory_name }}_many_vul.{{ cookiecutter.tool_file_type|lower }}")
        parser = {{ cookiecutter.tool_class_name }}Parser()
        findings = parser.get_findings(testfile, Test())
        testfile.close()
        for finding in findings:
            for endpoint in finding.unsaved_endpoints:
                endpoint.clean()
        self.assertEqual(3, len(findings))

    def test_{{ cookiecutter.tool_directory_name }}_parser_empty_with_error(self):
        with self.assertRaises(ValueError) as context:
            testfile = open("dojo/unittests/scans/{{ cookiecutter.tool_directory_name }}/empty_with_error.{{ cookiecutter.tool_file_type|lower }}")
            parser = {{ cookiecutter.tool_class_name }}Parser()
            findings = parser.get_findings(testfile, Test())
            testfile.close()
            for finding in findings:
                for endpoint in finding.unsaved_endpoints:
                    endpoint.clean()
            self.assertTrue(
                "{{ cookiecutter.tool_name }} report contains errors:" in str(context.exception)
            )
            self.assertTrue("ECONNREFUSED" in str(context.exception))
