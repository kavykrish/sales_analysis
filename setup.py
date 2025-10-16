from setuptools import setup, find_packages

setup(
    name="sales_analysis",
    version="1.0.0",
    author="Krishna Veni S",
    author_email="krish1822003@gmail.com",
    description="A Python package for analyzing and visualizing sales data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kavykrish/sales_analysis.git",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "scikit-learn>=1.3.0"
    ]
)
