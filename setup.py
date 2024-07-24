from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='sooraj',
    author_email='soorajwizard01@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2", "langchain-openai"],
    packages=find_packages(),
)
