var moduleComment = (function() {
    var authToken = "token "+ localStorage.getItem("auth_token");
    function listComment(url) {
        $.ajax({
            url: url,
            method: "GET",
            headers: {"Authorization": authToken},
            success: function(data){
                console.log(data);
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
        listComment: listComment
    };
  }());