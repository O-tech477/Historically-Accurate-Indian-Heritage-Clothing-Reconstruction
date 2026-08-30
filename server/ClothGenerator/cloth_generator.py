import torch
from diffusers import StableDiffusionXLPipeline



class GarmentGenerator:

    def __init__(self,model_id="stabilityai/stable-diffusion-xl-base-1.0"):

        if not torch.cuda.is_available():
            raise RuntimeError("CUDA GPU not available")

        self.pipe = StableDiffusionXLPipeline.from_pretrained(model_id,torch_dtype=torch.float16,use_safetensors=True,variant="fp16")
        self.pipe.enable_sequential_cpu_offload()


    def generate(self,prompt):

        with torch.inference_mode():
            result = self.pipe(prompt=prompt)

        return result.images[0].save("cloth.png")
