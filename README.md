### Hexlet tests and linter status:
[![Actions Status](https://github.com/AndyRiddle/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/AndyRiddle/python-project-lvl2/actions)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Github Actions Status](https://github.com/AndyRiddle/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/AndyRiddle/python-project-lvl2/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a6207f0f2cce4d4cbb53/test_coverage)](https://codeclimate.com/github/AndyRiddle/python-project-lvl2/test_coverage)

## Description
Package compares two configuration files in JSON or YAML format.

## Installation
Clone the repository:
```bash
git clone git@github.com:AndyRiddle/python-project-lvl2.git
```
Run from the root directory of the project commands:
```bash
make build
make publish
make package-install
```

## Option
- `--help (-h)` : Display help information.
- `--format (-f)` : Format of output (default=`stylish`, other supported formats: `plain`, `json`).

#### Example usage `--help`:
[![asciicast](https://asciinema.org/a/tkLvXcsgJRQZlP3L8BvKeiugF.png)](https://asciinema.org/a/tkLvXcsgJRQZlP3L8BvKeiugF?autoplay=1)

## Usage
#### Example run `gendiff` for JSON files wiht output in `stylish` format:
[![asciicast](https://asciinema.org/a/9Dz0HwPSEdovpE7fRTR3DB1zu.png)](https://asciinema.org/a/9Dz0HwPSEdovpE7fRTR3DB1zu?autoplay=1)
#### Example run `gendiff` for YAML files wiht output in `plain` format:
[![asciicast](https://asciinema.org/a/KuHoou8bCyDUktqemXNwUIvTq.png)](https://asciinema.org/a/KuHoou8bCyDUktqemXNwUIvTq?autoplay=1)
#### Example run `gendiff` for JSON files wiht output in `json` format:
[![asciicast](https://asciinema.org/a/f7Wap5AGJ1dETfHeKQUbdsOH1.png)](https://asciinema.org/a/f7Wap5AGJ1dETfHeKQUbdsOH1?autoplay=1)

