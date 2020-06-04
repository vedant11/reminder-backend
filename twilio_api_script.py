from twilio.rest import Client 
 
account_sid = 'Enter your account_sid here' 
auth_token = 'auth_token here' 
client = Client(account_sid, auth_token) 
def sendText(): 
	message = client.messages.create( 
	                              from_='<Enter number here from twilio sandbox>',  
	                              body='<reminder body>',      
	                              to='whatsapp:<number registered with the sandbox>' 
	                          ) 
	 
	print(message.sid)
