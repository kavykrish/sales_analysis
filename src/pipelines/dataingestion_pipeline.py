from src.components.data_ingestion import DataIngestion
from src.config import DataIngestionConfig

b=DataIngestionConfig()
# print(b.source_path)
a=DataIngestion(b)
a.ingestdata()
