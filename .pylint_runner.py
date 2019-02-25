import sys
from pylint import lint

#https://stackoverflow.com/questions/50944575/how-to-set-a-pylint-score-threshold
THRESHOLD = 9

if len(sys.argv) < 2:
    raise ArgumentError("Module to evaluate needs to be the first argument")
try:
    # python 3.X
    run = lint.Run([sys.argv[1]], do_exit=False)
except TypeError:
    #python 2.7
    run = lint.Run([sys.argv[1]])
score = run.linter.stats['global_note']
if score < THRESHOLD:
    sys.exit(1)
