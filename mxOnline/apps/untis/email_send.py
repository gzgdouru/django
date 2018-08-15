import string, random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from mxOnline.settings import DEFAULT_FROM_EMAIL

def random_str(randomLenght=8):
    chars = string.ascii_letters + string.digits
    length = len(chars) - 1
    outStr = ""
    for i in range(randomLenght):
        outStr += chars[random.randint(0, length)]
    return outStr

def send_register_email(email, sendType="register"):
    emailRecord = EmailVerifyRecord()
    emailRecord.code = random_str(16)
    emailRecord.email = email
    emailRecord.send_type = sendType
    emailRecord.save()

    if sendType == "register":
        emailTitle = "慕学在线网注册激活链接"
        emailBody = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/users/active/{}".format(emailRecord.code)
    else:
        emailTitle = "慕学在线网密码重置链接"
        emailBody = "请点击下面的链接重置你的密码: http://127.0.0.1:8000/users/reset/{}".format(emailRecord.code)

    status = send_mail(emailTitle, emailBody, DEFAULT_FROM_EMAIL, [email])

