from jsonschema import _utils


class ConfigError(Exception):
    pass


class ConfigValidationError(ConfigError):
    def __init__(self, message=None, exc=None, *args):
        if not exc:
            raise ValueError('`exc` with type `jsonschema.exception.ValidationError` '
                             'needs to be supplied when raising ConfigValidationError')

        message = ('%s\n' % message) if message else ''
        message += 'On instance: %s\n' % _utils.format_as_index(exc.relative_path)
        message += 'Error: %s' % exc.args[0]

        super(ConfigValidationError, self).__init__(message, *args)


class PostValidationError(ConfigError):
    pass


def parse_int(v):
    if v:
        try:
            return int(v)
        except ValueError:
            raise ConfigError('not an int: %s' % v)


def remove_key_dashes(data, exceptions=[]):
    if isinstance(data, dict):
        new_dict = {}

        for k, v in data.items():
            value = v if k in exceptions else remove_key_dashes(v, exceptions)
            new_dict[k.replace('-', '_')] = value

        return new_dict
    else:
        return data

def remove_empty_values(data):
    if isinstance(data, dict):
        return dict((k, v) for k, v in data.items() if v is not None)
    else:
        return data
