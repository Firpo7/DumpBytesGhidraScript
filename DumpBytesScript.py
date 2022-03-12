#Dump bytes as C arrays, Python lists or other formats (only Little Endian)
#@author Tiziano Firpo
#@category Firpo Tesi
#@keybinding alt p
#@menupath 
#@toolbar 

def parseBytes(listing, start, end, format_str, split = True):
    output = ''
    count = 0
    while True:
        bytes_data = listing.getCodeUnitAt(start).getBytes()
        for b in bytes_data:
            if split and count % 16 == 0:
                output += '\n    '
    
            if (256 + b) < 256:
                b += 256
    
            output += format_str % b
            count += 1
        
        if listing.getCodeUnitAt(start).getMaxAddress() >= end:
            break
        
        start = listing.getCodeUnitAt(start).getMaxAddress().add(1)
    
    return output

def parseAsCArray(name, start, end, size):
    # C array
    listing = currentProgram.getListing()    
    output = ('unsigned char %s[%d] = {' % (name, size)) + parseBytes(listing, start, end, '0x%02X, ')[:-2] + '\n};'
    
    print output

def parseAsCArrayWord(name, start, end, size):
    array_size = (size + 1) / 2

    # C array (WORD)
    output = "unsigned short %s[%d] = {" % (name, array_size)
    listing = currentProgram.getListing()
    hex_string = parseBytes(listing, start, end, '%02X', split = False) + '00' # zero padding
    
    for i in range(0, size*2, 4):
        if i % 64 == 0:
            output += "\n    "
        # little endian
        output += "0x" 
        output += hex_string[i+2:i+4]
        output += hex_string[i:i+2]
        output += ', '
    output = output[:-2] + "\n};"
    print output

def parseAsCArrayDword(name, start, end, size):
    array_size = (size + 3) / 4

    # C array (DWORD)
    output = "unsigned int %s[%d] = {" % (name, array_size)
    listing = currentProgram.getListing()
    hex_string = parseBytes(listing, start, end, '%02X', split = False) + '00'*3 # zero padding

    for i in range(0, size*2, 8):
        if i % 64 == 0:
            output += "\n    "
        # little endian
        output += "0x" 
        output += hex_string[i+6:i+8]
        output += hex_string[i+4:i+6]
        output += hex_string[i+2:i+4]
        output += hex_string[i:i+2]
        output += ', '
    output = output[:-2] + "\n};"
    print output

def parseAsCArrayQword(name, start, end, size):
    array_size = (size + 7) / 8

    # C array (QWORD)
    output = "unsigned long %s[%d] = {" % (name, array_size)
    listing = currentProgram.getListing()
    hex_string = parseBytes(listing, start, end, '%02X', split = False) + '00' * 7 # zero padding
    
    for i in range(0, size*2, 16):
        if i % 64 == 0:
            output += "\n    "
        # little endian
        output += "0x" 
        output += hex_string[i+14:i+16]
        output += hex_string[i+12:i+14]
        output += hex_string[i+10:i+12]
        output += hex_string[i+8:i+10]
        output += hex_string[i+6:i+8]
        output += hex_string[i+4:i+6]
        output += hex_string[i+2:i+4]
        output += hex_string[i:i+2]
        output += ', '
    output = output[:-2] + "\n};"
    print output

def parseAsString(start, end):
    listing = currentProgram.getListing()    
    print '"' + parseBytes(listing, start, end, "\\x%02x", split = False)  + '"'

def parseAsHexString(start, end):
    listing = currentProgram.getListing()
    print parseBytes(listing, start, end, "%02X", split = False)

def parseAsPythonList(name, start, end):
    # Python list
    listing = currentProgram.getListing()
    output = ('%s = [' % name) + parseBytes(listing, start, end, '0x%02X, ')[:-2] + '\n]'

    print output

def parseAsPythonListWord(name, start, end):
    array_size = (size + 1) / 2

    # Python List (WORD)
    output = '%s = [' % name
    listing = currentProgram.getListing()
    hex_string = parseBytes(listing, start, end, '%02X', split = False) + '00' # zero padding
    
    for i in range(0, size*2, 4):
        if i % 64 == 0:
            output += "\n    "
        # little endian
        output += "0x" 
        output += hex_string[i+2:i+4]
        output += hex_string[i:i+2]
        output += ', '
    output = output[:-2] + '\n]'
    print output

