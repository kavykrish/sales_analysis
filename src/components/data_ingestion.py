import os
import shutil






class DataIngestion:
    def __init__(self,config):
        self.source_path=config.source_path
        self.destination_path=config.destination_path
    def ingestdata(self):
        destination_dir = os.path.dirname(self.destination_path)
        os.makedirs(destination_dir, exist_ok=True)

        # Check if source file exists
        if not os.path.exists(self.source_path):
            print(f"❌ Source file not found: {self.source_path}")
            return

        # Copy file
        shutil.copy(self.source_path, self.destination_path)
        print(f"✅ Data copied successfully to {self.destination_path}")
