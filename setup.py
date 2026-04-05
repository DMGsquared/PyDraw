from setuptools import setup, find_packages

with open("Readme.md", "r") as f:
    description = f.read()
setup(
    name='pydrawgen',
    version='0.1.0',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'numpy>=2.0.2',
        'opencv-python>=4.0.1',
        'matplotlib>=3.10.8'
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)