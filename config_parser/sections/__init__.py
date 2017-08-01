from .deploy import DeploySection
from .train import TrainSection
from .repository import RepositoryConfig
from .resources import ResourcesSection, ResourceValuesSection

__all__ = ['RepositoryConfig', 'DeploySection', 'TrainSection', 'job_section_classes',
           'ResourcesSection', 'ResourceValuesSection', ]

job_section_classes = {
    'deploy': DeploySection,
    'train': TrainSection
}