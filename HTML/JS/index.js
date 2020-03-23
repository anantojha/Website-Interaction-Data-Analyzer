var mystring ="";
var symbols ="";
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

function entered(str){
    var str = document.getElementById("text1").value;
    document.getElementById("text1").value = "";
    if(str == mystring)
        alert("You got it right");
    else
        alert("You got it wrong it");
    
}