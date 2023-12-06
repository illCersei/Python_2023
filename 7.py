import csv
import pickle

class Table:
    def __init__(self, table):
        self.table = table

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        if stop is None:
            stop = start + 1

        if copy_table:
            return [row.copy() for row in self.table[start:stop]]
        else:
            return self.table[start:stop]

    def load_table_csv(path_file):
        with open(path_file,'r') as file:
            reader = csv.reader(file)
            return([i for i in reader])

    def save_table_csv(path_file,data):
        with open(path_file, 'w', newline='') as file:
            for i in data:
                writer = csv.writer(file)
                writer.writerow(i)
    
    def load_table_pickle(path_file):
        with open(path_file, 'rb') as file:
            return (pickle.load(file))

    def save_table_pickle(path_file,data):
        with open(path_file, 'wb') as file:
            pickle.dump(data, file)

    def load_table_txt(path_file):
        with open(path_file, 'r') as file:
            r = []
            for line in file:
                r.append([i.strip() for i in line.split(',')])
            return r 
        
    def save_table_txt(path_file, data):
        with open(path_file, 'w') as file:
            for i in data:
                file.write(','.join(i) + '\n')

#est_table = "fdfdsfsdgsdgsg"       
test_table = [['name', 'smth1', 'smth2'], ['name1', '0', '0'], ['name2', '1', '1']]
            
Table.save_table_csv("test_csv.csv", test_table)
test_csv = Table.load_table_csv("test_csv.csv")
Table.save_table_csv("test_csv2.csv", test_csv)
print(test_csv)

x = Table(test_csv)
z = x.get_rows_by_number(2)
print(z)

Table.save_table_pickle("test_pickle.pickle",test_table)
test_pickle = Table.load_table_pickle("test_pickle.pickle")
print(test_pickle)

Table.save_table_txt("test_txt.txt",test_table)
test_txt = Table.load_table_txt("test_txt.txt")
print(test_txt)
