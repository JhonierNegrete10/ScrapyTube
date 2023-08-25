from typing import List
from matplotlib import pyplot as plt
import numpy as np


def plot_confusion_matrix(cm, 
                          labels: List, 
                          title='Confusion matrix',
                          cmap=plt.cm.Blues
                          ):
    
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(labels))
    target_names = labels
    plt.xticks(tick_marks, target_names, rotation=45)
    plt.yticks(tick_marks, target_names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')