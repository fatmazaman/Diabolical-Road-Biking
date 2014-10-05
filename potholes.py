import csv

potholes_by_block = { }

def make_block(address):

	parts = address.split()
	parts[0] = parts[0][:-3] + 'XXXX'
	return ' '.join(parts)


f = open('potholes.csv')
for row in csv.DictReader(f):
    status = row['STATUS']  
    if status == 'open':
    	address = row ['STREET ADDRESS']
        block = make_block(address)
        if block not in potholes_by_block:
	        potholes_by_block[block] = 1
        else:
            potholes_by_block[block] += 1	