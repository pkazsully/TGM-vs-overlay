
const serverUrl = 'http://127.0.0.1:5000';
const socket = io(serverUrl);

socket.on('playerUpdate', (data) => update(data));

socket.on('updateScores', (data) => updateScores(data));

socket.on('hide', () => {
    var p1Element = document.querySelector('.p1');
    var p2Element = document.querySelector('.p2');
    var middleElement = document.querySelector('.middle')
    // Add class to slide out elements
    middleElement.classList.add('slide-out-top');
    p1Element.classList.add('slide-out-left');
    p2Element.classList.add('slide-out-right');
})

socket.on('show', () => {
    
    var p1Element = document.querySelector('.p1');
    var p2Element = document.querySelector('.p2');
    var middleElement = document.querySelector('.middle')
    // Add class to slide out elements
    middleElement.classList.add('slide-in-top');
    p1Element.classList.add('slide-in-left');
    p2Element.classList.add('slide-in-right');
    setTimeout(function() {
        middleElement.classList.remove('slide-in-top');
        p1Element.classList.remove('slide-in-left');
        p2Element.classList.remove('slide-in-right');
        middleElement.classList.remove('slide-out-top');
        p1Element.classList.remove('slide-out-left');
        p2Element.classList.remove('slide-out-right');
    }, 600) 
})

const clear ={
    "match":{"firstTo":2},
    "players":[
        {
            "username":"","pfp":"/static/placeholder.png","rank":"X","country":"","flag_img":"/static/placeholder.png",
            "since":"","stats":[[0, 0, 0],[0, 0, 0],[0, 0,0],[0,0,0],[0,0,0]],"rival":""
        },
        {
            "username":"","pfp":"/static/placeholder.png","rank":"X","country":"","flag_img":"/static/placeholder.png",
            "since":"","stats":[[0, 0, 0],[0, 0, 0],[0, 0,0],[0,0,0],[0,0,0]],"rival":""
        }
    ]
}
temp = false;
socket.on('clear', () => {actualUpdate(clear)})

function updateScores(data){
    console.log("score update");
    document.getElementsByClassName("p1Score")[0].innerText = data.p1;
    document.getElementsByClassName("p2Score")[0].innerText = data.p2;
}

function actualUpdate(data){
    //initialize header
        //get the p1Name field
        p1Name = document.getElementsByClassName('p1name');
        //set p1 rank
        p1Name[0].children[0].src = letterToImg(data.players[0].rank);
        //set p1 name
        p1Name[0].children[1].innerText = data.players[0].username;
        //get the p2Name field
        p2Name = document.getElementsByClassName('p2name');
        //set p2 name
        p2Name[0].children[0].innerText = data.players[1].username;
        //set p2 rank
        p2Name[0].children[1].src = letterToImg(data.players[1].rank);
        //set the match count
        document.getElementsByClassName("sets")[0].innerText = data.match.firstTo;
        document.getElementsByClassName("p1Score")[0].innerText = "0";
        document.getElementsByClassName("p2Score")[0].innerText = "0";
        
        //get elements 
        icons = document.getElementsByClassName("icon");
        country = document.getElementsByClassName("country");
        since = document.getElementsByClassName("date");
        wins = document.getElementsByClassName("wins");
        losses = document.getElementsByClassName("loss");
        percent = document.getElementsByClassName("percent");
        rival = document.getElementsByClassName("name");

        //set p1
        //make referencing p1 easier
        p1 = data.players[0];       
        //set pfp                     
        icons[0].children[0].src = p1.pfp;  
        //set flag+country name         
        country[0].children[0].src = p1.flag_img;
        country[0].children[1].innerText = p1.country;
        //set fightcade join date
        since[0].innerText = p1.since;
        //convert htmlcollections to array, so can slice
        var temp = Array.from(wins);
        p1Wins = temp.slice(0, 5);
        temp = Array.from(losses)
        p1Loss = temp.slice(0,5);
        temp = Array.from(percent);
        p1Percent = temp.slice(0,5);
        //set up the stats table
        p1Wins.forEach((win, i) => win.innerText = p1.stats[i][0]);
        p1Loss.forEach((loss, i) => loss.innerText = p1.stats[i][1]);
        p1Percent.forEach((percent, i) => percent.innerText = p1.stats[i][2]);
        //set rival
        rival[0].innerText = p1.rival;
        

        //set p2
        //make referencing p2 easier
        p2 = data.players[1];       
        //set pfp                     
        icons[1].children[0].src = p2.pfp;  
        //set flag+country name         
        country[1].children[0].src = p2.flag_img;
        country[1].children[1].innerText = p2.country;
        //set fightcade join date
        since[1].innerText = p2.since;
        //convert htmlcollections to array, so can slice
        var temp = Array.from(wins);
        p2Wins = temp.slice(5);
        temp = Array.from(losses)
        p2Loss = temp.slice(5);
        temp = Array.from(percent);
        p2Percent = temp.slice(5);
        //set up the stats table
        p2Wins.forEach((win, i) => win.innerText = p2.stats[i][0]);
        p2Loss.forEach((loss, i) => loss.innerText = p2.stats[i][1]);
        p2Percent.forEach((percent, i) => percent.innerText = p2.stats[i][2]);
        //set rival
        rival[1].innerText = p2.rival;
}

function update(data){
    var p1Element = document.querySelector('.p1');
    var p2Element = document.querySelector('.p2');
    var middleElement = document.querySelector('.middle')
    // Add class to slide out elements
    middleElement.classList.add('slide-out-top');
    p1Element.classList.add('slide-out-left');
    p2Element.classList.add('slide-out-right');

    // Wait for the slide-out animation to complete before updating
    setTimeout(function() {
        actualUpdate(data);

        middleElement.classList.remove('slide-out-top');
        p1Element.classList.remove('slide-out-left');
        p2Element.classList.remove('slide-out-right');

        // Add class to slide in elements
        middleElement.classList.add('slide-in-top');
        p1Element.classList.add('slide-in-left');
        p2Element.classList.add('slide-in-right');

        // Wait for the slide-in animation to complete before removing the class
        setTimeout(function() {
            middleElement.classList.remove('slide-in-top');
            p1Element.classList.remove('slide-in-left');
            p2Element.classList.remove('slide-in-right');
        }, 600); // Adjust the timing to match your CSS animation duration
    }, 800); // Adjust the timing to match your CSS animation duration
    console.log("player update");
    
    
}

//take in rank as letter and return reference to rank img in imgs folder
function letterToImg(rank){
    switch (rank) {
        case("S"):
            return "/static/rank6.png";
        case("A"):
            return "/static/rank5.png";
        case("B") :
            return "/static/rank4.png";
        case("C") :
            return "/static/rank3.png"
        case("D"):
            return "/static/rank2.png"
        case("E"):
            return "/static/rank1.png"
        default:
            return "/static/rank0.png"

    }
}

