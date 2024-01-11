from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig():
    root_dir: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataPreparingConfig():
    root_dir: Path
    boardgame_data_file: Path
    ratings_data_file: Path

@dataclass(frozen=True)
class DataProcessingConfig():
    root_dir: Path
    knowledge_data_cb_preparing_file: Path
    pickle_dir: Path

@dataclass(frozen=True)
class ModelConfig():
    root_dir: Path
    knowledge_stems_cb: Path
    pickle_dir: Path
    

@dataclass(frozen=True)
class ModelParams():
    K : int
    BOARDGAME_NAME : str
    MAX_FEATURES : int
    STOP_WORDS: str