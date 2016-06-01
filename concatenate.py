import csv

fr = open('input.txt', 'rb')
fw = open('concat.txt','w')
try:
    reader = csv.reader(fr)
    for row in reader:
        exception_name = str(row[0])
        file_name = "./results/" + exception_name + ".txt"
        file = open(file_name, 'rb')
        file_exception = csv.reader(file)
        csv_writer = csv.writer(fw,dialect='excel')
        for r in file_exception:
            r[7] = exception_name
            csv_writer.writerow(r[0:8])
        print file_name

finally:
    fr.close()
    fw.close()
