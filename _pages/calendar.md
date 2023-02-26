---
permalink: /calendar/
title: Event Calendar
---

<script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.4/index.global.min.js" integrity="sha256-z82jYOK/utiAteR0z6FjIOQmdWzvxqXJ6wsXbGJkBwY=" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@fullcalendar/icalendar@6.1.4/index.global.min.js" integrity="sha256-FyMK7xygCQe5tPAN+WAPVYPyFzvrgapsqiC/zUNyco4=" crossorigin="anonymous"></script>

    document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: [
            iCalendarPlugin,
            dayGridPlugin
        ],
        initialView: 'dayGridMonth',
        events: {
            url: 'calendars/boogie-baeren.ics',
            format: 'ics' // important!
        }
      });
    calendar.render();
    });

</script>

<div id="calendar"></div>
