awk 'NR%2' *.fasta | awk 'FS="." {print $1}' | sort | uniq -d > listOfGenes.txt

for i in $(cat listOfGenes.txt)
do
	grep -h --no-group-separator -A1 $i *.fasta > ${i}.fasta
	~/Users/prashant/muscle -in ${i}.fasta -out ${i}_aligned.fasta
done