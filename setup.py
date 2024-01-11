from setuptools import setup

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

NAME_REPO = "BOARDGAME_RECOMMENDATION_SYSTEM"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["Flask"]
__version__ = "1.0"
AUTHOR_USER_NAME = "tph-kd"
AUTHOR_EMAIL = "tranphihung8383@gmail.com"

setup(
    name= NAME_REPO,
    version= __version__,
    long_description= long_description,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "Build a Boardgame Recommendation System and deploy into the realtime life.",
    long_description_content_type = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{NAME_REPO}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{NAME_REPO}/issues"
    },
    packages= setuptools.find_packages(where=f"{SRC_REPO}"),
    package_dir={"" : f"{SRC_REPO}"},
    python_requires = '>=3.7' ,
    install_requires = LIST_OF_REQUIREMENTS,

)