from setuptools import find_packages, setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='hx711',
    packages=['.'],
    version='1.0.0',
    description='hx711 chip interface library',
    author_email="everylumi@gmail.com",
    url="https://github.com/everylumi/hx711",
    python_requires='>=3',
    zip_safe=False,
    long_description=readme()
)
