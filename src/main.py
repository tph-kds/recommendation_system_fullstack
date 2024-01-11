from src.Collaborative_Filtering_Based_RS.boardgame_recommendation_system.main import main_cfb
from src.Content_Based_RS.boardgame_recommendation_system.main import main_cb
from src.Hybrid_RS.boardgame_recommendation_system.main import main_hybrid
from src.Recommendation.boardgame_recommendation_system.main import main_prepare_data_for_deploy
from src import logger

def main_pipeline():
    main_cfb()
    logger.info("<<<<<<<<<<<<<<<<<<<<< Completed Stage I >>>>>>>>>>>>>>>>>>>>>>>")
    main_cb()
    logger.info("<<<<<<<<<<<<<<<<<<<<< Completed Stage II >>>>>>>>>>>>>>>>>>>>>>>")
    main_hybrid()
    logger.info("<<<<<<<<<<<<<<<<<<<<< Completed Stage III >>>>>>>>>>>>>>>>>>>>>>>")
    main_prepare_data_for_deploy()
    logger.info("<<<<<<<<<<<<<<<<<<<<< Completed PipeLine >>>>>>>>>>>>>>>>>>>>>>>")


main_pipeline()