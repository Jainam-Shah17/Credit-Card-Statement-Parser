import pdfplumber
import re
import json

BANK_PATTERNS = {
    "Axis Bank": r"Axis Bank",
    "HDFC Bank": r"HDFC Bank|HDFC",
    "ICICI Bank": r"ICICI Bank",
    "SBI Bank": r"SBI Card|SBI|State Bank of India",
    "Kotak Bank": r"Kotak Mahindra Bank|Kotak Bank|Kotak",
}

def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            first_page = pdf.pages[0]
            return first_page.extract_text()
    except Exception as e:
        print(f"Error reading PDF file at {pdf_path}: {e}")
        return None

def parse_statement(text, bank_patterns):
    data = {
        "bank_name": None,
        "card_last_4": None,
        "statement_period": None,
        "statement_date": None, # <-- ADDED THIS LINE
        "due_date": None,
        "total_due": None
    }
    
    card_pattern = re.search(r"Card Number:.*?(?:(?:XXXX-){3}|(?:\d{4}-){3})(\d{4})", text, re.IGNORECASE)
    
    period_pattern = re.search(r"Statement Period:\s*(\d{2}/\d{2}/\d{4}\s*-\s*\d{2}/\d{2}/\d{4})", text)
    
    statement_date_pattern = re.search(r"Statement Date:\s*(\d{2}/\d{2}/\d{4})", text)

    due_date_pattern = re.search(r"Payment Due Date:\s*(\d{2}/\d{2}/\d{4})", text)

    total_due_pattern = re.search(r"Total Amount Due\s*Rs\. ([\d,]+\.\d{2})", text)

    text_lower = text.lower()
    for standardized_name, pattern in bank_patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            data["bank_name"] = standardized_name
            break
            
    if card_pattern:
        data["card_last_4"] = card_pattern.group(1)
        
    if period_pattern:
        data["statement_period"] = period_pattern.group(1)

    if statement_date_pattern:
        data["statement_date"] = statement_date_pattern.group(1)
        
    if due_date_pattern:
        data["due_date"] = due_date_pattern.group(1)
        
    if total_due_pattern:
        amount_str = total_due_pattern.group(1)
        data["total_due"] = float(amount_str.replace(",", ""))
    return data

if __name__ == "__main__":
    
    pdf_file_path = 'Kotak_Bank.pdf' 
    
    full_text = extract_text_from_pdf(pdf_file_path)
    
    if full_text:
        parsed_data = parse_statement(full_text, BANK_PATTERNS)

        if parsed_data:
            print("--- Successfully Parsed Data ---")
            print(json.dumps(parsed_data, indent=2))
            print("---------------------------------")
            
    else:
        print(f"Could not extract text from {pdf_file_path}")
