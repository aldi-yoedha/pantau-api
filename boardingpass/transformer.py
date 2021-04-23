def transform(values):
	arr = []

	for item in values:
		arr.append(singleTransform(item))

	return arr

def singleTransform(values):
	try:
		return {
			'nik' 	: values.nik.nik,
			'nama' 	: values.nik.nama,
			'kode'	: values.kode_booking,
			'status': values.status,
			'wajah' : values.wajah,
			'masker': values.masker,
			'suhu'	: values.suhu,
		}
	except:
		return {
			'nik' 	: values.nik,
			'nama' 	: values.nama,
			'email'	: values.email
		}