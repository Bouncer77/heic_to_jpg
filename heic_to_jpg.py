import os
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()

def main():
    input_dir = "input_heic"
    output_dir = "output_jpg"

    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(".heic"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(
                output_dir,
                os.path.splitext(file_name)[0] + ".jpg"
            )

            try:
                image = Image.open(input_path)
                image.convert("RGB").save(output_path, "JPEG", quality=95)
                print(f"Готово: {file_name}")
            except Exception as e:
                print(f"Ошибка: {file_name} — {e}")

    print("Преобразование завершено.")

if __name__ == "__main__":
    main()
