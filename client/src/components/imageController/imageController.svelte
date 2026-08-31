<script lang="ts">
    let files = $state<FileList>();
    let inputPreview = $state("");
    let outputPreview = $state("");
    let processing = $state(false);
    let error = $state("");

    const SERVER_URL = import.meta.env.VITE_PIPELINE_SERVER_URL;

    function handleFiles() {
        if (!files || files.length === 0) { return; }

        const file = files[0];
        console.log("Selected file:", file);

        const reader = new FileReader();
        reader.onload = () => { inputPreview = reader.result as string; };

        reader.readAsDataURL(file);

        outputPreview = "";
        error = "";
    }

    async function processImage() {
        if (!files || files.length === 0) { return; }

        const file = files[0];
        processing = true;
        error = "";

        const formData = new FormData();
        formData.append("image", file);

        console.log("Sending image to FastAPI...");

        try {
            const response = await fetch(
                `${SERVER_URL}/get_image`,
                {
                    method: "POST",
                    body: formData
                }
            );

            console.log("FastAPI response:", response.status);

            if (!response.ok) {
                throw new Error(
                    `FastAPI returned ${response.status}`
                );
            }

            const blob = await response.blob();
            console.log("Received output:", blob);

            const reader = new FileReader();

            reader.onload = () => {
                outputPreview = reader.result as string;
            };

            reader.readAsDataURL(blob);

        } catch (err) {

            console.error("Processing failed:", err);

            error = "Failed to process image.";

        } finally {

            processing = false;

        }
    }
</script>


<div class="main-div">

    <p class="heading">
        Upload the image of the person
    </p>


    <input
        id="file-input"
        type="file"
        accept="image/*"
        bind:files
        onchange={handleFiles}
    />


    <div class="image-container">

        <label class="image input" for="file-input">

            {#if inputPreview}

                <img
                    src={inputPreview}
                    alt="Uploaded person"
                />

            {:else}

                <div class="upload-content">
                    <div class="upload-icon">+</div>
                    <p>Click to upload</p>
                </div>

            {/if}

        </label>


        <div class="image output">

            {#if processing}

                <div class="loading-container">
                    <div class="spinner"></div>
                    <p>Processing...</p>
                </div>

            {:else if outputPreview}

                <img
                    src={outputPreview}
                    alt="Processed result"
                />

            {:else}

                <p class="placeholder">
                    Output will appear here
                </p>

            {/if}

        </div>

    </div>


    <button
        onclick={processImage}
        disabled={!files || files.length === 0 || processing}
    >
        {#if processing}
            Processing...
        {:else}
            Generate
        {/if}
    </button>


    {#if error}
        <p class="error">{error}</p>
    {/if}

</div>


<style>
    .main-div {
        width: 80%;
        min-height: 70vh;
        margin-left: 10vw;
        margin-top: 5vh;
        padding: 20px;

        background-color: #460B2F;

        display: flex;
        flex-direction: column;
        align-items: center;
        box-sizing: border-box;

        border-radius: 10px;
    }


    .heading {
        color: white;

        font-size: 26px;
        font-weight: bold;

        margin-bottom: 30px;

        text-align: center;
    }


    #file-input {
        display: none;
    }


    .image-container {
        display: flex;
        flex-direction: row;
        gap: 30px;

        width: 100%;
        justify-content: center;
    }


    .image {
        width: 400px;
        height: 500px;

        border: 2px dashed rgba(255, 255, 255, 0.5);

        border-radius: 12px;

        display: flex;
        align-items: center;
        justify-content: center;

        overflow: hidden;

        background-color: rgba(255, 255, 255, 0.05);

        box-sizing: border-box;
    }


    .input {
        cursor: pointer;

        transition:
            border-color 0.2s ease,
            background-color 0.2s ease;
    }


    .input:hover {
        border-color: white;
        background-color: rgba(255, 255, 255, 0.1);
    }


    .image img {
        width: 100%;
        height: 100%;

        object-fit: contain;
    }


    .upload-content {
        display: flex;
        flex-direction: column;
        align-items: center;

        color: rgba(255, 255, 255, 0.7);
    }


    .upload-icon {
        width: 50px;
        height: 50px;

        border: 2px solid rgba(255, 255, 255, 0.7);

        border-radius: 50%;

        display: flex;
        align-items: center;
        justify-content: center;

        font-size: 32px;
        font-weight: 300;

        margin-bottom: 15px;
    }


    .upload-content p {
        margin: 0;
        font-size: 16px;
    }


    .placeholder {
        color: rgba(255, 255, 255, 0.5);
        text-align: center;
        padding: 20px;
    }


    .loading-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;

        color: white;
    }


    .spinner {
        width: 45px;
        height: 45px;

        border: 4px solid rgba(255, 255, 255, 0.25);

        border-top-color: white;

        border-radius: 50%;

        animation: spin 0.8s linear infinite;
    }


    @keyframes spin {
        to {
            transform: rotate(360deg);
        }
    }


    button {
        margin-top: 30px;

        padding: 12px 35px;

        border: none;
        border-radius: 6px;

        font-size: 16px;
        font-weight: bold;

        cursor: pointer;
    }


    button:disabled {
        cursor: not-allowed;
        opacity: 0.5;
    }


    .error {
        color: #ffb3b3;
        margin-top: 15px;
        text-align: center;
    }


    @media (max-width: 768px) {

        .main-div {
            width: 94%;
            min-height: auto;

            margin-left: auto;
            margin-right: auto;

            margin-top: 3vh;

            padding: 16px;
        }


        .heading {
            font-size: 20px;
            margin-bottom: 20px;
        }


        .image-container {
            flex-direction: column;

            align-items: center;

            gap: 20px;
        }


        .image {
            width: 100%;
            max-width: 400px;
            aspect-ratio: 4 / 5;

            height: auto;
        }


        button {
            width: 100%;
            max-width: 400px;

            padding: 14px 20px;

            margin-top: 25px;

            font-size: 16px;
        }
    }


    @media (max-width: 400px) {
        .main-div {
            width: 96%;
            padding: 12px;
        }
        .heading {
            font-size: 18px;
        }
        .image {
            aspect-ratio: 4 / 5;
        }
    }

</style>
