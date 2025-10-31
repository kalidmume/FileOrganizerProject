# 🗂️ File Organizer – Basic Version

A simple Python script that automatically organizes all files in a folder into subfolders based on their file types (extensions). Perfect for keeping downloads, documents, and project folders neat and tidy.


---

## 📦 Features

Organizes files into folders by extension (.txt, .pdf, .jpg, etc.)

Works on any folder path you provide

Automatically creates subfolders for each file type (e.g., Files_txt, Files_pdf)

Moves files safely while keeping everything organized

Beginner-friendly and easy to run on Windows, Linux, or Android (Pydroid3/Termux)



---

### 🧑‍💻 Skills Demonstrated

File handling with Python (os, shutil)

Path and folder management

Automation scripting

Clean code practices



---

### 📁 Project Structure

FileOrganizerProject/
│
├── file_organizer_basic.py      # Main Python script
├── README.md                    # Project guide (this file)
│
├── 📁 sample_folder/            # Example files to test
│   ├── notes.pdf
│   ├── image.jpg
│   ├── report.docx
│   └── data.csv
│
└── 📁 output_folder/            # Organized files (created automatically)


---

## ⚙️ How It Works (Step by Step)

1️⃣ Select folder path
The script asks you:

Enter your folder path:

→ Type the folder you want to organize.

2️⃣ Check if folder exists

If the folder doesn’t exist → an error is shown, and the script stops.


3️⃣ List all files

The script goes through every item in the folder.


4️⃣ Check if it’s a file

Only files are moved; folders are skipped.


5️⃣ Get file extension

Example: notes.pdf → extension is pdf.


6️⃣ Create folder for extension

Creates folders like Files_pdf or Files_jpg.

If the folder already exists → no problem.


7️⃣ Move files

Moves each file to its corresponding folder.

Errors are handled gracefully.


8️⃣ Print confirmation

Moved notes.pdf -> Files_pdf

Lets the user know everything is done.


9️⃣ Finish

File organization complete ✅


---

## 🖼️ Sample Demo

Before running the script:

Documents/
 ├── test.txt
 ├── image.jpg
 └── notes.pdf

After running the script:

Documents/
 ├── Files_txt/test.txt
 ├── Files_jpg/image.jpg
 └── Files_pdf/notes.pdf
## 🚀 How to Run

Option 1 — Run directly

python file_organizer_basic.py

Then enter your folder path when prompted.

Option 2 — Run with default folder
Edit the script line:

folder = input("Enter your folder path: ")

to:

folder = "Documents"

Then run the script.


### 🧰 Requirements

Python 3.x

Works on Windows, Linux, Android 


### Move vs Copy

By default, the script **moves files**:

```python
shutil.move(file_path, dst_path)

To keep the original files, use:

shutil.copy(file_path, dst_path)
### 🧩 Notes

This version moves files by default.

To copy files instead (keep originals untouched), replace:


shutil.move(file_path, dst_path)

with:

shutil.copy(file_path, dst_path)

Can be upgraded to Standard/Pro versions:

Standard: Logging, error handling, and configuration

Pro: Undo function, CLI support, and category grouping

###  Bonus Tips for Clients

Works with any folder (Documents, Downloads, Projects)

Can be packaged with sample_folder and README for easy distribution

### 🧑‍💻 Created By

KalidCode –  Python Freelancer

Focused on easy-to-use, client-ready automation script