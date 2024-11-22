#pubtest

import publication

def main():
    subscription1 = publication.Magazine("Wired", 4.00, 12)
    subscription2 = publication.Newspaper("Wall Street Journal", 1.50, True)
    
    print(subscription1.getTitle() + " yearly price $ " + str(subscription1.calcSubscription()))
    print(subscription2.getTitle() + " yearly price $ " + str(subscription2.calcSubscription()))

    subscription3 = publication.Magazine("Mad Magazine", 5.95, 6)
    subscription4 = publication.Newspaper("New York Times", 1.00, False)
    
    print(subscription3.getTitle() + " yearly price $ " + str(subscription3.calcSubscription()))
    print(subscription4.getTitle() + " yearly price $ " + str(subscription4.calcSubscription()))


    
main()