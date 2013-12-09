/**
 * Created by zou on 13-11-30.
 */

var optionMsg = {
    form_email:'用来找回密码',
    form_password:'只包含字母和数字，8-15个字符，区分大小写'
}

var validateError={
    id:{
        isNull:'学号不能为空'
    },
    email: {
        isNull:'Email不能为空',
        invalidFormat:'Email格式不正确'
    },
    password:{
        isNull:'密码不能为空',
        isShort: '密码长度不足8个字符',
        invalidFormat: '请使用英文字母或数字'
    }


}

function validate_register(validateRules,validateError,optionMsg){

}