import csv


class CSVAdapter:

    @staticmethod
    def get_csv_file(filename):
        data_from_csv = []
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            # print(reader.__dir__())
            # print(reader.line_num)
            for row in reader:
                data_from_csv.append(row)

        return data_from_csv

    @staticmethod
    def write_csv_in_file(filename, data):
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print('Данные записаны')
        return True

if __name__ == '__main__':
    adapter = CSVAdapter()
    data_from_csv = adapter.get_csv_file(r'CSV_data/customers_data.csv')
    adapter.write_csv_in_file(r'CSV_data/data_from_csv.scv', data_from_csv)