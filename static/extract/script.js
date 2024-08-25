document.getElementById('submitBtn').addEventListener('click', async () => {
    const urlInput = document.getElementById('urlInput').value;
    const urls = urlInput.split('\n').map(url => url.trim()).filter(url => url.length > 0);

    if (urls.length === 0) {
        alert("Please enter at least one URL.");
        return;
    }

    document.getElementById('loadingSpinner').classList.remove('hidden');

    try {
        const response = await fetch('/submit_song_urls', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ urls })
        });

        document.getElementById('loadingSpinner').classList.add('hidden');

        if (response.ok) {
            const result = await response.json();
            displayResults(result.songs);

            document.getElementById('toggleSection').classList.remove('hidden');
            document.getElementById('response').classList.remove('hidden');
        } else {
            document.getElementById('response').innerText = "Failed to submit URLs.";
        }
    } catch (error) {
        document.getElementById('loadingSpinner').classList.add('hidden');
        document.getElementById('response').innerText = "An error occurred: " + error.message;
    }
});

function displayResults(songs) {
    const tableBody = document.querySelector('#songsTable tbody');
    tableBody.innerHTML = '';

    songs.forEach((song, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="border px-4 py-2 min-w-4 number-column">${index + 1}</td>
            <td class="border px-4 py-2 title-column">${song.title}</td>
            <td class="border px-4 py-2 artist-column">${song.artist}</td>
            <td class="border px-4 py-2 url-column hidden break-all"><a href="${song.url}" target="_blank">${song.url}</a></td>
        `;
        tableBody.appendChild(row);
    });
}

function toggleColumn(columnClass) {
    const columnElements = document.querySelectorAll(`.${columnClass}`);
    columnElements.forEach(element => {
        element.classList.toggle('hidden');
    });
}
