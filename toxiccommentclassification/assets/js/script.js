document.addEventListener('DOMContentLoaded', ()=>{
    // comment = "It was a bad movie";
    comment = "It was a great movie";

    async function getResponse(comment) {
        const api = 'http://127.0.0.1:8080/predict';

        const req = {
            'comment' : comment
        }

        const response = await fetch(api,{
                method : 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify(req)
            }
        )

        if (!response.ok) {
            const errorData = await response.json(); // Get error details
            console.log("Error response:", errorData); // Log error message
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        return data;
    }

    getResponse(comment);
})