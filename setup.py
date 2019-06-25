"""
@author: magician
@file: pd_pickle.py
@date: 2019/06/21
"""
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data-pre",
    version="0.1.0",
    author="magician",
    author_email="ftconan@163.com",
    description="pandas data preprocessing tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ftconan/data_pre.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Licence",
        "Operating System :: OS Independent",
    ],
)
