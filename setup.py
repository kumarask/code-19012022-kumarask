from importlib.metadata import entry_points
import setuptools

with open("README.md", "r", encoding="utf-8") as _file:
    descriptions = _file.read()

setuptools.setup(
    name="codeTest",
    version="0.0.1",
    author="Kumara Krishnappa",
    description="A sample example package",
    long_description=descriptions,
    long_description_content_type="text/markdown",
    url="https://github.com/kumarask/code-19012022-kumarask",
    classifiers=[
        "Programming Launguage :: Python :: 3",
    ],
    packages=["codeTest", "codeTest/core", "codeTest/utilities"],
    package_data={"resources": ["*.db", "*.json"], "data": ["*.db", "*.json"]},
    python_requires=">=3.8",
)