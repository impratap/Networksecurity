'''
setup.py is a script that uses the setuptools library 
to define metadata about our project 
(e.g., name, version, author) and its dependencies. 
It allows us to package our project as a Python module, 
which can then be installed locally or distributed via PyPI 
(Python Package Index). In a machine learning project, 
this is particularly useful for organizing code into 
a reusable library and ensuring that dependencies are installed 
consistently.



'''

from setuptools import find_packages, setup
from typing import List


def get_requirements()->List[str]:
    '''
    this function will return list of requirements
    '''

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read line from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")


    return requirement_lst

print(get_requirements())


setup(
    name="Networksecurity",
    version="0.0.1",
    author="Ankit Singh",
    author_email="ankitpratapsingh333@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)