console.log("Let's get this party started!");
let currentIndex = 0;

document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const searchTerm = document.getElementById('searchTerm').value.trim();
    if (!searchTerm) {
        alert('Please enter a search term.');
        return;
    }

    const apiKey = 'MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym';
    const apiUrl = `http://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=${apiKey}`;

    axios.get(apiUrl)
        .then(response => {
            console.log(response.data);
            
          
                const gifDisplay = document.getElementById('gif-display');
                const gifs = response.data.data; 
                if (gifs.length > 0) {
                    const gif = gifs[currentIndex]; 
                    const img = document.createElement('img');
                    img.src = gif.images.fixed_height.url;
                    img.alt = gif.title;
                    img.classList.add('gifs'); 
                    gifDisplay.appendChild(img);

             
                    currentIndex = (currentIndex + 1) % gifs.length;
                } else {
                
                    const errorMessage = document.createElement('p');
                    errorMessage.textContent = 'No GIF found.';
                    gifDisplay.appendChild(errorMessage);
                }
          
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
        document.querySelector('.removebtn').addEventListener('click', function () {
            const gifDisplay = document.getElementById('gif-display');
            gifDisplay.innerHTML = '';
        });
});