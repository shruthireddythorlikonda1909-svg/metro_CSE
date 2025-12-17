import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64

def generate_qr(data):
    qr=qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    return img
st.set_page_config(page_title="metro ticket booking")
st.title("Metro Ticket Booking System with QR code + Auto Voice")
stations=["AMEERPET","MIYAPUR","LB NAGAR","KPHB","JNTU"]
name=st.text_input("passenegr name")
source=st.selectbox("Source Station",stations)
destination=st.selectbox("destination station",stations)
no_tickets = st.number_input("Numberof tickets",min_value=1,value=1)
price_per_ticket=30
total_amount= no_tickets+ price_per_ticket
st.info(f"Total Amount: {total_amount}")
if st.button("Book Ticket"):
    if name.strip()=="":
        st.error("please enter passenger name.")
    elif source == destination:
        st.error("Source and destination cannot be the same")
    else:
        booking_id =str(uuid.uuid4())[:8]
        qr_data=(
            f"BookingID: {booking_id}\n"
            f"Name: {name}\n From :{source}\n To:{destination}\n tickets:{no_tickets}")
        qr_img=generate_qr(qr_data)
        buf =BytesIO()
        qr_img.save(buf , format="PNG")
        qr_bytes=buf.getvalue()
        st.write("Ticket Details")
        st.write("Booking ID:",booking_id)
        st.write("Passenger",name)
        st.write("from",source)
        st.write("to",destination)
        st.write("tickets",no_tickets)
        st.write("amount paid",total_amount)
        st.image(qr_bytes, width=250)
