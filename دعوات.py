import os
os.system("pip install amino.fix")
os.system("pip install amino.py")
import aminofix as amino
from  threading import Thread
import  requests,os
import timestamp
c=amino.Client()
c.login(email="2f34f17854@firemailbox.club",password="صادق99")
sid=c.sid
headers={
"NDCAUTH":f"sid={sid}",	"NDCDEVICEID":"52C182187C2E6AFABAA182670BB9B32D677C036AFC28C8854C08213C742CA1F2EDA846A0590C7D8EDE",
"content-type":"application/json; charset=utf-8"
	}
data = {"timestamp": int(timestamp()*1000)}
print(data)
u="http://aminoapps.com/p/egc7pc"
chatId=c.get_from_code(u).objectId
comId=c.get_from_code(u).path
comId = comId[1:comId.index('/')]
userIds=[]
userId=c.get_from_code(input('user link : ')). objectId
userId=userId
sub=amino.SubClient(comId,profile=c.profile)
U=Y=sub.get_online_users().userProfileCount
Y=sub.get_online_users(size=U).profile.userId
print(Y)
userIds.extend(Y)
def invite (comId,chatId,userId):
    url=f"https://service.narvii.com/api/v1/x{comId}/s/chat/thread/{chatId}/co-host/{userId}"
    req=requests.delete(url=url,headers=headers)
    if req.status_code==200:
        print("Done")
    if req.status_code!=200:
        print (req.text)
while True:
    for i in range (50):
        Thread(target=invite,args=(comId,chatId,userId)).start()
