from src.pipeline.data_deploy_pipeline import DataDeployPipeline

from src import logger
def main_prepare_data_for_deploy():
    STAGE_NAME = "Data Deploy Stage"


    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = DataDeployPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<\n\n +x==================x+")
    except Exception as e:
        logger.exception(e)
        raise e

