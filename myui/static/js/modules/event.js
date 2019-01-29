var moduleEvent = (function () {
  const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  page = 1

  function events(data) {
    for (i in data) {
      start_date = new Date(data[i].start_date)
      $('#list_event').append(`<div class="event">
            <div class="row row-lg-eq-height">
              <div class="col-lg-6 event_col">
                <div class="event_image_container">
                  <div class="background_image" style="background-image:url(/static/images/event_9.jpg)"></div>
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

  return {
    listEvent: listEvent,
    events: events,
  };
}());
