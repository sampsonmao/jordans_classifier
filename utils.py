import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def show_random_set_of_shoes(paths_list, num_imgs_to_show, col_wrap=3):
    ncol = col_wrap
    nrow = int(np.ceil(num_imgs_to_show / col_wrap))
    sample_img_paths = random.sample(paths_list, num_imgs_to_show)
    fig, axs = plt.subplots(nrow, ncol)

    for ax, path_to_img in zip(axs.flatten(), sample_img_paths):
        im = Image.open(path_to_img)
        ax.imshow(im)
        shoe_series_num = path_to_img.split("\\")[-2]
        ax.set_title(f"AJ {shoe_series_num}")
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    for ax in axs.flat[num_imgs_to_show:]:
        ax.remove()
    fig.tight_layout()
    
def show_shoe_series(paths_dict, shoe_series_num, num_imgs_to_show, col_wrap=3):
    ncol = col_wrap
    nrow = int(np.ceil(num_imgs_to_show / col_wrap))
    fig, axs = plt.subplots(nrow, ncol)

    shoe_series_paths_list = random.sample(
        paths_dict[str(shoe_series_num)], num_imgs_to_show
    )

    for ax, path_to_img in zip(axs.flatten(), shoe_series_paths_list):
        im = Image.open(path_to_img)
        ax.imshow(im)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    for ax in axs.flat[num_imgs_to_show:]:
        ax.remove()

    fig.suptitle(f"Air Jordan {shoe_series_num}")
    fig.tight_layout()