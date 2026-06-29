
from setuptools import find_packages,setup
from typing import List

def getrequirements(filepath:str)->List[str]:
    """
    This function will return the list of requirements
    """
    with open(filepath) as f:
        requirements=f.readlines()

        requirements=[req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author="Vrashbh",
    author_email="sonivrashbh@gmail.com",
    packages=find_packages(),
    install_requires=getrequirements("requirements.txt")
)