from enum import Enum

class BookingStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"

class PaymentStatus(Enum):
    PENDING = "Pending"
    PAID = "Paid"
    REFUNDED = "Refunded"

class ClassType(Enum):
    ECONOMY = "Economy"
    BUSINESS = "Business"
    FIRST_CLASS = "First Class"

    def formatted(self):
        return self.value.title().replace("_", " ")

class Passenger:
    """Class to represent a Passenger"""

    # constructor to initialize attributes
    def __init__(self, firstName, lastName, age, phoneNumber, passportNumber):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        self.__phoneNumber = phoneNumber
        self.__passportNumber = passportNumber

    # Setter and getter for first name
    def setFirstName(self, firstName):
        self.__firstName = firstName

    def getFirstName(self):
        return self.__firstName

    # Setter and getter for last name
    def setLastName(self, lastName):
        self.__lastName = lastName

    def getLastName(self):
        return self.__lastName

    # Setter and getter for age
    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    # Setter and getter for phone number
    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def getPhoneNumber(self):
        return self.__phoneNumber

    # Setter and getter for passport number
    def setPassportNumber(self, passportNumber):
        self.__passportNumber = passportNumber

    def getPassportNumber(self):
        return self.__passportNumber


class BoardingPass:
    """Class to represent a boarding pass"""

    # constructor to initialize attributes
    def __init__(self, electronicTicketNumber, classType, seatNumber, gateNumber, passengerName, boardingTill,
                 therminal):
        self.__electronicTicketNumber = electronicTicketNumber
        self.__classType = classType
        self.__seatNumber = seatNumber
        self.__gateNumber = gateNumber
        self.__passengerName = passengerName
        self.__boardingTill = boardingTill
        self.__therminal = therminal

    # Setter and getter for electronic ticket number
    def setElectronicTicketNumber(self, electronicTicketNumber):
        self.__electronicTicketNumber = electronicTicketNumber

    def getElectronicTicketNumber(self):
        return self.__electronicTicketNumber

    # Setter and getter for class type
    def setClassType(self, classType):
        self.__classType = classType

    def getClassType(self):
        return self.__classType

    # Setter and getter for seat number
    def setSeatNumber(self, seatNumber):
        self.__seatNumber = seatNumber

    def getSeatNumber(self):
        return self.__seatNumber

    # Setter and getter for gate number
    def setGateNumber(self, gateNumber):
        self.__gateNumber = gateNumber

    def getGateNumber(self):
        return self.__gateNumber

    # Setter and getter for passenger name
    def setPassengerName(self, passengerName):
        self.__passengerName = passengerName

    def getPassengerName(self):
        return self.__passengerName

    # Setter and getter for boarding till
    def setBoardingTill(self, boardingTill):
        self.__boardingTill = boardingTill

    def getBoardingTill(self):
        return self.__boardingTill

    # Setter and getter for therminal
    def setTherminal(self, therminal):
        self.__therminal = therminal

    def getTherminal(self):
        return self.__therminal


class Flight:
    """Class to represent a flight"""

    # constructor to initialize attributes
    def __init__(self, airline, cityOfDeparture, arrivalTime, departureTime, departureDate, flightNumber,
                 cityOfArrival):
        self.__airline = airline
        self.__cityOfDeparture = cityOfDeparture
        self.__arrivalTime = arrivalTime
        self.__departureTime = departureTime
        self.__departureDate = departureDate
        self.__flightNumber = flightNumber
        self.__cityOfArrival = cityOfArrival

    # Setter and getter for airline
    def setAirline(self, airline):
        self.__airline = airline

    def getAirline(self):
        return self.__airline

    # Setter and getter for country of departure
    def setCityOfDeparture(self, cityOfDeparture):
        self.__cityOfDeparture = cityOfDeparture

    def getCityOfDeparture(self):
        return self.__cityOfDeparture

    # Setter and getter for arrival time
    def setArrivalTime(self, arrivalTime):
        self.__arrivalTime = arrivalTime

    def getArrivalTime(self):
        return self.__arrivalTime

    # Setter and getter for departure time
    def setDepartureTime(self, departureTime):
        self.__departureTime = departureTime

    def getDepartureTime(self):
        return self.__departureTime

    # Setter and getter for departure date
    def setDepartureDate(self, departureDate):
        self.__departureDate = departureDate

    def getDepartureDate(self):
        return self.__departureDate

    # Setter and getter for flight number
    def setFlightNumber(self, flightNumber):
        self.__FlightNumber = flightNumber

    def getFlightNumber(self):
        return self.__flightNumber

    # Setter and getter for city of arrival
    def setCityOfArrival(self, cityOfArrival):
        self.__CityOfArrival = cityOfArrival

    def getCityOfArrival(self):
        return self.__cityOfArrival


class BookingSystem:
    """Class to represent a booking system"""

    # constructor to initialize attributes
    def __init__(self, passengerEmail, bookingStatus, paymentStatus, bookingAmount, bookingDate):
        self.__passengerEmail = passengerEmail
        self.__bookingStatus = bookingStatus
        self.__paymentStatus = paymentStatus
        self.__bookingAmount = bookingAmount
        self.__bookingDate = bookingDate

    # Setter and getter for passenger's email
    def setPassengerEmail(self, passengerEmail):
        self.__passengerEmail = passengerEmail

    def getPassengerEmail(self):
        return self.__passengerEmail

    # Setter and getter for booking status
    def setBookingStatus(self, bookingStatus):
        self.__bookingStatus = bookingStatus

    def getBookingStatus(self):
        return self.__bookingStatus

    # Setter and getter for payment status
    def setPaymentStatus(self, paymentStatus):
        self.__paymentStatus = paymentStatus

    def getPaymentStatus(self):
        return self.__paymentStatus

    # Setter and getter for booking amount
    def setBookingAmount(self, bookingAmount):
        self.__bookingAmount = bookingAmount

    def getBookingAmount(self):
        return self.__bookingAmount

    # Setter and getter for booking date
    def setBookingDate(self, bookingDate):
        self.__bookingDate = bookingDate

    def getBookingDate(self):
        return self.__bookingDate


# Create Passenger object
passenger = Passenger("James", "Smith", 30, "0501234567", 123456)

# Create BoardingPass object
boarding_pass = BoardingPass(629, ClassType.FIRST_CLASS, "09A", 3, "James Smith", "11:20", 2)

# Create Flight object
flight = Flight("National Airlines", "Chicago ORD", "13:30", "11:40", "06 DEC 20", "NA4321", "New York JFK")

# Create BookingSystem object
booking_system = BookingSystem("john.smith1@gmail.com", BookingStatus.CONFIRMED, PaymentStatus.PAID, 1000.00,
                               "01 DEC 20")

# Get and print the boarding pass details
print("Boarding Pass Details:")
print("Passenger Name:", boarding_pass.getPassengerName())
print("Airline:", flight.getAirline())
print("Electronic Ticket Number:", boarding_pass.getElectronicTicketNumber())
print("Flight Number:", flight.getFlightNumber())
print("City of Departure:", flight.getCityOfDeparture())
print("City of Arrival:", flight.getCityOfArrival())
print("Therminal:", boarding_pass.getTherminal())
print("Class Type:", boarding_pass.getClassType().formatted())
print("Seat Number:", boarding_pass.getSeatNumber())
print("Gate Number:", boarding_pass.getGateNumber())
print("Flight Date:", flight.getDepartureDate())
print("Boarding Till:", boarding_pass.getBoardingTill())
print("Departure Time:", flight.getDepartureTime())
print("Arrival Time:", flight.getArrivalTime())