import csv
import pandas as pd
rows = []

file_count = 1
second_count = 1
for i in range(38):
	print("Iteration #"+str(i))
	print("File #"+str(file_count))
	row_count = 0
	with open(f'./tweets/return_{file_count}.csv', 'r') as fileC:
		csvreader = csv.reader(fileC)
		row_count = sum(1 for row in csvreader)
	with open(f'./tweets/return_{file_count}.csv', 'r') as fileC:
		csvreader = csv.reader(fileC)
		with open(f'./tweets/text/text_{second_count}.txt', 'w', encoding='utf-8') as f:
			print("Txt file #"+str(second_count))
			for i in range(row_count-1):
				#print("Row "+str(i))
				f.write(next(csvreader)[1].replace('\n',' '))
				f.write('\n')
			second_count += 1
		file_count +=1