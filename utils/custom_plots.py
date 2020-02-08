import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('dark_background')
# https://matplotlib.org/examples/color/named_colors.html
colors = {1:'deepskyblue', 2:'lightskyblue', 3:'limegreen', 4:'orangered',
          5:'red', 6:'gold', 7:'snow', 8:'black'}

fc='black'
cm='gray'
theme_col = colors[8]

fig, ax = plt.subplots(1, 1, figsize=(9.143, 5.143))

fig.patch.set_facecolor(fc)
fig.suptitle(" ")
    
    
def show_img(img, ask=True):
    plt.ion()
    plt.imshow(img, cmap=cm)
    plt.show()
    ax.spines['bottom'].set_color(theme_col)
    ax.spines['top'].set_color(theme_col)
    ax.spines['right'].set_color(theme_col)
    ax.spines['left'].set_color(theme_col)
    ax.tick_params(axis='x', colors=theme_col)
    ax.tick_params(axis='y', colors=theme_col)
    ax.yaxis.set_ticks([])
    ax.xaxis.set_ticks([])
    ax.yaxis.label.set_color(theme_col)
    ax.xaxis.label.set_color(theme_col)
    ax.title.set_color(theme_col)
    
    plt.tight_layout()
    plt.draw()
    if ask:
        accept = input('')
    else:
        accept = 'y'
        plt.pause(0.0001)
    plt.cla()
    return(accept)


def write_img(img, iframeStr, out_dir):
    plt.ion()
    plt.imshow(img, cmap=cm)
    ax.spines['bottom'].set_color(theme_col)
    ax.spines['top'].set_color(theme_col)
    ax.spines['right'].set_color(theme_col)
    ax.spines['left'].set_color(theme_col)
    ax.tick_params(axis='x', colors=theme_col)
    ax.tick_params(axis='y', colors=theme_col)
    ax.yaxis.label.set_color(theme_col)
    ax.xaxis.label.set_color(theme_col)
    plt.xticks([])
    plt.yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.title.set_color(theme_col)  
    ax.set_title(iframeStr, fontname='Hack', color='white') 
    plt.savefig(out_dir+'/'+iframeStr, bbox_inches='tight')
    plt.cla()
