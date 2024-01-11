from src.config.configuaration import ConfiguarationManager
from src.components.data_processing import DataProcessing
from src import logger

STAGE_NAME = "Data Processing Stage"

class DataProcessingTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        data_processing_config = config.get_data_processing_config()
        data_processing = DataProcessing(config=data_processing_config)
        # Read File
        bg_df = data_processing.read_file(data_processing_config.boardgame_data_file)
        ratings_df = data_processing.read_file(data_processing_config.ratings_data_file)

        # bg_pivot = data_processing.file_ratings(ratings_df)
        data_processing.save_dataset_processing(ratings_df, "ratings_data_cfb_processing")

        # print(bg_pivot)






if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = DataProcessingTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<\n\n +x==================x+")
    except Exception as e:
        logger.exception(e)
        raise e