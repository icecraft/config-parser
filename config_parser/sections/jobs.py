import re

from ..utils import PostValidationError
from .base import SectionBase


class ImageSection(SectionBase):
    def __init__(self, name, install=None):
        self.name = name
        self.install = [] if not install else install

        # check if image exists here


class JobSection(SectionBase):
    def __init__(self, image, run):
        self.image = ImageSection(**image)
        self.run = run

    @classmethod
    def post_validate(cls, data):
        if data.get('params'):
            mentioned_params = set(re.findall('{{([\w-]*)}}', data['run']))
            declared_params = set(data['params'].keys())

            undeclared_params = mentioned_params - declared_params

            if len(undeclared_params) > 0:
                raise PostValidationError(
                    'Usage of non-declared params: (`%s`) in run command `%s`' %
                    ('`, `'.join(undeclared_params), data['run'])
                )