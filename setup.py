from distutils.core import setup

setup(
    name='Django-Bootstrap3-Validator',
    version='0.2.0',
    author='Xu Yuan',
    author_email='ankh2008@gmail.com',
    packages=['bootstrap_validator', 'bootstrap_validator.templatetags', 'demo', 'demo.demo'],

    license='LICENSE.txt',
    description='BootstrapValidator support for Django projects',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.0",
    ],
)