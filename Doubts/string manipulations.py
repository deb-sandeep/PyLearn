# Take the following Python code that stores a string:
# str = "X-DSPAM-Confidence: 0.8475"
# 
# Use find and string slicing to extract the portion of the string after 
# the colon character and then use the float function to convert the extracted 
# string into a floating point number.
# 
# ## Just want to understand logically how string splitting happens

# [Sandy] :)
str = 'X-DSPAM-Confidence: 0.8475'
print float(str[str.rfind(':')+1:])

#I'm still confused. Can we take this up on wednesday's call?
