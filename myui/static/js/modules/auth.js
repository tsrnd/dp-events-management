var moduleAuth = (function() {
    function login(url, formdata) {
        $.ajax({
            url: url,
            method: "POST",
            data: formdata,
            success: function(data){
                localStorage.setItem("auth_token", JSON.stringify(data['token']));
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

    return {
        login: login
    };
  }());