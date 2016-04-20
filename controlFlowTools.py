"""
To clear the screen in the shell, use:		subprocess.call('cls', shell=True)

You can change the way you call modules: 	import subprocess as sp

Then you can use: 							sp.call('cls', shell=True) 

This will work for any as [varible]: 		import subprocess as foo

And again:									foo.call('cls', shell=True)
"""

print('\n' + 50*'-' + '\n' 'Below is an example of a nested for loop.' '\n' + 50*'-' + '\n')
for x in range(3):
	print('X is', x)
	
	for y in range(3):
		print('Y is', y, end=' ')
		print('Foo')
		
	print('\n' 'Y is now', y, 'the "for y in range(3)" loop is done.' '\n')
	
print('X is now', x, 'the "for x in range(3) loop is done.')



print(3*'\n' + 50*'-' + '\n' 'Below is an example of the break statement.' '\n' + 50*'-' + '\n')
for x in range(3):
	print('X is', x)
	
	for y in range(3):
		print('Y is', y, end=' ')
		if x > 0 and y > 0:
			print('I am breaking now.')
			break
		print('Foo')
		
	print('\n' 'Y is now', y, 'the "for y in range(3)" loop is done.' '\n')
	
print('X is now', x, 'the "for x in range(3) loop is done.')



print(3*'\n' + 50*'-' + '\n' 'Below is an example of the continue statement.' '\n' + 50*'-' + '\n')
for x in range(3):
	print('X is', x)
	
	for y in range(3):
		print('Y is', y, end=' ')
		if x > 0 and y > 0:
			print('I am continuing now.')
			continue
		print('Foo')
		
	print('\n' 'Y is now', y, 'the "for y in range(3)" loop is done.' '\n')
	
print('X is now', x, 'the "for x in range(3) loop is done.')