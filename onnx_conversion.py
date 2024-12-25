import onnx
import torch
import torch.nn as nn
from torchvision.models import resnet34

model= resnet34()
in_features= 512
classes= 200

model.fc= nn.Sequential(nn.Linear(in_features, classes))

model.load_state_dict(torch.load('./checkpoints/model_200.pth'))
model= model.to('cuda')

# dummy input in the format how pytorch model was trained
dummy_input = torch.randn(1, 3, 224, 224, device="cuda")

# convert model from pytorch to onnx
torch.onnx.export(model,
                  dummy_input,
                  './checkpoints/model_200_onnx.onnx',
                  export_params=True,
                  opset_version=10,
                  verbose=True,                   
                  do_constant_folding=False,)
