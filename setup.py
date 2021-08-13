import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mpl_sizes",
    version="0.0.1",
    author="Jack Turner",
    author_email="jackwilliamturner@icloud.com",
    description="Default figure sizes for matplotlib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BayesWatch/matplotlib_size_sheets",
    project_urls={
        "Bug Tracker": "https://github.com/BayesWatch/matplotlib_size_sheets/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
