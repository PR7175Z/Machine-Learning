document.addEventListener('DOMContentLoaded', ()=>{
    async function getResponse(comment) {
        api = 'http://127.0.0.1:8080/predict';

        const response = await fetch(api,{
            method : 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body:JSON.stringify(comment)
        })

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    }
})