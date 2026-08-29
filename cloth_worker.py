import sys

from ClothGenerator.cloth_generator import GarmentGenerator


def main():
    prompt = sys.argv[1]
    output_path = sys.argv[2]

    generator = GarmentGenerator()

    image = generator.generate(
        prompt=prompt,
        width=384,
        height=512,
        num_inference_steps=8,
        seed=7,
    )

    image.save(output_path)

if __name__ == "__main__":
    main()
