function editarMesa(idMesa) {
  console.log(`ID mesa: ${idMesa}`);
  document.querySelector("#idMesa").value = idMesa;
}

function updateMesa() {
  var idMesa = document.querySelector("#idMesa").value;
  var url = "/atualizarMesa";
  var form = document.createElement("form");
  form.action = url;
  form.method = "POST";

  var input = document.createElement("input");
  input.type = "hidden";
  input.name = "idMesa";
  input.value = idMesa;
  form.appendChild(input);
  document.body.appendChild(form);
  form.submit();
}
function deleteMesa() {
  var idMesa = document.querySelector("#idMesa").value;
  var url = "/removerMesa";
//   console.log(idMesa);
  var form = document.createElement("form");
  form.action = url;
  form.method = "POST";

  var input = document.createElement("input");
  input.type = "hidden";
  input.name = "idMesa";
  input.value = idMesa;
  form.appendChild(input);
  document.body.appendChild(form);
  form.submit();
}
