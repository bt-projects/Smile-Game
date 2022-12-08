const smileAPI_url = "https://marcconrad.com/uob/smile/api.php";

async function getAPI(url) {

    // Storing response
    const response = await fetch(url);

    // Storing data in json
    var data = await response.json();
    console.log(data);
    console.log(typeof data);
    console.log(data.question);

    /***************************************************************/
    // Fetching and displaying image from api
    function showImg(data) {
        document.getElementById('imgID').src = data.question;
    }

    // Getting data from input field
    function checkAnswer() {
        var inputData = document.getElementById("userValue").value;
        // console.log("solution datatype ", typeof data.solution, " and ", "input datatype ", typeof inputData);

        console.log("solution - ", data.solution, " input - ", inputData);

        if(inputData == data.solution) {
            console.log("Success");
            document.getElementById('nxtBtn').style.visibility = 'visible';
            document.getElementById('result').innerHTML = 'Correct';
            
        } else {
            console.log("not correct");
            document.getElementById('nxtBtn').style.visibility = 'hidden';
            document.getElementById('result').innerHTML = 'Not Correct';
        }
    }
    // calling checkAnswer() function
    document.getElementById('submit').addEventListener("click", checkAnswer);
    /***************************************************************/

    if(response) {
        showImg(data);
        // checkAnswer();
        showResult()
    }

}
    
// calling async function
getAPI(smileAPI_url);

function nextButton() {
    // location.reload();
    getAPI(smileAPI_url);
    document.getElementById('nxtBtn').style.visibility = 'hidden';
}

// Default
function showResult() {
    document.getElementById('result').innerHTML = 'Check Value';
}
