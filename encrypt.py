#Name:Moosa Shehzad Abbasi
#UID: U37033529
#Brief Description Of Program: Encrypt.py




# Encrypt_Code dictionary

Encrypt_Code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\

'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\

'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\

'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\

'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\

'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\

'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\

'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\

'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\

'@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\

'%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\

'*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\

':':',',',':':','?':'.','.':'?','<':'>','>':'<',\

"'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\

'{':'[','[':'{','}':']',']':'}'}

 

# Function to encrypt the file

def encrypt_file_content(content):

    encrypted_content = ""

    for char in content:

        if char.isspace():

            encrypted_content += char

        else:

            encrypted_content += Encrypt_Code[char]

    return encrypted_content

 

# Prompt the user for the name of a text file

input_file_name = input("Enter the name of the input text file: ")

 

try:

    with open(input_file_name, 'r') as input_file:

        content = input_file.read()

        encrypted_content = encrypt_file_content(content)

 

    output_file_name = input("Enter the name of the output text file: ")

 

    with open(output_file_name, 'w') as output_file:

        output_file.write(encrypted_content)

 

    print("File has been successfully encrypted and written to", output_file_name)

 

except FileNotFoundError:

    print("File not found. Please enter a valid file name.")

except Exception as e:

    print("An error occurred:", e)

















