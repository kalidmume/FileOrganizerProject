#get module
import os, shutil
# Step 1: Select the folder path
folder = input("Enter your folder path: ")
#check if folder exists
if not os.path.exists(folder):
   print(f"Error: folder '{folder}' not found ")
   exit()
# Step 2: List all files in that folder
for file in os.listdir(folder):
# Step 3: Check each item → if it's a file
  file_path = os.path.abspath(os.path.join(folder, file))
  if os.path.isfile(file_path):
# Step 4: Get file extension (like .pdf, .jpg)
    name, ext = os.path.splitext(file)
# Step 5: Create a folder for that extension if not exists
    ext = ext.replace(".", "") or "no_ext,"
    dst_path = os.path.abspath(os.path.join(folder, f"Files_{ext}"))
    os.makedirs(dst_path, exist_ok=True)
# Step 6: Move the file to that folder and handling error 
    try:
        shutil.move(file_path, dst_path )
    except Exception as error:
        print(f"Error: {error}")
# Step 7: Print confirmation for each moved file
    print(f"Moved {file} -> {dst_path}")
print("File organization complate ✅️")