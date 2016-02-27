var mongoose = require('mongoose');

var BotSchema = new Schema({
    "active": Boolean,
    "service": String,
    "contollerType": String,
    "botType": String,
    "teamID": String,
    "slackToken" : String,
    "options": {}
});

module.exports = mongoose.model("Bot", BotSchema);
