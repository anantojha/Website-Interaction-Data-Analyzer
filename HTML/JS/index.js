var mystring ="";
var symbols ="";
var trackstr = ["","",""];
var tracksym = ["","",""];
var count = 0;

if(localStorage.getItem("count")==null){
    localStorage.setItem("count", 0);
}

if(localStorage.getItem("str")==null){
    localStorage.setItem("str", JSON.stringify(["","",""]));
}

if(localStorage.getItem("sym")==null){
    localStorage.setItem("sym", JSON.stringify(["","",""]));
}

function random(){
    count = localStorage.getItem("counting");
    for(let i = 0;i<7;i++){
        var temp = Math.floor(Math.random() * 8) + 1;
        if (temp == 1){
            mystring += "w";
            symbols += "↑";
        }

        else if (temp == 2){
            mystring += "q";
            symbols += "↖";;
        }
        else if (temp == 3){
            mystring += "e";
            symbols += "↗"
        }
        else if (temp == 4){
            mystring += "a";
            symbols += "←";
        }
        else if (temp == 5){
            mystring += "d";
            symbols += "→";
        }
        else if (temp == 6){
            mystring += "z";
            symbols += "↙";
        }
        else if (temp == 7){
            mystring += "x";
            symbols += "↓";
        }
        else if (temp == 8){
            mystring += "c";
            symbols += "↘";
        }
        
    }
    var temp = JSON.parse(localStorage.getItem("str"));
    var temp2 = JSON.parse(localStorage.getItem("sym"));
    tracksym [localStorage.getItem("count")] = symbols;
    trackstr[localStorage.getItem("count")] = mystring;
    for(let i = 0; i < 3; i++){
        if(trackstr[i] == ""){
            trackstr[i] = temp[i];
        }
        if(tracksym[i] == ""){
            tracksym[i] = temp2[i];
        }
    }
    localStorage.setItem("str", JSON.stringify(trackstr));
    localStorage.setItem("sym", JSON.stringify(tracksym));

}

function entered(str){
    var str = document.getElementById("text1").value;
    document.getElementById("text1").value = "";
    if(str == mystring)
        alert("You got it right");
    else
        alert("You got it wrong it");    
}

function done(){
    location.replace("Index.html");
}

function increase(){
    if(parseInt(localStorage.getItem("count")) < 2){
        localStorage.setItem("count", parseInt(localStorage.getItem("count"))+1);
    }
}
function opened(){
    console.log("test");
    location.replace("Password.html");
    console.log("test");
}


if (performance.navigation.type == 1) {
    localStorage.clear();
}
