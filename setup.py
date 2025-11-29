# from setuptools import setup, find_packages

# setup(
#     name="pyfilemetre",
#     version="0.1.2",
#     author="Aditi Gupta",
#     author_email="aditig135@gmail.com",
#     description="A simple AST-based Python code analyzer with CLI support",
#     long_description=open("README.md", encoding="utf-8").read(),
#     long_description_content_type="text/markdown",
#     packages=find_packages(),
#     include_package_data=True,
#     python_requires=">=3.8",
#     install_requires=["tabulate>=0.9.0"],
#     entry_points={
#         "console_scripts": [
#             "pyfilemetre=pyfilemetre.cli:main",
#         ],
#     },
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#         "Development Status :: 4 - Beta",
#         "Intended Audience :: Developers"
#     ],
#     license="MIT",
# )

from setuptools import setup, find_packages
from pathlib import Path

# Read the long description safely
this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="pyfilemetre",
    version="0.1.4",  
    author="Aditi Gupta",
    author_email="aditig135@gmail.com",
    description="A simple AST-based Python code analyzer with CLI support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["tabulate>=0.9.0"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "pyfilemetre=pyfilemetre.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ],
    license="MIT",
)