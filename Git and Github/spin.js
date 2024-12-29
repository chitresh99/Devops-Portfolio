const express = require('express');
const app = express();
PORT = 3000;
app.get('/',function(req,res){
    res.send("Hello git and github");
})

app.listen(PORT,function(err){
    if(err){
        console.log("error in setup");
    }
    console.log(`server is running on ${PORT}`)
})