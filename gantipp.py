from linepy import *
from akad.ttypes import *

print('[ DEBUG ] Starting Bot')

# choose your login method below by uncomment it

# client = LineClient(id='your_line_email@email.com', passwd='your_line_password') -> email & pass
# client = LineClient(authToken='using_token') -> token
# client = LineClient() -> QR (not working anymore)

client.log("Auth Token : " + str(client.authToken))
channel = LineChannel(client)

# object = LineObject(client) #this is for trial :3 ignore this

client.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(client)

print('[DEBUG] Bot Started ^_^')

print("****************Welcome*************")
print('Bot Name: Sb Simple')
print('Version: 1.2')
print('Codename: Adamantite Black')

while True:
	try:
		ops = poll.singleTrace(count=50)
		print("=-=-=-=-=-=-=-=-=---=-=-=-=-=-=-=-=-=\n")
		print(ops)
		print("=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		if ops != None:
			for op in ops:
				if op.type == 26 or op.type == 25:
					msg = op.message
					text = str(msg.text)
					msg_id = msg.id
					if msg.toType == 0: # bkn room
						receiver = msg._from
						sender = msg.to
					else:
						receiver = msg.to # room
						sender = msg._from
					try:
						if msg.contentType == 0:
							if msg.toType == 2 or 1 or 0:
								client.sendChatChecked(receiver, msg_id)
								contact = client.getContact(sender)
								if text.lower() == '/update': # you can change this command whatever you want :3
									client.sendMessage(receiver, "Proses...")

									# use video.mp4 file name for your video profile pic, or you can edit whatever you want
									client.updateProfileVideoPicture('video.mp4') 
									# this method above is in the /linepy/object.py file, you can edit image.png in the "path_p" variable whatever you want

									client.sendMessage(receiver,"Update Video Profile & Pict Success")
									client.sendMessage(receiver, "Terima Kasih Sudah Menggunakan Bot ini ^_^\n\n Created By: Altair (semara inc), Fhmisml, linepy")
					except Exception as d:
						print('[ERROR] You Got Error On Chat Bot Command Section :p')
						print(str(d))
				poll.setRevision(op.revision)
	except Exception as e:
		print('[ERROR] Well You Got Error On Your Bot -,-')
		print(str(e))
