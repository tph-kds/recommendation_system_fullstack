import os
import shutil
import zipfile
from src import logger
from src.utils.common import get_size
from src.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Nếu là một file xác định | copy cho phòng trường hợp mất dữ liệu góc (đặt tên hơi sai)
    def copy_file_data(self) -> str:
        """
            Target: 
                copy data file from dataset of original foler to main folder
        """
        try: 
            name_file = self.config.local_data_file.split("/")[-1]
            original_filepath = f"Datasets/{name_file}"
            destination_folder = self.config.root_dir
            if not os.path.exists(os.path.join(destination_folder, name_file)):
                shutil.copy(original_filepath, destination_folder)
                logger.info(f" Loaded successfully file from {original_filepath} to path: {destination_folder}")
            else:
                logger.info(f" File was existed with path: {destination_folder}")
        except Exception as e:
            raise e
    
    def unzip_file_data(self):
        """
        Target: 
            unzip data file from dataset of original foler to main folder
            Extracts the zip file  into the data directory
            Function returns None
        """
        try: 
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            name_file = self.config.local_data_file.split("/")[-1]
            original_filepath = f"Datasets/{name_file}"
            destination_folder = self.config.root_dir

            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f" Unzip successfully data file from {original_filepath} to path: {destination_folder}")
                # Kiểm tra xem file tồn tại không trước khi xóa
            if os.path.exists(self.config.local_data_file):
                os.remove(self.config.local_data_file)
                logger.info(f"File '{self.config.local_data_file}' đã được xóa thành công.")
            else:
                logger.info(f"File '{self.config.local_data_file}' không tồn tại.")
        except Exception as e:
            raise e