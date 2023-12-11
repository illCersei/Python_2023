import csv
import pickle

class Table:
    def get_rows_by_number(data, start, stop=None, copy_table=True):
        if stop:
            if start<1 or stop > len(data):
                print("Ошибка индексов")
                return 0
        else:
            if start<1:
                print("Ошибка индексов")
                return 0
  
        new_data = data.copy() if copy_table else data

        if stop is None:
            stop = start

        new_data = {zagolovok: [] for zagolovok in new_data.keys()}
        for i in range(start - 1, stop):
            for zagolovok in data.keys():
                new_data[zagolovok].append(data[zagolovok][i])

        return new_data
        
    def get_rows_by_index(data, *values, copy_table=True):
        new_data = data.copy() if copy_table else data
        index_column = list(new_data.keys())[0] 

        if not values:
            return new_data

        new_data = {zagolovok: [] for zagolovok in new_data.keys()}
        for i, index_value in enumerate(data[index_column]):
            if index_value in values:
                for zagolovok in data.keys():
                    new_data[zagolovok].append(data[zagolovok][i])
        
        if not new_data["City"]:
            print("Не найдено")
            return 0

        return new_data
    
    def get_column_types(data, by_number=True):
        """Всегда str в нормальной таблице"""
        type_xd = {}
        for zagolovok, values in data.items():
            if all(isinstance(value, int) for value in values):
                data_type = int
            elif all(isinstance(value, float) for value in values ):
                data_type = float
            elif all(value.upper() in ('TRUE', 'FALSE') for value in values):
                data_type = bool
            else:
                data_type = str

            if by_number:
                zagolovok = list(data.keys()).index(zagolovok) + 1

            type_xd[zagolovok] = data_type

        return type_xd
    
    def set_column_types(data, types_dict, by_number=True):
        new_data = data.copy()

        for zagolovok, data_type in types_dict.items():
            if by_number:
                zagolovok = list(data.keys())[zagolovok - 1]

            new_values = []
            for value in new_data[zagolovok]:
                try:
                    new_values.append(data_type(value))
                except:
                    new_values.append(value)
            new_data[zagolovok] = new_values

        return new_data
    
    def get_values(data, column=0):
        if isinstance(column, int):
            zagolovok = list(data.keys())[column]
        else:
            zagolovok = column

        values = data.get(zagolovok)
        type_xd = Table.get_column_types(data).get(zagolovok, str)
        typed_values = [type_xd(value) for value in values]
        return typed_values
    
    def get_value(data, num, column=0):
        values = Table.get_values(data, column)
        return values[num-1]
    
    def set_values(data, new_values, column=0):
        new_data = data.copy()
        if isinstance(column, int):
            zagolovok = list(data.keys())[column]
        else:
            zagolovok = column

        type_xd = Table.get_column_types(data).get(zagolovok, str)
        typed_values = [type_xd(value) for value in new_values]
        new_data[zagolovok] = typed_values
        return new_data
    
    def set_value(data, num, value, column=0):
        if isinstance(column, int):
            zagolovok = list(data.keys())[column]
        else:
            zagolovok = column

        type_xd = Table.get_column_types(data).get(zagolovok, str)
        typed_value = type_xd(value)

        data[zagolovok][num-1] = typed_value
        return data
    
    def print_table(data):
        zagolovok = list(data.keys())
        max_length = {zag: max(len(zag), *[len(str(value)) for value in values]) for zag, values in data.items()}
                                        
        def print_row(values):
            row = [f"{str(value).center(max_length[zag])}" for zag, value in zip(zagolovok, values)]
            print("|".join(row))

        sep = "+".join("-" * (max_length[zag]) for zag in zagolovok)

        print(sep)
        print_row(zagolovok)
        print(sep)

        for i in range(len(data[next(iter(data))])):
            values = [data[zag][i] for zag in zagolovok]
            print_row(values)

        print(sep)

    def load_table_csv(path):
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file)
            zagolovok = next(reader)
            data = {stolb: [] for stolb in zagolovok}
            for row in reader:
                for stolb, value in zip(zagolovok, row):
                    data[stolb].append(value)
        
        return data

    def save_table_csv(path, data):
        if data:
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data.keys())
                
                max_rows = max(len(stolb) for stolb in data.values())
                for i in range(max_rows):
                    writer.writerow([data[stolb][i] for stolb in data.keys()])
        else:
            print("Ошибка в данных csv")
            return 0

    def load_table_pickle(path):
        with open(path, 'rb') as file:
            try:
                data = pickle.load(file)
            except:
                print("Ошибка load pickle")
                return 0
        return data

    def save_table_pickle(path, data):
        if data:
            with open(path, 'wb') as file:
                pickle.dump(data, file)
        else:
            print("Ошибка в данных pickle")
            return 0

    def save_table_txt(path, data):
        if data:
            with open(path, 'w') as file:
                for stolb, values in data.items():
                    try:
                        file.write(f"{stolb}: {', '.join(values)}\n")
                    except:
                        print("Ошибка txt save")
                        return 0

        else:
            print("Ошибка в данных txt")
            return 0
    
test_table = {'City': ['Moscow', 'London', 'New York City', 'Paris'],
              'Population': ['13_000_000', '9_000_000', '8_500_000', '2_600_000'],
              'Country': ['Russia', 'UK', 'USA', 'France'],
              'Test' : ['1','2','3','4']}

test_types_table= {'City': [1,1,2,5],
                   'Population': [13000000.6, 9000000.8, 8500000.7, 2600000.7],
                   'Country': ['Russia', 'UK', 'USA', 'France'],
                    'Test': ['True','False','True','False']}
            
Table.save_table_csv("test_csv.csv", test_table)
test_csv = Table.load_table_csv("test_csv.csv")
Table.save_table_csv("test_csv2.csv", test_csv)
print(f"csv print:")
Table.print_table(test_csv)

Table.save_table_pickle("test_pickle.pickle",test_table)
test_pickle = Table.load_table_pickle("test_pickle.pickle")
Table.save_table_pickle("test_pickle2", test_pickle)
print(f"pickle print:")
Table.print_table(test_pickle)

Table.save_table_txt("test_txt.txt",test_table)

z = Table.get_rows_by_number(test_csv,1,1)
print(f"get_rows_by_number:")
Table.print_table(z)
z1 = Table.get_rows_by_index(test_csv, "Moscow", "New York City")
print(f"get_rows_by_index:")
Table.print_table(z1)

t = Table.get_column_types(test_types_table)
print(f"get_column_types:")
print(t)
t1 = Table.set_column_types(test_types_table,{1: str, 2: str, 3: str, 4:str})
print(f"set_column_types:")
Table.print_table(t1)

s = Table.get_values(test_table)
print(f"get_values:")
print(s)
s1 = Table.get_value(test_table, 1, "City")
print(f"get_value:")
print(s1)

n = Table.set_values(test_table, ["dsfgfdg", "xd", "fgg", "jkkkkk"],1)
print(f"set_values:")
Table.print_table(n)
n1 = Table.set_value(test_table, 1, "ccccccccc", "Country")
print(f"set_value:")
Table.print_table(n1)

z = Table.get_rows_by_index(test_csv, "Moscow", "London")
print(f"get_rows_by_index:")
Table.print_table(z)



