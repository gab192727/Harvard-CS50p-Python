from fpdf import FPDF

def create_text_in_shirt(text):
    fpdf = FPDF(orientation="P", unit="mm", format='A4')
    fpdf.set_auto_page_break(auto=False)
    fpdf.add_page()
    fpdf.set_font("helvetica", "B", 45)
    fpdf.set_text_color(0, 0, 0)
    fpdf.set_xy(0, 10)
    fpdf.text(45, 45, "CS50 Shirtificate")
    fpdf.image("shirtificate.png", 10, 65, 190, 190)
    text_width = fpdf.get_string_width(text)
    x_coordinate = (210 - text_width) / 2
    fpdf.set_xy(x_coordinate, 140)
    fpdf.set_font("helvetica", "B", 25)
    fpdf.set_text_color(255, 255, 255)
    fpdf.text(x_coordinate, 140, f"{text}")
    fpdf.output("shirtificate.pdf")


create_text_in_shirt(input("Name: "))
