import os
from django.core.exceptions import ValidationError
from moviepy import VideoFileClip

ALLOWED_VIDEO_EXTENSIONS = ['.mp4']

def validate_video_extension(value):
    ext = os.path.splitext(value.name)[1]

    if ext.lower() not in ALLOWED_VIDEO_EXTENSIONS:
        raise ValidationError(
            'Only MP4 videos are allowed.'
        )
    
def validate_video_size(value):
    filesize = value.size

    max_size = 50 * 1024 * 1024

    if filesize > max_size:
        raise ValidationError(
            'Video file too large. Max size is 50MB.'
        )
    
def validate_video_duration(value):
    try:
        video = VideoFileClip(value.temporary_file_path())
    except Exception as e:
        raise ValidationError(
            'Error occurred while processing the video file.'
        )

    duration = video.duration

    max_duration = 300  # 5 minutes

    if duration > max_duration:
        raise ValidationError(
            'Video exceeds maximum duration of 5 minutes.'
        )