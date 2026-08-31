<script>

</script>

<div class="top-bar">
    <p class="heading">
        Historically Accurate <br>
        Cloth Reconstruction
    </p>

    <img
        src="/images/in.svg"
        alt="Indian Map"
        class="indianMap"
    />
</div>


<style>
    .heading {
        font-family: 'Times New Roman', Times, serif;
        font-weight: bold;
        font-style: italic;
        font-size: 30px;
        color: #9A031E;

        padding: 15px;
        margin: 0;

        text-align: center;
    }


    .indianMap {
        height: 80px;
        width: 80px;

        flex-shrink: 0;
    }


    .top-bar {
        background-color: #FB8B24;

        min-height: 100px;

        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;

        box-sizing: border-box;

        padding: 0 20px;
    }


    @media (max-width: 768px) {

        .top-bar {
            min-height: 85px;
            padding: 5px 12px;
            gap: 5px;
        }


        .heading {
            font-size: 22px;
            padding: 10px;
            line-height: 1.1;
        }


        .indianMap {
            width: 60px;
            height: 60px;
        }
    }

    @media (max-width: 400px) {

        .top-bar {
            min-height: 75px;
            padding: 4px 8px;
        }

        .heading {
            font-size: 18px;
            padding: 8px;
            line-height: 1.1;
        }

        .indianMap {
            width: 50px;
            height: 50px;
        }
    }
</style>
