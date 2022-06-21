

const textField = document.getElementById("user_input");
const trigger = document.getElementById("trigger");
const list = document.getElementById("list");

trigger.addEventListener("click", function () {
    if (textField.value.trim().length < 1) return;
    const item = document.createElement("li");
    list.appendChild(item);
   
    const itemText = document.createElement("span");
    itemText.innerText = textField.value;
    item.appendChild(itemText);

    const completeButton = document.createElement("button");
    completeButton.innerText = "Complete";
    completeButton.className = "complete";
    item.appendChild(completeButton);

    const deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";
    deleteButton.className = "delete";

    item.appendChild(deleteButton);

    textField.value = "";
 
  });



document.addEventListener("click", function(event) {
    if(event.target.className === "complete"){
        if(event.target.parentNode.className.includes("completed")){
            event.target.parentNode.className = event.target.parentNode.className.replace("completed", "");
            event.target.innerText = "Complete";

        }
        else{
            event.target.parentNode.className += " completed";
            event.target.innerText = "undo";

        }
        
    }
    if(event.target.className === "delete"){
        list.removeChild(event.target.parentNode)
    }

})