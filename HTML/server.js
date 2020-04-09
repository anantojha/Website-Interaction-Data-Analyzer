/*
    app.post('/data') - sends info to the csv from the html
    app.get('/') - takes you to the home page/ DirectPass.ejs
    app.get('/user') - sends the info to the form of what user they are
    app.get('/Password.html') - sends you to the Password.ejs
    app.get('/Testing.html') - sends you to the Testing.ejs

*/
var express = require('express');
var fs = require('fs');
var id = 100;
var app = express();
app.use( express.static('public'));
app.use(express.json());
app.set('view engine','ejs');

console.log("Server has started");

app.post('/data', (req, res)=>{
    const data = req.body;
    fs.appendFile('database.csv', data + '\n', (err) => {
        if (err) console.error('Couldn\'t append the data');
        console.log('The data was appended to file!');
    });
    res.end();
});

app.get('/',function (req, res){
    res.render('DirectPass');
});

app.get('/user',function (req,res){
    let temp = "drt" + id;
    id++;
    res.json({id:temp});
})

app.get('/Password.html', function (req, res){
    res.render('Password');
});
app.get('/Testing.html', function (req, res){
    res.render('Testing');
});

app.listen(8000);
