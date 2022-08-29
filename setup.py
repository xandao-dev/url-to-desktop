from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="url-to-desktop",
    version="1.0.0",
    install_requires=["pyfiglet>=0.8",
                      "fire>=0.2.1"],
    packages=find_packages(),
    description="Converts .url files to .desktop files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alexandre Calil Martins Fonseca",
    author_email="alexandrecalilmf@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    url="https://github.com/xandao6/url-to-desktop",
    download_url="https://pypi.org/project/url-to-desktop/",
    keywords=[
        "url",
        "link",
        "convert",
        "url convert",
        "desktop conversor",
        "url linux"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["url-to-desktop = scripts.conversor:main"]},
)
