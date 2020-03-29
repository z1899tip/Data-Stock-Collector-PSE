#!/usr/bin/python

import os

import smtplib

import email

 

def send_automail(mail_name,stock_name,res,stat_res,set_price,cur_val,update_time):

 

    sender = 'stephenangelo.villanueva@toshiba.co.jp'

    receiver = [mail_name]

 

    message = """From: <Databot@toshiba.co.jp>

To:<{}>

MIME-Version: 1.0

Content-type: text/html

Subject: Notification (Stock Name: {})

 

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

    {} : {}

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

""".format(mail_name,stock_name,stock_name,res,stat_res,set_price,price_str,max_min_price,cur_val,update_time)

    host_f = "172.25.128.94"
    port_f = 25
    smtpObj = smtplib.SMTP()
    smtpObj.connect(host_f,port_f)       
    smtpObj.sendmail(sender, receiver, message)
    print ("Message Sent!")