let shoppingList = [];
let shoppingListCategory = [];
let itemCompletionStatus = [];
let shoppingListQuantity = [];
let shoppingListColour = [];
var token;
let dropdownText;

$(document).ready(function() {
    document.getElementById("viewListFromLink").value = "";
    document.getElementById("overlay").style.display = "block";
    document.getElementById("nameOverlay").style.display = "none";
    dropdownText = "Category";
    token = generateToken();
    document.getElementById("printName").textContent = "";
    document.getElementById("listName").value = "";
    document.getElementById("notesBox").value = "";
});

function loadExisitingShoppingList() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("secondOverlay").style.display = "block";
}

function cancelLoadList() {
    document.getElementById("secondOverlay").style.display = "none";
    document.getElementById("overlay").style.display = "block";
}

function newShoppingList() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("printName").textContent = "";
    document.getElementById("notesBox").value = "";
    token = generateToken();
    removeList();
}

function makeEditable(ID, value) {
    // make a field editable
    document.getElementById(ID).setAttribute("contenteditable", value)
}

function toggleButton() {
    // Check that text is added to the field before category can be added and item can be submitted
    let item = document.getElementById("ShoppingListItem").value;

    if (item.length == 0) {
        document.getElementById("SubmitButton").disabled = true;
        document.getElementById("dropdownButton").disabled = true;
        document.getElementById("ShoppingListQuantity").disabled = true;
    } else {
        document.getElementById("SubmitButton").disabled = false;
        document.getElementById("dropdownButton").disabled = false;
        document.getElementById("ShoppingListQuantity").disabled = false;
    }
}

function submitEditedItem(ID, oldName) {
    var index = parseInt(ID) + 1; //make an integer so that it can be incremented
    var payload = {
        id: index.toString(),
        oldName: oldName,
        newName: shoppingList[ID],
        category: shoppingListCategory[ID],
        completed: itemCompletionStatus[ID],
        quantity: shoppingListQuantity[ID],
        arrayIndex: index.toString(),
        token: token 
    };
    $.ajax({
        url: "/edititem",
        type: "POST",
        contentType: "application/json",
        processData: false,
        data: JSON.stringify(payload),
        complete: function(data) {}
    });
}

function submitEditedQuantity(ID, oldQuantity) {
    var index = parseInt(ID) + 1; //make an integer so that it can be incremented
    var payload = {
        id: index.toString(),
        oldQuantity: oldQuantity,
        name: shoppingList[ID],
        category: shoppingListCategory[ID],
        completed: itemCompletionStatus[ID],
        newQuantity: shoppingListQuantity[ID],
        arrayIndex: index.toString(),
        token: token 
    };
    $.ajax({
        url: "/editQuantity",
        type: "POST",
        contentType: "application/json",
        processData: false,
        data: JSON.stringify(payload),
        complete: function(data) {}
    });
}

function editItem(itemID) {

    let ID = itemID.toString().split("_")[1];
    let oldName = shoppingList[ID];

    shoppingList[ID] = document.getElementById(itemID.toString()).innerHTML;

    submitEditedItem(ID, oldName);
    document.getElementById(itemID).setAttribute("contenteditable", "false")
}

function editCategory(itemID) {

    let ID = itemID.toString().split("_")[1];
    submitEditedItem(ID, shoppingList[ID]);
}

function editQuantity(itemID) {

    let ID = itemID.toString().split("_")[1];
    let oldQuantity = shoppingListQuantity[ID];

    shoppingListQuantity[ID] = document.getElementById(itemID.toString()).innerHTML;

    submitEditedQuantity(ID, oldQuantity);
    document.getElementById(itemID).setAttribute("contenteditable", "false")
}

function editPurchaseStatus(itemID) {

    let ID = itemID.toString().split("_")[1];
    itemCompletionStatus[ID] = document.getElementById(itemID.toString()).checked;
    submitEditedItem(ID, shoppingList[ID]);
}

function submitNameChangesOnEnter(e, ID) {
    let enterKey = 13;
    if (e.keyCode === enterKey) {
        editItem(ID);
    }
}

function submitQuantityChangesOnEnter(e, ID) {
    let enterKey = 13;
    if (e.keyCode === enterKey) {
        editQuantity(ID);
    }
}

function submitCategoryChangesOnEnter(e, ID) {
    let enterKey = 13;
    if (e.keyCode === enterKey) {
        editCategory(ID);
    }
}

