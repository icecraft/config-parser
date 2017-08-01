import yaml
import json
import jsonschema
from jsonschema.exceptions import ValidationError
import os.path as P

from ..utils import ConfigError, ConfigValidationError, remove_key_dashes


class SectionBase(object):
    schema_file = None

    def __iter__(self):
        for key in self.__dict__:
            value = getattr(self, key)
            if isinstance(value, SectionBase):
                value = dict(value)
            yield key, value

    def __getitem__(self, item):
        return self.__dict__[item]

    @classmethod
    def from_dict(cls, data):
        # exception can be raised here
        cls.validate(data)

        return cls(**remove_key_dashes(data, exceptions=['params']))

    @classmethod
    def from_json(cls, json_text):
        try:
            data = json.loads(json_text)
        except ValueError as e:
            raise ConfigError('Incorrect json: ', e)

        return cls.from_dict(data)

    @classmethod
    def from_yml_file(cls, filename):
        with open(filename, 'rb') as f:
            return cls.from_yml(f.read())

    @classmethod
    def from_yml(cls, yml_text):
        data = yaml.load(yml_text)
        return cls.from_dict(data)

    @classmethod
    def validate(cls, data):
        assert cls.schema_file is not None, \
            'You should set `%s` for independently validated section `%s`' \
            % ('schema_file', cls.__name__)

        schemas_path = P.join(P.dirname(P.abspath(__file__)), '../schemas')

        base_schema_path = P.join(schemas_path, cls.schema_file)
        with open(base_schema_path) as f:
            schema = json.load(f)

        # to enable support of local refs
        resolver = jsonschema.RefResolver('file://' + schemas_path + '/', None)

        try:
            jsonschema.validate(data, schema, resolver=resolver)
        except ValidationError as e:
            # re-raise it with our exception adapter
            raise ConfigValidationError(exc=e)