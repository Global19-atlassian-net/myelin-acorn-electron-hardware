lines = """B2
GND
GND
GND
GND
GND
B15
GND
GND
GND
GND
GND
C3
GND
GND
GND
GND
GND
C14
GND
GND
GND
GND
GND
D4
GND
GND
GND
GND
GND
D13
GND
GND
GND
GND
GND
E5
GND
GND
GND
GND
GND
E12
GND
GND
GND
GND
GND
F6
GND
GND
GND
GND
GND
F11
GND
GND
GND
GND
GND
H8
GND
GND
GND
GND
GND
H9
GND
GND
GND
GND
GND
J8
GND
GND
GND
GND
GND
J9
GND
GND
GND
GND
GND
L6
GND
GND
GND
GND
GND
L11
GND
GND
GND
GND
GND
M5
GND
GND
GND
GND
GND
M12
GND
GND
GND
GND
GND
N4
GND
GND
GND
GND
GND
N13
GND
GND
GND
GND
GND
P3
GND
GND
GND
GND
GND
P14
GND
GND
GND
GND
GND
R2
GND
GND
GND
GND
GND
R15
GND
GND
GND
GND
GND
A1
VCC
VCC
VCC
VCC
VCC
A16
VCC
VCC
VCC
VCC
VCC
G7
VCC
VCC
VCC
VCC
VCC
G10
VCC
VCC
VCC
VCC
VCC
K7
VCC
VCC
VCC
VCC
VCC
K10
VCC
VCC
VCC
VCC
VCC
T1
VCC
VCC
VCC
VCC
VCC
T16
VCC
VCC
VCC
VCC
VCC
D5
VCCIO0
VCCIO0
VCCIO0
VCCIO0
VCCIO0
D12
VCCIO0
VCCIO0
VCCIO0
VCCIO0
VCCIO0
G8
VCCIO0
VCCIO0
VCCIO0
VCCIO0
VCCIO0
G9
VCCIO0
VCCIO0
VCCIO0
VCCIO0
VCCIO0
E13
VCCIO1
VCCIO1
VCCIO1
VCCIO1
VCCIO1
H10
VCCIO1
VCCIO1
VCCIO1
VCCIO1
VCCIO1
J10
VCCIO1
VCCIO1
VCCIO1
VCCIO1
VCCIO1
M13
VCCIO1
VCCIO1
VCCIO1
VCCIO1
VCCIO1
K8
VCCIO2
VCCIO2
VCCIO2
VCCIO2
VCCIO2
K9
VCCIO2
VCCIO2
VCCIO2
VCCIO2
VCCIO2
N5
VCCIO2
VCCIO2
VCCIO2
VCCIO2
VCCIO2
N12
VCCIO2
VCCIO2
VCCIO2
VCCIO2
VCCIO2
M4
VCCIO3
VCCIO3
VCCIO3
VCCIO3
VCCIO3
H7
VCCIO4
VCCIO4
VCCIO4
VCCIO4
VCCIO4
J7
VCCIO4
VCCIO4
VCCIO4
VCCIO4
VCCIO4
E4
VCCIO5
VCCIO5
VCCIO5
VCCIO5
VCCIO5
A2
NC
NC
NC
NC
NC""".split()

for i in range(len(lines) / 6):
	ball = lines[i*6]
	label = lines[i*6+1]
	for x in range(i*6+1, i*6+6):
		assert lines[x] == label
	print 'Pin("%s", "%s", "%s"),' % (
		ball,
		label,
		'' if label == 'NC' else 'GND' if label == 'GND' else '3V3'
	)
	