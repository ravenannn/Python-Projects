from abc import ABC, abstractmethod

#create a parent class
class School_Costs(ABC):
    # Assign a
    def monthlyPayment(self, amount):
        print("Your monthly tuition payment: ", amount)
    # This function is telling us to pass in an argument, but we won't tell you
    # how or what kind of data it will be
        @abstractmethod
        def payment(self, amount):
            pass

# Create a child class
class CreditCardPayment(School_Costs):
    # Here we define how to utilize the monthly payment function from it's parent
    def payment(self, amount):
        print("Your payment amount of {} does not fulfill your $200 obligation ".format(amount))

obj = CreditCardPayment()
obj.monthlyPayment("$200")
obj.payment("$100")
