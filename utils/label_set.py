import torch
import torch.nn as nn
from config import *
from utils.stft_istft import STFT


class LabelHelper(nn.Module):

    def __init__(self):
        super(LabelHelper, self).__init__()
        self.stft = STFT(FILTER_LENGTH, HOP_LENGTH)

    def forward(self, speech_spec, noise_spec):
        # return self.cal_IRM(speech_spec, noise_spec)
        return self.cal_speech_mag(speech_spec)

    def cal_IRM(self, speech_spec, noise_spec):
        noise_real = noise_spec[:, :, :, 0]
        noise_imag = noise_spec[:, :, :, 1]
        speech_real = speech_spec[:, :, :, 0]
        speech_imag = speech_spec[:, :, :, 1]
        return torch.pow((speech_real.pow(2) + speech_imag.pow(2))/(speech_real.pow(2) + speech_imag.pow(2) + noise_real.pow(2) + noise_imag.pow(2) + EPSILON), 0.5).clamp(0, 1)

    def cal_speech_mag(self, speech_spec):
        speech_real = speech_spec[:, :, :, 0]
        speech_imag = speech_spec[:, :, :, 1]
        return torch.sqrt(speech_real ** 2 + speech_imag ** 2)
