var express = require('express');
var app = express();

//body-parser is a body parsing middleware
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

//it will only be parsing JSON
app.use(bodyParser.json());

var router = express.Router();

router.get('/', function(req, res){
    res.json({message: 'success! api is functioning'});
});

app.use('/api', router);


//start the server
var port = process.env.PORT || 8080;
app.listen(port);
console.log('botserver now running on port ' + port);
