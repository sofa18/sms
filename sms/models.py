from django.db import models

from twilio.rest import Client

# TIP: to comment out multiple lines, highlights everything
# then press command / aka ?


# Create your models here.
# this is where you edit/add code


# from twilio.rest import Client
# # Your Account SID from twilio.com/console
# account_sid = "AC241a59d7708d3b81f149d3467ed6545f"
# # Your Auth Token from twilio.com/console
# auth_token  = "a9f282be7cfc4b61b8b2243c8a2f5bba"
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     to="+17874262186", 
#     from_="+13214148051",
#     body="Hello from Python!")
# print(message.sid)

# to RUN:
# python manage.py makemigrations
# python manage.py makemigrations
# "python manage.py shell"
# then said "from sms.models import User"
# then "User.text_user('','7874262186')
# gives u this: SMce0af4f9bcb4401a841de1a6441d06c7

class User(models.Model):
	name = models.CharField(max_length=150, null=True)
	pin = models.IntegerField(max_length=6)
	cell = models.IntegerField(max_length=9)

	def text_user(self, phone):
		account_sid = "AC241a59d7708d3b81f149d3467ed6545f"
		auth_token  = "a9f282be7cfc4b61b8b2243c8a2f5bba"
		client = Client(account_sid, auth_token)
		message = client.messages.create(
			#to="+17874262186", 
			to=phone,
			from_="+13214148051",
			body="Hello from Python!")
		print(message.sid)









