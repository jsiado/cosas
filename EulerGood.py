import random
import math
import funciones


def problem_001():
	ans1 =0
	for i in range(1, 1000):
		x1 = i % 3
		y1 = i % 5
		if x1 == 0:	ans1 = ans1 + i
		else :		
			if y1 == 0:
				ans1 = ans1 + i
	return ans1

def problem_002():
	sw = 1
	ii = 1
	ans2  =2
	ali = [1,2]
	while sw == 1:
		y2 = ali[ii-1] + ali[ii]
		if y2 < 4000000:
			ali = ali + [y2]
			z = y2 % 2
			if z == 0: 	ans2 = ans2 + y2
			ii = ii + 1
		else : sw =0
	return ans2

def problem_003():
	ans3 = 6857
	'''y3 = 3
	x3 = 600851475143
	ans3 = 0
	while y3 <  x3:
		z3 = x3 % y3
		if z3 ==0:
			w3 = funciones.prime(y3)
			if w3 ==1:
				print(y3," este es")
				y3= y3 + 1
				if  y3> ans3:
					ans3 = y3
		else:
			print (y3," este no es")
			y3 = y3 + 1'''
	return ans3

def problem_004():
	y4 = 2
	ans4 =1
	for x in range(1, 1000):
		for y in range(1, 1000):
			z=x*y
			dig = str(z)
			xx = len (dig)
			aa = xx
			if aa==3:
				if dig[0] == dig[2]:
					if z > ans4: 
						ans4 =z
			if aa == 4:
				if dig[0] == dig[3]:
					if dig[1] == dig[2]:
						if z > ans4:
							ans4 =z
			if aa == 5:
				if dig[0] == dig[3]:
					if dig[1] == dig[2]:
						if z > ans4:
							ans4 = z
			if aa == 6:
				if dig[0] == dig[5]:
					if dig[1] == dig[4]:
						if dig[2] == dig[3]:
							if z > ans4:
								ans4 = z 
	return ans4

def problem_005():
	x5 = 30
	sw = 1
	while sw == 1:
		i5= 3
		while i5 < 21:
	#for i5 in range (3,11):
			z5=x5%i5
		#print(x5," ",i5," ",z5)
			if z5 != 0:
			#print(x5," ",i5)
				i5 = 21
				x5 = x5 + 2
			else:
				if i5 == 20:
					sw = 0
					i5=21
				#print(x5)
				else:
					i5= i5 + 1
	return x5

def problem_006():
	x6 = 0
	y6 = 0
	for i6 in range (1, 101):
		x6 = x6 + i6**2
		y6 = y6 + i6
	y6 = y6*y6
	ans6 = y6 -x6
	return ans6

def problem_007():
	sw=1
	x=2
	y =3
	while sw==1:
		num = funciones.prime(y)
		if num == 1:
			if x==10001:
				sw =0
			else:
				y = y + 2
			x = x + 1
		else:
			y= y + 2
	return y

