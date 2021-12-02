import os

import requests
import img2pdf

def get_data():
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }

    img_list = []
    for i in range(1, 49):
        url = f"https://recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            img_list.append(f"media/{i}.jpg")
            print(f"Downloaded {i} of 48")

        print("#" * 20)
        print(img_list)


    # create PDF file
    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF file created successfully!")


def write_to_pdf():
    os.listdir("media")
    img_list = [f"media/{i}.jpg" for i in range(1, 49)]

    # create PDF file
    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF file created successfully!")

def main():
    # get_data() # создает и записывает изображения в pdf
    write_to_pdf() # записывает уже созданые изображения в pdf

if __name__ == '__main__':
    main()