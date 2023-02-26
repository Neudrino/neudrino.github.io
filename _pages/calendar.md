---
permalink: /calendar/
title: Event Calendar
---

<script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.4/index.global.min.js" integrity="sha256-z82jYOK/utiAteR0z6FjIOQmdWzvxqXJ6wsXbGJkBwY=" crossorigin="anonymous"></script>

    document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'resourceTimelineWeek',
    });
    calendar.render();
    });

</script>

<div id="calendar"></div>
