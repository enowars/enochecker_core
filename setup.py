import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="enochecker_core",
    version="0.7.0",
    author="Trolldemorted",
    author_email="benediktradtke@gmail.com",
    description="Base library for enochecker libs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enowars/enochecker_core",
    packages=setuptools.find_packages(),
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        # 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',

    ],
    python_requires=">=3.7",
)
