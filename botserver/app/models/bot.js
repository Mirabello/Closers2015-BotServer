var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var BotSchema = new Schema({
    "active": Boolean,
    "service": String,
    "contollerType": String,
    "type": String,
    "teamID": String,
    "token" : String,
    "properties": {}
});


var Botkit = require('botkit');
var botController = Botkit.slackbot({
    debug: false
});

//Bot Methods
BotSchema.methods.start = function(){

    bot = botController.spawn({
        token: this.token
    })

    bot.startRTM();

    //activate event listeners for bot
    require('./bot_libraries/toneBot.js')(bot, botController);
};


module.exports = mongoose.model("Bot", BotSchema);
