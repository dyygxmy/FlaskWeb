function append()
{
    var eld = document.getElementsByName("show")[0]
    var newText = document.form1.content.value
    var result = eld.value+"\n"+newText
    eld.value=result
    // alert(result)
}
// var x = document.getElementsByName("type").value;  //此时的x就是页面中所有name="type"所形成的一个数组
//  var x = document.getElementsByName("type")[0].value;     //此时的x就是页面中第一个name=''type"的值
// var x = document.getElementsByTagName("p")[2].value;       //此时的x是页面中第三个段落标签的值
//  var x = document.getElementsByTagName("p").value;       //此时的x是一个数组，是有页面中所有<p></p>所组成的一个数组
