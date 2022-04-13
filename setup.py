import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pydantic_errors_messages_translations",
    version="1.0.0",
    description="It's a collection of translations for pydantic errors in any languages",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/fabriciomsdev/pydantic-errors-messages-translation",
    author="Fabricio Magalhães Sena",
    author_email="fabricioms.dev@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pydantic_errors_messages_translations"],
    include_package_data=True,
    install_requires=["pydantic", "pydantic-i18n"],
)