#!/usr/bin/env python
# coding: utf-8

# In[8]:


from PIL import Image
import numpy as np
def find_rgb(filepath, r_threshold, g_threshold, b_threshold):
    img = Image.open(filepath)
    pix = img.load()
    coordinates= []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b = pix[x,y]
            if match(r, g, b, r_threshold, g_threshold, b_threshold):
                coordinates.append((x, y))
    return(coordinates)


def match(r, g, b, r_query, g_query, b_query):
    if r >= r_query and g >= g_query and b>=b_query:
        return True
    else:
        return False


# In[ ]:


#black is 000
#dark grey 105
#light grey is 195

find_rgb('test_image.png', 105, 105, 105)


# In[53]:


#mark vein cells 
img = Image.open('TestImage2.png')
img_width = img.size[0]
img_height = img.size[1]
bin_img = np.zeros((img_width, img_height))
thresh_1 = 200
thresh_2 = 50
pix = img.load()
for x in range(img_width):
    for y in range(img_height):
        r,g,b = pix[x,y]
        if r > thresh_2 and r < thresh_1:
            bin_img[x,y] = 1

        
            
            
        
        
        
        
     


# In[73]:


#find edges

vein_coords = []
for x in range(img_width):
    for y in range(img_height):
            if bin_img[x,y] == 1:
                vein_coords.append((x,y))


# In[72]:


#vein_coords = sorted(vein_coords)
vein_start = vein_coords[0]

