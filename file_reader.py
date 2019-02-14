import jsonlines
from glob import glob


json_files = glob("**/*.json", recursive=True)

for file in json_files:
	with jsonlines.open(file,'r') as reader:
		for obj in reader:
			print(obj['identifier'])