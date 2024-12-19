from setuptools import setup, find_packages

setup(
    name="Octopus",
    version="0.1.0",
    packages=find_packages(),
    description="An optimized hierarchical data structure for fast lookups and problem-solving.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Likith S G",
    author_email="likithsg1@gmail.com",
    url="https://github.com/likith-sg/Octopus",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
  
