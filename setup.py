from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ligdicash',
    version='1.0.2',
    packages=find_packages(),
    install_requires=['requests'],
    author='LigdiCash',
    author_email='info@ligdicash.com',
    description='Une bibliothèque Python pour manipuler l\'API de Ligdicash.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://developers.ligdicash.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11.7',
    readme = "README.md"
)