def isPalindrome(s):
	return s == s[::-1]
s = input()
ans = isPalindrome(s)
if ans:
	print("Palindrome number")
else:
	print("Not a Palindrome number")
