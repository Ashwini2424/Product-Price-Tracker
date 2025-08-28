import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


EMAIL_ADDRESS = "Your@gmail.com"
EMAIL_PASSWORD = "Your app password"   

def send_email(product_title, product_price, product_url):
    try:
    
        subject = f"Price Drop Alert: {product_title}"
        body = f"""
        Good news! The price dropped for:
        
        Product: {product_title}
        Current Price: ₹{product_price}
        Link: {product_url}
        """

     
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS  
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

     
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(" Email sent successfully!")

    except Exception as e:
        print(f" Email failed: {e}")
