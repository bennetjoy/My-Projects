import pdfkit

def topdf():
    print("Enter 1 to convert HTML file to PDF")
    print("Enter 2 to convert webpage to PDF")
    print("Enter 3 to convert text to PDF")
    print("Press any other key to exit.")
    opt = input()
    if opt==1:
        pdfkit.from_file('test.html', 'out.pdf')
    elif opt==2:
        pdfkit.from_url('https://www.google.co.in/','shaurya.pdf')
    elif opt==3:
        pdfkit.from_string('Shaurya GFG','GfG.pdf')
    else:
        exit()

topdf()