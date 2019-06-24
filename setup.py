import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NZ_Business_Number_Validator",
    version="1.0.0",
    author="Daniel Cerezo Rodriguez",
    author_email="danielcerezo.dev@gmail.com",
    description="A validator python package for New Zealand Business Numbers (NZBN)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielcerezodev/NZ_Business_Number_Validator.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
)
