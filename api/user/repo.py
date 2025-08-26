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
    
#get all configs on db
def get_configs_repo(db:Client):
    quesry = db.table("configs").select("*")
    result = quesry.execute()
    return result

#check config availability based on id
def check_config_repo_by_id(id,db:Client):
    q = db.table("configs").select("").eq("id",id)
    result = q.execute()
    if len(result.data) == 0:
        return None
    else:
        return True
    
#delete config based on id
def delete_config_based_on_id(id,db:Client):
    q = db.table("configs").delete().eq("id",id)
    result = q.execute()
    if len(result.data) == 0:
        return None
    else:
        return True
    