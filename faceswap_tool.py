import os
import subprocess

def banner():
    print("""
    █████▒█      ██  ▄████▄   ▒█████   ██████
    ▓██   ▒ ██  ▓██▒▒██▀ ▀█  ▒██▒  ██▒██    ▒
    ▒████ ░▓██  ▒██░▒▓█    ▄ ▒██░  ██░ ▓██▄
    ░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██ ▒██   ██░ ▒   ██
    ░▒█░   ▒▒█████▓ ▒ ▓███▀  ░ ████▓▒▒██████
     ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒   ░ ▒░▒░▒░ ░ ▒░ ░
     ░     ░░▒░ ░ ░   ░  ▒     ░ ▒ ▒░ ░ ░  ░
     ░ ░    ░░░ ░ ░ ░        ░ ░ ░ ▒    ░
              ░     ░ ░          ░ ░    ░  ░
    """)

def main_menu():
    while True:
        os.system("clear")  # Clears the terminal
        banner()
        print("[1] Swap Face in Image")
        print("[2] Swap Face in Video")
        print("[3] Enhance Image")
        print("[4] Enhance Video")
        print("[5] Generate Deepfake Video")
        print("[6] Apply Filters to Image")
        print("[7] Convert Image to Cartoon")
        print("[8] Face Detection in Image")
        print("[9] Face Detection in Video")
        print("[10] Blur Faces in Image")
        print("[11] Blur Faces in Video")
        print("[12] Background Removal in Image")
        print("[13] Background Removal in Video")
        print("[14] Exit")
        choice = input("\nEnter your choice: ")
        
        options = {
            '1': face_swap_image,
            '2': face_swap_video,
            '3': enhance_image,
            '4': enhance_video,
            '5': generate_deepfake,
            '6': apply_filters,
            '7': convert_to_cartoon,
            '8': detect_face_image,
            '9': detect_face_video,
            '10': blur_faces_image,
            '11': blur_faces_video,
            '12': remove_background_image,
            '13': remove_background_video,
            '14': exit_tool
        }
        
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again!")
            input("Press Enter to continue...")

def execute_command(command):
    try:
        subprocess.run(command, check=True)
        print("Operation Completed Successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    input("Press Enter to continue...")

def face_swap_image():
    img = input("Enter target image path: ")
    face = input("Enter source face image path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "faceswap.py", "--src", face, "--dst", img, "--output", output])

def face_swap_video():
    video = input("Enter target video path: ")
    face = input("Enter source face image path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "faceswap.py", "--src", face, "--dst", video, "--output", output, "--video"])

def enhance_image():
    img = input("Enter image path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "enhance.py", "--input", img, "--output", output])

def enhance_video():
    video = input("Enter video path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "enhance.py", "--input", video, "--output", output, "--video"])

def generate_deepfake():
    src_video = input("Enter source video path: ")
    target_video = input("Enter target video path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "deepfake.py", "--src", src_video, "--dst", target_video, "--output", output])

def apply_filters():
    img = input("Enter image path: ")
    filter_type = input("Enter filter type (grayscale, sepia, etc.): ")
    output = input("Enter output filename: ")
    execute_command(["python3", "filter.py", "--input", img, "--filter", filter_type, "--output", output])

def convert_to_cartoon():
    img = input("Enter image path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "cartoon.py", "--input", img, "--output", output])

def blur_faces_image():
    img = input("Enter image path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "blur_faces.py", "--input", img, "--output", output])

def blur_faces_video():
    video = input("Enter video path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "blur_faces.py", "--input", video, "--output", output, "--video"])

def remove_background_image():
    img = input("Enter image path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "remove_bg.py", "--input", img, "--output", output])

def remove_background_video():
    video = input("Enter video path: ")
    output = input("Enter output filename: ")
    execute_command(["python3", "remove_bg.py", "--input", video, "--output", output, "--video"])

def exit_tool():
    print("Exiting... Goodbye!")
    exit()

if __name__ == "__main__":
    main_menu()
