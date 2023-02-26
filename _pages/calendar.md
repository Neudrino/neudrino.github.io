---
permalink: /calendar/
title: Event Calendar
---


<script src="https://cdn.jsdelivr.net/npm/fullcalendar-scheduler@6.1.4/index.global.min.js" integrity="sha256-ZraR3q2Tudjvaiz6AUCr8pWkjOb+DGzPfa+fyVIRSE4=" crossorigin="anonymous"></script>
<script src='https://cdn.jsdelivr.net/npm/fullcalendar-scheduler@6.1.4/index.global.min.js'></script>
<script>

    document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'resourceTimelineWeek',
    });
    calendar.render();
    });

</script>

<div id="calendar"></div>
