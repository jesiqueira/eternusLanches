function editarLanche(idLanche) {
    document.querySelector("#idLanche").value = idLanche
}

function updateLanche() {
    let idLanche = document.querySelector("#idLanche").value
    let url = "/atualizarlanche"

    let form = document.createElement("form")
    form.action = url
    form.method = "POST"

    let input = document.createElement("input")
    input.type = "hidden"
    input.name = "idLanche"
    input.value = idLanche
    form.appendChild(input)
    document.body.appendChild(form)
    form.submit()
}

function deleteLanche() {
    let idLanche = document.querySelector("#idLanche").value
    let url = "/removerlanche"
    let form = document.createElement("form")
    form.action = url
    form.method = "POST"

    let input = document.createElement("input")
    input.type = "hidden"
    input.name = "idLanche"
    input.value = idLanche
    form.appendChild(input)
    document.body.appendChild(form)
    form.submit()
}
