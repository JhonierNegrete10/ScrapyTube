import os
import pandas as pd

class DataSaver:
    def __init__(self, path):
        self.path = path

    def save(self, df: pd.DataFrame):
        # Crear cualquier subcarpeta necesaria
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        # Verificar si el archivo ya existe
        if os.path.exists(self.path):
            base, extension = os.path.splitext(self.path)
            i = 1
            while os.path.exists(f"{base}_{i}{extension}"):
                i += 1
            self.path = f"{base}_{i}{extension}"

        # Guardar el DataFrame en un archivo CSV
        df.to_csv(self.path, index=False)

 
'''#! Uso de la clase
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
saver = DataSaver('data/data.csv')
saver.save(df)
'''