from setuptools import setup, find_packages

# Đọc các phụ thuộc từ tệp requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='telefinbot',
    version='0.1.0',
    author='nxtung',
    author_email='tungatinternet@gmail.com',
    description='A bot for handling telefin operations',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)