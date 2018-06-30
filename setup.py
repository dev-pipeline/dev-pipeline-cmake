#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name="dev-pipeline-cmake",
    version="0.2.0",
    package_dir={
        "": "lib"
    },
    packages=['devpipeline_plugins.cmake'],

    install_requires=[
        'dev-pipeline >= 0.2.0'
    ],

    author="Stephen Newell",
    description="cmake plugin for dev-pipeline",
    license="BSD-2",
    url="https://github.com/dev-pipeline/dev-pipeline-cmake",
)
