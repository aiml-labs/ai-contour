class DicomDataSet:
	"""
	DicomDataSet class provides utilities for handing Dicom files. 
	It assumes the DicomFiles are stored in following directory structure.
	./data/
		./Patient1/
			./file1.dcm
			./file2.dcm
			./file3.dcm
			./rs-file.dcm <-- RT structure file with contour details.
		./Patient2/
			...
		./PatientN/
	"""
	def __init__(self, srcPath):
		"""
		Initializes object.
		Parameters:
			srcPath (string): Path where dicom files are store in above mentioned directory structure
		"""
		pass

	def prepare(self):
		"""
		Scans through files in srcPath and populates file details in internal data structures
		"""
		pass

	def getInfo(self):
		"""
		Returns details about the dataset in pandas dataFrame format.
		DataFrame Columns:
			PatientID:
			PatientName:
			Age:
			...
			DicomFiles: <list of dicom files>
			ContourFile: <RT structure file containing contour details
		"""
		pass

	def getROINames(self):
		"""Returns a list of ROIs(Region of Interests) available across all dicom files."""
		pass

	def getDataGenerator(self, roiName):
		"""
		Returns ai-countour.data.DataGenerator object which can be passed to model.fit_generator() function.
		Parameter:
			rioName(string): RIO name for which data generator object needs to be created.
		"""
		pass
