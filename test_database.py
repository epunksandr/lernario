from services import userrepo
from services import authentification_service

print("start")
authentification_service.login_user('stest123b@gmail.com', '12345678')
authentification_service.get_current_user()
userrepo.do()
print("asdf")