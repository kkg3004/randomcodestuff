import random
from pathlib import Path
from PIL import Image
import qrcode
import pyperclip
import time
import requests
import socket

# Get the computer's hostname
hostname = socket.gethostname()
# Get the local IP address for safe mode check
local_ip = socket.gethostbyname(hostname)

def generate_and_save(filename="random_image.png"):
    # 1. Dynamically find the Downloads folder path
    downloads_path = Path.home() / "Downloads"
    full_save_path = downloads_path / filename

    # 2. Random dimensions
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))

    # 3. Create the image
    image = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            random_color = (random.randint(0, 255), 
                            random.randint(0, 255), 
                            random.randint(0, 255))
            image.putpixel((x, y), random_color)
            
    # 4. Save to the specific Downloads location
    image.save(full_save_path)
    print(f"Image successfully saved to: {full_save_path}")

def create_qr_code(filename="custom_qr.png"):
    downloads_path = Path.home() / "Downloads"
    full_save_path = downloads_path / filename
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(input("Enter the website to encode in the QR code: "))
    qr.make(fit=True)

    # Create an image with custom colors
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(full_save_path)

def jew_or_not():
    name = input("Enter a name to check if they're Jewish: ")
    if name.lower() == "benjamin netanyahu" or name.lower() == "netanyahu" or name.lower() == "bibi":
        print(f"really bro, {name.lower()} is literally the prime minister of israel. he's definitely jewish.")
    elif name.lower() == "zayd" or name.lower() == "zatie" or name.lower() == "zayd zaheer":
        print(f"zatie is the most jewist person ever, and hes white as hell, but he says hes pakistani, which is a lie. he is the ultimate jew.")
    elif name.lower() == "trump" or name.lower() == "donald trump":
        print(f"he's literally bibi's little gay boy and bibi is his master, so he's definitely jewish.")
    elif name.lower() == "leonid":
        print(f"leonid is jew af and he doesnt deny it, even tho hes also russian.")
    elif name.lower() == "epstein" or name.lower() == "jeffrey" or name.lower() == "jeffrey epstein":
        print(f"big stein is jewish of course, he's a pedophile and and a billionaire, so he's definitely jewish.")
    elif name.lower() == "mark zuckerberg" or name.lower() == "zuckerberg":
        print(f"mark zuckerberg is a lizard person and he's also jewish cuz of facebook, which is a jewish company.")
    elif name.lower() == "peter thiel" or name.lower() == "thiel":
        print(f"palantir is the most jewish company ever, so peter thiel is definitely jewish.")
    elif name.lower() == "elon musk" or name.lower() == "musk":
        print(f"elon musk is jewish cuz he became american instead of being a true south african, and also because tesla's cars suck.")
    elif name.lower() == "jeff bezos" or name.lower() == "bezos":
        print(f"jeff bezos, eh it depends, he's a billionaire, but he's also a white guy who looks like a potato, so it's hard to say.")
    elif name.lower() == "ilgaz" or name.lower() == "ilgaz cilingir":
        print(f"ilgaz is a jew and he's also a turkish citizen, so he's definitely jewish.")
    elif name.lower() == "tejas gupta" or name.lower() == "tejas":
        print(f"tejas gupta is an indian, and israel is the fatherland and india the motherland, so he's definitely jewish.")
    elif random.randint(0, 1) == 0:
        print(f"yes, {name.lower()} is jewish.")
    else:
        print(f"no, {name.lower()} is not Jewish.")

arr = [random.randint(1, 90) for _ in range(100)]
def stein_sort(arr):
    #removes any number over 18 and then sorts the remaining numbers in ascending order
    filtered_arr = [x for x in arr if x < 18]
    return arr, sorted(filtered_arr)

def nine_eleven_conspiracy():
    ans = input("""do you believe that 9/11 was an inside job? (yes/no): """)
    if ans.lower() == "yes":
        print("""you are correct.
9/11 was an inside job orchestrated by the US government
to justify invading the Middle East and controlling global oil resources.
The Twin Towers were brought down by controlled demolitions, and the Pentagon was hit by a missile, not a plane.
The official story is a cover-up to hide the truth from the public.""")
    elif ans.lower() == "no":
        print("wrong, 9/11 was definitely an inside job, wake up sheeple.")
    else:
        print("invalid input, please enter yes or no.")

def zihan_and_izzy():
    a = input("should zihan ask izzy out? (yes/no): ")
    if a.lower() == "yes":
        print("lets leave it up to chance!")
        if random.randint(0, 1) == 0:
            print("WIN. zihan should ask izzy out, they would be perfect together and it would be a shame if they didn't end up together. come on zihan, just ask izzy out already, you know you want to. lock tf in.")
        else:
            print("LOSE. zihan should still ask izzy out anyways, they would be perfect together and it would be a shame if they didn't end up together. come on zihan, just ask izzy out already, you know you want to. lock tf in.")
    elif a.lower() == "no":
        print("this is the wrong answer, zihan should definitely ask izzy out, they would be perfect together and it would be a shame if they didn't end up together. come on zihan, just ask izzy out already, you know you want to. lock tf in.")
    else:
        print("invalid input, please enter yes or no.")

def scramble_image_pixels(filename="scrambled_image.png"):
    downloads_path = Path.home() / "Downloads"
    full_save_path = downloads_path / filename
    image = Image.open(image_path)
    pixels = list(image.get_flattened_data())
    random.shuffle(pixels)
    scrambled_image = Image.new(image.mode, image.size)
    scrambled_image.putdata(pixels)
    scrambled_image.save(full_save_path)

def morse_code():
    morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}
    text = input("Enter text to convert to Morse code: ")
    morse_code = ' '.join(morse_dict.get(char.upper(), '') for char in text)
    pyperclip.copy(morse_code)
    print("Copied to clipboard.")

if __name__ == "__main__":
    ask = "no"
    if local_ip == "172.16.195.188":
        choice = input("Choose an option:\n1. Generate Random Image\n2. Create QR Code\n3. Scramble Image Pixels\n4. Convert to Morse Code\n5. Override.\nEnter 1, 2, 3, 4 or 5: ")
        if choice == '1':
            generate_and_save()
        elif choice == '2':
            create_qr_code()
        elif choice == '3':
            image_path = input("Enter the path to the image file: ")
            scramble_image_pixels(image_path)
        elif choice == '4':
            morse_code()
        elif choice == '5':
            ask = input("Are you sure you want to override safe mode? This will give you access to all features, including the potentially dangerous ones. (yes/no): ")
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")
    if ask == "yes":
        print("WARNING: unsafe mode activated. all features will be available.")
        choice = input("Choose an option:\n1. Generate Random Image\n2. Create QR Code\n3. Jew or Not\n4. Epstein Sort\n5. 9/11 Conspiracy\n6. Zihan and Izzy\n7. Scramble Image Pixels\n8. Convert to Morse Code\nEnter 1, 2, 3, 4, 5, 6, 7 or 8: ")
        if choice == '1':
            generate_and_save()
        elif choice == '2':
            create_qr_code()
        elif choice == '3':
            jew_or_not()
        elif choice == '4':
           arr, sorted_arr = stein_sort(arr)
           print(f"Original array: {arr}")
           print(f"Sorted array: {sorted_arr}")
        elif choice == '5':
            nine_eleven_conspiracy()
        elif choice == '6':
          zihan_and_izzy()
        elif choice == '7':
            image_path = input("Enter the path to the image file: ")
            scramble_image_pixels(image_path)
        elif choice == '8':
            morse_code()
        else:
           print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7 or 8.")