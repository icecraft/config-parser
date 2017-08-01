from .jobs import JobSection
from .resources import ResourcesSection, ResourceValuesSection
from .frameworks import fw_mappings
from .hyperparams import HyperparamsSection

from ..utils import ConfigError, remove_key_dashes


class TrainSection(JobSection):

    schema_file = 'train.json'

    def __init__(self, image, run, inputs=None, framework=None, resources=None,
                 params=None, hyperparams=None, **kwargs):

        self.framework = framework
        self.inputs = inputs if inputs else None
        self.params = params
        self.hyperparams = HyperparamsSection(**(hyperparams or {}))

        if self.framework:
            if self.framework not in kwargs:
                raise ConfigError(
                    "You should include `{0}` block with framework = {0}".format(self.framework)
                )
            fw_data = remove_key_dashes(kwargs.pop(self.framework))
            setattr(self, self.framework, fw_mappings.get(self.framework)(**fw_data))


        if not resources:
            self.resources = None
        elif resources.get('cpus'):
            if hasattr(self, 'tensorflow') and self.tensorflow.distributed:
                raise ConfigError(
                    'You need to set `master`, `worker` and `ps` '
                    'resource groups for distributed jobs'
                )
            self.resources = ResourceValuesSection(**resources)
        else:
            if hasattr(self, 'tensorflow') and not self.tensorflow.distributed:
                raise ConfigError(
                    'You need to set single resource `mem`, `cpus` and `gpus` '
                    'values for non-distributed jobs. '
                )
            self.resources = ResourcesSection(**resources)

        super(TrainSection, self).__init__(image, run)

    @property
    def framework_details(self):
        # proxy
        return getattr(self, self.framework) if self.framework else {}
