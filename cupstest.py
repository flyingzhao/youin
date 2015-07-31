import cups

cups.setServer('121.248.53.183')
cups.setPort(631)
# conn = cups.Connection()
# print cups.getServer(),cups.getPort()
# conn.printFile('xerox','123.pdf','test',{})
# printers = conn.getPrinters ()

# for printer in printers:
# 	print printer, printers[printer]["device-uri"]
conn = cups.Connection()
printers = conn.getPrinters()
printer_name = printers.keys()[0]
print printer_name
conn.printFile(printer_name, '123.pdf', "Photo Booth",{'media':'A4','page-ranges':'7-8','sides':'two-sided-short-edge'})

#conn.printFile(printer_name, BPicture, "Photo Booth",{"copies": "2"})

