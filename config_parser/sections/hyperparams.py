from .base import SectionBase

class HyperparamsSection(SectionBase):
    def __init__(self, max_parallel_experiments=1):
        self.max_parallel_experiments = max_parallel_experiments
