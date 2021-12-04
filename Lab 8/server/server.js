var http = require('http');
var service = require('./service.js');
var url=require('url')
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'application/json'});
    let params = url.parse(req.url, true).query;
    let query = params.query;
    let index=params.index;
    let count = service.getindex();
    if(query==1)
    {
        let response = service.GetHighestMarks();
        res.write(JSON.stringify(response));
    }
    else if(query==2 &&(index>=0&&index<=count-1))
    {
        let response = service.GetSubjectiToppers(index);
        res.write(JSON.stringify(response));
    }
    else
    {
        res.write("Invalid query");
    }
    return res.end();
  }).listen(8080, () => {
    console.log("Server is now lisning on port "+ 8080);
  });