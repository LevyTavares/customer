document.getElementById('queueForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var name = document.getElementById('nameInput').value;
    var queueList = document.getElementById('queueItems');
    var newItem = document.createElement('li');
    newItem.textContent = name;
    queueList.appendChild(newItem);
    document.getElementById('nameInput').value = '';
});