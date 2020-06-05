from twilio.rest import Client 
from constants import messages
account_sid = '<from your twilio sandbox>' 
auth_token = '<frm your twilio sandbox' 
client = Client(account_sid, auth_token) 
count=0
increases= True

def sendText(): 
	global count
	message = client.messages.create( 
	                              from_='whatsapp:+<your twilio sandbox>',  
	                              body=messages[count],      
	                              to='whatsapp:+<subscribed member>' 
	                          ) 
	 
	print(message.sid)
	print(len(messages))
	
	global increases
	print(messages[count])
	if (count<(len(messages)-1) and increases):
		count+=1
	elif(count==(len(messages)-1)):
		increases=False
		count-=1
	elif(count>0 and not increases):
		count-=1
	elif(count==0):
		increases=True
		# print("Increased count")