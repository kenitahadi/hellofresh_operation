# HelloFresh Case Study
## Objectives
This exercise aims to apply Python for Data Wrangling such as data cleaning, standardization and fuzzy matching to a case study for HelloFresh. The objectives of this exercise are as follows:
1. Loading a JSON format dataset to a readable csv dataset
2. Create a subset of data that only contains a specific ingredient (Chillies) and its mispelled words (string matching)
3. Create categorization for recipes based on their prep time and cook time

## Python Version
This exercise is ran using Python version 3.9.12

## Installations for required dependencies
To be executed in Command Prompt Windows
1. Pandas 
`` pip install pandas ``
2. Fuzzywuzzy 
`` pip install fuzzywuzzy``
3. Isodate
`` pip install Isodate``

## Usage
1. Ensure that the dataset saved in the original format (JSON).
2. Make sure that the downloaded JSON file in located in the same folder wih the `recipe_reader.py`
3. Run the `recipe_reader.py` script:
4. The program will execute data wrangling tasks on the provided dataset, resulting in 4 csv datasets based on the completion of each required task. 
5. The final dataset `recipes_chilies_only_final.csv' will be saved in the specified output file path.

## Dependencies

- **pandas**: Used for data manipulation and analysis, providing powerful data structures and functions. 
- **fuzzywuzzy**: Enables fuzzy string matching, useful for handling variations or misspellings in ingredient names.
- **isodate**: Helps with parsing and formatting ISO 8601 dates, if needed in the dataset.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



