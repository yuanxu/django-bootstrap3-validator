from distutils.core import setup
import os

base_dir = os.path.dirname(__file__)
setup(
    name='Django-Bootstrap3-Validator',
    version='0.3',
    author='Xu Yuan',
    author_email='ankh2008@gmail.com',
    packages=['bootstrap_validator', 'bootstrap_validator.templatetags','bootstrap_validator.migrations'],
    url="https://github.com/yuanxu/django-bootstrap3-validator",
    license='LICENSE.txt',
    description='BootstrapValidator support for Django projects',
    include_package_data=True,
    long_description=open(os.path.join(base_dir, 'README.md')).read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)