import pandas as pd
from fastapi import FastAPI, HTTPException, Request, Response, Header

df = pd.read_csv('players.csv')

app = FastAPI()

API_KEY = "h8ftds"

@app.get("/")
def root():
    return {"message":"Welcome to Players API! There are some features that you can explore",
            "menu":{1:"See all players (/players)",
                    2:"See player by ID (/players/id)",
                    3:"Add player (/add) - You may need request",
                    4:"Edit player (/edit/id)",
                    5:"Delete player (/del/id)"}
                    }

@app.get("/players")
def show():
    return df.to_dict()

@app.get("/players/{id}")
def show_by_id(id:int):
    if id not in dyf['ID'].values:
        raise HTTPException(status_code=404, detail=f"Player with ID {id} not found")
    else:
        return df[df['ID']==id].to_dict()
    
@app.post("/add")
def add_player(added_player:dict, api_key: str = Header(None)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        id = len(df['ID'].values)+1
        df.loc[id] = added_player
        return f"Player successfully added into your database with ID {id}"
    
@app.put("/edit/{id}")
def edit_player(id:int,updated_player:dict, api_key: str = Header(None)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    elif id not in df['ID'].values:
        raise HTTPException(status_code=404, detail=f"Player with ID {id} not found")
    else:
        df.loc[id] = updated_player
        return {"message": f"Player with ID {id} has been updated successfully."}
    
@app.delete("/del/{id}")
def remove_row(id:int, api_key: str = Header(None)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    elif id not in df['ID'].values:
        raise HTTPException(status_code=404, detail=f"Player with ID {id} not found")
    else:
        df.drop(df[df['ID']==id].index, inplace=True)
        
#@app.get("/players/{state}")
#def getPlayerState(state:str,api_key:str=Header(None)
#    print(API_KEY)
#    print(state)
#    if api_key is None or api_key != API_KEY:
#        raise HTTPException(status_code = 401, detail = "Unverivied API key"/)