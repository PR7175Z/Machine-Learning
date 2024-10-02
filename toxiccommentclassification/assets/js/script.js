document.addEventListener('DOMContentLoaded', ()=>{

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
        return data;
    }

    document.getElementById('commentform').addEventListener('submit', async (e)=>{
        e.preventDefault();
        const cmt = document.querySelector('#commentform textarea').value;
        const resultdisplay = document.getElementById('result');
        const res = await getResponse(cmt);

        let resulttext = '';

        if(res['pred'] === 0){
            resulttext = 'Non Toxic';
        }else{
            resulttext = 'Toxic';
        }
        resultdisplay.innerHTML = `This comment is ${resulttext}`;
    });
})