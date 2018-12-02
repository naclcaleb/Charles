from passlib.hash import pbkdf2sha256
class Validator:
    def __init__(self):
        pass
    def validate(self, token):
        valid_tokens = []
        with open("tokens.txt","r") as file:
            txt = file.read()
            valid_tokens = txt.split("\n")
            
        
            
        if token in valid_tokens:
            return True
        else:
            return False
