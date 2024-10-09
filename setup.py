from setuptools import setup, find_packages

setup(
    name="cloudmesh",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add dependencies here
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
        ],
    },
    entry_points={
        "console_scripts": [
            "cloudmesh=cloudmesh.cli:main",
        ],
    },
)
