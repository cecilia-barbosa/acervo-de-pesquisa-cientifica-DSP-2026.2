import logging
import logging.config
from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
LOGGING_FILE = BASE_DIR / "logging.yaml"

with open(LOGGING_FILE, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

LOG_DIR = BASE_DIR / "storage" / "logs"
config["handlers"]["file"]["filename"] = str(LOG_DIR / "sistema.log")

logging.config.dictConfig(config)

logger = logging.getLogger("AcervoPesquisa_api")
logger.info("Sistema de logging inicializado.")