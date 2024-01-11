import os
from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import (DataIngestionConfig, DataPreparingConfig, DataProcessingConfig, ModelConfig, ModelParams)

class ConfiguarationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_preparing_config(self) -> DataPreparingConfig:
        config = self.config.data_preparing

        create_directories([config.root_dir])

        data_preparing_config = DataPreparingConfig(
            root_dir=config.root_dir,
            boardgame_data_file=config.boardgame_data_file,
            ratings_data_file= config.ratings_data_file
        )

        return data_preparing_config

    def get_data_processing_config(self) -> DataProcessingConfig:
        config = self.config.data_processing

        create_directories([config.root_dir])    
        create_directories([config.pickle_dir])

        data_processing_config = DataProcessingConfig(
            root_dir=config.root_dir,
            boardgame_data_file=config.boardgame_data_file,
            ratings_data_file= config.ratings_data_file,
            pickle_dir = config.pickle_dir
        )

        return data_processing_config

    def get_model_config(self) -> ModelConfig:
        config = self.config.model

        create_directories([config.root_dir])    

        model_config = ModelConfig(
            root_dir=config.root_dir,
            weight_ratings_hb_file=config.weight_ratings_hb_file,
            pickle_dir = config.pickle_dir,
            bg_info = config.bg_info,
            data_cb = config.data_cb,
            similarity_cb = config.similarity_cb, 
            model_cfb = config.model_cfb,
            bg_pivot_cfb = config.bg_pivot_cfb
        )

        return model_config

    def get_model_params(self) -> ModelParams:
        params = self.params.model_params

        model_params = ModelParams(
            K=params.K,
            BOARDGAME_NAME=params.BOARDGAME_NAME,
        )

        return model_params