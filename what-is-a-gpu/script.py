# -*- coding: utf-8 -*-
"""
# What is a GPU? Are GPUs Needed for Deep Learning?

* Tutorial: https://news.towardsai.net/gpu
* Github: https://github.com/towardsai/tutorials/tree/master/what-is-a-gpu

**<h2>GPU Usage on Your Local Computer / Google Colab</h2>**

In this notebook you will connect to a GPU, and then run some basic TensorFlow operations on both the CPU and a GPU, observing the speedup provided by using the GPU.

#### Enabling and testing the GPU

First, you'll need to enable GPUs for the notebook:

1.  Navigate to Edit→Notebook Settings
2.  Select GPU from the Hardware Accelerator drop-down

### Installing TensorFlow GPU

As a first step, we need to install *tensorflow-gpu*.

If you are going to install it on your computer, you should follow these steps.

As a result of this code, you will have the latest version tensorflow gpu.
"""

pip install tensorflow-gpu

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

"""If the TensorFlow version you want to use is specific, install it by entering the version name."""

pip install tensorflow-gpu==1.15.0

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

"""Configuration Specific GPU on TensorFlow"""

import tensorflow as tf
try:
    tf.device('/job:localhost/replica:0/task:0/device:GPU:1')
except RuntimeError as e:
  print(e)

"""### Checking installed TensorFlow GPU version"""

pip show tensorflow-gpu

"""As you can see, the latest version of TensorFlow has been installed. If you want to use a specific version distribution, it is necessary to install with the version name.

If you are also getting warnings as above, it is because of:
- Other libraries that came with the last version of tensorflow-gpu that we installed before are not uninstall, so they have version conflicts with the newly installed version. Decide on the version you want to use and use only that version distribution.

To check the new TensorFlow version installed, work again with the command.
```
pip show packagename
```

### Listing Eligible CPU and GPU Devices

Next, we are at the step of showing all possible devices that can be used.
"""

from tensorflow.python.client import device_lib
device_lib.list_local_devices()

"""4 devices are shown in the list here. 2 of them are a concept excluding CPU and GPU.

As mentioned in the docs, XLA stands for "accelerated linear algebra". It's Tensorflow's relatively new optimizing compiler that can further speed up your ML models' GPU operations by combining what used to be multiple CUDA kernels into one (simplifying because this isn't that important for your question).

In the next step, the default device name used will be listed.
"""

import tensorflow as tf
tf.test.gpu_device_name()

"""### Speed Comparison in Model Tutorials for GPU and CPU"""

import tensorflow as tf
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images / 255.0
test_images=test_images / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=5)

test_loss = model.evaluate(test_images, test_labels)

"""As you can see, ETA times are very short. One minute to train almost this amount of data! Now, by following the steps below, let's choose the hardware CPU for the runtime and see how we will experience a difference in speed.


---

You'll need to enable CPUs for the notebook:


1.  Navigate to Edit→Notebook Settings
2.  Select None from the Hardware Accelerator drop-down
"""

import tensorflow as tf
tf.test.gpu_device_name()

"""And now when we test whether it is using GPU or not, we see that the value of None comes out. After making sure we are using a CPU, we can provide the training for this as well."""

import tensorflow as tf
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images / 255.0
test_images=test_images / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=5)

test_loss = model.evaluate(test_images, test_labels)

"""Here, as the number of data increases and the problem becomes more intense, the difference between training will become much wider.

Since there is not a very large data set in this example line of code, there are no big differences between CPU and GPU when processing data. However, there will be a significant difference when processing big data.


---

# A sample GPU setup on the local computer

If you want to learn the features of your graphics card, you can learn the features of your graphics card by typing **dxdiag**. Or instead, you can run the command below on your **computer's terminal**.

### Controlling graphic card name
"""

wmic path win32_VideoController get name

"""Since I do not want to work in the base area of the machine, I create a virtual environment and I do this with Conda. You can also use Mini Conda if you wish.

### Creating virtual environment
"""

conda create -n virtualenv python=3.6
conda activate virtualenv

"""### TensorFlow GPU Installation

To use GPU with TensorFlow, it is necessary to install the tensorflow-gpu library. If loading with conda, the appropriate CUDA and cuDNN versions will also be displayed during the process.
"""

conda install tensorflow-gpu==1.15.0
#pip install tensorflow-gpu==1.15.0

"""After all these stages, TensorFlow GPU must be installed. If you wish, you can control the terminal with the following commands."""

import tensorflow as tf
sess=tf.Session(config=tf.ConfigProto(log_device_placement=True))

"""### Keras Installation"""

pip install keras==2.2.5
