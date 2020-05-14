
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header


def send_automail(mail_name,stock_name,result_str,status_result,set_price,cur_val,update_time):

    #send via Gmail, replace None to your user and password

    user = None  
    password = None

    if None in (user,password):
      try:
        from Credential import email_credential
        user,password = email_credential()
      except ImportError as Ie:
        print("Please replace the None value in user and password variable to your gmail Credential")
        os.abort()


    sender = user
    receiver = mail_name

    mail = MIMEMultipart('alternative')
    mail['Subject'] = "Notification (Stock Name: {})".format(stock_name)
    mail['From'] = formataddr((str(Header('StockBot','utf-8')),sender))
    mail['To'] = ', '.join(receiver)

    message = """

</style>

<!--[if gte mso 9]><xml>

<o:shapedefaults v:ext="edit" spidmax="1026" />

</xml><![endif]-->

    <!--[if gte mso 9]><xml>

<o:shapelayout v:ext="edit">

<o:idmap v:ext="edit" data="1" />

</o:shapelayout></xml><![endif]-->

   </meta>

  </meta>

</head>

<body lang="EN-US" link="#0563C1" vlink="#954F72">

  <div class="WordSection1">

   <p class="MsoNormal">

    Hello!

    <o:p>

    </o:p>

   </p>

   <p class="MsoNormal">

    <o:p>

    </o:p>

   </p>

   <p class="MsoNormal">

   Stock Name: {}

    <o:p>

    </o:p>

   </p>

   <p class="MsoNormal">

    {}!

    <o:p>

    </o:p>

   </p>

   <p class="MsoNormal">

    <o:p>

    </o:p>

   </p>

   <p class="MsoNormal">

    {} Price: {}

    <o:p>

    </o:p>

   </p>

   <p class="MsoNormal">

    Current Value: {} As of {}

    <o:p>

    </o:p>

   </p>
   <p class="MsoNormal">
    <o:p>
    </o:p>
   </p>
   <p class="MsoNormal">
    Goodluck!
    <o:p>
    </o:p>
   </p>
   <p class="MsoNormal">
    <o:p>
    </o:p>
   </p>
   <p class="MsoNormal">
    <o:p>
    </o:p>
   </p>
  </div>
</body>
</html>

""".format(stock_name,result_str,status_result,set_price,cur_val,update_time)


#send via Gmail
    
    user = None
    password = None

    if None in (user,password):
      try:
        from Credential import email_credential
        user,password = email_credential()
      except ImportError as Ie:
        print("Please change the None value to your gmail Credential")

    html_in = MIMEText(message,'html')
    mail.attach(html_in)

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(user,password)     
    smtpObj.sendmail(sender, receiver, mail.as_string())
    smtpObj.quit()
    print ("Message Sent!")

