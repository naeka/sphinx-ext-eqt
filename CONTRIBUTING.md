## Instructions for building the package:

#### 1. Generate distribution archives

Make sure you have the latest versions of setuptools and wheel installed:

`python3 -m pip install --user --upgrade setuptools wheel`

Now run this command from the same directory where setup.py is located:

`python3 setup.py sdist bdist_wheel`


#### 2. Upload the distribution archives

You must be registered on pypi to upload archives.

Once registered, you can use twine to upload the distribution packages. You’ll need to install Twine:

`python3 -m pip install --user --upgrade twine`

Once installed, run Twine to upload all of the archives under `dist`:

`twine upload dist/*`
