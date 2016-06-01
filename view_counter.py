import csv

def get_view_count(row):
    file_name = "./results/"+row+".txt"
    file = open(file_name, 'rb')
    file_exception = csv.reader(file)
    sum = 0
    for r in file_exception:
        sum = sum + int(r[3])
    return sum

fr = open('input.txt', 'rb')
fw = open('results.txt','w')
try:
    reader = csv.reader(fr)
    for row in reader:
        total = get_view_count(str(row[0]))
        printer = str(row[0]) + "," + str(total) + '\n'
        fw.write(printer)
        print row[0] + " " + str(total)

finally:
    fr.close()
    fw.close()
