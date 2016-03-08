# Closers-2015 BOTS: Final Byte Project

### Background:
We chose to build our final project around the concept of conversational commerce (#convconn) where much of future user interaction will occur within the context of a converstion.  In March 2016, the dominant players are [Slack] (www.slack.com) and in the near future, [Facebook Messenger] (https://www.messenger.com).

### Integration:
We created a Bot subscription landing page, where users who want to include our bots into their site will be able to configure
a) choose which bot to download and
b) adjust the parameters of a particular bot


### Installation:
1. Install NodeJS
2. Install MongoDB
3. CD into the botserver folder and run 'npm install'
4. Sign up for an IBM Bluemix account and [get credentials for the Tone Analyzer API](https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/tone-analyzer/tutorial.shtml#credentials)
5. Add your IBM Watson credentials to 'botserver/lib/config.js' The file should be in the following format:
6. Start the app by running the following code:
7. go to \frontend and run

```
module.exports = function (watson){
    return {
        personality_insights: watson.personality_insights({
          username: '***YOUR USERNAME****',
          password: '****YOUR PASSWORD****',
          version: 'v2'
        }),

        tone_analyzer: watson.tone_analyzer({
          username: '***YOUR USERNAME****',
          password: '****YOUR PASSWORD****',
          version: 'v3-beta',
          version_date: '2016-02-11'
        })
    }
}
```


6. 

```
node server.js
```
7. 
```
pip3 install -r requirements.txt
```
 








###Use Case:
Provide multiple interactions with users in the context of working inside the Slack app, including:

1. Super-Kai, the pre-customer Onboarding Bot
2. Mama-Kai, the company Culture Bot
3. Aziz_bot: the Watson API Conversation Tone Analyzer Bot
4. Teriyaki-boy:  the company Lunch Bot
5. Billy : the Dev Team's Daily Development Reporter Bot


