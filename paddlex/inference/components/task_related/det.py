# copyright (c) 2024 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ....utils import logging
from ..base import BaseComponent


class DetPostProcess(BaseComponent):
    """Save Result Transform"""

    INPUT_KEYS = ["img_path", "boxes"]
    OUTPUT_KEYS = ["boxes", "labels"]
    DEAULT_INPUTS = {"boxes": "boxes"}
    DEAULT_OUTPUTS = {
        "boxes": "boxes",
        "labels": "labels",
    }

    def __init__(self, threshold=0.5, labels=None):
        super().__init__()
        self.threshold = threshold
        self.labels = labels

    def apply(self, boxes):
        """apply"""
        expect_boxes = (boxes[:, 1] > self.threshold) & (boxes[:, 0] > -1)
        boxes = boxes[expect_boxes, :]
        result = {"boxes": boxes, "labels": self.labels}

        return result
