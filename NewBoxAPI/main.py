from fastapi import FastAPI

app = FastAPI()

#endpoint for setting the volume
@app.put("/admin/volume/{amount}")
async def set_volume(amount: int):
    return

#endpoint for setting the maximum volume
@app.put("/admin/maxvolume/{amount}")
async def set_max_volume(amount: int):
    return

#endpoint for setting the minimum volume
@app.put("/admin/minvolume/{amount}")
async def set_minM_volume(amount: int):
    return

#endpoint for adding a song to the queue
@app.put("/use/queue/{id}")
async def add_to_queue(id: str):
    return

#endpoint for getting the queue
@app.get("/use/getqueue")
async def get_queue():
    return

#endpoint for playing songs
@app.put("/use/play/{id}")
async def play_music(id: str):
    return

#endpoint to toggle the state of the current song
@app.put("/use/toggleplay")
async def toggle_music():
    return

#endpoint for searching songs in the local database
@app.get("/use/search/{key}")
async def search_music(key: str):
    return