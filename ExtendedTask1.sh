echo "Filename of Hard puzzles to convert:"
read convert
echo "Output file for solved puzzles:"
read out_file

python converter.py $convert temp_file.txt
python master.py temp_file.txt $out_file
rm temp_file.txt