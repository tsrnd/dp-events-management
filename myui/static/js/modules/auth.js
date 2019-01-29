var moduleAuth = (function () {
    var authToken = "token " + localStorage.getItem("auth_token")

    function login(url, formdata) {
        $.ajax({
            url: url,
            method: "POST",
            data: formdata,
            success: function (data) {
                localStorage.setItem("auth_token", data['token'])
            },
            statusCode: {
                200: function (response) {
                    alert(response);
                },
                401: function (response) {
                    alert("401");
                },
            }
        });
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
                200: function (response) {
                    localStorage.removeItem("auth_token")
                },
                401: function (response) {
                    alert("401")
                },
            }
        })
    }


    return {
        login: login,
        logout: logout,
    };
}());
