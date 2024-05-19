'''Create a Python module that demonstrates skills in fetching data from the web, processing it using Python collections, and writing the processed data to different file formats.'''

# Standard library imports
import csv
import logging
import os
import re
import json
import pathlib
from io import StringIO

# External library imports (requires virtual environment)
from numpy import save
import requests  
from collections import Counter
import pandas as pd
import xlrd

def fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url):

    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(txt_folder_name):
            os.makedirs(txt_folder_name)

        # Fetch text data from the URL
        response = requests.get(txt_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Extract text from HTML using regex
        text_data = re.sub('<[^<]+?>', '', response.text)
        
        # Write text data to the output file
        output_file_path = os.path.join(txt_folder_name, txt_filename)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text_data)
        
        print(f"Text data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing text data: {e}")

def fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url):

    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(csv_folder_name):
            os.makedirs(csv_folder_name)

        # Fetch CSV data from the URL
        response = requests.get(csv_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Write CSV data to the output file
        output_file_path = os.path.join(csv_folder_name, csv_filename)
        with open(output_file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"CSV data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing CSV data: {e}")

def fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url):

    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(excel_folder_name):
            os.makedirs(excel_folder_name)

        # Fetch Excel data from the URL
        response = requests.get(excel_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Write Excel data to the output file
        output_file_path = os.path.join(excel_folder_name, excel_filename)
        with open(output_file_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Excel data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing Excel data: {e}")

def fetch_and_write_json_data(json_folder_name, json_filename, json_url):

    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(json_folder_name):
            os.makedirs(json_folder_name)

        # Fetch JSON data from the URL
        response = requests.get(json_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse JSON data
        json_data = response.json()
        
        # Write JSON data to the output file
        output_file_path = os.path.join(json_folder_name, json_filename)
        with open(output_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
        
        print(f"JSON data successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error fetching or writing JSON data: {e}")

def process_txt_file(txt_folder_name, txt_filename, output_filename):
    try:
        # Read the text data from the file
        text_folder_path = pathlib.Path(txt_folder_name)
        text_file_path = text_folder_path / txt_filename
        text_data = text_file_path.read_text(encoding='utf-8')

        # Processing text data
        words = text_data.split()
        unique_words = set(words)

        # Writing unique words to a file
        with open('unique_words_P3.txt', 'w') as file:
            for word in unique_words:
                file.write(word + '\n')
        processed_data = f"Unique words count: {len(unique_words)}"

        # Define output file path
        output_file_path = os.path.join(txt_folder_name, output_filename)
            
        # Write processed data to output text file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(processed_data)
            
        print(f"Processed data written to '{output_file_path}'")
    except Exception:
        print("Error processing text file.")

def process_csv_file(csv_folder_name, csv_filename, output_filename):
    try:
        input_file_path = os.path.join(csv_folder_name, csv_filename)

        # Read input CSV file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            # Read the header to dynamically determine column names
            header = next(csv_reader)

            # Read data and convert rows to tuples
            data = [tuple(row) for row in csv_reader]

        # Pandas dataframe for analysis
        df = pd.DataFrame(data, columns=header)

        # display the dataframe
        df

        # Calculate summary statistics
        summary_statistics = df.describe(include=['object'])

        #convert summary statistics to processed data string
        processed_data = str(summary_statistics)

        # Define output file path
        output_file_path = os.path.join(csv_folder_name, output_filename)
        
        # Write processed data to output text file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(processed_data)

        print(f"Processed data written to '{output_file_path}'")
    except Exception:
        print("Error processing csv file.")

def process_excel_file(excel_folder_name, excel_filename, output_filename):
    try:
        # Construct the file paths
        input_file_path = os.path.join(excel_folder_name, excel_filename)
        output_file_path = os.path.join(excel_folder_name, output_filename)
        
        # Read input Excel file
        df = pd.read_excel(input_file_path)
        
        # Calculate summary statistics
        summary_stats = df.describe()
        
        # Convert the summary statistics DataFrame to a string for processed data
        processed_data = summary_stats.to_string()
        
        # Write summary statistics to output text file
        with open(output_file_path, 'w') as output_file:
            output_file.write(processed_data)
        
        print(f"Summary statistics written to '{output_file_path}'")
    except Exception:
        print("Error processing Excel file")

def process_json_file(json_folder_name, json_filename, output_filename):
    try:
        input_file_path = os.path.join(json_folder_name, json_filename)
        with open(input_file_path, 'r') as file:
            json_data = json.load(file)
        
        # Print the loaded JSON data to see its structure
        print("JSON Data Structure:")
        print(json_data)
        
        # Check if "people" key exists in the JSON data
        if "people" in json_data:
            people_list = json_data["people"]
            for person in people_list:
                name_value = person["name"]
                craft_value = person["craft"]
                print(f"Name: {name_value}, Craft: {craft_value}")
                
                # Construct formatted information
                json_info = f"Name: {name_value}\nCraft: {craft_value}"
                
                # Define output file path for each person
                output_person_path = os.path.join(json_folder_name, f"{name_value}_{output_filename}")
                
                # Write information to output text file for each person
                with open(output_person_path, 'w') as output_file:
                    output_file.write(json_info)
                
                print(f"Formatted information saved to '{output_person_path}'")
        else:
            print("Error: 'people' key not found in JSON data.")
            return
        
    except Exception:
        print("Error parsing json data")

def main():
    ''' Main function to demonstrate module capabilities. '''
    #my name input
    name = "Kari Taylor"
    print(f"Name: {name}")
    #urls
    txt_url = 'https://www.gutenberg.org/cache/epub/1342/pg1342-images.html'
    csv_url = 'https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv'
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    json_url = 'http://api.open-notify.org/astros.json'
    #names for output folders
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 
    #names for output files
    txt_filename = 'prideandprejudice.txt'
    csv_filename = 'movies.csv'
    excel_filename = 'cattle.xls' 
    json_filename = 'astronauts.json' 
    #call functions to take web file and convert it to a usable file format
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)
    #call functons for text processing in different file formats
    process_txt_file(txt_folder_name, 'prideandprejudice.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'movies.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'cattle.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'astronauts.json', 'results_json.txt')
    
if __name__ == '__main__':
    main()
