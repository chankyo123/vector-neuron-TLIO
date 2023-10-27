from network.model_resnet import BasicBlock1D, ResNet1D

# from network.model_vn_resnet_2 import VN_BasicBlock1D, VN_ResNet1D
# from network.model_vn_resnet_3reslay import VN_BasicBlock1D, VN_ResNet1D
from network.model_vn_resnet_23reslay import VN_BasicBlock1D, VN_ResNet1D
# from network.model_vn_resnet_fc1lay import VN_BasicBlock1D, VN_ResNet1D
# from network.model_vn_resnet_fc2lay import VN_BasicBlock1D, VN_ResNet1D

# from network.model_vn_resnet_original import VN_BasicBlock1D_original, VN_ResNet1D_original

from network.model_resnet_seq import ResNetSeq1D
from network.model_tcn import TlioTcn

from utils.logging import logging

def get_model(arch, net_config, input_dim=6, output_dim=3):
    if arch == "resnet":
        network = ResNet1D(
            BasicBlock1D, input_dim, output_dim, [2, 2, 2, 2], net_config["in_dim"]
        )
    elif arch == "vn_resnet":
        network = VN_ResNet1D(
            VN_BasicBlock1D, input_dim, output_dim, [2, 2, 2, 2], net_config["in_dim"]
        )
        # network = VN_ResNet1D_original(
        #     VN_BasicBlock1D_original, input_dim, output_dim, [2, 2, 2, 2], net_config["in_dim"]
        # )
    elif arch == "resnet_seq":
        network = ResNetSeq1D(
            BasicBlock1D, input_dim, output_dim, [2, 2, 2, 2], net_config["in_dim"]
        )
    elif arch == "tcn":
        network = TlioTcn(
            input_dim,
            output_dim,
            [64, 64, 64, 64, 128, 128, 128],
            kernel_size=2,
            dropout=0.2,
            activation="GELU",
        )
    else:
        raise ValueError("Invalid architecture: ", arch)

    num_params = 0
    for p in network.parameters():
        num_params += p.numel()
    logging.info(f"Number of params for {arch} model is {num_params}")   

    return network
