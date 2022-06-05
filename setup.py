from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
            name = "Stat",
            version = "1.0.0",
            description = "A python module for statistics",
            long_description = long_description, 
            long_description_content_type = "text/markdown",
            author = "Promise Okoli",
            license = "MIT",
            classifiers = [
                    "Development Status :: 4 - Beta",
                    "Intended Audience :: Developers",
                    "License :: OSI Approved :: MIT License"
            ],
            keywords = "Statistics and computation",
            author_email = "okoli4promise@gmail.com",
            url = "https://www.github.com/Premerie/Stat",
            packages = find_packages(),
            python_requires = "~=3.5",
            install_requires = [],
            py_modules=['Stat.Stat'],
            entry_points = {
                            "console_scripts": [
                                            "Spat-cli = Spat.Spat",
                            ],
            }
)