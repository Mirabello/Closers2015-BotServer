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

    //test route to return all bots in a list
    //.get(function(req, res){
        //Bot.find(function(err, bots){
            //if(err)
                //res.send(err);
            //res.json(bots);
        //});
    //})


    //create new bot
    .post(function(req, res){
        var bot = Bot(req.body.bot);

        bot.save( function(err){
            console.log(req.body);
            if (err)
                res.send(err);
            res.json({ message: 'Bot created!' });
        });

        bot.start();
    });


router.route('/bots/:bot_id')

    //get a single bot by id
    .get(function(req, res){
        Bot.findById(req.params.bot_id, function(err, bot){
            if (err)
                res.send(err);
            res.json(bot);
        });
    })


    //update the properties of a single bot by id
    .put(function(req, res){
        Bot.findById(req.params.bot_id, function(err, bot){
            if (err)
                res.send(err);

            //caller will include the properties of bot in reqeust
            bot.properties = req.body.properties;
            bot.save(function(err){
                if(err)
                    res.send(err);
                res.json({ message: 'Bot updated!' });
            });
        });
    })


    //delete the bot by id
    .delete(function(req,res){
        Bot.remove({
            _id: req.params.bot_id
        }, function(err, bot){
            if (err)
                res.send(err);
            res.json({ message: 'Deleted bot!' });
        });
    });




app.use('/api', router);


//start the server
var port = process.env.PORT || 8080;
app.listen(port);
console.log('botserver now running on port ' + port);
