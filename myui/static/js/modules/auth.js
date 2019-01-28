var moduleAuth = (function () {
    function login(url, formdata) {
        if (validatelogin(formdata)) {
            $("#login_error").empty()
            $.ajax({
                url: url,
                method: "POST",
                data: formdata,
                success: function (data) {
                    localStorage.setItem("auth_token", data['token'])
                },
                statusCode: {
                    200: function (response) {
                        alert(response)
                    },
                    400: function (response) {
                        $("#login_error").empty().append("<i>Username or password not correct</i>")

                    },
                    401: function (response) {
                        alert("401")
                    },
                }
            })
        }
    }

    function register(url, formdata) {
        if (validateregister(formdata)) {
            $.ajax({
                url: url,
                method: "POST",
                data: formdata,
                success: function (data) {
                    login("/api/login", formdata)
                },
                statusCode: {
                    200: function (response) {

                    },
                    400: function (response) {
                        key = Object.keys(response.responseJSON)[0]
                        messages = Object.values(response.responseJSON)[0]
                        $("#" + key + "_error").empty().append("<i>" + messages + "</i>")
                    },
                    401: function (response) {
                        alert("401")
                    },
                }
            })
        }
    }

    function validate(data, key, messages) {
        if (data == "") {
            $(key + "_error").empty().append(messages)
            $(key).focus()
        } else {
            $(key + "_error").empty()
        }
    }

    function validatelogin(data) {
        if (data[1].value == "" || data[2].value == "") {
            validate(data[2].value, "#password", "<i>Password is empty!</i>")
            validate(data[1].value, "#username", "<i>Username is empty!</i>")
            return false
        }
        $("#username_error").empty()
        $("#password_error").empty()
        return true
    }

    function validateregister(data) {
        if (data[1].value == "" || data[2].value == "" || data[3].value == "" || data[4].value == "") {
            validate(data[4].value, "#repassword", "<i>Repeat password is empty!</i>")
            validate(data[3].value, "#password", "<i>Password is empty!</i>")
            validate(data[2].value, "#email", "<i>Email is empty!</i>")
            validate(data[1].value, "#username", "<i>Username is empty!</i>")
            return false
        }
        $("#username_error").empty()
        $("#email_error").empty()
        $("#password_error").empty()
        $("#repassword_error").empty()
        return true
    }

    return {
        login: login,
        register: register,
        validate: validate,
        validatelogin: validatelogin,
        validateregister: validateregister,
    };
}());
