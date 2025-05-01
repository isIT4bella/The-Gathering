# The-Gathering
🍎tEAM persistance Lab

This Lab is designed (for lab testing purposes only!!) to replicates a persistent harvesting tool

    Persistence Mechanism:

        Installs itself in the Startup folder (%AppData%\Microsoft\Windows\Start Menu\Programs\Startup)

        Adds a Registry Run key (HKCU\Software\Microsoft\Windows\CurrentVersion\Run)

        This means it will automatically run every time the user logs in

    Information Gathering:

        Harvests Outlook email database files (.pst/.ost)

        Collects running processes (could reveal sensitive applications)

        Shows network connections (could reveal private services)

    Expansion Potential:

        The script could easily be modified to:

            Send harvested data to a remote server

            Install additional malware

            Capture screenshots or keystrokes

            To learn Defensive you must learn offensive. All information is for training purposes and to streangthen our forensics as the defenders of the innocent.
            Team BLUE
