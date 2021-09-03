def isPalindrome(s):
    return s == s[::-1]
 
def test_answer():
	assert isPalindrome("software engineering gnireenigne erawtfos") == True
	assert isPalindrome("HomeWork 2 Github Homework") == False
	assert isPalindrome("reviver") == True
	assert isPalindrome("Group12orG") == False
	assert isPalindrome("wasitacatisaw") == True
	assert isPalindrome("SE is cool SE") == False
	assert isPalindrome("rotator") == True
