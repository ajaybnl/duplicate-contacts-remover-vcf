import sys
import re

def clean_phone_number(phone):
    """Removes spaces and adds +91 to 10-digit numbers."""
    phone = re.sub(r'\s+', '', phone)
    phone = re.sub(r'^\+91', '', phone)  # Remove existing +91
    if re.match(r'^\d{10}$', phone):
        return '+91' + phone
    return phone

def validate_vcard(vcard_lines):
    """Validates and ensures a vCard contains necessary fields."""
    has_version = any(line.startswith("VERSION:") for line in vcard_lines)
    has_fn = any(line.startswith("FN:") for line in vcard_lines)
    has_n = any(line.startswith("N:") for line in vcard_lines)
    
    if not has_version:
        vcard_lines.insert(1, "VERSION:3.0")
    if not has_fn:
        vcard_lines.insert(2, "FN:Unknown")
    if not has_n:
        vcard_lines.insert(3, "N:Unknown;;;;")
    
    return vcard_lines

def process_vcard_line(line):
    """Processes each line of a vCard, cleaning and extracting relevant data."""
    if "TEL" in line:
        phone = re.sub(r'[^0-9+]', '', line.split(':')[-1])
        phone = clean_phone_number(phone)
        return f"TEL;type=pref:{phone}", phone
    elif any(x in line for x in ["PRODID", "REV", "CATEGORIES"]):
        return None, None  # Remove non-essential fields
    return line, None

def remove_duplicate_vcards(input_file, output_file):
    """Cleans and deduplicates vCards based on phone numbers."""
    vcards = {}
    vcard = []
    phone_numbers = set()
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        return
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("BEGIN:VCARD"):
            vcard = []
            current_phone = None
        elif line.startswith("END:VCARD"):
            vcard = validate_vcard(vcard)  # Ensure required fields exist
            if current_phone and current_phone not in phone_numbers:
                phone_numbers.add(current_phone)
                vcards[current_phone] = "\n".join(vcard)
        else:
            processed_line, phone = process_vcard_line(line)
            if processed_line:
                vcard.append(processed_line)
            if phone:
                current_phone = phone
    
    if not vcards:
        print("No valid vCards found! Check input file format.")
    
    # Output unique vCards
    with open(output_file, "w", encoding="utf-8") as output_file:
        for vcard in vcards.values():
            output_file.write("BEGIN:VCARD\n" + vcard + "\nEND:VCARD\n")
    
    print(f"Processing complete. Cleaned vCards saved to {output_file}")

if __name__ == "__main__":
    input_file = "e:\\c.vcf"
    output_file = "e:\\cleaned_vcards.vcf"
    remove_duplicate_vcards(input_file, output_file)

