import cmu_sphinx4

audio_URL = 'http://website.com/url'
transcriber = cmu_sphinx4.Transcriber(audio_URL)

for line in transcriber.transcript_stream():
	print line