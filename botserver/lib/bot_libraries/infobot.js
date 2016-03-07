var apiai = require("apiai")

//TODO: move keys into apiai-config.js or something
var app = apiai("6e2d55c35974485a9e4d4834669426f4", "f8090a6b-5c13-4d9e-9a62-9cc62e8c396e");

module.exports = function (botSettings, bot, botController){
    botController.on('direct_mention', function(bot, message) {

        if (message.type !== "message") return false;
        var request = app.textRequest(message.text);

        request.on('response', function(response) {
            console.log(response);
            bot.reply(message, response.result.metadata.speech);
        });

        request.on('error', function(error) {
            console.log(error);
        });

        request.end();
    });
};
