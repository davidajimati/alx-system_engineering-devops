# WEBSITE DOWNTIME - POSTMORTEM REPORT

### ISSUE SUMMARY
- `Duration`: This issue lasted for 2 hours and 5 minutes
- `Impact`: The company website was inaccessible and 43.4% of users who tried to use our services were unable to access product information.
- `Root cause`: Nginx was unable to listen to HTTP requests on port 80.

### TIMELINE
- The issue was detected at 13:52:04 - 25th May 2023 ( to 15:09:55 - 25th May 2023)
- This was detected when a customer complained about their inability to access their dashboard and track the progress of their orders.
- Actions taken: The Nginx’s default ‘site-enabled’ file was inspected and was found to contain errors that couldn’t allow Nginx to listen on port 80.
- Misleading investigation/debugging paths that were taken: The sys admin team started by inspecting the Nginx configuration file, after this, they checked for the server for possible services that might have hijacked port 80 from the Nginx web server.
- The issue was escalated to David M. ajimati, the Head of the engineering team.
- The Incident was resolved by deleting the default “sites-enabled” file, then creating a symbolic link between the ‘sites-available’ and ‘sites-enabled’ files.


### ROOT CAUSE AND RESOLUTION
#### ERROR DETAILS:
- The sites-enabled configuration file contained links to pages on our website that are no longer accessible (since they were updated to another).
- The sites-available configuration file contained the updated pages that contained the up-to-date information on our products. And since the sites-enabled were pointing to the wrong(inexisting) pages, users accessing the product info website got error 500.
#### FIXING DETAILS:
- The error was fixed by creating a symbolic link from the default configuration file in the sites-available directory to the sites-enabled directory for NGINX. By doing so, the default configuration becomes enabled and active for NGINX to use.
- This will allow us to enable or disable specific site configurations by simply creating or removing symbolic links and ensuring such issues do not re-occur.


### CORRECTIVE AND PREVENTATIVE MEASURES
- What may be improved includes: how we update the available pages on our website and ensure the NGINX web server takes these changes into effect immediately to minimize downtimes or related issues.
- Task list to address this issue:
- install web-server monitoring application
- Compare the sites-enabled and sites-available configuration files
- Check if there is a symbolic link between both
- Delete the sites-enabled file
- Create symbolic links from sites-enabled to sites-available file
- Check if other services are not using/blocking port 80.
- Restart nginx

code to fix this issue:
```
#!/usr/bin/env bash
# This script reconfigures nginx to listens to port 80a
rm /etc/nginx/sites-enabled/default
ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
```

### AUTHOR
David M. Ajimati
