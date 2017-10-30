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
        self.image = ImageSection(**image) if image else None
        self.run = [run] if not isinstance(run, list) else run

    @classmethod
    def post_validate(cls, data):
        if data.get('params'):
            run = data.get('run')
            run_list = [run] if not isinstance(run, list) else run

            for run_line in run_list:
                mentioned_params = set(re.findall('{{([\w-]*)}}', run_line))
                declared_params = set(key.replace('_', '-') for key in data['params'].keys())

                undeclared_params = mentioned_params - declared_params

                if len(undeclared_params) > 0:
                    raise PostValidationError(
                        'Usage of non-declared params: (`%s`) in run command `%s`' %
                        ('`, `'.join(undeclared_params), run_line)
                    )