import pandas as pd
class DataPreprocessing:
    def __init__(self,a):
        self.raw_path=a.rawdata_path
        self.pre_path=a.processed_path
    def dataprocessing(self):
        
       data=pd.read_csv(self.raw_path)
       data.fillna(method="ffill", inplace=True)
       data.to_csv(self.pre_path,index=False)