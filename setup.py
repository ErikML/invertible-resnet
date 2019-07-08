
from setuptools import find_packages, setup

setup(
    name='invertible_resnet',
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