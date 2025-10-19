import os
class DataIngestionConfig:
    def __init__(self):
        self.source_path=os.path.join("data", "external_sources", "data.csv")
        self.destination_path=os.path.join("data", "rawdata","rawdata.csv")
class DataProcessingConfig:
    def __init__(self):
        self.rawdata_path=os.path.join("data", "rawdata","rawdata.csv")
        self.processed_path=os.path.join("data", "processed_data","pdata.csv")