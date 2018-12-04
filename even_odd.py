print('Wel Come. \n This program check wether a number is EVEN or ODD')
while 1:
   x = int(raw_input('Enter an integer'))
   if x%2==0:
      print('Entered Number '+str(x)+' is EVEN')
   else:
      print('Entered Number '+str(x)+' is ODD')
   y = raw_input("Would you like to continue\n enter 'y' to  continue")
   if y =='y':
      continue
   else:
      break
