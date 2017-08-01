from .deploy import DeploySection
from .train import TrainSection
from .base import SectionBase


class RepositoryConfig(SectionBase):
    schema_file = 'repository.json'

    def __init__(self, repository, train=None, deploy=None):
        self.repository = repository

        if train:
            self.train = TrainSection(**train)
        if deploy:
            self.deploy = DeploySection(**deploy)