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
