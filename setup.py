import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='sphinx-ext-eqt',
    version='1.3',
    author='Naeka',
    author_email='contact@naeka.fr',
    description="A sphinx extension to integrate multiple choices "
                "questionnaires",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/naeka/sphinx-ext-eqt',
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=[
        ('_static', [
            'eqt_ext/_static/css/eqt.css',
            'eqt_ext/_static/js/eqt.js',
        ])
    ],
    classifiers=(
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Topic :: Utilities',
    ),
)
