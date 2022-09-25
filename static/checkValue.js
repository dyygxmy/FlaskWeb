function getValue()
{
    var text=document.form2.text1.value
    var check=document.form2.Option.value //单选框选中了才会输出其值
    var arr=document.form2.check //多选框是以数组方式传过来的
    alert(text)
    alert(check)
    alert(arr[0].value)
}