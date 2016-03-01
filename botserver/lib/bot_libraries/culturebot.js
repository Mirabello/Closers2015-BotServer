module.exports = function (botSettings, bot, botController){
    botController.on('direct_mention', function(bot, message) {
        if (message.type !== "message") return false;
		bot.reply(message, "I am the culture bot. Fuck yeah!");
    });
};
