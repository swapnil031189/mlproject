from setuptools import find_packages,setup  # This Automatically finds out all the packages that are available in the entire ML application in the directory that we have actually created

Hypen_E_dot= '-e .'
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''This function will return a list of requirements'''
    requirements = []
    # with open ('requirements.txt')
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]

        if Hypen_E_dot in requirements:
            requirements.remove(Hypen_E_dot)
    return requirements

# Metadata Information about entire project
setup(
    name='mlproject',
    version='0.0.1',
    author='Swapnil Amale',
    author_email='ssamale.electrical@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires = get_requirements('requirements.txt')
)