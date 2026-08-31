import subprocess
from pathlib import Path

from database.database import Database

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


SERVER_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SERVER_DIR.parent

MAIN_PYTHON = PROJECT_DIR / ".venv/bin/python"
CATVTON_PYTHON = PROJECT_DIR / ".catvtonevnv/bin/python"


def generate_cloth(prompt: str):
    subprocess.run(
        [
            str(MAIN_PYTHON),
            str(SERVER_DIR / "cloth_worker.py"),
            prompt,
        ],
        check=True,
    )


def run_catvton(person: str, cloth: str, output: str):
    subprocess.run(
        [
            str(CATVTON_PYTHON),
            str(SERVER_DIR / "vton_worker.py"),
            person,
            cloth,
            output,
        ],
        check=True,
    )


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://localhost",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/get_image")
async def get_image(garment_type:str = Form(...), image: UploadFile = File(...)):

    person = SERVER_DIR / "person.jpeg"
    cloth = SERVER_DIR / "cloth.png"
    output = SERVER_DIR / "output.png"

    image_data = await image.read()

    with open(person, "wb") as f:
        f.write(image_data)

    db = Database()


    print("Garment type received:", repr(garment_type))
    prompt = db.getPrompt(garment_type)
    generate_cloth(prompt)
    db.closeDB()


    run_catvton(
        str(person),
        str(cloth),
        str(output)
    )

    return FileResponse(
        output,
        media_type="image/png",
        filename="output.png"
    )
