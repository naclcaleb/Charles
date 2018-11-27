import urllib2

class NetworkCheck:
    def __init__(self, ip='google.com'):
        self.ip = ip
    def check(self):
        try:
            print("https://" + self.ip)
            urllib2.urlopen('https://' + self.ip, timeout=1)
            return True
        except urllib2.URLError as err:
            return False
nc = NetworkCheck()
nc.check()
