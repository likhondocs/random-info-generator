document.getElementById('generate').addEventListener('click', async () => {
    const response = await fetch('/api/generate');
    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data, null, 2);
});
