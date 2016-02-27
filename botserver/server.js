var express = require('express');
var app = express();
var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/botdb");

var Bot = require('./app/models/bot');


//body-parser is a body parsing middleware
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

//it will only be parsing JSON
app.use(bodyParser.json());

var router = express.Router();


router.route('/bots')
    .get(function(req, res){
        console.log("looking for bots");
        Bot.find(function(err, bots){
            if(err)
                res.send(err);
            res.json(bots);
        });
        console.log("found bot");
    });

app.use('/api', router);


//start the server
var port = process.env.PORT || 8080;
app.listen(port);
console.log('botserver now running on port ' + port);
