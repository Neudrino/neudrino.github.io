---
permalink: /calendars/
title: Event Calendars
---

<!--
<script src="https://code.jquery.com/jquery-3.6.3.slim.min.js"></script>
-->

<script src="https://cdn.jsdelivr.net/npm/ical.js@1.5.0/build/ical.min.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.4/index.global.min.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@fullcalendar/icalendar@6.1.4/index.global.min.js" crossorigin="anonymous"></script>

<script>
    document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        initialView: 'dayGridMonth',
        events: {
            url: 'www.boogie-baeren.de.ics',
            format: 'ics'
        }
      });
    calendar.render();
    });

</script>

# BB Kalender Titel

[Boogie-Bären Kalender iCalendar](../calendars/boogie-baeren.ics)

<div id="calendar"></div>
