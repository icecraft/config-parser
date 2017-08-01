from .jobs import JobSection


class DeploySection(JobSection):
    schema_file = 'deploy.json'

    def __init__(self, image, run, **kwargs):
        super(DeploySection, self).__init__(image, run)