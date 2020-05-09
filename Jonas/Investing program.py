import bs4
import requests
import multiprocessing
from functools import partial


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
links = ["http://eoddata.com/stocklist/NYSE/", "http://eoddata.com/stocklist/NASDAQ/", "http://eoddata.com/stocklist/AMEX/"]
ending = ".htm"

price = 1000000
min_score = 95

analizeLink = "https://toolbox.ruleoneinvesting.com/members/finance/default.aspx?stock="
calculate_link = "https://toolbox.ruleoneinvesting.com/members/finance/ValuationCalculations.ashx"
login_url = "https://toolbox.ruleoneinvesting.com/login.aspx"

email = "hocolifi@simpleemail.info"
password = "123"


payload = {'email':email, 'password':password}

result_file = "results.txt"
config_file = "configs.txt"

class stock:
	price = 0
	symbol = ""
	score = 0
	is_disabled = False
	margin_of_safety_price = 0
	def __init__(self, symbol, price):
		self.price = price
		self.symbol = symbol

def getPrimaryData(letter, ns):
	global ending
	page = requests.get(ns.link+letter+ending)
	soup = bs4.BeautifulSoup(page.content, "html.parser")
	stocks = soup.find_all("tr", ["re", "ro"])

	for z in stocks:
		if(float(z.find_all("td")[4].decode_contents().replace(",", "")) <= price):
			ns.stock_array.append(stock(z.find("a").decode_contents().strip(), float(z.find_all("td")[4].decode_contents().replace(",", "."))))


def analizeData(index, stock_object, ns, s):
	ns.counter += 1
	global calculate_link, analizeLink
	print(ns.counter)
	page = s.get(analizeLink+stock_object.symbol)
	soup = bs4.BeautifulSoup(page.content, "html.parser")
	score = soup.find("div" , id="ctl00_ctl00_ctl00_MainContent_MainContent_quoteDetail_TownScoresCtrl_score_rule_one")
	if score is None:
		obj = ns.stock_array[index]
		obj.is_disabled = True
		ns.stock_array[index] = obj
	else:
		score = float(score.decode_contents())
		if (score >= min_score):
			obj = ns.stock_array[index]
			obj.score = score
			ns.stock_array[index] = obj
			SymbolId = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtSymbolId")['value'])
			MOS = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtMOSHidden")['value'])
			EPS = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtEPSTTMHidden")['value'])
			FutureEPS = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtFutureEPSHidden")['value'])
			PE = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtPEHidden")['value'])
			Rate = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtRateHidden")['value'])
			FutureValue = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtFutureValueHidden")['value'])
			MARR = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtMarrHidden")['value'])
			FCFPerShare = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtFCFPerShareHidden")['value'])
			CalcType = str(soup.find("select", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_ddlGreenCalcType").find(selected="selected")['value'])
			PBTYears = str(soup.find("select", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_ddlPBTYears").find(selected="selected")['value'])
			CurrentSymbol = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtCurrentSymbol")['value'])
			ContactId = str(soup.find("input", id="ctl00_ctl00_ctl00_MainContent_MainContent_MainContent_UC_MOSCalc_txtContactId")['value'])

			getInfoPayload = {"myData[MOS]": MOS, "myData[EPS]": EPS, "myData[FutureEPS]": FutureEPS, "myData[PE]": PE, "myData[Rate]": Rate, "myData[FutureValue]": FutureValue, "myData[MARR]": MARR, "myData[FCFPerShare]": FCFPerShare, "myData[CalcType]": CalcType, "myData[PBTYears]": PBTYears, "myData[CurrentSymbol]": CurrentSymbol, "myData[ContactId]": ContactId, "myData[SymbolId]": SymbolId}
			
			response = s.post(calculate_link, data=getInfoPayload)
			margin_of_safety_price = float(response.json()["MOS"])
			if (margin_of_safety_price >= stock_object.price):
				obj = ns.stock_array[index]
				obj.margin_of_safety_price = margin_of_safety_price
				ns.stock_array[index] = obj
			else:
				obj = ns.stock_array[index]
				obj.is_disabled = True
				ns.stock_array[index] = obj

		else:
			obj = ns.stock_array[index]
			obj.is_disabled = True
			ns.stock_array[index] = obj

		

def showData(stock_array):
	global result_file
	f = open(result_file , "w")
	for i in stock_array:
		if(i.is_disabled == False):
			f.write("Stock symbol: " + i.symbol+ " Stock price: "+str(i.price)+" Rule #1 Score: "+ str(i.score)+" Margin of safety price: "+str(i.margin_of_safety_price)+'\n')
			print("Stock symbol: " + i.symbol+ " Stock price: "+str(i.price)+" Rule #1 Score: "+ str(i.score)+" Margin of safety price: "+str(i.margin_of_safety_price)+'\n')

if __name__ == '__main__':
	p = multiprocessing.Pool()
	manager = multiprocessing.Manager()
	ns = manager.Namespace()
	ns.stock_array = manager.list()
	ns.counter = 0
	print("0/3")
	for i in links:
		ns.link = i
		prod = partial(getPrimaryData, ns=ns)
		p.map(prod, letters)

	print("1/3")

	print(len(ns.stock_array))
	s = requests.Session()
	s.post(login_url, data=payload)
	prod = partial(analizeData, ns=ns, s=s)
	p.starmap(prod, enumerate(ns.stock_array))

	print("2/3")

	showData(ns.stock_array)

	print("3/3")

	p.close()
