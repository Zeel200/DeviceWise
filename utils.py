class User:
    def __init__(self, first_name, last_name, email, phone, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

    def save_tofile(self):
        line = self.first_name + ':' + self.last_name + ':' + self.email + ':' + self.phone + ':' + self.username + ':' + self.password
        with open("data/users.txt", mode="a") as f:
            f.write("\n"+line+"\n")
    

### THINGS TO BE ADD in FUTURE !important
## Password requirements (@zeel)
## Unique username (@zeel)


    
        

users_data = {}


def load_data():
    with open("data/users.txt") as f:
        data = f.read().splitlines()
    for row in data:
        if len(row.strip()) > 0:
            fName, lName, email, phone, username, password = row.split(':')
            # d = row.split(":")
            # username = d[0]
            # passwd = d[1]
            users_data[username] = User(fName, lName, email, phone, username, password)

def get_user(username):
    user = users_data.get(username, False)
    return user
def check_password(user, passwd) -> bool:
    return user.password == passwd