import os
import setuptools

NAME = "tomlconfig"

DEPENDENCIES_ARTIFACTORY = [
    'toml'
]

DEPENDENCIES_GITHUB = {
}


def generate_pip_links_from_url(url, version):
    """ Generate pip compatible links from Socialcoding clone URLs

    Arguments:
        url {str} -- Clone URL from Socialcoding
    """
    package = url.split('/')[-1].split('.')[0]
    url = url.replace("https://", f"{package} @ git+https://")
    url = url + f"@{version}"

    return url

# create pip compatible links
DEPENDENCIES_GITHUB = [generate_pip_links_from_url(url, version) for url, version in DEPENDENCIES_GITHUB.items()]
DEPENDENCIES = DEPENDENCIES_ARTIFACTORY + DEPENDENCIES_GITHUB

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name=NAME,
    version_format='{tag}.dev{commitcount}+{gitsha}',
    author="srw2ho",
    author_email="",
    description="",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    package_data={},
    install_requires=DEPENDENCIES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License"
        "Operating System :: OS Independent",
    ],
)
