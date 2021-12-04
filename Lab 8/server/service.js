var http = require('http');
var fs = require('fs');
var students;
var count;
fs.readFile("./data.json", "utf8", (err, jsonString) => {
    if (err) {
      console.log("File read failed:", err);
      return;
    }
    try {
        students = JSON.parse(jsonString);
        count = Object.keys(students)[0].length;
      } catch (err) {
        console.log("Error parsing JSON string:", err);
      }
  });
  exports.GetHighestMarks = ()=>
  {
    var max=0;
    var name;
    for(i in students)
    {
        var sum=0;
        for(var j =0;j<count;j++)
        {
            sum+=students[i][j];
        }
        if(max<sum)
        {
            max=sum;
            name=i;
        }
    }
      return name;
  }
exports.getindex=()=>
{
    return count;
}
exports.GetSubjectiToppers = (index) => {

    let array = [];
    for(let key in students) {
        let o = [
            key,
            students[key][index]
        ];
        array.push(o);
    }
    array = array.sort((a,b) => a[1] - b[1]);
    return array;
}