import pickle
from src.config.configuaration import ConfiguarationManager
from src.components.model import Model
from src import logger

STAGE_NAME = "Model Stage"

class ModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        model_config = config.get_model_config()
        model_params = config.get_model_params()
        model = Model(config=model_config)
        # Read File
        knowledge_stems_df = model.read_file(model_config.knowledge_stems_cb)

        vector = model.embedding_vector(knowledge_stems_df, max_features= model_params.MAX_FEATURES, stop_words= model_params.STOP_WORDS)
        similarity = model.calculate_similarity(vector)

        file_name_pickle = ["knowledge_stems_cb", "similarity_cb", "embedding_vector_cb"]
        model.save_dataset_model(knowledge_stems_df, similarity , vector, file_name_pickle)
        
        k = model_params.K
        boardgame_name = model_params.BOARDGAME_NAME
        model.recommendation_system_cb(knowledge_stems_df, similarity, boardgame_name, k)


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = ModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<\n\n +x==================x+")
    except Exception as e:
        logger.exception(e)
        raise e