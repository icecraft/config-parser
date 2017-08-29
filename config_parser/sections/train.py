from .jobs import JobSection
from .resources import ResourcesSection
from .tensorflow import Tensorflow

from ..utils import ConfigError, remove_key_dashes


fw_mappings = {
    "tensorflow": Tensorflow,
}

class TrainSection(JobSection):

    schema_file = 'train.json'

    def __init__(self, image, run, resources, framework=None,
                 parameters=None, concurrency=None, **kwargs):

        self.resources = ResourcesSection(**resources)
        self.framework = framework
        self.parameters = parameters
        self.concurrency = concurrency

        if self.framework:
            if self.framework not in kwargs:
                raise ConfigError(
                    "You should include `{0}` block with framework = {0}".format(self.framework)
                )
            fw_data = remove_key_dashes(kwargs.pop(self.framework))
            setattr(self, self.framework, fw_mappings.get(self.framework)(parent=self, **fw_data))

        super(TrainSection, self).__init__(image, run)

    @property
    def framework_config(self):
        # proxy
        return getattr(self, self.framework) if self.framework else {}
