import os
import sys
import subprocess

# Ensure reportlab is installed
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
except ImportError:
    print("reportlab is not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle


def generate_receipt(receipt_data, file_name="payment_receipt.pdf"):
    # Create the PDF document
    pdf = SimpleDocTemplate(file_name, pagesize=A4)

    # Sample styles for the document
    styles = getSampleStyleSheet()
    elements = []

    # Title of the receipt
    title = Paragraph("Payment Receipt", styles['Title'])
    elements.append(title)

    # Add a space
    elements.append(Paragraph("<br/><br/>", styles['Normal']))

    # Transaction details
    transaction_details = [
        ["Transaction ID:", receipt_data['transaction_id']],
        ["Date:", receipt_data['date']],
        ["Amount:", f"${receipt_data['amount']}"],
        ["Payment Method:", receipt_data['payment_method']],
        ["Customer Name:", receipt_data['customer_name']],
        ["Customer Email:", receipt_data['customer_email']],
    ]

    # Create a table with the transaction details
    table = Table(transaction_details, colWidths=[2 * inch, 4 * inch])

    # Add style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Add the table to the PDF elements
    elements.append(table)

    # Final message
    elements.append(Paragraph("<br/><br/>Thank you for your payment!", styles['Normal']))

    # Build the PDF
    pdf.build(elements)
    print(f"Receipt generated: {file_name}")


# Input data from user
receipt_data = {
    "transaction_id": input("Enter Transaction ID: "),
    "date": input("Enter Date (YYYY-MM-DD): "),
    "amount": input("Enter Amount: "),
    "payment_method": input("Enter Payment Method: "),
    "customer_name": input("Enter Customer Name: "),
    "customer_email": input("Enter Customer Email: "),
}

# Generate the receipt
generate_receipt(receipt_data)