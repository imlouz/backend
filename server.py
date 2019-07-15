# fastapi
from fastapi import FastAPI

# lib
from transliterate import lat2cyr, Direction

# misc
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


app = FastAPI(
    title="Imlo Project",
    description="Imlo Project Description",
    version="0.1.0",
)


@app.post("/transliterate")
async def transliterate(content: str, direction: Direction):
    logging.info(f"Transliterate direction -> {direction}")
    data = {"status": False}

    if direction == Direction.lat2cyr:
        result = await lat2cyr(content)
        data = {"status": True, "data": result}
    elif direction == Direction.cyr2lat:
        result = await cyr2lat(content)
        data = {"status": True, "data": result}

    return data


@app.post("/spellchecker")
async def spellchecker(word: str):
    raise HTTPException(status_code=400, detail="Not implemented yet.")


@app.post("/autocomplete")
async def autocomplete(word: str):
    raise HTTPException(status_code=400, detail="Not implemented yet.")
