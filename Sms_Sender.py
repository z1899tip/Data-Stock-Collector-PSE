from twilio.rest import Client
import os

#Need to replace all None with Twilio generated account.
account_sid = None 
auth_token = None
From = None
To = None

if None in (account_sid,auth_token,From,To):
	try:
		from Credential import my_twilio_credential
		account_sid,auth_token,From,To = my_twilio_credential()
	except ImportError as Ie:
		print(Ie, 'This module is for my personal use to hide all my twilio credentials.')
		print("Please create your twilio account and fill up above variable with your account_sid, auth_token and twilio generated phone number.")
		os.abort()

def sms_sender(stock_name,result_str,status_result,set_price,current_value,Update_time):
	From_= From
	To_ = To 


	body = f"""
	Stock Name: {stock_name} 
	{result_str}! 
	Current Value: {current_value}
	{status_result}: {set_price}
	as of {Update_time}

	"""

	client = Client(account_sid,auth_token)
	message = client.messages.create(body=body,from_= From_ ,to=To_)


