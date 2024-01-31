Burp Suite:
Burp Suite is a web application security testing tool. It is widely used for finding various types of security vulnerabilities.

First you can open browser from the proxy tab 

Examples   - 
1. Intercepting Proxy: After turning this feature on it captures and can be used to modify HTTP traffic.
2. Decoder : Used to decode or encode a text or ciphertext
3. Repeater: Manually manipulate and reissue requests.
4. Intruder: Automated attacks on web applications.

Nmap:
Nmap is an open-source network scanner used to discover hosts and services on a computer network.
  
Example :
1. Basic Scan: nmap 192.168.1.1
2. Service Version Detection: nmap -sV 192.168.1.1
3. Operating System Detection: nmap -O 192.168.1.1
4. Aggressive Scan: nmap -A 192.168.1.1

Gobuster:

Gobuster is a directory and file brute-forcing tool designed to locate existing web resources on a target server.

Examples:
1. Basic directory brute force: gobuster http://hello.com/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt 
2. Brute force with a specified extension: gobuster dir -u http://10.10.63.233 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php,html,txt 
3. Brute force without a specific status code:gobuster dir -u https://hello.com/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -b 404
4. Brute force with custom user-agent: gobuster  dir -u http://10.10.63.233 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -a "Admin”
5. Brute force with a specified number of threads: gobuster  dir -u http://10.10.63.233 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 10
  

Dirb:

Dirb is a web scanner, specifically designed for identifying and analyzing webserver directories.

Examples:
1. Basic directory scan:  dirb http://10.10.242.236
2. Scan with a specific wordlist: dirb http://10.10.242.236 -w /usr/share/dirb/wordlists/directory-list-2.0.txt  
3. Scan a specific URL with a specified extension: dirb http://10.10.242.236 -w usr/share/dirb/wordlists/directory-list-2.0.txt -X .php
4. Scan with a custom user-agent to find the response changes: dirb http://10.10.242.236 -w /usr/share/dirb/wordlists/directory-list-2.0.txt -a "pickle-rick"
  

Nikto:
Nikto is an open-source  web server scanner designed to identify potential security vulnerabilities on websites. By scanning for a wide range of issues such as dangerous files, misconfigured services, and vulnerable scripts, Nikto helps assess the overall security posture of a website. 

Examples:
1. Basic scan: nikto -h https://hello.com
2. Forces to use ipv4 to scan : nikto -h https://hello.com -ipv4
3. Saves the result into a file: nikto -h https://hello.com -output /home/kali/Desktop/result.txt
4. Run chains of proxy serviers to not get detected: sudo proxychains nikto -h https://hello.com 

