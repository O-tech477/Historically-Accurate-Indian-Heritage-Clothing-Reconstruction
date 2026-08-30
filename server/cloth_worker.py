import sys

from ClothGenerator.cloth_generator import GarmentGenerator


def main():
    prompt = sys.argv[1]

    generator = GarmentGenerator()
    image = generator.generate(prompt=prompt)

if __name__ == "__main__":
    main()
