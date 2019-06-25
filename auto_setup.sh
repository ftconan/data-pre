#!/usr/bin/env bash

sudo rm -rf dist
sudo rm -rf build
python setup.py bdist_egg
python setup.py sdist
twine upload dist/*
