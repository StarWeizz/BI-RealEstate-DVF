async function getAll() {
    try {
        const res = await fetch("http://localhost:9000/api/all");
        const data = await res.json();

        return data;
    } catch (err) {
        console.log(err)
    }
}

document.querySelector("#afficherBiens").addEventListener("click", async () => {
    console.log('Bouton cliqué !');

    const biens = await getAll();
    console.log(biens);

    document.querySelector("#nb-biens").textContent = biens.length;

    const container = document.querySelector("#list-container");
    container.innerHTML = "";
    biens.forEach(bien => {
        const div = document.createElement("div");
        div.textContent = `${bien.type_bien} - ${bien.ville} - ${bien.prix} €`;
        container.appendChild(div);
    });
});