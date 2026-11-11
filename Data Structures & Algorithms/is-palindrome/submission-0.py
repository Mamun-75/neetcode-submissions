"""
📌 Python Slicing s[::-1] নোট (সহজ ভাষায়):

* স্লাইসিং-এর ফর্মুলা 📐:
পাইথনে যেকোনো স্ট্রিং কাটাকাটি করার নিয়ম হলো -> s[start : stop : step]
১. start (শুরু) 🏁: কোন ঘর থেকে শুরু হবে।
২. stop (শেষ) 🛑: কোন ঘরের আগে গিয়ে থামবে।
৩. step (পদক্ষেপ/লাফ) 👣: কয় ঘর করে সামনে বা পেছনে যাবে।

* s[::-1] কীভাবে কাজ করে? 🔄:
এখানে প্রথম দুটি ঘর খালি রাখা হয়েছে এবং step-এর জায়গায় -1 দেওয়া হয়েছে:
- start খালি থাকায় ও step মাইনাস (-1) হওয়ায় পাইথন একদম শেষ অক্ষর থেকে শুরু করে।
- stop খালি থাকায় একদম প্রথম অক্ষর পর্যন্ত পুরোটা নেয়।
- step = -1 হওয়ার মানে হলো "এক ঘর করে পেছনের দিকে (ডান থেকে বামে) হাঁটো!"

* উদাহরণ 💻:
s = "PYTHON"
print(s[::-1])  # আউটপুট: "NOHTYP"

#c.isalnum() this check either the character alphanumeric or not , aplhanumeric means A to Z, a to Z, and 0 to 9,, and case insensetive means  we can convert them all to lower case for fair comparision without any issue

"""
""""
        newString = ""

        for c in s:
            if c.isalnum():
                newString += c.lower()
        return newString == newString[::-1]
         
         # this solution is ok , but it uses extra memory and builtin isalnum() function to check alphanumeric characters

        
        """
        ## lets see a solution with constant space , with out creating 
        ## a new version of the string, just by using two pointer technique 
        
""""
        we can ignore  space and non alphanumeric characters 
        by applying a while loop, while the left pointer is not  alphanumerical ,
        left pointer ++,  

        time O(n), cause we need to traverse the whole string once, 
        but space is O(1) , because we are not using any extra memories,
        here we need to create our own function to check alphanumeric
         # to find ascii value in python we use ord(c) function

        ascii value for 0 = 48
                        9 = 57
                        a = 
    """

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1

        while l<r:
            while l<r and not self.alphanum(s[l]):
                l += 1
            while r>l and not self.alphanum(s[r]):
                 r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l,r = l+1, r-1

        return True


    def alphanum(self, c):
            return (ord('A') <= ord(c) <=ord('Z') or
                    ord('a') <= ord(c) <=ord('z') or
                    ord('0') <= ord(c) <=ord('9')) 



"""
📌 Valid Palindrome নোট (Two Pointers পদ্ধতি):

* কী কাজ করে? 🎯:
একটি বাক্য বা শব্দকে সামনে থেকে পড়লে এবং উল্টো দিক (পেছন) থেকে পড়লে একই হয় কি না তা চেক করে (যেমন: "A man, a plan, a canal: Panama")। তবে হিসাবের সময় সব স্পেস, কমা বা বিরামচিহ্ন বাদ দেওয়া হয় এবং বড়-ছোট হাতের অক্ষরকে একই ধরা হয়।

* আসল জাদু (Two Pointers) 🪄:
নতুন কোনো স্ট্রিং না বানিয়ে (O(1) মেমোরিতে) আমরা দুটি আঙুল ব্যবহার করি—বাম আঙুল (l 👈) থাকে শুরুর অক্ষরে (`0`), আর ডান আঙুল (r 👉) থাকে শেষ অক্ষরে (`len(s) - 1`)। এরপর দুই দিক থেকে অক্ষর মেলাতে মেলাতে মাঝখানের দিকে এগিয়ে আসি।

* লাইন-বাই-লাইন ব্যাখ্যা 📝:
১. while l < r: 🔄: যতক্ষণ বাম আঙুল ডান আঙুলের বাম পাশে আছে, ততক্ষণ চেক চলবে।
২. ভেতরের দুটি while লুপ ⏭️: বাম বা ডান আঙুল যদি কোনো ফাঁকা জায়গা (space) বা চিহ্নের (যেমন `,` বা `:`) ওপর পড়ে, তবে `l += 1` এবং `r -= 1` করে আঙুল দুটিকে সরিয়ে আসল অক্ষর বা সংখ্যার ওপর নিয়ে যাওয়া হয়।
৩. if s[l].lower() != s[r].lower(): 🚨: দুই আঙুলের অক্ষর দুটিকে ছোট হাতের অক্ষরে রূপান্তর (`.lower()`) করে মেলানো হয়। না মিললেই সাথে সাথে `False`!
৪. l, r = l + 1, r - 1 👣: অক্ষর মিলে গেলে পরের জোড়া মেলানোর জন্য বাম আঙুল এক ঘর ডানে এবং ডান আঙুল এক ঘর বামে এগিয়ে আসে।
৫. alphanum(self, c) ফাংশন 🔢: `ord()` ফাংশন দিয়ে চেক করা হয় অক্ষরটি কি ASCII টেবিলের বড় হাতের (A-Z), ছোট হাতের (a-z) নাকি সংখ্যার (0-9) ভেতরে পড়েছে।

Time Complexity: O(n) (পুরো স্ট্রিং মাত্র একবার দেখা হয়)
Space Complexity: O(1) (অতিরিক্ত কোনো মেমোরি বা নতুন স্ট্রিং তৈরি হয় না)
"""

        
       