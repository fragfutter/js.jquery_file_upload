from setuptools import setup, find_packages

version = '2013.01.17'

setup(name='js.jquery_file_upload',
      version=version,
      description="jquery file upload",
      long_description="""\
""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Christoph Handel',
      author_email='',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['setuptools-git'],
      install_requires=[
          'fanstatic',
          'setuptools',
          # TODO add dependency on js.jqueryui once it packs something >= 1.9
          'js.jquery',
          'js.jquery_iframe_transport',
      ],
      entry_points={
          'fanstatic.libraries': ['jquery_file_upload = js.jquery_file_upload:library', ],
      }
      )
