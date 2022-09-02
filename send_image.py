import requests
import base64

with open("1.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
#“image”: base64 encoded image.
#r = requests.post("http://bugs.python.org", data={'number': '12524', 'type': 'issue', 'action': 'show'})
#r = requests.post("https://w4fk1dhnfi.execute-api.eu-west-1.amazonaws.com/", data={"authsecret":'ufzapoxnuygrz^paoiuzauyzgvejqkjqbctcrapdmsdkfh',"image":str(encoded_string)})
r = requests.post("https://w4fk1dhnfi.execute-api.eu-west-1.amazonaws.com/", data={"authsecret":'ufzapoxnuygrz^paoiuzauyzgvejqkjqbctcrapdmsdkfh'})

print(r.status_code, r.reason)
print(r.text)
