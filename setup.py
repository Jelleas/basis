from setuptools import setup, find_packages

setup(
    author="jelleas",
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3.7",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    description="This is Basis. A programming language implementation for Basisbook Programming",
    install_requires=["colorama==0.4.1", "antlr4-python3-runtime==4.7.2"],
    keywords=["basis", "basisboek", "basisbook"],
    name="basis",
    python_requires=">=3.5",
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": ["basis=basis.__main__:main"]
    },
    url="https://github.com/jelleas/basis",
    version="0.0.3",
    include_package_data=True,
)
