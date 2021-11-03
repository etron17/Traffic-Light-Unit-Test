"""
Name: Dojae Kim
Student Number: 400420323
Student email: kim408@mcmaster.ca
File name: Assignment 5 stubs traffic light file.
"""

import time

verticalRoad = "\t\t\t\t\t        |\n\t\t\t\t\t        |\n\t\t\t\t\t        |\n\t\t\t\t\t        |\n\t\t\t\t\t        |"
horizontalRoad = "===================="


class Intersection:
    def __init__(self):
        self.mainRoadCar = "GREEN"
        self.sideRoadCar = "RED"
        self.mainRoadPedestrian = "GREEN"
        self.sideRoadPedestrian = "RED"
        self.road = f"\t\t\tCars (MAIN): {self.mainRoadCar} Pedestrians (MAIN): {self.mainRoadPedestrian}\n{verticalRoad}\nCars (SIDE): {self.sideRoadCar} Pedestrians (SIDE): {self.sideRoadPedestrian}{horizontalRoad}Cars (SIDE): {self.sideRoadCar} Pedestrians (SIDE): {self.sideRoadPedestrian}\n{verticalRoad}\n\t\t\tCars (MAIN): {self.mainRoadCar} Pedestrians (MAIN): {self.mainRoadPedestrian}"

    def changeSignals(self):
        if self.mainRoadCar == "GREEN" and self.mainRoadPedestrian == "GREEN" and self.sideRoadCar == "RED" and self.sideRoadPedestrian == "RED":
            self.mainRoadCar = "RED"
            self.mainRoadPedestrian = "RED"
            self.sideRoadCar = "GREEN"
            self.sideRoadPedestrian = "GREEN"
            self.road = f"\t\t\tCars (MAIN): {self.mainRoadCar} Pedestrians (MAIN): {self.mainRoadPedestrian}\n{verticalRoad}\nCars (SIDE): {self.sideRoadCar} Pedestrians (SIDE): {self.sideRoadPedestrian}{horizontalRoad}Cars (SIDE): {self.sideRoadCar} Pedestrians (SIDE): {self.sideRoadPedestrian}\n{verticalRoad}\n\t\t\tCars (MAIN): {self.mainRoadCar} Pedestrians (MAIN): {self.mainRoadPedestrian}"

        elif self.mainRoadCar == "RED" and self.mainRoadPedestrian == "RED" and self.sideRoadCar == "GREEN" and self.sideRoadPedestrian == "GREEN":
            self.mainRoadCar = "GREEN"
            self.mainRoadPedestrian = "GREEN"
            self.sideRoadCar = "RED"
            self.sideRoadPedestrian = "RED"
            self.road = f"\t\t\tCars (MAIN): {self.mainRoadCar} Pedestrians (MAIN): {self.mainRoadPedestrian}\n{verticalRoad}\nCars (SIDE): {self.sideRoadCar} Pedestrians (SIDE): {self.sideRoadPedestrian}{horizontalRoad}Cars (SIDE): {self.sideRoadCar} Pedestrians (SIDE): {self.sideRoadPedestrian}\n{verticalRoad}\n\t\t\tCars (MAIN): {self.mainRoadCar} Pedestrians (MAIN): {self.mainRoadPedestrian}"
        else:
            print("Something is not right")

    def printIntersection(self):
        print()
        print(self.road)
        print()

    def simulate_first_signals_change(self):
        # first, the main roads are GREEN and side roads are RED
        time.sleep(91)
        # traffic on the side street has been waiting for more than 90 seconds, so lights change
        self.changeSignals()
        # now, we expect main roads to be RED and side roads to be GREEN


def main():
    intersection = Intersection()

    while True:
        intersection.printIntersection()
        time.sleep(91)
        # traffic on the side street has been waiting for more than 90 seconds
        print("\nLights changing!")
        intersection.changeSignals()
        intersection.printIntersection()
        time.sleep(30)
        # after 30 seconds the side street turns red and the main street turns green
        print("\nLights changing!")
        intersection.changeSignals()


if __name__ == "__main__":
    main()

