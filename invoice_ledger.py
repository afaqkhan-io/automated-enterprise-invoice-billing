import pandas as pd


def generate_invoice_data():
    """Simulates a secure corporate accounts receivable ledger for outstanding dues"""
    invoice_records = [
        {
            "Invoice_ID": "INV-2026-001",
            "Client_Name": "Acme Tech Solutions",
            "Client_Email": "billing@acmetech.com",
            "Amount_Due": 4500.00,
            "Due_Date": "2026-09-05",
            "Status": "Unpaid",
        },
        {
            "Invoice_ID": "INV-2026-002",
            "Client_Name": "Stark Global Industries",
            "Client_Email": "finance@starkind.com",
            "Amount_Due": 12500.50,
            "Due_Date": "2026-08-20",
            "Status": "Overdue",
        },
        {
            "Invoice_ID": "INV-2026-003",
            "Client_Name": "Wayne Enterprises",
            "Client_Email": "accounts@waynecorp.com",
            "Amount_Due": 8900.00,
            "Due_Date": "2026-09-10",
            "Status": "Unpaid",
        },
        {
            "Invoice_ID": "INV-2026-004",
            "Client_Name": "Cyberdyne Systems",
            "Client_Email": "payments@cyberdyne.co",
            "Amount_Due": 3200.25,
            "Due_Date": "2026-08-15",
            "Status": "Overdue",
        },
        {
            "Invoice_ID": "INV-2026-005",
            "Client_Name": "Oscorp Industries",
            "Client_Email": "treasury@oscorp.org",
            "Amount_Due": 0.00,
            "Due_Date": "2026-08-25",
            "Status": "Paid",
        },
    ]

    df = pd.DataFrame(invoice_records)
    output_csv = "corporate_invoice_registry.csv"
    df.to_csv(output_csv, index=False)
    print(f"[LEDGER PIPELINE] Secure financial database written to '{output_csv}'")


if __name__ == "__main__":
    generate_invoice_data()
