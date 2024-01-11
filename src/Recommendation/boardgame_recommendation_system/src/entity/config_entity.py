from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen=True)
class DataDeployConfig():
    root_dir: Path
    weight_ratings_hb_file: Path
    bg_info :Path
    data_cb: Path
    similarity_cb: Path
    model_cfb: Path
    bg_pivot_cfb: Path
    dir_deploy: Path
    zip_dir: Path
    file_zip: Path
    all_file_cfb: Path
    all_file_cb: Path
