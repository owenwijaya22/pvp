import csv
from pathlib import Path
import pandas
import os
csv_path = Path.home() / Path('Downloads')
csv_files = [file for file in csv_path.glob('*.csv')]
latest_csv_file_path = max(csv_files, key=os.path.getctime)
print(latest_csv_file_path)
read_file = pandas.read_csv(f'{latest_csv_file_path}')
new_name = input('New file name: ')
read_file.to_excel((fr"{csv_path}\{new_name}.xlsx"))