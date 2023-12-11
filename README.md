# TempusLabra
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)

Measure elapsed time in Python functions in a human-readable way.

---

## Quickstart
### Installation

To add _tempuslabra_ to your project, run one of the following commands:

```shell
# Install with poetry and HTTPS
poetry add git+https://github.com/rogelhojunior/tempuslabra.git

# Install with poetry and SSH
poetry add git+ssh://git@github.com:rogelhojunior/tempuslabra.git

# Install with pip and HTTPS
pip install git+https://github.com/rogelhojunior/tempuslabra.git

# Install with pip and SSH
poetry add git+ssh://git@github.com:rogelhojunior/tempuslabra.git
```

> **Warning**: When using pip to install _tempuslabra_, we highly recommend install it within the virtual environment of your project.

### Usage

To measure elapsed time of your function:

```python
from tempuslabra import timeit

@timeit
def any_function():
  return 'Dummy Return'

# Output: any_function took 15 seconds to run.
```
