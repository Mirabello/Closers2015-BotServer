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

//Bot Methods
//
//BotSchema.methods.start = function(){

//};


module.exports = mongoose.model("Bot", BotSchema);
