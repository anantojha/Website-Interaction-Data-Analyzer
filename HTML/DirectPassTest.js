
var express = require('express');
var fs = require('fs');
var id = 100;
var app = express();

app.use(express.json());
app.set('view engine','ejs');

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
