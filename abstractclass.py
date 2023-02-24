import abc


class PrimeChecker(abc.ABC):

    @abc.abstractmethod
    def is_prime(self, num):
        def is_prime(self, num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

    @classmethod
    def register(cls, VirtualPrimeChecker):
        pass


class NewPrimeChecker(PrimeChecker):

    def is_prime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

class VirtualPrimeChecker:

    def is_prime(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True


PrimeChecker.register(VirtualPrimeChecker)


check = VirtualPrimeChecker()

print(isinstance(check, PrimeChecker))  

checker = NewPrimeChecker()
print(checker.is_prime(3))
print(checker.is_prime(12))




