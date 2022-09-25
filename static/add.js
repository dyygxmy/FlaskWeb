function add()
{
    var adder1=Number(document.form1.adder1.value); //定义变量
    var adder2=Number(document.form1.adder2.value);
    var result=adder1+adder2;
    document.form1.result.value = result; // 让index.html的form1表单中的result元素的值为变量result的值
    // alert(adder1) //弹窗界面输出
}