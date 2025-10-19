from src.components.data_preprocessing import DataPreprocessing
from src.config import DataProcessingConfig

config=DataProcessingConfig()
b=DataPreprocessing(config)
b.dataprocessing()