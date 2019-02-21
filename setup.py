import setuptools


with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py3_quartus",
    version="0.0.2",
    author="Akash Gutha",
    author_email="gutha.3@buckeyemail.osu.edu",
    description="Python 3 interface for quartus tcl programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AkashGutha/py3_quartus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
)