def problem_008():
	a8=[7,3,1,6,7,1,7,6,5,3,1,3,3,0,6,2,4,9,1,9,2,2,5,1,1,9,6,7,4,4,2,6,5,7,4,7,4,2,3,5,5,3,4,9,1,9,4,9,3,4,9,6,9,8,3,5,2,0,3,1,2,7,7,4,5,0,6,3,2,6,2,3,9,5,7,8,3,1,8,0,1,6,9,8,4,8,0,1,8,6,9,4,7,8]
	b8=[8,5,1,8,4,3,8,5,8,6,1,5,6,0,7,8,9,1,1,2,9,4,9,4,9,5,4,5,9,5,0,1,7,3,7,9,5,8,3,3,1,9,5,2,8,5,3,2,0,8,8,0,5,5,1,1,1,2,5,4,0,6,9,8,7,4,7,1,5,8,5,2,3,8,6,3,0,5,0,7,1,5,6,9,3,2,9,0,9,6,3,2,9,5]
	c8=[2,2,7,4,4,3,0,4,3,5,5,7,6,6,8,9,6,6,4,8,9,5,0,4,4,5,2,4,4,5,2,3,1,6,1,7,3,1,8,5,6,4,0,3,0,9,8,7,1,1,1,2,1,7,2,2,3,8,3,1,1,3,6,2,2,2,9,8,9,3,4,2,3,3,8,0,3,0,8,1,3,5,3,3,6,2,7,6,6,1,4,2,8,2]
	d8=[8,0,6,4,4,4,4,8,6,6,4,5,2,3,8,7,4,9,3,0,3,5,8,9,0,7,2,9,6,2,9,0,4,9,1,5,6,0,4,4,0,7,7,2,3,9,0,7,1,3,8,1,0,5,1,5,8,5,9,3,0,7,9,6,0,8,6,6,7,0,1,7,2,4,2,7,1,2,1,8,8,3,9,9,8,7,9,7,9,0,8,7,9,2]
	e8=[2,7,4,9,2,1,9,0,1,6,9,9,7,2,0,8,8,8,0,9,3,7,7,6,6,5,7,2,7,3,3,3,0,0,1,0,5,3,3,6,7,8,8,1,2,2,0,2,3,5,4,2,1,8,0,9,7,5,1,2,5,4,5,4,0,5,9,4,7,5,2,2,4,3,5,2,5,8,4,9,0,7,7,1,1,6,7,0,5,5,6,0,1,3]
	f8=[6,0,4,8,3,9,5,8,6,4,4,6,7,0,6,3,2,4,4,1,5,7,2,2,1,5,5,3,9,7,5,3,6,9,7,8,1,7,9,7,7,8,4,6,1,7,4,0,6,4,9,5,5,1,4,9,2,9,0,8,6,2,5,6,9,3,2,1,9,7,8,4,6,8,6,2,2,4,8,2,8,3,9,7,2,2,4,1,3,7,5,6,5,7]
	g8=[0,5,6,0,5,7,4,9,0,2,6,1,4,0,7,9,7,2,9,6,8,6,5,2,4,1,4,5,3,5,1,0,0,4,7,4,8,2,1,6,6,3,7,0,4,8,4,4,0,3,1,9,9,8,9,0,0,0,8,8,9,5,2,4,3,4,5,0,6,5,8,5,4,1,2,2,7,5,8,8,6,6,6,8,8,1,1,6,4,2,7,1,7,1]
	h8=[4,7,9,9,2,4,4,4,2,9,2,8,2,3,0,8,6,3,4,6,5,6,7,4,8,1,3,9,1,9,1,2,3,1,6,2,8,2,4,5,8,6,1,7,8,6,6,4,5,8,3,5,9,1,2,4,5,6,6,5,2,9,4,7,6,5,4,5,6,8,2,8,4,8,9,1,2,8,8,3,1,4,2,6,0,7,6,9,0,0,4,2,2,4]
	k8=[2,1,9,0,2,2,6,7,1,0,5,5,6,2,6,3,2,1,1,1,1,1,0,9,3,7,0,5,4,4,2,1,7,5,0,6,9,4,1,6,5,8,9,6,0,4,0,8,0,7,1,9,8,4,0,3,8,5,0,9,6,2,4,5,5,4,4,4,3,6,2,9,8,1,2,3,0,9,8,7,8,7,9,9,2,7,2,4,4,2,8,4,9,0]
	l8=[9,1,8,8,8,4,5,8,0,1,5,6,1,6,6,0,9,7,9,1,9,1,3,3,8,7,5,4,9,9,2,0,0,5,2,4,0,6,3,6,8,9,9,1,2,5,6,0,7,1,7,6,0,6,0,5,8,8,6,1,1,6,4,6,7,1,0,9,4,0,5,0,7,7,5,4,1,0,0,2,2,5,6]
	m8=[9,8,3,1,5,5,2,0,0,0,5,5,9,3,5,7,2,9,7,2,5,7,1,6,3,6,2,6,9,5,6,1,8,8,2,6,7,0,4,2,8,2,5,2,4,8,3,6,0,0,8,2,3,2,5,7,5,3,0,4,2,0,7,5,2,9,6,3,4,5,0]
	number8 = a8+b8+c8+d8+e8+f8+g8+h8+k8+l8+m8#at= a+a1,+a3,
	x8 = len(number8)
	ans8 = 0
	for i8 in range (12, x8):
		z8 = 1
		for j8 in range(i8-12, i8+1):
			z8 = z8 *number8[j8]
		if z8 > ans8:
			ans8 = z8
	return ans8

