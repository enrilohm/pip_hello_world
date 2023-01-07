from setuptools import setup, find_packages
from os import path
import re
from os import listdir
from os.path import isfile, join

description="pip_hello_world package"
here = path.abspath(path.dirname(__file__))
scripts_dir= join(here,"scripts")
scriptfiles = [join("scripts",f) for f in listdir(scripts_dir) if isfile(join(scripts_dir, f))]

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
    scripts=scriptfiles,
    author_email='enrico.lohmann@protonmail.com',
    python_requires='>=3.7',
    install_requires=requirements,
    packages=["pip_hello_world"],
    package_data={
        package_name: [
            "data/*"
        ]
    },
)
