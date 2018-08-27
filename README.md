# sphinx-ext-eqt

This is a sphinx extension to integrate multiple choices questionnaires


## Installation

This module is registered on pypi, simply run `pip install sphinx-ext-eqt` or add `sphinx-ext-eqt` to your requirements file.


## Configuration

Static files are not handled by extensions, to properly display the questionnaire, the module's *static dir* must be append to sphinx configuation:

```
from eqt_ext import get_eqt_ext_static_dir
html_static_path = ['<your_project_static_dir>', get_eqt_ext_static_dir()]
```
