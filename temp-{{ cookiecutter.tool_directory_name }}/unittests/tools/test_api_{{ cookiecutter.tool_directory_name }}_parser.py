from django.test import TestCase

from dojo.tools.{{ cookiecutter.tool_directory_name }}.parser import {{ cookiecutter.tool_class_name }}Parser
from dojo.models import Test


class Test{{ cookiecutter.tool_class_name }}Parser(TestCase):

    def test_get_scan_types(self):
        parser = {{ cookiecutter.tool_class_name }}Parser()
        self.assertEqual(parser.get_scan_types(), ["{{ cookiecutter.tool_name }} Scan"])

    def test_get_label_for_scan_types(self):
        scan_type = "{{ cookiecutter.tool_name }} Scan"
        parser = {{ cookiecutter.tool_class_name }}Parser()
        self.assertEqual(parser.get_label_for_scan_types(scan_type), "{{ cookiecutter.tool_name }} Scan")

    def get_description_for_scan_types(self):
        scan_type = "{{ cookiecutter.tool_name }} Scan"
        parser = {{ cookiecutter.tool_class_name }}Parser()
        self.assertEqual(
            parser.get_description_for_scan_types(scan_type),
            "{{ cookiecutter.tool_name }} findings can be imported by API"
        )

    def test_requires_file(self):
        parser = {{ cookiecutter.tool_class_name }}Parser()
        self.assertEqual(parser.requires_file("scan_type"), False)

    def test_requires_tool_type(self):
        parser = {{ cookiecutter.tool_class_name }}Parser()
        self.assertEqual(parser.requires_tool_type("scan_type"), "{{ cookiecutter.tool_name }}")

    def test_parse_file_with_no_vuln_has_no_findings(self):
        with open("unittests/scans/{{ cookiecutter.tool_directory_name }}/no_vuln.json") as testfile:
            parser = {{ cookiecutter.tool_class_name }}Parser()
            findings = parser.get_findings(testfile, Test())
            self.assertEqual(0, len(findings))

    def test_parse_file_with_one_vuln_has_one_findings(self):
        with open("unittests/scans/{{ cookiecutter.tool_directory_name }}/one_vuln.json") as testfile:
            parser = {{ cookiecutter.tool_class_name }}Parser()
            findings = parser.get_findings(testfile, Test())
            self.assertEqual(1, len(findings))
            finding = findings[0]
            self.assertEqual(finding.title, "Cross-site scripting (reflected)")
            self.assertEqual(finding.date, "2014-12-05")
            self.assertEqual(finding.cwe, 75)
            self.assertEqual(1, len(finding.unsaved_vulnerability_ids))
            self.assertEqual(finding.unsaved_vulnerability_ids[0], "CVE-2021-5300")
            self.assertEqual(finding.cvssv3, "CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N")
            self.assertEqual(finding.url, "192.168.1.1")
            self.assertEqual(finding.severity, "High")
            self.assertEqual(finding.description, "Description Text")
            self.assertEqual(finding.mitigation, "Remediation Text")
            self.assertEqual(finding.active, True)
            self.assertEqual(finding.tags, ["APPROVED", "Demo-Asset", "ABC Corporate", "test"])
            self.assertEqual(finding.unique_id_from_tool, 21581)
            self.assertEqual(1, len(finding.unsaved_endpoints))
            self.assertEqual(finding.unsaved_endpoints[0].host, "192.168.1.1")
            self.assertEqual(finding.unsaved_endpoints[0].protocol, None)

    def test_parse_file_with_multiple_vuln_has_multiple_finding(self):
        with open("unittests/scans/{{ cookiecutter.tool_directory_name }}/many_vulns.json") as testfile:
            parser = {{ cookiecutter.tool_class_name }}Parser()
            findings = parser.get_findings(testfile, Test())
            self.assertEqual(2, len(findings))
            finding_1 = findings[0]
            finding_2 = findings[1]
            self.assertEqual(finding_1.title, "Cross-site scripting (reflected)")
            self.assertEqual(finding_1.date, "2014-12-05")
            self.assertEqual(finding_1.cwe, 75)
            self.assertEqual(1, len(finding_1.unsaved_vulnerability_ids))
            self.assertEqual(finding_1.unsaved_vulnerability_ids[0], "CVE-2021-5300")
            self.assertEqual(finding_1.cvssv3, None)
            self.assertEqual(finding_1.url, "https://test.example.com")
            self.assertEqual(finding_1.severity, "High")
            self.assertEqual(finding_1.description, "Description Text")
            self.assertEqual(finding_1.mitigation, "Remediation Text")
            self.assertEqual(finding_1.active, True)
            self.assertEqual(finding_1.tags, ["APPROVED", "Demo-Asset"])
            self.assertEqual(finding_1.unique_id_from_tool, 21581)
            self.assertEqual(1, len(finding_1.unsaved_endpoints))
            self.assertEqual(finding_1.unsaved_endpoints[0].host, "test.example.com")
            self.assertEqual(finding_1.unsaved_endpoints[0].protocol, "https")
            self.assertEqual(finding_2.title, "Directory listing")
            self.assertEqual(finding_2.date, "2014-09-05")
            self.assertEqual(finding_2.cwe, 77)
            self.assertEqual(1, len(finding_2.unsaved_vulnerability_ids))
            self.assertEqual(finding_2.unsaved_vulnerability_ids[0], "CVE-2021-4008")
            self.assertEqual(finding_2.cvssv3, "CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N")
            self.assertEqual(finding_2.url, "example.test.com")
            self.assertEqual(finding_2.severity, "Low")
            self.assertEqual(finding_2.description, "Description Text 2")
            self.assertEqual(finding_2.mitigation, "Remediation Text 2")
            self.assertEqual(finding_2.active, False)
            self.assertEqual(finding_2.tags, [])
            self.assertEqual(finding_2.unique_id_from_tool, 21583)
            self.assertEqual(1, len(finding_2.unsaved_endpoints))
            self.assertEqual(finding_2.unsaved_endpoints[0].host, "example.test.com")
            self.assertEqual(finding_2.unsaved_endpoints[0].protocol, None)
