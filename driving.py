country = input('where are you come from?:')
age = input('please enter your age:')
age = int(age)
if country =='TaiWan':
	if age >= 18:
		print('you can go to examine for the Driver License')
	else:
		print('you still can not to examine the Driver License')
elif country == "America":
	if age >= 16 :
		print('you can go to examine for the Driver License')
	else:
		print('you still can not to examine the Driver License')
else:
	print('you simply enter the TaiWan and American country')