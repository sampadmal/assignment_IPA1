import logging
logging.basicConfig(
    filename="freq.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d -%(levelname)s - %(message)s",
    filemode='a'    
)
def frequency(c:str) -> int : 
    '''counting frequency of a character in a string
       Parameters:
            c(str):Input string
       Returns:
            int:frequency of the character
    '''
    logging.info("frequency of characters  in the string")
    freq={}
    for i in c:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
f=frequency('sampad')
logging.info(f)
        

        