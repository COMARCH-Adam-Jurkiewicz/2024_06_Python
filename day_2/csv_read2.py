import csv
plik = "OMNI_PICKUP_CONFIRMATION_DELV2024_06_20.csv"

with open(plik, "r") as csv_file_descriptor:
    csv_read_object = csv.reader(csv_file_descriptor,  delimiter=';')
    for data_row in csv_read_object:
        # print(f"{data_row=}")
        try:
            sales_office = data_row[5]
            if sales_office == "POSAgent":
                print(f"{data_row=}")
        except:
            pass

