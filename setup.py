from setuptools import setup

setup(name='slash',
      version='3.0',
      description='Slash is a command line tool that scrapes the most popular e-commerce websites to get the best deals on the searched items across these websites.',
      author='Anshul, Bhavya, Darshan, Pragna, Rohan',
      author_email='rohan22shah@gmail.com',
      url='https://github.com/rohan22shah/slash-phase3.git',
      packages=['slash'],
      long_description="""\
            Hands on for the standard github repo files.
            .gitignore
            .travis.yml
            CITATION.md : fill on once you've got your ZENODO DOI going
            CODE-OF-CONDUCT.md
            CONTRIBUTING.md
            LICENSE.md
            README.md
            setup.py
            requirements.txt
            test/
              README.md
            src/
              __init__.py
        """,
      classifiers=[
            "License :: MIT License",
            "Programming Language :: Python",
            "Development Status :: Initial",
            "Intended Audience :: Developers",
            "Topic :: Software Engineering",
        ],
      keywords='python requirements license gitignore',
      license='MIT',
      install_requires=[
            'BeautifulSoup',
            'pytest',
            'uvicorn',
            'streamlit',
            'webdriver_manager',
            'pyshorteners',
            'link-button',
            'ebaysdk',
            'requests',
            'pandas'
        ],
     )