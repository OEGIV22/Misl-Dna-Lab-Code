from re import A, T, X
import numpy as np
from Bio import AlignIO
from BasesToWords import basestoWords
from Bio import pairwise2
from Bio import Align
alignments = []
initial_sequences = 1
expected_alignments = 3
sequence_array = [1]*3
expected_nucleotides = 16
accepted_nucleotides = int(16*.9)
#alignments = np.array(alignments)
for alignment in AlignIO.parse("testfasta.faa","fasta", seq_count=initial_sequences):
     for record in alignment:
         alignments.append(str(record.seq))
print(alignments)

counter = 0

while counter < len(alignments) - 1:
    num = 0
    aligner = Align.PairwiseAligner()
    aligner.mode='global'
    aligner.open_gap_score = -1
    aligner.extend_gap_score = -.5
    alignment = aligner.align(alignments[counter],alignments[counter + 1])
    if  alignment.score > .7*expected_nucleotides:
        print(alignment.score)
        print(alignment[0])
        sequence_array[num] += 1
        counter += 1
    else:
        print(alignment[0])
        print(alignment.score)
        num += 1 
        counter += 1
sequence_array[num] += 1
print(sequence_array)

#clustal w: align multiple sequences
#attempt to do multi sequence alignment
#chance to do one gap
#subtract points for moving around
# if the sequences are too similar I cant seperate it into sequences
# if too small throw it out
#make expected size length in parameter
#paramter file, expected sequence, allowed sequence length, use percentages

def compare(a,multiplier,charval,sequences):
    numA = 0
    numT = 0
    numC = 0
    numG = 0
    num = sequences*multiplier
    while num < sequences*multiplier+sequences:
        if charval < len(a[num]):
            if (a[num])[charval] == 'A':
                numA = numA + 1
            elif (a[num])[charval] == 'T':
                numT = numT + 1
            elif (a[num])[charval] == 'C':
                numC = numC + 1
            elif (a[num])[charval] == 'G':
                numG = numG + 1
            num = num+1
        else:
            return ""
    numlist = {'A':numA,'T':numT,'C':numC,'G':numG}
    return max(numlist, key=numlist.get)

baseCounter = 0
sequenceCounter = 0
currentAlignment = 0
finalString = ""
finalStringStorage = []
for a in sequence_array:
    while baseCounter < expected_nucleotides:
        finalString = finalString + compare(alignments,sequenceCounter,baseCounter,sequence_array[sequenceCounter])
        baseCounter += 1
    finalStringStorage.append(finalString)
    sequenceCounter += 1
    baseCounter = 0
    finalString = ''

for x in finalStringStorage:
    basestoWords(x)

#gap: Bio.pairwise 2 module
#kNN: classifies an object into a particular category and is a form of clustering
#High Gap penalty makes aligner not use gaps
#For encoding data, part of the encoding step is randomizing the dna nucleotide sequences