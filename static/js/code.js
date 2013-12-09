/**
 * Created by zou on 13-11-30.
 */

/** 生成验证码 **/
var code

function createCode(){
    code = "";
    var codeLength = 4;
    var checkCode = document.getElementById("checkCode");
    checkCode.value = "";

    var selectChar = new Array(1,2,3,4,5,6,7,8,9,0,
        'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
        'Q','W','E','R','T','Y','U','I','O','p','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M');


    for(var i = 0;i<codeLength;i++){
        var charIndex = Math.floor(Math.random()*60);
        code += selectChar[charIndex];
    }

    if(code.length != codeLength){
        createCode();
    }
    checkCode.value = code;
  }


/** 验证 验证码 **/
function validate(){
    var inputCode = document.getElementById('inputcode').value.toUpperCase();
    var codeToUp = code.toUpperCase();
    if(inputCode.length <= 0){
        alert("请输入验证码！");
        return false;
    }
    else if(inputCode != codeToUp){
        alert("验证码错误！");
        createCode();
        return false;
    } else{
        return true;
    }
}

/**  **/



















