# PDF Number Finder and Mover

## Description

This Python application searches for PDF files in a specified folder and checks if a specific number is present in the first column (Verw.-Nr.) of tables within each PDF. If the number is found, the PDF is moved to a designated output folder.


### Paths to directories on the desktop (example)
pdf_dir = r'C:\Users\YOUR_USERNAME\Desktop\re_'  # Directory containing PDFs to be checked
done_dir = r'C:\Users\YOUR_USERNAME\Desktop\re_Erledigt'  # Directory where PDFs will be moved if the number is found

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Set up a virtual environment** (recommended):

    ```bash
    python3 -m venv env
    ```

3. **Activate the virtual environment**:

    - On **Windows**:

        ```bash
        .\env\Scripts\activate
        ```

    - On **macOS and Linux**:

        ```bash
        source env/bin/activate
        ```

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application**:

    ```bash
    python move_pdf_windows.py
    ```


## TESTEN


