function editarPorcao(idPorcao) {
    document.querySelector("#idPorcao").value = idPorcao
    console.log(`id porcao: ${idPorcao}`)
}

function updatePorcao() {
    let idPorcao = document.querySelector("#idPorcao").value
    let url = "/updatePorcao"

    let form = document.createElement("form")
    form.action = url
    form.method = "POST"

    let input = document.createElement("input")
    input.type = "hidden"
    input.name = "idPorcao"
    input.value = idPorcao
    form.appendChild(input)
    document.body.appendChild(form)
    form.submit()
}

function deletePorcao() {
    let idPorcao = document.querySelector("#idPorcao").value
    let url = "/removerPorcao"

    let form = document.createElement("form")
    form.action = url
    form.method = "POST"

    let input = document.createElement("input")
    input.type = "hidden"
    input.name = "idPorcao"
    input.value = idPorcao
    form.appendChild(input)
    document.body.appendChild(form)
    form.submit()
}
