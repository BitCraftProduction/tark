from setuptools import setup, find_packages

setup(
    name='tark',
    version='0.1.0',
    description='Tark - A Hindi Programming Language',
    author='Bitcraft Production',
    author_email='contact@bitcraftproduction.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tark = tark.__main__:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
