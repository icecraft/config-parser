# RiseML config parser

## Installation

You can install config parser:
* via `pip instal -e config-parser`, and `config_parser` module will be linked with `config-parser` folder.
* via `requirements.txt`, just add `-e git+https://github.com/riseml/config-parser.git@master#egg=config_parser` to `requirements.txt`
* via `setup.py`:
  * create `dependency-links.txt` in root of your python package (if not exists)
  * add `git+https://github.com/riseml/config-parser.git#egg=config_parser-0.1` to `dependency-links.txt`
  * add `config_parser` to setup's `install_requires` list
  
## Run standalone
 
```bash
riseml-config-parser [<name-of-config-here>.yml]
```

It will show parsed json dictionary if config is valid. 
In case when config is not valid, it will show description of `ConfigError` exception like this:
```
WARNING: no input config file supplied. Using file from `tests/sample_config.yml`
ConfigParseError: Usage of non-declared params: (`gamma`) in run command `python run.py -b {{beta}} -g {{gamma}}`
```