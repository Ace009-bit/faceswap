# faceswap
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip ffmpeg libgl1 -y
pip3 install numpy opencv-python moviepy dlib face_recognition torch torchvision torchaudio tensorflow keras mediapipe imageio imageio[ffmpeg] tqdm onnxruntime rembg
git clone https://github.com/iperov/DeepFaceLab.git
cd DeepFaceLab
pip3 install -r requirements-colab.txt
cd ..
pip3 install insightface gfpgan basicsr realesrgan
python3 -c "import cv2, torch, face_recognition; print('All dependencies installed successfully!')"
python3 faceswap_tool.py
