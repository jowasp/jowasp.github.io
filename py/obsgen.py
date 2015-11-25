import binascii
def encode(f):
	arr = ''
	data = ''
	eval = ''
	val = 'val'
	n = 0
	m = 1
	for line in f:
		arr += binascii.b2a_hex(str(line)) + '_'
	arr = arr.rsplit('_')[:-1]
	for hex in arr:
		n+=1
		data += str(val) + str(n) + ' = "' + str(hex) + '";\n'
	while(m<=n):
		eval += str(val) + str(m) + '+'
		m+=1
	f = '''
%s

function hex2str(hexx) {
    var hex = hexx.toString();
    var str = '';
    for (var i = 0; i < hex.length; i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}
data = %s;
eval(hex2str(data));'''%(data,eval[:-1])
	return f
	
f = open('good.js')	
min = 0
max = 2
while(min<max):
	f = encode(f)
	min += 1
fw = open('encode.js','w')
fw.write(f)
fw.close()
