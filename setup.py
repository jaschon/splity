import setuptools

setuptools.setup(
    name='split',
    version='.1',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)