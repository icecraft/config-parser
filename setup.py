from setuptools import setup, find_packages

setup(
    name='config_parser',
    version='0.2.0',
    description="RiseML Config Parser",
    author_email="contact@riseml.com",
    url="https://riseml.com",
    keywords=["RiseML"],
    entry_points={
        'console_scripts': [
          'riseml-config-parser = config_parser.__main__:main'
        ]
    },
    install_requires=['jsonschema >= 2.6.0', 'ruamel.yaml'],
    packages=find_packages(),
    include_package_data=True,
    long_description=""
)