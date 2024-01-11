import os
import sys
import logging

logging_str = "[%(asctime)s : %(levelname)s: %(module)s : %(message)s]"

original_path = "src/Collaborative_Filtering_Based_RS/boardgame_recommendation_system"
log_dir = "logs"
log_path_dir = original_path + "/" + log_dir

log_filepath = os.path.join(log_path_dir,"running_logs.log")
os.makedirs(log_path_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("bg_rs_Logger")
