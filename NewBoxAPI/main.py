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
