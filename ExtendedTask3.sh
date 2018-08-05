echo "Do not use this script unless you have already done the following:"
echo " -  Changed the master.py temporarily to measure clock time (ask Braiden how)"
echo " -  Have installed cryptominisat5 and it is available on your path"
read -p "Do you wish to proceed?" proceed

if [ "$proceed" = "y" ]
then
    echo "cryptominisat Easy puzzles:"
    python master_cryptominisat.py puzzles.txt output.txt
    echo "minisat Eazy puzzles:"
    python master.py puzzles.txt output.txt

    read -p "Press [Enter] key to start backup..."
    python converter.py hard_puzzles.txt hard_puzzles_converted.txt
    echo "cryptominisat on hard puzzles:"
    python master_cryptominisat.py hard_puzzles_converted.txt output.txt
    echo "minisat on hard puzzles:"
    python master.py hard_puzzles_converted.txt output.txt
    rm hard_puzzles_converted.txt output.txt
else
    echo "Exiting"
fi