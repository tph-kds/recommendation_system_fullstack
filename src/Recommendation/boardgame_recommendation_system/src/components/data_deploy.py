import os
import shutil
import zipfile
from src import logger
from src.utils.common import get_size
from src.entity.config_entity import (DataDeployConfig)
from src.utils.common import read_yaml, create_directories


class DataDeploy:
    def __init__(self, config: DataDeployConfig):
        self.config = config

    # Nếu là một file xác định | copy cho phòng trường hợp mất dữ liệu góc (đặt tên hơi sai)
    def move_file_data(self) -> str:
        """
            Target: 
                Move data file from dataset of original foler to main folder to deploy model
        """
        try: 
                name_file = self.config.zip_dir.split("/")[-1]
                original_filepath = self.config.zip_dir
                destination_folder = self.config.dir_deploy
                if not os.path.exists(os.path.join(destination_folder, name_file)):
                    shutil.move(original_filepath, destination_folder)
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
                # Kiểm tra xem file tồn tại không trước khi xóa
            # if os.path.exists(self.config.file_zip):
            #     os.remove(self.config.file_zip)
            #     logger.info(f"File '{self.config.file_zip}' đã được xóa thành công.")
            # else:
            #     logger.info(f"File '{self.config.file_zip}' không tồn tại.")
            unzip_path = self.config.dir_deploy
            # os.makedirs(unzip_path, exist_ok=True)

            original_filepath = self.config.dir_deploy

            with zipfile.ZipFile(self.config.file_zip, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f" Unzip successfully data file from {original_filepath}")
        except Exception as e:
            raise e
        
    def zip_file_data(self):
        """
        Target: 
            zip data file from dataset of original foler to the deploy folder
             zip some file  into only one solely file
        """
        try: 
            ## Firstly, delete folder artifact in app folder.
            folder_path_cb = self.config.dir_deploy            
            name_folder_path_cb = self.config.dir_deploy.split("/")[-1]             
            if os.path.exists(folder_path_cb):
                shutil.rmtree(folder_path_cb)
                logger.info(f" Delete successfully folder with name:{name_folder_path_cb}")
                os.makedirs(self.config.dir_deploy)
            else:
                os.makedirs(self.config.dir_deploy)
                logger.info(f" Create successfully a new folder with name:{name_folder_path_cb}")

            
            
            path_file = self.config.file_zip
            original_filepath = self.config.dir_deploy

            file_paths = [self.config.weight_ratings_hb_file,self.config.bg_info,self.config.data_cb,self.config.similarity_cb,self.config.model_cfb,self.config.bg_pivot_cfb]

            with zipfile.ZipFile(path_file, 'w') as zip_ref:
                for file in file_paths:
                    zip_ref.write(file, os.path.basename(file))
                    logger.info(f" Zip successfully data file { os.path.basename(file)} to folder: {original_filepath}")
        except Exception as e:
            raise e

    ## Delete all file which was reated from some floder beforehand.
    def delete_file_data(self):
        """
        Target: 
            delete all of data file from dataset of original foler 
        """
        try: 
            folder_path_cb = self.config.all_file_cb 
            folder_path_cfb = self.config.all_file_cfb 
            folder_path_zip = self.config.file_zip 
            name_folder_path_cfb = self.config.all_file_cfb.split("/")[-1]             
            name_folder_path_cb = self.config.all_file_cb.split("/")[-1]             
            name_folder_path_zip = folder_path_zip.split("/")[-1]             
            if os.path.exists(folder_path_cb) and os.path.isdir(folder_path_cb):
                shutil.rmtree(folder_path_cb)
                logger.info(f" Delete successfully folder with name:{name_folder_path_cb}")

            if os.path.exists(folder_path_cfb) and os.path.isdir(folder_path_cfb):
                shutil.rmtree(folder_path_cfb)
                logger.info(f" Delete successfully folder with name:{name_folder_path_cfb}")
            
            if os.path.exists(folder_path_zip) and os.path.isdir(folder_path_zip):
                shutil.rmtree(folder_path_zip)
                logger.info(f" Delete successfully folder with name:{name_folder_path_zip}")
        except Exception as e:
            raise e   

