# frontier

Te goal of this repository is to apply knowledge of engineering fundamentals to the financial world. This team aims to provide a lean, modular codebase that is both simple to use and highly effective in retrieving data, extracting appropriate data, and applying significant metrics to neural net models using TensorFlow. The API will be able to handle data extraction, manipulation and equities trading.

## Setting up environment

Below is a list of instructions to get the codebase functional on your machine.

1. Make sure you have Python 3.6 installed and added to PATH. Python 3.7 support will be added later.

1. Copy the repository to a local area via `git clone https://github.com/rschweiz1/frontier.git`.

2. Use `pip install --upgrade -r requirements.txt` to install latest dependencies in requirements file.

3. Download [CUDA v10.0 library](https://developer.nvidia.com/cuda-downloads) *(Note: CUDA v10.0 currently only works with tf-nightly-gpu)*.

4. If you do not have an NVIDIA developer account you will need to make one to download [CUDNN for CUDA 10.0](https://developer.nvidia.com/rdp/cudnn-download). Copy the 3 CUDNN files (bin, include, lib) into their respective CUDA paths. For a default installation, the three folders are located in C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0.

5. You should now be able to compile machine learning models on your NVIDIA GPU. Run main.py in python to test the installation.
