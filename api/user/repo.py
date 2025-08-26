from supabase import Client


#Get user name based on the key
def get_user_repo(key,db:Client):
    querry = db.table("users").select("*").eq("key",key["login_key"])
    result = querry.execute()
    if len(result.data) == 0:
        return None
    else:
        return result.data[0]
   

#create config on db
def create_config_repo(config,db:Client):
    query = db.table("configs").insert(config)
    result = query.execute()
    if len(result.data) > 0:
        #succussfully added data
        return True
    else:
        return False