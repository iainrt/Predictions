from replit import db

def db_init():
    if "challenges" not in db.keys():
        db["challenges"] = {}

    if "competition_started" not in db.keys():
        db["competition_started"] = False