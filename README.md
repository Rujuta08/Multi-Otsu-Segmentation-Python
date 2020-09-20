# Multi-Otsu-Segmentation-Python

**Image Segmentation**

Image Segmentation is a technique of dividing an image into multiple segments and thus help in the Image Analysis. Locating objects and boundaries are few of the major tasks forwhich Image Segmentation is used.
An image is composed of pixels. Image Segmentation allows us to group together the pixels with similar attributes. Image Segmentation is widely used in Medical Imaging, Traffic Control Systems, Object detection, Recognition tasks such as facial recognition, and many other applications. 

**Thresholding**

This is one of the simplest method used for Image segmentation. In this method, an Image is segmented by using its pixel values. Thresholding can be Bi-level (Image is segmented into two regions) and Multi-level ( image is segmented into several regions. In this
technique, multiple thresholds can be determined for an image, segmenting it into regions with certain brightness corresponding to different objects and one background)

**Otsu's Method**

In this method Optimum thresholds are obtained by minimizing
the within-class variance. 

In order to define the Otsu’s objective function, let’s assume a gray-scale image having L intensity levels within the range [0,1,2 ... L-1] and N be the total number of pixels in the image. Let n<sub>i</sub> be the number of times a particular gray level i occurs. The probability
distribution can be given by normalizing the gray level histogram of the image and the occurrence probability of a certain gray level is p<sub>i</sub>, where p<sub>i</sub> = n<sub>i</sub>/N. 

If the number of thresholds to be selected are m,  they can be given as (t<sub>1</sub>, t<sub>2</sub>, t<sub>3</sub> ... t<sub>m</sub>). The optimum value of these m thresholds divides the image into m+1 classes by minimizing the within-class variance (σ<sup>2</sup><sub>w</sub>) which can be given as:

F(t<sub>1</sub>, t<sub>2</sub>, t<sub>3</sub> ... t<sub>m</sub>) = q<sub>0</sub> ∗ σ<sup>2</sup><sub>0</sub> + q<sub>1</sub> ∗ σ<sup>2</sup><sub>1</sub> + ... + q<sub>m</sub> ∗ σ<sup>2</sup><sub>m</sub> = σ<sup>2</sup><sub>w</sub> 

Where,

![ q_{0} = \sum_{i=0}^{t_{1} - 1} p_{i} and  \sigma ^{2}_{0} = \sum_{i=0}^{t_{1} - 1}[i - \mu_{0}]^{2} \frac{p_{i}}{q_{0}}  for \mu_{0} = \sum_{i=0}^{t_{1} - 1} \frac{i*p_{i}}{q_{0}}](<a href="https://www.codecogs.com/eqnedit.php?latex=q_{0}&space;=&space;\sum_{i=0}^{t_{1}&space;-&space;1}&space;p_{i}&space;and&space;\sigma&space;^{2}_{0}&space;=&space;\sum_{i=0}^{t_{1}&space;-&space;1}[i&space;-&space;\mu_{0}]^{2}&space;\frac{p_{i}}{q_{0}}&space;for&space;\mu_{0}&space;=&space;\sum_{i=0}^{t_{1}&space;-&space;1}&space;\frac{i*p_{i}}{q_{0}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?q_{0}&space;=&space;\sum_{i=0}^{t_{1}&space;-&space;1}&space;p_{i}&space;and&space;\sigma&space;^{2}_{0}&space;=&space;\sum_{i=0}^{t_{1}&space;-&space;1}[i&space;-&space;\mu_{0}]^{2}&space;\frac{p_{i}}{q_{0}}&space;for&space;\mu_{0}&space;=&space;\sum_{i=0}^{t_{1}&space;-&space;1}&space;\frac{i*p_{i}}{q_{0}}" title="q_{0} = \sum_{i=0}^{t_{1} - 1} p_{i} and \sigma ^{2}_{0} = \sum_{i=0}^{t_{1} - 1}[i - \mu_{0}]^{2} \frac{p_{i}}{q_{0}} for \mu_{0} = \sum_{i=0}^{t_{1} - 1} \frac{i*p_{i}}{q_{0}}" /></a>)

