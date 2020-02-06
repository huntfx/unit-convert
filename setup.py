import os
from setuptools import setup, find_packages


# Get the README.md text
with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
    readme = f.read()

# Parse unit_convert.py for a version
with open(os.path.join(os.path.dirname(__file__), 'unit_convert.py'), 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = eval(line.split('=')[1].strip())
            break
    else:
        raise RuntimeError('no version found')

setup(
    name = 'unit-convert',
    packages = find_packages(),
    version = version,
    license='MIT',
    description = 'Easy way of converting units.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author = 'Peter Hunt',
    author_email='peterh@blue-zoo.co.uk',
    py_modules=['unit_convert'],
    url = 'https://github.com/Peter92/unit-convert',
    download_url = 'https://github.com/Peter92/unit-convert/archive/{}.tar.gz'.format(version),
    project_urls={
        #'Documentation': 'https://github.com/Peter92/unit-convert/wiki',
        'Source': 'https://github.com/Peter92/unit-convert',
        'Issues': 'https://github.com/Peter92/unit-convert/issues',
    },
    keywords = ['unit', 'convert', 'conversion'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires=('>=2.5')
)
