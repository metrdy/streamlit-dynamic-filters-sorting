from setuptools import setup, find_packages

VERSION = '1'
DESCRIPTION = "Dynamic multiselect filters for Streamlit sorted by frequency"

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

with open("CHANGELOG.md", "r", encoding="utf-8") as fh:
    changelog = fh.read()

setup(
    name="streamlit_dynamic_filters_sorting",
    version=VERSION,
    author="Oleksandr Arsentiev",
    author_email="<arsentiev9393@gmail.com>",
    description=DESCRIPTION,
    long_description=f"{readme}\n\n{changelog}",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['streamlit'],
    keywords=['streamlit', 'custom', 'component'],
    license="MIT",
    url="https://github.com/metrdy/streamlit-dynamic-filters-sorting.git",
)
