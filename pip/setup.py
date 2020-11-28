import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="namemcpy",
    version="1.3.1",
    license="MIT",
    author="Luke Lass",
    author_email="ants.uk.us@gmail.com",
    description="Api Wrapper for namemc",
    long_description="Api Wrapper for https://namemc.com. This moudule is to make it easier to use namemcs api.",
    long_description_content_type="text/markdown",
    url="https://github.com/lasscat/namemcpy",
    packages=setuptools.find_packages(),
    install_requires = ["requests", "bs4"],
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
