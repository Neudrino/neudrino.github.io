---
permalink: /calendars/
title: Event Calendars
---

<!--
<script src="https://code.jquery.com/jquery-3.6.3.slim.min.js"></script>
-->

<script src="https://cdn.jsdelivr.net/npm/ical.js@1.5.0/build/ical.min.js" integrity="sha256-uotVKltUv5neKsIlZxrxUccba0PaptusFj6p+w8Sons=" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/fullcalendar@5/main.min.js" integrity="sha256-Dfd6KUTo4z5AmFLv2yo91WxDAJyDtbZH3PPbf7o/kN4=" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fullcalendar@5/main.min.css" integrity="sha256-EAq+X/hXd44MlSOCkm9hchPJT78vQ4UBTT7FBkQl9qE=" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/@fullcalendar/icalendar@5/main.global.min.js" integrity="sha256-ZUc36g9C2lYR9GmRtOmCBHFDFS1sOJsTAnCFX8ZYbZk=" crossorigin="anonymous"></script>

<script>
    document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        initialView: 'dayGridMonth',
        events: {
            url: 'boogie-baeren.ics',
            format: 'ics' // important!
        }
      });
    calendar.render();
    });

</script>

<div id="calendar"></div>
