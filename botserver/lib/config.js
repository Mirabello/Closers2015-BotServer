module.exports = function (watson){
    return {
        personality_insights: watson.personality_insights({
          username: '****Username goes here***',
          password: '****Password goes here****',
          version: 'v2'
        }),

        tone_analyzer: watson.tone_analyzer({
          username: '****Username goes here***',
          password: '****Password goes here****',
          version: 'v3-beta',
          version_date: '2016-02-11'
        })
    }
}
