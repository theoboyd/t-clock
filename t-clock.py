#(c) 2012 Theodore Boyd
import sys
import time
import datetime as dt
from time import localtime
from threading import Thread

height_scale = 5
show_millis = False

big_digits = {'0': [',---.',
                    '|   |',
                    '|   |',
                    '|   |',
                    '`---´'],
              '1': ['  ,. ',
                    '   | ',
                    '   | ',
                    '   | ',
                    ' ----'],
              '2': [',---.',
                    '    |',
                    '.---´',
                    '|    ',
                    '`---´'],
              '3': [',---.',
                    '    |',
                    '  -< ',
                    '    |',
                    '`---´'],
              '4': ['   . ',
                    '  /| ',
                    ' / | ',
                    '´--+ ',
                    '   \' '],
              '5': [',---.',
                    '|    ',
                    '\'--. ',
                    '    |',
                    '`---´'],
              '6': [',---.',
                    '|    ',
                    ' >-. ',
                    '|   |',
                    '`---´'],
              '7': ['.----',
                    '    /',
                    '   / ',
                    '  |  ',
                    '  \'  '],
              '8': [',---.',
                    '|   |',
                    ' >-<',
                    '|   |',
                    '`---´'],
              '9': [',---.',
                    '|   |',
                    '`--< ',
                    '    |',
                    '`---´'],
              ':': [' ,. ',
                    ' `´ ',
                    '    ',
                    ' ,. ',
                    ' `´ '],
             }

def main(*args):
  if sys.version_info[0] < 3 or (sys.version_info[0] == 3
                                 and sys.version_info[1] < 1):
    print('You are using an unsupported version of Python.' +
          '\nTry running with the command \'python3.1 t-clock.py\'.')
    return

  if show_millis:
     t = Thread(target=sub_thread) # Separate, concurrent sub-second display
     t.daemon = True # Die on main thread terminating
     t.start()

  while True:
    draw_num(localtime())
    time.sleep(1)

def draw_num(time_struct):
   h = '%02d' % time_struct[3]
   m = '%02d' % time_struct[4]
   s = '%02d' % time_struct[5]

   time_array = h + ':' + m + ':' + s
   current_digit_pointer = 0
   to_print = current_digit_pointer * 3
   to_print2 = to_print + 1
   output_string = '\n'

   for y in range(0, height_scale):
      current_digit_pointer = 0
      dots = big_digit(':', y)

      for x in range(0, 3):
         to_print = current_digit_pointer * 3
         to_print2 = to_print + 1
         if current_digit_pointer < 2:
           dots_digit = dots + ' '
         else:
           dots_digit = ' '
         output_string += big_digit(time_array[to_print], y) + ' '
         output_string += big_digit(time_array[to_print2], y) + ' '
         output_string += dots_digit
         current_digit_pointer += 1
      if y < height_scale - 1:
        output_string += '\n'

   print(output_string, end='')

def big_digit(digit, y):
   return big_digits[digit][y]

def sub_thread():
   dtdt = dt.datetime
   while True:
      print('\r' + '%1d' % int(dtdt.now().microsecond / 100000), end='')
      time.sleep(0.001)

if __name__ == '__main__':
   sys.exit(main(*sys.argv))
