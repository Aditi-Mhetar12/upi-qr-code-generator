import qrcode

upi_id=input("Enter your UPI ID :")

phonepe=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
gpay=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

phonepe_qr=qrcode.make(phonepe)
paytm_qr=qrcode.make(paytm)
gpay_qr=qrcode.make(gpay)

phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
gpay_qr.save("gpay_qr.png")

phonepe_qr.show()
paytm_qr.show()
gpay_qr.show()