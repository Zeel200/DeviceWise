class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    

    
        

users_data = {}


def load_data():
    with open("data/users.txt") as f:
        data = f.read().splitlines()
    for row in data:
        username, passwd = row.split(':')
        # d = row.split(":")
        # username = d[0]
        # passwd = d[1]
        users_data[username] = User(username, passwd)

def get_user(username):
    user = users_data.get(username, False)
    return user
def check_password(user, passwd) -> bool:
    return user.password == passwd