from setuptools import find_packages, setup

setup(
    name = "UKGE-PSL",
    version = "0.1.0",
    author = "Mou YongLi, Qihui Feng, Er Jin, Gerhard Lakemeyer, Stefan Decker",
    author_email = "mou@dbis.rwth-aachen.de",
    description = ("Enhancing Uncertain Knowledge Graphs Embedding using Probabilistic Soft Logic"),
    license = "MIT",
    url = "https://github.com/MouYongli/UKGE-PSL",
    package_dir={"": "src"},
    packages=find_packages("src"),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic ::Enhancing Uncertain Knowledge Graphs Embedding using Probabilistic Soft Logic",
        "License :: OSI Approved :: MIT License",
    ],
)