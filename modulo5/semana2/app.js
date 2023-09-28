let tarefas = document.getElementById('tarefas')
let bnt = document.getElementById('bnt')
let campo = document.getElementById('tarefa')

let listaTarefas = localStorage.getItem('tarefas')

if(!listaTarefas) {
    listaTarefas = []
} else {
    listaTarefas = JSON.parse(listaTarefas)
}

for (let i =0; i < listaTarefas.length; i++) {
    const itemTarefa = listaTarefas[i];
    let itemSalvo = document.createElement('li')
    itemSalvo.setAttribute('class', 'list-goup-item')
    itemSalvo.innerText = itemTarefa
    tarefas.appendChild(itemSalvo)
}


function adicionarTarefa(){
    let texto = campo.value 
    let item = document.createElement('li')
    item.setAttribute('class', 'list-group-item')
    item.innerText = texto
    tarefas.appendChild(item)
    campo.value = ''
    listaTarefas.push(texto)
    localStorage.setItem('tarefas', JSON.stringify(listaTarefas))
}


bnt.addEventListener('clik', adicionarTarefa)