import magazine

def main():
    subscription1 = magazine.Magazine("Wired", 4.00)
    subscription2 = magazine.Newspaper("Wall Street Journal", 1.50)
    
    print(subscription1.getTitle() + " yearly subscription is $" + str(subscription1.calcSubscription()))
    print(subscription2.getTitle() + " yearly subscription is $" + str(subscription2.calcSubscription()))

main()