# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='HarassmentClassifier',
    version='0.0.1',
    author='Faisal Alshargi',
    author_email='alshargi@hotmail.de',
    description='Arabic Harassment classifier',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alshargi/HarassmentClassifier.git',
    project_urls = {
        "Bug Tracker": "https://github.com/alshargi/HarassmentClassifier.git/issues"
    },
    license='MIT',
    packages=['HarassmentClassifier'],
    package_data={'HarassmentClassifier': ['haras/*.sav']}, 
    install_requires=['requests'],
)