from .base import SectionBase


class ImageSection(SectionBase):
    def __init__(self, name, install=None):
        self.name = name
        self.install = [] if not install else install

        # check if image exists here


class JobSection(SectionBase):
    def __init__(self, image, run):
        self.image = ImageSection(**image)
        self.run = run