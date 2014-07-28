import math
def calculateSingleLayerInductance(turns, Dout, Din, type):
	U0 = 4*math.pi*10**-7
	C1 = 0
	C2 = 0
	C3 = 0
	C4 = 0
	if type == 1: #square
		C1 = 1.27 
		C2 = 2.07
		C3 = 0.18
		C4 = 0.13
	if type == 2: #Hex
                C1 = 1.09
                C2 = 2.23
                C3 = 0 
                C4 = 0.19
	Davg = calculateDavg(Dout, Din)
	phi = calculateFillratio(Dout, Din)
	L1 = (U0*(turns**2)*Davg*C1)/2.0
	L2 = (math.log(C2/phi)+(C3*phi)+(C4*(phi**2)))
	L = L1 * L2
	print L1
	print L2
	print Davg
	print phi
	print "Single layer inductance: " + str(L) + " mH"
	return L

def calculateCoupling(turns, H):
	A = 0.184
	B = -0.525
	C = 1.038
	D = 1.001
	Kc = turns**2/((A*H**3 + B*H**2 +C*H + D) * (1.67*turns**2 - 5.84 * turns + 65)*0.64)
	print "Coupling factor: " + str(Kc)
	return Kc

def calculateTwoLayerInductance(turns, Dout, Din, type, H):
	Lone = calculateSingleLayerInductance(turns, Dout, Din, type)
	Kc = calculateCoupling(turns, H)
	Ltot = 2*Lone + 2*Kc*Lone
	return Ltot 

def calculateFourLayerInductance(turns, Dout, Din, type, H1, H2, H3):
	Ltot = 0
	Lone = calculateSingleLayerInductance(turns, Dout, Din, type)
	Ltot += Lone
	Kc = calculateCoupling(turns, H1)
	Ltot += 2*Lone*Kc # mutual coupling 1-2
	Kc = calculateCoupling(turns, (H1+H2))
	Ltot += 2*Lone*Kc # mutual coupling 1-3
	Kc = calculateCoupling(turns, (H1 + H2 + H3))
	Ltot += 2*Lone*Kc # mutual coupling 1-4
	Kc = calculateCoupling(turns, (H2))
	Ltot += 2*Lone*Kc # mutual coupling 2-3
	Kc = calculateCoupling(turns, (H2 + H3))
	Ltot += 2*Lone*Kc # mutualcoupling 2-4
	Kc = calculateCoupling(turns, H3)
	Ltot += 2*Lone*Kc
	return Ltot

def calculateDavg(Dout, Din):
	return (Dout+Din)/2.0


def calculateFillratio(Dout, Din):
	Dout = float(Dout)
	return (Dout-Din)/(Dout+Din)*1.0

