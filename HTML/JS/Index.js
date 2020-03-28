var mystring ="";
var trackstr = ["","",""];
var count = 0;
var suc = 0;
var fail = 0;
var order = [0,1,2];

//Converts the string to the arrows
function correct(){
    var temp = localStorage.getItem("str");
    console.log(temp)
    for(let i = 0; i < 7; i++){
        if (temp[i] == "q")
            document.write('&#8598;');
        else if (temp[i] == "w")
            document.write('&#8593');
        else if (temp[i] == "e")
            document.write('&#8599');
        else if (temp[i] == "a")
            document.write('&#8592');
        else if (temp[i] == "d")
            document.write('&#8594');
        else if (temp[i] == "z")
            document.write('&#8601');
        else if (temp[i] == "x")
            document.write('&#8595');
        else if (temp[i] == "c")
            document.write('&#8600');
    }
}

//randomizes the password
function random(){
    mystring = "";
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
    trackstr[count] = mystring;


}

//Checks if the entered string is correct
function entered(str){
    var str = document.getElementById("text1").value;
    document.getElementById("text1").value = "";
    if(str == mystring)
        alert("You got it right");
    else
        alert("You got it wrong it");    
}

//window close
function done(){
    window.close();
}

//Goes to the next password
function increase(){
    if (localStorage.getItem("suc") == 1){
        suc += 1;
        localStorage.setItem("suc",0);
    }
    else{
        fail += 1;
    }
    attempt = 0;
    count++;
    setup();
}

//Openes the page for memorizing and praticing passwords
function opened(){
    random();
    localStorage.setItem("str", trackstr[count]);
    window.open('Password.html','_blank','titlebar=no,toolbar=no,location=no, height = 350,width = 500');
    setup();
}

//function set up to shuffle the order 
function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
}
  
//used to show the parts in a diffrent order
function show(){
    shuffle(order);
    for(let i = 0; i < 3; i++){
        if (order[i] == 0){
            document.write("<h4 id = 'text4'> Email <br> Only 3 attempts allowed <br><br> <button onclick = 'pass()' id = 'email3'>Create</button><button onclick = 'increase()' id = 'email4'>Next</button></h4>");
        }
        else if (order[i]== 1){
            document.write("<h4 id = 'text5'>Bank <br> Only 3 attempts allowed <br><br>  <button onclick = 'pass()' id = 'bank3'>Create</button><button onclick = 'increase()' id = 'bank4'>Next</button></h4>");
        }
        else if(order[i]==2){   
            document.write("<h4 id = 'text6'>Shopping <br> Only 3 attempts allowed <br><br>  <button onclick = 'pass()' id = 'shop3'>Create</button><button onclick = 'submit()' id = 'shop4'>Next</button></h4>");
        }
    }
    
}

//All the things that needs to be set up for index including disabled buttons
function setup(){   
    if(count==0){
        document.getElementById("email1").disabled = false;
        document.getElementById("email2").disabled = false;
        document.getElementById("email3").disabled = true;
        document.getElementById("email4").disabled = true;
        document.getElementById("bank1").disabled = true;
        document.getElementById("bank2").disabled = true;
        document.getElementById("bank3").disabled = true;
        document.getElementById("bank4").disabled = true;
        document.getElementById("shop1").disabled = true;
        document.getElementById("shop2").disabled = true;
        document.getElementById("shop3").disabled = true;
        document.getElementById("shop4").disabled = true;
        if(trackstr[0]=="")
            document.getElementById("email2").disabled = true;
        document.getElementById("text1").style = "border:1px solid black; background-color: #c5fcc8";
        document.getElementById("text2").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text3").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text4").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text5").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text6").style = "border:1px solid black; background-color: #bababa";
    }
    else if (count ==1){
        document.getElementById("email1").disabled = true;
        document.getElementById("email2").disabled = true;
        document.getElementById("email3").disabled = true;
        document.getElementById("email4").disabled = true;
        document.getElementById("bank1").disabled = false;
        document.getElementById("bank2").disabled = false;
        document.getElementById("bank3").disabled = true;
        document.getElementById("bank4").disabled = true;
        document.getElementById("shop1").disabled = true;
        document.getElementById("shop2").disabled = true;
        document.getElementById("shop3").disabled = true;
        document.getElementById("shop4").disabled = true;
        if(trackstr[1]=="")
            document.getElementById("bank2").disabled = true;
        document.getElementById("text1").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text2").style = "border:1px solid black; background-color: #c5fcc8";
        document.getElementById("text3").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text4").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text5").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text6").style = "border:1px solid black; background-color: #bababa";
    }
    else if (count==2){
        document.getElementById("email1").disabled = true;
        document.getElementById("email2").disabled = true;
        document.getElementById("email3").disabled = true;
        document.getElementById("email4").disabled = true;
        document.getElementById("bank1").disabled = true;
        document.getElementById("bank2").disabled = true;
        document.getElementById("bank3").disabled = true;
        document.getElementById("bank4").disabled = true;
        document.getElementById("shop1").disabled = false;
        document.getElementById("shop2").disabled = false;
        document.getElementById("shop3").disabled = true;
        document.getElementById("shop4").disabled = true;
        if(trackstr[2]=="")
            document.getElementById("shop2").disabled = true;
        document.getElementById("text1").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text2").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text3").style = "border:1px solid black; background-color: #c5fcc8";
        document.getElementById("text4").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text5").style = "border:1px solid black; background-color: #bababa";
        document.getElementById("text6").style = "border:1px solid black; background-color: #bababa";
    }
    else if (count == 3){
        if(order[0]==0){
            first();
        }
        else if (order[0]==1){
            sec();
        }
        else{
            third();
        }
    }
    else if (count == 4){
        if(order[1]==0){
            first();
        }
        else if (order[1]==1){
            sec();
        }
        else{
            third();
        }
    }
    else if(count == 5){
        if(order[2]==0){
            first();
        }
        else if (order[2]==1){
            sec();
        }
        else{
            third();
        }
    }
}

