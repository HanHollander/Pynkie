# Pynkie
Pygame extension

## Type stub generation

Dependencies
```bash
pip3 install mypy
```

Generate type stubs
```bash
stubgen src/pynkie -o stubs
```
Note 1: Most likely the `__init()__` methods of classes annotated with `@dataclass` has to be manually deleted in the generated .pyi files
Notd 2: the `__init__.py` file should be manually copied to `__init__.pyi` for typing (mypy, pyright etc.) to work

## Build

Dependencies:
```bash
pip3 install build
```

Building:
```bash
python3 -m build --wheel
```

## Install

```bash
pip3 install <path to wheel> [--force-reinstall]
```