### REQUIRED PACKAGES ###
import pandas
import json
import csv
from fuzzywuzzy import fuzz
import isodate


### CONVERT JSON FILE TO CSV ###
data = []
with open('recipes.json', 'r') as f: 
    for line in f: 
        data.append(json.loads(line))


csv_file_path = "recipes_chillies_only.csv"

headers = list(data[0].keys())

with open(csv_file_path, 'w', newline='', encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)

    # write headers
    writer.writeheader()

    for record in data: 
        writer.writerow(record)



### READ THE INGRIDIENTS COLOUMNS TO EXTRACT RECIPES WITH CHILIES ###
def extract_rows_with_ingredient(csv_file, ingredient_name):
    # List to store rows with the specified ingredient
    rows_with_ingredient = []

    # Open the CSV file and iterate through each row
    with open(csv_file, 'r', newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Check if the "ingredient" column contains the specified ingredient
            if ingredient_name.lower() in row['ingredients'].lower():
                # If the ingredient is found, append the row to the list
                rows_with_ingredient.append(row)
            


### EXTRACT RECIPES THAT INCLUDE ALSO THE MISPELLED OF CHILIES ###
            # Check if the target word is in the specified column using fuzzy string matching
            threshold = 70
            if fuzz.partial_ratio(ingredient_name.lower(), row['ingredients'].lower()) >= threshold:
                rows_with_ingredient.append(row)
            

    return rows_with_ingredient

data2 = extract_rows_with_ingredient("recipes_chillies_only.csv", "Chilies")

# Append the extracted data to a new csv file
csv_file_path_2 = "recipes_chillies_only_2.csv"
with open(csv_file_path_2, 'w', newline='', encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)

    # write headers
    writer.writeheader()

    for record in data2: 
        writer.writerow(record)


        
### CREATE A CATEGORIZATION FOR RECIPES' DIFFICULTY LEVEL BASED ON COOKTIME AND PREPTIME ###
        
# Convert the PrepTime and CookTime to a recognizeable time format
def sum_columns(input_file, output_file, column1_name, column2_name, new_column_name):
    # Open the input CSV file for reading and the output CSV file for writing
    with open(input_file, 'r', newline='', encoding="utf-8") as infile, \
         open(output_file, 'w', newline='', encoding="utf-8") as outfile:
        
        # Create a CSV reader and writer objects
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + [new_column_name])
        
        # Write the header row to the output file
        writer.writeheader()
        
        # Iterate through each row in the input file
        for row in reader:
            # Extract values from the specified columns and convert them to integers
            if row[column1_name] != '':
                column1_value = isodate.parse_duration(row[column1_name]).total_seconds()
            if row[column2_name] != '':
                column2_value = isodate.parse_duration(row[column2_name]).total_seconds()
            
# Create collumn TotalTime from the summation of PrepTime and CookTime
            # Calculate the sum of the two columns
            sum_value = column1_value + column2_value
            
            # Update the row with the sum value
            row[new_column_name] = sum_value
            
            # Write the updated row to the output file
            writer.writerow(row)


# Categorize the TotalTime into difficuty levels
def difficulty_categorize(input_file, output_file, new_column_name):
    # Open the input CSV file for reading and the output CSV file for writing
    with open(input_file, 'r', newline='', encoding="utf-8") as infile, \
         open(output_file, 'w', newline='', encoding="utf-8") as outfile:
        
        # Create a CSV reader and writer objects
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + [new_column_name])
        
        # Write the header row to the output file
        writer.writeheader()
        
        # Iterate through each row in the input file
        for row in reader:
            # Extract values from the specified columns and convert them to integers
            total_time = int(float(row["Total Time"]))

            difficulty = ""

            if total_time > 3600:
                difficulty = "Hard"
            elif total_time >= 1800  and total_time <= 3600:
                difficulty = "Medium"
            elif total_time < 1800:
                difficulty = "Easy"
            
            # Update the row with the sum value
            row[new_column_name] = difficulty
            
            # Write the updated row to the output file
            writer.writerow(row)


# Sum the preparation time
csv_file_path_3 = "recipes_chillies_only_3.csv"
sum_columns(csv_file_path_2, csv_file_path_3, "cookTime", "prepTime", "Total Time")

# Categorize the difficulty
csv_file_path_final = "recipes_chillies_only_final.csv"
difficulty_categorize(csv_file_path_3, csv_file_path_final, "Difficulty")