# 💳 Credit Card Statement Parser

A simple web application built with **Python**, **Streamlit**, and **pdfplumber** to parse credit card statements.

This system allows users to:

- Upload any PDF credit card statement.
- Parse the statement for key data points using regex.
- Display the extracted data in a clean, user-friendly dashboard.

---

## 🔧 Tech Stack

- **Python**
- **Streamlit** (for the web UI)
- **pdfplumber** (for PDF text extraction)
- **re** (Python's regex module for parsing)



## 📊 Extracted Data Points

This application parses the PDF to find and display the following **6 key data points**:

| Data Point | Description |
|-------------|-------------|
| **Bank Name** | Identifies the bank (e.g., "SBI Bank", "HDFC Bank"). |
| **Card (Last 4 Digits)** | The last four digits of the card number. |
| **Total Amount Due** | The total outstanding bill amount. |
| **Payment Due Date** | The deadline for the payment. |
| **Statement Date** | The date the statement was generated. |
| **Statement Period** | The billing cycle for the statement. |

---

## 🛠️ Run Locally

### 1. Clone the project

```bash
git clone https://github.com/Jainam-Shah17/Credit-Card-Statement-Parser.git
```

### 2. Go to the project directory

```bash
cd Credit-Card-Statement-Parser
```

### 3. Install dependencies
This project uses pip and a requirements.txt file.

```bash
pip install -r requirements.txt
```

### 4. Start the server
This will start the Streamlit web application.

```bash
streamlit run app.py
```

## ✍️ Author

- GitHub: [@Jainam-Shah17](https://github.com/Jainam-Shah17/)
