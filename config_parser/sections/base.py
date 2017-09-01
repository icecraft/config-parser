import yaml
import json
import jsonschema
from jsonschema.exceptions import ValidationError
import os.path as P

from ..utils import ConfigError, ConfigValidationError, remove_key_dashes, remove_empty_values


class SectionBase(object):
    schema_file = None

    def __new__(cls, *args, **kwargs):
        cls.post_validate(kwargs)
        return object.__new__(cls)

    def __iter__(self):
        for key in self.__dict__:
            value = getattr(self, key)
            if isinstance(value, SectionBase):
                value = dict(value)
            yield key.replace('_', '-'), value

    def __getitem__(self, item):
        return self.__dict__[item]

    def as_dict(self):
        return remove_empty_values(dict(self))

    @classmethod
    def from_dict(cls, data):
        # exception can be raised here
        cls.validate(data)

        return cls(**remove_key_dashes(data, exceptions=['parameters']))

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
        try:
            data = yaml.safe_load(yml_text)
        except yaml.YAMLError, exc:
            raise ConfigError("Error in configuration file: {}".format(exc))
        return cls.from_dict(data)

    @classmethod
    def validate(cls, data):
        cls.pre_validate(data)

        assert cls.schema_file is not None, \
            'You should set `%s` for independently validated section `%s`' \
            % ('schema_file', cls.__name__)

        schemas_path = P.join(P.dirname(P.dirname(P.abspath(__file__))), 'schemas')

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

    @classmethod
    def pre_validate(cls, data):
        """
        Override this method with additional validators.
        They will be applied BEFORE jsonschema validation.
        Note: don't rely blindly on dictionary keys, structure can be invalid.
        """
        pass

    @classmethod
    def post_validate(cls, data):
        """
        Override this method with additional validators.
        They will be applied AFTER jsonschema structure will be validated.
        Dictionary keys can be accessed safely.
        """
        pass
