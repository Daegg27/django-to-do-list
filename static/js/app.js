function newUser(event){
    event.preventDefault()

    let newTask = {}
    
    for (let i = 0; i < event.target.length - 1; i++){ // event.target.length - 1 is to account for the button that is also in the form 
        
        let name = event.target[i].name
        let value = event.target[i].value

        newTask[name] = value
        event.target[i].value = '' // Clears the input fields so you can add more (not important if redirecting).

    }

    axios.post('/todos/', newTask)
    // .then((response => {
    //     console.log(response)
    // })
    // )
}