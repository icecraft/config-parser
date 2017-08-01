from .base import SectionBase

# from ...models import Node
# from ...db import session
#
#
# def get_default_num_gpus():
#     nodes = session.query(Node)
#     return max([n.gpus for n in nodes] + [0])


class ResourceValuesSection(SectionBase):
    def __init__(self, cpus=None, gpus=None, mem=None):
        self.cpus = cpus
        self.mem = mem
        self.gpus = gpus

        # if gpus is not None:
        #     self.gpus = gpus
        # else:
        #     self.gpus = get_default_num_gpus()


class ResourcesSection(SectionBase):
    def __init__(self, master=None, worker=None, ps=None):
        self.master = ResourceValuesSection(**master) if master else None
        self.worker = ResourceValuesSection(**worker) if worker else None
        self.ps = ResourceValuesSection(**ps) if ps else None