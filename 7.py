import csv
import pickle

class Table:
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
            while file:
                r.append(file.readline())
            return r 
            

#test = Table.load_table_csv("test_csv.csv")
#Table.save_table_csv("test_csv2.csv", test)

#Table.save_table_pickle("test_pickle.pickle",[['name', 'smth1', 'smth2'], ['name1', '0', '0'], ['name2', '1', '1']])
#test = Table.load_table_pickle("test_pickle.pickle")

test = Table.load_table_txt("test_txt.txt")
print(test)
