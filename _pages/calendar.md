---
permalink: /calendar/
title: Event Calendar
---

<script src="https://cdn.jsdelivr.net/npm/ical.js@1.5.0/build/ical.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.4/index.global.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@fullcalendar/icalendar@6.1.4/index.global.min.js"></script>

<script>
    document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
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
