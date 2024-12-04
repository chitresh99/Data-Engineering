import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                      logging.FileHandler('app.log',mode='w'),#makes a file and saves the logs there
                      logging.StreamHandler() #prints to the console
                    ])

def calculate_sum(a,b):
    logging.debug(f"calculating sum of {a} and {b}")
    result = a + b
    logging.info(f"sum calculated successfully : {result}")
    return result

if __name__ == "__main__":
  logging.info("starting the program")
  result = calculate_sum(10,20)
  logging.info("program completed")