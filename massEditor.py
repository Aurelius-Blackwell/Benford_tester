import os

source_folder = 'F:/YOUR SOURCE FOLDER HERE/'
destination_folder = 'F:/YOUR TARGET FOLDER HERE/'

p = os.listdir(source_folder)

for file in p:
    filex = open(source_folder+file, 'r', encoding="utf-8")
    text = filex.read()
    text = text.replace(',', '') #remove commas
    text = text.replace('.', '') #remove periods
    destination = destination_folder+file #no punctuation
    with open(destination, 'w', encoding="utf-8") as new_file:
        new_file.write(text)
