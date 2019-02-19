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
  function getDetail(url) {
    $.ajax({
      url: url,
      method: "GET",
      success: function (data) {
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
          <input class="form-check-input" type="checkbox" id="alldaycheck" name="is_all_day" >
          <label class="form-check-label check-form" for="alldaycheck">
            All day
          </label>
          <span id="is_all_day_error" style="color:red"></span>
        </div>
      </div>
      <div class="form-group">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="dailycheck" name="is_daily" >
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
      <div class="form-group" id= "image">
        <label> Image Event</label >
        <input type="file"  name="file_attack">
      </div>
          <div class="form-group">
            <label for="itemPre">Item Preparing</label>
            <textarea type="text" class="form-control" id="itemPre" name="item_preparing">`+ data.item_preparing + `</textarea>
            <span id="item_preparing_error" style="color:red"></span>
          </div>
          <div class="form-group">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" id="publicCheck" name="is_public">
                <label class="form-check-label check-form" for="publicCheck">Public</label>
                <span id="is_public_error" style="color:red"></span>
        </div>
            </div>
            <button type="submit" class="btn btn-primary">Update</button>`)
        $('#alldaycheck').click(function (event) {
          if ($('#alldaycheck').is(':checked')) {
            $('#startTime').attr("disabled", true)
            $('#endTime').attr("disabled", true)
          } else {
            $("#startTime").removeAttr("disabled")
            $("#endTime").removeAttr("disabled")
          }
        })
        d = new Date()
        date = d.getDate()
        month = d.getMonth() + 1
        year = d.getFullYear()
        month = month < 10 ? '0' + month : month
        date = date < 10 ? '0' + date : date
        mindate = year + "-" + month + "-" + date
        document.getElementById("startDate").setAttribute("min", mindate)
        document.getElementById("endDate").setAttribute("min", mindate)
        $("#startDate").change(function (e) {
            document.getElementById("endDate").setAttribute("min", $("#startDate").val())
        })
        $("#endDate").change(function (e) {
            document.getElementById("startDate").setAttribute("max", $("#endDate").val())
        })
      },

    });
  }

  function updateEvent(url, formdata) {
    $.ajax({
      url: url,
      method: "PUT",
      headers: {
        "Authorization": authToken
      },
      data: formdata,
      processData: false,
      contentType: false,
      success: function (data) {
        arr = url.split("/")
        id = arr[arr.length - 2]
        alert("Success")
        location.href = "/events/" + id

      },
      statusCode: {
        200: function (response) {
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
        event_content = data.event_content
        if (event_content == null) {
          event_content = "Do not have description for this event"
        }
        item_preparing = data.item_preparing
        if (item_preparing == null) {
          item_preparing = "Do not have item preparing for this event"
        }
        $("#content-detail-event").append(`<div class="row">
        <div class="col-md-5 p-b-30">
          <div class="hov-img-zoom" id="image-event">
          <img src="` + data.file_attack + `" alt="IMG-ABOUT">
          </div>
        </div>
  
        <div class="col-md-7 p-b-30">
          <div class="p-t-30 respon5">
            <h4 class="product-detail-name m-text17 p-b-13" id="title-event">` + data.title + `</h4>
  
            <p class="m-text10">Start time:
              <span>` + startTime + `</span>
            </p>
            <p class="m-text10 p-b-15">End time:
              <sp>` + endTime + `</span>
            </p>
            <div class="p-b-30">
              <p class="m-text10">Location:
                <span class="m-text10 m-r-35">` + data.location + `</span>
              </p>
            </div>
  
            <div class="wrap-dropdown-content bo6 p-t-15 p-b-14 active-dropdown-content">
              <h5 class="js-toggle-dropdown-content flex-sb-m cs-pointer m-text19 color0-hov trans-0-4">
                Description
                <i class="down-mark fs-12 color1 fa fa-minus dis-none" aria-hidden="true"></i>
                <i class="up-mark fs-12 color1 fa fa-plus" aria-hidden="true"></i>
              </h5>
  
              <div class="dropdown-content dis-none p-t-15 p-b-23">
                <p class="m-text10">` + event_content + `</p>
              </div>
            </div>
  
            <div class="wrap-dropdown-content bo7 p-t-15 p-b-14">
              <h5 class="js-toggle-dropdown-content flex-sb-m cs-pointer m-text19 color0-hov trans-0-4">
                Item preparing
                <i class="down-mark fs-12 color1 fa fa-minus dis-none" aria-hidden="true"></i>
                <i class="up-mark fs-12 color1 fa fa-plus" aria-hidden="true"></i>
              </h5>
  
              <div class="dropdown-content dis-none p-t-15 p-b-23">
                <p class="m-text10">` + item_preparing + `</p>
              </div>
            </div>
          </div>
          <div class="event_buttons" id="btn-detail-event"></div>
        </div>
      </div>`)
        if (localStorage.getItem("auth_token") && localStorage.getItem("id") == data.owner) {
          $('#btn-detail-event').append(
            `<div class="button event_button event_button_1" id="btn-edit-event"><a href="/events/update/` + data.id + `">Edit</a></div>
              <div class="button event_button event_button_1" id="btn-delete-event"><a href="#">Delete</a></div>`
          )
        } else {
          $('#btn-detail-event').append(
            `<div class="button event_button event_button_1" id="btn-edit-event"><a href="#">Join</a></div>`)
        }
        // dropdown description and item preparing
        $('.active-dropdown-content .js-toggle-dropdown-content').toggleClass('show-dropdown-content');
        $('.active-dropdown-content .dropdown-content').slideToggle('fast');

        $('.js-toggle-dropdown-content').on('click', function () {
          $(this).toggleClass('show-dropdown-content');
          $(this).parent().find('.dropdown-content').slideToggle('fast');
        });
      },
      statusCode: {
        404: function (response) {
          $("#image-notfound").removeAttr("hidden")
        },
      }
    });
  }

  return {
    listEvent: listEvent,
    events: events,
    create: create,
    getDetail: getDetail,
    detailEvent: detailEvent,
    updateEvent: updateEvent,
  };
}());

