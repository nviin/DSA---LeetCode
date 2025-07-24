🧠 Problem Statement
Given a string s, find the longest substring that is a palindrome (i.e., it reads the same backward as forward).

🔁 Example
txt
Copy
Edit
Input:  s = "noonabcba"
Output: "abcba"
✅ What is a Palindrome?
A palindrome is a word or sequence that reads the same forward and backward. Examples:

"madam"

"noon"

"racecar"

"abcba"

🔍 Solution Approach: Expand Around Center
💡 Idea:
Every palindrome is like a mirror with a center. That center could be:

a single letter (odd-length palindrome like "racecar")

or between two letters (even-length palindrome like "noon")

We try to expand outward from every character (and between characters) and check how far we can go while the substring remains a palindrome.

🧩 Python Code
python
Copy
Edit
def longestPalindrome(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        odd_pal = expand_around_center(i, i)       # odd length
        even_pal = expand_around_center(i, i + 1)   # even length

        if len(odd_pal) > len(longest):
            longest = odd_pal
        if len(even_pal) > len(longest):
            longest = even_pal

    return longest
🧪 Example Execution with "noonabcba"
The function will:

Expand around each character to find palindromes

Keep track of the longest one

Step-by-step found palindromes:
Center Index	Palindrome Found
0	"n"
1	"noon" ✅
2	"o"
3	"n"
4	"a"
5	"b"
6	"abcba" ✅✅
7	"b"
8	"a"

✔️ Final answer: "abcba"

⏱️ Time & Space Complexity
Aspect	Value
Time Complexity	O(n²)
Space Complexity	O(1)

We check around every center (O(n)), and expand at most O(n) per center ⇒ O(n²) time.

📌 Key Points to Remember
Use expand around center to avoid using extra memory (like DP table).

Always check both odd and even centers.

Update the result only when a longer palindrome is found.

🧠 Real Life Analogy
Imagine holding a mirror in the middle of a word. Expand outward while both sides of the mirror show the same letter — that’s your palindrome!
