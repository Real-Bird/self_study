const toDoForm = document.getElementById("todo-form");
const toDoInput = document.querySelector("#todo-form input");
const toDoList = document.getElementById("todo-list");

function handleToDoSubmit(event) {
    event.preventDefault();
    const newTodo = toDoInput.value;
    console.log(`todoinput value = ${toDoInput.value}`);
    toDoInput.value = "";
    console.log(`new todo = ${newTodo}, todoinput value = ${toDoInput.value}`);
}

toDoForm.addEventListener("submit", handleToDoSubmit);