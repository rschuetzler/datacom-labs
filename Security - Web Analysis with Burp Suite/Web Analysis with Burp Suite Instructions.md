Web Analysis with Burp Suite
=================================

Burp Suite is a tool used to test websites for vulnerabilities. Burp Suite can also be used simply to better understand the data that is being sent between the web browser and the web server.

Prerequisites
------------------
1. Kali Linux installed in VirtualBox
2. PentesterWeb installed

Virtual Machine Setup
------------------------
1. In VirtualBox, ensure that the network adaptesr for Kali Linux and PentesterWeb are both set to "internal network."
1. In VirtualBox, start the Kali Linux and PentesterWeb virtual machines.
2. Ensure that the IP addresses are correct. Run `ifconfig` in a terminal to determine if the IP address matches the value below.
  - Kali: 192.168.2.10
  - PentesterWeb: 192.168.2.5
  
If the Kali IP address needs to be udpated, run:

```
ifconfig eth0 192.168.2.10
```

If the PentesterWeb IP address needs to be updated, run:

```
sudo ifconfig eth0 192.168.2.5
```

3. Ensure that the machines can ping each other. You can close the Kali terminal when the pings are successful.

Kali Iceweasel Configuration
------------------------------
Iceweasel is a custom version of Mozilla Firefox.

1. In Kali, Launch Iceweasel by clicking on the icon with the polar bear.

&nbsp;![Iceweasel Icon](iceweasel-icon.png)

2. In Iceweasel, open preferences.

&nbsp;![Iceweasel Proxy Settings](iceweasel-settings1.png)

3. Click `Advanced`, `Network`, `Connection Settings`.

&nbsp;![Iceweasel Proxy Settings](iceweasel-settings2.png)

4. Make the following changes to the proxy.
  - Select `Manual proxy configuration`.
  - Enter `127.0.0.1` as the HTTP Proxy.
  - Enter `8080` for the port.
  - Check the box to use the proxy for all protocols.
  - Delete all text in the "No proxy for:" textbox.

&nbsp;![Iceweasel Proxy Settings](iceweasel-settings3.png)

5. Click OK and Close to save the settings.

Burp Suite
---------------------------------
1. Launch Burp Suite by clicking on the gray and orange icon on the Kali desktop.

&nbsp;![Burp Suite Icon](burp-icon.png)

2. Click the `Proxy` tab. Notice that button that says, "Intercept is on." All traffic going from Iceweasel to the web will be intercepted by Burp Suite.

&nbsp;![Burp Suite Intercept](burp-intercept.png)

3. In Iceweasel, enter `192.168.2.5` for the URL and press [enter].

&nbsp;![Load Website in Iceweasel](iceweasel-load.png)

Notice that the page does not render.

4. Open Burp Suite. A new `GET` request should show up on the Proxy > Intercept tab.

&nbsp;![Burp Suite Intercept](burp-intercept-get.png)

5. Click the `Forward` button in Burp Suite.

&nbsp;![Burp Suite Forward](burp-forward.png)

Notice that the page will begin to load in Iceweasel. Also notice that Burp Suite wil show other requests that have been intercepted. All images and other files needed by the web page will have to be forwarded for the website to render as if no proxy were being used.

6. In Burp Suite, click the "Intercept is on" button to turn off intercepting.

7. Reload the page in Iceweasel. Notice that the page will load almost instantly with no need to forward the requests from Burp Suite.

Why do you think it would be helpful to intercept all requsts and responses?

Request Analysis
--------------------------------------
1. Turn Burp Suite intercepting on.
2. In Iceweasel, click the XSS Example 1 link.
3. The `GET` request will be captured in Burp Suite.
4. Click the `Params` tab to see all parameters being sent to the server. You may need to resize the columns to see all data.

&nbsp;![Request Parameters](burp-intercept-params.png)

5. Modify the `name` parameter value by double clicking on the existing value. Change it to "friend."

&nbsp;![Modify Parameters](burp-intercept-params-change.png)

6. Click `Forward`.

7. In Iceweasel, look at the output. Notice how the name value in the URL does not match the name value in the web page. Why do you think this happened?

&nbsp;![URL and Variable Mismatch](iceweasel-url-variable-mismatch.png)

Reflection
---------------------------------------
  - Can you trust user input?
  - Can you trust user input if you use JavaScript validation?
  - How can you properly sanitize user input?

