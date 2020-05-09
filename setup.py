import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kanye_the_wrapper", # Replace with your own username
    version="0.0.1",
    author="AlbertUlysses",
    author_email="albertulysseschavez@gmail.com",
    description="An API wrapper for the Kanye API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlbertUlysses/Kanye_the_Wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)
