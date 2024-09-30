document.addEventListener('DOMContentLoaded', ()=>{
    comment = "It was a bad movie";
    // comment = "It was a great movie";

    async function getResponse(comment) {
        const api = 'http://127.0.0.1:8080/predict';
        const response = await fetch(api,{
                method : 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify({'comment':comment})
            }
        )

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        return data;
    }

    console.log(JSON.stringify({'comment':comment}));

    getResponse(comment);
})