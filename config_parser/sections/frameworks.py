from .base import SectionBase
from ..utils import ConfigError


class BaseFrameworkSection(SectionBase):
    pass


class Tensorflow(BaseFrameworkSection):
    def __init__(self, tensorboard, distributed=False, ps_count=None, worker_count=None, ):
        self.tensorboard = tensorboard
        self.distributed = distributed

        if not distributed:
            if ps_count or worker_count:
                raise ConfigError('ps_count and worker_count makes no sense '
                                  'with non-distributed jobs')
        else:
            if ps_count and worker_count:
                self.ps_count = ps_count
                self.worker_count = worker_count
            else:
                raise ConfigError('ps_count and worker_count is required '
                                  'for distributed jobs')


class RiseMLBasic(BaseFrameworkSection):
    pass

fw_mappings = {
    "tensorflow": Tensorflow,
    "riseml_basic": RiseMLBasic
}