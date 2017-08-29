from .deploy import DeploySection
from .train import TrainSection
from .base import SectionBase


class RepositoryConfig(SectionBase):
    schema_file = 'repository.json'

    def __init__(self, project, train=None, deploy=None):
        self.project = project

        if train:
            self.train = TrainSection(**train)
        if deploy:
            self.deploy = DeploySection(**deploy)
