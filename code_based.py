import os
from pathlib import Path
import logging

# logging string
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name = "Boardgame_Recommendation_System"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/src/__init__.py",
    f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/src/components/__init__.py",
    f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/src/constants/__init__.py",
    f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/src/entity/__init__.py",
    f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/src/pipeline/__init__.py",
    f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/src/utils/__init__.py",
    f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/config/config.yaml",
    f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/main.py",
    f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/params.yaml",

    f"src/Content_Based_RS/{project_name.lower()}/src/__init__.py",
    f"src/Content_Based_RS/{project_name.lower()}/src/components/__init__.py",
    f"src/Content_Based_RS/{project_name.lower()}/src/constants/__init__.py",
    f"src/Content_Based_RS/{project_name.lower()}/src/entity/__init__.py",
    f"src/Content_Based_RS/{project_name.lower()}/src/pipeline/__init__.py",
    f"src/Content_Based_RS/{project_name.lower()}/src/utils/__init__.py",
    f"src/Content_Based_RS/{project_name.lower()}/config/config.yaml",
    f"src/Content_Based_RS/{project_name.lower()}/main.py",
    f"src/Content_Based_RS/{project_name.lower()}/params.yaml",

    f"src/Hybrid_RS/{project_name.lower()}/src/__init__.py",
    f"src/Hybrid_RS/{project_name.lower()}/src/components/__init__.py",
    f"src/Hybrid_RS/{project_name.lower()}/src/constants/__init__.py",
    f"src/Hybrid_RS/{project_name.lower()}/src/entity/__init__.py",
    f"src/Hybrid_RS/{project_name.lower()}/src/pipeline/__init__.py",
    f"src/Hybrid_RS/{project_name.lower()}/src/utils/__init__.py",
    f"src/Hybrid_RS/{project_name.lower()}/config/config.yaml",
    f"src/Hybrid_RS/{project_name.lower()}/main.py",
    f"src/Hybrid_RS/{project_name.lower()}/params.yaml",

    # f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/src/data_preparing.py",
    # f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/src/data_processing.py",
    # f"src/Collaborative_Filtering_Based_RS/{project_name.lower()}/src/modeling.py",
    # f"src/Content_Based_RS/{project_name.lower()}/src/__init__.py",
    # f"src/Content_Based_RS/{project_name.lower()}/src/data_preparing.py",
    # f"src/Content_Based_RS/{project_name.lower()}/src/data_processing.py",
    # f"src/Content_Based_RS/{project_name.lower()}/src/modeling.py",
    # f"src/Hybrid_RS/{project_name.lower()}/src/__init__.py",
    # f"src/Hybrid_RS/{project_name.lower()}/src/data_preparing.py",
    # f"src/Hybrid_RS/{project_name.lower()}/src/data_processing.py",
    # f"src/Hybrid_RS/{project_name.lower()}/src/modeling.py",
    "requirements.txt",
    "setup.py",
    "Test/test.ipynb",
    "README.md",
    "Dockerfile",
    "docker-compose.yaml",
    "Makefile", 
    ".gitignore",
    "app.py",

]
def Create__Or_Check_File(list_of_files):
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
        if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass
                logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"{filename} is already exists..")

if __name__ == "__main__":
    Create__Or_Check_File(list_of_files)