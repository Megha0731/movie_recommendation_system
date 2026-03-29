let isLoading = false;

function getRecommendations() {
    if (isLoading) return;  // prevent multiple calls
    isLoading = true;

    let movie = document.getElementById("movieInput").value;

    fetch('/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ movie: movie })
    })
    .then(response => response.json())
    .then(data => {
        let results = document.getElementById("results");
        results.innerHTML = "";

        data.forEach(movie => {
            let li = document.createElement("li");
            li.innerText = movie;
            results.appendChild(li);
        });

        isLoading = false;
    });
}