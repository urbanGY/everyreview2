from setuptools import setup, find_packages

setup(
    name                = 'everyreview2',
    version             = '0.1',
    description         = 'everyreview2',
    author              = 'urbanGY',
    author_email        = 'sfsfkj@gmail.com',
    url                 = 'https://github.com/urbanGY/everyreview2',    
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['everyreview2'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
