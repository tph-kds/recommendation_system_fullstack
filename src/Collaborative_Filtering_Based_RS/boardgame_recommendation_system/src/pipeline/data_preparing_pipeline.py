from src.config.configuaration import ConfiguarationManager
from src.components.data_preparing import DataPreparing
from src import logger
from pathlib import Path

STAGE_NAME = "Data Preparing Stage"

class DataPreparingTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        data_preparing_config = config.get_data_preparing_config()
        data_preparing = DataPreparing(config=data_preparing_config)
        
        # Read File
        # print(str(data_preparing_config.boardgame_data_file))
        bg_df = data_preparing.read_file(data_preparing_config.boardgame_data_file)
        ratings_df = data_preparing.read_file(data_preparing_config.ratings_data_file)

        bg_cfb_data = data_preparing.file_bg(bg_df)
        ratings_cfb_data = data_preparing.file_ratings(ratings_df)

        data_preparing.save_dataset_preparing(bg_cfb_data, file_name = "bg_data_cfb_preparing")
        data_preparing.save_dataset_preparing(ratings_cfb_data, file_name ="ratings_data_cfb_preparing")
        # print(ratings_cfb_data)




if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = DataPreparingTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<\n\n +x==================x+")
    except Exception as e:
        logger.exception(e)
        raise e