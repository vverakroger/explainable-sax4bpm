from setuptools import setup, find_packages


with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    "graphviz>=0.20.3",
    "lingam>=1.9.0",
    "networkx>=3.2.1",
    "numpy>=1.26.4",
    "pandas>=2.2.2",
    "pm4py>=2.7.11.12",
    "scikit-learn>=1.5.1",
    "scipy>=1.11.4",
]

setup(
    name="sax4bpm", 
    version='{{VERSION_PLACEHOLDER}}', 
    author="Inna Skarbovsky",
    author_email="inna@il.ibm.com",
    description="Open source Python library for deriving explanations about business processes based on process,causal and XAI perspectives",
    long_description=long_description,
    license='GPL 3.0',
    long_description_content_type="text/markdown",
    url="https://github.com/IBM/sax4bpm",
    packages=find_packages(include=['sax', 'sax.*']),    
    python_requires='>=3.9',
    install_requires=install_requires,
    include_package_data=True,
)
