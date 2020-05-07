import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-akhildraju", # Replace with your own username
    version="3.0.0",
    author="Akhil Raju",
    author_email="alhildraju@gmail.com",
    description="A small test package",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/akhildraju/lambdata-akhildraju",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
