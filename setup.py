from setuptools import find_packages,setup
from typing import List

hyp_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
      """This function will return list of requirments"""

      requirments=[]
      with open('requirments.txt') as file_obj:
            requirments = file_obj.readlines()
            requirments=[req.replace("\n","") for req in requirments]
            if hyp_e_dot in requirments:
                requirments.remove(hyp_e_dot)
                  
     
setup(
    name = 'MlProject',
    version='0.0.1',
    author = 'Preeti',
    author_email='b21313@students.iitmandi.ac.in',
    packages = find_packages(),
    install_requires = get_requirements('requirments.txt')

)