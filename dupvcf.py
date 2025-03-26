import sys
import re
import base64

def clean_phone_number(phone):
    """Removes spaces and adds +91 to 10-digit numbers."""
    phone = re.sub(r'\s+', '', phone)
    if re.match(r'^\d{10}$', phone):
        return '+91' + phone
    return phone

def is_base64(s):
    """Checks if a string is Base64-encoded."""
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False

def validate_vcard(vcard_lines):
    """Validates if a vCard contains necessary fields."""
    has_version = any(line.startswith("VERSION:") for line in vcard_lines)
    has_fn = any(line.startswith("FN:") for line in vcard_lines)
    return has_version and has_fn

def process_vcard_line(line, debug):
    """Processes each line of a vCard, cleaning and extracting relevant data."""
    if "TEL" in line:
        phone = re.sub(r'[^0-9+]', '', line.split(':')[-1])
        phone = clean_phone_number(phone)
        return f"TEL;type=pref:{phone}", phone
    elif any(x in line for x in ["X-ADDRESSING-GRAMMAR", "PRODID", "REV", "CATEGORIES", "NOTE"]):
        return None, None  # Remove Apple-specific fields
    elif is_base64(line.split(':')[-1]):
        return None, None  # Remove Base64-encoded data
    return line, None

def remove_duplicate_vcards(input_file, output_file):
    """Cleans and deduplicates vCards based on phone numbers from an external file."""
    vcards = {}
    vcard = []
    current_key = None
    debug = True  # Enable debugging
    
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
            current_key = None
            if debug:
                print("Begin vCard")
        elif line.startswith("END:VCARD"):
            if debug:
                print("End vCard")
            if validate_vcard(vcard):
                key = current_key if current_key else "_NO_PHONE_" + str(len(vcards))
                vcards[key] = "\n".join(vcard)
        else:
            processed_line, phone = process_vcard_line(line, debug)
            if processed_line:
                vcard.append(processed_line)
            if phone and not current_key:
                current_key = phone
    
    if not vcards:
        print("No valid vCards found! Check input file format.")
    
    # Output unique vCards
    with open(output_file, "w", encoding="utf-8") as output_file:
        for vcard in vcards.values():
            output_file.write("BEGIN:VCARD\n" + vcard + "\nEND:VCARD\n")
    
    print(f"Processing complete. Cleaned vCards saved to {output_file}")



    # ------------------------------------------------------------------------



if __name__ == "__main__":
    
    input_file = "c:\\input.vcf"
    output_file = "c:\\cleaned_vcards.vcf"
    
    remove_duplicate_vcards(input_file, output_file)
