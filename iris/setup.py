import setuptools

setuptools.setup(
    name="iris",
    packages=setuptools.find_packages(exclude=["iris_tests"]),
    install_requires=[
        "dagster==0.12.7",
        "dagit==0.12.7",
        "pytest",
    ],
)