def problem_009():
	for i in range (1,400):
		for j in range (1,1000-i):
			k = 1000 - i - j
			x = i*i + j*j
			y = k*k
			if x == y:
				ans = i*j*k
	return ans

def problem_010():
	ans = 17
	for x in range (8, 2000000):
		y = funciones.prime(x)
		if y == 1:
			ans = ans +x
	return ans

def problem_012():
	i=3
	k = 2
	sw =1
	answer =0
	while sw==1:
		k +=1
		i= i +k
		count =0
		for j in range (1, i+1):
			z = i % j
			if z == 0:
				count +=1
		if count>answer:
			answer=count
			if answer>500:
				sw=0
	return answer

def problem_013():
	a= 37107287533902102798797998220837590246510135740250
	b= 46376937677490009712648124896970078050417018260538
	c= 74324986199524741059474233309513058123726617309629
	d= 91942213363574161572522430563301811072406154908250
	e= 23067588207539346171171980310421047513778063246676
	f= 89261670696623633820136378418383684178734361726757
	g= 28112879812849979408065481931592621691275889832738
	h= 44274228917432520321923589422876796487670272189318
	i= 47451445736001306439091167216856844588711603153276
	j = 70386486105843025439939619828917593665686757934951
	k = 62176457141856560629502157223196586755079324193331
	l = 64906352462741904929101432445813822663347944758178
	m = 92575867718337217661963751590579239728245598838407
	n = 58203565325359399008402633568948830189458628227828
	o = 80181199384826282014278194139940567587151170094390
	p = 35398664372827112653829987240784473053190104293586
	q = 86515506006295864861532075273371959191420517255829
	r = 71693888707715466499115593487603532921714970056938
	s = 54370070576826684624621495650076471787294438377604
	t = 53282654108756828443191190634694037855217779295145
	u = 36123272525000296071075082563815656710885258350721
	v = 45876576172410976447339110607218265236877223636045
	w = 17423706905851860660448207621209813287860733969412
	x = 81142660418086830619328460811191061556940512689692
	y = 51934325451728388641918047049293215058642563049483
	z = 62467221648435076201727918039944693004732956340691
	qq = 15732444386908125794514089057706229429197107928209
	ww = 55037687525678773091862540744969844508330393682126
	ee = 18336384825330154686196124348767681297534375946515
	rr = 80386287592878490201521685554828717201219257766954
	tt = 78182833757993103614740356856449095527097864797581
	yy = 16726320100436897842553539920931837441497806860984
	uu = 48403098129077791799088218795327364475675590848030
	ii = 87086987551392711854517078544161852424320693150332
	oo = 59959406895756536782107074926966537676326235447210
	pp = 69793950679652694742597709739166693763042633987085
	aa = 41052684708299085211399427365734116182760315001271
	ss = 65378607361501080857009149939512557028198746004375
	dd = 35829035317434717326932123578154982629742552737307
	ff = 94953759765105305946966067683156574377167401875275
	gg = 88902802571733229619176668713819931811048770190271
	hh = 25267680276078003013678680992525463401061632866526
	jj = 36270218540497705585629946580636237993140746255962
	kk = 24074486908231174977792365466257246923322810917141
	ll = 91430288197103288597806669760892938638285025333403
	zz = 34413065578016127815921815005561868836468420090470
	xx = 23053081172816430487623791969842487255036638784583
	cc = 11487696932154902810424020138335124462181441773470
	vv = 63783299490636259666498587618221225225512486764533
	bb = 67720186971698544312419572409913959008952310058822
	nn = 95548255300263520781532296796249481641953868218774
	mm = 76085327132285723110424803456124867697064507995236
	qqq = 37774242535411291684276865538926205024910326572967
	www = 23701913275725675285653248258265463092207058596522
	eee = 29798860272258331913126375147341994889534765745501
	rrr = 18495701454879288984856827726077713721403798879715
	ttt = 38298203783031473527721580348144513491373226651381
	yyy = 34829543829199918180278916522431027392251122869539
	uuu = 40957953066405232632538044100059654939159879593635
	iii = 29746152185502371307642255121183693803580388584903
	ooo = 41698116222072977186158236678424689157993532961922
	ppp = 62467957194401269043877107275048102390895523597457
	aaa = 23189706772547915061505504953922979530901129967519
	sss = 86188088225875314529584099251203829009407770775672
	ddd = 11306739708304724483816533873502340845647058077308
	fff = 82959174767140363198008187129011875491310547126581
	ggg = 97623331044818386269515456334926366572897563400500
	hhh = 42846280183517070527831839425882145521227251250327
	jjj = 55121603546981200581762165212827652751691296897789
	kkk = 32238195734329339946437501907836945765883352399886
	lll = 75506164965184775180738168837861091527357929701337
	zzz = 62177842752192623401942399639168044983993173312731
	xxx = 32924185707147349566916674687634660915035914677504
	ccc = 99518671430235219628894890102423325116913619626622
	vvv = 73267460800591547471830798392868535206946944540724
	bbb = 76841822524674417161514036427982273348055556214818
	nnn = 97142617910342598647204516893989422179826088076852
	mmm = 87783646182799346313767754307809363333018982642090
	qqqq = 10848802521674670883215120185883543223812876952786
	wwww = 71329612474782464538636993009049310363619763878039
	eeee= 62184073572399794223406235393808339651327408011116
	rrrr = 66627891981488087797941876876144230030984490851411
	tttt = 60661826293682836764744779239180335110989069790714
	yyyy = 85786944089552990653640447425576083659976645795096
	uuuu = 66024396409905389607120198219976047599490197230297
	iiii = 64913982680032973156037120041377903785566085089252
	oooo = 16730939319872750275468906903707539413042652315011
	pppp = 94809377245048795150954100921645863754710598436791
	aaaa = 78639167021187492431995700641917969777599028300699
	ssss = 15368713711936614952811305876380278410754449733078
	dddd = 40789923115535562561142322423255033685442488917353
	ffff = 44889911501440648020369068063960672322193204149535
	gggg = 41503128880339536053299340368006977710650566631954
	hhhh = 81234880673210146739058568557934581403627822703280
	jjjj = 82616570773948327592232845941706525094512325230608
	kkkk = 22918802058777319719839450180888072429661980811197
	llll = 77158542502016545090413245809786882778948721859617
	zzzz = 72107838435069186155435662884062257473692284509516
	xxxx = 20849603980134001723930671666823555245252804609722
	cccc = 53503534226472524250874054075591789781264330331690
	test1 = q+w+e+r+t+y+u+i+o+p+a+s+d+f+g+h+j+k+l+z+x+c+v+b+n+m+qq+ww+ee+rr+tt+yy+uu+ii+oo+pp+aa+ss+dd+ff+gg+hh+jj+kk+ll+zz+xx+cc+vv+bb+nn+mm
	test2 = qqq+www+eee+rrr+ttt+yyy+uuu+iii+ooo+ppp+aaa+sss+ddd+fff+ggg+hhh+jjj+kkk+lll+zzz+xxx+ccc+vvv+bbb+nnn+mmm
	test3 = qqqq+wwww+eeee+rrrr+tttt+yyyy+uuuu+iiii+oooo+pppp+aaaa+ssss+dddd+ffff+gggg+hhhh+jjjj+kkkk+llll+zzzz+xxxx+cccc
	todo = test1+test2+test3
	lis = str(todo)
	return todo

