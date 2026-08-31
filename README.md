# Introduction
This is a project made in an attempt to reconstruct historically accurate Indian heritage clothing. The initial idea of implementation involved creating an applied AI pipeline comprising of a knowledge base, retrieval system, a diffusion model to generate the garment image and finally a VTON (Virtual Try ON); to concatenate a persons image and the garment image.

## Initial Pipeline

 - The VTON model decided to be used is CatVTON (https://arxiv.org/abs/2407.15886) due to its low memory optimizations and good outputs.
 - The diffusion model we found the best to use as of now is https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0; it gives sufficiently good prompt adherence and works on ~6GB VRAM locally. Need to experiment more on this :)

## Setting Up
The repo requires the creation of two virtual environments titles '.env' & '.catvtonevnv'. The requirementsCatVTON.txt is for the .catvtonevnv and the requirements.txt is for the other libraries. 

## To-Do

 - [x] Decide which diffusion model to use
 - [ ] Decide the LLM reasoning model
 - [ ] Construct a knowledge base for the prototype
