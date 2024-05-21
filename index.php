<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bússola de Big Data</title>
    <style>
        #bussola {
            width: 200px;
            height: 200px;
            border: 1px solid black;
            border-radius: 50%;
            position: relative;
        }
        #seta {
            width: 2px;
            height: 100px;
            background: red;
            position: absolute;
            top: 50%;
            left: 50%;
            transform-origin: bottom;
            transform: rotate(0deg);
        }
    </style>
</head>
<body>
    <h1>Bússola de Big Data</h1>
    <div id="bussola">
        <div id="seta"></div>
    </div>
    <script>
        async function fetchData() {
            const response = await fetch('http://localhost:9000/analisar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    coordenadas: [
                        {frequencia_potassio: 0.8, x: 100, y: 200},
                        {frequencia_potassio: 0.3, x: 150, y: 250}
                    ],
                    detridos: [
                        {amplitude: 1.5, frequencia_base: 0.9, periodo: 10},
                        {amplitude: 0.5, frequencia_base: 1.2, periodo: 5}
                    ],
                    massa: 5.97e24,
                    raio: 6371,
                    constante_gravitacional: 6.67430e-11
                })
            });
            return response.json();
        }

        function updateCompass(data) {
            const seta = document.getElementById('seta');
            const angle = (data.frequencia_gravitacional % 360);
            seta.style.transform = `rotate(${angle}deg)`;
        }

        window.onload = async () => {
            const data = await fetchData();
            updateCompass(data);
        };
    </script>
</body>
</html>
