import os

import torch
from diffusers.image_processor import VaeImageProcessor
from huggingface_hub import snapshot_download

from .model.cloth_masker import AutoMasker
from .model.pipeline import CatVTONPipeline
from .utils import init_weight_dtype, resize_and_crop, resize_and_padding


class CatVTON:
    def __init__(self, base_model_path = "booksforcharlie/stable-diffusion-inpainting", repo_id = "zhengchong/CatVTON", mixed_precision = "fp16", allow_tf32 = True) -> None:
        repo_path = snapshot_download(
                    repo_id=repo_id
                )

        self.pipeline = CatVTONPipeline(
        base_ckpt=base_model_path,
        attn_ckpt=repo_path,
        attn_ckpt_version="mix",
        weight_dtype=init_weight_dtype(mixed_precision),
        use_tf32=allow_tf32,
        device='cuda'
        )

        self.mask_processor = VaeImageProcessor(vae_scale_factor=8, do_normalize=False, do_binarize=True, do_convert_grayscale=True)

        self.automasker = AutoMasker(
            densepose_ckpt=os.path.join(repo_path, "DensePose"),
            schp_ckpt=os.path.join(repo_path, "SCHP"),
            device='cuda',
        )


    def generate(self, person_image, cloth_image, cloth_type, width = 384, height = 512, seed = 7, num_inference_steps=25, guidance_scale=2.5):

        person_image = resize_and_crop(person_image,(width, height))
        cloth_image = resize_and_padding(cloth_image,(width, height))

        mask = self.automasker(person_image,cloth_type)["mask"]
        mask = self.mask_processor.blur(mask,blur_factor=9)

        generator = torch.Generator(device='cuda').manual_seed(seed)

        result_image = self.pipeline(
            image=person_image,
            condition_image=cloth_image,
            mask=mask,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            generator=generator
        )[0]

        return result_image
