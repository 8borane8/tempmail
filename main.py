import requests

def getApiUrl():
    return "https://www.1secmail.com/api/v1"

class TempMail:
    def __init__(self):
        self.refreshMail()

    def refreshMail(self):
        self.mail = requests.get(getApiUrl() + "?action=genRandomMailbox&count=1").json()[0]

    def getAllMessages(self):
        return requests.get(getApiUrl() + "?action=getMessages&login="+self.mail.split("@")[0]+"&domain="+self.mail.split("@")[1]).json()

    def getMessage(self, id):
        return requests.get(getApiUrl() + "?action=readMessage&login="+self.mail.split("@")[0]+"&domain="+self.mail.split("@")[1] + "&id=" + str(id)).json()

    def downloadAttachment(self, id, filename, destination):
        with requests.get(getApiUrl() + "?action=download&login="+self.mail.split("@")[0]+"&domain="+self.mail.split("@")[1] + "&id="+str(id)+"&file=" + filename, stream=True) as r:
            r.raise_for_status()
            with open(destination, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