// allows user to submit an item on press of the enter button
function saveItemOnEnter(e) {
    let enterKey = 13;
    if (e.keyCode === enterKey) { // makes sure that enter is the button being pressed
        let quantity_value = document.getElementById("ShoppingListQuantity").value;
        if (quantity_value.match(/^[0-9]+$/) != null) {
            storeItem();
        } else {
            alert("Quantity should only contain numbers");
            document.getElementById("ShoppingListQuantity").value = "";
        }
    }
}

function saveQuantityOnEnter(e) {
    let enterKey = 13;
    if (e.keyCode === enterKey) { // makes sure that enter is the button being pressed
        let quantity_value = document.getElementById("ShoppingListQuantity").value;
        if (quantity_value.match(/^[0-9]+$/) != null) {
            storeItem();
        } else {
            alert("Quantity should only contain numbers");
            document.getElementById("ShoppingListQuantity").value = "";
        }
    }
}

function deleteItem(itemID) {
    let ID = itemID.toString().split("_")[1];
    let itemName = document.getElementById("shoppingList_" + ID).innerHTML;

    var payload = {
        name: itemName,
        token: token
    };
    $.ajax({
        url: "/deleteitem",
        type: "POST",
        contentType: "application/json",
        processData: false,
        data: JSON.stringify(payload),
        complete: function(data) {}
    });

    shoppingList.splice(ID, 1);

    var card = document.getElementById("list-entry_" + ID);
    return card.parentNode.removeChild(card);
}

function addItem(name, category, status, quantity,colour) {

    let item_name = name;
    let item_category = category;
    let initialCompletionStatus = status;
    let item_quantity = quantity;
    let item_colour = colour;

    if (item_name == "none") {
        item_name = document.getElementById("ShoppingListItem").value;
    }

    if (item_category == "none") {
        item_category = dropdownText;
    }

    if (item_quantity === 0) {
        item_quantity = document.getElementById("ShoppingListQuantity").value;
    }

    // Check that the category is not empty, if so assign a default value (This default is not added 
    // to the card but the arrays should still be the same lemgth)
    if (item_category == null) {
        item_category = "Category/Aisle";
    } else if (item_category.length == 0) {
        item_category = "Category/Aisle";
    }

    if (item_quantity == null) {
        item_quantity = 1;
    } else if (item_quantity.length == 0) {
        item_quantity = 1;
    }

    shoppingList.push(item_name);
    shoppingListCategory.push(item_category);
    shoppingListQuantity.push(item_quantity);
    shoppingListColour.push(item_colour);

    itemCompletionStatus.push(initialCompletionStatus);
    // Clear input text field once the item has been saved to the array
    document.getElementById("ShoppingListItem").value = "";
    document.getElementById("dropdownButton").innerHTML = "Category";// &#11167";
    dropdownText = "Category";
    document.getElementById("ShoppingListQuantity").value = "";

    // Disable the button again for no input
    document.getElementById("SubmitButton").disabled = true;
    document.getElementById("ShoppingListQuantity").disabled = true;
    document.getElementById("dropdownButton").disabled = true;

    renderCards();
}

function orderByPurchased() {
    //token = document.getElementById("viewListFromLink").innerHTML;
    document.getElementById("secondOverlay").style.display = "none";
    if (token.match(/^[0-9]+$/) != null) {
        removeList();

        $.ajax({
            url: "/itemsorderedbypurchased/" + token.toString(),
            type: "GET",
            contentType: "application/json",
            async: true,
            success: function(resp) {
                let nameArray = (resp);
                let names = nameArray.map(function(a) { return a.name; });
                let categories = nameArray.map(function(a) { return a.category; });
                let purchaseStatus = nameArray.map(function(a) { return a.completed; });
                let quantities = nameArray.map(function(a) { return a.quantity; });
                let colours = nameArray.map(function(a) { return a.colour; });
                if (names.length === 0) {
                    alert("No shopping list found");
                    document.getElementById("viewListFromLink").value = "";
                } 
                else if (names.length != 0) {
                    removeList();
                    for (let i = 0; i < names.length; i++) {
                        shoppingList.push(names[i]);
                        shoppingListCategory.push(categories[i]);
                        itemCompletionStatus.push(purchaseStatus[i]);
                        shoppingListQuantity.push(quantities[i]);
                        shoppingListColour.push(colours[i]);
                        if (itemCompletionStatus[i] === 0) {
                            itemCompletionStatus[i] = false;
                        } else if (itemCompletionStatus[i] === 1) {
                            itemCompletionStatus[i] = true;
                        }
                    }
                    document.getElementById("viewListFromLink").value = "";

                    renderCards();
                }
            }
        });

    } else {
        alert("Token should only contain numbers: " + document.getElementById("viewListFromLink").innerHTML);
        document.getElementById("viewListFromLink").value = "";
    }
}

