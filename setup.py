import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intake-custom-drivers",
    version="0.0.1",
    author="MH Data",
    author_email="author@example.com",
    description="Custom drivers for intake",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mh-data-science/intake-custom-drivers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)