def parseAsPythonListDword(name, start, end):
    array_size = (size + 3) / 4

    # Python List (DWORD)
    output = '%s = [' % name
    listing = currentProgram.getListing()
    hex_string = parseBytes(listing, start, end, '%02X', split = False) + '00'*3 # zero padding
    
    for i in range(0, size*2, 8):
        if i % 64 == 0:
            output += "\n    "
        # little endian
        output += "0x" 
        output += hex_string[i+6:i+8]
        output += hex_string[i+4:i+6]
        output += hex_string[i+2:i+4]
        output += hex_string[i:i+2]
        output += ', '
    output = output[:-2] + '\n]'
    print output

def parseAsPythonListQword(name, start, end):
    array_size = (size + 7) / 8

    # Python List(QWORD)
    output = '%s = [' % name
    listing = currentProgram.getListing()
    hex_string = parseBytes(listing, start, end, '%02X', split = False) + '00'*7 # zero padding
    
    for i in range(0, size*2, 16):
        if i % 64 == 0:
            output += "\n    "
        # little endian
        output += "0x" 
        output += hex_string[i+14:i+16]
        output += hex_string[i+12:i+14]
        output += hex_string[i+10:i+12]
        output += hex_string[i+8:i+10]
        output += hex_string[i+6:i+8]
        output += hex_string[i+4:i+6]
        output += hex_string[i+2:i+4]
        output += hex_string[i:i+2]
        output += ', '
    output = output[:-2] + '\n]'
    print output

def parseAsBase64(start, end):
    import base64
    listing = currentProgram.getListing()    
    bytes_data = parseBytes(listing, start, end, '%c', split = False)
    b64 = base64.b64encode(bytes_data)
    print b64    
    
def parseAsJavascript(name, start, end):
    import base64
    listing = currentProgram.getListing()    
    bytes_data = parseBytes(listing, start, end, '%c', split = False)
    b64 = base64.b64encode(bytes_data)       
    
    output = ('var %s = new Buffer("' % name) + b64 + '", \'base64\');'
    print output

def parseAsYara(name, start, end):
    listing = currentProgram.getListing()
    output = ('$%s = { ' % name) + parseBytes(listing, start, end, '%02x ') + '}'
    print output
    

if currentSelection is None:
    print 'Error: No selection found, please select something on Listing View...'
    import sys
    sys.exit(1)

start = currentSelection.getMinAddress()
end = currentSelection.getMaxAddress()
size = end.offset - start.offset + 1
print '\n[+] Dump 0x%X - 0x%X (%u bytes) :' % (start.offset, end.offset, size)

listing = currentProgram.getListing()
name = listing.getCodeUnitAt(start).getPrimarySymbol()
if name is None:
    name = 'data'

choice = askChoice("Choose the parsing type", "Choices: ", ["String", "Hex String", "C array", "C array Word", "C array Dword", "C array Qword", "Python List", "Python List Word", "Python List Dword", "Python List Qword", "Base64", "Javascript", "Yara"], "String")

print '\n'
if choice == "C array": parseAsCArray(name, start, end, size)
elif choice == "C array Word": parseAsCArrayWord(name, start, end, size)
elif choice == "C array Dword": parseAsCArrayDword(name, start, end, size)
elif choice == "C array Qword": parseAsCArrayQword(name, start, end, size)
elif choice == "String": parseAsString(start, end)
elif choice == "Hex String": parseAsHexString(start, end)
elif choice == "Python List": parseAsPythonList(name, start, end)
elif choice == "Python List Word": parseAsPythonListWord(name, start, end)
elif choice == "Python List Dword": parseAsPythonListDword(name, start, end)
elif choice == "Python List Qword": parseAsPythonListQword(name, start, end)
elif choice == "Base64": parseAsBase64(start, end)
elif choice == "Javascript": parseAsJavascript(name, start, end)
elif choice == "Yara": parseAsYara(name, start, end)
print '\n'