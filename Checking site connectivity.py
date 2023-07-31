import urllib.request as urllib


def main(url):
    print("Checking the connectivity ")

    response = urllib.urlopen(url)
    print("Connected to ", url, "Successfully")
    print("The response code was: ", response.getcode())

print("This is a site connectivity checker program")
input_url =input("Input the url of the site you want to check: ")

main(input_url)

