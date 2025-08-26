from .exceptions import UnauthorizedKey
from .repo import create_config_repo, get_configs_repo, get_user_repo

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
    
#config create service
def create_config_service(config,db):
    #pass the data to repo layer
    result = create_config_repo(config,db)
    return result

#get all configs
def get_configs_service(db):
    result = get_configs_repo(db=db)
    if len(result.data) == 0:
        return None
    return result