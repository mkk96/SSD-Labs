function myFunction(input)
{
	var elementValue = input.value;
	document.getElementById("ptagchange").innerHTML = elementValue;
}
function function1(input)
{
    var d = new Date();
    var node = document.createElement("Li");
    var text = document.getElementById("ptagchange1").value+": "+d; 
    var textnode=document.createTextNode(text);
    node.addEventListener("mouseover",function2);
    node.addEventListener("mouseout",function3);
    node.appendChild(textnode);
    document.getElementById("list").appendChild(node);
}
function removeItem() {
    var list=document.getElementById("list");
    var listItems = list.getElementsByTagName("Li");
    var last=listItems[listItems.length-1];
    list.removeChild(last);
}
function2 = ($event) =>
{
    let li=$event.target;
    li.style.color="red";
    li.style.fontSize="20px";
}
function3 = ($event) =>
{
    let li=$event.target;
    li.style.color="#000";
    li.style.fontSize="16px";
}
function function4()
{
    let list=document.getElementById("list");
    list.style.fontFamily=list.style.fontFamily=="Arial"?"auto":"Arial";
}