from pytube import YouTube
from openai import OpenAI

#! Only handles Youtube

video_url = 'https://www.youtube.com/watch?v=NjuQ0DhEoEM'

# Step 1: Download audio from the video url
yt = YouTube(video_url)
tube = yt.streams.filter(only_audio=True).first().download('./videos/')

# use OpenAI API to transcribe audio2text
client = OpenAI()

audio_file = open('./video/Medical Monday Water  1552017.mp4', 'rb')

transcription = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file
)

# Save transcript to a file
transcript_path = './transcripts/macka_b.txt'
with open(transcript_path, 'w') as f:
    f.write(transcription.text)

print(f"Transcript saved to {transcript_path}")
