import logging
logging.basicConfig(
    filename="vowel.log",
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d -%(levelname)s - %(message)s",
    filemode='a'    
)
def vowel_count(c:str) -> int:
    '''count vowel number in string
    Parameters:
        c(str):Input string
    Returns:
        int:total numbers of vowels in the string

    '''
    logging.info("counting no of vowels in the string")
    count=0
    for i in c:
        if i in ['a','e','i','o','u']:
            count+=1
    logging.info(f"vowel count calculated :{count}")
    return count
vowel_count('sampad')