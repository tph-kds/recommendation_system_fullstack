from src.config.configuaration import ConfiguarationManager
from src.components.data_deploy import DataDeploy
from src import logger

STAGE_NAME = "Data Ingestion Stage"

class DataDeployPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        data_deploy_config = config.get_data_deploy_config()
        data_deploy = DataDeploy(config=data_deploy_config)
        data_deploy.zip_file_data()
        # data_deploy.move_file_data()
        data_deploy.unzip_file_data()
        data_deploy.delete_file_data()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = DataDeployPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<\n\n +x==================x+")
    except Exception as e:
        logger.exception(e)
        raise e