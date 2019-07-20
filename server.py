# fastapi
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

# lib
from transliterate.core import lat2cyr, Direction

# misc
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


app = FastAPI(
    title="Imlo Project",
    description="Imlo Project Description",
    version="0.1.0",
)

origins = [
    "http://tekshir.uz",
    "https://tekshir.uz",
    "http:localhost",
    "http:localhost:8888",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/transliterate")
async def transliterate(content: str, direction: Direction):
    logging.info(f"Transliterate direction -> {direction}")
    data = {"status": "failure", "direction": direction}

    if direction == Direction.lat2cyr:
        result = await lat2cyr(content)
        data = {"status": "success", "direction": direction, "data": result}
    elif direction == Direction.cyr2lat:
        raise HTTPException(status_code=400, detail="Not implemented yet.")

    return data


@app.post("/spellchecker")
async def spellchecker(word: str):
    raise HTTPException(status_code=400, detail="Not implemented yet.")


@app.post("/autocomplete")
async def autocomplete(word: str):
    raise HTTPException(status_code=400, detail="Not implemented yet.")
