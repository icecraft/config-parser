from .jobs import JobSection
from .resources import ResourcesSection
from .tensorflow import Tensorflow

from ..utils import ConfigError, remove_key_dashes


fw_mappings = {
    "tensorflow": Tensorflow,
}

class TrainSection(JobSection):

    schema_file = 'train.json'

    def __init__(self, run, resources, image=None, install=None, framework=None,
                 parameters=None, concurrency=None, **kwargs):

        self.resources = ResourcesSection(**resources)
        self.framework = framework
        self.parameters = parameters
        self.concurrency = concurrency

        if self.framework:
            fw_data = dict()
            if self.framework in kwargs:
                fw_data = remove_key_dashes(kwargs.pop(self.framework))
            setattr(self, self.framework, fw_mappings.get(self.framework)(parent=self, **fw_data))

        super(TrainSection, self).__init__(image, install, run)

        self.map_tensorflow_image()
        if not self.image:
            raise ConfigError("No image configured")

    def map_tensorflow_image(self):
        if self.framework == 'tensorflow' and not self.image:
            tensorflow = getattr(self, 'tensorflow')
            name = tensorflow.version if tensorflow.version else 'latest'
            if self.resources.gpus > 0 or (tensorflow.distributed and tensorflow.distributed.type == 'default' and (
                    tensorflow.distributed.master.resources.gpus > 0 or
                    tensorflow.distributed.worker.resources.gpus > 0 or
                    tensorflow.distributed.ps.resources.gpus > 0)):
                name += '-gpu'
            self.image = 'tensorflow/tensorflow:{}'.format(name)


    @property
    def framework_config(self):
        # proxy
        return getattr(self, self.framework) if self.framework else {}
