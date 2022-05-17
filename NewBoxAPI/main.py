from fastapi import FastAPI

app = FastAPI()

#endpoint voor het zetten van het volume
@app.put("/beheer/volume/{amount}")
async def set_volume(amount: int):
    return

#endpoint voor het zetten van het maximum volume
@app.put("/beheer/maxvolume/{amount}")
async def set_max_volume(amount: int):
    return

#endpoint voor het zetten van het minimum volume
@app.put("/beheer/minvolume/{amount}")
async def set_minM_volume(amount: int):
    return

#endpoint voor het toevoegen aan wachtrij
@app.put("/use/queue/{id}")
async def add_to_queue(id: str):
    return

#endpoint voor het ophalen van de wachtrij
@app.get("/use/getqueue")
async def get_queue():
    return

#endpoint voor afspelen muziek
@app.put("/use/play/{id}")
async def play_music(id: str):
    return

#endpoint voor het pauzeren van spelende muziek
@app.put("/use/toggleplay")
async def toggle_music():
    return

#endpoint voor het zoeken van muziek
@app.get("/use/search/{key}")
async def search_music(key: str):
    return