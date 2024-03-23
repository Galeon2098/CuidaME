// BUSCADOR

// Get the input field and list
const searchInput = document.getElementById('search');
const list = document.getElementById('my-chats').getElementsByTagName('li');

// Add event listener for input change
searchInput.addEventListener('input', function () {
    // Get the search query and convert to lowercase for case-insensitive search
    const query = this.value.toLowerCase();

    // Loop through each list item
    Array.from(list).forEach(function (item) {
        // Get the text content of the list item and convert to lowercase
        const text = item.textContent.toLowerCase();

        // Check if the search query is found in the text content
        // If found, display the list item, otherwise hide it
        if (text.includes(query)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
});