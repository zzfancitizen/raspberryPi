
from parking import ParkingLot
from bottle import route, get, post, run, request, template

lot = ParkingLot()

@route('/hello')
def hello():
    return "Hello World!"

@post("/open")
def open():
	lot.setup()
	return lot.openGate()
	lot.destroy()

@post("/close")
def close():
	lot.setup()
	return lot.closeGate()
	lot.destroy()

run(host = "0.0.0.0", port = "9999")






