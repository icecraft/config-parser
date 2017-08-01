# RiseML config parser

## Installation

You can install config parser:
* via `pip install -e config-parser`, and `config_parser` module will be linked with `config-parser` folder.
* via `requirements.txt`, just add `-e git+https://github.com/riseml/config-parser.git@master#egg=config_parser` to `requirements.txt`
* via `setup.py`:
  * create `dependency-links.txt` in root of your python package (if not exists)
  * add `git+https://github.com/riseml/config-parser.git#egg=config_parser-0.1` to `dependency-links.txt`
  * add `config_parser` to setup's `install_requires` list
  
## Run standalone
 
```bash
 riseml-config-parser [<name-of-config-here>.yml]
```

Without arguments:
```bash
$ riseml-config-parser
WARNING: no input config file supplied. Using file from `tests/sample_config.yml`
{'train': {'inputs': 'sample-data', 'run': ['python run.py -b {{beta}}', 'mybinary {{optim}} {{enabled}} {{beta}} {{learning-rate}}'], 'image': {'name': 'riseml/base:latest-squashed', 'install': ['apt-get -y update', 'apt-get -y install python3-minimal python3-pip', 'pip3 install -r requirements.txt']}, 'hyperparams': {'max_parallel_experiments': 4}, 'framework': 'tensorflow', 'params': {'optim': 'rmsprop abcdef', 'learning_rate': [1.4, 2.9, 4.2], 'more_value': 1, 'enabled': True, 'beta': {'range': {'max': 1, 'step': 0.1, 'min': 0.1}}, 'something': ['test123', 'myvalue3']}, 'tensorflow': {'worker_count': 4, 'ps_count': 2, 'distributed': True, 'tensorboard': 'some/directory/with/summaries'}, 'resources': {'master': {'mem': 1024, 'gpus': 1, 'cpus': 4}, 'worker': {'mem': None, 'gpus': 2, 'cpus': None}, 'ps': None}}, 'repository': 'myRepoName', 'deploy': {'image': {'name': 'riseml/base:latest-squashed', 'install': 'apt-get -y update'}, 'run': 'python3 demo.py'}}
```

It will show parsed json dictionary if config is valid. 
In case when config is not valid, it will show description of `ConfigError` exception like this:
```bash
$ riseml-config-parser riseml.yml
ConfigParseError: Usage of non-declared params: (`gamma`) in run command `python run.py -b {{beta}} -g {{gamma}}`
```