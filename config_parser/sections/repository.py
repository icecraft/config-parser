import re

from ..utils import ConfigError

from .deploy import DeploySection
from .train import TrainSection
from .base import SectionBase


class RepositoryConfig(SectionBase):
    schema_file = 'repository.json'

    def __init__(self, project, train=None, deploy=None):
        self.project = project
        if not re.match(r'^[A-Za-z0-9][A-Za-z0-9_\-]*[A-Za-z0-9]$', project):
            raise ConfigError('Project name must start and end with an alphanumeric character and may additionally consist out of hyphens and underscores inbetween.')

        if train:
            self.train = TrainSection(**train)
        if deploy:
            self.deploy = DeploySection(**deploy)
