# Introduction
This is a project made in an attempt to reconstruct historically accurate Indian heritage clothing. The initial idea of implementation involved creating an applied AI pipeline comprising of a knowledge base, retrieval system, a diffusion model to generate the garment image and finally a VTON (Virtual Try ON); to concatenate a persons image and the garment image.

## Initial Pipeline

 - The VTON model decided to be used is CatVTON (https://arxiv.org/abs/2407.15886) due to its low memory optimizations and good outputs.
 - The diffusion model we still we need to decide; as stable diffusion is unable to adhere to prompt well and thus is no suitable for this application. The SD-FLUX models do load on a ~6GB VRAM but the text encoder used i.e. Qwen3 gives OOM error.

## Setting Up
The repo requires the creation of two virtual environments titles '.env' & '.catvtonevnv'. The requirementsCatVTON.txt is for the .catvtonevnv and the requirements.txt is for the other libraries. 

## To-Do

 - [ ] Decide which diffusion model to use
 - [ ] Decide the LLM reasoning model
 - [ ] Construct a knowledge base for the prototype
