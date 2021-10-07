#strings

s = "I am a string."
print(type(s)) 			#will say str

#boolean

yes = True				#boolean true
print(type(yes))

no = False 				#boolean false
print(type(no))

#List -- ordered and changeable 

alpha_list = ["a", "b", "c"] 	#list initialization
print(type(alpha_list))			#will say tuple
print(type(alpha_list[0]))		#will say string
alpha_list.append("d") 			#will add "d" to the list end
print(alpha_list)				#will print list

#tuple -- ordered and unchangeable 

alpha_tuple = ("a", "b", "c") 	#tuple initialization
print(type(alpha_tuple))		#will say tuple

try:								#attempt the following line
	alpha_tuple[2] = "d"			#won't work and willl raise TypeError
except TypeError: 					#when we get a TypeError
	print("We can't add elements to tuples!") 	#print this message
print(alpha_tuple)				#will print tuple