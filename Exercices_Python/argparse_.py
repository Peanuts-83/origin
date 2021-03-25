import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', help='display the square of a given number', type=int)
parser.add_argument('y', help='display the square of a given number', type=int)
parser.add_argument('-e', '--echo', help='echo the string used as argument')
#parser.add_argument('-v', '--verbose', help='verbose mode', action='store_true')
parser.add_argument('-v', '--verbose', help='Different levels of verbosity (1 or 2)', type=int, choices=[0,1,2])
args = parser.parse_args()
if args.echo:
    print(args.echo)

if args.verbose == 1:
    print(f'{args.x} ^ {args.y} == {args.x**args.y}')
elif args.verbose == 2:
    print(f'{args.x} to the square of {args.y} is obviously {args.x**args.y}!')
else:
    print(args.x**args.y)

"""
$ python3 ./argparse_.py 3 2 -v 2
3 to the square of 2 is obviously 9!
"""