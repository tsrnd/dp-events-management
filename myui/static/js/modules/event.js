var moduleEvent = (function () {
  var authToken = "token " + localStorage.getItem("auth_token")
  const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  page = 1

  function events(data) {
    for (i in data) {
      start_date = new Date(data[i].start_date)
      $('#list_event').append(`<div class="event">
            <div class="row row-lg-eq-height">
              <div class="col-lg-6 event_col">
                <div class="event_image_container">
                  <div class="background_image" style="background-image:url(` + data[i].file_attack + `)"></div>
                  <div class="date_container">
                    <a href="#">
                      <span class="date_content d-flex flex-column align-items-center justify-content-center">
                        <div class="date_day">` + start_date.getDate() + `</div>
                        <div class="date_month">` + monthNames[start_date.getMonth()] + `</div>
                      </span>
                    </a>
                  </div>
                </div>
              </div>
              <div class="col-lg-6 event_col">
                <div class="event_content" id="event_content">
                  <div class="event_title"><a href="/events/` + data[i].id + `">` + data[i].title + `</a></div>
                  <div class="event_location">` + data[i].location + `</div>
                  <div class="event_text">
                    <p>` + data[i].event_content + `</p>
                  </div>
                  <div class="event_speakers">
                    <!-- Event Speaker -->
                    <div class="event_speaker d-flex flex-row align-items-center justify-content-start">
                      <div>
                        <div class="event_speaker_image"><img src="/static/images/event_speaker_1.jpg" alt=""></div>
                      </div>
                      <div class="event_speaker_content">
                        <div class="event_speaker_name">Michael Smith</div>
                        <div class="event_speaker_title">Marketing Specialist</div>
                      </div>
                    </div>
                    <!-- Event Speaker -->
                    <div class="event_speaker d-flex flex-row align-items-center justify-content-start">
                      <div>
                        <div class="event_speaker_image"><img src="/static/images/event_speaker_2.jpg" alt=""></div>
                      </div>
                      <div class="event_speaker_content">
                        <div class="event_speaker_name">Jessica Williams</div>
                        <div class="event_speaker_title">Marketing Specialist</div>
                      </div>
                    </div>
                  </div>
                  <div class="event_buttons">
                    <div class="button event_button event_button_1"><a href="#">Join</a></div>
                    <div class="button_2 event_button event_button_2"><a href="/events/` + data[i].id + `">Read more</a></div>
                  </div>
                </div>
              </div>
            </div>
          </div>`)
    }
  }

  function listEvent(url) {
    $.ajax({
      url: url,
      method: "GET",
      data: {
        "page": page,
      },
      success: function (data) {
        events(data.result)
      },
      statusCode: {
        200: function (response) {
          page = response.page + 1
          if (!response.next_page_flg) {
            $("#loadMore").hide()
          }
        },
        401: function (response) {
          alert("401");
        },
      }
    });
  }


  function create(url, formdata) {
    $("#event_error").empty()
    $("#title_error").empty()
    $("#start_date_error").empty()
    $("#start_time_error").empty()
    $("#end_date_error").empty()
    $("#end_time_error").empty()
    $("#is_all_day_error").empty()
    $("#is_daily_error").empty()
    $("#location_error").empty()
    $("#event_content_error").empty()
    $("#file_attack_error").empty()
    $("#item_preparing_error").empty()
    $("#is_public_error").empty()
    $.ajax({
      url: url,
      method: "POST",
      headers: {
        "Authorization": authToken
      },
      data: formdata,
      processData: false,
      contentType: false,
      success: function (data) {
        // appenddata(data.result)
      },
      statusCode: {
        201: function (response) {
          location.replace("/")
        },
        400: function (response) {
          console.log(response)
          for (i in Object.keys(response.responseJSON)) {
            key = Object.keys(response.responseJSON)[i]
            messages = response.responseJSON[key]
            $("#" + key + "_error").empty().append("<i>" + messages + "</i>")
          }
        },
        401: function (response) {
          alert("401")
        },
        500: function (response) {
          console.log(response)
        },
      }
    })
  }

  function detailEvent(url) {
    $.ajax({
      url: url,
      method: "GET",
      success: function (data) {
        console.log(data)
        if (data.start_time == null) {
          var startDate = new Date(data.start_date)
          var endDate = new Date(data.end_date)
          $("#start-time").append(startDate.getDate() + "/" + startDate.getMonth() + "/" + startDate.getFullYear())
          $("#end-time").append(endDate.getDate() + "/" + endDate.getMonth() + "/" + endDate.getFullYear())
        } else {
          var startDate = new Date(data.start_date + " " + data.start_time)
          var endDate = new Date(data.end_date + " " + data.end_time)
          $("#start-time").append(startDate.getDate() + "/" + startDate.getMonth() + "/" + startDate.getFullYear() + " @ " + startDate.getHours() + ":" + startDate.getMinutes())
          $("#end-time").append(endDate.getDate() + "/" + endDate.getMonth() + "/" + endDate.getFullYear() + " @ " + endDate.getHours() + ":" + endDate.getMinutes())
        }
        var startDate = new Date(data.start_date + " " + data.start_time)
        var endDate = new Date(data.end_date + " " + data.end_time)
        $("#image-event").append(`<img src="` + data.file_attack + `" alt="IMG-ABOUT">`)
        $("#title-event").append(data.title)

        $("#location").append(data.location)
        $("#content").append(data.event_content)
        $("#item-preparing").append(data.item_preparing)
      },
      statusCode: {
        200: function (response) {
          // alert("200");
        },
        401: function (response) {
          alert("401");
        },
      }
    });
  }

  return {
    listEvent: listEvent,
    events: events,
    create: create,
    detailEvent: detailEvent,
  };
}());
