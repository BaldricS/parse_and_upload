import ffmpeg

def encode_video(input: str, output: str):
    pass_one(input)
    pass_two(input, output)

def pass_one(input: str):
    ffmpeg.input(input).output('/dev/null', **ffmpeg_args(**{ 'pass': 1 }, f='null', an=None)).run()

def pass_two(input: str, output: str):
    ffmpeg.input(input).output(output, **ffmpeg_args(**{ 'c:a': 'aac', 'b:a': '320k', 'pass': 2 })).run()

def ffmpeg_args(**kwargs):
    return {
        'c:v': 'libx264',
        'preset': 'veryfast',
        'b:v': '24000k',
        **kwargs
    }