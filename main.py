import subprocess

def generate_cloth(prompt, output_path):
    subprocess.run(
        [   ".venv/bin/python",
            "cloth_worker.py",
            prompt,
            output_path,
        ],
        check=True,
    )


def run_catvton(person, cloth, output):

    subprocess.run(
        [   ".catvtonevnv/bin/python",
            "vton_worker.py",
            person,
            cloth,
            output,
        ],
        check=True,
    )


def main():

    person = "person.jpeg"
    cloth = "cloth.png"
    output = "output.png"

    prompt = """
    A high-quality e-commerce product photograph of a single
        men's plain black short-sleeve cotton shirt, displayed completely
        flat and fully unfolded, front-facing, centered, entire shirt
        visible from collar to bottom hem, sleeves extended naturally,
        clearly visible collar, button placket, seams and hem,
        realistic cotton fabric texture and natural folds,
        isolated on a pure white background,
        professional clothing catalog photography,
        soft even studio lighting, sharp focus,
        no person wearing the shirt,
        photorealistic
    """

    print("Generating garment...")

    generate_cloth(prompt,cloth,)

    print("Garment generated.")

    print("Running CatVTON...")

    run_catvton(person,cloth,output)

    print("Finished!")

if __name__ == "__main__":
    main()