//Continuation of setup but for the email Only 3 attempts allowed
function first(){
    document.getElementById("email1").disabled = true;
    document.getElementById("email2").disabled = true;
    document.getElementById("email3").disabled = false;
    document.getElementById("email4").disabled = false;
    document.getElementById("bank1").disabled = true;
    document.getElementById("bank2").disabled = true;
    document.getElementById("bank3").disabled = true;
    document.getElementById("bank4").disabled = true;
    document.getElementById("shop1").disabled = true;
    document.getElementById("shop2").disabled = true;
    document.getElementById("shop3").disabled = true;
    document.getElementById("shop4").disabled = true;

    if(attempt == 0)
        document.getElementById("email4").disabled = true;
    if(attempt == 3)
        document.getElementById("email3").disabled = true;
    document.getElementById("text1").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text2").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text3").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text4").style = "border:1px solid black; background-color: #c5fcc8";
    document.getElementById("text5").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text6").style = "border:1px solid black; background-color: #bababa";
}

//Continuation of setup but for the bank Only 3 attempts allowed
function sec(){
    document.getElementById("email1").disabled = true;
    document.getElementById("email2").disabled = true;
    document.getElementById("email3").disabled = true;
    document.getElementById("email4").disabled = true;
    document.getElementById("bank1").disabled = true;
    document.getElementById("bank2").disabled = true;
    document.getElementById("bank3").disabled = false;
    document.getElementById("bank4").disabled = false;
    document.getElementById("shop1").disabled = true;
    document.getElementById("shop2").disabled = true;
    document.getElementById("shop3").disabled = true;
    document.getElementById("shop4").disabled = true;
    if(attempt == 0)
        document.getElementById("bank4").disabled = true;
    if(attempt == 3)
        document.getElementById("bank3").disabled = true;
    document.getElementById("text1").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text2").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text3").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text4").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text5").style = "border:1px solid black; background-color: #c5fcc8";
    document.getElementById("text6").style = "border:1px solid black; background-color: #bababa";
}

//Continuation of setup but for the shop Only 3 attempts allowed
function third(){
    document.getElementById("email1").disabled = true;
    document.getElementById("email2").disabled = true;
    document.getElementById("email3").disabled = true;
    document.getElementById("email4").disabled = true;
    document.getElementById("bank1").disabled = true;
    document.getElementById("bank2").disabled = true;
    document.getElementById("bank3").disabled = true;
    document.getElementById("bank4").disabled = true;
    document.getElementById("shop1").disabled = true;
    document.getElementById("shop2").disabled = true;
    document.getElementById("shop3").disabled = false;
    document.getElementById("shop4").disabled = false;
    if(attempt == 0)
        document.getElementById("shop4").disabled = true;
    if(attempt == 3){
        document.getElementById("shop3").disabled = true;
    }
    document.getElementById("text1").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text2").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text3").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text4").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text5").style = "border:1px solid black; background-color: #bababa";
    document.getElementById("text6").style = "border:1px solid black; background-color: #c5fcc8";   
}


//Send all the data to the file
function submit(){
    alert("Thank you we are done");
}

function pass(){
    localStorage.setItem("str2", trackstr[order[count-3]]);
    window.open('Testing.html','_blank','titlebar=no,toolbar=no,location=no, height = 220,width = 500');
    attempt++;
    setup();
}

//Check passwords for Testing.html
function check(){
    var temp = localStorage.getItem("str2")
    console.log(temp, document.getElementById("in").value)
    if(temp == document.getElementById("in").value){
        localStorage.setItem("suc",1);
        alert("You got it right");
        window.close();
    }
    else{
        document.getElementById("in").value = "";
        alert("You got it wrong");
        window.close();
    }
}

if (performance.navigation.type == 1) {
    localStorage.clear();
}
