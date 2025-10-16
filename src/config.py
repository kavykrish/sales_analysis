import os
class DataIngestionConfig:
    def __init__(self):
        self.source_path=os.path.join("data", "external_sources", "data.csv")
        self.destination_path=os.path.join("data", "rawdata","rawdata.csv")