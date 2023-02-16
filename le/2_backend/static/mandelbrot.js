function sample() {
    const real = document.getElementById("real").value;
    const imag = document.getElementById("imag").value;

    const url = `http://localhost:8000/sample`;
    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
        }),
    };
    fetch(url, params)
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("result").innerHTML = data;
        })
        .catch((error) => {
            console.log("ERROR!");
            console.log(error);
        });
}
