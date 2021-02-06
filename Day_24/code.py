test_str = 'naruto is best . naruto also has ninja now. \ ninja help people from bad' 
  
# printing original string 
print("The original string is : " + str(test_str)) 
  
# initializing replace mapping  
repl_dict = {'naruto' :  'It', 'ninja' : 'They' } 
  
# Replace duplicate Occurrence in String 
# Using split() + enumerate() + loop 
test_list = test_str.split(' ') 
res = set() 
for idx, ele in enumerate(test_list): 
    if ele in repl_dict: 
        if ele in res: 
            test_list[idx] = repl_dict[ele] 
        else: 
            res.add(ele) 
res = ' '.join(test_list) 
  
# printing result  
print("The string after replacing : " + str(res))  