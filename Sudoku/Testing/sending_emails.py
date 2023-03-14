import smtplib


my_email = "theopythontesting@gmail.com"
email_pw = "nfjhntyaixvzafhu"

with smtplib.SMTP("smtp.gmail.com") as connection: # saves having to do connection.close()
    connection.starttls()
    connection.login(user=my_email, password=email_pw)
    print("sending...")
    connection.sendmail(from_addr=my_email, 
        to_addrs="theomantelcooper@gmail.com",
        msg="Subject: Password code\n\nHello there. Your code is: 567891."
    )


print("Email has been sent")