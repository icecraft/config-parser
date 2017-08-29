from .base import SectionBase

class ResourcesSection(SectionBase):
    def __init__(self, cpus=None, gpus=None, mem=None):
        self.cpus = cpus
        self.mem = mem
        self.gpus = gpus
