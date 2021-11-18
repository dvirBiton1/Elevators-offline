from unittest import TestCase
import Elevators
import CallForElevator
import Building
import Ex1


class Test(TestCase):
    list = ["Elevator call",4.37472729,0,-1,0,-1]
    call = CallForElevator(list)
    print(CallForElevator)
    building = Building("input\Ex1_Buildings\B2.json")
    calls = Ex1.readCalls("input\Ex1_Calls\Calls_a.csv")
    Ex1.offline_algorithm()

