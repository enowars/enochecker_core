# enochecker_core [![PyPI version](https://badge.fury.io/py/enochecker-core.svg)](https://pypi.org/project/enochecker-core) [![Build Status](https://github.com/enowars/enochecker_core/actions/workflows/pythonapp.yml/badge.svg?branch=main)](https://github.com/enowars/enochecker_core/actions/workflows/pythonapp.yml) ![Lines of code](https://tokei.rs/b1/github/enowars/enochecker_core)

This package provides dataclasses and enums adhering to the [specification](https://github.com/enowars/specification).

Since the specification defines keys in camel case, whereas this package follows python naming convention and has keys in snake case, the keys need to be transformed when sending/receiving them over the wire. The recommended way is to use the `jsons` (not `json`) package.

Example:
```
>>> from enochecker_core import CheckerTaskResult, CheckerResultMessage
>>> import jsons
>>> jsons.dumps(CheckerResultMessage(result=CheckerTaskResult.OK, message="some message"), use_enum_name=False, key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE)
'{"message": "some message", "result": "OK"}'
>>> jsons.loads('{"message": "some message", "result": "OK"}', CheckerResultMessage, key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE, strict=True)
CheckerResultMessage(result=<CheckerTaskResult.OK: 'OK'>, message='some message')
```