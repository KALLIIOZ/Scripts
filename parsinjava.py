import os
import re
import argparse

def search_bluetooth_functions_in_file(java_file, keyword):
    bluetooth_functions = []
    with open(java_file, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            if re.search(keyword, line, re.IGNORECASE):
                bluetooth_functions.append((java_file, line_number, line.strip()))
    return bluetooth_functions

def search_bluetooth_functions_in_directory(directory, keyword):
    bluetooth_functions = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.java'):
                java_file = os.path.join(root, file)
                bluetooth_functions.extend(search_bluetooth_functions_in_file(java_file, keyword))
    return bluetooth_functions

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search for a keyword in Java files within a directory.')
    parser.add_argument('directory', type=str, help='The directory to search for Java files.')
    parser.add_argument('keyword', type=str, help='The keyword to search for in Java files.')

    args = parser.parse_args()
    
    directory_to_search = args.directory
    keyword_to_search = args.keyword

    bluetooth_functions = search_bluetooth_functions_in_directory(directory_to_search, keyword_to_search)
    
    if bluetooth_functions:
        print(f"References to '{keyword_to_search}' in .java files:")
        for func in bluetooth_functions:
            print(f"File: {func[0]}, Line: {func[1]}, Content: {func[2]}")
    else:
        print(f"No references to '{keyword_to_search}' found in .java files.")