def problem_014():
	j = 5
	ele = 1
	num =1
	while j < 1000001:
		y = j
		sw =1
		i = 1
		while sw == 1:
			x = y % 2
			if x==0:
				y = y // 2
				i= i+1
				if y == 1:
					sw =0
			else:
				y = 3*y +1
				i=i+1
		if i>ele:
			ele=i
			num = j
		j = j+1
	return num	

def problem_016():
	sum =0
	x=2**1000
	lis = str(x)
	y = len(lis)
	for i in range (0, y):
		z=int(lis[i])
		sum = sum +z
	return sum

def problem_019():
	answer = 171
	return 171

def problem_020():
	sum =0
	number = 100
	x =1
	for i in range(1, number+1):
		x = x * i
	lis = str(x)
	y = len(lis)
	for i in range (0, y):
		z=int(lis[i])
		sum = sum +z
	return sum

def problem_021():
	total =0
	for i in range (1, 10000):
		count = 0
		for j in range(1, i):
			z= i%j
			if z==0:
				count = count +j			
		if count !=i:
			count2=0
			for k in range	(1, count):
				y= count % k
				if y== 0:
					count2=count2 + k
			if count2 == i:
				total = total +i 
				#print(i,count) 
	return total

def problem_024():
	x = 1
	for i in range (0,10):
		for j in range (0,10):
			if i !=j:
				for k in range (0,10):
					if i!=k and j!=k:
						for l in range (0,10):
							if i!=l and j!=l and k!=l:
								for m in range (0,10):
									if i!=m and j!=m and k!=m and l!=m:
										for n in range (0,10):
											if i!=n and j!=n and k!=n and l!=n and m!=n:
												for o in range (0,10):
													if i!=o and j!=o and k!=o and l!=o and m!=o and n!=o:
														for p in range (0,10):
															if i!=p and j!=p and k!=p and l!=p and m!=p and n!=p and o!=p:
																for q in range (0,10):
																	if i!=q and j!=q and k!=q and l!=q and m!=q and n!=q and o!=q and p!=q:
																		for r in range (0,10):
																			if i!=r and j!=r and k!=r and l!=r and m!=r and n!=r and o!=r and p!=r and q!=r:
																					if x == 1000000:
																						y=(i,j,k,l,m,n,o,p,q,r)
																					x += 1
	return y


