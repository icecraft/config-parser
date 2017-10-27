from __future__ import print_function

import json
from config_parser.utils import ConfigError
from config_parser.sections.repository import RepositoryConfig


def main():
    import sys
    import os.path as P

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print('WARNING: no input config file supplied. Using file from `tests/sample_config.yml`')
        path = P.join(P.dirname(__file__), 'tests/sample_config.yml')

    try:
        c = RepositoryConfig.from_yml_file(path)
        print(json.dumps(dict(c), indent=4))

        # from .sections.deploy import DeploySection
        # deploy = DeploySection.from_yml_file('api/config_parser/sample_deploy.yml')
        # print(dict(deploy))

    except ConfigError as e:
        print('ConfigParseError: %s' % e)


if __name__ == '__main__':
    main()