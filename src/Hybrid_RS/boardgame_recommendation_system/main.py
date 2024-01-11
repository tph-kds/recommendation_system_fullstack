from src.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipeline.data_preparing_pipeline import DataPreparingTrainingPipeline
from src.pipeline.data_processing_pipeline import DataProcessingTrainingPipeline
from src.pipeline.model_pipeline import ModelPipeline

from src import logger
def main_hybrid():
    STAGE_NAME = "Data Ingestion Stage"

    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<")
        logger.info(f">------------  +x=======================x+  -----------------<")
    except Exception as e:
        logger.exception(e)
        raise e


    STAGE_NAME = "Data Preparing Stage"
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = DataPreparingTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<")
        logger.info(f">------------  +x=======================x+  -----------------<")
    except Exception as e:
        logger.exception(e)
        raise e


    STAGE_NAME = "Model Stage"
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = ModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<")
        logger.info(f">------------  +x=======================x+  -----------------<")
    except Exception as e:
        logger.exception(e)
        raise e
