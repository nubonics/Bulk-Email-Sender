import argparse

from pandas import read_csv


def the_parser():
	parser = argparse.ArgumentParser(description="Coverts a specific txt/csv file to thee excel format.")
	parser.add_argument('--input_file', type=str, help='The input file to parse')
	parser.add_argument('--output_file', type=str, help='The filename of the parsed data')
	args = parser.parse_args()

	r = read_csv(input_file, delimiter=":")

	df = r.replace(25, 587).replace(25, 587)

	with pd.ExcelWriter(output_file+'.xlsx') as writer:
		df1.to_excel(writer, sheet_name='Sheet_name_1')


if __name__ == "__main__":
	the_parser()