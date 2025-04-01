# Text Similarity Checker (Plagiarism Detection)

## Overview

This Python script compares two text files to determine their similarity using the `SequenceMatcher` class from the `difflib` module. The script calculates a similarity ratio, which can be interpreted as the percentage of potentially plagiarized content between the two files. This can be useful in detecting overlapping or copied content between two documents.

## Requirements

- Python 3.x
- `difflib` (Standard Python Library)

## Files

- `book1.txt`: The first text file to compare.
- `book2.txt`: The second text file to compare.
  
Both files should be placed in the same directory as the script, or you can modify the script to use the correct file paths.

## Usage

### Step 1: Prepare the Text Files
Ensure that both `book1.txt` and `book2.txt` are present in the same directory as the script. The content of these files will be compared for similarities.

### Step 2: Run the Script

```bash
python similarity_checker.py
```

When the script is run, it will:
1. Read the contents of `book1.txt` and `book2.txt`.
2. Use `SequenceMatcher` to calculate the similarity ratio between the two files.
3. Print the similarity ratio as a percentage. The higher the percentage, the more similar the content is between the two files.

Example output:

```
The plagiarized content is 85.7%
```

This indicates that 85.7% of the content between `book1.txt` and `book2.txt` is similar, which could suggest a high degree of overlap or potential plagiarism.

## Explanation of Code

1. **File Reading**: The script opens both `book1.txt` and `book2.txt` using the `with open()` method, which ensures the files are automatically closed after reading.
   
2. **Sequence Matching**: It then uses `SequenceMatcher` from the `difflib` module to compare the content of both files. `SequenceMatcher` calculates the similarity ratio by comparing sequences of characters and checking how similar they are.

3. **Similarity Calculation**: The `ratio()` method of `SequenceMatcher` returns a value between 0 and 1, where 1 means the two files are identical. This value is then multiplied by 100 to represent the similarity percentage.

4. **Output**: The script prints out the percentage of similarity between the two files.

## Example Code

```python
from difflib import SequenceMatcher

# Open both text files ('book1.txt' and 'book2.txt') simultaneously using the 'with' statement
with open('book1.txt') as file1, open('book2.txt') as file2:
    data_file1 = file1.read()  # Read the entire content of the first file into data_file1
    data_file2 = file2.read()  # Read the entire content of the second file into data_file2
    
    # Use SequenceMatcher to compare the contents of both files and calculate the similarity ratio
    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    
    # Print the similarity ratio as a percentage, indicating the potential plagiarized content
    print(f" The plagiarized content is {matches * 100}%")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like to modify anything in the README!
