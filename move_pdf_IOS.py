import pdfplumber
import os
import shutil

# TODO: it not reconizes the number 309, because is the same that 308 (see pdf)

# Paths to directories on the desktop
pdf_dir = '/Users/MAXEDV/Desktop/re_'  # Directory containing PDFs to be checked
done_dir = '/Users/MAXEDV/Desktop/re_Erledigt'  # Directory where PDFs will be moved if the number is found

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

# Function to search for numbers in the first column of a PDF
def find_number_in_pdf(pdf_path, numbers):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.splitlines()
            for line in lines:
                columns = line.split()  # Adjust based on how columns are separated
                if columns:
                    first_column = columns[0].strip()
                    if first_column in numbers:
                        return first_column
    return None

# Process each PDF in the target directory
if os.path.exists(pdf_dir):
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]

    # Extract object numbers from all PDFs
    all_object_numbers = set()
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        object_numbers = extract_object_numbers(pdf_path)
        all_object_numbers.update(object_numbers)

    moved_files = []
    remaining_files = []

    # Process each PDF to find the object numbers
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        number_found = find_number_in_pdf(pdf_path, all_object_numbers)
        if number_found:
            # New filename
            new_filename = f"{number_found}_{pdf_file}"
            new_path = os.path.join(done_dir, new_filename)
            # Move and rename the file
            shutil.move(pdf_path, new_path)
            moved_files.append(pdf_file)
        else:
            remaining_files.append(pdf_file)

    # Print the results
    print("Files moved to done directory:")
    for file in moved_files:
        print(file)

    print("\nFiles remaining in the original directory:")
    for file in remaining_files:
        print(file)

else:
    print(f"The directory {pdf_dir} does not exist.")