![q_{k} = $\sum_{i=t_{k}}^{t_{k+1} - 1} p_{i}$ , $\sigma ^{2}_{k} = \sum_{i=t_{k}}^{t_{k+1} - 1}[i - \mu_{k}]^{2} \frac{p_{i}}{q_{k}} $  for  $\mu_{k} = \sum_{i=t_{k}}^{t_{k+1} - 1} \frac{i*p_{i}}{q_{k}}$ ( k = 1,2, ... m-1)](<a href="https://www.codecogs.com/eqnedit.php?latex=q_{k}&space;=&space;\sum_{i=t_{k}}^{t_{k&plus;1}&space;-&space;1}&space;p_{i}&space;,&space;\sigma&space;^{2}_{k}&space;=&space;\sum_{i=t_{k}}^{t_{k&plus;1}&space;-&space;1}[i&space;-&space;\mu_{k}]^{2}&space;\frac{p_{i}}{q_{k}}&space;for&space;\mu_{k}&space;=&space;\sum_{i=t_{k}}^{t_{k&plus;1}&space;-&space;1}&space;\frac{i*p_{i}}{q_{k}}&space;(&space;k&space;=&space;1,2,&space;...&space;m-1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?q_{k}&space;=&space;\sum_{i=t_{k}}^{t_{k&plus;1}&space;-&space;1}&space;p_{i}&space;,&space;\sigma&space;^{2}_{k}&space;=&space;\sum_{i=t_{k}}^{t_{k&plus;1}&space;-&space;1}[i&space;-&space;\mu_{k}]^{2}&space;\frac{p_{i}}{q_{k}}&space;for&space;\mu_{k}&space;=&space;\sum_{i=t_{k}}^{t_{k&plus;1}&space;-&space;1}&space;\frac{i*p_{i}}{q_{k}}&space;(&space;k&space;=&space;1,2,&space;...&space;m-1)" title="q_{k} = \sum_{i=t_{k}}^{t_{k+1} - 1} p_{i} , \sigma ^{2}_{k} = \sum_{i=t_{k}}^{t_{k+1} - 1}[i - \mu_{k}]^{2} \frac{p_{i}}{q_{k}} for \mu_{k} = \sum_{i=t_{k}}^{t_{k+1} - 1} \frac{i*p_{i}}{q_{k}} ( k = 1,2, ... m-1)" /></a>)

(<a href="https://www.codecogs.com/eqnedit.php?latex=q_{m}&space;=&space;\sum_{i=t_{m}}^{L&space;-&space;1}&space;p_{i}&space;,&space;\sigma&space;^{2}_{m}&space;=&space;\sum_{i=t_{m}}^{L&space;-&space;1}[i&space;-&space;\mu_{m}]^{2}&space;\frac{p_{i}}{q_{m}}&space;for&space;\mu_{m}&space;=&space;\sum_{i=t_{m}}^{L&space;-&space;1}&space;\frac{i*p_{i}}{q_{m}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?q_{m}&space;=&space;\sum_{i=t_{m}}^{L&space;-&space;1}&space;p_{i}&space;,&space;\sigma&space;^{2}_{m}&space;=&space;\sum_{i=t_{m}}^{L&space;-&space;1}[i&space;-&space;\mu_{m}]^{2}&space;\frac{p_{i}}{q_{m}}&space;for&space;\mu_{m}&space;=&space;\sum_{i=t_{m}}^{L&space;-&space;1}&space;\frac{i*p_{i}}{q_{m}}" title="q_{m} = \sum_{i=t_{m}}^{L - 1} p_{i} , \sigma ^{2}_{m} = \sum_{i=t_{m}}^{L - 1}[i - \mu_{m}]^{2} \frac{p_{i}}{q_{m}} for \mu_{m} = \sum_{i=t_{m}}^{L - 1} \frac{i*p_{i}}{q_{m}}" /></a>)


Here, q0, q1 ... qm are class probabilities 

