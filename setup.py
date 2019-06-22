"""
@author: magician
@file: pd_pickle.py
@date: 2019/06/21
"""
from setuptools import setup, find_packages

setup(
    name="data_pre",
    version="0.1.0",
    keywords=("pip", "data_pre", "excel", "csv", "json", "pickle"),
    description="pandas data preprocessing tool",
    long_description="Use pandas to preprocess data tool. "
                     "support excel, csv, json, pickle different IO format data read and write; "
                     "DataFrame preview function; "
                     "DataFrame delete data; "
                     "DataFrame select data; "
                     "DataFrame add style; "
                     "DataFrame data preprocessing; "
                     "DataFrame data statistics ;"
                     "DataFrame add subtotal, total; "
                     "DataFrame pivot table"
                     "...",
    license="Apache Licence",

    url="https://github.com/ftconan/data-pre.git",
    author="magician",
    author_email="ftconan@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        'numpy',
        'pandas',
        'pkg-resources',
        'python-dateutil',
        'pytz',
        'six'
    ]
)
