---
permalink: /calendars/
title: Event Calendars
---

<!--
<script src="https://code.jquery.com/jquery-3.6.3.slim.min.js"></script>
-->

<script src="https://cdn.jsdelivr.net/npm/ical.js@1.5.0/build/ical.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.4/index.global.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@fullcalendar/icalendar@6.1.4/index.global.min.js"></script>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fullcalendar@5.11.4/main.min.css">


<script>
    document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        initialView: 'dayGridMonth',
        events: {
            url: 'https://www.gov.uk/bank-holidays/england-and-wales.ics',
            format: 'ics' // important!
        }
      });
    calendar.render();
    });

</script>

<div id="calendar"></div>
