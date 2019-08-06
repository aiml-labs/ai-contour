class DataGenerator(tf.keras.utils.Sequence):
	"""
	DataGenerator instance for dicom images that can be used as a parameter for model.fit_generator() function.
	Note: Sample DataGenerator in: https://colab.research.google.com/drive/1a-5HoDFhg2EK5si7SkcmKyDtL-kWrcgD
	"""
	def __init__(self, file_path_list, labels, batch_size=32, #batch_size=32
                 img_size=256, channels=1, shuffle=True):
		"""
		Initializes DataGenerator Object.
		Parameters:
			file_path_list:
			labels:
			batach_size:
			img_size:
			channels:
			shuffle:
		"""
		#Note: Please update the signature as appropriate
		self.file_path_list = file_path_list
        self.labels = labels
        self.batch_size = batch_size
        self.img_size = img_size
        self.channels = channels
        self.shuffle = shuffle
        self.on_epoch_end()

    def __len__(self):
        """denotes the number of batches per epoch"""
        return int(np.floor(len(self.file_path_list)) / self.batch_size)

    def __getitem__(self, index):
        """generate one batch of data"""
        pass

    def on_epoch_end(self):
        """update ended after each epoch"""
        pass

    def __data_generation(self, file_path_list_temp):
        """generate data containing batch_size samples"""
        pass
        
