#!d:\python34\python

import time
from datetime import datetime

t = datetime.now();
print(t.hour);
h = t.hour+4;print(h)
hm = h%8
print(hm)

p10 =0;p20=0;p30=0;p40=0;p50=0;p60=0;p70=0;p80=0
if hm >= 4 :
	p10 = 1
	hm = hm - 4
print("p10: " + str(p10))

if hm >= 2 :
	p20 = 1
	hm = hm - 2
print("p20: " + str(p20))

if hm >= 1 :
	p30 = 1
print("p30: " + str(p30))

m=t.minute;print(m)

if m >= 30 :
	p40 = 1
	m = m - 30
print("p40: " + str(p40))

if m >= 15 :
	p50 = 1
	m = m - 15
print("p50: " + str(p50))

if m >= 8 :
	p60 = 1
	m = m - 8
print("p60: " + str(p60))

if m >= 4 :
	p70 = 1
	m = m - 4
print("p70: " + str(p70))

if m >= 2 :
	p80 = 1
print("p80: " + str(p80))

while 1:
	print("Hello World!");

	h=datetime.now().strftime('%Y-%m-%d %H:%M:%S');
	print(h);
	print(str(datetime.now()));

	print("Hello World!2");
	t = datetime.now();
	print(t.hour);
	h = t.hour+4;print(h)
	hm = h%8
	print(hm)

	p1 =0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0
	if hm >= 4 :
		p1 = 1
		hm = hm - 4
		if p10 != 1 :
			p10 = 1
			print("p10 Changed to 1")
	else :
		if p10 != 0 :
			p10 = 0
			print("p10 Changed to 0")
	print("p1: " + str(p1))

	if hm >= 2 :
		p2 = 1
		hm = hm - 2
		if p20 != 1 :
			p20 = 1
			print("p20 Changed to 1")
	else :
		if p20 != 0 :
			p20 = 0
			print("p20 Changed to 0")
	print("p2: " + str(p2))

	if hm >= 1 :
		p3 = 1
		if p30 != 1 :
			p30 = 1
			print("p30 Changed to 1")
	else :
		if p30 != 0 :
			p30 = 0
			print("p30 Changed to 0")
	print("p3: " + str(p3))

	m=t.minute;print(m)

	if m >= 30 :
		p4 = 1
		m = m - 30
		if p40 != 1 :
			p40 = 1
			print("p40 Changed to 1")
	else :
		if p40 != 0 :
			p40 = 0
			print("p40 Changed to 0")
	print("p4: " + str(p4))
	
	if m >= 15 :
		p5 = 1
		m = m - 15
		if p50 != 1 :
			p50 = 1
			print("p50 Changed to 1")
	else :
		if p50 != 0 :
			p50 = 0
			print("p50 Changed to 0")		
	print("p5: " + str(p5))

	if m >= 8 :
		p6 = 1
		m = m - 8
		if p60 != 1 :
			p60 = 1
			print("p60 Changed to 1")
	else :
		if p60 != 0 :
			p60 = 0
			print("p60 Changed to 0")
	print("p6: " + str(p6))

	if m >= 4 :
		p7 = 1
		m = m - 4
		if p70 != 1 :
			p70 = 1
			print("p70 Changed to 1")
	else :
		if p70 != 0 :
			p70 = 0
			print("p70 Changed to 0")
	print("p7: " + str(p7))

	if m >= 2 :
		p8 = 1
		if p80 != 1 :
			p80 = 1
			print("p80 Changed to 1")
	else :
		if p80 != 0 :
			p80 = 0
			print("p80 Changed to 0")
	print("p8: " + str(p8))

	
	time.sleep(5)	
