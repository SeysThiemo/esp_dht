import yagmail

def send_email(sender="thiemoseys123@gmail.com" ,password="lookroker13" ,receiver="thiemo.seys@student.howest.be" ,subject="python_mail" ,message="mail from python script"):
        yag = yagmail.SMTP(sender,password)
        yag.send(
            to=receiver,
            subject=subject,
            contents=[message])
