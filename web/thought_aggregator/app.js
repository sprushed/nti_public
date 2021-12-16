const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require('body-parser')

const app = express();
app.use(bodyParser.json())

const Schema = mongoose.Schema;
const userScheme = new Schema({name: String, age: Number}, {versionKey: false});
const User = mongoose.model("messages", userScheme);

mongoose.connect(`mongodb://mongodb:27017/reach-humanity`, { useNewUrlParser: true }, function(err){
    if(err) return console.log(err);
    app.listen(3000, function(){
        console.log("api listener started");
    });
});

app.post("/api", function (req, res) {

    if(!req.body) return res.sendStatus(500);
    User.aggregate([req.body], function(err, doc){
        if(err) return console.log(err);
        res.send(doc)
    });
});

app.use('/', express.static('./static'));
