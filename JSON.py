import json

response = '''{
"base":"USD",
"date":"2016-05-13",
"rates":{
	"AUD":1.3728,
	"BGN":1.7235,
	"BRL":3.486,
	"CAD":1.2882,
	"CHF":0.97145,
	"CNY":6.5211,
	"CZK":23.811,
	"DKK":6.556,
	"GBP":0.69403,
	"HKD":7.7632,
	"HRK":6.6109,
	"HUF":277.73,
	"IDR":13318.0,
	"ILS":3.7737,
	"INR":66.78,
	"JPY":108.88,
	"KRW":1172.8,
	"MXN":18.05,
	"MYR":4.0299,
	"NOK":8.1669,
	"NZD":1.4709,
	"PHP":46.645,
	"PLN":3.8711,
	"RON":3.9633,
	"RUB":65.271,
	"SEK":8.2204,
	"SGD":1.3705,
	"THB":35.43,
	"TRY":2.9643,
	"ZAR":15.168,
	"EUR":0.88121}
}
'''

responseAsDict = json.loads(response)

ratesDict = responseAsDict['rates']
conversionFactor = ratesDict['BGN']

print(conversionFactor)
