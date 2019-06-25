#!/usr/bin/env bash

python setup.py bdist_egg
python setup.py sdist
twine upload dist/*
