var mystring ="";
var trackstr = ["","",""];
var count = 0;
var alarm = 0;

if(localStorage.getItem("count")==null){
    localStorage.setItem("count", 0);
}

if(localStorage.getItem("str")==null){
    localStorage.setItem("str", JSON.stringify(["","",""]));
}

function correct(){
    for(let i = 0; i < 7; i++){
        if (mystring[i] == "q")
            document.write('&#8593');
        else if (mystring[i] == "w")
            document.write('&#8593');
        else if (mystring[i] == "e")
            document.write('&#8599');
        else if (mystring[i] == "a")
            document.write('&#8592');
        else if (mystring[i] == "d")
            document.write('&#8594');
        else if (mystring[i] == "z")
            document.write('&#8601');
        else if (mystring[i] == "x")
            document.write('&#8595');
        else if (mystring[i] == "c")
            document.write('&#8600');
    }
}

function random(){
    count = localStorage.getItem("counting");
    for(let i = 0;i<7;i++){
        var temp = Math.floor(Math.random() * 8) + 1;
        if (temp == 1)
            mystring += "w";
        else if (temp == 2)
            mystring += "q";
        else if (temp == 3)
            mystring += "e";
        else if (temp == 4)
            mystring += "a";
        else if (temp == 5)
            mystring += "d";
        else if (temp == 6)
            mystring += "z";
        else if (temp == 7)
            mystring += "x";
        else if (temp == 8)
            mystring += "c";
    }
    var temp = JSON.parse(localStorage.getItem("str"));
    trackstr[localStorage.getItem("count")] = mystring;
    for(let i = 0; i < 3; i++){
        if(trackstr[i] == "")
            trackstr[i] = temp[i];   
    }
    localStorage.setItem("str", JSON.stringify(trackstr));

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

function setup(){
    /*document.getElementById("email1").disabled = true;
    document.getElementById("email2").disabled = true;
    document.getElementById("email3").disabled = true;
    document.getElementById("email4").disabled = true;
    document.getElementById("bank1").disabled = true;
    document.getElementById("bank2").disabled = true;
    document.getElementById("bank3").disabled = true;
    document.getElementById("bank4").disabled = true;
    document.getElementById("shop1").disabled = true;
    document.getElementById("shop2").disabled = true;
    document.getElementById("shop3").disabled = true;
    document.getElementById("shop4").disabled = true;*/
}

if (performance.navigation.type == 1) {
    localStorage.clear();
}
