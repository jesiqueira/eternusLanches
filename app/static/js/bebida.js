function editarBebida(idBebida) {
    document.querySelector("#idBebida").value = idBebida
}

function updateBebida() {
    let idBebida = document.querySelector("#idBebida").value
    let url = "/updateBebida"

    let form = document.createElement("form")
    form.action = url
    form.method = "POST"

    let input = document.createElement("input")
    input.type = "hidden"
    input.name = "idBebida"
    input.value = idBebida
    form.appendChild(input)
    document.body.appendChild(form)
    form.submit()
}

function deleteBebida() {
    let idBebida = document.querySelector("#idBebida").value
    let url = "/removerBebida"

    let form = document.createElement("form")
    form.action = url
    form.method = "POST"

    let input = document.createElement("input")
    input.type = "hidden"
    input.name = "idBebida"
    input.value = idBebida
    form.appendChild(input)
    document.body.appendChild(form)
    form.submit()
}
