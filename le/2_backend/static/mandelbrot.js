function sample() {
    const real = document.getElementById("real").value;
    const imag = document.getElementById("imag").value;
    const maxIters = document.getElementById("maxIters").value;

    const url = `http://localhost:8000/sample`;
    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
            max_iters: maxIters,
        }),
    };
    document.getElementById("submit").disabled = true;
    fetch(url, params)
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("result").innerHTML = data;
            document.getElementById("submit").disabled = false;
        })
        .catch((error) => {
            document.getElementById("submit").disabled = false;
            console.log("ERROR!");
            console.log(error);
        });
}

function col() {
    const real = document.getElementById("real").value;
    const imag = document.getElementById("imag").value;
    const hexStart = document.getElementById("hexStart").value;
    const hexEnd = document.getElementById("hexEnd").value;
    const maxIters = document.getElementById("maxIters").value;

    const url = `http://localhost:8000/col`;
    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
            max_iters: maxIters,
            hex_start: hexStart,
            hex_end: hexEnd,
        }),
    };
    document.getElementById("submit").disabled = true;
    fetch(url, params)
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("result").innerHTML = data.numIters;
            document.body.style.backgroundColor = data.col;
            document.getElementById("submit").disabled = false;
        })
        .catch((error) => {
            document.getElementById("submit").disabled = false;
            console.log("ERROR!");
            console.log(error);
        });
}

function image() {
    const real = document.getElementById("real").value;
    const imag = document.getElementById("imag").value;
    const delta = document.getElementById("delta").value;
    const resolution = document.getElementById("resolution").value;
    const hexStart = document.getElementById("hexStart").value;
    const hexEnd = document.getElementById("hexEnd").value;
    const maxIters = document.getElementById("maxIters").value;

    const url = `http://localhost:8000/image`;
    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
            delta: delta,
            resolution: resolution,
            max_iters: maxIters,
            hex_start: hexStart,
            hex_end: hexEnd,
        }),
    };
    document.getElementById("submit").disabled = true;
    fetch(url, params)
        .then((response) => response.blob())
        .then((blob) => {
            const objectURL = URL.createObjectURL(blob);
            document.body.style.backgroundImage = `url(${objectURL})`;
            document.getElementById("submit").disabled = false;
        })
        .catch((error) => {
            document.getElementById("submit").disabled = false;
            console.log("ERROR!");
            console.log(error);
        });
}