function orderByCategory() {
    //token = document.getElementById("viewListFromLink").innerHTML;
    document.getElementById("secondOverlay").style.display = "none";
    if (token.match(/^[0-9]+$/) != null) {
        removeList();

        $.ajax({
            url: "/itemsorderedbycategory/" + token.toString(),
            type: "GET",
            contentType: "application/json",
            async: true,
            success: function(resp) {
                let nameArray = (resp);
                let names = nameArray.map(function(a) { return a.name; });
                let categories = nameArray.map(function(a) { return a.category; });
                let purchaseStatus = nameArray.map(function(a) { return a.completed; });
                let quantities = nameArray.map(function(a) { return a.quantity; });
                let colours = nameArray.map(function(a) { return a.colour; });
                if (names.length === 0) {
                    alert("No shopping list found");
                    document.getElementById("viewListFromLink").value = "";
                } 
                else if (names.length != 0) {
                    removeList();
                    for (let i = 0; i < names.length; i++) {
                        shoppingList.push(names[i]);
                        shoppingListCategory.push(categories[i]);
                        itemCompletionStatus.push(purchaseStatus[i]);
                        shoppingListQuantity.push(quantities[i]);
                        shoppingListColour.push(colours[i]);
                        if (itemCompletionStatus[i] === 0) {
                            itemCompletionStatus[i] = false;
                        } else if (itemCompletionStatus[i] === 1) {
                            itemCompletionStatus[i] = true;
                        }
                    }
                    document.getElementById("viewListFromLink").value = "";

                    renderCards();
                }
            }
        });

    } else {
        alert("Token should only contain numbers: " + document.getElementById("viewListFromLink").innerHTML);
        document.getElementById("viewListFromLink").value = "";
    }
}

function categoryDropdownShow(ID) {
    if(ID.includes("_")) {
        let index = ID.split("_")[1];
        document.getElementById("categoryDropdown_"+index).classList.toggle("show");
        document.getElementById(ID).innerHTML = shoppingListCategory[index];
    }
    else
    {
        document.getElementById("categoryDropdown").classList.toggle("show");
        document.getElementById("dropdownButton").innerHTML = dropdownText;// + " &#11165";
    }
}

function categoryDropdownHide() {
    let dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
}

window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) 
    {
        if(e.target.parentNode.id.includes('categoryDropdown')) {

            if(e.target.parentNode.id.includes("_")){
                var index = e.target.parentNode.id.split("_")[1];
                shoppingListCategory[index] = e.target.innerHTML;

                document.getElementById("dropdownButton_"+index).innerHTML = shoppingListCategory[index];
                editCategory("categoryDropdown_"+index);
            }
            else {
                dropdownText = e.target.innerHTML
                document.getElementById("dropdownButton").innerHTML = dropdownText;// + ' &#11167';
            }
        }
        else {
            document.getElementById("dropdownButton").innerHTML = dropdownText;// + ' &#11167';
        }
        categoryDropdownHide();
    }
  }

