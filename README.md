# RiseML Config Parser

The RiseML config parser parses and validates the `riseml.yml` configuration file used to describe RiseML experiments.

## Installation

To use the config parser in a program/library, you have several options.
Install:
* via `pip install -e path/to/config-parser`
* via `requirements.txt` - add `-e git+https://github.com/riseml/config-parser.git@master#egg=config_parser` to `requirements.txt`
* via `setup.py` add `git+https://github.com/riseml/config-parser.git@master#egg=config_parser-0.1.0` to setup's kwarg `dependency_links`
  
## Run standalone
 
You can also run the config parser in standalone mode:

```bash
 riseml-config-parser [<name-of-config-here>.yml]
``

Without arguments:
```bash
$ riseml-config-parser riseml.yml
{
    "train": {
        "image": {
            "name": "tensorflow/tensorflow:1.2.1",
            "install": [
                "pip install -r requirements.txt"
            ]
        },
        "run": [
            "sleep 10",
            "ls | grep x",
            "python cifar10.py --epochs 2"
        ],
        "framework": "tensorflow",
        "resources": {
            "gpus": 0,
            "cpus": 0.3,
            "mem": 496
        },
        "parameters": null,
        "concurrency": null,
        "tensorflow": {
            "tensorboard": true,
            "distributed": null
        }
    },
    "project": "cifar10-example"
}

```

It will show a parsed json dictionary if the configuration is valid. 
If the configuration is not valid, it will show description of `ConfigError` exception like this:
```bash
$ riseml-config-parser riseml.yml
ConfigParseError: Usage of non-declared params: (`gamma`) in run command `python run.py -b {{beta}} -g {{gamma}}`
```
