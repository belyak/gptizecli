import setuptools
from gptizecli.version import Version


setuptools.setup(name='gptizecli',
                 version=Version('1.0.0').number,
                 description='CLI tool for prompting OpenAI ChatGPT API',
                 long_description=open('README.md').read().strip(),
                 author='Package Author',
                 author_email='you@youremail.com',
                 url='https://github.com/belyak/gptizecli',
                 py_modules=['gptizecli'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='CLI ChatGPT OpenAI',
                 classifiers=['Packages', 'Boilerplate'])
