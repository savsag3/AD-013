from AD_013 import AD_013# as AD_013
import time
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
#    roll = 0

    if sys.platform == "linux":
        try:
            p = AD_013.PyFingerprint_AD_013('/dev/tty.usbserial-DO00BECT')
        except Exception as e:
            print("tty.usbserial-DO00BECT not found")
            print('Exception message: ' + str(e))
        try:
            p = AD_013.PyFingerprint_AD_013('/dev/ttyUSB0')
        except Exception as e:
            print("ttyUSB0 not found")
            print('Exception message: ' + str(e))
    elif sys.platform == "darwin":
        try:
            p = AD_013.PyFingerprint_AD_013('/dev/tty.usbserial-FTZ2AE1U')
        except Exception as e:
            print("tty.usbserial-FTZ2AE1U not found")
            print('Exception message: ' + str(e))


    #while (roll < 5):
    # try:
    #     p.delete_all()
    # except Exception as e:
    #     print(str(e))

    """
    if exists enrolled user
        identify user
    elif
        enroll user
        identify user
    """
    try:
        # print("Put your finger three times at the scanner to enroll")
        # p.enrollUser()
        print("Read System Basic Parameter")
        time.sleep(2)
        pos = p.ReadSysPara()
        print(pos)
        # if(pos>=0):
        #     print("Your finger was found at " + str(pos))
        # else:
        #     print("finger not found")
        #p.delete(pos)
        #p.off_Led()
    except Exception as e:
        print('Exception message: ' + str(e))



    # try:
    #     checkEnrolled = p.enroll_Count()
    #     logger.debug(checkEnrolled)
    # except Exception as e:
    #     print('Exception message: ' + str(e))
    #
    # try:
    #     # print("Put your finger three times at the scanner to enroll")
    #     # p.enrollUser()
    #     print("Now lets identify you finger")
    #     time.sleep(2)
    #     pos = p.IdentifyUser()
    #     print(pos)
    #     if(pos>=0):
    #         print("Your finger was found at " + str(pos))
    #     else:
    #         print("finger not found")
    #     # For other functions simply check the datasheet and the api
    #     #p.delete(pos)
    #     p.off_Led()
    # except Exception as e:
    #     print('Exception message: ' + str(e))
    # #roll = roll + 1



if __name__ == "__main__":
    main()
