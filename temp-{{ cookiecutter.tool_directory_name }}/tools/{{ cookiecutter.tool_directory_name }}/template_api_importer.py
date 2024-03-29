from dojo.models import Product_API_Scan_Configuration
from .api_client import {{ cookiecutter.tool_class_name }}API


class {{ cookiecutter.tool_class_name }}Importer(object):
    """
    Import from {{ cookiecutter.tool_name }} API
    """

    def get_findings(self, test):
        client, config = self.prepare_client(test)
        findings = client.get_findings(config.service_key_1)
        return findings

    def prepare_client(self, test):
        product = test.engagement.product
        if test.api_scan_configuration:
            config = test.api_scan_configuration
            if config.product != product:
                raise Exception('API Scan Configuration for {{ cookiecutter.tool_name }} and Product do not match.')
        else:
            configs = Product_API_Scan_Configuration.objects.filter(product=product)
            if configs.count() == 1:
                config = configs.first()
            elif configs.count() > 1:
                raise Exception(
                    'More than one Product API Scan Configuration has been configured, but none of them has been chosen.\n'
                    'Please specify at Test which one should be used.'
                )
            else:
                raise Exception(
                    'There are no API Scan Configurations for this Product.\n'
                    'Please add at least one API Scan Configuration for {{ cookiecutter.tool_name }} to this Product.'
                )

        tool_config = config.tool_configuration
        return {{ cookiecutter.tool_class_name }}API(tool_config), config
