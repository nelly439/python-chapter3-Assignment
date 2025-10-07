def is_palindrome_prime(a: int):
	if a < 2:
		return False
	if str(a)!= str(a)[ -1]:
		return False
	for count in range (2, int (a**0.5) + 1):
		if a % count == 0:
		
			return False

			return True

print(is_palindrome_prime(12312))
print(is_palindrome_prime(131))
print(is_palindrome_prime(49))
print(is_palindrome_prime(11))
print(is_palindrome_prime(3))