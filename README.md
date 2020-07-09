

# ICS-Import-to-Google
A set of tools to directly import iCalendar (.ics) files from Thunderbird into Google Calendar 

## Prerequisites

 - Python 3: https://www.python.org/downloads/
 - [gcalcli](https://github.com/insanum/gcalcli) to communicate with the Google Calendar API via the Windows command-line.
  - [cx_Freeze](https://marcelotduarte.github.io/cx_Freeze/) to compile the Python script into a Windows exe.

## Installation

 1. Use the [Google Calendar API Python Quickstart](https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the) to generate a pair of API credentials to use with gcalcli.
 2. To configure the default pair of API credentials for gcalcli, run the following command:
    ```
    gcalcli --client_id [ClientID] --client_secret [ClientSecret]
    ```
 3. Use gcalcli to determine the name of the calendar you would like to import events to. You can list the calendars on your Google account with the following command:
    ```
    gcalcli list
    ```
 4. Make the following changes to your local copy of the [gcalcli-import.py](./gcalcli-import.py) script:
	 - The `GCALCLI_PATH` constant should point to the path where the gcalcli executable was installed.
	 - The `CALENDAR_NAME` constant should indicate the calendar name you determined from the previous step.
 5. Freeze the gcalcli-import script into an exe file:
    ```
    cxfreeze gcalcli-import.py
    ```
 6. The executable will be created in the `dist` subfolder inside the directory that contains the gcalcli-import.py script.
 7. Open an email in Thunderbird that contains an iCalendar invitation. Click the invite.ics file to open it.
 8. In the open file dialog, click the dropdown box next to "Open with" and select "Other..."
 9. Click "Browse...". Double click the executable that was generated by cxfreeze in the previous step.
 10. Check the box for "Do this automatically for files like this from now on." and click OK.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
