import pandas as pd
from datetime import datetime


def process_and_dispatch_billing():
    print("[BILLING AGENT] Initializing secure automated ledger scan...")

    # 1. Load corporate invoice database
    csv_file = "corporate_invoice_registry.csv"
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(
            f"[ERROR] Source ledger '{csv_file}' not found. Run 'invoice_ledger.py' first."
        )
        return

    dispatch_counter = 0
    overdue_counter = 0

    print("\n=== STARTING AUTOMATED EMAIL DISPATCH LIVE LOGS ===")

    # 2. Iterate through each client row dynamically
    for _, row in df.iterrows():
        client_name = row["Client_Name"]
        client_email = row["Client_Email"]
        invoice_id = row["Invoice_ID"]
        amount_due = row["Amount_Due"]
        due_date = row["Due_Date"]
        status = row["Status"]

        # 3. Smart Filtering: Skip completely paid accounts
        if status == "Paid":
            print(
                f" -> [SKIPPED] {client_name} ({invoice_id}) - Account Balance cleared ($0.00)."
            )
            continue

        # 4. Context Identification & Dynamic Templates (Unpaid vs Overdue)
        if status == "Overdue":
            overdue_counter += 1
            subject = (
                f"⚠️ UGENT NOTICE: Invoice {invoice_id} is OVERDUE - Action Required"
            )
            urgency_banner = "🚨 CRITICAL OVERDUE ALERT"
            closing_text = "Please note that persistent non-payment may impact your corporate service continuity. Kindly settle this amount immediately."
        else:
            subject = f"📄 Invoice Reminder: {invoice_id} due by {due_date}"
            urgency_banner = "📊 STANDARD PAYMENT REMINDER"
            closing_text = "We appreciate your partnership. Please ensure payment is processed on or before the due date."

        # 5. Smart Corporate HTML Email Body Mock Generation
        email_body = f"""
========================================================================
[SMTP DISPATCH OUTBOUND] -> Sending to: {client_email}
Subject: {subject}
------------------------------------------------------------------------
Dear {client_name} Finance Team,

This is an automated notification from our Enterprise Accounts Receivable System.

[{urgency_banner}]
Invoice Reference: {invoice_id}
Total Amount Due : ${amount_due:,.2f}
Designated Due Date: {due_date}
Current Account Status: {status.upper()}

{closing_text}

Secure Wire Transfer Details:
- Bank: International Corporate Trust Bank
- Routing Number: XXXXXXX89
- Account Number: XXXXXXXX4511

If payment has already been initiated, please reply directly to this email 
with the transaction receipt so our automated tracking engine can reconcile your ledger.

Sincerely,
Automated Financial Billing Agent
Afaq Corporate Solutions Ltd.
========================================================================"""

        print(email_body)
        dispatch_counter += 1

    print("\n=== DISPATCH ENGINE SUMMARY ===")
    print(f"[SUMMARY] Total Outbound Financial Emails Sent: {dispatch_counter}")
    print(f"[SUMMARY] High-Priority Overdue Alerts Issued : {overdue_counter}")
    print(f"[SUMMARY] Operational State: Idle.")


if __name__ == "__main__":
    process_and_dispatch_billing()
