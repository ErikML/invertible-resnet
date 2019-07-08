
from setuptools import find_packages, setup

setup(
    name='invertable_resnets',
    packages=find_packages(),
    install_requires=[
        'certifi',
        'chardet',
        'idna',
        'joblib',
        'numpy',
        'Pillow',
        'pyzmq',
        'requests',
        'scipy',
        'six',
        'torch',
        'torchfile',
        'torchvision',
        'tornado',
        'urllib3',
        'visdom',
        'websocket-client',
    ]
)