# ICS-Import-to-Google
A set of scripts that enable automatically importing ics files from Thunderbird into Google Calendar.

**This documentation is a work in progress.**

Resources:

  - [cx_Freeze](https://marcelotduarte.github.io/cx_Freeze/) to compi;e the Python script into a Windows exe
 - [gcalcli](https://github.com/insanum/gcalcli) to communicate with the Google Calendar API via the Windows command-line
 - [Google Calendar API Python Quickstart](https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the) to quickly generate API credentials to use with gcalcli
 
To configure the default pair of API credentials for gcalcli:

    gcalcli --client_id [ClientID] --client_secret [ClientSecret]

To freeze the gcalcli-import script:

    cxfreeze gcacli-import.py
