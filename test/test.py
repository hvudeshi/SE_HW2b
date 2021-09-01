def isPalindrome(s):
    return s == s[::-1]

def test_answer():
	assert isPalindrome("hiih") == True
	assert isPalindrome("not a palindrome") == False
	assert isPalindrome("holloh") == True