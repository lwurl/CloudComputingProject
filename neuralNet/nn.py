from keras.models import Model
from keras.layers import *

class NN(object):
	'''
		The architecture of the model is based off of the model used in this link:
		https://github.com/AppliedDataSciencePartners/DeepReinforcementLearning/blob/master/model.py
	'''
	def __init__(self, input_shape):
		self.input_shape = input_shape
		self.model = self.create_model()

	def create_model(self):
		'''
			This method should create the deep neural net
			It should take the game state as the input,
			then stack several residual/convulutional layers
			on top of each and then split off into the policy_head and the
			value_head
		'''
		## Main input Shape to the model
		inputs = Input(shape=self.input_shape, dtype='int32', name='main_input')

		## Base of the model before split
		x = LeakyReLU()(inputs)
		x = Dense(64, activation='relu')(x)
		x = Dense(64, activation='relu')(x)
		x = Dense(64, activation='relu')(x)

		## Next, generate the value_head and the policy_head
		p = Dense(64, activation='relu')(x)
		p = Dense(64, activation='relu')(p)
		p = Dense(64, activation='relu')(p)
		policy_head = Dense(42, activation='softmax')(p)

		v = Dense(64, activation='relu')(x)
		v = Dense(64, activation='relu')(v)
		v = Dense(64, activation='relu')(v)
		value_head = Dense(1, activation='softmax')(v)

		## Creat the model and compile it
		model = Model(inputs=inputs, outputs=[policy_head, value_head])
		model.compile(optimizer='rmsprop', loss=['categorical_crossentropy', 'binary_crossentropy'], metrics=['accuracy'])

		return model


	def fit(self, data, labels, epochs, batch_size):
		self.model.fit(data, labels, epochs=epochs, batch_size=batch_size)

	def evaluate(self, x, y, batch_size):
		return self.model.evaluate(x, y, batch_size=batch_size)

	def policy_head(self):
		'''
			This head will create a probability vector of all of the
			moves
		'''
		## Questions to answer
		#	1.) If there are a fixed number of outputs, what happens to invalid moves
		#			-> I am guessing they just go to 0

		pass

	def value_head(self):
		'''
			This head will have 1 output node of how favorable the board is for the user
			between -1 and 1
		'''
		pass


		