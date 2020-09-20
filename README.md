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

![ q_{0} = \sum_{i=0}^{t_{1} - 1} p_{i} and  \sigma ^{2}_{0} = \sum_{i=0}^{t_{1} - 1}[i - \mu_{0}]^{2} \frac{p_{i}}{q_{0}}  for \mu_{0} = \sum_{i=0}^{t_{1} - 1} \frac{i*p_{i}}{q_{0}}](https://latex.codecogs.com/svg.latex?x%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D)

![q_{k} = $\sum_{i=t_{k}}^{t_{k+1} - 1} p_{i}$ , $\sigma ^{2}_{k} = \sum_{i=t_{k}}^{t_{k+1} - 1}[i - \mu_{k}]^{2} \frac{p_{i}}{q_{k}} $  for  $\mu_{k} = \sum_{i=t_{k}}^{t_{k+1} - 1} \frac{i*p_{i}}{q_{k}}$ ( k = 1,2, ... m-1)](https://latex.codecogs.com/svg.latex?x%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D)

![q$_{m}$ = $\sum_{i=t_{m}}^{L - 1} p_{i}$ , $\sigma ^{2}_{m} = \sum_{i=t_{m}}^{L - 1}[i - \mu_{m}]^{2} \frac{p_{i}}{q_{m}} $  for  $\mu_{m} = \sum_{i=t_{m}}^{L - 1} \frac{i*p_{i}}{q_{m}}$](https://latex.codecogs.com/svg.latex?x%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D)

q0 = Pt1−1i=0 pi and σ20 =Pt1−1i=0 [i − µ0]2 piq0 for µ0 =Pt1−1i=0i∗piq0

qk = Ptk+1−1i=tkpi, σ2k = Ptk+1−1i=tk[i − µk]2 piqk for µk = Ptk+1−1 i=tk i∗pi qk ( k = 1,2, ... m-1)
qm = PL−1 i=tm pi , σ 2 m = PL−1 i=tm [i − µm] 2 pi qm for µm = PL−1 i=tm i∗pi qm
Here, q0, q1 ... qm are class probabilities 

