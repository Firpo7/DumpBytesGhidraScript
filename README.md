# DumpBytes Script

A Ghidra script that allows you to dump bytes in different formats, from a loaded binary in Ghidra.

The available formats are: HexString, String, Base64, JavaScript buffer, Yara, Python list and C arrays of bytes, word, dword or qword.

## Installation
Copy the script in folder `$HOME/ghidra_scripts`, then open the _Script Manager_ and check the _"In Tool"_ checkbox to enable the shortcut.

## Usage
Select a portion of code or a bunch of bytes from Ghidra then press _alt-p_, if you enabled the shortcut. Otherwise run it from the _Script Manager_. The result will be printed in the _Console_ of Ghidra.