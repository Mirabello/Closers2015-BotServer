var watson = require('watson-developer-cloud');
var apis = require('./config.js')(watson);

module.exports = function (bot, botController){
    botController.on('ambient', function(bot, message) {
        if (message.type !== "message") return false;

        apis.tone_analyzer.tone({text: message.text}, function(err, tone){

            var toneCategory = tone.document_tone.tone_categories[0] ;

            var toneScores = {
                anger: toneCategory.tones[0].score,
                disgust: toneCategory.tones[1].score,
                fear: toneCategory.tones[2].score,
                joy: toneCategory.tones[3].score,
                sadness: toneCategory.tones[4].score
            }

            console.log(toneScores);


            var responses = {
                anger:[
                    "Settle down! There is no reason to be angry",
                    "Simmer down now! You'll give youself a hear attack!"
                ],
                disgust: [
                    "yeah.....ewww",
                    "oy.....now I am going to be sick"
                ],
                fear: [
                    "Don't be scared! I will protect you :)",
                    "OH NO!!!!"
                ],
                joy: [
                    "It looks like you are feeling happy today. Good stuff!",
                    "Give me some of whatever this person is smoking!"
                ],
                sadness: [
                    "Don't be sad. I am here to comfort you!",
                    "Aww cheer up motherfucker!"
                ]
            };

            var dominantScore = 0;
            var dominantTone;
            for(var tone in toneScores){
                if(toneScores[tone] > dominantScore){
                    dominantTone = tone;
                    dominantScore = toneScores[tone];
                }
            }

            var threshold = 0.6;

            if(dominantScore > threshold){
                var responseIndex = Math.floor(Math.random() * responses[dominantTone].length);
                bot.reply(message, responses[dominantTone][responseIndex]);
                console.log("Dominant tone: " + dominantTone + " , Score: " + dominantScore);
            }
        });
    });

};
