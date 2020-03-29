from twilio.rest import Client
# import os
# import requests

#Ragnasav21@gmail.com
account_sid = 'AC1fd746fac0383ef6f7275985eb6a6444'
auth_token = '0a98c0a52b0882d31d457e9356a0525d'
From= "+12039042250"

#Sypdy0521@gmail.com
# account_sid = 'ACb11b941dee36537066a2671b3d3c3d3e'
# auth_token = '773bc8ea7efc8c341d7bb3c0530b44ff'
# From = "+12052559450"


# (stock_name=None,result_str=None,status_result=None,set_price=None,current_value=None,Update_time=None)

def sms_sender(stock_name,result_str,status_result,set_price,current_value,Update_time):
# def sms_sender():	
	From_= From
	To = "+639291267700"
	# To = "+639998997173"

	body = f"""
	{stock_name} as of {Update_time}
	{result_str}! 
	Current Value: {current_value}
	{status_result}: {set_price}


	"""

	client = Client(account_sid,auth_token)
	message = client.messages.create(body=body,from_= From_ ,to=To)