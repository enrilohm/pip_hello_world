from setuptools import setup, find_packages
from os import path
import re

description="pip_hello_world package"

here = path.abspath(path.dirname(__file__))
# package_name = re.sub(r".*/", "", here)
package_name = "pip_hello_world"


with open(path.join(here, "requirements.txt"),"r") as f:
    requirements=f.read().splitlines()

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=package_name,
    version='0.1.0',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/enrilohm/{package_name}",
    author='Enrico Lohmann',
    scripts=["scripts/pip_hello_world"],
    author_email='enrilohm@gmail.com',
    python_requires='>=3.7',
    install_requires=requirements,
    packages=["pip_hello_world"],
)
