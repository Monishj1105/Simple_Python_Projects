from difflib import SequenceMatcher  # Importing SequenceMatcher from difflib module for comparing text

# Open both text files ('book1.txt' and 'book2.txt') simultaneously using the 'with' statement
with open('book1.txt') as file1, open('book2.txt') as file2:
    data_file1 = file1.read()  # Read the entire content of the first file into data_file1
    data_file2 = file2.read()  # Read the entire content of the second file into data_file2
    
    # Use SequenceMatcher to compare the contents of both files and calculate the similarity ratio
    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    
    # Print the similarity ratio as a percentage, indicating the potential plagiarized content
    print(f" The plagiarized content is {matches * 100}%")