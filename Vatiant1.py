from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime("%A, %d, %B, %Y"))

if __name__ == "__main__":
    main()