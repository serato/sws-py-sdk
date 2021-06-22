import os
import re
import json

class ServiceUrisService():
    NON_TEST_ENVS = [
        'dev',
        'staging',
        'preprod'
    ]

    def __init__(self, environment):
        if environment not in self.NON_TEST_ENVS:
            test_stack_regex = re.compile(r"^test-[0-9]+$")
            if not test_stack_regex.match(environment):
                raise Exception('Invalid environment')
        self.environment = environment

    def get_default_service_uris(self):
        json_file = open(os.path.dirname(__file__) + "/../data/service_uris.json")
        variables = json.load(json_file)
        json_file.close()

        if self.environment in self.NON_TEST_ENVS:
            return variables[self.environment]

        result = {}
        testUris = variables['test']
        for key, value in testUris.items():
              result[key] = value.replace(":test_env", self.environment)

        return result
