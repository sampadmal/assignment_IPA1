
import logging
logging.basicConfig(
    filename="sec.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d -%(levelname)s - %(message)s",
    filemode='a'    
)
def sec_lar(l:list) -> int:
    '''finding second largest element in a list
    Parameters:
        l(list): input list
    Returns:
        int: Second largest character
    '''
    logging.info("Second largest character in the list")
    a=float('-inf')
    b=float('-inf')
    for i in l:
        if i>a:
            b=a
            a=i
        if i>b and i!=a:
            b=i
    return b
num=[1,2,3,4,5,6]
s=sec_lar(num)
logging.info(s)



