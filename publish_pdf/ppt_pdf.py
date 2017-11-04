# Got the main idea from 
# http://odetocode.com/blogs/scott/archive/2013/06/26/convert-a-directory-of-powerpoint-slides-to-pdf-with-python.aspx

# PS Note I have not pushed the ppts folder
# please create a folder called source_ppts which contains the ppt files
import sys  
import os 
import glob  
import win32com.client   

# folder containing the ppts
ppt_src = 'source_ppts'

# dir where pdf is getting saved
output_folder = 'output_pdfs'


output_dir = os.path.join(os.path.abspath(os.getcwd()), 'output_pdfs')

# create the pdf dir if it doesn't exists
if ~os.path.isdir(output_dir):
    os.makedirs(output_dir)

def convert_ppt_to_pdfs(folder, formatType = 32):
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    powerpoint.Visible = 1

    # get only ppt files from the dir
    for filename in glob.glob(os.path.join(ppt_src, "*.ppt*")):
        ppt_file = os.path.join(os.getcwd(), filename)
        deck = powerpoint.Presentations.Open(ppt_file) 
        newname = os.path.splitext(os.path.basename(filename))[0] + ".pdf"
        newname = os.path.join(output_dir, newname)
        deck.SaveAs(newname, formatType)  
        deck.Close() 
    powerpoint.Quit()

convert_ppt_to_pdfs("ppts")


