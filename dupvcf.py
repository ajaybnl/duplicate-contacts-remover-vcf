import re


def clean_phone_number(phone):
    """Removes spaces and adds +91 to 10-digit numbers."""
    phone = re.sub(r'\s+', '', phone)  # Remove spaces
    if re.match(r'^\d{10}$', phone):  # If exactly 10 digits, add +91
        return '+91' + phone
    return phone


def normalize_vcard(vcard):
    """Extracts and normalizes key information from a vCard."""
    phone_numbers = set()
    cleaned_vcard = []
    fn_name = ""

    for line in vcard:
        if line.startswith("TEL"):
            phone = re.sub(r'[^0-9+]', '', line.split(':')[-1])  # Extract numbers only
            phone = clean_phone_number(phone)  # Normalize phone format
            if phone not in phone_numbers:
                phone_numbers.add(phone)
                cleaned_vcard.append(f"TEL;TYPE=PREF:{phone}")
        elif line.startswith("FN:"):
            fn_name = line.split("FN:")[-1]  # Extract Full Name
            cleaned_vcard.append(line)
        elif line.startswith("N:"):
            cleaned_vcard.append(line)
        elif not line.startswith(("NOTE", "PRODID", "REV", "CATEGORIES")):  # Remove Apple-specific fields
            cleaned_vcard.append(line)

    return fn_name, phone_numbers, cleaned_vcard


def remove_duplicate_vcards(input_file, output_file):
    """Removes duplicate vCards based on phone numbers."""
    unique_contacts = {}
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        return
    
    vcard = []
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("BEGIN:VCARD"):
            vcard = []
        elif line.startswith("END:VCARD"):
            if vcard:
                fn_name, phone_numbers, cleaned_vcard = normalize_vcard(vcard)
                if phone_numbers:
                    key = tuple(sorted(phone_numbers))  # Use phone numbers as unique key
                    if key not in unique_contacts:
                        unique_contacts[key] = cleaned_vcard
        else:
            vcard.append(line)

    if not unique_contacts:
        print("No valid vCards found! Check input file format.")
    
    with open(output_file, "w", encoding="utf-8") as output_f:
        for vcard in unique_contacts.values():
            output_f.write("BEGIN:VCARD\n" + "\n".join(vcard) + "\nEND:VCARD\n")
    
    print(f"Processing complete. Cleaned vCards saved to {output_file}")


if __name__ == "__main__":
    input_vcf = "e:\\c.vcf"
    output_vcf = "e:\\cleaned_vcards.vcf"
    remove_duplicate_vcards(input_vcf, output_vcf)

