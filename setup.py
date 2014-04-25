from distutils.core import setup

setup(name='adyen',
      version='0.0.1',
      description='Python library for the Adyen payment provider',
      license="MIT",
      author='Markus Bertheau',
      author_emai='mbertheau@gmail.com',
      long_description=open('README.md').read(),
      packages=['adyen', 'django_adyen', 'oscar_adyen'],
      install_requires=['pytz', 'zope.dottedname'])