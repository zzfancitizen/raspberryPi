
from parking import ParkingLot
from bottle import route, get, post, run, request, template

lot = ParkingLot()

@route('/hello')
def hello():
    return "Hello World!"

@post("/open")
def open():
	lot.setup()
	lot.openGate()
	return "Gate opened!"
	lot.destroy()

@post("/close")
def close():
	lot.setup()
	lot.closeGate()
	return "Gate closed!"
	lot.destroy()

run(host = "0.0.0.0", port = "9999")






