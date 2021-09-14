## SMTP

# Sending email using telnet/nc

```
$ telnet / nc <ip address> <port>
helo example.com
mail from: example@example.com
rcpt to: person1@localhost, person2@localhost
data
Subject: This is a test

This is a test.
.
quit
```

# sending email using sendemail

```
$ sendemail -f '<rcpt>' -t '<sender>' -s <smtp server 127.0.0.1:25> -u '<subject>' -m '<message>' -a <attachment>
```