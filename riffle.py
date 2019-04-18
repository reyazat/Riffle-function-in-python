import sys

def get_input(q):
	if(sys.version_info > (3, 0)) :
		arg = input(q)
	else :
		arg = raw_input(q)
	return arg;

def get_list(arg , type = int):
	if(sys.version_info > (3, 0)) :
		numbers = list(map(type, arg.split()))
	else :
		numbers = map(type, arg.split())
	return numbers;

def interleave(lst1, lst2):
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    return lst1[0:1] + interleave(lst2, lst1[1:])
	

def riffle(lst, out = False):
	ln = len(lst)
	ln = int(ln)
	if ln % 2 == 0 :
		if out == True :
			lst1 = lst[:ln//2]
			lst2 = lst[ln//2:]
		else : 
			lst1 = lst[ln//2:]
			lst2 = lst[:ln//2]

		return interleave(lst1, lst2)
	else :
		return "Your list must have even  length"