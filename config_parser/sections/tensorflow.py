from ..utils import ConfigError
from .base import SectionBase
from .resources import ResourcesSection

class DistributedJobSection(SectionBase):
    def __init__(self, count=1, resources=None):
        self.count = count
        self.resources = ResourcesSection(**resources) if resources else None

class DistributedMasterOverrideSection(SectionBase):
    def __init__(self, resources=None):
        self.resources = ResourcesSection(**resources) if resources else None

class TFDistributedDefaultSection(SectionBase):
    def __init__(self, master=None, worker=None, ps=None):
        self.master = DistributedMasterOverrideSection(**(master or {}))
        if isinstance(worker, int):
            self.worker = DistributedJobSection(count=worker)
        else:
            self.worker = DistributedJobSection(**(worker or {}))
        if isinstance(ps, int):
            self.ps = DistributedJobSection(count=ps)
        else:
            self.ps = DistributedJobSection(**(ps or {}))

class TFHorovodSection(SectionBase):
    def __init__(self, workers=None, version=None):
        self.version = version
        self.workers = workers

class Tensorflow(SectionBase):
    def __init__(self, parent, version=None, tensorboard=True, distributed=None, horovod=None):
        self.version = version
        self.tensorboard = tensorboard
        self.distributed = None
        self.horovod = None
        if distributed:
            self.distributed = TFDistributedDefaultSection(**distributed)
            if not self.distributed.master.resources:
                self.distributed.master.resources = parent.resources
            if not self.distributed.worker.resources:
                self.distributed.worker.resources = parent.resources
            if not self.distributed.ps.resources:
                self.distributed.ps.resources = parent.resources
        if horovod:
            if self.distributed:
                raise ConfigError("You cannot use Distributed TensorFlow and Horovod at the same time!")
            self.horovod = TFHorovodSection(**horovod)
