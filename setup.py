from distutils.core import setup
setup(
  name = 'beautify',
  packages = ['beautify'], # this must be the same as the name above
  version = '0.1.3',
  install_requires=[
        "requests",
    ],
  description = 'Simplifies the process of formatting and printing beautiful and responsive output in terminals',
  author = 'Adivandhya B R',
  author_email = 'adivandhya@yahoo.co.in',
  url = 'https://github.com/adivandhya/beautify', # use the URL to the github repo
  download_url = 'https://github.com/adivandhya/beautify/tarball/0.1', # I'll explain this in a second
  keywords = ['terminal', 'console', 'output','beautify','simplify','colorma'], # arbitrary keywords
  classifiers = [],
)