import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Matematica",
    version="0.9.2",
    author="Caio Vieira",
    author_email="caiovieiraproficional@protonmail.com",
    description="A simple, and powerful, math library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CaioVieiraF/MathLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
