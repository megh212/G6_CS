**Assignment -3**

\*Explain any 5 tools in Kali Linux and explain 5 commands in each of
that with images.

Sol:\
Here I am explaining the 5 tools in the kali Linux 1.Nmap\
2.theharvester\
3.Nikto\
4.Hydra\
5.gobuster

1\. Nmap\
Nmap is short for Network Mapper. It is an open-source Linux
command-line tool that is used to scan IP addresses and ports in a
network and to detect installed applications.

Commands:\
1.OS detection (it scans the operating system of an target)

> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image1.png){width="5.891666666666667in"
> height="3.15in"}
>
> 2.Aggressive Scan

The aggressive scan option combines various scan techniques, including
service version detection, OS detection, and script scanning, to provide
comprehensive information about the target.

> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image2.png){width="6.5in"
> height="4.0625in"}
>
> 3.Port scanning
>
> It scans the ports in a given range

![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image3.png){width="4.458333333333333in"
height="2.3in"}

> 4.Version Detection\
> It tries to determine the version of services running on the target
> ports. Useful for identifying vulnerabilities.
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image4.png){width="5.330555555555556in"
> height="3.3305555555555557in"}
>
> 5.Timing and Performance (-T\<0-5\>):
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image5.png){width="5.330555555555556in"
> height="3.330554461942257in"}
>
> 2\. theHarvester :\
> The package contains a tool for gathering subdomain names, e-mail
> addresses, virtual hosts, open ports/ banners, and employee names from
> different public sources.
>
> Commands :\
> 1.theharvester -d kali.org -b duckduckgo
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image6.png){width="5.329166666666667in"
> height="3.3305555555555557in"}
>
> 2.theharvester -d gatesit.ac.in -b duckduckgo
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image7.png){width="4.583333333333333in"
> height="2.330554461942257in"}
>
> 3.theHarvester -d gatesit.ac.in -b google,duckduckgo,pgp,bing
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image8.png){width="6.5in"
> height="3.6597222222222223in"}
>
> 3.Nikto
>
> The Nikto web server scanner is a security tool that will test a web
> site for thousands of possible security issues. Including dangerous
> files, mis-configured services, vulnerable scripts and other issues.
> It is open source and structured with plugins that extend the
> capabilities. These plugins are frequently updated with new security
> checks.
>
> Commands:\
> 1.nikto -h 192.168.193.7
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image9.png){width="5.708333333333333in"
> height="3.0694444444444446in"}
>
> 2.nikto -h -full
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image10.png){width="6.5in"
> height="3.6555555555555554in"}
>
> 3.nikto -h gatesit.ac.in -p 8080
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image11.png){width="6.5in"
> height="3.6555555555555554in"}
>
> 4.nikto -h gatesit.ac.in google.com

we can use this operation on multiple hosts

> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image12.png){width="5.516666666666667in"
> height="3.716666666666667in"}
>
> 5.Nikto -h gatesit.ac.in -id 9347:1234

![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image13.png){width="6.266666666666667in"
height="3.6555555555555554in"}

> 4.Hydra tool

Hydra is a parallelized login cracker which supports numerous protocols
to attack. It is very fast and flexible, and new modules are easy to
add.

This tool makes it possible for researchers and security consultants to
show how easy it would be to gain unauthorized access to a system
remotely.

Commands:

> 1.hydra -l user -P rockyou.txt
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image14.png){width="6.5in"
> height="3.6555555555555554in"}
>
> 2.hydra -l user -P rockyou.txt [telnet://192.169.0.1]{.underline}
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image15.png){width="6.5in"
> height="3.6555555555555554in"}
>
> 3.hydra -l user -P wordlist.txt rdp://192.169.0.1
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image16.png){width="6.5in"
> height="3.6555555555555554in"}
>
> 5.Gobuster\
> Gobuster is a brute-force scanner tool that can find hidden files,
> directories, and URLs on websites. It can also help find DNS
> subdomains and virtual host names.

Commands:\
1.gobuster -dir -u -w rockyou.txt

![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image17.png){width="4.919444444444444in"
height="2.7694433508311462in"}

> 2.gobuster -dns -d -w rockyou.txt
>
> ![](vertopal_0a4b8b8d2bbf46e281dc88babf77cbd7/media/image18.png){width="6.5in"
> height="3.6555555555555554in"}
