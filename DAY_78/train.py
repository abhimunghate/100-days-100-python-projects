import os
import subprocess
import sys

YOLOV5_DIR = "yolov5"
DATASET_YAML = "dataset.yaml"

EPOCHS = 20
IMAGE_SIZE = 640
BATCH_SIZE = 4
WORKERS = 0

def main():
    train_script = os.path.join(YOLOV5_DIR, "train.py")

    if not os.path.exists(train_script):
        print("YOLOv5 repository not found.")
        print("Please clone YOLOv5 into the project folder.")
        return

    if not os.path.exists(DATASET_YAML):
        print("dataset.yaml not found.")
        return

    command = [sys.executable, train_script,

        "--img",
        str(IMAGE_SIZE),

        "--batch",
        str(BATCH_SIZE),

        "--epochs",
        str(EPOCHS),

        "--data",
        DATASET_YAML,

        "--weights",
        "yolov5s.pt",

        "--workers",
        str(WORKERS),

        "--project",
        "runs/train",

        "--name",
        "day78_custom",

        "--exist-ok"
    ]
    print("\nStarting YOLOv5 custom training...\n")

    print("Command:")
    print(" ".join(command))
    print()

    subprocess.run(command, check=False)
    print("\nTraining completed.")

    best_model = os.path.join(YOLOV5_DIR, "runs", "train", "day78_custom", "weights", "best.pt")

    if os.path.exists(best_model):
        os.makedirs("models", exist_ok=True)
        destination = os.path.join("models", "best.pt")
        
        import shutil
        shutil.copy2(best_model, destination)

        print(f"\nBest model copied to:\n{destination}")
    else:
        print("\nCould not find best.pt.")

if __name__ == "__main__":
    main()
    
# Done