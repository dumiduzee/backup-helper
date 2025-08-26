from fastapi import status
from .utils import send_sms
from .exceptions import AddClientexception, DeleteConfigException, UnauthorizedKey
from .repo import (add_client_to_system, check_config_repo_by_id, create_config_repo,
    delete_config_based_on_id, get_configs_repo, get_user_repo, getcliet_based_on_name)
import uuid
import random
import string

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
    
#config create servicereturn
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

#delete specific config
def delete_config_service(id,db):
    #check id is a valid id 
    try:
        id = uuid.UUID(id)
    except ValueError:
        raise DeleteConfigException(status_code=status.HTTP_400_BAD_REQUEST,detail="Malforemed config id.")
    #first check that id exists on the database
    result = check_config_repo_by_id(id=id,db=db)
    #if available then delete it
    if result:
        deleted = delete_config_based_on_id(id=id,db=db)
        if deleted:
            return deleted
        else:
            return False
    else:
        raise DeleteConfigException(status_code=status.HTTP_400_BAD_REQUEST,detail="Selected config not found!") 


#add new client to the system
def add_new_client_service(client_name,db):
    #check that client already exists
    result = getcliet_based_on_name(client_name,db=db)
    if result is False:
        raise AddClientexception(status_code=status.HTTP_404_NOT_FOUND,detail="User already exists")
    #genarate key for the client
    key = uuid.uuid4().hex.upper()[0:6]
    client_name["key"] = key
    #add client to the system
    result = add_client_to_system(client=client_name,db=db)
    #send key and name to the admins phone number
    if result:
        send_sms(key=key,name=client_name["client_name"])
    