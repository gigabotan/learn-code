package leetcode150

import "unicode"

func isPalindrome(s string) bool {
    start := 0
	end := len(s) - 1
	for start < end {
		if !unicode.IsLetter(rune(s[start])) {
			start++
			continue
		}
		if !unicode.IsLetter(rune(s[end])) {
			end--
			continue
		}
		if unicode.ToLower(rune(s[start])) != unicode.ToLower(rune(s[end])) {
			return false
		}
		start++
		end--
	}

	return true
}