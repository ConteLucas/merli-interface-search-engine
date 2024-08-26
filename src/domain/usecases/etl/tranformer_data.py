from pandas import DataFrame
from typing import List, Dict


class TransformerData:
    def transform(self, df: DataFrame) -> List[Dict[str, any]]:
        try:
            result = []
            for index, row in df.iterrows():
                result.append({
                    "index": row['Index'],
                    "title": row['Title'],
                    "link": row['Link'],
                })
            return result
        except Exception as e:
            print(f"Error during transformation: {e}")
            return None
