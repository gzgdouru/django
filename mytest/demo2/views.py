from django.shortcuts import render

# Create your views here.
def index(request, maker=0):
    car_maker = ["Ford", "Honda", "Mazda"]
    carList = [
        [{"model" : "Fiesta", "price" : 203500, "count" : 11},
         {"model" :"Focus", "price" : 605000, "count" : 6},
         {"model" : "Modeo", "price" : 900000, "count" : 5}],
        [{"model" : "Fit", "price" : 450000, "count" : 15},
         {"model" : "Odyssey", "price" : 150000, "count" : 113},
         {"mode" : "CR-V", "price" : 12000000, "count" : 21}],
        [{"model" : "Mazda3", "price" : 329999, "count" : 111},
         {"model" : "Mazda5", "price" : 603000, "count" : 1123},
         {"model" : "Mazda6", "price" : 850000, "count" : 112}],
    ]

    maker_name = car_maker[int(maker)]
    cars = carList[int(maker)]

    return render(request, "demo2/index.html", context={
        "car_maker" : car_maker,
        "maker_name" : maker_name,
        "cars" : cars,
    })