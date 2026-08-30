import pandas as pd


def process_and_dispatch_billing():
    print("[BILLING AGENT] Initializing invoice workflow simulation...")

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

    print("\n=== STARTING NOTIFICATION SIMULATION ===")

    for _, row in df.iterrows():
        client_name = row["Client_Name"]
        client_email = row["Client_Email"]
        invoice_id = row["Invoice_ID"]
        amount_due = row["Amount_Due"]
        due_date = row["Due_Date"]
        status = row["Status"]

        if status == "Paid":
            print(
                f" -> [SKIPPED] {client_name} ({invoice_id}) - Account balance cleared ($0.00)."
            )
            continue

        if status == "Overdue":
            overdue_counter += 1
            subject = (
                f"URGENT NOTICE: Invoice {invoice_id} is OVERDUE - Action Required"
            )
            urgency_banner = "CRITICAL OVERDUE ALERT"
            closing_text = (
                "Please review the outstanding balance and follow your normal payment process."
            )
        else:
            subject = f"Invoice Reminder: {invoice_id} due by {due_date}"
            urgency_banner = "STANDARD PAYMENT REMINDER"
            closing_text = "Please ensure payment is processed on or before the due date."

        email_body = f"""
========================================================================
[NOTIFICATION SIMULATION] -> Would send to: {client_email}
Subject: {subject}
------------------------------------------------------------------------
Dear {client_name} Finance Team,

This is a simulated automated invoice notification.

[{urgency_banner}]
Invoice Reference: {invoice_id}
Total Amount Due : ${amount_due:,.2f}
Designated Due Date: {due_date}
Current Account Status: {status.upper()}

{closing_text}

This demo does not send real emails or contain real payment instructions.
========================================================================"""

        print(email_body)
        dispatch_counter += 1

    print("\n=== WORKFLOW SUMMARY ===")
    print(f"[SUMMARY] Notification drafts generated: {dispatch_counter}")
    print(f"[SUMMARY] High-priority overdue records: {overdue_counter}")
    print("[SUMMARY] Operational State: Complete.")


if __name__ == "__main__":
    process_and_dispatch_billing()
