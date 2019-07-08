
from setuptools import find_packages, setup

setup(
    name='invertable_resnets',
    packages=find_packages(),
    install_requires=[
        'certifi==2019.3.9',
        'chardet==3.0.4'
        'idna==2.8',
        'joblib==0.13.2',
        'numpy==1.16.4',
        'Pillow==6.0.0',
        'pyzmq==18.0.1',
        'requests==2.22.0',
        'scipy==1.3.0',
        'six==1.12.0',
        'torch==1.1.0',
        'torchfile==0.1.0',
        'torchvision==0.3.0',
        'tornado==6.0.2',
        'urllib3==1.25.3',
        'visdom==0.1.8.8',
        'websocket-client==0.56.0',
    ]
)