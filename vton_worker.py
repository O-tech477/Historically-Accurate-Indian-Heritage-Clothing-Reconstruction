import sys
from PIL import Image
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "CatVTON"))
from CatVTON.catviton import CatVTON


def main():
    person_path = sys.argv[1]
    cloth_path = sys.argv[2]
    output_path = sys.argv[3]

    model = CatVTON()

    person = Image.open(person_path).convert("RGB")
    cloth = Image.open(cloth_path).convert("RGB")

    result = model.generate(
        person_image=person,
        cloth_image=cloth,
        cloth_type="upper",
        width=384,
        height=512,
        seed=7,
        num_inference_steps=50,
        guidance_scale=2.5,
    )

    result.save(output_path)


if __name__ == "__main__":
    main()