def problem_025():
	sw = 1
	ii = 1
	answer  =2
	ali = [1,2]
	count = 3
	while sw ==1:
		y2 = ali[ii-1] + ali[ii]
		ali= ali + [y2]
		alic = str(y2)
		z = len(alic)
		count +=1
		ii = ii + 1
		if z==1000:
			return count
			sw=0


def problem_029():##remove repeated items
	mylist=[]
	for a in range(2,101):
		for b in range (2,101):
			f=a ** b
			mylist.append(f)
	todo =int(len(mylist))
	mylist.sort()
	i=0
	while i<todo:
		j=0
		sw=0
		while j<todo:
			if i != j and mylist[i] == mylist[j]:
				mylist.remove(mylist[i])
				todo-=1
				i-=1
			j+=1		
		i+=1
	return todo


def problem_030():
	sw=1
	i=10
	result = 0
	while i< 1000000:
		alicia = str (i)
		l = len(alicia)
		total = 0
		for j in range (0,l):
			y = int(alicia[j])
			total = total + y ** 5
		if total ==i:
			result = result +i
		i+=1
	return result


def problem_034():
	i=10
	sw=1
	count = 0
	answer =0
	while sw ==1:
		lis=str(i)
		y = len(lis)
		test =0
		for j in range (0,y):
			z= int (lis[j])
			x = math.factorial (z)
			test = test +x
			if test == i:
				answer= answer+ test
				count +=1
		if count==20 or i==99999999:
			sw=0
		else: i +=1
	return answer


def problem_039():
	answer = 0
	for p in range (1,1000):
		count =0
		for a in range (1,p):
			for b in range (1, p):
				c= p - a - b;
				if c > 0:
					part = a*a + b*b
					if part == c*c:
						count +=1
		if count > answer:
			answer= p
	return answer


def problem_044():
	



def separation():
	print ("esta es la separation")

## main function to run all problems
def main ():
	print ("	")
	print ("	The solution for problem 39 is " ,problem_029())
	print ("	")

main()