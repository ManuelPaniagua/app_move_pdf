import pdfplumber
import os
import shutil

# Define the specific number you want to search for
specific_number = '42'  # Replace this with the number you're searching for

# Paths to directories on the desktop
pdf_dir = '/Users/MAXEDV/Desktop/re_'  # Directory containing PDFs to be checked
done_dir = '/Users/MAXEDV/Desktop/re_Erledigt' 

# Expand user paths (e.g., replace ~ with the full path to the home directory)
pdf_dir = os.path.expanduser(pdf_dir)
done_dir = os.path.expanduser(done_dir)

# Ensure the destination directory exists
os.makedirs(done_dir, exist_ok=True)

# Function to extract object numbers from a PDF
def extract_object_numbers(pdf_path):
    object_numbers = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.splitlines()
            for line in lines:
                columns = line.split()  # Adjust based on how columns are separated
                if columns:
                    first_column = columns[0].strip()
                    if first_column.isdigit():
                        object_numbers.append(first_column)
    return object_numbers

# Function to search for a specific number in the first column of a PDF
def find_specific_number_in_pdf(pdf_path, number):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.splitlines()
            for line in lines:
                columns = line.split()  # Adjust based on how columns are separated
                if columns:
                    first_column = columns[0].strip()
                    if first_column == number:
                        return True
    return False

# Process each PDF in the target directory
if os.path.exists(pdf_dir):
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]

    moved_files = []
    remaining_files = []
    found_number = False  # Flag to check if the specific number is found

    # Process each PDF to find the specific number
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        number_found = find_specific_number_in_pdf(pdf_path, specific_number)
        if number_found:
            found_number = True  # Set the flag to True if the number is found
            # New filename
            new_filename = f"{specific_number}_{pdf_file}"
            new_path = os.path.join(done_dir, new_filename)
            # Move and rename the file
            shutil.move(pdf_path, new_path)
            moved_files.append(pdf_file)
        else:
            remaining_files.append(pdf_file)

    # Print the results
    if moved_files:
        print("Files moved to done directory:")
        for file in moved_files:
            print(file)
    else:
        print(f"No files contained the specific number '{specific_number}'.")

    print("\nFiles remaining in the original directory:")
    for file in remaining_files:
        print(file)

else:
    print(f"The directory {pdf_dir} does not exist.")
