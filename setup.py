import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line for line in fh.read().splitlines() if len(line.strip()) > 0]

setuptools.setup(
    name="tussik-zpl",
    version="0.1.0.0",
    install_requires=requirements,
    author="Darren Martz",
    author_email="darren@tussik.com",
    description="Tussik ZPL Writer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tussikcom/tussik-zpl",
    project_urls={
        "Source Code": "https://github.com/tussikcom/tussik-zpl/",
        "Bug Tracker": "https://github.com/tussikcom/tussik-zpl/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Topic :: Internet",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9, <4",
    keywords="zpl, zpl2, python",
    include_package_data=True,
    tests_require=[
        "pytest",
    ],
    extras_require={
        'images': ["pillow"]
    }
)