function createCardCategoryDropdown(i) {
    let categoryElement = document.createElement("div");
        categoryElement.className = "dropdown";
        categoryElement.id = "ddDiv_"+i;

        let categoryElementButton = document.createElement("button");
        categoryElementButton.className = "btn dropbtn";
        categoryElementButton.id = "dropdownButton_"+i;
        categoryElementButton.type = "button";
        categoryElementButton.setAttribute("onclick", "categoryDropdownShow(id)");
        categoryElementButton.innerHTML = shoppingListCategory[i];

        let categoryElementDropdown = document.createElement("div");
        categoryElementDropdown.className = "dropdown-content";
        categoryElementDropdown.id = "categoryDropdown_"+i;
        categoryElementDropdown.style.left = "33%";
        //categoryElementDropdown.align = "middle";

        var dropdownItemArray = [];

        for(let j=0; j<9; j++)
        {
            dropdownItemArray[j] = (document.createElement("a"));
            dropdownItemArray[j].style.textAlign = "left";
            dropdownItemArray[j].id = "categoryDropdown_"+i+"_Item_"+j;
        }

        
        dropdownItemArray[0].innerHTML = "Baked Goods";
        dropdownItemArray[1].innerHTML = "Beverages";
        dropdownItemArray[2].innerHTML = "Dairy";
        dropdownItemArray[3].innerHTML = "Fresh Produce";
        dropdownItemArray[4].innerHTML = "Frozen Foods";
        dropdownItemArray[5].innerHTML = "Hygiene";
        dropdownItemArray[6].innerHTML = "Meat";
        dropdownItemArray[7].innerHTML = "Non-perishables";
        dropdownItemArray[8].innerHTML = "Other";

        for(let j=0; j<9; j++)
        {
            categoryElementDropdown.appendChild(dropdownItemArray[j]);
        }
        
        categoryElement.appendChild(categoryElementButton);
        categoryElement.appendChild(categoryElementDropdown);

        return categoryElement;
}

function renderCards() {
    // Get the element that will contain the cards
    let container = document.getElementById('list-container')

    // Remove all cards before re-adding new cards. 
    // This ensures that there are no duplicate cards
    // TODO: More efficient way to do this
    while (container.hasChildNodes()) {
        container.removeChild(container.firstChild);
    }

    for (let i = 0; i < shoppingList.length; i++) {

        let cardDiv = document.createElement("div");
        cardDiv.className = "card";
        cardDiv.id = "list-entry_" + i.toString();

        let itemElement = document.createElement("span");
        itemElement.id = "shoppingList_" + i.toString();
        itemElement.className = "shoppingListItem";

        itemElement.setAttribute("onmouseover", "makeEditable(id, true)");
        itemElement.setAttribute("onfocusout", "editItem(id)");
        itemElement.setAttribute("onkeydown", "submitNameChangesOnEnter(event, id)");

        let itemName = document.createTextNode(shoppingList[i]);

        var categoryElement = createCardCategoryDropdown(i);

        let quantityElement = document.createElement("span");
        quantityElement.id = "shoppingListQuantity_" + i.toString();
        quantityElement.className = "shoppingListQuantity";
        let quantityAmount = document.createTextNode(shoppingListQuantity[i]);
        let quantityMultiplier = document.createElement("span");
        quantityMultiplier.className = "multiplier";
        let quantityText = document.createTextNode("X");

        quantityElement.setAttribute("onmouseover", "makeEditable(id, true)");
        quantityElement.setAttribute("onfocusout", "editQuantity(id)");
        quantityElement.setAttribute("onkeydown", "submitQuantityChangesOnEnter(event, id)");

        itemElement.appendChild(itemName);
        quantityElement.appendChild(quantityAmount);
        quantityMultiplier.appendChild(quantityText);

        let checkboxDiv = document.createElement("div");
        let checkBox = document.createElement("input");
        checkBox.type = "checkbox";
        if (itemCompletionStatus[i] == 0) {
            checkBox.checked = false;
        } else if (itemCompletionStatus[i] == 1) {
            checkBox.checked = true;
        }
        checkBox.id = "purchaseStatus_" + i.toString();

        checkBox.setAttribute("onclick", "editPurchaseStatus(id)");
        let purchasedText = document.createTextNode("Purchased  ");
        checkboxDiv.appendChild(purchasedText);
        checkboxDiv.appendChild(checkBox);

        let deleteDiv = document.createElement("div");
        let deleteButton = document.createElement("I");

        deleteButton.id = "deleteButton_"+i;
        deleteButton.setAttribute("onclick", "deleteItem(id)");
        deleteButton.className = "fa fa-times-circle";

        deleteDiv.align = "right";
        deleteDiv.appendChild(deleteButton);

        cardDiv.appendChild(deleteDiv);
        cardDiv.appendChild(itemElement);
        cardDiv.appendChild(quantityMultiplier);
        cardDiv.appendChild(quantityElement);
        cardDiv.appendChild(categoryElement);
        cardDiv.appendChild(checkboxDiv);

        container.appendChild(cardDiv);

        document.getElementById(cardDiv.id).style.backgroundColor = shoppingListColour[i];
    }
}

