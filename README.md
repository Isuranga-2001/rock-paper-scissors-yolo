# Rock-Paper-Scissors YOLO

This project uses YOLOv8 to train a model for detecting rock, paper, and scissors hand gestures. The dataset is located in `datasets/rock-paper-scissors`.

## Training the Model

To train the model, run:

```bash
yolo detect train data=datasets/rock-paper-scissors/data.yaml model=yolov8n.pt epochs=20 imgsz=640
```

- `data`: Path to the dataset configuration file.
- `model`: Pretrained YOLOv8 model.
- `epochs`: Number of training epochs (default: 20).
- `imgsz`: Image size (default: 640).

## Optimization

For better results, experiment with different values for `imgsz` and `epochs`. For example:

```bash
yolo detect train data=datasets/rock-paper-scissors/data.yaml model=yolov8n.pt epochs=50 imgsz=800
```

- Increasing `epochs` may improve accuracy but takes longer.
- Adjusting `imgsz` can affect detection performance and speed.

## Results

Training outputs (weights, metrics, images) are saved in the `runs/detect` directory.
