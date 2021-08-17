## Test task #2 for Junior Developer in QA

Script takes as input a text file containing file names, hash algorithm names and corresponding hash sums. Then it checks files' integrity.

Usage: <this script name>.py <path to the input file> <path to the directory containing the files to check>

Due to task specification the following assumptions were made.

###Assumptions:

1. Each line in the input file always contains three space-separated values and always has the same format.

2. Hash algorithm' name in the input file is always correct and takes one of the three values ('md5', 'sha1', 'sha256').