This is node.js application
To run this application
cd ../server
node server.js

Now Server will start listining on port 8080
if you open browser and open http://localhost:8080/ you will be able to access web page 

if query passed is 1
http://localhost:8080/?query=1)
it will display student name with highest marks

if query passed is 2 and some valid index
http://localhost:8080/?query=2&index=1
it will display of marks of each student of particular index in increasing order
if index is out of bound then it will show indvalid query

if query is not 1 & 2
then it will show invalid query

Inside service.js page
this script is reading data from data.json file inside server folder
and parsing and passing required result from GetHighestMarks and GetSubjectiToppers
GetSubjectiToppers return marks of each student of particular index
GetHighestMarks return name of student of highest marks

inside server.js file
taking data from service.js page and displaying result on webpage with port 8080