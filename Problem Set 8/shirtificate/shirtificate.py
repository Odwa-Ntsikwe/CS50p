from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 45)
pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.image("shirtificate.png", w=pdf.epw)
pdf.set_font_size(30)
pdf.set_text_color(255, 255, 255)
pdf.text(x=45, y=140, text=f"{name} took CS50")
pdf.output("shirtificate.pdf")
