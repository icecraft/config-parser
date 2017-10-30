import re

from ..utils import PostValidationError
from .base import SectionBase


class JobSection(SectionBase):
    def __init__(self, image, install, run):
        self.image = image
        self.install = [] if not install else install
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