import torch

from diffusers import StableDiffusionXLPipeline


def vram(label):
    free, total = torch.cuda.mem_get_info()

    print(
        f"[{label}] "
        f"VRAM free: {free / 1024**3:.2f} GB / "
        f"{total / 1024**3:.2f} GB"
    )


class GarmentGenerator:

    def __init__(
        self,
        model_id="segmind/SSD-1B",
    ):

        print("CUDA:", torch.cuda.is_available())

        if not torch.cuda.is_available():
            raise RuntimeError("CUDA GPU not available")

        print("GPU:", torch.cuda.get_device_name())

        vram("START")

        print("\nLoading SSD-1B...")

        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            use_safetensors=True,
            variant="fp16",
        )

        vram("AFTER MODEL LOAD")

        print("\nEnabling sequential CPU offload...")

        self.pipe.enable_sequential_cpu_offload()

        vram("AFTER CPU OFFLOAD")

        print("\nSSD-1B ready!")

    def generate(
        self,
        prompt,
        negative_prompt=None,
        width=512,
        height=768,
        num_inference_steps=30,
        guidance_scale=8.0,
        seed=7,
    ):

        print("\nGenerating image...")

        if negative_prompt is None:
            negative_prompt = (
                "person, human, man, woman, model, mannequin, body, "
                "shirt being worn, hanger, folded shirt, "
                "multiple garments, pants, trousers, accessories, "
                "cropped, cut off, incomplete garment, "
                "side view, back view, angled view, "
                "perspective distortion, "
                "room, furniture, clutter, "
                "text, watermark, logo, "
                "extra sleeves, missing sleeves, malformed collar, "
                "deformed buttons, distorted fabric, "
                "blurry, low quality, cartoon, illustration, CGI"
            )

        generator = torch.Generator(
            device="cuda"
        ).manual_seed(seed)

        with torch.inference_mode():

            result = self.pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
                generator=generator,
            )

        print("Image generated!")

        return result.images[0]
