# Case 1: Class schedule
Topics:
- structure of html files
- web scrapting with python
- parametrization of projects (config files)
- other standards (for example: iCal files)

## Presentation
Class schedules on the Bocconi website do not offer the option to download them in a standard format, 
namely iCalendar. (accent on "Ca")
This is a pity, since many people are using calendar tools (iCal, Google Calendar, etc.) to 
manage their schedule and the availability of an iCalendar file to import would be useful.

We start from understanding how the iCalendar format works and what are the pieces of information needed to build an iCalendar file. Then, we will verify that those pieces are indeed displayed on the web page and we will learn how to do some **web scraping** on that page. Web scraping is the process of extracting data from web pages, data that are not available directly in usable form (that is, csv, etc.). Finally, we will parametrize our script so that it works with all Bocconi courses.

To do so, we need to:
- understand object oriented programming
- understand the iCalendar format
- understand a web page is organized *internally*
- use the python packages to scrape the page and do the remaining tasks

## The iCalendar format
- The website: https://icalendar.org/
- Look at specifications, validator, etc.
- An example from Google Calendar (iozzi30590@gmail.com): create event, download ics file and analyze it
- The format is with "containers": vcalendar, vevent, and more. Every container contains lines and other containers. Every line is in the form PROPERTY;PARAMETERS(OPTIONAL):VALUE
- do we get all that we need from the Bocconi page? (yes)

## Define an objects data structure for the iCalendar
- How to define a data structure for the calendar?
- Suggesting a data structure (how would you implement this?)
- show ics.py (help(ics))

## The structure of an HTML page
- A sample page (sample.html)

