import os
from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import (DataDeployConfig)

class ConfiguarationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_deploy_config(self) -> DataDeployConfig:
        config = self.config.data_deploy

        create_directories([config.root_dir])

        data_deploy_config = DataDeployConfig(
            root_dir = config.root_dir,
            weight_ratings_hb_file = config.weight_ratings_hb_file,
            bg_info = config.bg_info,
            data_cb = config.data_cb,
            similarity_cb = config.similarity_cb,
            model_cfb = config.model_cfb,
            bg_pivot_cfb = config.bg_pivot_cfb,
            dir_deploy = config.dir_deploy,
            zip_dir = config.zip_dir,
            file_zip = config.file_zip,
            all_file_cfb = config.all_file_cfb,
            all_file_cb = config.all_file_cb,
        )

        return data_deploy_config
