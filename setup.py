from setuptools import setup, find_packages

setup(
    name="swahili2words",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "swahili2words=swahili2words.cli:main",
        ],
    },
    author="Your Name",
    description="Convert numbers into Swahili words (supports currency and decimals)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
