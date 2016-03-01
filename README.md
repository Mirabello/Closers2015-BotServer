# Closers-2015 BOTS: Final Byte Project

### Background:
We chose to build our final project around the concept of conversational commerce (#convconn) where much of future user interaction will occur within the context of a converstion.  In March 2016, the dominant players are [Slack] (www.slack.com) and in the near future, [Facebook Messenger] (https://www.messenger.com).

### Integration:
We created a Bot subscription landing page, where users who want to include our bots into their site will be able to configure 
a) choose which bot to download and
b) adjust the parameters of a particular bot


### Installation:
1. Node needs to be installed
2. mongoDB as well
3. Everything else should be in package.json
4. CD into the botserver folder
5. do npm install
   it should look like this:

```
module.exports = function (watson){
    return {
        personality_insights: watson.personality_insights({
          username: '0f635c39-46ea-4fd9-be58-6199798e3e45',
          password: 'hHsuHNcbE7WP',
          version: 'v2'
        }),

        tone_analyzer: watson.tone_analyzer({
          username: 'd015c389-688f-4449-8aee-c2135ac5ed7f',
          password: 'P7PLKxRbZKmK',
          version: 'v3-beta',
          version_date: '2016-02-11'
        })
    }
}
```


6. Start the app by running the following code:

```
node server.js
```






###Use Case:
Provide multiple interactions with users in the context of working inside the Slack app, including:

1. Super-Kai, the pre-customer Onboarding Bot
2. Mama-Kai, the company Culture Bot
3. Aziz_bot: the Watson API Conversation Tone Analyzer Bot
4. Teriyaki-boy:  the company Lunch Bot
5. Billy : the Dev Team's Daily Development Reporter Bot

