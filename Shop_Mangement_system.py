import pandas as pd
from datetime import datetime
import os

#Initialisation of info Dictionary
info = {}
def add(name, s_name, bill, s_stat):
    info[name] = [s_name, bill, s_stat]
    print(info)

def main():
    while True:
        Name = input("Enter Name of The Customer: ")
        Ser_name = input("Enter Service Name: ")
        Bill = int(input(f"Enter Total Amount of Bill For {Name}: "))
        Ser_stat = input("Enter Service Done Status(Done/Not Done): ")
        add(Name, Ser_name, Bill, Ser_stat.upper())
        x = input("Want To Add More Customer (Y/N):")
        if x.upper() == 'N':
            break
    create_excel_file()

def create_excel_file():
    current_date = datetime.now().strftime("%Y-%m-%d")   #using date time module to get the current date 
    filename = f"data_{current_date}.xlsx"

    # Convert the dictionary to a DataFrame
    new_data_df = pd.DataFrame.from_dict(info, orient='index', columns=['Service Name', 'Bill', 'Service Done Status'])

    if os.path.exists(filename):
        # If the file exists,it will read the existing data
        existing_data_df = pd.read_excel(filename, index_col='Name')
        
        # Append new data to the existing data
        updated_data_df = pd.concat([existing_data_df, new_data_df])
    else:
        # If the file does not exist, the new data is the updated data
        updated_data_df = new_data_df

    # Save the updated data to the Excel file
    updated_data_df.to_excel(filename, index_label='Name')

    print(f"Customer information has been saved to {filename}")

if __name__ == "__main__":
    main()
