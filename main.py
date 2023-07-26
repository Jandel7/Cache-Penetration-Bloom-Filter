'''
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
'''


import sys
import csv
import math
import array as arr

'''
The BloomFilter class has four instance variables: n, p, m, and bit_Array. 
n is the number of elements to be inserted into the Bloom filter. 
p is the false positive probability, which determines the probability 
that the Bloom filter will indicate that an element is a member of the set when it is actually not. 
m is the size of the bit array used to store the Bloom filter. 
bit_Array is the actual bit array used to store the Bloom filter.
'''

class BloomFilter(object):
    
    def __init__(self,elm_count,false_pos_prob):
        '''
        The __init__ method is the constructor for the BloomFilter class. 
        It takes two arguments: elm_count and false_pos_prob. 
        It initializes the instance variables n, p, m, and bit_Array using these arguments.
        '''

        self.n = elm_count # n = ceil(m / (-k / log(1 - exp(log(p) / k))))
        
        self.p = false_pos_prob # p = pow(1 - exp(-k / (m / n)), k)

        self.m = int(math.ceil((self.n * math.log(self.p)) / math.log(1 / pow(2, math.log(2))))); # m = ceil((n * log(p)) / log(1 / pow(2, log(2))));
        
        self.size = self.m

        self.k = int(round((self.m / self.n) * math.log(2))); # k = round((m / n) * log(2));

        self.bit_Array = arr.array('B', [0 for i in range(self.m)]) # Create a bit array of size(self.m) and initialize it with all zeros

                
    def addElm(self, elm_count):
        
        '''
        The addElm method is used to add an element to the Bloom filter. 
        It takes one argument: elm_count. It hashes the element k times, where k is the number of hash functions to be used. 
        The result of each hash function is used to set a bit in the bit_Array to 1.
        '''
        
        for seed in range(self.k):
            
            result = hash(elm_count + str(seed)) % self.size
            self.bit_Array[result] = 1
                
    def checkElm(self, elm_count):
        
        '''
        The checkElm method is used to check if an element is a member of the set represented by the Bloom filter. 
        It takes one argument: elm_count. It hashes the element k times, where k is the number of hash functions to be used.
        If any of the bits in the bit_Array indicated by the hash function results are 0, the method returns False 
        to indicate that the element is definitely not a member of the set. Otherwise, it returns True to indicate that the
        element is probably a member of the set.
        '''
        
        for seed in range(self.k):
            
            result = hash(elm_count + str(seed)) % self.size
            
            if self.bit_Array[result] == 0:
                return 0
        return 1
            
        
        
        
        
def csvReader(file):
    
    '''
    The csvReader function is a helper function used to read data from a CSV file and return a list of elements. 
    It takes one argument: file, which is the path to the CSV file to be read. It opens the file, reads the data 
    using the csv module, and returns a list of elements from the first column of the file.
    '''
    
    rows = []
    with open(file, 'r') as file:
        
        reader = csv.reader(file)
        
        for row in reader:
            
            if row[0] != 'Email' and row[0] != 'E-mail':
                
                rows.append(row[0])
    return rows



def main():
    
    '''
    The main function is the entry point of the program. It takes no arguments. 
    It first checks that the program was called with at least one command-line argument, which should be the file 
    to the input CSV file containing the elements to be added to the Bloom filter. It then reads the input CSV file and 
    the second CSV file provided as the second command-line argument. It uses the first CSV file to populate the Bloom filter 
    and the second CSV file to check if the elements are members of the set represented by the Bloom filter. 
    It prints the results of the check to the standard output.
    
    '''
    
    if len(sys.argv) > 1:
        
        db_input = csvReader(sys.argv[1])
        
        db_check = csvReader(sys.argv[2])
        
        n = len(db_input)
        p = 0.0000001
        
        BF = BloomFilter(n,p)
        
        for elm in db_input:
            
            BF.addElm(elm)
            
            
        for elm in db_check:
            
            if BF.checkElm(elm) and elm in db_input:
                
                print(elm + ",Probably in the DB")

            elif BF.checkElm(elm) and elm not in db_input:
                
                print(elm + ",False positive")
                
            elif not BF.checkElm(elm) and elm not in db_input:
                
                print(elm + ",Not in the DB")
main()
