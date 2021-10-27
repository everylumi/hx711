from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='hx711',
    packages=['hx711'],
    version='1.0.0',
    description='hx711 chip interface library',
    author_email="everylumi@gmail.com",
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: BSD 3-Clause",
    "Operating System :: OS Independent",
    ],
    keywords='hx711 raspberry',
    url="https://github.com/everylumi/hx711",
    python_requires='>=3',
    zip_safe=False,
    long_description=readme()
)
