from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name="flowity",
    version="0.0.1",
    description="Workflow language designed for LLM.",
    long_description=open("README.md", "rt", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RockChinQ/Flowity",
    project_urls={
        "Bug Report": "https://github.com/RockChinQ/Flowity/issues"
    },
    author="RockChinQ",
    author_email="junyan_qin@qq.com",
    # license="GNU Affero General Public License v3.0",
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    py_modules=["flowity"],
    package_data={"": ["*.json"]},
    install_requires=[
        "langchain",
        "langchain-openai",
        "pydantic",
        "ply",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
)