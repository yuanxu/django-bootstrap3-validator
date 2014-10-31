from distutils.core import setup
import os

base_dir = os.path.dirname(__file__)
setup(
    name='Django-Bootstrap3-Validator',
    version='0.2.0',
    author='Xu Yuan',
    author_email='ankh2008@gmail.com',
    packages=['bootstrap_validator', 'bootstrap_validator.templatetags', 'demo', 'demo.demo'],
    url="https://github.com/yuanxu/django-bootstrap3-validator",
    license='LICENSE.txt',
    description='BootstrapValidator support for Django projects',
    long_description=open(os.path.join(base_dir, 'README.md')).read(),
    install_requires=[
        "Django >= 1.0",
    ],
)