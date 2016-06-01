import csv

fr = open('sorted_questions.csv', 'rb')
fw = open('deduped.csv','w')
try:
    reader = csv.reader(fr)
    current_row = [];
    next_row =[];
    exceptions = [];
    csv_writer = csv.writer(fw, dialect='excel')
    for row in reader:
        if not current_row:
            current_row = row;
            exceptions.extend([row[7]])
        else:
            next_row = row
            if current_row[0] == next_row[0]:
                exceptions.extend([row[7]])
            else:
                current_row[7] = exceptions;
                csv_writer.writerow(current_row)
                print(current_row)
                current_row = row;
                next_row = [];
                exceptions = [];
                exceptions.extend([row[7]])
finally:
    fr.close()
    fw.close()
