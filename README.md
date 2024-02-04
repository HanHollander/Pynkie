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
Note: some manual tweaks may be needed


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