function storeItem() {
    let completedStatus = false;
    let quantity_value = document.getElementById("ShoppingListQuantity").value;
    let listIndex = shoppingList.length + 1; // Add 1 because the new item hasn't been added yet 
    let item_colour = document.getElementById("itemColor").value;
    if (quantity_value.match(/^[0-9]+$/) != null) {
        var payload = {
            name: document.getElementById("ShoppingListItem").value,
            category: dropdownText,
            quantity: quantity_value,
            token: token,
            completed: completedStatus,
            arrayIndex: listIndex,
            colour: item_colour,
        };

        $.ajax({
            url: "/items",
            type: "POST",
            contentType: "application/json",
            processData: false,
            data: JSON.stringify(payload),
            complete: function(data) {
                addItem('none', 'none', false, quantity_value, item_colour);
            }
        });
    } else {
        alert("Quantity should only contain numbers");
        document.getElementById("ShoppingListQuantity").value = "";
    }
}

// set the length of the string
var stringLength = 15;

// list containing characters for the random string
var stringArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

function generateToken() {

    var randomString = "";

    // build a string with random characters
    for (var i = 1; i < stringLength; i++) {
        var randomNumber = Math.ceil(Math.random() * stringArray.length) - 1;
        randomString = randomString + stringArray[randomNumber];
    }
    return randomString;
}

function printURL() {
    let linkContainer = document.getElementById('sharingLink');
    while (linkContainer.hasChildNodes()) {
        linkContainer.removeChild(linkContainer.firstChild);
    }

    let resultURL = token;
    document.getElementById("sharingLink").value = resultURL;

}


function copyLink() {
    var copyText = document.getElementById("sharingLink");
    copyText.select();
    document.execCommand("Copy");
}

function toggleLinkSubmit() {
    var link = document.getElementById("viewListFromLink").value;

    if (link.length === 0) {
        document.getElementById("navigateToLink").disabled = true;
    } else
        document.getElementById("navigateToLink").disabled = false;
}

function viewList(listName) {
    token = document.getElementById("viewListFromLink").value;
    if (token.match(/^[0-9]+$/) != null) {
        removeList();
        $.ajax({
            url: "/items/" + token.toString(),
            type: "GET",
            contentType: "application/json",
            async: true,
            success: function(resp) {
                loadSharedEmails();
                getNotes();
                let nameArray = (resp);
                let names = nameArray.map(function(a) { return a.name; });
                let categories = nameArray.map(function(a) { return a.category; });
                let purchaseStatus = nameArray.map(function(a) { return a.completed; });
                let quantities = nameArray.map(function(a) { return a.quantity; });
                let colours = nameArray.map(function(a) { return a.colour; });
                if (listName !== null) {
                    document.getElementById("printName").textContent = "";
                    printListName(listName);
                    document.getElementById("viewListFromLink").value = "";
                    removeList();
                }
                if (names.length === 0 && listName === null) {
                    alert("No shopping list found");
                    document.getElementById("viewListFromLink").value = "";
                } else if (names.length !== 0) {
                    removeList();
                    for (let i = 0; i < names.length; i++) {
                        let item_name = names[i];
                        let item_category = categories[i];
                        let item_status = purchaseStatus[i];
                        let item_quantity = quantities[i];
                        let item_colour = colours[i];
                        if (item_status === 0) {
                            item_status = false;
                        } else if (item_status === 1) {
                            item_status = true;
                        }
                        addItem(item_name, item_category, item_status, item_quantity, item_colour);
                    }
                    document.getElementById("viewListFromLink").value = "";
                }

            }
        });

    } else {
        alert("Token should only contain numbers");
        document.getElementById("viewListFromLink").value = "";
    }
}

function removeList() {
    let listContainer = document.getElementById('list-container')
    shoppingList = [];
    shoppingListCategory = [];
    itemCompletionStatus = [];
    shoppingListQuantity = [];
    shoppingListColour = [];
    while (listContainer.hasChildNodes()) {
        listContainer.removeChild(listContainer.firstChild);
    }
}

function removeEmail(index, ID) {
    let element = document.getElementById(ID);
    let selector = "emailShareClass_" + index.toString();
    let email = document.getElementById(selector).textContent;
    element.parentNode.removeChild(element);

    var payload = {
        token: token,
        email: email
    };
    $.ajax({
        url: "/remove-share",
        type: "POST",
        contentType: "application/json",
        processData: false,
        data: JSON.stringify(payload),
        complete: function(data) {
            removeList();
        }
    });
}

