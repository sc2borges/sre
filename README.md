# sre 

This Repo contains the assessment questions requested 

## Q1
**A service daemon in production has stopped responding to network requests. You receive an**
**alert about the health of the service. Where would you start with handling the alerting condition?**
**How would you gather more information about the process and its doing? What are common**
**reasons a process might appear to be locked up, and how would you rule out each possibility?**

First of all after received the alert, I need to check a few things.
 - The host running the application is accessible via remote connection (SSH)? 
    * If not accessible, the host is on, if not turns on and restart the service.
    * Verify if the host has network connectivity and is easy acessible via network connection.

 - Try to restart the service and check the status
   * The service continue not responding even after restart process.(Continue with Troubleshooting)
   * check `systemctl` or `journalctl` commands to understand the startup process.

 - Check logs to understand if the Service Daemon generated any output related to reported outage.
   * The Logs should show potential issues within the service, Binary execution errors , Exceptions and DoS

 - Confirm if the host service has enough resources to run the Service, check CPU, Memory, Disk
   * CPU is not running at 100% that could cause the service to halt with no capacity of process.
   * Memory is not leaking and not running at the top with no free memory to support the service request - OOM errors
   * Disk has enough space to write temporary files and/or store data.
   * Check if the node has network access and can communicate with the default router and nothing is blocked via firewall.

 - If this service depends on a external Application, check connectivity between those.
   * The service relies on Databases to respond requests, if so check the database.?
   * This service has any API communication that is mandatory to respond any request, check the 3rd party API and confirm if there's any external outage running with the Partner. 
   
 - If the service still not responding, check if is possible to redirect the traffic to another server/POD/Container and Isolate the host for further investigation.
 - **Proceed with Post Mortem process to document the failure after indentify the root cause and provide the document for easy resolution if that happens again**

---


## Q2
You have a Linux binary you need to run called blackbox. When you attempt to run it in a
terminal (e.g. ./blackbox), it prints a blank line and exits. What are the common reasons a
binary could behave this way? How would you troubleshoot it?

* Do I have the rights to run this binary, checking the permissions will answer that question: 
if not have right to execute just run , `chmod 755 blackbox` on the file to change the default permission (the user need to has enough right to execute the command)
```
ls -la blackbox 
-rw-------   1 user.user  staff       914 11 Oct 19:55 blackbox
```

* The command request arguments to execute and is waiting for extra parameters?
 - perhaps execute help command will show more options
```
blackbox --help 
```

* The binary was compiled for the system that I am running.
 - running the command `file` will show what system the file supports
 in this example if the system is X64 bits and the file is `arm64` will not work since the system is incompatible 
 `/usr/bin/blackbox: Mach-O 64-bit executable arm64`

* Check Binary documentation if any exists.

---
## Q3

Check the solution explained [here](TimeComplexity.md)


---
## Q4
One of the specifics of working in hospitality is a certain "seasonality" to our app. Peaks in traffic
correspond to Breakfast, Lunch, Dinner, increasing on Thursday/Friday nights and pretty much
all day Saturday. At the same time, we're working in many timezones so they don't all
correspond.
The application needs to scale to handle the load as each peak/trough window for a timezone is
observed. How would you design for this? Where do you think the main bottlenecks could be?
What actions would you take to understand the problem and to finally deliver an infrastructure
that would support it?


First of all, if the Peaks are already known, 
* I think that we should have a predefined rule set on the AutoScaler Group that will increase the resources based on the volume expected.
* If the application works with a MicroService pattern, some services can be identified as more important than others so defining the Autoscale rules to constantly look at these resources
and scale up as soon as an increase in traffic/requests is detected
* To minimize the data transfer when loading the Restaurant Menu, set a CDN Cache to manage the static resources closest to the requested source to reduce latency.
* Define the SLO/SLI and revisit those from time to time and make sure it is accurate so that we can define more or less resources and help to predict how much resources will be used during
this peaks, so we can assume the correct resource in use avoiding extra cost with idle Worker Nodes. 
* Set HA Cluster and make sure that in case an outage within a TimeZone all traffic can easily be redirected to the closest Region based on the Metrics defined.
