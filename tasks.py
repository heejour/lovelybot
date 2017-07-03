from microsoftbotframework import ReplyToActivity
import requests

def echo_response(message):
  if message["type"] == "message":
    ReplyToActivity(fill=message,
                    text=message["text"]).send()

def bit_response():
  ct = bit_contact()
  if message["type"] == "message":
    if message["text"] == "bitcoin"
      ReplyToActivity(fill=message,
                      text=ct).send()
    else:
      ReplyToActivity(fill=message,
                      text=message["text"]).send()
      
def bit_contact():
  res = requests.get("https://api.korbit.co.kr/v1/ticker")
  t = str(res.text)
  res_dict = eval(t)
  
  last = res_dict.get('last')
  ct = "last cost : {}".format(last)
  
  print (ct)
  return ct