function renderSharedEmail(email, ID) {
    let node = document.createElement("LI");
    node.id = "emailShare_" + ID.toString();
    let email_node = document.createElement("SPAN");
    email_node.id = "emailShareClass_" + ID.toString();
    let textnode = document.createTextNode(email);
    let cross_node = document.createElement("I");
    cross_node.className = "fa fa-times-circle";
    cross_node.id = "emailDelete_" + ID.toString();
    cross_node.onclick = function() { removeEmail(ID.toString(), node.id); };
    email_node.appendChild(textnode)
    node.appendChild(email_node);
    node.appendChild(cross_node);
    document.getElementById("email-list").appendChild(node);
}

function loadSharedEmails() {
    document.getElementById("email-list").innerHTML = "";

    $.ajax({
        url: "/share/" + token.toString(),
        type: "GET",
        contentType: "application/json",
        async: true,
        success: function(resp) {
            let emailArray = (resp);
            let emails = emailArray.map(function(a) { return a.email; });
            let uniqueEmails = [...new Set(emails)]
            for (let i = 0; i < uniqueEmails.length; i++) {
                renderSharedEmail(uniqueEmails[i], i);
            }
        }
    });
}

function shareEmail() {
    let email = document.getElementById("email-share").value;
    document.getElementById("email-share").value = "";

    var payload = {
        token: token,
        email: email,
    };

    $.ajax({
        url: "/share",
        type: "POST",
        contentType: "application/json",
        processData: false,
        data: JSON.stringify(payload),
        complete: function(data) {
            loadSharedEmails();
        }
    });
}

function clearDB() {
    var payload = {};
    $.ajax({
        url: "/delete",
        type: "POST",
        contentType: "application/json",
        processData: false,
        data: JSON.stringify(payload),
        complete: function(data) {
            removeList();
        }
    });
}

function setColor() {
    var x = document.getElementById("listColor").value;
    document.getElementById("list-container").style.backgroundColor = x;
}

function setDefaultColor() {
    document.getElementById('itemColor').value = "#fafafa";
}

function on() {
    document.getElementById("overlay").style.display = "block";
}

function off() {
    document.getElementById("overlay").style.display = "none";
}

function addListName() {
    document.getElementById("nameOverlay").style.display = "block";
}

function saveNotes() {
    let notes = document.getElementById("notesBox").value;
    var payload = {
        token: token,
        name: name,
        notes: notes,
    };
    $.ajax({
        url: "/add-notes",
        type: "POST",
        contentType: "application/json",
        processData: false,
        data: JSON.stringify(payload),
        complete: function(data) {}
    });
}

function saveListName() {
    let name = document.getElementById("listName").value;
    document.getElementById("nameOverlay").style.display = "none";
    document.getElementById("printName").value = name;
    document.getElementById("listName").value = "";
    let notes = document.getElementById("notesBox").value;
    printListName(name);
    var payload = {
        token: token,
        name: name,
        notes: notes,
    };
    $.ajax({
        url: "/add-name",
        type: "POST",
        contentType: "application/json",
        processData: false,
        data: JSON.stringify(payload),
        complete: function(data) {}
    });
}

function getListName() {
    token = document.getElementById("viewListFromLink").value;
    document.getElementById("secondOverlay").style.display = "none";
    document.getElementById("printName").textContent = "";
    $.ajax({
        url: "/name/" + token.toString(),
        type: "GET",
        contentType: "application/json",
        async: true,
        success: function(resp) {
            let nameArray = (resp);
            let name = nameArray.map(function(a) { return a.name; });

            if (name.length === 0) {
                name[0] = null;
            }
            viewList(name[0]);
        }
    });
}

function getNotes() {
    token = document.getElementById("viewListFromLink").value;
    document.getElementById("notesBox").value = "";
    $.ajax({
        url: "/notes/" + token.toString(),
        type: "GET",
        contentType: "application/json",
        async: true,
        success: function(resp) {
            let notesArray = (resp);
            let notes = notesArray.map(function(a) { return a.notes; });

            if (notes.length === 0) {
                notes[0] = "";
            }
            document.getElementById("notesBox").value = notes[0];
        }
    });
}

function cancelAddName() {
    document.getElementById("nameOverlay").style.display = "none";

}

function printListName(name) {
    document.getElementById("printName").innerHTML = "";
    let printedName = document.createTextNode(name);
    document.getElementById("printName").appendChild(printedName);
}