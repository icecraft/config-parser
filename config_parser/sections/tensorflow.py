from .base import SectionBase
from .resources import ResourcesSection

class DistributedJobSection(SectionBase):
    def __init__(self, count=1, resources=None):
        self.count = count
        self.resources = ResourcesSection(**resources) if resources else None

class DistributedMasterOverrideSection(SectionBase):
    def __init__(self, resources=None):
        self.resources = ResourcesSection(**resources) if resources else None

class DistributedSection(SectionBase):
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

class Tensorflow(SectionBase):
    def __init__(self, parent, tensorboard=True, distributed=None, version=None):
        self.tensorboard = tensorboard
        self.version = version
        if distributed:
            self.distributed = DistributedSection(**distributed)
            if not self.distributed.master.resources:
                self.distributed.master.resources = parent.resources
            if not self.distributed.worker.resources:
                self.distributed.worker.resources = parent.resources
            if not self.distributed.ps.resources:
                self.distributed.ps.resources = parent.resources
        else:
            self.distributed = None
