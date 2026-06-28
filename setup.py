from setuptools import setup, find_packages

setup(
    name="genai-mcq",
    version="0.1.0",
    author="MD Irfan",
    author_email="irfan02md@gmail.com",
    description="A Python package for generating multiple-choice questions using AI.",
    packages=find_packages(),
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2"
    ]
)