var moduleAuth = (function () {
    var authToken = "token " + localStorage.getItem("auth_token")

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
                        location.replace("/")
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
        $("#username_error").empty()
        $("#email_error").empty()
        $("#password_error").empty()
        $("#password_confirm_error").empty()
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
                    for (i in Object.keys(response.responseJSON)) {
                        key = Object.keys(response.responseJSON)[i]
                        messages = response.responseJSON[key]
                        $("#" + key + "_error").empty().append("<i>" + messages + "</i>")
                    }
                },
                401: function (response) {
                    alert("401")
                },
            }
        })
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
            validate(data[2].value, "#password", "<i>Password is required!</i>")
            validate(data[1].value, "#username", "<i>Username is required!</i>")
            return false
        }
        $("#username_error").empty()
        $("#password_error").empty()
        return true
    }

    function logout(url) {
        $.ajax({
            url: url,
            method: "POST",
            headers: {
                "Authorization": authToken
            },
            success: function (data) {
                // localStorage.setItem("auth_token", data['token'])
            },
            statusCode: {
                204: function (response) {
                    localStorage.removeItem("auth_token")
                    location.replace("/")
                },
                401: function (response) {
                    alert("401")
                },
            }
        })
    }


    return {
        login: login,
        register: register,
        validate: validate,
        validatelogin: validatelogin,
        logout: logout,
    };
}());
