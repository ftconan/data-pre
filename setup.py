"""
@author: magician
@file: pd_pickle.py
@date: 2019/06/21
"""
from setuptools import setup, find_packages

setup(
    name="pd-data-pre",
    version="0.1.0",
    keywords=("pip", "pd-data-pre", "excel", "csv", "json", "pickle"),
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

    url="https://github.com/ftconan/pd-data-pre.git",
    author="magician",
    author_email="ftconan@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        'alabaster',
        'Babel',
        'certifi',
        'chardet',
        'commonmark',
        'docutils',
        'future',
        'idna',
        'imagesize',
        'Jinja2',
        'MarkupSafe',
        'numpy',
        'packaging',
        'pandas',
        'pkg-resources',
        'Pygments',
        'pyparsing==2.4.0',
        'python-dateutil',
        'pytz',
        'recommonmark',
        'request',
        'six',
        'snowballstemmer',
        'Sphinx',
        'sphinxcontrib-applehelp',
        'sphinxcontrib-devhelp',
        'sphinxcontrib-htmlhelp',
        'sphinxcontrib-jsmath',
        'sphinxcontrib-qthelp',
        'sphinxcontrib-serializinghtml',
        'urllib3',
    ]
)
