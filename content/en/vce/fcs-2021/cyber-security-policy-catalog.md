---
title: "Cyber Security Policy Catalog"
description: "FCS Unit 3 notes - cyber governance, user issues, and policy catalog."
weight: 3
markup:
  tableOfContents:
    startLevel: 2
    endLevel: 2
---

{{< intro >}}
Notes for cyber security policy catalog (governance, DNS, email, malvertising, impersonation, cyber crime, and appendix). Below are **Table of Contents**: 
{{< /intro >}}
{{< toc >}}

## Cyber Governance Issues

The Internet began as the Advanced Research Projects Agency Network (ARPANET), a U.S. military-funded network designed to survive a nuclear attack. It quickly became a tool for sharing information among computer science researchers in the military, its contractors, and its academic collaborators. The Internet Engineering Task Force (IETF) published as these new protocols as Requests for Comments, which allowed others to quickly learn and extend them.

### Internet Corporation for Assigned Names and Numbers (ICANN)

- The vast majority of Internet infrastructure and functions are decentralized, certain centralized planning and coordination functions are required. The most visible are the allocation of names ( like [whitehouse.gov](http://www.whitehouse.gov)) and numbers (Internet Protocol address). These coordination functions were initially performed at Stanford Research Institute. 

- In 1972, these functions were transitioned to the Internet Assigned Numbers Authority (IANA). The National Telecommunications and Information Administration (NTIA), an agency of the U.S. Department of Commerce, announced a non profit organization the Internet Corporation for Assigned Names and Numbers (ICANN) in 1998 to govern the IANA functions. 

- The Internet is a U.S. creation, and the US Govt. has been leery to relinquish all control over the basic Internet coordination functions. ICANN technically remained a U.S. government (USG) contractor until the signing of the Affirmation of Commitments (AoC) a Memorandum of Understanding between the USG and ICANN on principles of multistakeholder Internet governance in 2009. 

- The key cyber security policy issue is the Internet governance model and, in particular, the modality of participation by world governments. If governments disagree on the central coordination functions and begin to use different standards/procedures, the Internet may fragment into multiple or partially connected pieces. 

- On October 1, 2016, ICANN ended its contract with the NTIA and entered the private sector.

### Net Neutrality

Most people get their high-speed internet access from only a few telecommunications giants When we send or receive data over the internet, we expect those companies to transfer that data from one end of the network to the other. Period. We don’t expect them to analyze or manipulate it.

Network neutrality means applying well-established “common carrier” rules to the internet in order to preserve its freedom and openness. Common carriage prohibits the owner of a network that holds itself out to all-comers from discriminating against information by halting, slowing, or otherwise tampering with the transfer of any data (except for legitimate network management purposes such as easing congestion or blocking spam). At times few cyber security policies and net neutrality principles seem to be at odds.

#### Cyber Security Policy Issues Concerning Net Neutrality

Below are few policy issues from textbook (fig: 6.1.1): 

  * The operation of the DNS Root Server System shall be performed under contract with some entity or entities.
  * The Internet Center for Assigned Names and Numbers (ICANN) shall be required to allocate a percentage of its revenues for security and resilience.
  * ICANN shall turn over responsibility for Internet name and number space to the International Telecommunications Union (ITU).
  * ISPs shall filter at their client connections to ensure that source address in incoming traffic is within some legitimate network prefix range allocated to the corresponding customer.



### Internet Names and Numbers

#### Internet Addresses

With so many devices connected to the internet, we require some mechanism to uniquely identify every device that is connected to the internet. Also we require some centralized system which takes care of this mechanism so that the signs which are used to identify each device are not duplicate; else the whole purpose is defeated. To take care of this, we have a centralized authority known as **Internet Assigned Numbers Authority (IANA)** , which is responsible for assigning a unique number known as **IP(Internet Protocol)** address.

- An IPv4 address is a 32-bit binary number which is divided into four octets and each octet consists of 8 binary digits and these octet are separated by a dot(.). An example of an IPv4 address is `11110110.01011010.10011100.1111100`

- Each 8-bits in an octet can have two binary values i.e. 0 and 1. Therefore, each octet can have min value 0 to max value 256 and in total have 256 different combinations. In decimal, the above IP address is expressed as `123.45.78.125`

- An IPv4 address consists of two parts: the Network Part and the Host Part. The network part identifies the network to which a device belongs, while the host part identifies a specific device within that network. 

- IPv4 address are running out due to expoetinally increasing number of devices so a newer IPv6 address represented as eight groups, separated by colons, of four hexadecimal digits. 

- The full representation may be shortened; For example: `2001:0db8:0000:0000:0000:8a2e:0370:7334` becomes `2001:db8::8a2e:370:7334` was drafted and implemented as defualt now as days.

#### Domain Name System (DNS)

Whenever we browse any website on the internet, we type name something like `www.uou.ac.in` and we rarely deal with IP address like `104.28.2.92` but the fact is even if we type `http://104.28.2.92` in the URL, it will land us to the same webpage.

We are comfortable using and remembering the names instead of a number. Moreover, these IP address changes over time and some of the sites have multiple IP address. Also, the transfer of the data over internet is only possible using IP addresses because the routing of the packet of data sent over internet is done using IP address. **Domain Name System (DNS)** take cares of this translation job to simplify and to save us from remembering these changing IP address numbers.

Whenever we type an address like `http://www.uou.ac.in`, the process of DNS name resolution, takes place in the background. The computer keeps the track of recently visited sites and locally maintains a (routing table) database in the DNS cache. In case, the IP address of the site you have requested for is not found in the DNS cache of our local computer, then it proceeds to find it in the DNS server of the Internet Service Provider(ISP). These DNS servers of ISP also maintain the cache of the recently visited pages. Just in case, the information is not found here also, the DNS server of the ISP forward the query to the root nameservers. The root name servers publish the root zone file to other DNS servers and clients on the Internet. The root zone file describes where the authoritative servers for the DNS top-level domains (TLD) are located. There are currently 13 root name servers.

These root nameservers directs the query to the appropriate Top-Level Domain(TLD) nameservers by reading the last part of the URL first. In our example the URL was `http://www.uou.ac.in`. The last part is `.in` Some of the examples of TLD name servers are `.com, .biz, .org, .us, .in,` etc. These TLD nameservers acts as a switchboard and direct the query to the appropriate authoritative nameserver maintained by each domain. These authoritative nameserver maintains DNS records along with other useful information. This address record is returned back to the requesting host computer via TLD nameservers, nameservers, ISP’s DNS server. These intermediary server keeps the record of this IP address in their DNS cache, so that if the same request is encountered again, they don’t have to go through this process again. If the same URL is requested again, the DNS cache of the local host computer will return the IP address of the URL.

#### Domain Name System Security Extensions (DNSSEC)

A major concern with Internet names and numbers is that of either accidental or intentional diversion of Internet traffic to unauthorized destinations. For example, the translation from Internet names to Internet numbers can be subverted by a cyber attack called _**DNS poisoning**_. DNS poisoning refers to the corruption of a DNS server so that it stores an incorrect address for a given computer name. The incorrect address is usually a malicious site designed to look just like the website on the computer named in the query. allows attackers to divert legitimate user traffic to malicious sites without their knowledge, and without touching the user’s computer, simply by attacking the DNS server that the user queries for addresses.

DNS was not designed with security in mind and is vulnerable to poisoning, man-in-the-middle attacks. Thus the DNSSEC were created to address these concerns. The process uses public-private key cryptography to authenticate DNS records with the authoritative source. For DNSSEC to work effectively, a DNS server public key must be distributed in such a manner that users can verify its integrity. Then users can encrypt queries that can only be decrypted by the target DNS server, and DNS servers can encrypt responses with a private key.

_**Digital Signature**_: the public-private key technology allows the key holder to sign data with the private key in such a way that allows the public key to be used to verify the digital signature. Because the public key is known to anyone, digital signatures do not facilitate confidentiality, merely data provenance and integrity.

> The figure 6.1 in course textbook illustrates Message sequence diagram for DNSSEC.

#### Concerned Cyber Security Policy Issues

Below are few policy issues from textbook (fig: 6.1.2): 

  * All DNS names shall be associated with individuals or corporations who are accountable for services provided under them.
  * DNS server operators shall be licensed, and failure to maintain proper security controls shall result in loss of license.
  * Operators of border gateway protocol routers shall be penalized for routing traffic to locations that are not registered for them.
  * Government telecommunications regulatory agencies shall recommend and enforce effective and efficient means of securing telecommunications infrastructure.

### Copyright and Trademarks

### Email and Messaging

Emails can be used blatantly to impersonate a company. Email impersonation may happen from a person’s own inbox due to malicious software or servers not requiring the presentation of a key for authentication or as long as any one server in the email relay between a sender and receiver supports a text-only-based command strings (email protocols).

#### Email Spamming & Phishing

- In the early days of the Internet, users would use the word “spam” to describe content they had no wish to see, and excessive unwanted multiple postings elicited “spam” as the reply from angry users. The term _**spam**_ now generically refers to any unwanted email content (Furr 1990). Internet watchdogs keep records of spam in order to identify perpetrators with the goal of reducing it. But, any Internet user knows, these efforts are largely unsuccessful in preventing spamming but these days email detection is at near perfect rate.

- _**Phishing**_ , refers to baiting, or luring, Internet users to click on links that take them to malicious websites. The malicious sites may be domain squatting look-alikes that collect user names and passwords. They may download malware. They may be fraudulent scams to trick users into transferring money from their bank accounts. When a specific set people like high net worth individuals or CxO’s of organizations are targeted by phishing emails, it is called _**spearphishing**_ , in analogy with whales as the target.

#### Security of Emails & Messages:

Sometimes we would like e-mail to be more secure. To define and implement a more secured email protocols, we need to understand the exposures & threats invovled in ordinary e-mail.

##### Threats to E-mail

  * Message interception (confidentiality)
  * Message interception (blocked delivery)
  * Message interception and subsequent replay
  * Message content modification
  * Message origin modification
  * Message content forgery by outsider
  * Message origin forgery by outsider
  * Message content forgery by recipient
  * Message origin forgery by recipient
  * Denial of message transmission

##### Requirements and solutions

Following protections must be taken for protection in emails

  * Message confidentiality (the message is not exposed enroute to the receiver)
  * Message integrity (what the receiver sees is what was sent)
  * Sender authenticity (the receiver is confident who the sender was)
  * Nonrepudiation (the sender cannot deny having sent the message)

##### Technologies available to companies that wish to secure email communications

  * **Sender Policy Framework (SPF)** was developed from 2000 with publication as an experimental RFC 4408 in 2006. The basic principle is that the domain owner publishes details of mail servers that legitimately send Email on behalf of the domain via DNS text (TXT) records. The intent is that if a message is received from a server not included in these DNS records, then the receiving Email server can presume the message has not been sent by a server in use by the domain and take appropriate ‘counter-spam’ action.
  * **Sender ID Framework (SIDF)** , which utilizes DNS to identify the authorized email server for a domain and does not allow email from a domain unless the sending server is identified in the DNS records for the domain when a valid signature is expected. SIDF is generally considered obsolete with its role now fulfilled by _**DMARC**_.
  * **DomainKeys Identified Mail (DKIM)** goes a step further and allows an encryption key to be stored in DNS, so companies can set rules to permit, rejection, deletion, or tag unsigned or improperly signed messages from a given business partner.
  * **Transport Layer Security (TLS)** , which is called an opportunistic protocol because it can be set to require the highest level of security that is available on the server with which it communicates.
  * **Domain-Based Message Authentication, Reporting And Conformance (DMARC)** introduces the idea of ‘domain alignment’ between the ‘From’ and ‘Mail From’ addresses. DMARC is designed to complement and bolster SPF and DKIM and uses both as its means of validating Email. DMARC provides a reporting mechanism so that a domain owner can gain visibility of how recipients are handling mail quoting their domain name. And a formal statement of the action the domain owner would like the recipient to take in the case of a message failing the DMARC checks.



#### Concerned Cyber Security Policy Issues

Below are few policy issues from textbook (fig: 6.1.4):

  * All entities that participate in electronic commerce shall offer customers the ability to verify their email server via standard protocols.
  * All email communications on behalf of or concerning the organization shall utilize organizationsupported email services.
  * Delivery and read receipts on email shall provide proof of electronic information delivery.
  * Individuals shall have the ability to place their email addresses on a list which would make it illegal for marketers to send them unwanted email.



## Cyber User Issues

Security issues for cyber users have mostly arisen from unintended side effects of the e-commerce race to participate in new markets. E-commerce transactions flow between the shopper, the shopper’s computer, the network connection between shopper and e-commerce web server, the e-commerce web server, and e-commerce vendor internal network, and the connections between the e-commerce vendor and the service providers they need to close the transaction, such as a credit card payment clearing company. 

All of these connections are created using software, and any of that software may have a bug or a flaw that allows an intruder to observe cyber user data flow or disrupt the e-commerce transaction. In many of these points of connectivity, observation of data flow provides information that may be used for later attacks. It is the attacker’s goal to exploit one or more of the three other players for illegal gains. Using vulnerabilities in software, application configurations, hardware, and even user habits, an attacker will seek to exploit these vulnerabilities to the attacker’s advantage. e-Commerce attacks are constantly occurring as the product of three archetypes: _**exploiters, enablers, and expeditor**_.

**Exploiters** carry out data theft and fraud. **Enablers** are businesses whose practices allow it. **Expeditors** are technologists who identify the root cause from a technical point of view, though they may be attackers or defenders. The exploiters not only exploit the consumer, an identity theft victim, but also exploit low-level social misfits, such as meth addicts. They enlist the social misfits to withdraw unwitting consumers’ cash out of automatic teller machines or to order luxuries on the unwitting consumers’ credit cards. 

The stories sporadically include tales of victories of law enforcement “expeditors” who figure out how the exploiters did it. The moral of every sad story is that the enabler did not sufficiently protect data within its custody, while an evil genius controlling three or more layers of organized criminal structure above the social misfits is never actually caught. The consumer is left with damaged credit, as well as loss of time and money, while the enabler claims that “adequate” risk measures are in place to secure the enterprise.

> Cyber user security issues can be divided into the six subsections.

### Malvertising

Malvertising is an anagram of the words “malicious” and “advertising.” e-Commerce businesses that rely on advertising typically are designed to attract consumers in a desired demographic, the advertising “target.” One method of reaching the target is to identify web pages frequented by the target and purchase ads directly on those web pages. The web page owner/seller may require that the ad be provided to them for placement, or they could simply link to a site provider by the ad buyer and direct the user’s browser to access the buyer’s web content directly. This easy access to the Internet consumer has attracted criminals seeking to install malware.

#### What is malware?

Malware = Malicious + Software, Malware is any piece of hardware, software or firmware that is intentionally included or introduced into a computer system for unauthorized purposes usually without the knowledge or consent of the user. Software can be considered malware even if it is not actually malicious. The perceived intent of the author is a consideration.

Malware includes viruses, trojans, worms, hoaxes, logic bombs, etc. Be careful with terminology _**!A virus is malware but not all pieces of malware are viruses!**_

#### Malware History - Early Malware

  * [ late 1940’s - early 50’s] Von Neumann designed a finite automata with 200,000 cells which could exist in one of twenty-nine states and could self-replicate.
  * [1979] - Christopher Langton writes a self-replicating computer “organism” on an Apple II desktop.
  * 1980’s saw the rise of the first true viruses, such as Elk Cloner [refer to appendix for complete timeline].

A less frequently reported but still significant profit margin e-commerce criminal activity that comes under the heading of malvertising is _**coupon fraud**_. Criminals often copy or modify coupons to increase values, decrease purchase requirements, defeat or eliminate security codes, extend or eliminate expiration dates, and/or alter disclaimers, terms and conditions or create complete fake coupons.

#### Concerned Cyber Security Policy Issues

Below are few policy issues from textbook (fig: 6.2.1):

  * e-Commerce marketing that includes redirection of individual computers to sites via links that they did not intentionally follow shall be illegal.
  * It shall be illegal to install and run software on machines owned by someone else.
  * All legitimate software execution shall be recognizable to the average computer user.
  * Internet coupons shall identify the authorized consumer by name, address, and a unique identification number.

### Impersonation

Impersonation deals with various types of impostors on the Internet, from anonymous postings to account hijacking. An **impersonation attack** is a form of fraud in which attackers pose as a known or trusted person to dupe an employee into transferring money to a fraudulent account, sharing sensitive information (such as intellectual property, financial data or payroll information), or revealing login credentials. Threat actors may impersonate family, friends, colleagues, and legitimate businesses and banks, including executives, vendors, and customers, also as officials from government agencies.

Impersonation Attacks Constructed by **Finding the Target** , then **Creating Credibility** and later **Executing the Attack**. The final and the most important step is to choose a type of attack. These are top 3 tactics used by attackers:

  * By Registering a Look-Alike Email Domain
  * Editing the Display Name: The majority of the mobile email clients only show the display name of the sender. This makes it quite easy for the attacker to edit their display name and trap the victim into their game. For example, the attacker sends the message using an email like [xyz@gmail.com](mailto:xyz@gmail.com) but edits the display name to the person being impersonated.
  * Using a Free Email Account: This is another common tactic used by attackers. All they do is send a message through a free email account such as Gmail, Yahoo, etc. In the email, the sender indicates that they have been locked out of their official account and need immediate help in order to get a task done.

#### Cyber Security Policy Issues Concerning Impersonation

Below are few policy issues from textbook (fig: 6.2.2):

  * All Internet communication shall be attributable to an individual. This policy would require identification and authentication as a condition for Internet connectivity. No anonymous access would be allowed.
  * Assuming a false identity on the Internet shall be prohibited.
  * Possession of credentials that correspond to another person’s digital identity shall be forbidden.
  * International and national standards organizations shall issue standards for identity assurance ratings, and these shall be required labels on e-commerce websites.



### Appropriate use

It addresses common Internet behaviors that some deem antisocial, and may not be criminal simply because they have not yet been formally considered by legislators. In the software industry, end-user license agreements (_**EULAs**_) are used to specify the terms and conditions under which software is licensed to those who purchase it. These agreements typically limit the authority of the user to copy the software and limit the liability of the vendor for any faults in software operation. These agreements are typically presented in an automated fashion while a user is installing software.

One common method of software license verification is for the software to _**phone home**_ , which is used to refer to the capability of software to access the software vendor’s website. Phone home features check attributes of the software installation with the vendor’s records of purchase. For example, if a purchaser has installed the software on more machines than permitted via the EULA, the software may disable itself. The opposite of a phone home feature is a _**command and control feature**_. A command and control feature allows a central administrator to control software on multiple computers. Each controlled computer is configured to listen to the network; that is, network listening is a technique that software uses to be alerted to Internet queries. Network listening features combine the Internet address of a computer with a subaddress, or port, that can be assigned by a computer operating system to a software process. A typical computer has _64,000 ports_ that can be distributed among software processes, and the controlled software will select one that is not used by any common programs. Malware command and control features are sometimes referred to as _**RATs**_ , an acronym for remote access tool that conveys its malicious purpose.

#### Cyber Security Policy Issues

Below are few policy issues from textbook (fig: 6.2.3):

  * Any software installed on computers without the express consent of the owner shall be considered trespassing.
  * Software companies shall be prohibited from implementing phone home features by default.
  * All computer operating systems that allow phone home and command and control features in software running on that operating system shall give users a choice of whether to enable them.
  * Software shall not be installed in such a way that it runs without the user’s express knowledge.



### Cyber Crime

The term cyber crime is used to describe an unlawful activity in which computer or computing devices such as smartphones, tablets, etc. which are stand alone or a part of a network are used as a tool or/and target of criminal activity.

### Classification of Cyber Crimes

The cyber criminal could be internal or external to the organization facing the cyber attack. Based on this fact, the cyber crime could be categorized into two types:

#### Insider Attack

An attack to the network or the computer system by some person with authorized system access is known as insider attack. It is generally performed by dissatisfied or unhappy inside employees or contractors. The motive of the insider attack could be revenge or greed. It is comparatively easy for an insider to perform a cyber attack as he is aware of the policies, processes, IT architecture and weakness of the security system. Moreover, the attacker have access to the network. Therefore, it is comparatively easy for an insider attacker to steel sensitive information, crash the network, etc. In most of the cases the reason for insider attack is when an employee is fired or assigned new roles in an organization, and the role is not reflected in the IT policies. This opens a vulnerability window for the attacker. The insider attack could be prevented by planning and installing an Internal intrusion detection systems (IDS) in the organization.

#### External Attack

When the attacker is either hired by an insider or an external entity to the organization, it is known as external attack. The organization which is a victim of cyber attack not only faces financial loss but also the loss of reputation. Since the attacker is external to the organization, so these attackers usually scan and gathering information. An experienced network/security administrator keeps regular eye on the log generated by the firewalls as external attacks can be traced out by carefully analyzing these firewall logs. Also, Intrusion Detection Systems are installed to keep an eye on external attacks.

The cyber attacks can also be classified as structure attacks and unstructured attacks based on the level of maturity of the attacker.

#### Unstructured Attacks

These attacks are generally performed by amatures who don‟t have any predefined motives to perform the cyber attack. Usually these amatures try to test a tool readily available over the internet on the network of a random company.

#### Structured Attacks

These types of attacks are performed by highly skilled and experienced people and the motives of these attacks are clear in their mind. They have access to sophisticated tools and technologies to gain access to other networks without being noticed by their Intrusion Detection Systems(IDSs). Moreover, these attackers have the necessary expertise to develop or modify the existing tools to satisfy their purpose. These types of attacks are usually performed by professional criminals, by a country on other rival person or the country, terrorists, companies, etc.

![Crimeware marketplace diagram](https://i.imgur.com/LJ2Fb0f.png)

#### Reasons for Commission of Cyber Crimes

There are many reasons which act as a catalyst in the growth of cyber crime. Some of the prominent reasons are:

  * [Money]: People are motivated towards committing cyber crime is to make quick and easy money.
  * [Fun]: The amateur do cyber crime for fun. They just want to test the latest tool they have encountered.
  * [Cyber Espionage]: At times, the government itself is involved in cyber trespassing to keep eye on other person/network/country. The reason could be politically, economically socially motivated.
  * [Revenge]: Some people try to take revenge with other person/organization/society/ caste or religion by defaming its reputation or bringing economical or physical loss. This comes under the category of cyber terrorism.
  * [Recognition]: It is pride if someone hacks the highly secured networks like defense sites or networks.
  * [Anonymity]: Many time the anonymity that a cyber space provide also motivates the person to commit cyber crime as it is much easy to commit a cyber crime over the cyber space and remain anonymous as compared to real world.


![Crimeware risk–profit tradespace](https://i.imgur.com/aLFliIy.png)

#### Cyber Security Policy Issues

> listed below are few policy issues from textbook fig: 6.2.4

  * The Internet shall not be used to incentivize violence against persons or property.
  * Individuals who are stalked, bullied, blackmailed, and/or harassed on the Internet shall be able to declare that the behavior is harassment under the law.
  * Individuals who use false identities or anonymous access to report false crimes or emergencies, as well as those who itness such events without reporting them, shall receive mandatory jail terms.
  * Existing international organizations—such as NATO, ASEAN, OAS, EU, and AU—shall include cyber crime as part of all their eliberations and treaties.


### Geolocation

![Botnet attack path](https://i.imgur.com/czqzWRE.png)

#### Cyber Security Policy Issues Concerning Geolocation

Below are few policy issues from textbook (fig: 6.2.5):

  * Purposely hiding one’s physical location, or helping others hide their physical location, on the Internet shall not be criminalized. This policy would allow anonymization services, as well as the installation of proxy services on bots, to mask the source of Internet activities.
  * Those who allow their networks to be used by cyber criminals shall be guilty of aiding and abetting any crime committed. This policy would require all networks owners to identify all users and police their borders for unauthorized use.
  * Geolocational information coordinates for any mobile device shall be available to law enforcement. This policy would require mobile devices to allow access to geolocational information files, such as GPS coordinates, on mobile devices upon request.


### Privacy & Cyber Conflict Issues

### Intellectual property Theft

### Cyber Espionage

Cyber spying or cyber espionage, is the act or practice of obtaining secrets and information without the permission and knowledge of the holder of the information from individuals, competitors, rivals, groups, governments and enemies for personal, economic, political or military advantage using methods on the Internet.

### Cyber Sabotage

Cyber sabotage is a phrase that reflects the damage potential from cyberspace terrorists. Any kind of enterprise may be targeted by saboteurs, from individuals to nation-states. It is not uncommon for disagreements among hackers to evolve into the cyber equivalent of gang wars, wherein rivals destroy each other’s information. uch activity may even escalate from the cyber to the physical world.

When cyber attackers bond over similar political or ethical causes, they are classified as hactivists. Objects of hactivist attacks may be corporate or non-for-profits or individuals. Nation-state threats aiming to exploit cyberspace vulnerabilities may target any component of the national infrastructure, including, but not limited to, the operation of industrial control systems, the integrity of banking transactions, or the readiness of military equipment.

#### Cyber Security Policy Issues Concerning Cyber Sabotage

Below are few policy issues from textbook (fig: 6.3.3):

  * International humanitarian law shall apply to conflict in cyberspace.
  * Hactivists shall be considered a form of free speech.
  * Government-classified sensitive information shall not be available to any one individual without the oversight of at least one other.
  * Nations shall define their critical infrastructure sectors and create mechanisms to coordinate with these sectors to create smarter policies for cyber and industrial control system security.

### Cyber Warfare

Cyber warfare refers to the use of digital attacks – like computer viruses and hacking – by one country to disrupt the vital computer systems of another, with the aim of creating damage, death and destruction. Future wars will see hackers using computer code to attack an enemy’s infrastructure, fighting alongside troops using conventional weapons like guns and missiles.

Cyber warfare involves the actions by a nation-state or international organization to attack and attempt to damage another nation’s computers or information networks through, for example, computer viruses or denial-of-service attacks.

### Cyber Terrorism

Cyber terrorism is the convergence of cyberspace and terrorism. It refers to unlawful attacks and threats of attacks against computers, networks and the information stored therein when done to intimidate or coerce a government or its people in furtherance of political or social objectives.

## Appendix

### IP Address Classes

IP addresses are classified into five categories based on the availability of IP range.

| IPv4 Address Class | Address range | Supports | 
|---|---|---|
| Class A | 1.0.0.1 to 126.255.255.254 | Supports 16 million hosts on each of 127 networks. | 
| Class B | 128.1.0.1 to 191.255.255.254 | Supports 65,000 hosts on each of 16,000 networks. | 
| Class C | 192.0.1.1 to 223.255.254.254 | Supports 254 hosts on each of 2 million networks |  
| Class D | 224.0.0.0 to 239.255.255.255 | Reserved for multicast groups |
| Class E | 240.0.0.0 to 254.255.255.254 | Reserved for future use, or Research and Development Purposes. |
  
### More Resources on Impersonation Attacks

  * [What is an impersonation attack? | Phishing | Egress US](https://www.egress.com/en-us/resources/cybersecurity-information/phishing/what-is-an-impersonation-attack)
  * [Impersonation Scams | New Jersey Cybersecurity & Communications Integration Cell (nj.gov)](https://www.cyber.nj.gov/garden_state_cyber_threat_highlight/impersonation-scams)


### Malware Timeline

> Credit: [Sheridan University Course - INFO43921 : Malicious Software](https://ulysses.sheridanc.on.ca/coutline/coutlineview.jsp?hide=true&term=1999&subjectCode=INFO&courseCode=43921)

  * [1981–1982] First Reported Computer Viruses: At least three separate viruses, including Elk Cloner, were discovered in games for the Apple II computer system, although the word virus wasn’t applied to this malicious code.
  * [1986] First PC Virus: The so-called Brain virus infected Microsoft DOS systems.
  * [1988] Morris Internet Worm: Robert Morris Jr. wrote the “Internet worm” in 1988 at Cornell University 
    * Exploited multiple vulnerabilities to spread from machine to machine
    * Generated huge traffic and completely clogged the Internet
    * On the positive side: Exposed the vulnerability of the network designed to be resilient against such attacks (including a nuclear strike)
    * The “Morris Worm” opened the virus and worm flood gate for more deadly viruses and worms: Melissa, CIH Chernobyl, Worm.ExploreZip, BubbleBoy, The Love Bug.
  * [1990] First Polymorphic Viruses: To evade antivirus systems, these viruses altered their own appearance every time they ran.
  * [1991] Virus Construction Set (VCS) - This tool hit the bulletin board system community and gave aspiring virus writers a simple toolkit to create their own customized malicious code.
  * [1994] Good Times Virus Hoax: This virus didn’t infect computers. Instead, it was entirely fictional. However, concern about this virus spread from human to human via word of mouth as frightened people warned others about impending doom from this totally bogus malicious code scam.
  * [1995] First Macro Viruses implemented in Microsoft Word macro languages, infecting document files.
  * [1996] Netcat released for UNIX: This tool written by Hobbit remains the most popular backdoor for UNIX systems to this day. Although it has legitimate uses, Netcat is often abused as a backdoor.
  * [1998] First Java Virus: The _**StrangeBrew**_ virus infected other Java programs, bringing virus concerns into the realm of Web-based applications.
  * [1998] Netcat released for Windows: Written by Weld Pond, it is used as popular backdoor on Windows systems.
  * [1998] Back Orifice: This tool released by Cult of the Dead Cow (cDc), a hacking group, allowed for remote control of Windows systems across the network.
  * [1999] The Melissa Virus/Worm: Microsoft Word macro virus infected  
thousands of computer systems around the globe by spreading through e-mail. It was both a virus and a worm in that it infected a document file, and propagated via the network.
  * [1999] Back Orifice 2000 (BO2K): Version of Back Orifice for remote control of a Windows system.
  * [1999] Distributed Denial of Service Agents: The Tribe Flood Network (TFN) and Trin00 denial of service agents. These tools offered an attacker control of dozens, hundreds, or even thousands of machines with an installed zombie via a single client machine. With a centralized point of coordination, these distributed agents could launch a devastating flood or other attack.
  * [1999] Knark Kernel-Level RootKit: Someone called Creed released this tool built on earlier ideas for kernel manipulation on Linux systems. Knark included a complete toolkit for tweaking the Linux kernel so an attacker could very effectively hide files, processes, and network activity.
  * [2000] Love Bug: VBScript worm that shut down tens of thousands of systems as it spread via several MS Outlook weaknesses.
  * [2001] Code Red Worm: This worm spread via a buffer overflow in Microsoft’s IIS Web server product. Over 250,000 machines were infected in less than eight hours.
  * [2001] Kernel Intrusion System: This tool by Optyx simplified the manipulation of Linux kernels by including GUI and effective hiding mechanisms.
  * [2001] Nimda Worm: This extremely virulent worm included numerous methods for infecting Windows machines, including Web server buffer overflows, Web browser exploits, Outlook e-mail attacks, and file sharing.
  * [2002] Setiri Backdoor: Although never formally released, this Trojan horse tool has the ability to bypass personal firewalls, network firewalls, and Network Address Translation devices by co-opting as an invisible browser.
  * [2003] SQL Slammer Worm: In January 2003, this worm spread rapidly, disabling several Internet service providers in South Korea and briefly causing problems throughout the world
  * [2003] Hydan Executable Steganography Tool: In February, this tool offered its users the ability to hide data inside of executables using polymorphic coding techniques on Linux, BSD, and Windows executables. These concepts could also be extended for antivirus and intrusion detection system evasion.
  * [2005] Koobface: Malware that, after infecting a user’s PC, would attack their social media accounts like Facebook, MySpace and Twitter.
  * [2008] Conflicker: MS Windows targeting worm. Used bruteforce attacks on admin passwords to gain access and add infected nodes to a botnet.
  * [2010] Stuxnet: A worm targeted at Iran’s nuclear program. Believed to have been created by a large team of developers working for a nation state or group of them. Notable as it infected an air gapped system and only targeted specific types of industrial hardware.
  * [2007-2011] Zeus Trojan: Notable since the source code was released in 2011, allowing other authors to incorporate it. It has become the backbone of many different botnet malware and banking trojan campaigns.
  * [2013] Cryptolocker: Probably the first widespread successful example of ransomware.
  * [2014] Backoff: Malware designed to target Point of Sale systems in retail and other customer-facing scenarios.
  * [2016] Cerber: A particularly successful breed of ransomware.
  * [2017] Wannacry: A combination of existing malicious software including the leaked NSA exploit Eternal Blue, modified Zeus code and ransomware payload. This wormable malware spread quickly and managed to infect a significant number of computers including the majority of the UK’s hospital systems.
