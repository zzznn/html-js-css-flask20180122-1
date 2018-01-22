$(document).ready(function(){
//           <!--登陆的按钮-->
              $("#btn1").click(function(){
                var username=$("#username").val();
                var password=$("#password").val();
                if(username == ""){
                       alert("账号不能为空，请重新输入！");
                }
                else if (password == ""){
                       alert("密码不能为空，请重新输入！");
                }
                else{
                      $.post("/login01", {"username": username, 'password': password},function(data, status){
                        if (data.get == "OK"){
                             $("#myformLogin").submit();
//                         <!--验证成功，实现跳转到个人界面-->
                        }
                        else{
                             alert("用户名: " + data.username + "\n密码: " + data.password + "\n账号密码不匹配，请重新输入！");
                           }
                    });
                }
            });

//          注册按钮
             $("#btn2").click(function(){
             var a = $("#usernamesignup").val();
             var b = $("#passwordsignup").val();
             var c = $("#passwordsignup_confirm").val();
             var d = $("#emailsignup").val();
                if (a == "")
                {
                    alert("注册用户名不能为空！！！");
                }
                else if (d == ""){
                    alert("邮箱不能为空！！！");
                }
                else if ( b == ""){
                    alert("密码不能为空！！！");
                }
                else if (b != c){
                    alert("两次输入密码不一致！！！");
                }
                else{
                    $.post("/signup01", {"usernamesignup": a},function(data, status){
                        if (data.g == "OK"){
                            alert("用户名已存在，请重新输入！！！");
                        }
                        else{
                            alert("注册成功，请登陆 ！！！");
                            $("#myformSignUp").submit();
                        }
                    });
                }
            });



 });//结尾


//实现 按下enter 回车键 登录和注册
$(document).keyup(function(event){
if(event.keyCode ==13){
 $("#btn1").trigger("click");
      }
    });

$(document).keyup(function(event){
if(event.keyCode ==13){
 $("#btn2").trigger("click");
      }
    });


