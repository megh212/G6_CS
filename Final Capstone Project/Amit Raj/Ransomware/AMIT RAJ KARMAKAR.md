+-----------------------------------------------------------------------+
| > **Theory: -**\                                                      |
| >  Ransomware offers attackers a potentially lucrative income stream |
| > through ransom payments.                                            |
| >                                                                     |
| >  The ease of use and potential for high impact make it an          |
| > attractive tool for malicious actors.                               |
| >                                                                     |
| >  However, the risk of non-payment, law enforcement attention, and  |
| > evolving defense strategies pose challenges for attackers.          |
| >                                                                     |
| > **Advantages:**\                                                    |
| > **Financial Gain:** The primary advantage for attackers is the     |
| > potential for significant financial gain through ransom payments.   |
| > Businesses and individuals often prioritize recovering their data   |
| > quickly, making them more likely to pay a ransom.                   |
| >                                                                     |
| > **Ease of Use:** Ransomware can be relatively easy to deploy,      |
| > often using readily available exploit kits and targeting common     |
| > vulnerabilities. This lowers the technical barrier for attackers.   |
| >                                                                     |
| > **Anonymity:** Ransomware attacks often leverage cryptocurrency    |
| > and anonymized communication channels, making it difficult to track |
| > down the attackers.                                                 |
| >                                                                     |
| > **High Impact:** Ransomware can cripple critical systems and       |
| > operations, causing significant disruption and financial losses to  |
| > victims. This can pressure them into paying the ransom.             |
| >                                                                     |
| > **Disadvantages:**\                                                 |
| > **Uncooperative Victims:** Not all victims will pay the ransom.    |
| > Some may choose to restore from backups or invest in incident       |
| > response. This reduces the attacker\'s guaranteed profit.           |
| >                                                                     |
| > **Law Enforcement Pressure:** Law enforcement agencies are         |
| > increasingly focused on combating ransomware. This can lead to      |
| > arrests and disruptions of attacker operations.                     |
| >                                                                     |
| > **Decreasing Trust:** As ransomware attacks become more common,    |
| > victims may become less likely to pay future ransoms, fearing they  |
| > won\'t receive their data back even if they comply.                 |
| >                                                                     |
| > **Technical Challenges:** Security measures and user awareness are |
| > improving, making it more difficult for ransomware to successfully  |
| > infiltrate and encrypt systems.                                     |
| >                                                                     |
| > **Practical: -**\                                                   |
| > **Imports: -**\                                                     |
| > **pathlib:** Provides path manipulation utilities.                  |
| >                                                                     |
| > **secrets:** Generates cryptographically secure random numbers.     |
| >                                                                     |
| > **os:** Interacts with the operating system (checking file          |
| > existence).                                                         |
| >                                                                     |
| > **base64:** Encodes/decodes binary data for textual representation. |
| >                                                                     |
| > **getpass:** Prompts users for passwords securely without echoing   |
| > them on the screen.                                                 |
| >                                                                     |
| > **cryptography:** Cryptographic library for secure key derivation   |
| > and encryption.                                                     |
| >                                                                     |
| > **Functions Used in the Code:**                                     |
| >                                                                     |
| > **generate_salt(size=16):** Generates a random salt (used for key   |
| > derivation) of the specified size (default 16 bytes).               |
| >                                                                     |
| > **derive_key(salt, password):** Derives a secure key from the       |
| > password using the provided salt. This employs Scrypt, a            |
| > memory-hard key derivation function that resists brute-force        |
| > attacks.\                                                           |
| > **load_salt():** Loads the previously saved salt from a file named  |
| > \"salt.salt\" (if it exists).                                       |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| > **generate_key(password, salt_size=16, load_existing_salt=False,    |
| > save_salt=True**): Generates a key from the password. It either     |
| > loads an existing salt or creates a new one based on the provided   |
| > arguments.                                                          |
| >                                                                     |
| > **encrypt(filename, key):** Encrypts a file using the Fernet        |
| > symmetric encryption algorithm and the given key.                   |
| >                                                                     |
| > **decrypt(filename, key):** Decrypts a file using the Fernet        |
| > algorithm and the key. It handles potential invalid key errors      |
| > (likely due to incorrect password).                                 |
| >                                                                     |
| > **encrypt_folder(foldername, key):** Recursively encrypts all files |
| > within a folder.                                                    |
| >                                                                     |
| > **decrypt_folder(foldername, key):** Recursively decrypts all files |
| > within a folder.                                                    |
| >                                                                     |
| > **How to run the code: -**\                                         |
| > encryptor.py = Python File Name\                                    |
| > Open the directory where the python code is saved as shown bellow   |
| > **Example: -**                                                      |
|                                                                       |
| ![](vert                                                              |
| opal_036df99e16ce4b63af04bcd9db97094d/media/image1.png){width="6.5in" |
| height="1.1388888888888888in"}                                        |
|                                                                       |
| > Create a file which you want to encrypt & Decrypt in the same       |
| > directory as shown bellow                                           |
| >                                                                     |
| > ![](vertopa                                                         |
| l_036df99e16ce4b63af04bcd9db97094d/media/image2.png){width="3.4375in" |
| > height="1.0625in"}                                                  |
| >                                                                     |
| > Enter the text inside it & Save the file\                           |
| > **Example: -**                                                      |
|                                                                       |
| ![](vert                                                              |
| opal_036df99e16ce4b63af04bcd9db97094d/media/image3.png){width="6.5in" |
| height="2.022222222222222in"}                                         |
|                                                                       |
| > In the File Path Bar type cmd and hit enter as shown bellow         |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| ![](vert                                                              |
| opal_036df99e16ce4b63af04bcd9db97094d/media/image4.png){width="6.5in" |
| height="0.9611100174978128in"}                                        |
|                                                                       |
| > **Enter the Bellow Command: -**\                                    |
| > **Command: -**\                                                     |
| > python encryptor.py -e                                              |
| > C:/Users/rajka/Documents/Ransomware/Encrypt_Decypt.txt **Command    |
| > Explanation: -**\                                                   |
| > **Python =** The programming language which the code is programmed\ |
| > **encryptor.py** = The file name where the code is stored           |
| >                                                                     |
| > **-e** = To encrypt the message\                                    |
| > **C:/Users/rajka/Documents/Ransomware/Encrypt_Decypt** = File path  |
| > where the message is stored                                         |
|                                                                       |
| ![](vert                                                              |
| opal_036df99e16ce4b63af04bcd9db97094d/media/image5.png){width="6.5in" |
| height="2.6305555555555555in"}                                        |
|                                                                       |
| > Hit Enter and it will ask to enter the password enter the password  |
| > which you want to encrypt the file data                             |
| >                                                                     |
| > **Note: -** As I had used the module getpass, due to security       |
| > reasons the password will be not visible make a note of it just     |
| > enter the password and hit enter as shown bellow                    |
|                                                                       |
| ![](vert                                                              |
| opal_036df99e16ce4b63af04bcd9db97094d/media/image6.png){width="6.5in" |
| height="0.4652777777777778in"}                                        |
|                                                                       |
| > **Now open the file where the data is stored: -**                   |
|                                                                       |
| ![](vert                                                              |
| opal_036df99e16ce4b63af04bcd9db97094d/media/image7.png){width="6.5in" |
| height="0.9944444444444445in"}                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| > **How to Decrypt the Data: -**                                      |
| >                                                                     |
| > **Command: -**                                                      |
| >                                                                     |
| > python encryptor.py -d                                              |
| > C:/Users/rajka/Documents/Ransomware/Encrypt_Decypt.txt              |
|                                                                       |
| ![](vert                                                              |
| opal_036df99e16ce4b63af04bcd9db97094d/media/image8.png){width="6.5in" |
| height="0.5in"}                                                       |
|                                                                       |
| ![](vert                                                              |
| opal_036df99e16ce4b63af04bcd9db97094d/media/image9.png){width="6.5in" |
| height="1.5625in"}                                                    |
|                                                                       |
| > **Prevention:**                                                     |
| >                                                                     |
| > **Back Up Your Data Regularly:** Implement a robust backup system, |
| > ideally with backups stored offline or in a separate cloud          |
| > location, to ensure you have a clean copy of your data to restore   |
| > in case of an attack.                                               |
| >                                                                     |
| > **Patch Systems and Software:** Regularly update your operating    |
| > systems, applications, and firmware with the latest security        |
| > patches to address known vulnerabilities that attackers might       |
| > exploit.                                                            |
| >                                                                     |
| > **Use Strong Passwords and Multi-Factor Authentication (MFA**):    |
| > Enforce strong password policies and enable MFA wherever possible.  |
| > MFA adds an extra layer of security that requires a second          |
| > verification factor beyond just a password to access systems.       |
|                                                                       |
| **Educate Users:** Train employees and users about ransomware        |
| threats, phishing tactics, and                                        |
|                                                                       |
| > best practices for secure online behavior. Teach them to be wary of |
| > suspicious emails, attachments, and links.                          |
| >                                                                     |
| > **Implement Security Software:** Use reputable antivirus and       |
| > anti-malware software with real-time protection to detect and block |
| > malicious software before it infects your system.                   |
| >                                                                     |
| > **Segment Your Network:** Consider segmenting your network to      |
| > minimize the potential impact of ransomware if a system is          |
| > compromised. This can help prevent it from spreading laterally      |
| > across your entire network.                                         |
| >                                                                     |
| > **Restrict User Privileges:** Implement the principle of least     |
| > privilege, granting users only the minimum level of access required |
| > to perform their jobs. This reduces the potential damage if an      |
| > attacker gains access to a user account.                            |
| >                                                                     |
| > **Disable Macros in Documents:** Macros in documents, particularly |
| > Microsoft Office files, can be used to launch malicious code.       |
| > Disabling macros by default can help prevent attacks.               |
| >                                                                     |
| > **Detection and Response:**                                         |
| >                                                                     |
| > **Monitor System Activity:** Implement real-time system monitoring |
| > tools to detect unusual activity that might indicate a ransomware   |
| > attack in progress. This can help you identify and respond to       |
| > threats quickly.                                                    |
+=======================================================================+
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| > **Have a Plan:** Develop a ransomware incident response plan       |
| > outlining the steps to take if ransomware infects your system. This |
| > plan should address containment, eradication, recovery, and         |
| > reporting procedures.                                               |
| >                                                                     |
| > **Limit Internet Access on Infected Systems:** If you suspect      |
| > infection, immediately isolate the affected device or system from   |
| > the network to prevent the ransomware from spreading to other       |
| > machines.                                                           |
| >                                                                     |
| > **Consider Reporting:** In many regions, it\'s mandatory to report |
| > ransomware attacks to law enforcement agencies. Doing so can help   |
| > them track and disrupt ransomware operations.                       |
+=======================================================================+
+-----------------------------------------------------------------------+
