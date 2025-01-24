# Re-creating the table structure from the second document and accurately inserting the data from the first document
from docx import Document

# Load the second document where the changes need to be made
doc = Document(second.docx)

# Mapping of values for each section
background_of_negotiation = [
    "This is a negotiation between your team (a project management team) and a supplier team regarding the terms of an ongoing supply agreement for crucial project materials.",
    "- YOU/Your Team: Project Management Team",
    "- Team Members: [List of your team members]",
    "- Context: Your team needs to negotiate terms for a new contract with a supplier for materials critical to your project.",
    "- Other Party/Other Team: Supplier Team",
    "- Team Members: [List of their team members]",
    "- Context: The supplier is negotiating to maintain or adjust current terms due to increasing costs and logistical challenges but is still keen to retain the business relationship."
]

issues = ["Pricing", "Delivery Timeline", "Quality Standards", "Penalties", "Contract Length"]
your_position = [
    "Cap price per unit at $50, no increase for first year",
    "Deliver within 30 days of order",
    "No more than 1% defect rate, must meet ISO standards",
    "5% of total order value per week of delay",
    "Fixed 18-month term with option to extend"
]
other_party_position = [
    "Requesting $55 per unit due to increased costs",
    "Requesting 45 days due to logistical issues",
    "Requesting 2% defect rate to reduce quality costs",
    "Requesting lower penalties (2-3%)",
    "Requesting 12 months citing market volatility"
]

rank_order = ["1. Quality Standards", "2. Pricing", "3. Delivery Timeline", "4. Penalties", "5. Contract Length"]
reservation_price = [
    "Willing to go up to $52 per unit",
    "Accept up to 40 days",
    "Accept a 1.5% defect rate if it doesn’t compromise project",
    "Minimum 3% penalty per week of delay",
    "Minimum 12 months with review at 9 months"
]
batna = [
    "Switch to another supplier if quality can’t be met",
    "Source from another supplier",
    "Temporary supply agreements for immediate needs",
    "Use internal resources for delays if penalties are too lenient",
    "Consider shorter terms with other suppliers"
]

# Updating the relevant sections of the second document's table with these values
table = doc.tables[0]

# Updating Background of the Negotiation
table.cell(1, 0).text = "\n".join(background_of_negotiation)

# Updating Issues and Positions
table.cell(3, 0).text = "\n".join(issues)
table.cell(3, 1).text = "\n".join(your_position)
table.cell(3, 2).text = "\n".join(other_party_position)

# Updating Rank Order, Reservation Price, and BATNA
table.cell(5, 0).text = "\n".join(rank_order)
table.cell(7, 0).text = "\n".join(reservation_price)
table.cell(9, 0).text = "\n".join(batna)

# Save the modified document
output_doc_path = "/mnt/data/Updated_Negotiation_Planning_Document_Formatted.docx"
doc.save(output_doc_path)

output_doc_path  # Return the path of the updated document
