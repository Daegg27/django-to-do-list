function changeTask(event, id) {
    event.preventDefault()

    newTask = {}

    for (let i = 0; i < event.target.length - 1; i++){ // event.target.length - 1 is to account for the button that is also in the form 
        
        let name = event.target[i].name
        let value = event.target[i].value

        newTask[name] = value
        event.target[i].value = '' // Clears the input fields so you can add more (not important if redirecting).

    }

    axios.get('/todos/update', {
        params: {
            title: newTask['title'],
            description: newTask['description'],
            id: id
        }
    })
    .then((response => {
        window.location.href = '/todos' // Work around for not being able to get the HttpResponseRedirect to work
    })
    )
}

function deleteTask(event, id){
    event.preventDefault()

    axios.post(`/todos/${id}/delete`, {
        'id':id
    }).then((response => {
        window.location.href = '/todos'
    })
    )
}