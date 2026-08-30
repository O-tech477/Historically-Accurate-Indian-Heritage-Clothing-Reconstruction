import subprocess
from fastapi import FastAPI
from fastapi.response import FileResponse

def generate_cloth(prompt:str):
    subprocess.run([".venv/bin/python","cloth_worker.py",prompt],
    check=True)

def run_catvton(person:str, cloth:str, output:str):
    subprocess.run([".catvtonevnv/bin/python",
            "vton_worker.py",
            person,
            cloth,
            output,
        ],
        check=True,
    )

app = FastAPI();

@app.get("/generate")
async def generate():

    person = "person.jpeg"
    cloth = "cloth.png"
    output = "output.png"

    prompt = """Single traditional men's royal-court garment, one garment only, full garment visible, centered on pure white background.
                Fitted torso, slightly flared waist, overlapping diagonal front panels with side cloth ties, no buttons.
                Long fitted sleeves to wrists.
                Plain cotton or silk, cream and ivory with deep-red accents.
                Narrow embroidery along front panel and hem. Realistic fabric, elegant tailoring, studio product photography."""


    generate_cloth(prompt)
    run_catvton(person,cloth,output)

@app.post("/get_image")
async def get_image():
    return FileResponse (
        "output.png",
        media_type = "image/png",
        filename = "output.png"
    )
