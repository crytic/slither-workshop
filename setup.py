from setuptools import setup, find_packages

setup(
    name="slither-secureum",
    description="Slither detectors written for secureum.",
    url="https://github.com/crytic/slither-secureum",
    author="Trail of Bits",
    version="0.01",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["slither-analyzer>=0.10.2"],
    entry_points={
        "slither_analyzer.plugin": "slither secureum=detectors:make_plugin",
    },
    extras_require={
        "dev": ["black==22.3.0", "pylint==2.13.4", "mypy==0.942"],
    },
)