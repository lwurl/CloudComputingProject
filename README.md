# Cloud Computing Project
Final Project for Cloud Computing. This is a simple implementation of AlphaZero. It uses WorkQueue and HTCondor to parallelize the process of the neural net playing games vs itself.


## Running with WorkQueue
To run:
- Make sure you are runnning this on `crcfe02.crc.nd.edu`
- Make sure that the most up to date cctools has been installed on your machine. If not, run:
```
cd $HOME
wget http://ccl.cse.nd.edu/software/files/cctools-7.0.4-source.tar.gz
tar xvzf cctools-7.0.4-source.tar.gz
cd cctools-7.0.4-source
./configure --prefix $HOME/cctools --tcp-low-port 9000
make
make install
cd $HOME
```
- Make sure that you have pip installed
- Run `export PATH=/afs/crc.nd.edu/user/$USERNAME[0]$/$USERNAME$/.local/bin:$PATH`
- Use `python -m pip install ___ --user` to install the necessary libraries: `numpy`, `keras`, `keras_applications`, `keras_preprocessing`, `pyyaml`, `h5py`, and `tensorflow`
- Run the commands found in the file `Path.txt` from the repository in the terminal
- Use the command `condor_submit_workers crcfe02.crc.nd.edu PORT NUM_WORKERS` to submit `NUM_WORKERS` workers to HTCondor
- Ensure that the `PORT` matches the port number specified in `params.py`
- Ensure that the paths specified in `condor_workers.py` are where the different libraries and files are located on your machine
- Set parameters in `params.py`
- Run `./main.py condor`

## Running on a single machine
- Set parameters in `params.py`
- Run `python main.py` 

## Results
The newly trained model will be stored in the models folder. The best model is saved there after every iteration is complete so if the program needs to be terminated in the middle of the execution, the model can be saved.

## Play against a model
- Run `python playGame.py PATH_TO_MODEL_H5`
- Enter the integer value of a square to make a move. The board is setup like this:

	```
	 0  1  2  3  4  5  6
	 7  8  9 10 11 12 13
	14 15 16 17 18 19 20
	21 22 23 24 25 26 27
	28 29 30 31 32 33 34
	35 36 37 38 39 40 41
	```

## Play models head to head
- Run `python playGameNNVsNN.py.py PATH_TO_MODEL1_H5 PATH_TO_MODEL2_H5`
- It will play 100 games, alternating which model goes first

## References
This project was based off of these two tutorials for AlphaZero:
- https://medium.com/applied-data-science/how-to-build-your-own-alphazero-ai-using-python-and-keras-7f664945c188
- https://web.stanford.edu/~surag/posts/alphazero.html

Also, here is a link to more information about AlphaZero from Deepmind's website
- https://deepmind.com/blog/alphazero-shedding-new-light-grand-games-chess-shogi-and-go/