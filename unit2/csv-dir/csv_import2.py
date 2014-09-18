#Source: http://java.dzone.com/articles/python-101-reading-and-writing
import csv
def csv_dict_reader(file_obj):
	"""
	Read a CSV file using csv.csv_dict_reader
	"""
	reader = csv.DictReader(file_obj, delimiter=',')
	for line in reader:
		print(line["first_name"]),
		print(line["last_name"]),
		print(line['address'])

if __name__ == "__main__":
	with open("data.csv") as file_obj:
		csv_dict_reader(file_obj)

