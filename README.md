# 📇 Duplicate Contacts Remover (VCF)

A Python script to clean and deduplicate contacts from `.vcf` (vCard) files, ensuring a well-organized contact list.

## 🚀 Features
- Removes duplicate contacts by matching phone numbers.
- Cleans and formats phone numbers (adds `+91` for 10-digit numbers, removes spaces).
- Ensures required fields (`VERSION`, `FN`, `N`) exist in each vCard.
- Keeps only one entry for duplicate contacts.
- Works with large `.vcf` files efficiently.

## 🔧 Usage
### Running the Script via Thonny IDE
1. Open **Thonny IDE** on your system.
2. Click on **File > Open** and select `dupvcf.py`.
3. Modify the input and output file paths if needed (default: `c:\contact_vcards.vcf` → `c:\cleaned_vcards.vcf`).
4. Click **Run** or press `F5` to execute the script.

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
TEL;TYPE=HOME:9871543210
END:VCARD

BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL;TYPE=WORK:9871543210
END:VCARD
```

**After Cleaning:**
```
BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL;TYPE=PREF:+919871543210
END:VCARD
```

## 🤝 Contributing
Feel free to submit pull requests or report issues to improve the script!

## 📜 License
This project is open-source and available under the MIT License.

