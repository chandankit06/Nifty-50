from setuptools import setup, find_packages

file_path='requirements.txt'
DOT_E='-e .'

def get_packages(file_path):
    packages_list=[]
    with open(file_path,'r') as fd:
        file_packages= fd.readlines()
        
        for package in file_packages:
            if DOT_E != package.strip():
                packages_list.append(package.strip())
    return packages_list
setup(
    name="NIFTY-50",
    author="ankit_chand",
    author_email="chandankit88@gmail.com",
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_packages(file_path)
    
)

print( get_packages(file_path))