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
conn.printFile(printer_name, '1234.pdf', "Photo Booth",{'page-ranges':'3-4','sides':'two-sided-long-edges'})

#conn.printFile(printer_name, BPicture, "Photo Booth",{"copies": "2"})

