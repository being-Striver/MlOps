from setuptools import find_packages, setup
from typing import List 

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath:str)-> List[str]:
    ''' 
     This function will return the list of requirements.
    '''
    requirements=[]
    with open(filepath, 'r') as file:
        requirement=file.readlines()
        requirements=[req.replace("\n", "") for req in requirement]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="ml-project",
    version='0.0.1',
    author='Sudhanshu',
    author_email="shudhanshubhagat@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')

)