import json
import os.path
import mysql.connector


        
    
def jload(self, path = str):
    if not os.path.exists(path):
        return SyntaxError
    if os.path.exists(path):
        with open(path) as f:
            info = json.load(f)
    return info
def jdump(self, data, path):
    if not isinstance(data, dict):
        print("Not A Dict")
        return SyntaxError
    if not os.path.isfile(path):
        f2 = open(path, "w+")
    with open(path, "r+") as f:
        json.dump(data, f,indent=4)
        
def checkKey(self, dict_obj, key): 
    
        if key in dict_obj.keys(): 
            return True
        else: 
            return False


def pull(*args):
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse",
                    )
    dbcursor = mydb.cursor(buffered=True)
    dbcursor.execute(*args)
    
    results = dbcursor.fetchall()
    mydb.commit()
    return results

def pull_one(*args):
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse")
    dbcursor = mydb.cursor(buffered=True)
    dbcursor.execute(*args)
    
    results = dbcursor.fetchone()
    mydb.commit()
    return results
def push(*args):
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="shad",
                    passwd="shadii",
                    database="finesse")
    dbcursor = mydb.cursor(buffered=True)
    dbcursor.execute(*args)
    mydb.commit()
    return 404


