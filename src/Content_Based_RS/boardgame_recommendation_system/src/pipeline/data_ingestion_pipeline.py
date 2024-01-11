from src.config.configuaration import ConfiguarationManager
from src.components.data_ingestion import DataIngestion
from src import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.copy_file_data()
        data_ingestion.unzip_file_data()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<\n\n +x==================x+")
    except Exception as e:
        logger.exception(e)
        raise e