Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
face_hogs = []
face_features = []
for i in range(15):
    hog_desc, hog_image = hog(face_images[i], orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
    face_hogs.append(hog_image)
     face_features.append(hog_desc)
     
SyntaxError: unexpected indent
face_hogs = []
face_features = []
for i in range(15):
    hog_desc, hog_image = hog(face_images[i], orientations=8, pixels_per_cell=(1
                                                                               6, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
face_hogs = []
face_features = []

for i in range(15):
    hog_desc, hog_image = hog(face_images[i], orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
    face_hogs.append(hog_image)
    face_features.append(hog_desc)

plot_images(3, 5, face_hogs)

print(face_features[0].shape)

fig = plt.figure()
fig, ax = plt.subplots(3,5, figsize = (10,6))
for i in range(3):
    for j in range(5):
        ax[i, j].imshow(resize(face_features[i*5+j], (128,16)))
        
SyntaxError: multiple statements found while compiling a single statement
face_hogs = []
face_features = []
for i in range(15):
    hog_desc, hog_image = hog(face_images[i], orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
    face_hogs.append(hog_image)
    face_features.append(hog_desc)
    plot_images(3, 5, face_hogs)
    print(face_features[0].shape)
    fig = plt.figure()
fig, ax = plt.subplots(3,5, figsize = (10,6))
for i in range(3):
    
SyntaxError: invalid syntax
face_hogs = []
face_features = []
for i in range(15):
    hog_desc, hog_image = hog(face_images[i], orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
    face_hogs.append(hog_image)
    face_features.append(hog_desc)
    plot_images(3, 5, face_hogs)
    print(face_features[0].shape)
    fig = plt.figure()
    fig, ax = plt.subplots(3,5, figsize = (10,6))
    for i in range(3):
        for j in range(5):
            ax[i, j].imshow(resize(face_features[i*5+j], (128,16)))

            
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    hog_desc, hog_image = hog(face_images[i], orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
NameError: name 'hog' is not defined
url = 'https://github.com/dknife/ML/raw/main/data/Proj2/animals/'
animal_images = []
for i in range(15):
    file = url + 'img{0:02d}.jpg'.format(i+1)
    img = imread(file)
    img = resize(img, (64,64))
    animal_images.append(img)
    plot_images(3, 5, animal_images)

    
Traceback (most recent call last):
  File "<pyshell#44>", line 3, in <module>
    img = imread(file)
NameError: name 'imread' is not defined
NameError: name 'imread' is not defined
SyntaxError: invalid syntax

animal_hogs = []
animal_features = []
for i in range(15):
    
SyntaxError: multiple statements found while compiling a single statement
animal_hogs = []
animal_features = []
SyntaxError: multiple statements found while compiling a single statement
animal_hogs = []
animal_features = []
for i in range(15):
    hog_desc, hog_image = hog(animal_images[i], orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
    animal_hogs.append(hog_image)
    animal_features.append(hog_desc)
    plot_images(3, 5, animal_hogs)
 fig = plt.figure()
 
SyntaxError: unindent does not match any outer indentation level
fig = plt.figure()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    fig = plt.figure()
NameError: name 'plt' is not defined
fig, ax = plt.subplots(3,5, figsize = (10,6))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    fig, ax = plt.subplots(3,5, figsize = (10,6))
NameError: name 'plt' is not defined
animal_hogs = []
animal_features = []
for i in range(15):
    hog_desc, hog_image = hog(animal_images[i], orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
    animal_hogs.append(hog_image)
    animal_features.append(hog_desc)
    plot_images(3, 5, animal_hogs)
    
SyntaxError: multiple statements found while compiling a single statement




KeyboardInterrupt
X, y = [], []
for feature in face_features:
    X.append(feature)
    y.append(1)
    for feature in animal_features:
        X.append(feature)
        y.append(0)
        fig = plt.figure()
        fig, ax =
        
SyntaxError: invalid syntax
for i in range(6):
  for j in range(5):
      ax[i, j].imshow(resize(X[i*5+j], (128,16)),interpolation='nearest')
      print(y)

      
Traceback (most recent call last):
  File "<pyshell#78>", line 3, in <module>
    ax[i, j].imshow(resize(X[i*5+j], (128,16)),interpolation='nearest')
NameError: name 'ax' is not defined. Did you mean: 'max'?

>>> 
>>> from sklearn.svm import SVC
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    from sklearn.svm import SVC
ModuleNotFoundError: No module named 'sklearn'
>>> ModuleNotFoundError: No module named 'sklearn'
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> from sklearn.svm import SVC
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    from sklearn.svm import SVC
ModuleNotFoundError: No module named 'sklearn'
>>> ModuleNotFoundError: No module named 'sklearn'
SyntaxError: invalid syntax
>>> test_hogs = []
>>> test_features = []
>>> for i in range(10):
...     hog_desc, hog_image = hog(test_images[i], orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
...     test_hogs.append(hog_image)
...     test_features.append(hog_desc)
...     plot_images(2, 5, test_hogs)
...     fig = plt.figure()
...     fig, ax = plt.subplots(2,5, figsize = (10,4))
...     for i in range(2):
...        for j in range(5):
...            ax[i, j].imshow(resize(test_features[i*5+j], (128,16)), interpolation='nearest')
... 
...            
Traceback (most recent call last):
  File "<pyshell#100>", line 2, in <module>
    hog_desc, hog_image = hog(test_images[i], orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, multichannel=True)
NameError: name 'hog' is not defined
