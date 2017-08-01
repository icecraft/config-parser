from .utils import ConfigValidationError
from .sections.repository import RepositoryConfig


if __name__ == '__main__':
    import sys
    try:
        if len(sys.argv) > 1:
            path = sys.argv[1]
        else:
            path = 'sample_config.yml'

        c = RepositoryConfig.from_yml_file('api/configs/%s' % path)
        print(dict(c))

        # from .sections.deploy import DeploySection
        # deploy = DeploySection.from_yml_file('api/config_parser/sample_deploy.yml')
        # print(dict(deploy))

    except ConfigValidationError as e:
        print('ConfigParseError:')
        print(e.message)