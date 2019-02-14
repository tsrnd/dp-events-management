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
                  <div class="event_title"> ` + data[i].title + `</div>
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
                    <div class="button event_button event_button_1"><a href="#">Buy Tickets Now!</a></div>
                    <div class="button_2 event_button event_button_2"><a href="#">Read more</a></div>
                    <div class="edit-event button_2 event_button event_button_3" data-event="`+ data + `"><a href="/events/update/` + data[i].id + `">Edit</a></div>
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
  function getDetail(url) {
    $.ajax({
      url: url,
      method: "GET",
      success: function (data) {
        console.log(data)
        if (data.start_time == null) {
          var startDate = new Date(data.start_date)
          var endDate = new Date(data.end_date)
          startTime = startDate.getDate() + "/" + startDate.getMonth() + "/" + startDate.getFullYear()
          endTime = endDate.getDate() + "/" + endDate.getMonth() + "/" + endDate.getFullYear()
        } else {
          var startDate = new Date(data.start_date + " " + data.start_time)
          var endDate = new Date(data.end_date + " " + data.end_time)
          startTime = startDate.getDate() + "/" + startDate.getMonth() + "/" + startDate.getFullYear() + " @ " + startDate.getHours() + ":" + startDate.getMinutes()
          endTime = endDate.getDate() + "/" + endDate.getMonth() + "/" + endDate.getFullYear() + " @ " + endDate.getHours() + ":" + endDate.getMinutes()
        }
        $("#update-form").append(`<div class="form-group">
        <label for="inputTitle">Title Events</label>
        <input type="text" class="form-control" id="inputTitle" name="title" value="`+ data.title + `">
        <span id="title_error" style="color:red"></span>
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="startDate">Start Date</label>
          <input type="date" class="form-control option-style" id="startDate" name="start_date" value = "`+ data.start_date + `">
          <span id="start_date_error" style="color:red"></span>
        </div>
        <div class="form-group col-md-6">
          <label for="startTime">Start Time</label>
          <input type="time" class="form-control option-style" id="startTime" name="start_time" value = "`+ data.start_time + `">
          <span id="start_time_error" style="color:red"></span>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group col-md-6">
          <label for="endDate">End Date</label>
          <input type="date" class="form-control option-style" id="endDate" name="end_date" value = "`+ data.end_date + `">
          <span id="end_date_error" style="color:red"></span>
        </div>
        <div class="form-group col-md-6">
          <label for="endTime">End Time</label>
          <input type="time" class="form-control option-style" id="endTime" name="end_time" value = "`+ data.end_time + `">
          <span id="end_time_error" style="color:red"></span>
        </div>
      </div>
      <div class="form-group">
        <div class="form-check">
          <input class="form-check-input" {%ifequal {{data.is_all_day}} is false %}checked="checked"{{% endifequal %}  type="checkbox" id="alldaycheck" name="is_all_day" >
          <label class="form-check-label check-form" for="alldaycheck">
            All day
          </label>
          <span id="is_all_day_error" style="color:red"></span>
        </div>
      </div>
      <div class="form-group">
        <div class="form-check">
          <input class="form-check-input" {% ifequal `+ data.is_daily + ` 'true' %}checked{% endifequal %} type="checkbox" id="dailycheck" name="is_daily" >
          <label class="form-check-label check-form" for="dailycheck">
            Daily
          </label>
          <span id="is_daily_error" style="color:red"></span>
        </div>
      </div>
      <div class="form-group">
        <label for="location">Location</label>
        <input type="text" class="form-control" id="location" value="`+ data.location + `" name="location">
        <span id="location_error" style="color:red"></span>
      </div>
      <div class="form-group">
        <label for="eventContent">Event content</label>
        <textarea type="text" class="form-control" id="eventContent"  name="event_content">`+ data.event_content + `</textarea>
        <span id="event_content_error" style="color:red"></span>
      </div>
      <div class="form-group">
        <span id="close" data-id="" data-token="{{ csrf_token() }}" class="close">&times;</span>
        <label>Image Event</label>
        <img src="`+ data.file_attack + `" alt=""> <br><br>    
        <input type="file"  value="`+ data.file_attack + `">
      </div>
      <div class="form-group">
        <label for="itemPre">Item Preparing</label>
        <textarea type="text" class="form-control" id="itemPre" name="item_preparing">`+ data.item_preparing + `</textarea>
        <span id="item_preparing_error" style="color:red"></span>
      </div>
      <div class="form-group">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="publicCheck">
          <label class="form-check-label check-form" for="publicCheck" name="is_public">Public</label>
          <span id="is_public_error" style="color:red"></span>
        </div>
      </div>
      <button type="submit" class="btn btn-primary" name="update-event">Update</button>`)


      },

    });
  }




  return {
    listEvent: listEvent,
    events: events,
    create: create,
    getDetail: getDetail,
  };
}());
// $('#edit-event').submit(function (event) {
//   event.preventDefault();
//   var id = $(this).attr('id')
//   console.log(id)
  // form_data = new FormData($('#update-form')[0]);

  // $.ajax({
  //   type: 'POST',
  //   url: 'http://localhost:8000/api/events/' + id,
  //   headers: {
  //     "Authorization": authToken
  //   },
  //   processData: false,
  //   contentType: false,
  //   data: form_data,
  //   success: function (data) {
  //     alert("Success")
  //   },

  // })
// })
