import requests


class {{ cookiecutter.tool_class_name }}API(object):
    """
    A simple client for the {{ cookiecutter.tool_name }} API
    """

    def __init__(self, tool_config):
        if tool_config.authentication_type == "API":
            self.api_key = tool_config.api_key
            self.url = tool_config.url
        else:
            raise Exception('{{ cookiecutter.tool_name }} Authentication type {} not supported'.format(tool_config.authentication_type))

    def get_findings(self, sk1):
        url = f"{self.url}/api/v1/vulnerabilities?id={sk1}"

        response = requests.get(
            url=url,
            headers=self.get_headers(),
        )
        response.raise_for_status()
        return response.json()

    def get_headers(self):
        headers = {
            "X-API-TOKEN": self.api_key,
            "Content-Type": "application/json",
            "User-Agent": "DefectDojo",
        }

        return headers
