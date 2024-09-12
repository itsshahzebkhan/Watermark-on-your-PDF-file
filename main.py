# step 1 - install Pycharm community edition from Google Chrome
# step 2 - before writing the code, you have to install a package from Python library
# step 3 - open terminal on your Pycharm app and write this thing in it and then press enter -
# pip3 install aspose-pdf
# now start coding

import aspose.pdf as ap

document = ap.Document("name of your pdf file.pdf")

stamp = ap.TextStamp("watermark that you want to put")

stamp.x_indent = 250
stamp.y_indent = 400
stamp.height = 60
stamp.width = 100
stamp.background = True

stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
stamp.text_state.font_size = 100
stamp.text_state.font_style = ap.text.FontStyles.ITALIC
stamp.text_state.foreground_color = ap.Color.red
stamp.opacity = 30

stamp.set_stamp_id(123456)

document.pages[1].add_stamp(stamp)

document.save("Watermark.pdf")

# note - after completing the code, open terminal on your Pycharm app and type "py main.py" I am writing this since it is the name of my file, you can write the name of your own file and press enter, after the process is completed, a new .pdf file will be displayed near your main file