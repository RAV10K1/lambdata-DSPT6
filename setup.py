import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-dspt6_rkt",
    version="0.0.3",
    author="Ravi Tennekone",
    author_email="ravindra-tennekone@lambdastudents.com",
    description="Simple test functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RAV10K1/lambdata-DSPT6",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)