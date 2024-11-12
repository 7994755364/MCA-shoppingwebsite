import numpy as np
from fpdf import FPDF


class make_pdf:
    def __init__(self, data1, data2):
        self.order_id=data2['order_id']
        self.date=data2['date']
        self.shop_name=data2['name']
        self.phone=data2['phone']
        self.email=data2['email']
        self.total=data2['total']
        self.disc=data2['savings']
        self.payable=data2['payable']
        self.data1=data1

    def start_Create(self):
        pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
        pdf.add_page()

        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(255, 0, 0)
        pdf.set_font_size(20)
        pdf.text(70, 20, "PAYMENT REPORT")     # heading


        pdf.set_text_color(0, 0, 0)
        pdf.set_font_size(18)
        pdf.text(20, 40, "ORDER DETAILS")     # heading

        pdf.set_text_color(0, 0, 0)
        pdf.set_font_size(14)
        pdf.text(20, 50, "ORDER NUMBER : ")     # TEXT
        pdf.text(65, 50, self.order_id)     # heading
        pdf.text(148, 50, "DATE : ")     # heading
        pdf.text(165, 50, self.date)     # heading


        pdf.set_text_color(0, 0, 0)
        pdf.set_font_size(18)
        pdf.text(20, 70, "SHOP DETAILS")     # heading

        pdf.set_font_size(14)
        pdf.text(20, 80, "Shop Name : ")     # heading
        pdf.text(65, 80, self.shop_name)     # heading
        pdf.text(20, 90, "Phone Number : ")     # heading
        pdf.text(65, 90, self.phone)     # heading
        pdf.text(20, 100, "Email Id : ")     # heading
        pdf.text(65, 100, self.email)     # heading

        pdf.set_text_color(0, 0, 0)
        pdf.set_font_size(16)
        pdf.text(20, 120, "Total Amount:")
        pdf.text(65, 120, str(self.total))

        pdf.text(20, 130, "Total Discount:")
        pdf.text(65, 130, str(self.disc))

        pdf.text(20, 140, "Bill Amount:")
        pdf.text(65, 140, str(self.payable))

        pdf.set_text_color(150, 0, 0)
        pdf.set_font_size(18)
        pdf.text(30, 155, "ITEMS")

        pdf.set_text_color(0, 0, 0)
        pdf.set_font_size(14)
        pdf.text(10, 165, "SL.NO ")
        pdf.text(30, 165, "PRODUCT")
        pdf.text(78, 165, "PRICE")
        pdf.text(98, 165, "QUANTITY")
        pdf.text(128, 165, "AMOUNT")
        pdf.text(155, 165, "DISCOUNT")
        pdf.text(185, 165, "PAYABLE")
        pdf.set_font_size(12)
        x=175
        cnt=1
        print("helllooooo   \n",self.data1)
        for i in self.data1:
            pdf.text(12, x, str(cnt))
            pdf.text(32, x, i['product_name'])
            pdf.text(80, x, i['product_price'])
            pdf.text(100, x, i['product_quantity'])
            pdf.text(130, x, str(i['amount']))
            pdf.text(157, x, str(i['disc']))
            pdf.text(187, x, str(i['offer_amount']))
            x=x+10
            cnt+=1

        pdf.output("E:\\New folder\\sample\\samples\\media\\bills_"+self.order_id+".pdf")
        return "ok"




# pdf.set_xy(x, y)
# pdf.cell(w, h, txt, border, align, fill)

