from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in haulage_management/__init__.py
from haulage_management import __version__ as version

setup(
	name="haulage_management",
	version=version,
	description="simple app to manage movement of goods from port to client address",
	author="Jide Olayinka",
	author_email="olajamesjide@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
