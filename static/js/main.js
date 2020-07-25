function getUserList(){
    fetch('/api/profiles/listAllUsers/')
    .then(res => res.json())
    .then(data => {
        showUserLists(data)
    })
    .catch(err => {
        console.error(err);
    })
}

function showUserLists(data){
    return data.map(user =>{
        showUserList(user);
    })
}

function createNode(element){
    return document.createElement(element);
}

function append(parent, el){
    return parent.appendChild(el);
}


function showUserList(user){
    const root = document.getElementById('root');
    const div = createNode('div');
    const name = createNode('p');
    const gender = createNode('p');
    const passportNo = createNode('p');
    const email = createNode('p');
    const address = createNode('p');
    const dateOfBirth = createNode('p');
    
    name.innerText = `Name: ${user.name}`;
    gender.innerText = `Gender: ${user.gender}`;
    passportNo.innerText = user.passportNo;
    email.innerText = user.email;
    address.innerText = user.address;
    dateOfBirth.innerText = user.dateOfBirth;

    append(div, name);
    append(div, gender);
    append(div, passportNo);
    append(div, email);
    append(div, address);
    append(div, dateOfBirth);
    append(root, div);
}

getUserList()