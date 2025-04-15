import pandas as pd

class Shared_data:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = {
                "candles":pd.DataFrame(columns=["open","close","high","low",]),
                "indicators":{},
                "objects":[]
            }
        return cls._instance