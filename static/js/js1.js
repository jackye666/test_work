var t = 0
var timer = null
var src = "0"
var obj
send_data()
function send_data() {
    var XHR = new XMLHttpRequest();
    var pay_load = {"a": "0","src":"0"};
    pay_load["a"] = JSON.stringify(t)
    pay_load["src"] = src
    XHR.open('POST', 'modify');
    XHR.setRequestHeader('content-type', 'application/json');  //先open再设置请求头
    XHR.send(JSON.stringify(pay_load));
    XHR.onreadystatechange = function(){
          if(XHR.readyState === 4 && XHR.status === 200){
            obj = JSON.parse(XHR.responseText)
            document.getElementById("myimage").src = src
            document.getElementById("p1").innerHTML = src
            document.getElementById("p3").innerHTML = obj.t
            src = obj.full_filename
            $(function () {
                var top = obj.top
                var left = obj.left
                var wid = obj.wid
                var hig = obj.hig
                $("span").width(wid).height(hig);
                $("span").css({'top':top+"px",'left':left+"px"});
            });
          }
    };
    t += 1
    timer = setTimeout("send_data()","1000")
    prev_src = src
}