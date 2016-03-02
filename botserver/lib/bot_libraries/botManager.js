/**
 * @botManager.js
 *
 * This module exports a botManager object. A botManager can:
 *  -load up active bot details from the database
 *  -wrap the bot information in a botWrapper object (which sets up
 *      their logic systems and slack connectivity)
 *  -start up the bots connection to slack
 *  -keep track of all running bots in the 'botList' property
 */


var mongoose = require("mongoose");
mongoose.createConnection("mongodb://localhost/botdb");
var Bot = require('../../app/models/bot');
var Botkit = require('botkit');



/**
 * botWrapper: a wrapper object to give a bot its logic system and slack connectivity
 *
 * @param {bot} botModel: unique information about bot, pulled from the database
 */
var botWrapper = function (botModel){
    this.botModel = botModel;

    this.botController = Botkit.slackbot({
        debug: false
    });

    this.slackBot = this.botController.spawn({
        token: this.botModel.token
    });


    /**
     * start:
     *
     * -load up the bots logic system (event handlers) by specifying bot type
     * -start up the connection to the slack api
     */
    this.start = function(){
        //botModel 'type' property must have same name as library file
        var botType = this.botModel.type;
        var eventHandlers = require('./' + botType + '.js')(this.botModel.properties, this.slackBot, this.botController);

        this.slackBot.startRTM();
    };

    //stop: disconnects bot from Slack API
    this.stop = function(){
        this.slackBot.closeRTM();
    };
}


/**
 * botManager: an object that is responsible for:
 *
 * -loading up all of the bots from the database
 * -instantiating and starting up the bots
 * -keeping a list of running bots in the botList property
 */
var botManager = function (){
    var self = this;
    this.botList = {};
    console.log("constructor botList: " + self.botList);

    this.init = function (){
        //loop through bots in database
        //TODO: make model method to return list of bots?
        Bot.find(function(err, bots){
            if(err)
                console.log(err);

            //for each one. create an instance
            for (var i = 0; i < bots.length; i++){
                if(bots[i].active){
                    self.addBot(bots[i]);
                }
            }
        });
    };

    //addBot(): adds bot to botList and starts it
    this.addBot = function (bot){
        var newBot = new botWrapper(bot);
        newBot.start();

        var botKey = bot._id;
        self.botList[botKey] = newBot;
    };

    //updateBot(): updates the bot settings
    this.updateBot = function (bot){
        //restart the bot with new settings
        var botKey = bot._id;
        self.botList[botKey].stop()
        self.addBot(bot);
    }
};

module.exports = function(){
    //instantiate the botManager and return instance
    return new botManager();
};

