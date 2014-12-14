
import unittest
import scanner.logSetup as logSetup
import os.path
import pArch

# Unit testing driven by lolcat images
# AS GOD INTENDED!

class TestSequenceFunctions(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		logSetup.initLogging()

		super().__init__(*args, **kwargs)


	def test_pArch_1(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		archPath = os.path.join(cwd, 'testArches', 'testArches.zip')

		arch = pArch.PhashArchive(archPath)


		match = [
				('Lolcat_this_is_mah_job.jpg',
					{'dHash': -4504585791368671746,
					'hexHash': 'd9ceeb6b43c2d7d096532eabfa6cf482',
					'imX': 493,
					'pHash': 27427800275512429,
					'imY': 389}
				),

				('Lolcat_this_is_mah_job.png',

					{'dHash': -4504585791368671746,
					'hexHash': '1268e704908cc39299d73d6caafc23a0',
					'imX': 493,
					'pHash': 27427800275512429,
					'imY': 389}
				),

				('Lolcat_this_is_mah_job_small.jpg',

					{'dHash': -4504585791368671746,
					'hexHash': '40d39c436e14282dcda06e8aff367307',
					'imX': 300,
					'pHash': 27427800275512429,
					'imY': 237}
				),

				('dangerous-to-go-alone.jpg',

					{'dHash': 4576150637722077151,
					'hexHash': 'dcd6097eeac911efed3124374f44085b',
					'imX': 325,
					'pHash': -149413575039568585,
					'imY': 307}
				),

				('lolcat-crocs.jpg',

					{'dHash': 167400391896309758,
					'hexHash': '6d0a977694630ac9d1d33a7f068e10f8',
					'imX': 500,
					'pHash': -5569898607211671279,
					'imY': 363}
				),

				('lolcat-oregon-trail.jpg',

					{'dHash': -8660145558008088574,
					'hexHash': '7227289a017988b6bdcf61fd4761f6b9',
					'imX': 501,
					'pHash': -4955310669995365332,
					'imY': 356}
				)
			]


		self.assertEqual(list(arch.iterHashes()), match)


	def test_pArch_2(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		archPath = os.path.join(cwd, 'testArches', 'testArches.zip')

		arch = pArch.PhashArchive(archPath)

		ret = arch.getHashInfo('dangerous-to-go-alone.jpg')

		expect = {
			'dHash': 4576150637722077151,
			'hexHash': 'dcd6097eeac911efed3124374f44085b',
			'imX': 325,
			'pHash': -149413575039568585,
			'imY': 307
		}

		self.assertEqual(ret, expect)


	def test_pArch_3(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		archPath = os.path.join(cwd, 'testArches', 'testArches.7z')

		arch = pArch.PhashArchive(archPath)


		match = [
				(
					'Lolcat_this_is_mah_job.jpg',
					{
						'dHash': -4504585791368671746,
						'hexHash': 'd9ceeb6b43c2d7d096532eabfa6cf482',
						'imX': 493,
						'pHash': 27427800275512429,
						'imY': 389
					}
				),

				(
					'Lolcat_this_is_mah_job.png',
					{
						'dHash': -4504585791368671746,
						'hexHash': '1268e704908cc39299d73d6caafc23a0',
						'imX': 493,
						'pHash': 27427800275512429,
						'imY': 389
					}
				),

				(
					'Lolcat_this_is_mah_job_small.jpg',
					{
						'dHash': -4504585791368671746,
						'hexHash': '40d39c436e14282dcda06e8aff367307',
						'imX': 300,
						'pHash': 27427800275512429,
						'imY': 237
					}
				),

				(
					'dangerous-to-go-alone.jpg',
					{
						'dHash': 4576150637722077151,
						'hexHash': 'dcd6097eeac911efed3124374f44085b',
						'imX': 325,
						'pHash': -149413575039568585,
						'imY': 307
					}
				),

				(
					'lolcat-crocs.jpg',
					{
						'dHash': 167400391896309758,
						'hexHash': '6d0a977694630ac9d1d33a7f068e10f8',
						'imX': 500,
						'pHash': -5569898607211671279,
						'imY': 363
					}
				),

				(
					'lolcat-oregon-trail.jpg',
					{
						'dHash': -8660145558008088574,
						'hexHash': '7227289a017988b6bdcf61fd4761f6b9',
						'imX': 501,
						'pHash': -4955310669995365332,
						'imY': 356
					}
				)
			]


		self.assertEqual(list(arch.iterHashes()), match)


	def test_pArch_4(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		archPath = os.path.join(cwd, 'testArches', 'testArches.7z')

		arch = pArch.PhashArchive(archPath)

		ret = arch.getHashInfo('dangerous-to-go-alone.jpg')

		expect = {
			'dHash': 4576150637722077151,
			'hexHash': 'dcd6097eeac911efed3124374f44085b',
			'imX': 325,
			'pHash': -149413575039568585,
			'imY': 307
		}

		self.assertEqual(ret, expect)
