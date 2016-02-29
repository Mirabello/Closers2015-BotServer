var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/botdb");

var Bot = require('./app/models/bot');

var Botkit = require('botkit');

module.exports = function(){


    var botInstance = function (botModel){
        //botModel...not the best name, but this
        //should just be the instantiated db model
        this.botModel = botModel;

        this.botController = Botkit.slackbot({
            debug: false
        });

        this.botInstance = botController.spawn({
            token: this.botModel.token
        });

        //TODO get botType from bot.Model.botType
        this.initHandlers = function(){
            require('./toneBot.js')(botInstance, botController);
        };

        this.start = function(){
            this.startRTM();
        };
    }

    var botManager = function (){
        this.botList = {
        };

        this.init = function (){
            //loop through bots in database
            //TODO: make model method to return list of bots?
            Bot.find(function(err, bots){
                if(err)
                    console.log(err);
                //for each one. create an instance
                for(var bot in bots){
                    if(bot.active){
                        var newBotInstance = botInstance(bot);
                        newBotInstance.initHandlers();
                        newBotInstance.start();

                        //add bot to this.botList, with the key being the id
                        this.botList[bot._id] = newBot;
                    }
                }
            });
        };
    };

    return botManager;
};

