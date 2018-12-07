import requests
class Validator:
    def __init__(self):
        pass
    def validate(self, token):
        #The auth token comes from Hoogle auth, a service that can be used by installing the Hoogle system at https://github.com/naclcaleb/Hoogle
        data = requests.get("http://localhost/hoogle/auth/validatetoken.php?token=" + token).json()
        if data["status"] == "success":
            return True
        else:
            return False

        
