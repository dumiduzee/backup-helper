from .exceptions import UnauthorizedKey
from .repo import get_user_repo

#login sevice
def login_service(key,db):
    #check the key in database
    result = get_user_repo(key=key,db=db)
    if result is None:
        #user not have invalid key situation
        raise UnauthorizedKey(detail="This is not a valid key")
    else:
        #user valid return the name and user type
        return {
            "name":result["name"],
            "user_type":result["user_type"]
        }