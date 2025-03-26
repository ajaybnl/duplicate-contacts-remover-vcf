# 🚀 **Duplicate Contacts Remover (VCF) - Now Available!**  

Tired of messy contact lists with duplicate entries? Our **Python-based vCard Cleaner** is here to help! 🧹✨  

🔹 **Features:**  
✅ Removes duplicate contacts based on phone numbers  
✅ Cleans & formats numbers automatically (+91 for 10-digit numbers)  
✅ Merges duplicate contacts, even if fields are reordered  
✅ Eliminates duplicate phone numbers within the same contact  
✅ Works with **iCloud, Google Contacts, and Android vCards**  

🔹 **How to Use?**  
1️⃣ Export your contacts as a `.vcf` file  
2️⃣ Run the script in **Thonny IDE** or Python  
3️⃣ Import the cleaned `.vcf` back to your phone or iCloud  

🔹 **Example Fix:**  
Before: Multiple contacts for **Scarlet Johansan** with different formats  
After: **One clean contact with a properly formatted number!**  


## 🔧 Usage
### Running the Script via Thonny IDE
1. Open **Thonny IDE** on your system.
2. Click on **File > Open** and select `dupvcf.py`.
3. Modify the input and output file paths if needed (default: `e:\c.vcf` → `e:\cleaned_vcards.vcf`).
4. Click **Run** or press `F5` to execute the script.

### Or Run it with python.exe
Install python, run with command line. 


The script will process the `.vcf` file and remove duplicate contacts automatically.

## 🛠 How It Works
1. Reads `.vcf` file and extracts contacts.
2. Cleans and standardizes phone numbers.
3. Removes duplicate contacts by checking phone numbers.
4. Writes the cleaned contacts to a new `.vcf` file.

## 📂 Example
**Before Cleaning:**
```
BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL;TYPE=HOME:9876543210
END:VCARD

BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL;TYPE=WORK:9876543210
END:VCARD
```

**After Cleaning:**
```
BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL;TYPE=PREF:+919876543210
END:VCARD
```

## 🌐 Cleaning iPhone / Google Contacts Duplicate Contacts
Follow these steps to clean duplicate contacts on iPhone using iCloud:

1. **Export Contacts from iCloud / Google Contacts:**
   - Go to [iCloud Contacts](https://www.icloud.com/contacts/). 
   - Press `Ctrl + A` (Windows) or `Cmd + A` (Mac) to select all contacts.
   - Click on the **gear icon** at the bottom left and select **Export vCard**.
   - Save the `.vcf` file to your computer.

2. **Remove Duplicates with the Script:**
   - Run the `dupvcf.py` script in Thonny as described above.
   - The cleaned `.vcf` file will be saved as `e:\cleaned_vcards.vcf`.


## MAKE SURE YOU HAVE THE BACKUP FILE!!!

3. **Delete All Contacts from iCloud:**
   - Go to [iCloud Contacts](https://www.icloud.com/contacts/).
   - Select all contacts and click **Delete**.
   - Confirm deletion.

4. **Re-Import Cleaned Contacts:**
   - Click the **gear icon** and select **Import vCard**.
   - Choose `cleaned_vcards.vcf` and upload it.

Your iPhone will now sync with the updated contacts automatically.

## 🤝 Contributing
Feel free to submit pull requests or report issues to improve the script!

## 🐜 License
This project is open-source and available under the MIT License.

