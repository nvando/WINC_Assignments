# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

order = 'leek 4'
number_leeks = int(order[order.find(' ')+1:])

sum_total = leek_price * number_leeks
print (sum_total)


broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'
broccoli_number = float(broccoli_order[broccoli_order.find(' '):])
broccoli_sum_total = round(broccoli_price * broccoli_number, 2)

print(str(broccoli_number) + 'kg broccoli costs ' + str(broccoli_sum_total) + 'e')

