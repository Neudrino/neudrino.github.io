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
<!-- For tooltips -->
<script src="https://unpkg.com/popper.js/dist/umd/popper.min.js" crossorigin="anonymous"></script>
<script src="https://unpkg.com/tooltip.js/dist/umd/tooltip.min.js" crossorigin="anonymous"></script>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {
            schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
            initialView: 'dayGridMonth',
            headerToolbar: {
                left: 'prev,next',
                center: 'title',
                right: 'today,dayGridMonth,dayGridYear,listYear'
            },
            events: {
                url: 'www.boogie-baeren.de.ics',
                format: 'ics'
            },
            eventDidMount: function(info) {
                var tooltip = new Tooltip(info.el, {
                    title: info.event.title,
                    placement: 'top',
                    trigger: 'hover',
                    container: 'body'
                });
            },
        });
        calendar.render();
    });
</script>

# BB Kalender Titel

[Boogie-Bären Kalender iCalendar](../calendars/www.boogie-baeren.de.ics)

<div id="calendar"></div>

<style>
.popper,
.tooltip {
  position: absolute;
  z-index: 9999;
  background: #FFC107;
  color: black;
  width: 150px;
  border-radius: 3px;
  box-shadow: 0 0 2px rgba(0,0,0,0.5);
  padding: 10px;
  text-align: center;
}
.style5 .tooltip {
  background: #1E252B;
  color: #FFFFFF;
  max-width: 200px;
  width: auto;
  font-size: .8rem;
  padding: .5em 1em;
}
.popper .popper__arrow,
.tooltip .tooltip-arrow {
  width: 0;
  height: 0;
  border-style: solid;
  position: absolute;
  margin: 5px;
}

.tooltip .tooltip-arrow,
.popper .popper__arrow {
  border-color: #FFC107;
}
.style5 .tooltip .tooltip-arrow {
  border-color: #1E252B;
}
.popper[x-placement^="top"],
.tooltip[x-placement^="top"] {
  margin-bottom: 5px;
}
.popper[x-placement^="top"] .popper__arrow,
.tooltip[x-placement^="top"] .tooltip-arrow {
  border-width: 5px 5px 0 5px;
  border-left-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
  bottom: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}
.popper[x-placement^="bottom"],
.tooltip[x-placement^="bottom"] {
  margin-top: 5px;
}
.tooltip[x-placement^="bottom"] .tooltip-arrow,
.popper[x-placement^="bottom"] .popper__arrow {
  border-width: 0 5px 5px 5px;
  border-left-color: transparent;
  border-right-color: transparent;
  border-top-color: transparent;
  top: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}
.tooltip[x-placement^="right"],
.popper[x-placement^="right"] {
  margin-left: 5px;
}
.popper[x-placement^="right"] .popper__arrow,
.tooltip[x-placement^="right"] .tooltip-arrow {
  border-width: 5px 5px 5px 0;
  border-left-color: transparent;
  border-top-color: transparent;
  border-bottom-color: transparent;
  left: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}
.popper[x-placement^="left"],
.tooltip[x-placement^="left"] {
  margin-right: 5px;
}
.popper[x-placement^="left"] .popper__arrow,
.tooltip[x-placement^="left"] .tooltip-arrow {
  border-width: 5px 0 5px 5px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
  right: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}
</style>
