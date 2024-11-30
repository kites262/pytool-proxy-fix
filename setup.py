from setuptools import setup, find_packages

setup(
    name="pytool-proxy-fix",
    version="0.1.2",
    description="Fix urllib for python 3.7/3.8",
    long_description=open("README.MD").read(),
    long_description_content_type="text/markdown",
    author="kites262",
    author_email="kites262@github.com",
    url="https://github.com/kites262/tool-fix-urllib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7, <3.9",
    entry_points={
        "console_scripts": [
            "pytool-proxy-fix=pytool_proxy_fix.main:main_fix_urllib",
        ],
    },
    license="MIT",
)
