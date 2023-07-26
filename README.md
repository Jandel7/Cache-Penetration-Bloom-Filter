# Biological-Sequence-Alignments


The Goal of project one is to create a Bloom Filter based on multiple hashes.

The Bloom Filter will be created dynamically based on dummy inputs (emails) from a file that must be evaluated at run time.
Bloom Filter must have a false positive probability of 0.0000001.

You can understand the equations involved at https://hur.st/bloomfilter/ 

Your program must take 2 files as inputs.
    Example: python <your_program> db_input.csv db_check.csv
    
The input comma-separated files will contain 1 column: Email.   
Based on the email key, your program will build the Bloom Filter based on file 1 inputs.  
Then it will need to check file 2 entries against the bloom filter and provide its assessment.

***
You don't need to develop your hash library, you can use 3rd party libraries like Murmur.
                                                ^
                                                |
Sadly Moodle Python installation dont have the Murmur and bitarrays libraries, so they can't be used.
***

Your program will output to the command line the original e-mail and the Bloom Filter result.

weseGLCIEPTUusDlU@aol.com,Probably in the DB
uEUSgDKJN@hotmail.com,Not  in the DB
PLekUVqtWnRVWShep,Not  in the DB
BXgWIGaZRv@aol.com,Probably in the DB
