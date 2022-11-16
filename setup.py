from setuptools import setup

requirements = ['numpy', 'pandas']

setup(
    name='comp_validator',
    version='0.1.0',
    description='BIDS-validator for computational data (simulations).',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Dinara Issagaliyeva',
    author_email='dinarissaa@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    install_requires=requirements,
    license="MIT license",
    keywords=['BIDS', 'validator', 'computational data'],
    packages=['comp_validator', 'comp_validator.issues', 'comp_validator.check'],
    url='https://github.com/dissagaliyeva/comp_bids'
)
