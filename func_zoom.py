def input_value(newX) :
    if input_value.newX >= newX :
        input_value.newX = func_zoomout.newX
    elif input_value.newX < newX :
        input_value.newX = func_zoomin.newX
input_value.newX = 0

def func_zoomin(newX) :
    func_zoomin.newX = int(newX + 1)
    input_value(func_zoomin.newX)
func_zoomin.newX = 0

def func_zoomout(newX) :
    func_zoomout.newX = int(newX - 1)
    input_value(func_zoomout.newX)
func_zoomout.newX = 0

newX = 10

func_zoomin(newX)
newX = input_value.newX
print(newX)
func_zoomin(newX)
newX = input_value.newX
print(newX)

func_zoomin(newX)
newX = input_value.newX
print(newX)

func_zoomin(newX)
newX = input_value.newX
print(newX)

func_zoomin(newX)
newX = input_value.newX
print(newX)

func_zoomout(newX)
newX = input_value.newX
print(newX)

func_zoomout(newX)
newX = input_value.newX
print(newX)

func_zoomout(newX)
newX = input_value.newX
print(newX)

func_zoomout(newX)
newX = input_value.newX
print(newX)

func_zoomout(newX)
newX = input_value.newX
print(newX)
